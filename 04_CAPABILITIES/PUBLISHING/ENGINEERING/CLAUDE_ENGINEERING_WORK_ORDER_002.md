# CLAUDE ENGINEERING WORK ORDER 002

**Work Order:** PCP-ENG-002  
**Capability:** Publishing Control Plane — WordPress Adapter  
**Assigned role:** Repository Steward / Engineer  
**Authority:** PCP-ENG-001 accepted and frozen; Founder-approved Publishing architecture on `main`  
**Status:** READY FOR EXECUTION

## Mission

Implement the first real destination adapter for the Finding My Wei Publishing Control Plane: `wordpress_v1`.

The adapter must transport an exact Founder-approved WordPress payload through the official WordPress REST API and return structured verification evidence and deployment receipts.

This work order does **not** authorize a production launch.

**Operating rule:** Founder approves content once. The adapter executes the exact approved state. It has no editorial discretion.

## Governing Sources

Read and treat as authoritative before engineering:

- `04_CAPABILITIES/PUBLISHING/REMOTE_PUBLISHING_AGENT_ARCHITECTURE.md`
- `04_CAPABILITIES/PUBLISHING/CLAUDE_STEWARD_DEPLOYMENT_PROTOCOL.md`
- `04_CAPABILITIES/PUBLISHING/PUBLISHING_CONTROL_PLANE_SPEC.md`
- `04_CAPABILITIES/PUBLISHING/RUNNERS/RUNNER_STEWARDSHIP_STANDARD.md`
- `04_CAPABILITIES/PUBLISHING/RUNNERS/runner-registry.template.yaml`
- `04_CAPABILITIES/PUBLISHING/DESTINATIONS/DESTINATION_REGISTRY.template.yaml`
- `04_CAPABILITIES/PUBLISHING/ENGINEERING/IMPLEMENTATION_ROADMAP.md`
- all accepted PCP-ENG-001 code, schemas, tests, fixtures, and documentation under `04_CAPABILITIES/PUBLISHING/control_plane/`

If this work order conflicts with accepted PCP-ENG-001 behavior, stop and report the conflict. Do not redesign the control plane.

## Runner Decision — LOCKED FOR PCP-ENG-002

The WordPress runner review concluded:

- WordPress interface: **official WordPress REST API — USE**
- Authentication: **WordPress Application Password over HTTPS — USE**
- Adapter: **institutional `wordpress_v1` — BUILD OUR OWN**
- Execution target: **GitHub-hosted Ubuntu runner — future remote-runner work order**
- Third-party WordPress publishing Action: **DO NOT USE**
- WordPress publishing plugin: **DO NOT ADD unless a documented site-specific limitation later proves one necessary**
- Self-hosted runner: **NOT JUSTIFIED**
- Browser automation / CAPTCHA / MFA / anti-bot bypass: **PROHIBITED**

Do not introduce Zapier, Make, browser automation, scraping, a WordPress publishing plugin, or a third-party GitHub publishing Action as a shortcut.

## Official Interface Contract

Use WordPress core REST endpoints where supported, including the appropriate `/wp-json/wp/v2/...` resources for:

- posts;
- media;
- categories;
- tags;
- authenticated user/readback needed for preflight and verification.

Use HTTPS only.

Application Password credentials must be supplied at runtime through secret references/environment injection. They must never appear in Git, fixtures, logs, prompts, receipts, exceptions, or committed configuration.

## Deliverables

Create the adapter cleanly within the existing control-plane implementation. Prefer a structure such as:

`04_CAPABILITIES/PUBLISHING/control_plane/adapters/wordpress_v1.py`

If the accepted PCP-ENG-001 module structure requires a different path, preserve its architecture and document the reason.

Required deliverables:

1. WordPress adapter implementation.
2. WordPress payload validation.
3. Authentication/preflight client.
4. Media upload support.
5. Category/tag resolution.
6. Post create/update/schedule/publish support.
7. Exact-state readback verification.
8. Idempotency/duplicate protection integration.
9. Structured WordPress-specific error mapping into existing institutional states.
10. Unit tests with mocked HTTP responses.
11. Integration-test harness that can run against a configured non-production WordPress site without storing credentials.
12. WordPress adapter documentation.
13. Runner-registry update describing the implemented adapter, dependency/version posture, scopes/capabilities, and review state.

## WordPress Payload Contract

Define and document a machine-readable WordPress payload containing only approved publication state. At minimum support, when declared:

- title;
- content/body;
- excerpt;
- slug;
- status: `draft`, `future`, or `publish` as authorized;
- publication date/time when scheduled;
- featured media asset reference;
- media alt text;
- categories;
- tags;
- author identity/reference when explicitly configured;
- comment/ping status when explicitly configured;
- permitted registered REST metadata only when explicitly declared and supported.

The adapter MUST NOT invent missing editorial fields.

