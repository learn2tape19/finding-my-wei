# Publishing Control Plane — Implementation

**Status:** COMPLETE — v1.0  
**Architecture:** Platform-independent approval and deployment orchestration  
**Execution model:** Offline validation with pluggable destination adapters

## Overview

The Publishing Control Plane implements the deterministic approval and deployment machinery for Finding My Wei publications across all domains and destinations.

**Core principle:** Founder approves once. Agents execute many.

This implementation provides:
- Deterministic package hashing (SHA-256)
- Founder approval validation gate
- Destination registry resolution
- Deployment receipt generation
- Adapter protocol for destination-specific publishing
- Dry-run adapter for offline testing
- Comprehensive test fixtures and error handling

No real platform credentials, tokens, or live connections are required to validate the control plane. All tests and validation occur offline with schema-validated fixtures.

## Architecture

### Core Modules

#### `errors.py`
Institutional failure states mapped to deployment receipt error classes.

- `HashMismatchError` → HASH_MISMATCH
- `ApprovalStateError` → BLOCKED_FOUNDER_APPROVAL
- `DestinationDisabledError` → BLOCKED_PLATFORM
- `AssetHashMismatchError` → FAILED_REQUIRES_FOUNDER
- And others per institutional policy

#### `manifest.py`
Publication manifest validation against schema.

**Validates:**
- Schema version (1.0)
- Required fields: publication_id, domain, canonical_commit, package_hash, status
- Asset references with SHA-256 hashes
- Destination declarations
- QA status

**Loads:** `publication.manifest.json`

#### `hasher.py`
Deterministic SHA-256 package hashing.

**Produces:** `sha256:<64_hex_chars>` format

**Guarantees:**
- Same package produces same hash locally and remotely
- Operational receipts excluded from hash
- Founder approval files excluded from hash
- Changing any approved public payload changes the hash
- Ordering/serialization produces no accidental drift
- All asset hashes verified against declared values

**Core function:** `compute_package_hash(manifest, manifest_dir)`

#### `approval.py`
Founder approval validation gate.

**Validates:**
- Approval state is exactly `FOUNDER_APPROVED_FOR_LAUNCH`
- Publication IDs match
- Package hashes match exactly
- Requested destination is in approved destinations list
- Founder is "Drew Freedman"

**Fails closed:** Any mismatch rejects deployment.

**Core function:** `check_approval_gate(publication_id, package_hash, requested_destination, approval_file_path)`

**Loads:** `founder.approval.json`

#### `destinations.py`
Destination registry resolution.

**Loads:** Destination registry (YAML)

**Validates:**
- Destination exists in registry
- Destination is enabled (not disabled)
- Destination configuration is complete

**Returns:** Destination record without exposing secret values.

**Core function:** `resolve_destination(registry_file_path, destination_id)`

#### `receipts.py`
Deployment receipt generation and management.

**Creates** schema-valid deployment receipts recording:
- Publication ID and package hash
- Destination and agent
- Remote platform object ID
- Public URL
- Verification results
- Error class and message (if failed)
- Timestamp of deployment attempt

**Detects duplicates** using publication/destination/hash identity to prevent re-publishing the same approved content.

**Core functions:**
- `create_receipt(...)` — creates receipt object
- `write_receipt(receipt, receipt_dir)` — persists to file
- `find_previous_receipt(...)` — detects duplicates

#### `adapters.py`
Adapter protocol and dry-run implementation.

**Contract:** All adapters implement the same lifecycle:
```
validate → authenticate → prepare → publish/schedule → verify → receipt
```

**DestinationAdapter (Abstract Base):**
- `validate(payload, destination)` — ensure compatibility
- `authenticate(credentials)` — establish connection
- `prepare(payload)` — transform if needed
- `publish(payload, destination, schedule_at)` — publish or schedule
- `verify(destination, remote_id, public_url)` — confirm success

**DryRunAdapter:**
- Simulates publishing without touching real platforms
- Proves exact payload reaches adapter unchanged
- Generates fake remote IDs and URLs
- Detects duplicate invocations
- Always succeeds verification (test only)

#### `orchestrator.py`
Deployment orchestrator — ties all components together.

**Workflow:**
1. Load and validate manifest
2. Compute package hash
3. Validate founder approval
4. For each destination:
   - Resolve destination record
   - Check for previous receipt (duplicate prevention)
   - Get adapter (dry-run or real)
   - Execute adapter lifecycle
   - Collect receipt

**Core class:** `DeploymentOrchestrator`

**Core methods:**
- `validate_manifest()` — load and validate
- `validate_approval(manifest)` — check approval against all destinations
- `deploy_to_destination(manifest, destination_id, payload)` — deploy to one destination
- `deploy_all(payload)` — deploy to all approved destinations

## Usage

