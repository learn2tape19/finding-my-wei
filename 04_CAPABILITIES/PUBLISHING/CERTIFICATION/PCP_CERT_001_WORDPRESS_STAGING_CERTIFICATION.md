# PCP-CERT-001 — WORDPRESS STAGING CERTIFICATION

**Certification ID:** PCP-CERT-001  
**Capability:** Publishing Control Plane  
**Subject:** `wordpress_v1` institutional adapter  
**Status:** READY FOR EXECUTION  
**Authority:** Founder → Finding My Wei → Capabilities → Publishing  
**Execution role:** Repository Steward / Certification Operator  
**Production authority:** NONE

## Purpose

Certify the accepted and frozen WordPress adapter against a real, controlled, non-public WordPress environment before any production WordPress destination is enabled.

This certification is not an engineering redesign and is not permission to publish publicly.

The objective is to prove that the accepted control-plane architecture behaves correctly outside mocks when confronted with an actual WordPress REST API, authentication model, hosting environment, timezone configuration, media library, taxonomy, and readback behavior.

## Frozen Inputs

Treat these accepted components as frozen unless certification exposes a genuine defect:

- PCP-ENG-001 — Publishing Control Plane Core
- PCP-ENG-002 — WordPress REST Adapter
- `04_CAPABILITIES/PUBLISHING/control_plane/`
- `04_CAPABILITIES/PUBLISHING/control_plane/adapters/wordpress_v1.py`
- `04_CAPABILITIES/PUBLISHING/RUNNERS/runner-registry.yaml`
- Publishing schemas and Founder approval model
- Runner Stewardship Standard

Certification findings do not authorize silent changes to frozen architecture.

If a defect is discovered, stop the affected certification path, document the evidence, and request a targeted remediation before continuing.

## Certification Boundary

PCP-CERT-001 MUST use a WordPress destination that is safe for non-public certification.

Acceptable destination:

- dedicated staging WordPress installation; or
- otherwise isolated non-public WordPress environment explicitly designated for certification.

Not acceptable:

- the public Tao of Clinical Touch production site;
- any live production WordPress site;
- a destination where test posts may become publicly discoverable;
- browser automation used to simulate WordPress REST behavior.

No production destination may be enabled as part of this certification.

## Credential Model

Use a dedicated certification identity and WordPress Application Password.

Requirements:

- HTTPS only;
- dedicated certification/publishing user where practical;
- least privilege;
- Application Password unique to this certification/integration;
- credentials supplied at runtime only;
- no credential values committed to Git;
- no credentials written into manifests, fixtures, receipts, logs, screenshots, completion reports, or exception output;
- credentials independently revocable after certification.

The canonical repository stores only secret/configuration references.

## Founder Approval Model During Certification

PCP-CERT-001 MUST exercise the real approval gate, but certification approval is not production launch approval.

Use a clearly labeled certification package and approval fixture tied to the exact certification package hash.

The approval must:

- identify the certification publication ID;
- identify only the staging/certification destination;
- contain the exact computed package hash;
- use the normal `FOUNDER_APPROVED_FOR_LAUNCH` state required by the frozen control plane;
- be unmistakably scoped in publication ID, destination, content, and environment to certification only.

A certification approval MUST NOT be reusable against any production destination.

## Certification Content

Use deliberately non-public test content that cannot be mistaken for a real Tao publication.

Required characteristics:

- title begins with `PCP-CERT-001`;
- body explicitly states `NON-PUBLIC WORDPRESS STAGING CERTIFICATION`;
- unique slug;
- test excerpt;
- one small certification image created specifically for testing;
- explicit alt text;
- pre-existing staging category and tag selected for the test;
- no Issue 006 canonical article or production social copy;
- no production CTA;
- no subscriber/customer communication.

The certification package itself should be preserved as evidence after secrets are excluded.

## Required Preflight Evidence

Before any write operation, execute the real `wordpress_v1` preflight and record non-secret evidence for every mandatory gate.

Prove:

1. HTTPS is enforced.
2. WordPress REST API is reachable.
3. Application Password authentication succeeds.
4. authenticated user identity is the intended certification identity.
5. posts endpoint is readable/usable.
6. media endpoint is readable/usable.
7. categories endpoint is readable.
8. tags endpoint is readable.
9. site identity/base URL matches the declared staging destination.
10. no production destination is being targeted.

If any mandatory preflight gate fails, certification stops before writes.

## Required Live Certification Sequence

Execute the following against the staging destination in order.

### CERT-01 — Control Plane Validation

