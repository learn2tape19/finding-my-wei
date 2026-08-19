# Publishing Control Plane — Implementation Roadmap

**Status:** AUTHORITATIVE — v1.0  
**Authority:** Founder → Finding My Wei → Capabilities → Publishing  
**Execution model:** Architect specifies; Repository Steward engineers and verifies; Founder retains final launch approval.

## Objective

Move the Publishing Control Plane from architecture into working infrastructure without weakening the single-approval model or introducing unnecessary middleware.

The reference implementation begins with The Tao of Clinical Touch and must remain reusable across all Founder domains.

## Phase 0 — Preserve Production

Before automation touches any live destination:

- existing manual publishing remains available as rollback;
- no production destination is enabled by default;
- no credential values enter Git;
- no agent may publish without a valid Founder approval object tied to the exact package hash;
- all engineering occurs in test/staging mode until acceptance criteria pass.

## Phase 1 — Core Control Plane

Build these platform-independent components first:

1. `manifest_validator`
   - validates `publication.manifest.json` against schema;
   - verifies all declared asset hashes;
   - rejects undeclared/missing payloads.

2. `package_hasher`
   - generates deterministic SHA-256 identity for the launch package;
   - excludes mutable operational receipts from the approved package hash;
   - produces reproducible output locally and remotely.

3. `approval_gate`
   - validates `founder.approval.json`;
   - requires `FOUNDER_APPROVED_FOR_LAUNCH`;
   - requires exact package-hash equality;
   - requires every requested destination to be Founder-approved;
   - fails closed.

4. `destination_resolver`
   - reads destination registry;
   - rejects disabled/unknown destinations;
   - resolves adapter and secret references without exposing secret values.

5. `receipt_writer`
   - creates append-only structured deployment receipts;
   - preserves remote IDs, URLs, timestamps, hashes and verification state;
   - never modifies approved content.

6. `deployment_orchestrator`
   - executes only after approval gate passes;
   - routes exact payload to adapter;
   - handles approved retry classes;
   - prevents duplicate deployment where platform semantics allow.

## Phase 2 — Reference Adapters

Engineering order:

1. WordPress
2. Brevo
3. Meta — Facebook/Instagram
4. LinkedIn

Each adapter implements:

`validate → authenticate → prepare → publish/schedule → verify → receipt`

Each adapter must be independently replaceable.

## Phase 3 — Remote Runner

Use GitHub Actions and/or an approved hosted worker after runner evaluation.

Requirements:

- protected production environment;
- least-privilege permissions;
- secrets supplied only at runtime;
- concurrency lock per publication/destination;
- manual workflow entry for controlled dry runs;
- scheduled execution for approved future publication times;
- artifact/log retention sufficient for diagnosis;
- no shell output of credentials;
- pinned Action dependencies;
- production environment separated from staging.

## Phase 4 — Tao Reference Deployment

Issue No. 006 becomes the reference package only after the entire weekly publication is canonical.

Test sequence:

1. validate package locally;
2. generate hash;
3. create non-production approval fixture;
4. run all adapters in dry-run mode;
5. publish to staging/test destinations where available;
6. verify readback;
7. generate receipts;
8. test duplicate prevention;
9. test expired-token refresh path;
10. test transient failure/retry;
11. test hash mismatch rejection;
12. test changed payload invalidates approval;
13. test disabled destination rejection;
14. test rollback/manual fallback.

Only after all acceptance tests pass may a production destination be enabled.

## Phase 5 — Domain Expansion

After Tao proves the architecture, register destinations for:

- Learn2Tape;
- Boston Bodyworker;
- StitchCore / Sidekick Air;
- Finding My Wei;
- authorized Freedman-Foundry clients;
- future domains.

Do not fork the control plane per brand. Add configuration, payload templates and destination records.

## Acceptance Criteria

The first production release is complete when:

- a frozen package produces a deterministic hash;
- Founder approval can be validated against that hash;
- no deployment occurs without approval;
- one approval authorizes all manifest-declared destinations;
- exact approved content reaches each enabled destination;
- remote execution does not require the Founder's Mac/browser;
- expected transient failures retry without asking Founder again;
- content-changing failures stop and escalate;
- live/scheduled state is verified;
- deployment receipts are written;
- duplicate execution does not create duplicate public posts where preventable;
- secrets remain outside Git and logs;
- every production runner is registered and reviewed under the Runner Stewardship Standard.

## Engineering Rule

Do not begin by wiring social networks together. Build the approval/hash/receipt spine first. Platform adapters are replaceable edges; Founder authority and canonical package integrity are the permanent center.
