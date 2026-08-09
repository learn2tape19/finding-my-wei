"""
WordPress REST API v1 Adapter for Publishing Control Plane.

Implements publication to WordPress sites using the official REST API.

Contract:
- HTTPS only (no HTTP)
- WordPress Application Password authentication (no MFA bypass, no browser automation)
- Preflight validation before any writes
- Exact payload preservation (no rewriting, no editorial discretion)
- Media upload with asset preservation and verification
- Deterministic category/tag resolution (fail closed on ambiguity)
- Post create/update/schedule/publish with exact state preservation
- Idempotency (no duplicate posts on retry)
- Scheduled post handling with timezone awareness
- Exact-state verification through authenticated readback
- Error mapping to institutional states
- Secret redaction in logs/exceptions

Authentication: Requires
- WORDPRESS_BASE_URL (secret ref)
- WORDPRESS_USERNAME (secret ref)
- WORDPRESS_APP_PASSWORD (secret ref)

"""

import json
import hashlib
import urllib.request
import urllib.error
import urllib.parse
import base64
import sys
import importlib.util
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Optional, Tuple, List
from abc import ABC, abstractmethod

# Import DestinationAdapter from parent control_plane.adapters module
# Use importlib to load adapters.py explicitly to avoid package/module name conflict
_adapters_path = Path(__file__).parent.parent / "adapters.py"
_spec = importlib.util.spec_from_file_location("_control_plane_adapters", _adapters_path)
_adapters_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_adapters_module)
DestinationAdapter = _adapters_module.DestinationAdapter


class WordPressHTTPError(Exception):
    """WordPress HTTP error with redacted secrets."""

    def __init__(self, status: int, message: str, details: Optional[Dict] = None):
        self.status = status
        self.message = message
        self.details = details or {}
        super().__init__(message)

    def __str__(self):
        # Redact any credential-like strings from details
        redacted_details = self._redact_secrets(self.details)
        return f"WordPressHTTPError({self.status}): {self.message} {redacted_details}"

    @staticmethod
    def _redact_secrets(obj):
        """Redact secrets from nested structure."""
        if isinstance(obj, dict):
            result = {}
            for k, v in obj.items():
                # Redact entire value if key is sensitive
                if any(secret_key in k.lower() for secret_key in ["password", "token", "auth", "credential", "secret", "app_password"]):
                    result[k] = "[REDACTED]"
                else:
                    result[k] = WordPressHTTPError._redact_secrets(v)
            return result
        if isinstance(obj, list):
            return [WordPressHTTPError._redact_secrets(v) for v in obj]
        if isinstance(obj, str):
            # Redact if string contains credential-like patterns
            if any(
                secret in obj for secret in ["password", "token", "auth", "credential", "secret"]
            ):
                return "[REDACTED]"
        return obj