### Local Test Execution

```python
from control_plane.orchestrator import DeploymentOrchestrator

orchestrator = DeploymentOrchestrator(
    manifest_file="publication.manifest.json",
    approval_file="founder.approval.json",
    destination_registry_file="destination_registry.yaml",
    receipts_dir="./receipts",
)

# Validate everything
manifest = orchestrator.validate_manifest()
approval = orchestrator.validate_approval(manifest)

# Deploy to all approved destinations
payload = {
    "publication_id": manifest["publication_id"],
    "package_hash": manifest["package_hash"],
    # ... actual content payload
}

results = orchestrator.deploy_all(payload)
print(results)
```

### Approval Gate Only

```python
from control_plane.approval import check_approval_gate

approval = check_approval_gate(
    publication_id="issue_006_tao",
    package_hash="sha256:abc123...",
    requested_destination="tao.wordpress.production",
    approval_file_path="founder.approval.json",
)

if approval["state"] == "FOUNDER_APPROVED_FOR_LAUNCH":
    print("✓ Approved for launch")
```

### Hashing and Verification

```python
from control_plane.manifest import load_manifest
from control_plane.hasher import compute_package_hash

manifest = load_manifest("publication.manifest.json")
package_hash = compute_package_hash(manifest, manifest_dir="/path/to/manifest/dir")

print(f"Package hash: {package_hash}")
```

### Duplicate Detection

```python
from control_plane.receipts import find_previous_receipt

previous = find_previous_receipt(
    receipt_dir="./receipts",
    publication_id="issue_006_tao",
    destination_id="tao.wordpress.production",
    package_hash="sha256:abc123...",
)

if previous:
    print(f"Already deployed: {previous['remote_id']}")
```

## Package Hashing Semantics

The package hash is the canonical identity of a publication.

### What is Included in Hash

- `publication_id`
- `domain`
- `canonical_commit`
- `status`
- `publish_at` (if present)
- **Assets** (sorted by ID):
  - id, path, sha256, media_type, alt_text (if present)
- **Destinations** (sorted by destination_id):
  - destination_id, payload_ref, publish_at, schedule_window_minutes
- **QA** (if present):
  - passed, checked_at

### What is Excluded from Hash

- `schema_version` (infrastructure)
- Deployment receipts
- Founder approval files
- Operational timestamps
- Any non-canonical infrastructure metadata

### Hash Immutability

The package hash changes if any approved public payload or asset changes:
- Article body
- Copy/caption
- Image/video assets
- Headlines or quotes
- CTAs or URLs
- Metadata (title, description, alt text)
- Publishing schedule

A changed package hash invalidates founder approval and requires new approval before deployment.

### Determinism Guarantee

The same manifest produces the identical hash locally, on CI, and on remote runners because:
- Canonical JSON serialization (deterministic key ordering)
- Asset hashes verified against files
- No timestamps or runtime state in hash
- No filesystem ordering dependencies

## Approval Gate

The approval gate is the security checkpoint for all deployments.

### Requirements for Passing

1. **Approval state** is exactly `FOUNDER_APPROVED_FOR_LAUNCH` (no other values accepted)
2. **Publication IDs match** between manifest and approval
3. **Package hashes match exactly** — byte-for-byte same SHA-256 identity
4. **Requested destination is in approved destinations list** (approval declares which destinations are approved)
5. **Destination exists and is enabled** in the destination registry

### Fails Closed Policy

Any mismatch rejects deployment:
- Wrong approval state → reject
- Wrong publication ID → reject
- Hash mismatch → reject
- Destination not approved → reject
- Destination disabled → reject

No fallback interpretations. No "close enough" approvals.

## Adapter Contract

Every destination adapter (WordPress, Meta, LinkedIn, Brevo, future) must implement:

### Input
- `publication_id` and `package_hash` for tracking
- Exact approved payload (content, media, metadata, timing, destination)
- Destination record from registry (account ID, auth method reference)
- Optional schedule time for delayed publication

### Execution
- Authenticate using managed credential reference (no secrets in code)
- Upload required media
- Create draft/scheduled/published object with exact approved copy
- Preserve links, tags, alt text, categories, timing
- Apply all metadata exactly as approved
- DO NOT rewrite, substitute, embellish, or improvise content

### Output
- Success/failure status
- Remote platform object ID (post ID, campaign ID, etc.)
- Live or preview URL
- Publication/schedule timestamp
- Verification result
- Error class if failed (maps to institutional state)

### Idempotency
Adapters should detect duplicate invocations using:
- Publication ID
- Destination ID  
- Package hash

When possible, return the existing remote object ID rather than creating a duplicate.

## Receipt Model

A deployment receipt is immutable proof of what was attempted and its outcome.

### Structure

