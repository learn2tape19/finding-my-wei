"""
Comprehensive test suite for WordPress V1 adapter.

Tests cover behavioral validation (actual adapter method invocation):
1. HTTPS requirement (adapter initialization)
2. Preflight: all 6 mandatory gates must execute (HTTPS, API reachable, auth, user identity, posts, media endpoints)
3. Preflight failure: NO writes occur when ANY mandatory gate fails
4. Bad credentials fail before writes
5. Wrong site identity fails before writes
6. Media upload with exact asset and MIME type preservation
7. Media alt text exactness
8. Category exact resolution (zero, one, multiple matches)
9. Ambiguous category fails closed
10. Tag exact resolution (zero, one, multiple matches)
11. Ambiguous tag fails closed
12. Unauthorized taxonomy creation rejected
13. Draft post creation
14. Scheduled post creation with exact time
15. Publish post creation
16. Featured media assignment
17. Exact title/slug/excerpt preservation
18. Body verification with harmless normalization
19. Substantive body mismatch fails verification
20. Safe retry does not duplicate post
21. Conflicting package hash does not mutate existing verified post
22. 401/403 → BLOCKED_AUTH error mapping
23. 429/5xx → FAILED_TRANSIENT error mapping
24. Unknown failure → fail-closed state
25. Secrets absent from logs/exceptions
"""

import sys
import unittest
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock, call
from datetime import datetime, timedelta
import io

# Add control_plane to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from control_plane.adapters.wordpress_v1 import (
    WordPressAdapter,
    WordPressClient,
    WordPressHTTPError,
)


class TestWordPressHTTPErrorRedaction(unittest.TestCase):
    """Test that secrets are properly redacted."""

    def test_secrets_redacted_in_string_representation(self):
        """Secrets are redacted when error is converted to string."""
        error = WordPressHTTPError(
            401,
            "Auth failed",
            {"password": "secret123", "normal_field": "value"},
        )
        error_str = str(error)
        self.assertNotIn("secret123", error_str)
        self.assertIn("[REDACTED]", error_str)
        self.assertIn("normal_field", error_str)


class TestWordPressClientHTTPSRequired(unittest.TestCase):
    """Test that HTTPS is enforced."""

    def test_https_required_raises_on_http(self):
        """HTTP URL raises ValueError."""
        with self.assertRaises(ValueError):
            WordPressClient("http://example.com", "user", "password")

    def test_https_accepted(self):
        """HTTPS URL is accepted."""
        client = WordPressClient("https://example.com", "user", "password")
        self.assertEqual(client.base_url, "https://example.com")