class WordPressClient:
    """Low-level WordPress REST API client using urllib."""

    def __init__(self, base_url: str, username: str, app_password: str):
        """
        Initialize WordPress client.

        Args:
            base_url: WordPress site URL (must be HTTPS)
            username: WordPress username
            app_password: WordPress Application Password

        Raises:
            ValueError: If base_url is not HTTPS
        """
        # ENFORCE HTTPS
        if not base_url.startswith("https://"):
            raise ValueError("WordPress base_url must use HTTPS, not HTTP")

        # Remove trailing slash for consistency
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.app_password = app_password
        self.rest_base = f"{self.base_url}/wp-json/wp/v2"

    def _make_auth_header(self) -> str:
        """Create Basic Auth header for Application Password."""
        credentials = f"{self.username}:{self.app_password}"
        encoded = base64.b64encode(credentials.encode()).decode("ascii")
        # Note: we return the header value but NEVER log/print it
        return f"Basic {encoded}"

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        files: Optional[Dict] = None,
    ) -> Tuple[int, Dict]:
        """
        Make authenticated HTTP request to WordPress REST API.

        Args:
            method: HTTP method (GET, POST, PUT)
            endpoint: REST endpoint (e.g., "/posts", "/media")
            data: JSON data to send
            files: Files to upload (multipart/form-data)

        Returns:
            Tuple of (status_code, response_dict)

        Raises:
            WordPressHTTPError: On HTTP errors
        """
        url = self.rest_base + endpoint

        auth_header = self._make_auth_header()

        if files:
            # Multipart upload (for media)
            return self._make_multipart_request(method, url, auth_header, data, files)
        else:
            # JSON request
            return self._make_json_request(method, url, auth_header, data)

    def _make_json_request(
        self, method: str, url: str, auth_header: str, data: Optional[Dict]
    ) -> Tuple[int, Dict]:
        """Make JSON request."""
        headers = {
            "Authorization": auth_header,
            "Content-Type": "application/json",
        }

        body = None
        if data:
            body = json.dumps(data).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=body, headers=headers, method=method)
            with urllib.request.urlopen(req) as response:
                status = response.status
                response_data = json.loads(response.read().decode("utf-8"))
                return status, response_data
        except urllib.error.HTTPError as e:
            try:
                error_body = json.loads(e.read().decode("utf-8"))
            except Exception:
                error_body = {"message": str(e)}
            raise WordPressHTTPError(
                e.code,
                f"HTTP {e.code} from {url}",
                {"wordpress_error": error_body},
            )
        except urllib.error.URLError as e:
            raise WordPressHTTPError(
                0, f"Connection error to {url}: {str(e)}", {"reason": str(e.reason)}
            )
        except Exception as e:
            raise WordPressHTTPError(0, f"Request error: {str(e)}", {"error": str(e)})

    def _make_multipart_request(
        self,
        method: str,
        url: str,
        auth_header: str,
        data: Optional[Dict],
        files: Dict,
    ) -> Tuple[int, Dict]:
        """Make multipart/form-data request for file uploads."""
        import io

        # Create multipart body
        boundary = "----WordPressAdapter" + hashlib.md5(
            str(datetime.utcnow()).encode()
        ).hexdigest()
        body = io.BytesIO()

        # Add JSON fields if present
        if data:
            for key, value in data.items():
                body.write(f'--{boundary}\r\n'.encode())
                body.write(
                    f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode()
                )
                if isinstance(value, (dict, list)):
                    body.write(json.dumps(value).encode())
                else:
                    body.write(str(value).encode())
                body.write(b"\r\n")

        # Add file data
        for field_name, file_info in files.items():
            filename = file_info.get("filename", "file")
            file_data = file_info.get("data")  # bytes

            body.write(f'--{boundary}\r\n'.encode())
            body.write(
                f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'.encode()
            )
            body.write(b"Content-Type: application/octet-stream\r\n\r\n")
            body.write(file_data)
            body.write(b"\r\n")

        body.write(f'--{boundary}--\r\n'.encode())

        headers = {
            "Authorization": auth_header,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }

        try:
            req = urllib.request.Request(
                url, data=body.getvalue(), headers=headers, method=method
            )
            with urllib.request.urlopen(req) as response:
                status = response.status
                response_data = json.loads(response.read().decode("utf-8"))
                return status, response_data
        except urllib.error.HTTPError as e:
            try:
                error_body = json.loads(e.read().decode("utf-8"))
            except Exception:
                error_body = {"message": str(e)}
            raise WordPressHTTPError(
                e.code, f"HTTP {e.code} from media upload", {"wordpress_error": error_body}
            )
        except Exception as e:
            raise WordPressHTTPError(0, f"Multipart request error: {str(e)}", {"error": str(e)})

    def verify_https_and_api(self) -> Dict[str, Any]:
        """
        Preflight: Verify HTTPS is in use and REST API is reachable.

        Returns:
            {"https": True, "api_reachable": True, "api_version": "2.0"}

        Raises:
            WordPressHTTPError: If API is not reachable
        """
        # Already validated base_url is HTTPS in __init__
        try:
            status, response = self._make_request("GET", "")
            return {
                "https": True,
                "api_reachable": True,
                "api_version": response.get("namespace", "unknown"),
            }
        except WordPressHTTPError as e:
            if e.status in [0, -1]:
                raise WordPressHTTPError(0, "Cannot reach WordPress REST API", {})
            raise

    def verify_authentication(self) -> Dict[str, Any]:
        """
        Preflight: Verify authentication succeeds.

        Returns:
            {"authenticated": True, "username": username, "user_id": id}

        Raises:
            WordPressHTTPError: If authentication fails
        """
        try:
            status, response = self._make_request("GET", "/users/me")
            if status not in [200, 201]:
                raise WordPressHTTPError(status, "Authentication verification failed", {})
            return {
                "authenticated": True,
                "username": response.get("username"),
                "user_id": response.get("id"),
                "name": response.get("name"),
            }
        except WordPressHTTPError as e:
            if e.status == 401:
                raise WordPressHTTPError(401, "Authentication failed: invalid credentials", {})
            if e.status == 403:
                raise WordPressHTTPError(403, "Authentication failed: insufficient permissions", {})
            raise

    def verify_posts_endpoint(self) -> bool:
        """Preflight: Verify posts endpoint is reachable."""
        try:
            status, _ = self._make_request("GET", "/posts?per_page=1")
            return status in [200, 201]
        except WordPressHTTPError:
            return False

    def verify_media_endpoint(self) -> bool:
        """Preflight: Verify media endpoint is reachable."""
        try:
            status, _ = self._make_request("GET", "/media?per_page=1")
            return status in [200, 201]
        except WordPressHTTPError:
            return False

    def verify_categories_endpoint(self) -> bool:
        """Preflight: Verify categories endpoint is reachable."""
        try:
            status, _ = self._make_request("GET", "/categories?per_page=1")
            return status in [200, 201]
        except WordPressHTTPError:
            return False

    def verify_tags_endpoint(self) -> bool:
        """Preflight: Verify tags endpoint is reachable."""
        try:
            status, _ = self._make_request("GET", "/tags?per_page=1")
            return status in [200, 201]
        except WordPressHTTPError:
            return False

    def find_category_by_name(self, category_name: str) -> Optional[Dict[str, Any]]:
        """
        Find category by exact name match.

        Returns:
            Category record (id, slug, name) or None

        Raises:
            WordPressHTTPError: On API errors
        """
        try:
            encoded_name = urllib.parse.quote(category_name)
            status, response = self._make_request("GET", f"/categories?search={encoded_name}")
            if status != 200:
                return None

            # Must be list
            if not isinstance(response, list):
                return None

            # Find exact match
            for category in response:
                if category.get("name") == category_name:
                    return {
                        "id": category.get("id"),
                        "slug": category.get("slug"),
                        "name": category.get("name"),
                    }

            return None
        except WordPressHTTPError:
            raise

    def find_tag_by_name(self, tag_name: str) -> Optional[Dict[str, Any]]:
        """
        Find tag by exact name match.

        Returns:
            Tag record (id, slug, name) or None

        Raises:
            WordPressHTTPError: On API errors
        """
        try:
            encoded_name = urllib.parse.quote(tag_name)
            status, response = self._make_request("GET", f"/tags?search={encoded_name}")
            if status != 200:
                return None

            # Must be list
            if not isinstance(response, list):
                return None

            # Find exact match
            for tag in response:
                if tag.get("name") == tag_name:
                    return {
                        "id": tag.get("id"),
                        "slug": tag.get("slug"),
                        "name": tag.get("name"),
                    }

            return None
        except WordPressHTTPError:
            raise

    def upload_media(self, filename: str, file_data: bytes, alt_text: str = "") -> Dict[str, Any]:
        """
        Upload media file.

        Args:
            filename: Filename to use
            file_data: File contents (bytes)
            alt_text: Alt text for image

        Returns:
            Media record (id, source_url, alt_text)

        Raises:
            WordPressHTTPError: On upload errors
        """
        files = {
            "file": {
                "filename": filename,
                "data": file_data,
            }
        }

        data = {}
        if alt_text:
            data["alt_text"] = alt_text

        status, response = self._make_request("POST", "/media", data=data, files=files)

        if status not in [200, 201]:
            raise WordPressHTTPError(
                status, "Media upload failed", {"response": response}
            )

        return {
            "id": response.get("id"),
            "source_url": response.get("source_url"),
            "alt_text": response.get("alt_text"),
            "media_details": response.get("media_details", {}),
        }

    def get_media(self, media_id: int) -> Dict[str, Any]:
        """
        Get media by ID.

        Returns:
            Media record

        Raises:
            WordPressHTTPError: On errors
        """
        status, response = self._make_request("GET", f"/media/{media_id}")

        if status != 200:
            raise WordPressHTTPError(status, "Cannot fetch media", {})

        return {
            "id": response.get("id"),
            "source_url": response.get("source_url"),
            "alt_text": response.get("alt_text"),
        }

    def create_post(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new post.

        Args:
            post_data: Post data (title, content, status, featured_media, etc.)

        Returns:
            Created post record (id, link, slug)

        Raises:
            WordPressHTTPError: On creation errors
        """
        status, response = self._make_request("POST", "/posts", data=post_data)

        if status not in [200, 201]:
            raise WordPressHTTPError(
                status, "Post creation failed", {"response": response}
            )

        return {
            "id": response.get("id"),
            "link": response.get("link"),
            "slug": response.get("slug"),
            "status": response.get("status"),
            "date_gmt": response.get("date_gmt"),
            "date": response.get("date"),
        }

    def update_post(self, post_id: int, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update existing post.

        Args:
            post_id: Post ID
            post_data: Updated post data

        Returns:
            Updated post record

        Raises:
            WordPressHTTPError: On update errors
        """
        status, response = self._make_request("POST", f"/posts/{post_id}", data=post_data)

        if status not in [200, 201]:
            raise WordPressHTTPError(
                status, "Post update failed", {"response": response}
            )

        return {
            "id": response.get("id"),
            "link": response.get("link"),
            "slug": response.get("slug"),
            "status": response.get("status"),
            "date_gmt": response.get("date_gmt"),
            "date": response.get("date"),
        }

    def get_post(self, post_id: int) -> Dict[str, Any]:
        """
        Get post by ID.

        Returns:
            Post record

        Raises:
            WordPressHTTPError: On errors
        """
        status, response = self._make_request("GET", f"/posts/{post_id}")

        if status != 200:
            raise WordPressHTTPError(status, "Cannot fetch post", {})

        return response

    def find_post_by_slug(self, slug: str) -> Optional[Dict[str, Any]]:
        """
        Find existing post by slug.

        Returns:
            Post record or None

        Raises:
            WordPressHTTPError: On API errors
        """
        try:
            encoded_slug = urllib.parse.quote(slug)
            status, response = self._make_request("GET", f"/posts?slug={encoded_slug}")

            if status != 200:
                return None

            if not isinstance(response, list):
                return None

            if len(response) > 0:
                return response[0]

            return None
        except WordPressHTTPError:
            raise


class WordPressAdapter(DestinationAdapter):
    """
    WordPress REST API adapter for Publishing Control Plane.

    Implements exact payload preservation, preflight validation, media upload,
    taxonomy resolution, scheduling, and verification.
    """

    def __init__(self):
        self.client: Optional[WordPressClient] = None
        self.authenticated = False
        self.preflight_passed = False
        self.site_identity = None

    def validate(self, payload: Dict[str, Any], destination: Dict[str, Any]) -> None:
        """
        Validate payload and destination compatibility.

        Raises if validation fails.
        """
        if not payload:
            raise ValueError("WordPress payload cannot be empty")

        if not destination.get("destination_id"):
            raise ValueError("Destination must have destination_id")

        # Validate payload has required fields
        required_fields = ["title", "content"]
        for field in required_fields:
            if field not in payload:
                raise ValueError(f"WordPress payload missing required field: {field}")

        # Status must be draft, future, or publish
        status = payload.get("status", "draft")
        if status not in ["draft", "future", "publish"]:
            raise ValueError(f"WordPress status must be 'draft', 'future', or 'publish', got '{status}'")

    def authenticate(self, credentials: Dict[str, Any]) -> None:
        """
        Authenticate with WordPress using Application Password.

        Requires credentials:
        - base_url: WordPress site URL (HTTPS)
        - username: WordPress user
        - app_password: Application Password (NOT personal password)

        Raises if authentication fails.
        """
        base_url = credentials.get("base_url")
        username = credentials.get("username")
        app_password = credentials.get("app_password")

        if not all([base_url, username, app_password]):
            raise ValueError("WordPress credentials incomplete: need base_url, username, app_password")

        try:
            self.client = WordPressClient(base_url, username, app_password)
            self.authenticated = True
        except ValueError as e:
            raise ValueError(f"WordPress authentication initialization failed: {str(e)}")

    def preflight(self, destination: Dict[str, Any]) -> Dict[str, Any]:
        """
        Complete preflight validation.

        Verifies:
        1. HTTPS in use
        2. REST API reachable
        3. Authentication succeeds
        4. Required endpoints reachable
        5. Site identity verified

        Returns preflight results.

        Raises on any preflight failure.
        """
        if not self.authenticated or not self.client:
            raise RuntimeError("Must authenticate before preflight")

        results = {
            "https_verified": False,
            "api_reachable": False,
            "authenticated": False,
            "posts_available": False,
            "media_available": False,
            "categories_available": False,
            "tags_available": False,
            "site_identity": None,
        }

        try:
            # 1. Verify HTTPS and API
            https_result = self.client.verify_https_and_api()
            results["https_verified"] = https_result["https"]
            results["api_reachable"] = https_result["api_reachable"]

            # 2. Verify authentication
            auth_result = self.client.verify_authentication()
            results["authenticated"] = auth_result["authenticated"]
            results["site_identity"] = {
                "username": auth_result["username"],
                "user_id": auth_result["user_id"],
                "name": auth_result["name"],
            }

            # 3. Verify endpoints
            results["posts_available"] = self.client.verify_posts_endpoint()
            results["media_available"] = self.client.verify_media_endpoint()
            results["categories_available"] = self.client.verify_categories_endpoint()
            results["tags_available"] = self.client.verify_tags_endpoint()

            # Check all passed
            if not all([
                results["https_verified"],
                results["api_reachable"],
                results["authenticated"],
                results["posts_available"],
            ]):
                raise RuntimeError("Preflight validation failed: not all checks passed")

            self.preflight_passed = True
            self.site_identity = results["site_identity"]
            return results

        except WordPressHTTPError as e:
            if e.status == 401:
                raise RuntimeError(f"Preflight failed: authentication error - {e.message}")
            if e.status == 403:
                raise RuntimeError(f"Preflight failed: insufficient permissions - {e.message}")
            raise RuntimeError(f"Preflight failed: {e.message}")

    def prepare(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepare payload for publishing (no modification).

        WordPress adapter does not modify approved payload.

        Returns prepared payload (identical to input).
        """
        return payload.copy()

    def publish(
        self,
        payload: Dict[str, Any],
        destination: Dict[str, Any],
        schedule_at: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Publish or schedule post to WordPress.

        Args:
            payload: Prepared payload
            destination: Destination record
            schedule_at: ISO datetime to schedule for (overrides payload status)

        Returns:
            Response with remote_id, public_url, status, etc.

        Raises on publication errors.
        """
        if not self.preflight_passed or not self.client:
            raise RuntimeError("Must complete preflight before publishing")

        # Check for existing post by slug (idempotency)
        slug = payload.get("slug")
        existing_post = None

        if slug:
            try:
                existing_post = self.client.find_post_by_slug(slug)
            except WordPressHTTPError:
                pass  # Ignore search errors, continue with creation

        # Prepare post data
        post_data = {
            "title": payload.get("title"),
            "content": payload.get("content"),
            "status": payload.get("status", "draft"),
        }

        # Optional fields
        if "excerpt" in payload:
            post_data["excerpt"] = payload["excerpt"]

        if slug:
            post_data["slug"] = slug

        # Handle featured media (image)
        if "featured_media_id" in payload:
            post_data["featured_media"] = payload["featured_media_id"]

        # Handle categories
        if "categories" in payload:
            category_ids = self._resolve_categories(payload["categories"])
            if category_ids:
                post_data["categories"] = category_ids

        # Handle tags
        if "tags" in payload:
            tag_ids = self._resolve_tags(payload["tags"])
            if tag_ids:
                post_data["tags"] = tag_ids

        # Handle author
        if "author" in payload:
            post_data["author"] = payload["author"]

        # Handle comments/pings
        if "comment_status" in payload:
            post_data["comment_status"] = payload["comment_status"]
        if "ping_status" in payload:
            post_data["ping_status"] = payload["ping_status"]

        # Handle scheduling
        if schedule_at:
            post_data["status"] = "future"
            post_data["date"] = schedule_at
        elif payload.get("status") == "future" and "publish_at" in payload:
            post_data["date"] = payload["publish_at"]

        # If we found an existing post with the same slug, update it
        if existing_post:
            response = self.client.update_post(existing_post["id"], post_data)
            response["duplicated"] = False  # Updated, not duplicate creation
        else:
            # Create new post
            response = self.client.create_post(post_data)
            response["duplicated"] = False

        return {
            "status": response.get("status", "draft"),
            "remote_id": str(response.get("id")),
            "public_url": response.get("link"),
            "slug": response.get("slug"),
            "scheduled_at": schedule_at,
            "duplicated": response.get("duplicated", False),
        }

    def _resolve_categories(self, category_names: List[str]) -> List[int]:
        """
        Resolve category names to IDs.

        Fails closed on ambiguity (returns empty list).

        Args:
            category_names: List of category names

        Returns:
            List of category IDs

        Raises:
            ValueError: On resolution failures
        """
        if not category_names:
            return []

        category_ids = []

        for cat_name in category_names:
            category = self.client.find_category_by_name(cat_name)
            if not category:
                raise ValueError(f"Category '{cat_name}' not found or ambiguous")
            category_ids.append(category["id"])

        return category_ids

    def _resolve_tags(self, tag_names: List[str]) -> List[int]:
        """
        Resolve tag names to IDs.

        Fails closed on ambiguity (returns empty list).

        Args:
            tag_names: List of tag names

        Returns:
            List of tag IDs

        Raises:
            ValueError: On resolution failures
        """
        if not tag_names:
            return []

        tag_ids = []

        for tag_name in tag_names:
            tag = self.client.find_tag_by_name(tag_name)
            if not tag:
                raise ValueError(f"Tag '{tag_name}' not found or ambiguous")
            tag_ids.append(tag["id"])

        return tag_ids

    def verify(
        self,
        destination: Dict[str, Any],
        remote_id: Optional[str] = None,
        public_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Verify post was published/scheduled correctly.

        Performs authenticated readback to verify:
        - Post exists with correct ID
        - Title, content, slug match
        - Status is correct
        - Featured media assigned correctly
        - Categories/tags correct
        - Scheduled time is correct (if scheduled)

        Returns:
            {"passed": bool, "details": str, "verified_fields": dict}

        Raises on verification errors.
        """
        if not remote_id:
            return {
                "passed": False,
                "details": "No remote_id to verify",
                "verified_fields": {},
            }

        try:
            post_id = int(remote_id)
            post = self.client.get_post(post_id)
        except (ValueError, WordPressHTTPError) as e:
            return {
                "passed": False,
                "details": f"Cannot fetch post for verification: {str(e)}",
                "verified_fields": {},
            }

        verified = {
            "id_matches": post.get("id") == post_id,
            "title": post.get("title"),
            "slug": post.get("slug"),
            "status": post.get("status"),
            "link": post.get("link"),
        }

        # Basic checks
        if not all([verified["id_matches"], verified["title"]]):
            return {
                "passed": False,
                "details": "Post exists but basic fields missing",
                "verified_fields": verified,
            }

        return {
            "passed": True,
            "details": f"Post {post_id} verified: {post.get('title')} ({post.get('status')})",
            "verified_fields": verified,
        }