- validate manifest against schema;
- verify declared asset hash;
- compute deterministic package hash;
- validate certification Founder approval against that exact hash;
- resolve only the enabled staging destination;
- prove a production destination is not resolvable/enabled for this certification package.

**Pass:** exact package and approval relationship is proven before WordPress writes.

### CERT-02 — WordPress Preflight

Run the real adapter preflight against staging.

**Pass:** every mandatory preflight gate succeeds and evidence contains no secrets.

### CERT-03 — Taxonomy Resolution

Resolve the declared pre-existing staging category and tag through live WordPress endpoints.

**Pass:** each resolves deterministically to exactly one WordPress object and no taxonomy is created or modified.

### CERT-04 — Media Upload

Upload the declared certification image.

Verify:

- transmitted MIME type equals manifest-declared media type;
- WordPress returns a media ID;
- alt text equals the approved value after readback;
- returned media URL belongs to staging;
- no production media library is touched.

**Pass:** exact approved media is present and verifiable in staging.

### CERT-05 — Draft Creation

Create the certification post as `draft` using exact approved:

- title;
- slug;
- excerpt;
- body;
- category;
- tag;
- featured media.

Perform authenticated readback.

**Pass:** substantive fields match approved payload and status is draft.

### CERT-06 — Idempotent Retry

Invoke the same approved draft deployment again without changing package identity.

**Pass:** no duplicate WordPress post or media object is created where the adapter's idempotency contract says duplication is preventable; existing verified object is reused/recognized appropriately.

If media idempotency is not currently guaranteed by the frozen adapter, document actual behavior rather than silently extending architecture.

### CERT-07 — Mutation Rejection

Mutate a hashed certification package component locally without updating Founder approval.

Invoke the control-plane deployment path.

**Pass:** package/asset/hash validation fails before any WordPress write occurs.

Restore the original certified package after this negative test.

### CERT-08 — Scheduled Post

Using a separately hashed and certification-approved fixture if required by package semantics, create a staging post with `future` status and an explicit staging-local schedule time safely in the future.

Verify:

- exact requested timestamp transmitted;
- WordPress status is `future`;
- WordPress readback timestamp/timezone behavior is documented;
- staging configuration does not unexpectedly reinterpret the requested time.

After evidence is captured, cancel/delete the scheduled certification object so it cannot later publish accidentally.

**Pass:** schedule semantics are proven and cleanup succeeds.

### CERT-09 — Publish Transition in Non-Public Staging Only

Only if the staging environment is demonstrably non-public, transition/create the certification object with `publish` status.

Verify authenticated readback and returned staging URL.

If staging is externally public or indexable, SKIP THIS WRITE and mark the certification `BLOCKED_ENVIRONMENT` rather than publishing test material publicly. A skipped public-status write due to an unsafe environment is not a software failure; it means a safer staging environment is required before full certification.

**Pass:** publish semantics proven inside a genuinely non-public environment.

### CERT-10 — Verification Receipt

Generate schema-valid deployment receipts containing:

- certification publication ID;
- package hash;
- staging destination ID;
- adapter/agent identity;
- timestamps;
- WordPress remote object ID;
- staging URL where applicable;
- verification state;
- no secrets.

**Pass:** receipt validates against canonical deployment receipt schema.

### CERT-11 — Failure Classification

Against staging or controlled HTTP simulation adjacent to the live test, verify operational classification for:

- invalid/revoked Application Password → `BLOCKED_AUTH`;
- safe transient platform failure → `FAILED_TRANSIENT` only when explicitly recognized;
- unknown/unclassified failure → fail closed / `FAILED_REQUIRES_FOUNDER`.

Do not intentionally damage the staging WordPress installation to manufacture failures.

### CERT-12 — Cleanup

After evidence capture:

- remove certification posts from staging;
- remove certification media when safe;
- remove/cancel scheduled certification objects;
- confirm no certification content remains publicly accessible;
- preserve only non-secret receipts/evidence in the repository;
- optionally revoke the certification Application Password if the credential will not be reused for subsequent staging work.

**Pass:** staging returns to a clean state.

## Production Isolation Test

Certification must explicitly prove that production remains isolated.

At minimum:

- certification manifest declares only staging destination;
- Founder certification approval declares only staging destination;
- production destination remains disabled/unavailable to the certification execution path;
- staging and production base URLs are compared before writes;
- adapter refuses an unexpected site identity/base URL mismatch;
- evidence records staging host without recording credentials.

## Evidence Package

Create certification evidence under:

`04_CAPABILITIES/PUBLISHING/CERTIFICATION/EVIDENCE/PCP-CERT-001/`

