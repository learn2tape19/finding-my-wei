"""
Institutional failure states and error classes.

Each error maps to a deployment receipt error_class and represents a
distinct escalation/retry policy.
"""


class ControlPlaneError(Exception):
    """Base exception for all control plane failures."""
    error_class = None

    def __init__(self, message, details=None):
        self.message = message
        self.details = details or {}
        super().__init__(message)


class ManifestValidationError(ControlPlaneError):
    """Manifest is malformed or missing required fields."""
    error_class = "MANIFEST_VALIDATION_FAILED"


class HashMismatchError(ControlPlaneError):
    """Approved hash does not match package hash."""
    error_class = "HASH_MISMATCH"


class ApprovalStateError(ControlPlaneError):
    """Approval state is not exactly FOUNDER_APPROVED_FOR_LAUNCH."""
    error_class = "BLOCKED_FOUNDER_APPROVAL"


class ApprovalNotFoundError(ControlPlaneError):
    """No founder approval record exists for this publication."""
    error_class = "BLOCKED_FOUNDER_APPROVAL"


class DestinationNotFoundError(ControlPlaneError):
    """Destination is not in registry."""
    error_class = "BLOCKED_PLATFORM"


class DestinationDisabledError(ControlPlaneError):
    """Destination is registered but disabled."""
    error_class = "BLOCKED_PLATFORM"


class ApprovalFileError(ControlPlaneError):
    """Approval file is malformed or unreadable."""
    error_class = "BLOCKED_FOUNDER_APPROVAL"


class DestinationRegistryError(ControlPlaneError):
    """Destination registry is malformed or missing."""
    error_class = "BLOCKED_PLATFORM"


class PackageHashError(ControlPlaneError):
    """Package hash could not be computed or is invalid."""
    error_class = "HASH_MISMATCH"


class DuplicateDeploymentError(ControlPlaneError):
    """Deployment has already been executed for this publication/destination/hash."""
    error_class = "FAILED_REQUIRES_FOUNDER"


class AssetHashMismatchError(ControlPlaneError):
    """Asset hash does not match declared hash in manifest."""
    error_class = "FAILED_REQUIRES_FOUNDER"