```json
{
  "schema_version": "1.0",
  "publication_id": "issue_006_tao",
  "package_hash": "sha256:abc123...",
  "destination_id": "tao.wordpress.production",
  "agent": "wordpress_v1",
  "attempted_at": "2026-08-10T14:05:00Z",
  "status": "VERIFIED",
  "remote_id": "wp_post_12345",
  "public_url": "https://taoclinicaltouch.com/issue-006-title",
  "verification": {
    "passed": true,
    "checked_at": "2026-08-10T14:06:00Z",
    "details": "Post found at URL with correct metadata"
  },
  "error_class": null,
  "error_message": null
}
```

### Status Values

**Success states:**
- `PUBLISHED` — content is live
- `SCHEDULED` — content is scheduled for future publication
- `VERIFIED` — verification confirmed publication

**Pending states:**
- `QUEUED` — awaiting execution

**Failure states:**
- `FAILED_TRANSIENT` — temporary failure (retry without new approval)
- `BLOCKED_AUTH` — authentication/credential issue
- `BLOCKED_PLATFORM` — platform restriction/capability not available
- `FAILED_REQUIRES_FOUNDER` — content-changing failure (requires new approval)

### Append-Only Log

Receipts are written to files and never modified. Multiple attempts to the same destination create multiple receipt files with different timestamps.

## Security Boundary

### No Credentials in Repository

- Publication manifests contain no secrets
- Founder approval files contain no secrets
- Destination registry contains no secret values, only secret references
- Actual credential values live in GitHub Actions Secrets or managed secret store

### Credential References

Example:
```yaml
auth:
  method: api_key
  secret_refs:
    - "WORDPRESS_TAO_PROD_CREDENTIAL_REF"
```

The orchestrator passes the reference name to the adapter. The adapter resolves it at runtime using the platform's secret store (GitHub Actions environment secrets, etc.).

### Fail Closed

- Invalid/missing credentials → adapter fails and escalates
- Expired tokens → adapter attempts refresh; if refresh fails, escalates
- Insufficient scope → adapter fails without retrying or broadening scope
- Security/MFA/CAPTCHA challenges → escalate to Founder

### No Bypass of Platform Security

Adapters must not:
- Bypass CAPTCHA or MFA
- Circumvent anti-bot controls
- Scrape around an official publishing API
- Defeat access controls
- Broaden OAuth scope without new authorization

## Testing

### Fixtures

Test fixtures provide representative scenarios for validation without mocking:

**Fixtures directory:** `04_CAPABILITIES/PUBLISHING/tests/fixtures/`

1. **manifest_valid_unapproved.json** — Valid manifest in QA status (not approved)
2. **manifest_valid_approved.json** — Valid manifest approved for launch
3. **approval_valid.json** — Matching founder approval for the approved manifest
4. **manifest_malformed.json** — Invalid schema/missing required fields
5. **approval_malformed.json** — Invalid approval (wrong state, wrong approver)
6. **destination_registry.yaml** — Registry with enabled and disabled destinations
7. **receipt_success.json** — Sample successful deployment receipt
8. **receipt_transient_failure.json** — Sample transient failure receipt

### Test Coverage

**test_control_plane.py** includes:

1. ✓ Deterministic hashing — same manifest produces same hash
2. ✓ Hash changes after payload mutation — modifying assets/destinations changes hash
3. ✓ Approval mismatch fails — rejecting hash/ID/state mismatches
4. ✓ Unapproved package fails — rejecting packages without valid approval
5. ✓ Undeclared destination fails — rejecting destinations not in approval
6. ✓ Disabled destination fails — rejecting disabled registry destinations
7. ✓ Valid approved dry-run succeeds — dry-run adapter completes successfully
8. ✓ Receipt conforms to schema — generated receipts match deployment.receipt.schema.json
9. ✓ Duplicate protection works — finding previous receipts prevents re-deployment
10. ✓ Errors map to institutional states — each error has correct error_class

**Run tests:**

```bash
cd /path/to/04_CAPABILITIES/PUBLISHING
python -m pytest tests/test_control_plane.py -v
```

## How Future WordPress/Brevo/Meta/LinkedIn Adapters Plug In

The adapter protocol is designed for replacement.

### Implementing a New Adapter

1. **Subclass `DestinationAdapter`:**
   ```python
   from control_plane.adapters import DestinationAdapter

   class WordPressAdapter(DestinationAdapter):
       def validate(self, payload, destination):
           # WordPress-specific validation
       def authenticate(self, credentials):
           # Use WordPress REST API + app password
       def prepare(self, payload):
           # Transform to WordPress post format if needed
       def publish(self, payload, destination, schedule_at):
           # POST to WordPress API
       def verify(self, destination, remote_id, public_url):
           # GET post and verify title, featured image, etc.
   ```