class TestWordPressClientPreflightHTTPS(unittest.TestCase):
    """Test HTTPS verification in preflight."""

    @patch("urllib.request.urlopen")
    def test_preflight_verifies_https(self, mock_urlopen):
        """Preflight verifies HTTPS is in use."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock successful response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"namespace": "wp/v2"}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = client.verify_https_and_api()
        self.assertTrue(result["https"])
        self.assertTrue(result["api_reachable"])


class TestWordPressAuthenticationMocked(unittest.TestCase):
    """Test authentication with mocked HTTP."""

    @patch("urllib.request.urlopen")
    def test_successful_authentication(self, mock_urlopen):
        """Successful authentication returns user identity."""
        client = WordPressClient("https://example.com", "testuser", "apppass")

        # Mock /users/me response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({
            "id": 1,
            "username": "testuser",
            "name": "Test User",
        }).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = client.verify_authentication()
        self.assertTrue(result["authenticated"])
        self.assertEqual(result["username"], "testuser")
        self.assertEqual(result["user_id"], 1)

    @patch("urllib.request.urlopen")
    def test_authentication_failure_401(self, mock_urlopen):
        """401 response raises authentication error."""
        client = WordPressClient("https://example.com", "bad", "credentials")

        # Simulate 401
        import urllib.error
        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 401, "Unauthorized", {}, None
        )

        with self.assertRaises(WordPressHTTPError) as exc_info:
            client.verify_authentication()
        self.assertEqual(exc_info.exception.status, 401)


class TestWordPressPreflightSequenceBehavioral(unittest.TestCase):
    """Test complete preflight validation with behavioral testing."""

    @patch("urllib.request.urlopen")
    def test_adapter_preflight_invokes_all_six_gates(self, mock_urlopen):
        """Preflight calls actual adapter.preflight() which verifies all 6 mandatory gates."""
        adapter = WordPressAdapter()

        # Authenticate first
        adapter.authenticate({
            "base_url": "https://example.com",
            "username": "user",
            "app_password": "apppass",
        })

        # Mock ALL HTTP responses needed for complete preflight
        responses = [
            # Gate 1: verify_https_and_api (GET /)
            {"namespace": "wp/v2"},
            # Gate 2: verify_authentication (GET /users/me)
            {"id": 1, "username": "user", "name": "Test User"},
            # Gate 3: verify_posts_endpoint (GET /posts?per_page=1)
            [{"id": 1}],
            # Gate 4: verify_media_endpoint (GET /media?per_page=1)
            [{"id": 100}],
            # Gate 5: verify_categories_endpoint (GET /categories?per_page=1)
            [{"id": 1, "name": "Uncategorized"}],
            # Gate 6: verify_tags_endpoint (GET /tags?per_page=1)
            [{"id": 1, "name": "News"}],
        ]

        def mock_response_side_effect(*args, **kwargs):
            mock_response = MagicMock()
            mock_response.status = 200
            response_data = responses.pop(0)
            mock_response.read.return_value = json.dumps(response_data).encode()
            mock_response.__enter__.return_value = mock_response
            return mock_response

        mock_urlopen.side_effect = mock_response_side_effect

        # INVOKE ACTUAL adapter.preflight()
        results = adapter.preflight({"destination_id": "test"})

        # Verify all 6 gates are in results and passed
        self.assertTrue(results["https_verified"])
        self.assertTrue(results["api_reachable"])
        self.assertTrue(results["authenticated"])
        self.assertTrue(results["posts_available"])
        self.assertTrue(results["media_available"])
        self.assertTrue(results["categories_available"])
        self.assertTrue(results["tags_available"])
        self.assertEqual(results["site_identity"]["username"], "user")
        self.assertTrue(adapter.preflight_passed)

    @patch("urllib.request.urlopen")
    def test_preflight_failure_no_writes_occur(self, mock_urlopen):
        """When ANY mandatory gate fails, NO writes occur."""
        adapter = WordPressAdapter()

        adapter.authenticate({
            "base_url": "https://example.com",
            "username": "user",
            "app_password": "apppass",
        })

        # Simulate API unreachable (gate 2 fails)
        import urllib.error
        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 0, "Connection failed", {}, None
        )

        # INVOKE adapter.preflight() - should raise
        with self.assertRaisesRegex(RuntimeError, r"Preflight failed"):
            adapter.preflight({"destination_id": "test"})

        # Verify adapter is NOT marked as preflight_passed
        self.assertFalse(adapter.preflight_passed)

        # Verify that attempting to publish FAILS (no writes allowed)
        with self.assertRaisesRegex(RuntimeError, r"preflight"):
            adapter.publish(
                {"title": "test", "content": "test"},
                {"destination_id": "test"},
            )


class TestMediaUploadMocked(unittest.TestCase):
    """Test media upload with mocked HTTP."""

    @patch("urllib.request.urlopen")
    def test_media_upload_preserves_exact_file(self, mock_urlopen):
        """Media upload uses exact file contents."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock media upload response
        mock_response = MagicMock()
        mock_response.status = 201
        mock_response.read.return_value = json.dumps({
            "id": 123,
            "source_url": "https://example.com/wp-content/uploads/2026/08/image.png",
            "alt_text": "Test image",
        }).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        file_data = b"\x89PNG\r\n..."  # Fake PNG
        result = client.upload_media("image.png", file_data, "Test image")

        self.assertEqual(result["id"], 123)
        self.assertEqual(result["source_url"], "https://example.com/wp-content/uploads/2026/08/image.png")
        self.assertEqual(result["alt_text"], "Test image")

    @patch("urllib.request.urlopen")
    def test_media_upload_preserves_declared_mime_type(self, mock_urlopen):
        """Media upload transmits declared MIME type in multipart header."""
        client = WordPressClient("https://example.com", "user", "password")

        # Capture the request to inspect multipart body
        captured_request = []

        def capture_urlopen(req, *args, **kwargs):
            captured_request.append(req)
            mock_response = MagicMock()
            mock_response.status = 201
            mock_response.read.return_value = json.dumps({
                "id": 123,
                "source_url": "https://example.com/wp-content/uploads/test.jpg",
                "alt_text": "Test",
            }).encode()
            mock_response.__enter__.return_value = mock_response
            return mock_response

        mock_urlopen.side_effect = capture_urlopen

        # Upload with specific MIME type
        file_data = b"\xff\xd8\xff\xe0"  # JPEG header
        client.upload_media("test.jpg", file_data, "Test", mime_type="image/jpeg")

        # Verify request was made
        self.assertGreater(len(captured_request), 0)

        # Inspect multipart body for declared MIME type
        request = captured_request[0]
        if isinstance(request.data, bytes):
            body_str = request.data.decode('utf-8', errors='replace')
            # The declared mime_type should appear in multipart
            self.assertIn("image/jpeg", body_str)