If a required field is absent, ambiguous, unsupported, or conflicts with the target site, fail closed with a structured error.

## Exact-State Rule

The adapter is a transporter, not an editor.

It MUST NOT:

- rewrite headlines;
- rewrite body copy;
- generate excerpts;
- generate or alter slugs;
- choose categories or tags;
- choose an image;
- alter alt text;
- add hashtags;
- change CTA language;
- alter publication status/time;
- change author;
- normalize approved prose in a way that changes public content;
- silently adapt content because WordPress rejects it.

Any public-content change returns to the canonical package and Founder approval process.

## Preflight Requirement

Before any write operation, implement a preflight that proves the configured destination is suitable.

At minimum verify:

1. base URL is HTTPS;
2. WordPress REST API is reachable;
3. authentication succeeds using the configured Application Password;
4. authenticated publishing identity matches configured expectations;
5. required post endpoint is reachable;
6. media endpoint is reachable when media is declared;
7. category/tag endpoints are reachable when taxonomies are declared;
8. credentials possess the capabilities required for the requested operation;
9. destination identity matches the registry entry sufficiently to prevent posting to the wrong site.

Preflight must perform no public publication.

If preflight fails, no content write occurs.

## Authentication and Secret Handling

Expected secret references conceptually include:

- WordPress base URL/configuration reference;
- publishing username/identity reference;
- Application Password secret reference.

Exact names should follow existing repository conventions.

Rules:

- never print the Authorization header;
- never print or persist the Application Password;
- redact credentials from exception text and HTTP diagnostics;
- never commit `.env` files containing credentials;
- use a dedicated publishing identity where configured;
- do not use Drew's ordinary interactive WordPress password;
- do not create credentials automatically in this work order.

## HTTP Client / Dependency Rule

Use the smallest auditable implementation.

Before adding a new HTTP dependency, evaluate Python standard library and existing trusted dependencies. If a dependency such as `requests` is selected, document:

- why it is preferable;
- exact pinned version;
- maintenance/security posture;
- transitive dependency implications;
- why the standard library implementation would be less reliable or maintainable.

No convenience dependency may be introduced without justification.

## Media Upload Behavior

When the approved payload declares media:

- verify local asset hash before upload through the existing control-plane guarantees;
- upload the exact approved file;
- preserve filename where appropriate;
- set declared alt text exactly;
- capture WordPress media ID and source URL;
- verify media readback;
- do not substitute or recompress media unless the canonical package explicitly authorizes a transformation;
- do not silently reuse an unrelated existing media item.

If the same immutable asset was previously uploaded for the same publication/destination and a verified receipt/state can safely identify it, the adapter may reuse that exact remote media object to preserve idempotency.

## Taxonomy Behavior

Categories and tags must be resolved deterministically.

The adapter may:

- resolve an existing exact configured term;
- create a term only if the approved payload/manifest and destination policy explicitly authorize term creation.

The adapter MUST NOT guess between similarly named terms or silently create new taxonomy because resolution failed.

Ambiguity fails closed.

## Create / Update Behavior

The adapter must distinguish between:

- new post creation;
- idempotent retry of the same publication;
- authorized update of the same remote post before launch;
- prohibited mutation of an already-verified post by a different package hash.

Use existing publication/package/destination identity and deployment receipts wherever possible.

A retry must not create duplicate posts merely because the first response was lost after WordPress accepted the request.

Document the exact idempotency strategy.

## Scheduling

For `future` status:

- use the exact approved scheduled time;
- account for WordPress site timezone semantics explicitly;
- do not infer a new time;
- read back and verify the stored scheduled state/time;
- fail closed if the site transforms the requested schedule materially.

No automatic rescheduling outside an already-approved manifest window.

## Verification Standard

A successful HTTP status is not sufficient.

After a create/update/upload operation, perform authenticated readback and verify the fields that the adapter is responsible for.

For posts, verify as applicable:

- remote post ID exists;
- destination/site is correct;
- title;
- body/content identity using a documented canonical comparison that does not mistake harmless WordPress rendering wrappers for editorial changes;
- excerpt;
- slug;
- status;
- scheduled/published time;
- featured media ID;
- categories;
- tags;
- configured author;
- configured comment/ping state;
- canonical link/permalink when available.

For media, verify:

- remote media ID;
- expected filename/source identity where available;
- alt text;
- attachment relationship when applicable.

Verification failures must produce a structured receipt/error and must not be represented as success.

## Error Mapping

Map WordPress failures into existing institutional states. At minimum distinguish:

- authentication/authorization failure → `BLOCKED_AUTH`;
- endpoint/platform incompatibility or unsupported site configuration → `BLOCKED_PLATFORM`;
- explicit rate limiting / timeout / temporary 5xx where retry is safe → `FAILED_TRANSIENT`;
- ambiguous taxonomy, content mismatch, destination mismatch, unsafe duplicate condition, unknown/unclassified failure → fail closed, normally `FAILED_REQUIRES_FOUNDER` unless the existing architecture defines a more precise non-retryable state.