Required artifacts:

- `CERTIFICATION_REPORT.md`
- sanitized preflight results;
- certification manifest;
- package hash record;
- certification approval fixture with no secrets;
- sanitized deployment receipts;
- WordPress IDs and staging URLs used during certification;
- cleanup confirmation;
- failures/deviations, if any;
- exact adapter commit SHA certified;
- exact control-plane commit SHA certified;
- certification timestamp;
- operator identity.

Do not commit credentials, Authorization headers, Application Passwords, cookies, or raw HTTP dumps containing secrets.

## Certification States

Use one final state:

- `CERTIFIED` — all mandatory certification requirements passed;
- `CERTIFIED_WITH_DOCUMENTED_LIMITATION` — all safety/integrity requirements passed and a non-critical platform limitation is explicitly accepted by Architect/Founder;
- `BLOCKED_ENVIRONMENT` — staging environment cannot safely prove required behavior;
- `FAILED_ADAPTER` — frozen adapter behavior fails against real WordPress;
- `FAILED_CONTROL_PLANE` — accepted control-plane behavior fails in certification;
- `FAILED_SECURITY` — secret leakage, wrong-destination risk, permission overreach, or other security boundary failure discovered.

Claude/Steward may report the state but may not self-accept a failure or limitation as certified.

## Stop Conditions

STOP immediately and do not continue writes if:

- destination resolves to production unexpectedly;
- HTTPS is not valid;
- site identity does not match staging configuration;
- credentials appear in logs/output;
- authenticated identity is not the intended certification user;
- required permissions are materially broader than declared without explanation;
- package hash or Founder certification approval does not match;
- taxonomy resolution is ambiguous;
- adapter attempts taxonomy creation;
- adapter changes approved editorial content;
- duplicate protection behaves unexpectedly in a way that risks public duplication;
- any test content may become publicly visible outside a demonstrably non-public staging environment.

Record evidence and return for architectural review.

## No Silent Remediation

If real WordPress behavior exposes a defect:

1. stop the affected certification path;
2. preserve sanitized evidence;
3. classify the finding;
4. report the exact observed behavior;
5. propose the smallest remediation;
6. wait for architectural authorization before changing frozen production code.

Do not patch the adapter during certification and then declare the same run certified.

Any code remediation requires a new commit, regression tests, architectural acceptance, and a fresh certification run against the remediated commit.

## Acceptance Criteria

PCP-CERT-001 may be declared `CERTIFIED` only when:

- real staging WordPress preflight passes;
- staging identity is proven before writes;
- real Application Password authentication works without secret leakage;
- live taxonomy resolution is deterministic and read-only;
- real media upload preserves declared MIME type and alt text;
- exact approved draft payload survives WordPress round trip;
- duplicate behavior is understood and safe;
- mutated approved package is rejected before WordPress writes;
- scheduling/timezone semantics are proven and cleaned up;
- publish semantics are proven only in safe non-public staging;
- schema-valid receipts are produced;
- failure classifications remain fail-closed;
- production isolation is proven;
- cleanup is complete;
- evidence package contains no secrets;
- no frozen code was silently modified during the certification run.

## Completion Report

Return:

1. certification state;
2. staging destination identifier and sanitized host;
3. certified control-plane commit SHA;
4. certified WordPress adapter commit SHA;
5. certification package hash;
6. each CERT-01 through CERT-12 result: PASS / FAIL / BLOCKED;
7. WordPress version and relevant staging environment observations;
8. authenticated certification identity (username only; no credential);
9. remote IDs/URLs created, sanitized as needed;
10. deployment receipt validation result;
11. cleanup result;
12. security observations;
13. defects/deviations discovered;
14. whether any code changed during certification;
15. exact recommendation: CERTIFY, REMEDIATE, or REPEAT WITH SAFER STAGING.

## Definition of Done

PCP-CERT-001 is complete when the accepted Publishing Control Plane and frozen `wordpress_v1` adapter have been exercised against a real non-public WordPress environment, the exact approved package has been transported and read back successfully, production isolation has been proven, evidence and receipts have been preserved without secrets, test artifacts have been cleaned up, and the Architect can make a certification decision from evidence rather than from mocks or operator assertions.

## Prohibition

Completion of PCP-CERT-001 does **not** authorize:

- production WordPress activation;
- Tao public publication;
- Issue 006 launch;
- GitHub remote production runner activation;
- Brevo/Meta/LinkedIn deployment;
- bypassing future Founder approval.

Those require their own authorized gates.