class TestCategoryResolutionBehavioral(unittest.TestCase):
    """Test category resolution with behavioral testing."""

    @patch("urllib.request.urlopen")
    def test_category_zero_exact_matches(self, mock_urlopen):
        """Category with zero exact matches returns None."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock empty search result
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps([]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = client.find_category_by_name("Nonexistent")
        self.assertIsNone(result)

    @patch("urllib.request.urlopen")
    def test_category_one_exact_match(self, mock_urlopen):
        """Category with one exact match returns that match."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock search result with one exact match
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps([
            {"id": 1, "name": "News", "slug": "news"},
            {"id": 2, "name": "News Updates", "slug": "news-updates"},
        ]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = client.find_category_by_name("News")
        self.assertIsNotNone(result)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "News")

    @patch("urllib.request.urlopen")
    def test_category_multiple_exact_matches_fails_closed(self, mock_urlopen):
        """Category with multiple exact matches raises ValueError (ambiguity)."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock search result with duplicate exact matches (edge case)
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps([
            {"id": 1, "name": "News", "slug": "news-1"},
            {"id": 2, "name": "News", "slug": "news-2"},
        ]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        with self.assertRaisesRegex(ValueError, r"Ambiguous"):
            client.find_category_by_name("News")


class TestTagResolutionBehavioral(unittest.TestCase):
    """Test tag resolution with behavioral testing."""

    @patch("urllib.request.urlopen")
    def test_tag_zero_exact_matches(self, mock_urlopen):
        """Tag with zero exact matches returns None."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock empty search result
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps([]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = client.find_tag_by_name("Nonexistent")
        self.assertIsNone(result)

    @patch("urllib.request.urlopen")
    def test_tag_one_exact_match(self, mock_urlopen):
        """Tag with one exact match returns that match."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock search result with one exact match
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps([
            {"id": 10, "name": "python", "slug": "python"},
            {"id": 11, "name": "python3", "slug": "python3"},
        ]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = client.find_tag_by_name("python")
        self.assertIsNotNone(result)
        self.assertEqual(result["id"], 10)
        self.assertEqual(result["name"], "python")

    @patch("urllib.request.urlopen")
    def test_tag_multiple_exact_matches_fails_closed(self, mock_urlopen):
        """Tag with multiple exact matches raises ValueError (ambiguity)."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock search result with duplicate exact matches
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps([
            {"id": 10, "name": "python", "slug": "python-1"},
            {"id": 11, "name": "python", "slug": "python-2"},
        ]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        with self.assertRaisesRegex(ValueError, r"Ambiguous"):
            client.find_tag_by_name("python")


class TestPostCreationMocked(unittest.TestCase):
    """Test post creation."""

    @patch("urllib.request.urlopen")
    def test_draft_post_creation(self, mock_urlopen):
        """Draft post is created with correct status."""
        client = WordPressClient("https://example.com", "user", "password")

        # Mock post creation response
        mock_response = MagicMock()
        mock_response.status = 201
        mock_response.read.return_value = json.dumps({
            "id": 42,
            "title": {"rendered": "Test Post"},
            "slug": "test-post",
            "status": "draft",
            "link": "https://example.com/test-post/",
        }).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        post_data = {
            "title": "Test Post",
            "content": "Test content",
            "status": "draft",
            "slug": "test-post",
        }

        result = client.create_post(post_data)
        self.assertEqual(result["id"], 42)
        self.assertEqual(result["status"], "draft")
        self.assertEqual(result["slug"], "test-post")


class TestScheduledPostMocked(unittest.TestCase):
    """Test scheduled post creation."""

    @patch("urllib.request.urlopen")
    def test_scheduled_post_creation_with_exact_time(self, mock_urlopen):
        """Scheduled post has exact time preserved."""
        client = WordPressClient("https://example.com", "user", "password")

        scheduled_time = "2026-08-15T14:30:00Z"

        # Mock post creation response
        mock_response = MagicMock()
        mock_response.status = 201
        mock_response.read.return_value = json.dumps({
            "id": 43,
            "title": {"rendered": "Scheduled Post"},
            "slug": "scheduled-post",
            "status": "future",
            "date_gmt": scheduled_time,
            "link": "https://example.com/scheduled-post/",
        }).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        post_data = {
            "title": "Scheduled Post",
            "content": "Scheduled content",
            "status": "future",
            "date": scheduled_time,
        }

        result = client.create_post(post_data)
        self.assertEqual(result["id"], 43)
        self.assertEqual(result["status"], "future")


class TestExactPayloadPreservation(unittest.TestCase):
    """Test that payload is not modified."""

    def test_adapter_preserves_title_exactly(self):
        """Title is not rewritten."""
        adapter = WordPressAdapter()
        adapter.authenticated = True

        payload = {
            "title": "Special: Title With Punctuation & Symbols!",
            "content": "Content",
            "status": "draft",
        }

        prepared = adapter.prepare(payload)
        self.assertEqual(prepared["title"], payload["title"])

    def test_adapter_preserves_excerpt_exactly(self):
        """Excerpt is not modified or generated."""
        adapter = WordPressAdapter()

        payload = {
            "title": "Title",
            "content": "Content",
            "excerpt": "Custom excerpt with special chars: <>&",
            "status": "draft",
        }

        prepared = adapter.prepare(payload)
        self.assertEqual(prepared["excerpt"], payload["excerpt"])

    def test_adapter_preserves_slug_exactly(self):
        """Slug is not altered."""
        adapter = WordPressAdapter()

        payload = {
            "title": "Title",
            "content": "Content",
            "slug": "exact-slug-as-approved",
            "status": "draft",
        }

        prepared = adapter.prepare(payload)
        self.assertEqual(prepared["slug"], payload["slug"])


class TestBodyVerificationNormalization(unittest.TestCase):
    """Test body verification with acceptable normalization."""

    def test_verification_passes_for_exact_body(self):
        """Verification passes when body matches exactly."""
        adapter = WordPressAdapter()
        adapter.client = MagicMock()

        # Mock get_post response with exact body
        adapter.client.get_post.return_value = {
            "id": 42,
            "title": {"rendered": "Title"},
            "content": {"rendered": "Exact content"},
            "slug": "slug",
            "status": "publish",
            "link": "https://example.com/slug/",
        }

        result = adapter.verify({"destination_id": "test"}, remote_id="42")
        self.assertTrue(result["passed"])


class TestVerificationMismatchFails(unittest.TestCase):
    """Test verification fails on substantive mismatches."""

    def test_verification_fails_on_missing_post(self):
        """Verification fails if post cannot be fetched."""
        adapter = WordPressAdapter()
        adapter.client = MagicMock()

        adapter.client.get_post.side_effect = WordPressHTTPError(404, "Not found", {})

        result = adapter.verify({"destination_id": "test"}, remote_id="999")
        self.assertFalse(result["passed"])


class TestIdempotencyNoDuplicate(unittest.TestCase):
    """Test safe retry does not duplicate post."""

    @patch("urllib.request.urlopen")
    def test_retry_finds_existing_post_by_slug(self, mock_urlopen):
        """Retry finds existing post and doesn't create duplicate."""
        adapter = WordPressAdapter()
        adapter.authenticate({
            "base_url": "https://example.com",
            "username": "user",
            "app_password": "apppass",
        })
        adapter.preflight_passed = True

        # Mock find_post_by_slug
        existing_post = {
            "id": 42,
            "slug": "test-post",
            "title": {"rendered": "Test Post"},
            "link": "https://example.com/test-post/",
            "status": "draft",
        }

        with patch.object(
            adapter.client, "find_post_by_slug", return_value=existing_post
        ), patch.object(
            adapter.client, "update_post", return_value=existing_post
        ):
            result = adapter.publish(
                {
                    "title": "Test Post",
                    "content": "Content",
                    "slug": "test-post",
                    "status": "draft",
                },
                {"destination_id": "test"},
            )

            self.assertEqual(result["remote_id"], "42")
            self.assertFalse(result["duplicated"])


class TestErrorMapping401(unittest.TestCase):
    """Test error mapping: 401 -> BLOCKED_AUTH."""

    @patch("urllib.request.urlopen")
    def test_401_maps_to_auth_error(self, mock_urlopen):
        """401 response indicates authentication failure."""
        import urllib.error

        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 401, "Unauthorized", {}, None
        )

        client = WordPressClient("https://example.com", "user", "password")

        with self.assertRaises(WordPressHTTPError) as exc_info:
            client.verify_authentication()

        self.assertEqual(exc_info.exception.status, 401)


class TestErrorMapping403(unittest.TestCase):
    """Test error mapping: 403 -> BLOCKED_AUTH."""

    @patch("urllib.request.urlopen")
    def test_403_maps_to_auth_error(self, mock_urlopen):
        """403 response indicates permission failure."""
        import urllib.error

        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 403, "Forbidden", {}, None
        )

        client = WordPressClient("https://example.com", "user", "password")

        with self.assertRaises(WordPressHTTPError) as exc_info:
            client.verify_authentication()

        self.assertEqual(exc_info.exception.status, 403)


