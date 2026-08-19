# REMOTE PUBLISHING AGENT ARCHITECTURE

**Status:** FOUNDER DIRECTIVE — ARCHITECTURE ESTABLISHED  
**Authority:** Drew Freedman, Founder  
**Applies to:** All Finding My Wei domains, brands, publications, client work, websites, social channels, email systems, and future distribution surfaces  
**Service layer:** `04_CAPABILITIES/PUBLISHING/`

## 1. Purpose

Create a single, repeatable publishing system in which Founder-approved work moves from canonical GitHub authority to its intended destinations without repeated manual permission prompts, repeated file handling, copy/paste deployment, or platform-by-platform improvisation.

The system must be operationally frictionless while remaining institutionally constrained.

The Founder retains final launch approval. After that approval, authorized remote publishing agents may execute the approved deployment plan without requesting additional editorial approval unless a material conflict, credential failure, destination-policy restriction, or content mismatch is detected.

## 2. Governing Principle

**Founder approves once. Agents execute many.**

No publishing agent may create new editorial authority. Agents distribute what has already been approved.

The system must never confuse operational autonomy with editorial autonomy.

## 3. Authority Chain

Founder → Canonical GitHub Package → QA Gate → Founder Launch Approval → Deployment Orchestrator → Destination Agents → Live Verification → Deployment Receipt → GitHub Archive

### Founder
- Holds final approval authority.
- Approves the complete launch package, not each mechanical deployment step.
- May revoke or supersede approval at any time before publication.

### Architect
- Defines publishing standards, schemas, interfaces, approval logic, QA, and destination requirements.
- Does not silently modify Founder-approved content during deployment.

### Repository Steward / Claude
- Reads canonical production authority from GitHub.
- Confirms package completeness.
- Builds or invokes the deployment manifest.
- Routes approved materials to authorized destination agents.
- Collects verification results and writes deployment receipts back to GitHub.
- Stops when authority is unclear.

### Remote Publishing Agents
- Are destination-specific executors.
- Receive exact approved copy, media, metadata, timing, account/destination, and expected verification rules.
- May format only where a platform mechanically requires it and where transformation rules are pre-authorized.
- May not rewrite, substitute, embellish, summarize, redesign, or improvise approved content.

## 4. No-Repeated-Approval Model

The system uses one human approval gate per launch package.

A package moves through these states:

`DRAFT → PRODUCTION_READY → QA_PASSED → FOUNDER_APPROVED → DEPLOYABLE → PUBLISHED → VERIFIED → ARCHIVED`

Only the Founder may create the `FOUNDER_APPROVED` state.

Once `FOUNDER_APPROVED` is present and the package hash has not changed, deployment agents may execute all approved destinations without additional human approval.

Any content change after Founder approval invalidates the approval hash and returns the package to `PRODUCTION_READY` or `QA_PASSED` as appropriate.

## 5. Canonical Launch Package

Every launchable unit must contain or reference:

- canonical body/article/content source
- final platform-specific copy
- final visual/media assets
- alt text/accessibility copy
- SEO metadata where applicable
- categories/tags/hashtags where applicable
- email subject, preview, sender profile, audience/segment where applicable
- destination registry keys
- scheduled publication date/time
- CTA and target URLs
- approved transformations, if any
- QA checklist and result
- Founder approval record
- immutable package/content hashes
- deployment manifest

No agent should need to infer any of these from conversation history.

## 6. Deployment Manifest

Each launch package must contain a machine-readable deployment manifest defining exactly where every item goes.

Required fields:

- `package_id`
- `domain`
- `campaign_or_project`
- `canonical_commit`
- `approval_status`
- `approval_timestamp`
- `approved_by`
- `package_hash`
- `destinations[]`
- `destination.account_key`
- `destination.channel`
- `destination.asset`
- `destination.copy_source`
- `destination.publish_at`
- `destination.url_target`
- `destination.transform_profile`
- `destination.verification_profile`

Agents execute the manifest. They do not construct campaign intent from scratch.

## 7. Remote Agent Connectivity

Remote agents must use authorized integrations capable of operating from hosted infrastructure rather than depending on the Founder's browser session or local computer.

Preferred connection order:

1. Official platform API with OAuth/service authorization.
2. First-party application password or API token where officially supported.
3. Approved scheduling/distribution service with official downstream integrations.
4. Managed browser automation only when the destination explicitly permits automated access and no supported API path exists.

The architecture does **not** authorize bypassing CAPTCHAs, MFA, anti-bot controls, account-security systems, rate limits, access restrictions, or platform terms. "Unencumbered" means pre-authorized and properly integrated, not circumventing security controls.

## 8. Credential Architecture

Credentials never live in canonical content files or committed repository text.

Use GitHub Environments / Actions Secrets or an equivalent managed secret store.

Each destination receives a named credential profile with least privilege, for example:

- `WORDPRESS_TAO_PROD`
- `WORDPRESS_LEARN2TAPE_PROD`
- `META_TAO_PROD`
- `LINKEDIN_TAO_PROD`
- `BREVO_LEARN2TAPE_PROD`

Credential profiles may persist across launches so the Founder is not asked to reauthorize routine deployments.

Reauthorization is required only when a provider expires/revokes credentials, changes scope, requires renewed consent, or the Founder intentionally removes access.

## 9. Destination Adapter Standard

Every destination agent implements the same contract:

### INPUT
- canonical package ID
- exact content/media references
- account key
- destination/channel
- schedule
- transform profile
- verification profile

### EXECUTE
- authenticate through managed credential profile
- upload required media
- create draft/scheduled/live object as instructed
- apply exact approved copy and metadata
- preserve links, tags, alt text, categories, and timing

