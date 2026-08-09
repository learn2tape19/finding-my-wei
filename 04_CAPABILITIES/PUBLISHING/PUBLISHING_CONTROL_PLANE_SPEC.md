# Publishing Control Plane Specification

**Status:** AUTHORITATIVE — v1.0  
**Authority:** Founder → Finding My Wei → Capabilities → Publishing  
**Owner:** Founder: Drew Freedman  
**Operational steward:** Claude / Repository Steward  

## 1. Purpose

The Publishing Control Plane (PCP) is the shared enterprise deployment system for every Founder-approved public work.

Its job is to transform an immutable, approved GitHub publication package into verified deployments across configured websites, social networks, email senders, and future destinations without requiring repeated Founder permissions.

**Operating principle:** Founder approves once. Agents execute many.

The Founder retains final launch authority. Operational execution after that approval is delegated to the system.

## 2. System Boundary

The PCP begins only after editorial and production work are complete.

Upstream:
1. Canonical source created.
2. Derivative copy and assets produced.
3. QA completed.
4. Launch package frozen.
5. Package hash generated.
6. Founder gives final approval against that exact package/hash.

Downstream:
1. Steward reads approved manifest.
2. Control plane validates approval and hash.
3. Destination agents receive only their authorized payloads.
4. Agents publish or schedule.
5. Agents verify live state.
6. Deployment receipts return to GitHub.
7. Exceptions are logged and escalated according to policy.

## 3. Non-Negotiable Approval Model

### Founder Approval Gate

A launch may execute only when all are true:
- `status: READY_FOR_FOUNDER_APPROVAL` has passed QA;
- immutable package hash exists;
- Founder changes state to `FOUNDER_APPROVED_FOR_LAUNCH`;
- approved hash equals deployed hash;
- all destinations are registered and enabled.

Founder approval authorizes every destination explicitly declared in that manifest.

The system MUST NOT request separate approval for each destination, upload, scheduling action, retry, verification request, or deployment receipt.

### Approval Invalidators

Founder approval is automatically invalid if any approved payload changes after approval, including:
- article body;
- caption/copy;
- image/video asset;
- hashtags;
- email subject/body;
- target account/site/list;
- publication time;
- audience/privacy state;
- CTA or destination URL.

A changed package receives a new hash and returns to Founder approval.

## 4. Core Repository Objects

Every launch uses these machine-readable objects:

### `publication.manifest.json`
Declares:
- publication ID;
- domain/project;
- canonical source commit;
- assets and hashes;
- platform payloads;
- destinations;
- publish/schedule times;
- dependencies;
- QA status.

### `founder.approval.json`
Declares:
- publication ID;
- approved package hash;
- approval timestamp;
- approval state;
- approved destinations;
- approving authority.

No credentials or secrets appear here.

### `deployment.receipt.json`
Records per destination:
- agent;
- attempt timestamp;
- status;
- remote content/post/message ID;
- canonical public URL when available;
- scheduled/live state;
- verification result;
- payload hash;
- error class if unsuccessful.

Receipts are append-only operational evidence.

## 5. Destination Registry

The enterprise maintains one registry describing available destinations.

Each destination record includes:
- stable destination ID;
- domain/project owner;
- platform;
- account/site/list identifier;
- agent/adapter name;
- authentication method class;
- secret references (never secret values);
- permitted operations;
- supported media/types;
- verification method;
- enabled/disabled state.

A new project should normally require registry configuration, not a new publishing architecture.

## 6. Agent Contract

Every remote publishing agent implements the same lifecycle:

`validate → authenticate → prepare → publish/schedule → verify → receipt`

Agents MUST:
- consume exact approved payloads;
- authenticate using platform-supported credentials/OAuth/application access;
- operate independently of the Founder's laptop/browser session where the platform supports it;
- use persistent or refreshable authorization where legitimately supported;
- preserve platform IDs and URLs;
- be idempotent when possible;
- distinguish transient failures from approval-invalidating failures;
- return structured receipts.

Agents MUST NOT:
- rewrite approved content;
- substitute media;
- change audience/privacy settings;
- broaden permissions;
- defeat CAPTCHA, MFA, anti-bot controls, access controls, or platform security;
- scrape around a blocked official publishing path when that violates platform rules;
- store credentials in the repository.

## 7. Initial Adapter Set

### WordPress Agent
Authorized functions may include:
- create/update draft;
- upload media;
- set featured image;
- apply slug, title, excerpt, categories, tags and alt text;
- schedule/publish;
- verify live URL and rendered metadata.