2. **Register in orchestrator factory:**
   ```python
   def my_adapter_factory(destination_id):
       if destination_id.startswith("wordpress."):
           return WordPressAdapter()
       elif destination_id.startswith("brevo."):
           return BrevoAdapter()
       # ... etc
   ```

3. **Supply via DeploymentOrchestrator:**
   ```python
   orchestrator = DeploymentOrchestrator(
       ...,
       adapter_factory=my_adapter_factory,
   )
   ```

4. **Update destination registry** to reference new adapter:
   ```yaml
   - destination_id: tao.wordpress.production
     platform: wordpress
     adapter: wordpress_v1  # <-- referenced here
   ```

The orchestrator remains unchanged. Each adapter is independently testable, replaceable, and versioned.

## Dependencies

**Standard library only:**
- `json` — manifest/approval/receipt parsing
- `hashlib` — SHA-256 computation
- `pathlib` — filesystem paths
- `datetime` — timestamps
- `abc` — abstract base classes
- `re` — validation patterns

**External dependency (required for destination registry):**
- `PyYAML` — YAML parsing for destination registry

**No:** network libraries, platform SDKs, credential management, or browser automation in the control plane itself. Those belong in adapters.

**Why:** The control plane must remain deterministic, testable offline, and free of platform-specific dependencies.

## Limitations and Future Work

### Known Limitations (v1.0)

1. **Dry-run adapter only** — no real platforms connected
   - WordPress adapter not yet implemented
   - Meta (Facebook/Instagram) adapter not yet implemented
   - LinkedIn adapter not yet implemented
   - Brevo adapter not yet implemented

2. **No remote execution** — orchestration only works locally
   - GitHub Actions integration to follow in Phase 3
   - Managed remote runners to be evaluated

3. **No scheduled retry logic** — failed deployments don't retry
   - Transient failures can be detected from receipts
   - Manual retry by re-running orchestrator with same manifest/approval

4. **Verification is adapter-dependent** — core doesn't enforce verification profiles
   - Each adapter implements its own verification logic
   - Verification profiles defined in destination registry but not enforced here

### Next Work Orders

**PCP-ENG-002: WordPress Adapter**
- Implement full WordPress REST API adapter
- Handle draft, schedule, and publish states
- Verify post content, featured image, metadata
- Test with staging WordPress instance

**PCP-ENG-003: Brevo Email Adapter**
- Implement Brevo API adapter for email campaigns
- Support campaign creation, scheduling, sending
- Verify campaign scheduled/sent state
- Test with Brevo sandbox

**PCP-ENG-004: Meta Adapter**
- Implement Meta API adapter for Facebook/Instagram
- Support feed posts and Stories where available
- Handle media uploads and container creation
- Verify post publication to feed

**PCP-ENG-005: GitHub Actions Remote Runner**
- Implement orchestrator invocation via GitHub Actions
- Secure credential passing via Actions Secrets
- Concurrency control per publication/destination
- Artifact/log retention for audit trail

**PCP-ENG-006: Production Deployment**
- Enable production destinations in registry
- Founder-approved test publication with Issue 006 Tao
- End-to-end deployment to all configured destinations
- Live verification and receipt collection

## Files Created

```
04_CAPABILITIES/PUBLISHING/control_plane/
├── __init__.py
├── errors.py                 — Institutional error classes
├── manifest.py               — Manifest validation
├── hasher.py                 — Deterministic SHA-256 hashing
├── approval.py               — Founder approval gate
├── destinations.py           — Destination registry resolution
├── receipts.py               — Deployment receipt generation
├── adapters.py               — Adapter protocol + dry-run adapter
├── orchestrator.py           — Deployment orchestration
└── README.md                 — This file

04_CAPABILITIES/PUBLISHING/tests/
├── test_control_plane.py     — Comprehensive test suite
└── fixtures/
    ├── manifest_valid_unapproved.json
    ├── manifest_valid_approved.json
    ├── approval_valid.json
    ├── manifest_malformed.json
    ├── approval_malformed.json
    ├── destination_registry.yaml
    ├── receipt_success.json
    └── receipt_transient_failure.json
```

## Acceptance

**Definition of Done:** PCP-ENG-001 is complete when the repository can prove, entirely offline and without platform credentials, that:

✓ An immutable publication package can be hashed deterministically  
✓ Hashes are matched to Founder approvals exactly  
✓ Publications are routed only to approved/enabled destinations  
✓ A dry-run adapter proves payloads reach adapters unchanged  
✓ Duplicate execution is prevented using publication/destination/hash identity  
✓ Deployment outcomes are recorded in schema-valid receipts  
✓ All institutional error states are represented  
✓ All tests pass with comprehensive fixtures  

Ready for Phase 2: WordPress, Meta, LinkedIn, Brevo adapters.
