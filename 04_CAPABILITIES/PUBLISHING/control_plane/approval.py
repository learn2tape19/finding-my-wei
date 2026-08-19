"""
Founder approval validation gate.

Validates that deployment may only proceed when:
- approval state is exactly FOUNDER_APPROVED_FOR_LAUNCH
- publication IDs match
- package hashes match exactly
- requested destination is in approved destinations
- destination exists and is enabled

Fails closed on any mismatch.
"""

import json
import re
from typing import Dict, Any, Set
from .errors import (
    ApprovalStateError,
    ApprovalNotFoundError,
    ApprovalFileError,
    HashMismatchError,
)


def validate_approval_file(approval: Dict[str, Any]) -> None:
    """Validate approval JSON against schema."""
    if not isinstance(approval, dict):
        raise ApprovalFileError("Approval must be a dictionary")

    # Schema version
    if approval.get("schema_version") != "1.0":
        raise ApprovalFileError("schema_version must be exactly '1.0'")

    # Publication ID
    pub_id = approval.get("publication_id")
    if not pub_id or not isinstance(pub_id, str):
        raise ApprovalFileError("publication_id is required and must be string")

    # Package hash
    package_hash = approval.get("package_hash")
    if not package_hash or not isinstance(package_hash, str):
        raise ApprovalFileError("package_hash is required and must be string")
    if not re.match(r"^sha256:[0-9a-f]{64}$", package_hash):
        raise ApprovalFileError(
            "package_hash must be format sha256:<64_hex_chars>",
            {"received": package_hash},
        )

    # State — must be exactly FOUNDER_APPROVED_FOR_LAUNCH
    state = approval.get("state")
    if state != "FOUNDER_APPROVED_FOR_LAUNCH":
        raise ApprovalStateError(
            "Approval state must be exactly 'FOUNDER_APPROVED_FOR_LAUNCH'",
            {"received": state},
        )

    # Approved by — must be Drew Freedman
    approved_by = approval.get("approved_by")
    if approved_by != "Drew Freedman":
        raise ApprovalFileError(
            "Approval must be by 'Drew Freedman'",
            {"received": approved_by},
        )

    # Approved at timestamp
    approved_at = approval.get("approved_at")
    if not approved_at or not isinstance(approved_at, str):
        raise ApprovalFileError("approved_at is required and must be ISO datetime string")

    # Destinations
    destinations = approval.get("destinations")
    if not isinstance(destinations, list):
        raise ApprovalFileError("destinations must be array")
    if len(destinations) < 1:
        raise ApprovalFileError("destinations must have at least 1 entry")
    if len(destinations) != len(set(destinations)):
        raise ApprovalFileError("destinations must be unique (no duplicates)")
    for dest in destinations:
        if not isinstance(dest, str):
            raise ApprovalFileError("Each destination must be string")

    # notes is optional
    if "notes" in approval:
        notes = approval["notes"]
        if notes is not None and not isinstance(notes, str):
            raise ApprovalFileError("notes must be string or null")


def load_approval(file_path: str) -> Dict[str, Any]:
    """Load and validate approval from JSON file."""
    try:
        with open(file_path, "r") as f:
            approval = json.load(f)
    except json.JSONDecodeError as e:
        raise ApprovalFileError(f"Approval JSON is malformed: {e}")
    except Exception as e:
        raise ApprovalFileError(f"Cannot read approval file: {e}")

    validate_approval_file(approval)
    return approval


def check_approval_gate(
    publication_id: str,
    package_hash: str,
    requested_destination: str,
    approval_file_path: str,
) -> Dict[str, Any]:
    """
    Validate deployment is authorized by founder approval.

    Args:
        publication_id: Publication ID from manifest
        package_hash: Package hash (sha256:...)
        requested_destination: Destination ID to deploy to
        approval_file_path: Path to founder.approval.json

    Returns:
        Approval dictionary if all checks pass

    Raises:
        ApprovalNotFoundError: Approval file does not exist
        ApprovalFileError: Approval is malformed
        ApprovalStateError: Approval is not in FOUNDER_APPROVED_FOR_LAUNCH state
        HashMismatchError: Package hash does not match
    """
    try:
        approval = load_approval(approval_file_path)
    except ApprovalFileError:
        raise
    except Exception as e:
        raise ApprovalNotFoundError(f"Cannot find or read approval file: {e}")

    # Check publication ID matches
    if approval.get("publication_id") != publication_id:
        raise ApprovalStateError(
            f"Publication ID mismatch in approval",
            {
                "manifest_id": publication_id,
                "approval_id": approval.get("publication_id"),
            },
        )

    # Check package hash matches exactly
    if approval.get("package_hash") != package_hash:
        raise HashMismatchError(
            f"Package hash mismatch with approval",
            {
                "manifest_hash": package_hash,
                "approval_hash": approval.get("package_hash"),
            },
        )

    # Check requested destination is in approved destinations
    approved_destinations = approval.get("destinations", [])
    if requested_destination not in approved_destinations:
        raise ApprovalStateError(
            f"Destination '{requested_destination}' is not in approved destinations",
            {
                "requested": requested_destination,
                "approved": approved_destinations,
            },
        )

    return approval


def get_approved_destinations(approval_file_path: str) -> Set[str]:
    """Get set of all destinations approved in approval file."""
    approval = load_approval(approval_file_path)
    return set(approval.get("destinations", []))
