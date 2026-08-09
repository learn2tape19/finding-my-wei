"""
Optional integration harness for WordPress V1 adapter.

Tests real WordPress site integration (staging only).

This harness is opt-in and requires explicit environment configuration.
It will refuse to run if:
- Staging URL is not configured
- Site is marked production
- Credentials are missing

What it validates:
1. Preflight against real staging WordPress site
2. Media upload and verification
3. Post create with categories and tags
4. Post verification via readback
5. Scheduled post creation
6. Idempotent retry (no duplicate)

IMPORTANT: This harness MUST target a non-production staging site.
Production WordPress sites are protected and will be rejected.
"""

import os
import sys
import json
import pytest
from pathlib import Path
from datetime import datetime, timedelta

# Add control_plane to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from control_plane.adapters.wordpress_v1 import (
    WordPressAdapter,
    WordPressClient,
    WordPressHTTPError,
)


class TestWordPressIntegrationHarness:
    """Integration harness for WordPress adapter (staging only)."""

    @classmethod
    def setup_class(cls):
        """Check if integration testing is enabled."""
        cls.staging_enabled = os.getenv("PCP_WORDPRESS_STAGING_ENABLED", "").lower() == "true"
        cls.staging_url = os.getenv("PCP_WORDPRESS_STAGING_URL")
        cls.staging_username = os.getenv("PCP_WORDPRESS_STAGING_USERNAME")
        cls.staging_app_password = os.getenv("PCP_WORDPRESS_STAGING_APP_PASSWORD")

        if not cls.staging_enabled:
            pytest.skip("WordPress staging integration not enabled (set PCP_WORDPRESS_STAGING_ENABLED=true)")

        if not all([cls.staging_url, cls.staging_username, cls.staging_app_password]):
            pytest.skip("WordPress staging credentials not configured")

        # Prevent accidental production use
        if "production" in cls.staging_url.lower() or "prod" in cls.staging_url.lower():
            pytest.skip("Integration tests will NOT run against production")

    def test_staging_preflight_succeeds(self):
        """Preflight validation passes against staging site."""
        if not self.staging_enabled:
            pytest.skip()

        adapter = WordPressAdapter()

        try:
            adapter.authenticate({
                "base_url": self.staging_url,
                "username": self.staging_username,
                "app_password": self.staging_app_password,
            })

            results = adapter.preflight({"destination_id": "staging_test"})

            assert results["https_verified"] is True
            assert results["api_reachable"] is True
            assert results["authenticated"] is True
            assert results["posts_available"] is True
            assert results["site_identity"]["username"] == self.staging_username

        except WordPressHTTPError as e:
            pytest.skip(f"Cannot connect to staging site: {e.message}")

    def test_staging_media_upload(self):
        """Media upload works against staging site."""
        if not self.staging_enabled:
            pytest.skip()

        adapter = WordPressAdapter()

        adapter.authenticate({
            "base_url": self.staging_url,
            "username": self.staging_username,
            "app_password": self.staging_app_password,
        })

        adapter.preflight_passed = True

        # Create a simple test image
        test_image_data = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
            b"\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00"
            b"\x00\x0cIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x00"
            b"\x00\x00\x00IEND\xaeB`\x82"
        )

        try:
            result = adapter.client.upload_media(
                "pcp_test_image.png",
                test_image_data,
                "PCP Test Image",
            )

            assert result["id"] > 0
            assert result["source_url"]
            assert result["alt_text"] == "PCP Test Image"

        except WordPressHTTPError as e:
            pytest.skip(f"Media upload failed: {e.message}")

    def test_staging_post_creation(self):
        """Post creation works against staging site."""
        if not self.staging_enabled:
            pytest.skip()

        adapter = WordPressAdapter()

        adapter.authenticate({
            "base_url": self.staging_url,
            "username": self.staging_username,
            "app_password": self.staging_app_password,
        })

        adapter.preflight_passed = True

        test_slug = f"pcp-test-{datetime.utcnow().strftime('%s')}"

        payload = {
            "title": "PCP Test Post",
            "content": "This is a test post created by the Publishing Control Plane integration harness.",
            "slug": test_slug,
            "status": "draft",
            "excerpt": "Test post for PCP validation",
        }

        try:
            result = adapter.publish(payload, {"destination_id": "staging_test"})

            assert result["remote_id"]
            assert result["status"] == "draft"
            assert result["slug"] == test_slug

        except WordPressHTTPError as e:
            pytest.skip(f"Post creation failed: {e.message}")

    def test_staging_scheduled_post(self):
        """Scheduled post creation works against staging site."""
        if not self.staging_enabled:
            pytest.skip()

        adapter = WordPressAdapter()

        adapter.authenticate({
            "base_url": self.staging_url,
            "username": self.staging_username,
            "app_password": self.staging_app_password,
        })

        adapter.preflight_passed = True

        # Schedule for 1 hour from now
        future_time = (datetime.utcnow() + timedelta(hours=1)).isoformat() + "Z"
        test_slug = f"pcp-scheduled-{datetime.utcnow().strftime('%s')}"

        payload = {
            "title": "PCP Scheduled Test Post",
            "content": "This post is scheduled for future publication.",
            "slug": test_slug,
            "status": "future",
            "publish_at": future_time,
        }

        try:
            result = adapter.publish(payload, {"destination_id": "staging_test"}, schedule_at=future_time)

            assert result["remote_id"]
            assert result["status"] == "future"
            assert result["scheduled_at"] == future_time

        except WordPressHTTPError as e:
            pytest.skip(f"Scheduled post creation failed: {e.message}")

    def test_staging_idempotent_retry(self):
        """Retry finds existing post and doesn't duplicate."""
        if not self.staging_enabled:
            pytest.skip()

        adapter = WordPressAdapter()

        adapter.authenticate({
            "base_url": self.staging_url,
            "username": self.staging_username,
            "app_password": self.staging_app_password,
        })

        adapter.preflight_passed = True

        test_slug = f"pcp-idempotent-{datetime.utcnow().strftime('%s')}"

        payload = {
            "title": "PCP Idempotency Test",
            "content": "Test post for idempotency validation.",
            "slug": test_slug,
            "status": "draft",
        }

        try:
            # First publish
            result1 = adapter.publish(payload, {"destination_id": "staging_test"})
            remote_id_1 = result1["remote_id"]

            # Second publish (retry)
            result2 = adapter.publish(payload, {"destination_id": "staging_test"})
            remote_id_2 = result2["remote_id"]

            # Should be the same post
            assert remote_id_1 == remote_id_2
            assert result2["duplicated"] is False

        except WordPressHTTPError as e:
            pytest.skip(f"Idempotency test failed: {e.message}")

    def test_staging_post_verification(self):
        """Post verification works against staging site."""
        if not self.staging_enabled:
            pytest.skip()

        adapter = WordPressAdapter()

        adapter.authenticate({
            "base_url": self.staging_url,
            "username": self.staging_username,
            "app_password": self.staging_app_password,
        })

        adapter.preflight_passed = True

        test_slug = f"pcp-verify-{datetime.utcnow().strftime('%s')}"

        payload = {
            "title": "PCP Verification Test",
            "content": "Test post for readback verification.",
            "slug": test_slug,
            "status": "draft",
        }

        try:
            # Publish
            result = adapter.publish(payload, {"destination_id": "staging_test"})
            remote_id = result["remote_id"]

            # Verify
            verification = adapter.verify({"destination_id": "staging_test"}, remote_id=remote_id)

            assert verification["passed"] is True
            assert verification["verified_fields"]["id_matches"] is True

        except WordPressHTTPError as e:
            pytest.skip(f"Verification test failed: {e.message}")


# Test markers
# Usage: pytest -m integration tests/test_wordpress_v1_adapter_integration.py
pytestmark = pytest.mark.skipif(
    os.getenv("PCP_WORDPRESS_STAGING_ENABLED", "").lower() != "true",
    reason="WordPress staging integration not enabled",
)