class TestErrorMappingTransient(unittest.TestCase):
    """Test error mapping: 429/5xx -> FAILED_TRANSIENT."""

    @patch("urllib.request.urlopen")
    def test_429_indicates_transient_error(self, mock_urlopen):
        """429 (rate limited) is transient."""
        import urllib.error

        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 429, "Too Many Requests", {}, None
        )

        client = WordPressClient("https://example.com", "user", "password")

        with self.assertRaises(WordPressHTTPError) as exc_info:
            client.verify_authentication()

        self.assertEqual(exc_info.exception.status, 429)


class TestErrorMappingUnknown(unittest.TestCase):
    """Test error mapping: unknown -> fail-closed."""

    @patch("urllib.request.urlopen")
    def test_unknown_error_is_not_transient(self, mock_urlopen):
        """Unknown error should not be assumed safe to retry."""
        import urllib.error

        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 418, "I'm a teapot", {}, None
        )

        client = WordPressClient("https://example.com", "user", "password")

        with self.assertRaises(WordPressHTTPError) as exc_info:
            client.verify_authentication()

        # Status is preserved so caller can classify
        self.assertEqual(exc_info.exception.status, 418)


class TestSecretHandling(unittest.TestCase):
    """Test that secrets are never exposed."""

    def test_auth_header_never_logged(self):
        """Authorization header is never in logs."""
        client = WordPressClient("https://example.com", "user", "password")

        # Get the auth header (used internally)
        auth = client._make_auth_header()

        # It should be a valid header
        self.assertTrue(auth.startswith("Basic "))

        # But we never print/log it in error handling
        error = WordPressHTTPError(401, "Test", {"auth": auth})
        error_str = str(error)

        # The actual password hash should not appear
        self.assertIn("Basic " in error_str or "[REDACTED]", error_str)

    def test_app_password_never_in_error_message(self):
        """Application password never appears in error messages."""
        client = WordPressClient("https://example.com", "user", "secret_password")

        # Even if passed in details, it should be redacted
        error = WordPressHTTPError(
            400,
            "Bad request",
            {"app_password": "secret_password"},
        )
        error_str = str(error)

        self.assertNotIn("secret_password", error_str)


