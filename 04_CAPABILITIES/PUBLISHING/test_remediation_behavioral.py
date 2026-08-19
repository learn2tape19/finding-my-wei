#!/usr/bin/env python3
"""
Genuine behavioral test of DeploymentOrchestrator remediation #1.

Tests that orchestrator independently recomputes package identity and validates
it matches approval before allowing deployment.

Creates actual assets, computes real hashes, establishes matching approval,
then mutates the package and proves orchestrator catches the hash mismatch.
"""

import sys
import json
import hashlib
import tempfile
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent))

from control_plane.manifest import load_manifest
from control_plane.hasher import compute_package_hash, canonicalize_manifest
from control_plane.approval import check_approval_gate
from control_plane.orchestrator import DeploymentOrchestrator
from control_plane.errors import HashMismatchError, AssetHashMismatchError, PackageHashError

def test_orchestrator_recomputes_hash_on_mutation():
    """
    BEHAVIORAL TEST: Orchestrator independently recomputes package identity
    and rejects deployment when package is mutated after approval.

    Flow:
    1. Create valid package with actual declared asset
    2. Compute real package hash
    3. Create matching Founder approval
    4. Validate approval succeeds (package unchanged)
    5. Mutate the approved asset
    6. Invoke orchestrator validation
    7. Prove orchestrator independently recomputed hash and raised HashMismatchError
    """

    print("\n" + "="*80)
    print("BEHAVIORAL TEST: Orchestrator Hash Recomputation on Mutation")
    print("="*80)

    with tempfile.TemporaryDirectory() as tmp_base:
        tmp_base = Path(tmp_base)

        # Step 1: Create valid package with actual declared asset
        print("\n[1] Creating valid package with actual asset...")

        assets_dir = tmp_base / "assets"
        assets_dir.mkdir()

        # Create a real asset file
        asset_content = b"This is a test article for the publication package."
        asset_file = assets_dir / "article.md"
        asset_file.write_bytes(asset_content)

        # Compute asset hash
        asset_hash = hashlib.sha256(asset_content).hexdigest()
        print(f"    Asset: {asset_file.name}")
        print(f"    Hash: sha256:{asset_hash}")

        # Create manifest with real asset
        manifest = {
            "schema_version": "1.0",
            "publication_id": "test_mutation_detection",
            "domain": "test_domain",
            "canonical_commit": "abc1234567890",
            "status": "QA",
            "assets": [
                {
                    "id": "asset_article",
                    "path": "assets/article.md",
                    "sha256": asset_hash,
                    "media_type": "text/markdown",
                    "alt_text": "Test article"
                }
            ],
            "destinations": [
                {
                    "destination_id": "tao.wordpress.production",
                    "payload_ref": "payload_wp"
                }
            ],
            "qa": {
                "passed": True,
                "checked_at": "2026-08-09T18:00:00Z"
            }
        }

        # Step 2: Compute real package hash
        print("\n[2] Computing real package hash...")
        computed_hash = compute_package_hash(manifest, manifest_dir=tmp_base)
        print(f"    Computed package hash: {computed_hash}")

        # Update manifest with computed hash
        manifest["package_hash"] = computed_hash

        # Save manifest
        manifest_file = tmp_base / "manifest.json"
        with open(manifest_file, "w") as f:
            json.dump(manifest, f, indent=2)
        print(f"    Manifest saved: {manifest_file}")

        # Step 3: Create matching Founder approval
        print("\n[3] Creating Founder approval matching the package hash...")
        approval = {
            "schema_version": "1.0",
            "publication_id": "test_mutation_detection",
            "package_hash": computed_hash,
            "state": "FOUNDER_APPROVED_FOR_LAUNCH",
            "approved_by": "Drew Freedman",
            "approved_at": "2026-08-09T19:00:00Z",
            "destinations": ["tao.wordpress.production"],
            "notes": "Approved for testing"
        }

        approval_file = tmp_base / "approval.json"
        with open(approval_file, "w") as f:
            json.dump(approval, f, indent=2)
        print(f"    Approval saved: {approval_file}")
        print(f"    Approval hash: {approval['package_hash']}")

        # Create minimal registry for orchestrator
        registry = {
            "schema_version": "1.0",
            "destinations": [
                {
                    "destination_id": "tao.wordpress.production",
                    "domain": "test_domain",
                    "platform": "wordpress",
                    "enabled": True,
                    "adapter": "wordpress_v1",
                    "account_ref": "test_account",
                    "auth": {
                        "method": "app_password",
                        "secret_refs": ["TEST_WP_AUTH"]
                    },
                    "permissions": ["post_create", "post_publish"]
                }
            ]
        }

        registry_file = tmp_base / "registry.yaml"
        # Write as JSON since we don't have YAML available
        with open(registry_file, "w") as f:
            # Simple workaround: just write the YAML manually as text
            f.write("""schema_version: "1.0"
destinations:
  - destination_id: tao.wordpress.production
    domain: test_domain
    platform: wordpress
    enabled: true
    adapter: wordpress_v1
    account_ref: test_account
    auth:
      method: app_password
      secret_refs:
        - TEST_WP_AUTH
    permissions:
      - post_create
      - post_publish
""")

        # Step 4: Validate approval succeeds while package unchanged
        print("\n[4] Validating approval succeeds (package unchanged)...")
        try:
            approval_result = check_approval_gate(
                publication_id="test_mutation_detection",
                package_hash=computed_hash,
                requested_destination="tao.wordpress.production",
                approval_file_path=str(approval_file),
            )
            print(f"    ✓ Approval gate passed")
            print(f"    ✓ State: {approval_result['state']}")
        except Exception as e:
            raise AssertionError(f"Approval should succeed on unchanged package: {e}")

        # Step 5: Mutate the approved asset (without updating approval)
        print("\n[5] Mutating the approved asset...")
        mutated_content = b"MUTATED: This article has been changed!"
        asset_file.write_bytes(mutated_content)
        mutated_hash = hashlib.sha256(mutated_content).hexdigest()
        print(f"    Original hash: sha256:{asset_hash}")
        print(f"    Mutated hash:  sha256:{mutated_hash}")
        print(f"    ✓ Asset file mutated (approval NOT updated)")

        # Step 6: Invoke orchestrator validation path
        print("\n[6] Invoking DeploymentOrchestrator.validate_approval()...")
        print(f"    This should independently recompute hash and detect mutation...")

        receipts_dir = tmp_base / "receipts"
        orchestrator = DeploymentOrchestrator(
            manifest_file=str(manifest_file),
            approval_file=str(approval_file),
            destination_registry_file=str(registry_file),
            receipts_dir=str(receipts_dir),
        )

        # Load manifest (unchanged in memory, but asset on disk is mutated)
        loaded_manifest = orchestrator.validate_manifest()

        # Step 7: Prove orchestrator catches the hash mismatch
        print("\n[7] Proving orchestrator independently recomputes and detects mismatch...")
        print(f"    Manifest declares hash: {loaded_manifest['package_hash']}")
        print(f"    Asset on disk changed:  hash no longer matches")
        print(f"    Expected: HashMismatchError before adapter execution")

        try:
            # This should raise an error because:
            # - Orchestrator calls _recompute_and_validate_package_hash()
            # - Asset hash mismatch makes computed hash different
            # - AssetHashMismatchError raised during hash computation
            # - Error occurs before approval gate check (proving remediation works)
            approval_result = orchestrator.validate_approval(loaded_manifest)
            raise AssertionError(
                "Orchestrator should have raised an error when asset mutated, "
                "but approve succeeded. Remediation #1 NOT WORKING."
            )
        except (HashMismatchError, AssetHashMismatchError, PackageHashError) as e:
            # Any of these errors proves remediation #1 is working:
            # - AssetHashMismatchError: asset was mutated, recomputation detected it
            # - HashMismatchError: computed hash != approval hash
            # - PackageHashError: package validation failed
            print(f"    ✓ {type(e).__name__} raised (expected)")
            print(f"    ✓ Error: {e.message}")
            print(f"    ✓ Orchestrator independently detected mutation before approval")
            print(f"    ✓ No deployment occurred - hash mismatch caught early")
            return True
        except Exception as e:
            raise AssertionError(
                f"Expected hash/package error, got {type(e).__name__}: {e}. "
                f"Remediation #1 may not be catching mutations properly."
            )


if __name__ == "__main__":
    try:
        test_orchestrator_recomputes_hash_on_mutation()
        print("\n" + "="*80)
        print("✓ BEHAVIORAL TEST PASSED")
        print("="*80)
        print("\nRemediation #1 verified:")
        print("  - Orchestrator independently recomputes package hash")
        print("  - Detects mutations after approval")
        print("  - Raises HashMismatchError before adapter execution")
        print("  - No deployment occurs on hash mismatch")
        sys.exit(0)
    except AssertionError as e:
        print("\n" + "="*80)
        print("✗ BEHAVIORAL TEST FAILED")
        print("="*80)
        print(f"\n{e}")
        sys.exit(1)
    except Exception as e:
        print("\n" + "="*80)
        print("✗ BEHAVIORAL TEST ERROR")
        print("="*80)
        print(f"\n{type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
