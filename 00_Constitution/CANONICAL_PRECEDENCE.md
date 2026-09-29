# Canonical Constitutional Precedence

## Status
Reconciliation authority map

## Date
September 29, 2026

---

# Purpose

Finding My Wei currently contains two case-variant constitutional directories:

- `00_Constitution/`
- `00_CONSTITUTION/`

They represent different architectural generations and cannot both be treated as independently canonical.

This document establishes precedence while unique knowledge is reconciled.

---

# Canonical constitutional home

**`00_Constitution/` is the canonical constitutional layer.**

Reasons:

1. It contains the ratified Repository Constitution v2.0 dated June 30, 2026.
2. Its `CHARTER.md` explicitly identifies the layer as the permanent governing charter and states that it governs all other layers.
3. It contains the broader constitutional corpus: authority, governance, amendment, AI collaboration, stewardship, directives, succession, Project Atlas constitutional doctrine, and related institutional standards.
4. The competing `00_CONSTITUTION/` directory is primarily an FC/ARCH architecture package rather than a complete constitutional layer.

Case is therefore meaningful during reconciliation: `00_Constitution/` is current; `00_CONSTITUTION/` is a later/parallel architecture package whose durable knowledge must be integrated rather than allowed to create a second constitution.

---

# Authority order

Unless a later Founder-ratified amendment explicitly changes it, use this order:

1. Current Founder direction
2. `00_Constitution/CONSTITUTION.md` and formally ratified amendments
3. Other current constitutional standards/directives in `00_Constitution/`, according to their stated authority and date
4. Canonical operating standards in `01_OPERATING_SYSTEM/`
5. Current operating state and approved domain/project evidence
6. Historical or superseded architecture packages as provenance

A document labeled draft, release candidate, work order, implementation specification, or migration plan does not silently override a ratified constitution.

---

# Treatment of `00_CONSTITUTION/`

`00_CONSTITUTION/` is classified as **RECONCILE THEN RETIRE AS A PARALLEL ROOT**.

Its four current files are handled as follows:

## `MASTER_REPOSITORY_MAP.md`

**PROMOTE SELECTIVELY / HISTORICAL ARCHITECTURE EVIDENCE**

The document contains valuable institutional framing, including the mission `Helping People Feel Better`, the concept of Mission Expressions, and the distinction between institutional continuity and product creation.

However, it is explicitly marked `1.0.0-rc1` and `Draft for Founder Ratification` and describes an architecture that differs from the ratified Constitution v2.0.

It therefore cannot independently redefine the permanent repository pillars or organizational model.

Durable concepts should be incorporated through formal constitutional amendment if the Founder wants them to supersede v2.0.

## `REPOSITORY_ARCHITECTURE.md`

**PROMOTE AS IMPLEMENTATION STANDARD**

Its strongest durable doctrine is implementation-level rather than constitutional:

- Integration over Reorganization
- inventory before moving or consolidating content
- one canonical home per document
- cross-reference instead of uncontrolled duplication
- README as navigation rather than governance
- preserve coherent existing naming rather than cosmetic churn

These principles remain valid and already guide the current reconciliation.

They should ultimately live under the canonical operating/architecture standards rather than as a competing constitutional root.

## `ARCH-002_IMPLEMENTATION_SPEC.md`

**ARCHIVE AFTER RECONCILIATION**

Implementation artifact for the parallel architecture program. Preserve as execution history; do not treat as constitutional authority.

## `ARCH-002_WORK_ORDER.md`

**ARCHIVE AFTER RECONCILIATION**

Work-order artifact. Preserve as migration/reconciliation history; it is not enduring doctrine.

---

# Important conflict resolution

The ratified Constitution v2.0 defines four permanent repository pillars and an entity-driven hierarchy.

The FC-001 draft describes Finding My Wei as an Institutional Operating System organized around Mission Expressions.

These ideas may be philosophically compatible, but their directory models are not identical.

Until formally amended, the ratified Constitution controls.

The reconciliation must not convert an unratified architecture proposal into constitutional law merely because it is newer or more detailed.

---

# Current architecture principle

The repository should become simpler through this reconciliation without losing constitutional meaning.

**Constitution defines enduring authority and identity.**

**Operating System defines reusable execution.**

**Operating State defines present attention.**

**Domains preserve enduring bodies of knowledge.**

**Projects/campaigns hold bounded work.**

**Archive preserves provenance without competing for authority.**

---

# Physical cleanup rule

Do not delete or rename the parallel constitutional directory until:

- its four files have been individually reconciled;
- implementation doctrine has a canonical successor;
- references to `00_CONSTITUTION/` have been identified sufficiently to avoid silent breakage;
- Git preservation is verified.

After those conditions are met, `00_CONSTITUTION/` should cease to exist as a live parallel constitutional root.