### Meta Agent
For configured Facebook Pages and Instagram professional accounts through supported Meta interfaces:
- create media containers/uploads where required;
- publish/schedule approved feed content;
- publish supported Story/Reel content when available through the authorized interface;
- capture platform IDs/permalinks;
- verify publication state.

### LinkedIn Agent
For configured member/organization destinations through supported LinkedIn interfaces:
- upload approved media;
- create/schedule supported posts;
- capture remote IDs/URLs;
- verify publication state.

### Email Agent
Initial reference adapter: Brevo.
Authorized functions may include:
- create campaign from approved subject/body/assets;
- select only manifest-declared sender/list/segment;
- schedule/send;
- capture campaign ID;
- verify scheduled/sent state.

## 8. Remote Execution

Execution should occur in managed remote infrastructure, with GitHub Actions and/or approved hosted workers coordinating jobs.

Requirements:
- no dependency on Founder's Mac being awake;
- least-privilege service credentials;
- environment/repository secret stores;
- protected production environment;
- auditable logs;
- retry policy;
- concurrency controls preventing duplicate publication;
- explicit separation of staging/test and production credentials.

## 9. Secret Architecture

GitHub contains secret REFERENCES and configuration only.

Secret values belong in managed secret storage such as:
- GitHub Actions encrypted secrets/environments;
- cloud secret manager;
- destination-native OAuth credential store.

Rules:
- one credential set per service/account boundary when practical;
- minimum scopes;
- refresh tokens rotated/revoked according to provider policy;
- no plaintext secrets in commits, manifests, logs, prompts, issues, or deployment receipts;
- credential failure does not authorize content modification.

## 10. Failure Policy

### Automatic Retry Allowed
Without new Founder approval:
- network timeout;
- temporary 5xx;
- rate limiting using provider guidance;
- token refresh through already-authorized refresh flow;
- delayed media processing;
- verification polling.

### Steward Resolution Allowed
Without new Founder approval when payload remains unchanged:
- re-run failed adapter;
- correct non-content deployment plumbing/configuration;
- replace expired authorization with equivalent approved authorization;
- reschedule within an already-approved scheduling rule when the manifest expressly permits a window.

### Founder Escalation Required
- approved payload must change;
- destination/audience changes;
- platform requires a materially different public presentation;
- security incident;
- account restriction/suspension;
- requested permission scope expands materially;
- deployment cannot be reconciled to the approved package.

## 11. Verification Standard

A successful API response is not sufficient.

Where platform capabilities permit, verification must confirm:
- expected remote ID exists;
- content is live or scheduled as intended;
- expected asset attached;
- expected destination/account;
- expected URL/slug;
- expected publication state;
- approved payload hash maps to deployment receipt.

For web publications, automated checks should also validate title, featured image, metadata/alt text when technically accessible.

## 12. Cross-Domain Use

This capability is shared by all present and future Founder work, including configured publications and campaigns for:
- The Tao of Clinical Touch;
- Learn2Tape;
- The Boston Bodyworker;
- StitchCore / Sidekick Air;
- Finding My Wei;
- Freedman-Foundry client work where the client has authorized deployment;
- future domains registered with the institution.

Domain-specific voice, accounts, schedules and assets live in configuration/manifests. The control plane remains shared.

## 13. Reference State Machine

`DRAFT → PRODUCTION → QA → READY_FOR_FOUNDER_APPROVAL → FOUNDER_APPROVED_FOR_LAUNCH → QUEUED → DEPLOYING → VERIFIED`

Exception states:

`BLOCKED_AUTH | BLOCKED_PLATFORM | FAILED_TRANSIENT | FAILED_REQUIRES_FOUNDER | PARTIALLY_DEPLOYED`

Only the Founder can create `FOUNDER_APPROVED_FOR_LAUNCH` for a new package hash.

## 14. Engineering Order

Implementation sequence:
1. machine-readable schemas;
2. destination registry;
3. package hash + Founder approval gate;
4. deployment receipt writer;
5. WordPress adapter;
6. Brevo adapter;
7. Meta adapter;
8. LinkedIn adapter;
9. remote runner workflows;
10. end-to-end dry run;
11. Founder-controlled production launch.

Issue No. 006 should serve as the first reference publication once its complete weekly package is canonical and Founder-approved.

## 15. Definition of Done

The control plane is operational when a Founder can approve one frozen publication package once, after which authorized remote agents can deploy every declared destination, verify the results, and return complete receipts without additional Founder intervention unless an approval-invalidating condition occurs.
