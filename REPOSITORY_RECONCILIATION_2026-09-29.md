# Finding My Wei — Repository Reconciliation

## Date
September 29, 2026

## Status
Founder-authorized reconciliation in progress

## Authority
Drew Freedman

---

# Purpose

This reconciliation compares the repository's inherited architecture with the system that is demonstrably operating in September 2026.

It applies the Founder-approved architectural rule:

> **Integration over Reorganization.**

The objective is not to create another architecture. It is to identify canonical homes, remove ambiguity from navigation, preserve history, and retire transitional structures only when their content has been accounted for.

---

# Safety Boundary

A preservation branch was created before destructive cleanup:

`archive/pre-reconciliation-2026-09-29`

Implementation work is isolated on:

`reconciliation-2026-09-29`

No active campaign assets or production schedules are to be altered by this reconciliation.

---

# Classification Standard

## KEEP
Valid content already living in a defensible canonical location.

## PROMOTE
Content or practice proven by real use that should become an explicit canonical reference.

## ARCHIVE
Historically meaningful material that should remain available but should no longer present itself as current operating doctrine.

## RETIRE
Transitional or duplicate material whose knowledge has been preserved elsewhere and which should no longer function as a live navigation or operating surface.

---

# Findings

## KEEP

- `00_Constitution/` as the current ratified constitutional/governance body pending individual conflict resolution.
- `00_CONSTITUTION/` architecture-engineering documents as an approved implementation layer; capitalization alone is not grounds for destructive consolidation.
- `01_OPERATING_SYSTEM/` as the current operational home.
- `02_PROJECT_ATLAS/` as the research capability.
- `03_INTELLECTUAL_ESTATE/` as preservation layer.
- `04_CAPABILITIES/` as shared capabilities.
- `05_DOMAINS/` as domain organization where still referenced by the current estate.
- `07_MARKETING/` because it contains active campaign production, including the working Tao Issue pipeline. Its June classification as merely transitional is superseded by real-world use.
- `00_EXECUTIVE/` as historical and operational executive material, but its older status claims must not override the current root navigation or `OPERATING_STATE.md`.

## PROMOTE

- `START_HERE.md` — canonical human entry point.
- `OPERATING_STATE.md` — canonical current attention/state layer.
- `SUCCESSION_BRIEF.md` — canonical continuity entry point.
- `01_OPERATING_SYSTEM/PRODUCTION_PLAYBOOK.md` — canonical reusable deployment playbook proven by Issues 013 and 014.
- The Issue 013/014 pattern of bounded Founder gates, independent reconciliation, explicit evidence states, and execution receipts.

## ARCHIVE

The following are valuable as design or intellectual history but should not compete with current navigation or current operating doctrine:

- `02_Core_Principles/`
- `03_Universal_Insight_Processor/`
- `04_Decision_Framework/`
- `05_Reflection_Engine/`
- superseded architecture/design documents at root identified by the June reconciliation
- old project snapshots in `_projects/`
- obsolete Notion/OpenClaw synchronization instructions when no longer part of the live system
- legacy operating documents in `_system/` that contain historical value after their current knowledge has been reconciled

Archive means preserve, not erase.

## RETIRE

- `_system/` as a live operating-system location after its surviving knowledge is reconciled into `01_OPERATING_SYSTEM/` or preserved in archive.
- `_projects/` as a live project-status system after snapshots are preserved.
- `_support/` as a catch-all location after its two known assets receive canonical homes or archival status.
- duplicate `INDEX.md` / `PROJECTS_MAP.md` navigation patterns superseded by `START_HERE.md`, README navigation, and current domain/campaign records.
- redundant March backup sets where Git history and a preservation ref already retain the state and no unique content is found.

---

# Material Change From the June Reconciliation

The June 30 report classified `07_MARKETING/` largely as transitional content to be moved into Project Atlas.

That recommendation is no longer valid as a blanket rule.

By September, `07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/` contains the live production record for the Tao publication system. Issues 013 and 014 demonstrate that this area is operational, auditable, and productive.

Therefore:

**Do not migrate active campaign production merely to satisfy the June folder model.**

Preserve the working campaign structure and improve navigation around it.

---

# Operating-System Conflict

The repository currently contains both:

- `01_OPERATING_SYSTEM/` — current operational layer
- `03_OPERATING_SYSTEM/` — an older operating-system generation containing standards and Tao brand assets

`03_OPERATING_SYSTEM/` contains valuable intellectual material, including the Knowledge Production Pipeline, publication success criteria, governance principles, and Tao visual identity material. It must not be deleted as a unit.

The canonical resolution is:

1. Treat `01_OPERATING_SYSTEM/` as the current operational home.
2. Reconcile still-valid standards from `03_OPERATING_SYSTEM/STANDARDS/` against newer doctrine before moving or archiving them.
3. Move domain-specific brand assets to their appropriate domain/capability only after confirming references.
4. Retire `03_OPERATING_SYSTEM/` only after every asset has a verified destination.

---

# Constitutional Case-Variant Conflict

Both `00_CONSTITUTION/` and `00_Constitution/` contain meaningful Founder-approved material.

This is not a safe case-only rename problem.

`00_Constitution/CONSTITUTION.md` is the ratified June Constitution, while `00_CONSTITUTION/REPOSITORY_ARCHITECTURE.md` is an August Founder-approved engineering specification that explicitly requires integration over reorganization and preservation of validated structures.

Therefore both remain in place during this reconciliation. Canonical cross-references will be clarified before any folder-level consolidation is attempted.

---

# Rest / Dormancy Resolution

The estate now recognizes DORMANT as a healthy operational state.

No AI collaborator, dashboard, project, or workflow should generate maintenance work solely because an asset exists.

Quarterly stewardship review is sufficient for intentionally quiet work unless a meaningful external trigger requires action.

---

# Definition of Done

This reconciliation is complete when:

- current navigation points to current doctrine;
- legacy structures no longer masquerade as active systems;
- every retired location has had its unique knowledge accounted for;
- active campaign production remains undisturbed;
- canonical conflicts are explicit rather than hidden;
- historical material remains recoverable through Git and documented archive paths;
- the repository is simpler to enter than it was before the reconciliation.

---

# Current Verdict

The repository does not need a new architecture.

It needs completion of the transition from architecture-building to evidence-driven operation.

The working system is being preserved. The obsolete scaffolding is being demoted carefully rather than erased blindly.
