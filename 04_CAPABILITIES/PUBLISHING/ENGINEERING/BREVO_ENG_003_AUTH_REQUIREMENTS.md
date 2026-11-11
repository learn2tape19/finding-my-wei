# PCP-ENG-003 — Brevo Authentication Requirements (Pre-Engineering Update)

**Status:** AUTHORITATIVE DESIGN INPUT — NOT IMPLEMENTED
**Reviewed:** 2026-11-11
**Scope:** `brevo_v1` candidate; no production migration authorized.

## Official sources

- https://developers.brevo.com/docs/oauth-m2m-authentication
- https://developers.brevo.com/changelog/2026/10/13
- https://developers.brevo.com/changelog/2026/10/6
- https://developers.brevo.com/guides/python/changelog

## Decision

For new institutional server-to-server Brevo adapters, **evaluate and prefer OAuth 2.0 machine-to-machine** (`client_credentials`) rather than a broad, long-lived API key when the required campaign operations/scopes are supported.

Do not conflate this design requirement with a completed installation or a production credential change.

### OAuth specifics

- OAuth grant: `client_credentials`.
- Recommended token endpoint: `https://api.brevo.com/realms/partner/oauth/token`.
- `client_id` and `client_secret` are **runtime secrets**, stored outside Git.
- Access token is short-lived (approximately one hour) and is obtained for execution; no refresh token is issued for this grant. Request a new token through the authorized client-credentials flow when needed.
- Every token request **MUST declare explicit `scope`**. If omitted, Brevo grants all scopes that the M2M application already possesses.
- `400 invalid_scope` is a configuration/authorization failure, **not** a transient retry and **not** permission to request broader scopes automatically.
- Required scopes must be mapped to the **actual approved actions**: campaign creation, readback, scheduling/sending and any specifically approved audience/list lookup. Do not guess scope strings; confirm official values from Brevo's current documentation and test least-privilege access.
- Keep dry-run/test credentials separate from production, and never put an access token/client secret into payload, receipt, logs, PRs or committed fixtures.

### SDK/runner selection

- Compare a small direct HTTP implementation with the **official Brevo Python SDK** available at engineering time, including its scoped OAuth M2M support, dependency footprint, version-pinning, maintenance and failure/receipt handling.
- Prefer the cleanest auditable supported implementation; do not add third-party automation middleware without documented benefit.
- Document required account setup and whether Brevo M2M is available to the relevant account. If unavailable, an API-key fallback may be **proposed** with limited operations, managed secrets and a documented risk decision, but must not be silently activated.
- Avoid deprecated bulk contacts `POST /contacts/batch`; use current documented import API if contact imports ever become part of an approved scope. Contact management is *out of scope* for the initial campaign sender unless specifically authorized.

## Acceptance tests

1. Token request includes explicit least-privilege `scope`.
2. Missing scope input is rejected locally before network call.
3. Unauthorized scope returns fail-closed error; does not broaden permissions.
4. Short-lived token is renewed through client-credentials flow when expired, without another Founder publication approval.
5. Invalid client secret and revoked app fail closed with redacted logs.
6. API calls retain exact approved campaign payload, sender, audience, time and metadata.
7. No unapproved audience expansion or contact import.
8. Campaign creation, scheduling/sending and verified receipt are separately tested with mocked responses and a staging/test pathway.
9. Current control-plane approval/hash gate and PCP-ENG-001 regressions remain green.
10. No live send before a properly scoped, Founder-approved certification/launch gate.

## Scope of this update

This updates **future engineering requirements and candidate registry metadata only**. It does NOT modify the accepted WordPress adapter, enable a destination, create Brevo applications/tokens, or send email.