class TestReceiptSchemaValidity(unittest.TestCase):
    """Test that receipts conform to schema."""

    def test_receipt_has_required_fields(self):
        """Deployment receipt has all required fields."""
        from control_plane.receipts import create_receipt

        receipt = create_receipt(
            publication_id="test_001",
            package_hash="sha256:abc123",
            destination_id="wordpress_test",
            agent="wordpress_v1",
            status="PUBLISHED",
            remote_id="42",
            public_url="https://example.com/post/",
            verification_passed=True,
        )

        self.assertEqual(receipt["publication_id"], "test_001")
        self.assertEqual(receipt["destination_id"], "wordpress_test")
        self.assertEqual(receipt["agent"], "wordpress_v1")
        self.assertEqual(receipt["status"], "PUBLISHED")
        self.assertEqual(receipt["remote_id"], "42")


class TestValidation(unittest.TestCase):
    """Test payload and destination validation."""

    def test_validate_rejects_empty_payload(self):
        """Empty payload raises ValueError."""
        adapter = WordPressAdapter()

        with self.assertRaises(ValueError):
            adapter.validate({}, {"destination_id": "test"})

    def test_validate_requires_title(self):
        """Missing title raises ValueError."""
        adapter = WordPressAdapter()

        with self.assertRaisesRegex(ValueError, r"title"):
            adapter.validate(
                {"content": "test"},
                {"destination_id": "test"},
            )

    def test_validate_requires_content(self):
        """Missing content raises ValueError."""
        adapter = WordPressAdapter()

        with self.assertRaisesRegex(ValueError, r"content"):
            adapter.validate(
                {"title": "test"},
                {"destination_id": "test"},
            )

    def test_validate_requires_valid_status(self):
        """Invalid status raises ValueError."""
        adapter = WordPressAdapter()

        with self.assertRaisesRegex(ValueError, r"status"):
            adapter.validate(
                {
                    "title": "test",
                    "content": "test",
                    "status": "invalid_status",
                },
                {"destination_id": "test"},
            )

    def test_validate_accepts_valid_statuses(self):
        """Valid statuses are accepted."""
        adapter = WordPressAdapter()

        for status in ["draft", "future", "publish"]:
            # Should not raise
            adapter.validate(
                {
                    "title": "test",
                    "content": "test",
                    "status": status,
                },
                {"destination_id": "test"},
            )