Do not classify all HTTP failures as transient.

## Tests — REQUIRED

No live production credentials are needed for the main suite.

Mocked/unit tests must cover at minimum:

1. HTTPS required;
2. successful preflight;
3. bad credentials fail before writes;
4. wrong-site/destination identity fails before writes;
5. media upload uses exact asset;
6. media alt text exactness;
7. category exact resolution;
8. ambiguous category fails closed;
9. tag exact resolution;
10. unauthorized taxonomy creation rejected;
11. draft post creation;
12. scheduled post creation with exact time;
13. publish post creation;
14. featured media assignment;
15. exact title/slug/excerpt preservation;
16. body verification succeeds for documented harmless REST/rendering normalization only;
17. substantive body mismatch fails verification;
18. safe retry does not duplicate post;
19. conflicting package hash does not mutate existing verified post;
20. 401/403 → `BLOCKED_AUTH`;
21. explicit safe 429/temporary 5xx/timeout → `FAILED_TRANSIENT`;
22. unknown failure → non-retryable fail-closed state;
23. secrets absent from logs/exceptions/receipts;
24. deployment receipt schema-valid;
25. original PCP-ENG-001 complete suite remains green with **0 skipped, 0 failed, 0 errors**.

Tests must exercise behavior, not merely inspect source code.

## Non-Production Integration Harness

Create an opt-in integration harness that runs only when explicit environment configuration is present.

It must:

- target only a configured staging/non-production WordPress destination;
- perform preflight;
- create a clearly identified test draft, not a public production post;
- optionally upload a test fixture media asset;
- read back and verify;
- clean up the test draft/media when safe and configured;
- redact credentials;
- refuse to run if the destination is marked production;
- never run automatically merely because tests are executed.

No real credentials are committed.

## GitHub Actions Boundary

Do **not** build the production remote GitHub Actions deployment workflow in this work order.

PCP-ENG-002 must make `wordpress_v1` runner-ready, but remote production execution belongs to its later dedicated work order after adapters are accepted.

If a small CI-only workflow is proposed for offline tests, it must use least privilege and pin every external Action to a full commit SHA. Do not add such a workflow unless it provides clear value to PCP-ENG-002 acceptance.

## Documentation

Add/update documentation explaining:

- WordPress adapter contract;
- supported endpoints and fields;
- authentication model;
- secret references;
- preflight behavior;
- idempotency strategy;
- taxonomy strategy;
- scheduling/timezone semantics;
- media behavior;
- verification semantics;
- error mapping;
- mocked test execution;
- optional staging integration test execution;
- known WordPress/plugin/hosting compatibility limitations;
- rollback/manual publishing fallback.

## Runner Registry

Update the runner registry to record the actual `wordpress_v1` implementation status.

Record, as applicable:

- implementation type: institutional adapter;
- upstream: official WordPress REST API;
- official interface: true;
- dependency/pinned version information;
- authentication class: Application Password;
- required WordPress capabilities rather than excessive administrator authority;
- review date;
- status: candidate/tested as justified by completed evidence;
- rollback target: manual WordPress publishing until production certification.

Do not mark the adapter production-ready merely because unit tests pass.

## Git Discipline

- Start from current canonical `main` containing accepted PCP-ENG-001.
- Use a dedicated engineering branch for implementation and review where practical.
- Do not modify Issue 006 canonical editorial content.
- Do not alter Founder approval semantics.
- Do not weaken PCP-ENG-001 tests.
- Do not skip tests because a dependency/environment is inconvenient; configure the declared test environment correctly.
- Keep commits coherent and auditable.
- Push completed work to the canonical repository before requesting acceptance.

## Completion Report

Return:

- canonical repository;
- branch;
- full commit SHA(s);
- push/remote verification;
- files created/modified/deleted;
- dependencies added or changed with rationale;
- complete test command(s);
- complete pass/skip/fail/error counts;
- WordPress adapter-specific test results;
- PCP-ENG-001 regression results;
- integration harness status and whether it was actually run;
- any site capabilities/configuration still required before staging;
- known limitations;
- security observations;
- exact recommendation for the next work order.

## Definition of Done

PCP-ENG-002 is complete when the repository proves, without production credentials, that `wordpress_v1` can safely preflight a WordPress destination, consume only exact approved payloads, authenticate through the supported Application Password model, deterministically resolve declared media/taxonomy, create/update/schedule the intended post without duplication, verify the remote state through readback, map failures correctly, protect secrets, generate schema-valid receipts, and preserve every accepted PCP-ENG-001 safety guarantee.

**Do not proceed to Brevo, Meta, LinkedIn, remote production runners, or live WordPress publication until PCP-ENG-002 receives architectural acceptance.**
