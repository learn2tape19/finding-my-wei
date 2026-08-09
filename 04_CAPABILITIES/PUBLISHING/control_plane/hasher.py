"""
Deterministic package hashing.

Computes canonical SHA-256 identity for publication packages ensuring:
- Same package produces same hash locally and remotely
- Operational receipts excluded from hash
- Approval files excluded from hash
- Asset hashes verified
- Ordering produces no accidental drift
"""

import hashlib
import json
from pathlib import Path
from typing import Dict, Any, Optional
from .errors import PackageHashError, AssetHashMismatchError


def compute_file_hash(file_path: str) -> str:
    """Compute SHA-256 hash of a file."""
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        raise PackageHashError(f"Failed to hash file {file_path}", {"error": str(e)})


def canonicalize_manifest(manifest: Dict[str, Any]) -> str:
    """
    Convert manifest to canonical JSON for hashing.

    Excludes: receipts, approval documents, schema_version.
    Includes: all declared public payload content and asset hashes in deterministic order.
    """
    canonical = {}

    # Core publication identity
    canonical["publication_id"] = manifest.get("publication_id")
    canonical["domain"] = manifest.get("domain")
    canonical["canonical_commit"] = manifest.get("canonical_commit")
    canonical["status"] = manifest.get("status")
    canonical["publish_at"] = manifest.get("publish_at")

    # Assets in sorted order (deterministic)
    if "assets" in manifest:
        assets = []
        for asset in sorted(manifest["assets"], key=lambda a: a.get("id", "")):
            asset_copy = {
                "id": asset.get("id"),
                "path": asset.get("path"),
                "sha256": asset.get("sha256"),
                "media_type": asset.get("media_type"),
            }
            if "alt_text" in asset and asset["alt_text"]:
                asset_copy["alt_text"] = asset["alt_text"]
            assets.append(asset_copy)
        canonical["assets"] = assets

    # Destinations in sorted order (deterministic)
    if "destinations" in manifest:
        destinations = []
        for dest in sorted(manifest["destinations"], key=lambda d: d.get("destination_id", "")):
            dest_copy = {
                "destination_id": dest.get("destination_id"),
                "payload_ref": dest.get("payload_ref"),
            }
            if dest.get("publish_at"):
                dest_copy["publish_at"] = dest.get("publish_at")
            if dest.get("schedule_window_minutes") is not None:
                dest_copy["schedule_window_minutes"] = dest.get("schedule_window_minutes")
            destinations.append(dest_copy)
        canonical["destinations"] = destinations

    # QA status
    if "qa" in manifest and manifest["qa"]:
        canonical["qa"] = {
            "passed": manifest["qa"].get("passed"),
            "checked_at": manifest["qa"].get("checked_at"),
        }

    return json.dumps(canonical, sort_keys=True, separators=(",", ":"))


def compute_package_hash(manifest: Dict[str, Any], manifest_dir: Optional[Path] = None) -> str:
    """
    Compute deterministic SHA-256 hash of publication package.

    Returns: "sha256:<hex_digest>"

    Verifies asset hashes match declared values.
    Fails closed if any declared asset is missing.
    Excludes operational receipts and approval documents.
    """
    # Canonicalize manifest (excludes schema_version, receipts, approval files)
    canonical_json = canonicalize_manifest(manifest)

    # Verify all asset hashes match declared values (if assets directory provided)
    if manifest_dir and "assets" in manifest:
        manifest_dir = Path(manifest_dir)
        for asset in manifest["assets"]:
            asset_path = manifest_dir / asset["path"]
            # MUST FAIL CLOSED: declared asset must exist
            if not asset_path.exists():
                raise PackageHashError(
                    f"Declared asset missing: {asset['path']}",
                    {
                        "asset_id": asset["id"],
                        "asset_path": str(asset_path),
                        "error": "asset_not_found",
                    },
                )
            computed_hash = compute_file_hash(str(asset_path))
            if computed_hash != asset["sha256"]:
                raise AssetHashMismatchError(
                    f"Asset {asset['path']} hash mismatch",
                    {
                        "asset_id": asset["id"],
                        "declared": asset["sha256"],
                        "computed": computed_hash,
                    },
                )

    # Hash the canonical JSON
    sha256_hash = hashlib.sha256(canonical_json.encode("utf-8"))
    digest = sha256_hash.hexdigest()

    return f"sha256:{digest}"


def validate_hash_format(package_hash: str) -> bool:
    """Validate that hash matches expected format: sha256:<64_hex_chars>."""
    if not isinstance(package_hash, str):
        return False
    if not package_hash.startswith("sha256:"):
        return False
    hex_part = package_hash[7:]
    if len(hex_part) != 64:
        return False
    try:
        int(hex_part, 16)
        return True
    except ValueError:
        return False
