"""
Deployment receipt generation and management.

Creates append-only structured receipts recording deployment outcomes,
remote IDs, verification results, and error states.
"""

import json
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path
from .errors import ControlPlaneError


def create_receipt(
    publication_id: str,
    package_hash: str,
    destination_id: str,
    agent: str,
    status: str,
    remote_id: Optional[str] = None,
    public_url: Optional[str] = None,
    verification_passed: bool = False,
    verification_checked_at: Optional[str] = None,
    verification_details: Optional[str] = None,
    error_class: Optional[str] = None,
    error_message: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a deployment receipt.

    Args:
        publication_id: Publication ID
        package_hash: Package hash (sha256:...)
        destination_id: Destination ID
        agent: Agent/adapter name
        status: One of QUEUED, SCHEDULED, PUBLISHED, VERIFIED, FAILED_TRANSIENT,
                BLOCKED_AUTH, BLOCKED_PLATFORM, FAILED_REQUIRES_FOUNDER
        remote_id: Remote platform object ID if applicable
        public_url: Public URL of published content if applicable
        verification_passed: Boolean
        verification_checked_at: ISO datetime of verification check
        verification_details: String details about verification
        error_class: Institutional error class if failed
        error_message: Error message if failed

    Returns:
        Receipt dictionary conforming to deployment.receipt.schema.json
    """
    valid_statuses = {
        "QUEUED",
        "SCHEDULED",
        "PUBLISHED",
        "VERIFIED",
        "FAILED_TRANSIENT",
        "BLOCKED_AUTH",
        "BLOCKED_PLATFORM",
        "FAILED_REQUIRES_FOUNDER",
    }

    if status not in valid_statuses:
        raise ValueError(f"status must be one of {valid_statuses}")

    receipt = {
        "schema_version": "1.0",
        "publication_id": publication_id,
        "package_hash": package_hash,
        "destination_id": destination_id,
        "agent": agent,
        "attempted_at": datetime.utcnow().isoformat() + "Z",
        "status": status,
        "remote_id": remote_id,
        "public_url": public_url,
        "verification": {
            "passed": verification_passed,
            "checked_at": verification_checked_at,
            "details": verification_details,
        },
        "error_class": error_class,
        "error_message": error_message,
    }

    return receipt


def write_receipt(receipt: Dict[str, Any], receipt_dir: str) -> str:
    """
    Write receipt to file in receipts directory.

    Filename pattern: {publication_id}_{destination_id}_{timestamp}.json

    Args:
        receipt: Receipt dictionary
        receipt_dir: Directory to write receipt to

    Returns:
        Path to written receipt file
    """
    receipt_dir = Path(receipt_dir)
    receipt_dir.mkdir(parents=True, exist_ok=True)

    publication_id = receipt["publication_id"]
    destination_id = receipt["destination_id"]
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")

    filename = f"{publication_id}_{destination_id}_{timestamp}.json"
    filepath = receipt_dir / filename

    with open(filepath, "w") as f:
        json.dump(receipt, f, indent=2)

    return str(filepath)


def read_receipts(receipt_dir: str) -> list:
    """Read all receipts from directory."""
    receipt_dir = Path(receipt_dir)
    if not receipt_dir.exists():
        return []

    receipts = []
    for receipt_file in sorted(receipt_dir.glob("*.json")):
        try:
            with open(receipt_file, "r") as f:
                receipt = json.load(f)
                receipts.append(receipt)
        except (json.JSONDecodeError, Exception):
            pass

    return receipts


def find_previous_receipt(
    receipt_dir: str,
    publication_id: str,
    destination_id: str,
    package_hash: str,
) -> Optional[Dict[str, Any]]:
    """
    Find previous successful receipt for same publication/destination/hash.

    Used for duplicate deployment detection.
    """
    receipts = read_receipts(receipt_dir)

    # Look for most recent receipt matching publication, destination, hash
    for receipt in reversed(receipts):
        if (
            receipt.get("publication_id") == publication_id
            and receipt.get("destination_id") == destination_id
            and receipt.get("package_hash") == package_hash
            and receipt.get("status") in ("PUBLISHED", "VERIFIED", "SCHEDULED")
        ):
            return receipt

    return None