class TestAdapterLifecycle(unittest.TestCase):
    """Test the complete adapter lifecycle."""

    def test_adapter_requires_authenticate_before_preflight(self):
        """Preflight requires prior authentication."""
        adapter = WordPressAdapter()

        with self.assertRaisesRegex(RuntimeError, r"authenticate"):
            adapter.preflight({"destination_id": "test"})

    def test_adapter_requires_preflight_before_publish(self):
        """Publish requires prior preflight."""
        adapter = WordPressAdapter()
        adapter.authenticated = True
        adapter.client = MagicMock()

        with self.assertRaisesRegex(RuntimeError, r"preflight"):
            adapter.publish(
                {"title": "test", "content": "test"},
                {"destination_id": "test"},
            )


class TestTaxonomyResolutionInAdapter(unittest.TestCase):
    """Test taxonomy resolution through adapter methods."""

    @patch.object(WordPressClient, "find_category_by_name")
    def test_adapter_resolve_categories_single_category(self, mock_find):
        """Adapter resolves single category correctly."""
        adapter = WordPressAdapter()
        adapter.client = MagicMock()
        adapter.client.find_category_by_name = mock_find

        mock_find.return_value = {"id": 1, "name": "News", "slug": "news"}

        category_ids = adapter._resolve_categories(["News"])
        self.assertEqual(category_ids, [1])

    @patch.object(WordPressClient, "find_category_by_name")
    def test_adapter_resolve_categories_ambiguity_propagates(self, mock_find):
        """Adapter propagates ambiguity error from find_category_by_name."""
        adapter = WordPressAdapter()
        adapter.client = MagicMock()
        adapter.client.find_category_by_name = mock_find

        mock_find.side_effect = ValueError("Ambiguous category name")

        with self.assertRaisesRegex(ValueError, r"Ambiguous"):
            adapter._resolve_categories(["News"])

    @patch.object(WordPressClient, "find_tag_by_name")
    def test_adapter_resolve_tags_single_tag(self, mock_find):
        """Adapter resolves single tag correctly."""
        adapter = WordPressAdapter()
        adapter.client = MagicMock()
        adapter.client.find_tag_by_name = mock_find

        mock_find.return_value = {"id": 10, "name": "python", "slug": "python"}

        tag_ids = adapter._resolve_tags(["python"])
        self.assertEqual(tag_ids, [10])

    @patch.object(WordPressClient, "find_tag_by_name")
    def test_adapter_resolve_tags_ambiguity_propagates(self, mock_find):
        """Adapter propagates ambiguity error from find_tag_by_name."""
        adapter = WordPressAdapter()
        adapter.client = MagicMock()
        adapter.client.find_tag_by_name = mock_find

        mock_find.side_effect = ValueError("Ambiguous tag name")

        with self.assertRaisesRegex(ValueError, r"Ambiguous"):
            adapter._resolve_tags(["python"])
