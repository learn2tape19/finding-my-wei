"""
Deployment orchestrator.

Executes the complete deployment pipeline:
1. Load and validate manifest
2. Compute package hash
3. Validate founder approval
4. Resolve destinations
5. Check for duplicates
6. Route to adapters
7. Collect receipts

Implements the control flow but only with a dry-run adapter (no live platforms).
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Callable

from .manifest import load_manifest, validate_manifest
from .hasher import compute_package_hash, validate_hash_format
from .approval import check_approval_gate, load_approval
from .destinations import resolve_destination
from .receipts import create_receipt, write_receipt, find_previous_receipt
from .adapters import DryRunAdapter, DestinationAdapter
from .errors import (
    DuplicateDeploymentError,
    DestinationNotFoundError,
    ManifestValidationError,
)


class DeploymentOrchestrator:
    """Orchestrates publication deployments."""

    def __init__(
        self,
        manifest_file: str,
        approval_file: str,
        destination_registry_file: str,
        receipts_dir: str,
        adapter_factory: Optional[Callable[[str], DestinationAdapter]] = None,
    ):
        """
        Initialize orchestrator.

        Args:
            manifest_file: Path to publication.manifest.json
            approval_file: Path to founder.approval.json
            destination_registry_file: Path to destination registry YAML
            receipts_dir: Directory to write receipts to
            adapter_factory: Optional function(destination_id) -> DestinationAdapter
                           If None, uses DryRunAdapter for all
        """
        self.manifest_file = manifest_file
        self.approval_file = approval_file
        self.destination_registry_file = destination_registry_file
        self.receipts_dir = receipts_dir
        self.adapter_factory = adapter_factory or self._default_adapter_factory

    @staticmethod
    def _default_adapter_factory(destination_id: str) -> DestinationAdapter:
        """Default factory: return DryRunAdapter for all destinations."""
        return DryRunAdapter()

    def validate_manifest(self) -> Dict[str, Any]:
        """Load and validate manifest."""
        manifest = load_manifest(self.manifest_file)
        return manifest

    def _recompute_and_validate_package_hash(self, manifest: Dict[str, Any]) -> str:
        """
        Independently compute package hash and validate it matches manifest.

        REQUIRED: Recompute package identity before approval/deployment.
        Orchestrator must independently call the canonical hasher against
        the current manifest and require the computed hash to equal
        manifest["package_hash"] before Founder approval is evaluated or
        any adapter executes.

        Args:
            manifest: Publication manifest

        Returns:
            Recomputed package hash

        Raises:
            PackageHashError if computed hash does not match declared hash
        """
        manifest_dir = Path(self.manifest_file).parent
        computed_hash = compute_package_hash(manifest, manifest_dir)
        declared_hash = manifest.get("package_hash")

        if computed_hash != declared_hash:
            from .errors import HashMismatchError
            raise HashMismatchError(
                "Package hash validation failed: computed hash does not match declared hash",
                {
                    "computed": computed_hash,
                    "declared": declared_hash,
                },
            )

        return computed_hash

    def validate_approval(self, manifest: Dict[str, Any]) -> Dict[str, Any]:
        """Validate founder approval against manifest."""
        publication_id = manifest["publication_id"]

        # REQUIRED: Recompute package hash before approval evaluation
        package_hash = self._recompute_and_validate_package_hash(manifest)

        # Load and check structure
        approval = load_approval(self.approval_file)

        # Validate all declared destinations have approvals
        for dest in manifest.get("destinations", []):
            dest_id = dest["destination_id"]
            check_approval_gate(
                publication_id,
                package_hash,
                dest_id,
                self.approval_file,
            )

        return approval

    def deploy_to_destination(
        self,
        manifest: Dict[str, Any],
        destination_id: str,
        payload: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Deploy approved publication to a single destination.

        Returns deployment receipt.
        """
        publication_id = manifest["publication_id"]

        # REQUIRED: Recompute package hash before deployment
        package_hash = self._recompute_and_validate_package_hash(manifest)

        # Check approval
        check_approval_gate(
            publication_id,
            package_hash,
            destination_id,
            self.approval_file,
        )

        # Resolve destination from registry
        destination = resolve_destination(self.destination_registry_file, destination_id)

        # Check for previous successful deployment (duplicate detection)
        previous = find_previous_receipt(
            self.receipts_dir,
            publication_id,
            destination_id,
            package_hash,
        )
        if previous:
            raise DuplicateDeploymentError(
                f"Publication {publication_id} already deployed to {destination_id}",
                {
                    "previous_receipt": previous,
                    "destination_id": destination_id,
                },
            )

        # Get adapter
        adapter = self.adapter_factory(destination_id)

        try:
            # Validate
            adapter.validate(payload, destination)

            # Authenticate
            adapter.authenticate({})  # No real credentials in dry-run

            # Prepare
            prepared = adapter.prepare(payload)

            # Publish/schedule
            response = adapter.publish(
                prepared,
                destination,
                schedule_at=self._get_schedule_time(manifest, destination_id),
            )

            # Verify
            verification = adapter.verify(
                destination,
                remote_id=response.get("remote_id"),
                public_url=response.get("public_url"),
            )

            # Create receipt
            receipt = create_receipt(
                publication_id=publication_id,
                package_hash=package_hash,
                destination_id=destination_id,
                agent=destination["adapter"],
                status=response.get("status", "PUBLISHED"),
                remote_id=response.get("remote_id"),
                public_url=response.get("public_url"),
                verification_passed=verification.get("passed", False),
                verification_checked_at=None,
                verification_details=verification.get("details"),
            )

            # Write receipt
            receipt_path = write_receipt(receipt, self.receipts_dir)

            return {
                "success": True,
                "destination_id": destination_id,
                "remote_id": response.get("remote_id"),
                "receipt": receipt,
                "receipt_path": receipt_path,
            }

        except Exception as e:
            # Determine error class from exception or default to non-retryable
            error_class = getattr(e, "error_class", None)

            # REQUIRED: Only explicitly recognized transient conditions become FAILED_TRANSIENT
            # Unknown/unclassified failures must fail closed using non-retryable state
            explicit_transient_classes = {"FAILED_TRANSIENT"}
            if error_class in explicit_transient_classes:
                receipt_status = "FAILED_TRANSIENT"
            elif error_class and error_class.startswith("BLOCKED_"):
                receipt_status = error_class
            else:
                # Unknown/unclassified exception: fail closed with non-retryable state
                receipt_status = "FAILED_REQUIRES_FOUNDER"
                if not error_class:
                    error_class = "FAILED_REQUIRES_FOUNDER"

            error_message = str(e)

            # Create failure receipt
            receipt = create_receipt(
                publication_id=publication_id,
                package_hash=package_hash,
                destination_id=destination_id,
                agent=destination.get("adapter", "unknown"),
                status=receipt_status,
                error_class=error_class,
                error_message=error_message,
            )

            # Write receipt
            receipt_path = write_receipt(receipt, self.receipts_dir)

            return {
                "success": False,
                "destination_id": destination_id,
                "error_class": error_class,
                "error_message": error_message,
                "receipt": receipt,
                "receipt_path": receipt_path,
            }

    def deploy_all(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deploy to all approved destinations in manifest.

        Returns consolidated report.
        """
        # Validate manifest
        manifest = self.validate_manifest()

        # Validate approval
        self.validate_approval(manifest)

        # Deploy to each destination
        results = []
        for dest in manifest.get("destinations", []):
            destination_id = dest["destination_id"]
            try:
                result = self.deploy_to_destination(manifest, destination_id, payload)
                results.append(result)
            except Exception as e:
                results.append({
                    "success": False,
                    "destination_id": destination_id,
                    "error": str(e),
                })

        return {
            "publication_id": manifest["publication_id"],
            "package_hash": manifest["package_hash"],
            "deployment_results": results,
            "successful_count": sum(1 for r in results if r.get("success")),
            "failed_count": sum(1 for r in results if not r.get("success")),
        }

    @staticmethod
    def _get_schedule_time(manifest: Dict[str, Any], destination_id: str) -> Optional[str]:
        """Extract schedule time for a destination from manifest."""
        for dest in manifest.get("destinations", []):
            if dest["destination_id"] == destination_id:
                return dest.get("publish_at")
        return None
