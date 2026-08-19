# Runner Stewardship Standard

**Status:** AUTHORITATIVE — v1.0  
**Authority:** Founder → Finding My Wei → Capabilities → Publishing  
**Applies to:** All remote publishing runners, adapters, GitHub Actions, SDKs, APIs, and deployment dependencies

## Purpose

Prevent the Publishing Control Plane from becoming stale, insecure, abandoned, unnecessarily complex, or dependent on obsolete platform interfaces.

The institution will continuously evaluate the machinery used to deploy Founder-approved work while protecting production stability.

**Principle:** Current without becoming experimental.

## Lifecycle

`DISCOVER → EVALUATE → SANDBOX → VERIFY → PROMOTE → MONITOR → RETIRE`

Discovery does not authorize adoption. Adoption does not authorize production deployment until verification is complete.

## Selection Priority

For every destination, prefer in this order when practical:

1. Official platform API or officially maintained integration.
2. Small purpose-built institutional adapter against the official API.
3. Mature, auditable, actively maintained third-party GitHub Action/runner.
4. Fork-and-harden an otherwise suitable open-source runner.
5. Additional middleware only when it materially reduces risk or complexity.

Popularity alone is not an adoption criterion.

## Runner Evaluation Scorecard

Every candidate is evaluated for:

- official/supported access path;
- maintenance activity and release recency;
- security advisories and vulnerability history;
- maintainer continuity/bus factor;
- dependency count and dependency health;
- permission scope required;
- secret handling;
- deterministic behavior;
- idempotency/duplicate-post protection;
- logging and deployment receipt support;
- testability;
- rollback capability;
- platform API/version compatibility;
- licensing;
- operational complexity;
- vendor lock-in;
- ability to pin immutable versions/commit SHAs;
- evidence of abandoned/deprecated interfaces.

The cleanest runner is the one that accomplishes the authorized task with the fewest trustworthy moving parts, not necessarily the newest or shortest implementation.

## Continuous Freshness Review

Runner health is reviewed on two tracks.

### Event-Driven Review
Triggered by:
- platform API deprecation or version announcement;
- security advisory;
- runner/action archival;
- material dependency vulnerability;
- authentication model change;
- repeated production failures;
- material permission expansion;
- new official publishing capability that may simplify the stack.

### Scheduled Review
At least monthly, the Steward reviews the active runner inventory for:
- newer official interfaces;
- meaningful runner releases;
- maintenance inactivity;
- dependency/security changes;
- GitHub Actions/runtime deprecations;
- API version deadlines;
- cleaner alternatives.

Quarterly, perform a deeper architecture review of every production adapter.

## No Silent Production Upgrades

The Steward may discover, research, test, benchmark, and sandbox alternatives without Founder approval.

The Steward MUST NOT silently replace a production runner merely because a newer option exists.

Promotion requires:
- functional parity for all required operations;
- security review;
- permission comparison;
- secret-handling review;
- staging deployment;
- verification/readback test;
- duplicate-post/idempotency test;
- deployment receipt validation;
- rollback plan;
- documented recommendation.

If the replacement changes public output, destination, audience, or Founder-approved payload, normal Founder launch approval rules apply.

Infrastructure-only upgrades that preserve the approved public payload may be promoted under Steward authority after the above verification, unless they materially expand permissions or risk.

## Production Pinning

Third-party Actions and dependencies should be pinned to immutable commit SHAs or otherwise reproducible versions wherever practical.

Do not depend on floating tags such as `latest` for production publication machinery.

Version updates are deliberate changes, tested before promotion.

## Runner Registry

Maintain a machine-readable inventory for every active runner with:
- runner ID;
- destination/platform;
- implementation type;
- repository/package/source;
- pinned version/SHA;
- upstream project;
- official vs third-party status;
- required scopes;
- production status;
- last reviewed date;
- last successful production execution;
- current API version;
- known deprecation date;
- replacement candidate, if any;
- rollback target.

## Steward Reporting

Routine reviews should be quiet when nothing meaningful changed.

Create a recommendation when there is an actionable finding such as:
- security issue;
- approaching deprecation;
- abandoned runner;
- significantly cleaner official path;
- reduced-permission alternative;
- reliability improvement;
- required migration.

Do not create noise for cosmetic releases or novelty.

## Security Boundary

No runner may be adopted because it claims to bypass platform access restrictions.

The system uses supported APIs, OAuth/application authorization, managed credentials, and legitimate remote execution. CAPTCHA, MFA, anti-bot systems, account controls, and platform security are not to be defeated.

## Definition of Healthy

A production runner is healthy when it is:
- supported by the current platform interface;
- securely authenticated;
- minimally permissioned;
- reproducibly pinned;
- actively monitored;
- recently verified;
- capable of deterministic deployment and receipt generation;
- replaceable through a documented rollback/migration path.

## Founder Role

The Founder retains final authority over public launches and material changes in institutional risk or permission posture.

The Founder is not responsible for manually tracking runner releases, API deprecations, GitHub ecosystem changes, or dependency freshness. That is a Stewardship responsibility of the Publishing capability.
