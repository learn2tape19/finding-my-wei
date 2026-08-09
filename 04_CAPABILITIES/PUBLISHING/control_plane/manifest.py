"""
Publication manifest validation.

Validates manifest.json against schema and structural constraints.
"""

import json
import re
from typing import Dict, Any
from .errors import ManifestValidationError


VALID_STATUSES = {
    "DRAFT",
    "PRODUCTION",
    "QA",
    "READY_FOR_FOUNDER_APPROVAL",
    "FOUNDER_APPROVED_FOR_LAUNCH",
    "QUEUED",
    "DEPLOYING",
    "VERIFIED",
    "BLOCKED_AUTH",
    "BLOCKED_PLATFORM",
    "FAILED_TRANSIENT",
    "FAILED_REQUIRES_FOUNDER",
    "PARTIALLY_DEPLOYED",
}


def validate_manifest(manifest: Dict[str, Any]) -> None:
    """
    Validate manifest against schema and constraints.

    Raises ManifestValidationError if validation fails.
    """
    if not isinstance(manifest, dict):
        raise ManifestValidationError("Manifest must be a dictionary")

    # Schema version
    if manifest.get("schema_version") != "1.0":
        raise ManifestValidationError("schema_version must be exactly '1.0'")

    # Publication ID
    pub_id = manifest.get("publication_id")
    if not pub_id or not isinstance(pub_id, str) or len(pub_id) < 1:
        raise ManifestValidationError("publication_id is required and must be non-empty string")

    # Domain
    domain = manifest.get("domain")
    if not domain or not isinstance(domain, str) or len(domain) < 1:
        raise ManifestValidationError("domain is required and must be non-empty string")

    # Canonical commit
    canonical_commit = manifest.get("canonical_commit")
    if not canonical_commit or not isinstance(canonical_commit, str):
        raise ManifestValidationError("canonical_commit is required and must be string")
    if not re.match(r"^[0-9a-f]{7,40}$", canonical_commit):
        raise ManifestValidationError(
            "canonical_commit must be 7-40 character hex string",
            {"received": canonical_commit},
        )

    # Package hash
    package_hash = manifest.get("package_hash")
    if not package_hash or not isinstance(package_hash, str):
        raise ManifestValidationError("package_hash is required and must be string")
    if not re.match(r"^sha256:[0-9a-f]{64}$", package_hash):
        raise ManifestValidationError(
            "package_hash must be format sha256:<64_hex_chars>",
            {"received": package_hash},
        )

    # Status
    status = manifest.get("status")
    if not status or status not in VALID_STATUSES:
        raise ManifestValidationError(
            f"status must be one of {VALID_STATUSES}",
            {"received": status},
        )

    # Publish time (optional)
    if "publish_at" in manifest:
        publish_at = manifest["publish_at"]
        if publish_at is not None and not isinstance(publish_at, str):
            raise ManifestValidationError("publish_at must be ISO datetime string or null")

    # Assets (required)
    assets = manifest.get("assets")
    if not isinstance(assets, list):
        raise ManifestValidationError("assets must be array")
    if len(assets) == 0:
        raise ManifestValidationError("assets array must not be empty")

    for i, asset in enumerate(assets):
        if not isinstance(asset, dict):
            raise ManifestValidationError(f"Asset {i} must be dictionary")

        asset_id = asset.get("id")
        if not asset_id or not isinstance(asset_id, str):
            raise ManifestValidationError(f"Asset {i}: id is required and must be string")

        asset_path = asset.get("path")
        if not asset_path or not isinstance(asset_path, str):
            raise ManifestValidationError(f"Asset {i}: path is required and must be string")

        asset_sha = asset.get("sha256")
        if not asset_sha or not isinstance(asset_sha, str):
            raise ManifestValidationError(f"Asset {i}: sha256 is required and must be string")
        if not re.match(r"^[0-9a-f]{64}$", asset_sha):
            raise ManifestValidationError(
                f"Asset {i}: sha256 must be 64-character hex string",
                {"received": asset_sha},
            )

        media_type = asset.get("media_type")
        if not media_type or not isinstance(media_type, str):
            raise ManifestValidationError(f"Asset {i}: media_type is required and must be string")

        # alt_text is optional
        if "alt_text" in asset:
            alt_text = asset["alt_text"]
            if alt_text is not None and not isinstance(alt_text, str):
                raise ManifestValidationError(f"Asset {i}: alt_text must be string or null")

    # Destinations (required)
    destinations = manifest.get("destinations")
    if not isinstance(destinations, list):
        raise ManifestValidationError("destinations must be array")
    if len(destinations) < 1:
        raise ManifestValidationError("destinations must have at least 1 entry")

    for i, dest in enumerate(destinations):
        if not isinstance(dest, dict):
            raise ManifestValidationError(f"Destination {i} must be dictionary")

        dest_id = dest.get("destination_id")
        if not dest_id or not isinstance(dest_id, str):
            raise ManifestValidationError(
                f"Destination {i}: destination_id is required and must be string"
            )

        payload_ref = dest.get("payload_ref")
        if not payload_ref or not isinstance(payload_ref, str):
            raise ManifestValidationError(
                f"Destination {i}: payload_ref is required and must be string"
            )

        # publish_at is optional
        if "publish_at" in dest:
            publish_at = dest["publish_at"]
            if publish_at is not None and not isinstance(publish_at, str):
                raise ManifestValidationError(
                    f"Destination {i}: publish_at must be ISO datetime string or null"
                )

        # schedule_window_minutes is optional
        if "schedule_window_minutes" in dest:
            window = dest["schedule_window_minutes"]
            if not isinstance(window, int) or window < 0:
                raise ManifestValidationError(
                    f"Destination {i}: schedule_window_minutes must be non-negative integer"
                )

    # QA (optional)
    if "qa" in manifest and manifest["qa"] is not None:
        qa = manifest["qa"]
        if not isinstance(qa, dict):
            raise ManifestValidationError("qa must be dictionary or null")
        if "passed" in qa and not isinstance(qa["passed"], bool):
            raise ManifestValidationError("qa.passed must be boolean")
        if "checked_at" in qa and not isinstance(qa["checked_at"], str):
            raise ManifestValidationError("qa.checked_at must be datetime string")
        if "notes" in qa:
            if not isinstance(qa["notes"], list):
                raise ManifestValidationError("qa.notes must be array")
            for note in qa["notes"]:
                if not isinstance(note, str):
                    raise ManifestValidationError("qa.notes entries must be strings")


def load_manifest(file_path: str) -> Dict[str, Any]:
    """Load and validate manifest from JSON file."""
    try:
        with open(file_path, "r") as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        raise ManifestValidationError(f"Manifest JSON is malformed: {e}")
    except Exception as e:
        raise ManifestValidationError(f"Cannot read manifest file: {e}")

    validate_manifest(manifest)
    return manifest