### OUTPUT
- success/failure state
- platform object ID
- live or preview URL when available
- publication/schedule timestamp
- media IDs
- API response summary
- verification result
- error class if failed

No adapter returns "success" merely because an API accepted a request. It must verify the resulting object where the platform permits verification.

## 10. Initial Destination Classes

This architecture is designed to support all current and future work through reusable adapters, including:

### Websites / CMS
- WordPress publishing
- WordPress media library
- SEO metadata
- featured image / OG image
- categories/tags
- scheduled publication
- page/post verification

### Social
- Instagram Feed
- Instagram Stories where API/account capability permits
- Facebook Pages
- LinkedIn
- future approved social channels
- optional scheduler hub such as Buffer when it reduces adapter complexity without sacrificing control

### Email
- Brevo or other approved sender
- campaign creation
- sender identity
- audience/segment selection
- subject/preview/body
- scheduled send
- test/render verification
- campaign ID and send receipt

### Distribution / Other
- Substack or newsletter platforms where authorized integration exists
- podcast/video publishing systems
- ecommerce announcements
- event and course marketing systems
- client-domain publishing destinations

## 11. Domain Independence

The publishing capability belongs to `04_CAPABILITIES`, not to any single brand.

Each domain supplies its own destination registry and brand/content rules while consuming the same publishing engine.

Examples include:

- The Tao of Clinical Touch
- Learn2Tape
- Boston Bodyworker / Drew Freedman professional identity
- StitchCore / Sidekick Air
- Finding My Wei institutional publishing
- Freedman-Foundry client work
- future ventures and publications

A new project should require configuration, not a new publishing architecture.

## 12. Transformation Policy

Platform constraints may require mechanical transformations. These must be predefined.

Examples:
- resize/compress to platform limits
- convert PNG to JPG where required
- shorten metadata fields to hard character limits
- map categories/tags to platform taxonomy
- render approved email HTML from canonical source

Transformations must never alter meaning, headline, visual doctrine, CTA, claim, quotation, or approved editorial intent.

If a required transformation exceeds its approved profile, the agent stops and escalates to the Steward before publishing.

## 13. Verification Gate

Every destination receives a verification profile.

Verification should confirm, where technically available:

- correct account/site
- correct copy
- correct image/media
- correct title/headline
- correct URL/CTA
- correct metadata
- correct alt text
- correct date/time or schedule
- correct visibility/state
- no duplicate publication

Failed verification creates a deployment incident. Agents do not silently retry content changes.

## 14. Deployment Receipt

Every deployment writes a machine-readable receipt back to GitHub containing:

- package ID
- canonical commit
- package hash
- destination
- platform object ID
- URL
- scheduled/published timestamp
- verification state
- agent/version
- API or connector method
- retry count
- failure details if any

The repository therefore records not only what was intended to publish, but what actually published and where.

## 15. Failure Policy

### Retry automatically
Only for known transient conditions such as rate-limit wait, temporary network failure, or service outage, using bounded retries.

### Stop and escalate
- authentication revoked
- permission/scope change
- destination account mismatch
- altered canonical hash
- missing required asset/copy
- platform rejects approved content
- duplicate-object ambiguity
- required transformation outside approved profile
- verification mismatch

Agents must never solve a blocker by changing the approved message without authority.

## 16. Security and Separation of Duties

- GitHub stores authority and manifests.
- Secret store holds credentials.
- Orchestrator routes work.
- Destination agents execute.
- Founder approves launches.
- Deployment receipts prove execution.

No single destination token should grant unnecessary access to unrelated domains.

Client credentials must remain segregated from Founder-owned brands.

Production and testing credentials/environments must be distinct where practical.

## 17. Operational Goal

For the Founder, the desired experience is:

1. Review complete finished launch package.
2. Approve launch once.
3. Publishing system deploys every approved component to every approved destination.
4. Founder receives one consolidated completion report with links, status, and any exceptions.

No repetitive login choreography. No repeated editorial approvals. No manual copy/paste deployment. No uncertainty about which version is live.

## 18. Implementation Sequence

### Phase A — Core Publishing Control Plane
- destination registry schema
- deployment manifest schema
- Founder approval artifact/hash
- deployment receipt schema
- QA gate
- GitHub Environment/Secrets convention

### Phase B — First Production Adapters
- WordPress
- Meta/Facebook/Instagram as supported by official APIs
- LinkedIn
- Brevo

### Phase C — Orchestration
- GitHub Actions or equivalent remote runner
- per-destination jobs
- retry/error handling
- verification jobs
- consolidated launch report

### Phase D — Domain Expansion
- configure each Founder domain
- configure client-domain isolation
- add scheduler/newsletter/video/podcast/ecommerce adapters only as real work requires them

## 19. First Reference Implementation

Issue No. 006 of *The Tao of Clinical Touch* will serve as the first end-to-end reference implementation.

The production precedent already defines canonical content, native assets, metadata, accessibility requirements, platform copy, scheduling, and Founder approval behavior. The publishing layer must consume that authority rather than recreate it.

## 20. Non-Negotiables

- Founder retains final launch approval.
- One Founder approval authorizes the complete unchanged deployment manifest.
- No repeated routine approval prompts after launch approval.
- No agent may create editorial authority.
- No platform security controls may be bypassed.
- Persistent authorized integrations are preferred over interactive logins.
- Credentials never enter committed content.
- Every publication is verified.
- Every deployment is receipted back to GitHub.
- Every domain uses the same architecture with destination-specific configuration.

## 21. Success Condition

The system is successful when a completed Founder-approved package can move from GitHub to all intended publishing destinations remotely, reliably, securely, and verifiably—with the Founder making one launch decision and the system handling the rest.