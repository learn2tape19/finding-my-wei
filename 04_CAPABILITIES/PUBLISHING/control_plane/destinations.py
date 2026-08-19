"""
Destination registry resolution.

Reads destination registry, validates destinations, and resolves adapter/auth
references without exposing secret values.

Dependencies: PyYAML (for parsing YAML registry files)
"""

import yaml
from typing import Dict, Any, Optional
from .errors import DestinationNotFoundError, DestinationDisabledError, DestinationRegistryError


def load_destination_registry(registry_file_path: str) -> Dict[str, Any]:
    """Load destination registry from YAML file."""
    try:
        with open(registry_file_path, "r") as f:
            registry = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise DestinationRegistryError(f"Destination registry YAML is malformed: {e}")
    except Exception as e:
        raise DestinationRegistryError(f"Cannot read destination registry: {e}")

    if not isinstance(registry, dict):
        raise DestinationRegistryError("Destination registry must be a dictionary")

    # Validate schema_version
    if registry.get("schema_version") != "1.0":
        raise DestinationRegistryError("schema_version must be exactly '1.0'")

    # Destinations must be array
    if not isinstance(registry.get("destinations"), list):
        raise DestinationRegistryError("destinations must be an array")

    return registry


def validate_destination_record(destination: Dict[str, Any], index: int = 0) -> None:
    """Validate a single destination registry record."""
    if not isinstance(destination, dict):
        raise DestinationRegistryError(f"Destination {index} must be dictionary")

    required_fields = ["destination_id", "domain", "platform", "enabled", "adapter", "auth"]
    for field in required_fields:
        if field not in destination:
            raise DestinationRegistryError(f"Destination {index}: missing required field '{field}'")

    # destination_id must be string
    if not isinstance(destination.get("destination_id"), str):
        raise DestinationRegistryError(f"Destination {index}: destination_id must be string")

    # enabled must be boolean
    if not isinstance(destination.get("enabled"), bool):
        raise DestinationRegistryError(f"Destination {index}: enabled must be boolean")

    # adapter must be string
    if not isinstance(destination.get("adapter"), str):
        raise DestinationRegistryError(f"Destination {index}: adapter must be string")

    # auth must be dict with method and secret_refs
    auth = destination.get("auth")
    if not isinstance(auth, dict):
        raise DestinationRegistryError(f"Destination {index}: auth must be dictionary")
    if "method" not in auth or not isinstance(auth["method"], str):
        raise DestinationRegistryError(f"Destination {index}: auth.method is required and must be string")
    if "secret_refs" not in auth or not isinstance(auth["secret_refs"], list):
        raise DestinationRegistryError(f"Destination {index}: auth.secret_refs must be array")


def resolve_destination(
    registry_file_path: str,
    destination_id: str,
) -> Dict[str, Any]:
    """
    Resolve a destination from registry.

    Args:
        registry_file_path: Path to destination registry
        destination_id: Destination ID to resolve

    Returns:
        Destination record (without secret values)

    Raises:
        DestinationNotFoundError: Destination not in registry
        DestinationDisabledError: Destination is disabled
        DestinationRegistryError: Registry is malformed
    """
    registry = load_destination_registry(registry_file_path)

    destinations = registry.get("destinations", [])
    for index, dest in enumerate(destinations):
        try:
            validate_destination_record(dest, index)
        except DestinationRegistryError:
            raise

        if dest.get("destination_id") == destination_id:
            # Found it
            if not dest.get("enabled"):
                raise DestinationDisabledError(
                    f"Destination '{destination_id}' is registered but disabled",
                    {"destination_id": destination_id},
                )

            # Return destination without exposing secret values
            return {
                "destination_id": dest.get("destination_id"),
                "domain": dest.get("domain"),
                "platform": dest.get("platform"),
                "adapter": dest.get("adapter"),
                "account_ref": dest.get("account_ref"),
                "auth": {
                    "method": dest["auth"].get("method"),
                    "secret_refs": dest["auth"].get("secret_refs", []),
                },
                "permissions": dest.get("permissions", []),
                "verification": dest.get("verification"),
            }

    raise DestinationNotFoundError(
        f"Destination '{destination_id}' not found in registry",
        {"destination_id": destination_id},
    )


def get_all_destinations(registry_file_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Get all destinations from registry as a mapping.

    Returns dict mapping destination_id -> destination record (enabled and disabled).
    """
    registry = load_destination_registry(registry_file_path)
    destinations = {}

    for index, dest in enumerate(registry.get("destinations", [])):
        try:
            validate_destination_record(dest, index)
        except DestinationRegistryError:
            raise

        dest_id = dest.get("destination_id")
        destinations[dest_id] = {
            "destination_id": dest_id,
            "domain": dest.get("domain"),
            "platform": dest.get("platform"),
            "enabled": dest.get("enabled"),
            "adapter": dest.get("adapter"),
            "account_ref": dest.get("account_ref"),
            "auth": {
                "method": dest["auth"].get("method"),
                "secret_refs": dest["auth"].get("secret_refs", []),
            },
            "permissions": dest.get("permissions", []),
            "verification": dest.get("verification"),
        }

    return destinations


def validate_destinations_exist(registry_file_path: str, destination_ids: list) -> None:
    """
    Validate that all requested destinations exist in registry.

    Raises DestinationNotFoundError if any destination is missing.
    """
    for dest_id in destination_ids:
        try:
            # Try to resolve, but don't fail if disabled
            registry = load_destination_registry(registry_file_path)
            destinations = registry.get("destinations", [])
            found = False
            for dest in destinations:
                if dest.get("destination_id") == dest_id:
                    found = True
                    break
            if not found:
                raise DestinationNotFoundError(
                    f"Destination '{dest_id}' not found in registry",
                    {"destination_id": dest_id},
                )
        except DestinationRegistryError:
            raise
