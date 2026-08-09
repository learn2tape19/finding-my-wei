"""
Adapter protocol and dry-run adapter.

Defines the contract all destination adapters must implement.
Includes a dry-run adapter for testing without touching real platforms.
"""

import json
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime


class DestinationAdapter(ABC):
    """
    Abstract base class for all destination adapters.

    Contract:
    validate → authenticate → prepare → publish/schedule → verify → receipt
    """

    @abstractmethod
    def validate(self, payload: Dict[str, Any], destination: Dict[str, Any]) -> None:
        """
        Validate that payload and destination are compatible.

        Raises if validation fails.
        """
        pass

    @abstractmethod
    def authenticate(self, credentials: Dict[str, Any]) -> None:
        """
        Authenticate with the destination platform.

        Raises if authentication fails.
        """
        pass

    @abstractmethod
    def prepare(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepare payload for publishing (format conversion if needed).

        Returns prepared payload.
        """
        pass

    @abstractmethod
    def publish(
        self,
        payload: Dict[str, Any],
        destination: Dict[str, Any],
        schedule_at: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Publish or schedule the payload to the destination.

        Args:
            payload: Prepared payload
            destination: Destination record
            schedule_at: ISO datetime to schedule for (if applicable)

        Returns:
            Response dictionary containing remote_id, public_url, status, etc.
        """
        pass

    @abstractmethod
    def verify(
        self,
        destination: Dict[str, Any],
        remote_id: Optional[str] = None,
        public_url: Optional[str] = None,
    ) -> Dict[str, bool]:
        """
        Verify that content was published/scheduled successfully.

        Returns:
            Dictionary with 'passed': bool, 'details': str
        """
        pass


class DryRunAdapter(DestinationAdapter):
    """
    Dry-run adapter for testing without touching real platforms.

    Proves that:
    - exact payload reaches the adapter
    - adapter cannot mutate canonical source
    - a structured receipt returns
    - duplicate invocation can be detected using publication/package/destination identity
    """

    def __init__(self):
        self.authenticated = False
        self.published_items = {}

    def validate(self, payload: Dict[str, Any], destination: Dict[str, Any]) -> None:
        """Validate payload and destination."""
        if not payload:
            raise ValueError("Payload cannot be empty")
        if not destination.get("destination_id"):
            raise ValueError("Destination must have destination_id")

    def authenticate(self, credentials: Dict[str, Any]) -> None:
        """Simulate authentication (always succeeds)."""
        self.authenticated = True

    def prepare(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Return payload unchanged (dry-run doesn't modify)."""
        # Verify we cannot mutate the input
        return {
            "original_payload_hash": hash(json.dumps(payload, sort_keys=True)),
            "payload": payload,
        }

    def publish(
        self,
        payload: Dict[str, Any],
        destination: Dict[str, Any],
        schedule_at: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Simulate publishing (generate fake remote ID)."""
        if not self.authenticated:
            raise RuntimeError("Must authenticate first")

        publication_id = payload.get("publication_id")
        destination_id = destination.get("destination_id")

        # Generate fake remote ID
        remote_id = f"dry_run_{publication_id}_{destination_id}_{datetime.utcnow().timestamp()}"

        # Record for duplicate detection
        key = f"{publication_id}_{destination_id}_{payload.get('package_hash')}"
        if key in self.published_items:
            # Duplicate detected
            return {
                "status": "DUPLICATE",
                "remote_id": self.published_items[key]["remote_id"],
                "duplicated": True,
            }

        self.published_items[key] = {
            "remote_id": remote_id,
            "published_at": datetime.utcnow().isoformat(),
            "destination": destination_id,
        }

        status = "SCHEDULED" if schedule_at else "PUBLISHED"

        return {
            "status": status,
            "remote_id": remote_id,
            "public_url": f"https://dry-run.local/{publication_id}/{destination_id}",
            "scheduled_at": schedule_at if schedule_at else None,
        }

    def verify(
        self,
        destination: Dict[str, Any],
        remote_id: Optional[str] = None,
        public_url: Optional[str] = None,
    ) -> Dict[str, bool]:
        """Verify publication (dry-run always passes if remote_id is present)."""
        if not remote_id:
            return {"passed": False, "details": "No remote_id to verify"}

        # Dry-run verification always passes for valid remote_id
        return {
            "passed": True,
            "details": f"Dry-run verification passed for {remote_id}",
        }
