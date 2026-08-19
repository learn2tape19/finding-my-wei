# FC-004 — ARCH-002_WORK_ORDER.md

**Institution:** Finding My Wei  
**Document Number:** FC-004  
**Document Class:** Repository Steward Work Order  
**Version:** 1.0.0-rc1  
**Status:** Founder Approved / Authorized for Execution  
**Authority:** Founder  
**Assigned Role:** Repository Steward  
**Canonical Location:** `finding-my-wei/00_CONSTITUTION/ARCH-002_WORK_ORDER.md`

---

# ARCH-002 — Repository Consolidation & Foundation Canon Implementation

## Mission

Implement Foundation Canon v1.0 RC1 exactly as approved.

The Repository Steward shall faithfully execute the architecture established by:

- FC-001 — `MASTER_REPOSITORY_MAP.md`
- FC-002 — `REPOSITORY_ARCHITECTURE.md`
- FC-003 — `ARCH-002_IMPLEMENTATION_SPEC.md`

No constitutional reinterpretation is authorized.

---

# Objective

Organize the Finding My Wei institutional repository ecosystem into a coherent, maintainable, version-controlled operating environment that reflects the approved constitutional architecture while preserving useful existing structure and active work.

---

# Governing Directives

The Repository Steward shall follow these directives throughout ARCH-002:

1. **Integration over Reorganization.**
2. **Repository before Memory.** Canonical truth belongs in version-controlled repositories.
3. **Understanding precedes intervention.** Inventory before migration.
4. Protect active workstreams from unrelated structural changes.
5. Preserve useful existing architecture.
6. Do not create parallel architecture for cosmetic consistency.
7. No force push or history rewrite.
8. No destructive action without Founder approval.
9. No repository creation, renaming, merger, or deletion without Founder approval.
10. Architectural observations belong in `LESSONS_LEARNED.md` unless separately authorized.

---

# Scope of Authority

The Repository Steward **is authorized** to:

- Inspect current repository and branch state.
- Build an actual-state repository inventory.
- Identify canonical sources.
- Identify duplicates and orphaned material.
- Build a current-to-target migration plan.
- Improve README navigation and cross-references where meaning is unchanged.
- Execute non-destructive, Founder-approved migrations.
- Create required ARCH-002 reports.
- Prepare small logical commits.
- Run validation and existing CI/checks where relevant.
- Record implementation lessons without modifying Foundation Canon.

---

# Prohibited Actions

The Repository Steward **is not authorized** to:

- Change constitutional language or intent.
- Introduce new governance concepts.
- Redefine Mission Expressions.
- Rewrite doctrine or editorial philosophy.
- Create new repositories.
- Rename repositories.
- Merge or delete repositories.
- Delete canonical documents.
- Delete duplicate or orphaned content without Founder approval.
- Rewrite Git history.
- Force push.
- Contaminate active audit, production, or implementation branches with unrelated migration work.
- Modify Foundation Canon because a possible improvement is discovered.

When authority is unclear, stop and surface the decision to the Founder.

---

# Phase 1 — Inventory

## Required Work

Verify actual current state before making structural changes.

Record, where accessible:

- Repository name and URL
- Mission Expression or institutional function
- Default branch
- Relevant active branches
- Current top-level structure
- Canonical documents
- Governance and standards
- Active projects
- Production assets
- Archives
- Cross-repository dependencies
- Potential duplicates
- Potential orphans
- Current risks or conflicts

Do not assume repository names, local paths, or remote state when they can be verified.

## Deliverables

- `REPOSITORY_INVENTORY.md`
- `CANONICAL_SOURCE_REGISTER.md`

## Gate 1

If inventory reveals conflicting canonical sources, major structural ambiguity, or active-work risk, pause for Founder/Architect review.

Otherwise proceed to Phase 2.

---

# Phase 2 — Migration Planning

## Required Work

Map current state to the approved FC-001 / FC-002 architecture.

Classify each material finding as:

- No change required
- Navigation-only improvement
- Cross-reference improvement
- Safe migration candidate
- Duplicate requiring review
- Orphan requiring review
- Structural conflict requiring Architect review

Preserve existing validated naming and folder structures unless there is a documented reason to change them.

## Deliverables

- `MIGRATION_PLAN.md`
- `DUPLICATE_CONTENT_REPORT.md`
- `ORPHAN_FILE_REPORT.md`

## Gate 2

Pause before any destructive, ambiguous, or cross-repository migration requiring Founder approval.

No silent reconciliation of conflicting canonical sources.

---

# Phase 3 — Approved Implementation

## Required Work

Execute only approved migrations and navigation improvements.

For every material move, record:

- Original path
- New path
- Reason
- Governing authority
- Commit reference
- Verification result

Prefer small logical commits.

Preserve history where practical.

Do not restructure content solely to produce visual uniformity.

## Deliverable

- `MIGRATION_REPORT.md`

---

# Phase 4 — Validation

## Required Work

Validate the resulting state.

Confirm, as applicable:

- Canonical sources are identifiable and non-conflicting.
- README navigation is accurate.
- Cross-references resolve.
- No untracked institutional assets were lost.
- No unapproved deletion occurred.
- No unapproved repository creation or rename occurred.
- Git history remains intact.
- Git working state is clean after approved commits.
- Existing CI/checks pass where present.
- No credentials or secrets were introduced.
- Active work branches remain intact.
- Migration records are complete.

## Deliverable

- `VALIDATION_REPORT.md`

## Gate 3

Pause for Founder review if validation reveals unresolved exceptions.

---

# Phase 5 — Completion

Submit:

- `ARCH_002_COMPLETION_REPORT.md`

The completion report shall include:

- Executive summary
- Repositories reviewed
- Approved migrations completed
- Validation status
- Outstanding exceptions
- Required Founder decisions
- Lessons learned reference
- Recommended closeout status

ARCH-002 closes only after Founder acceptance.

---

# Required Deliverables — Complete List

1. `REPOSITORY_INVENTORY.md`
2. `CANONICAL_SOURCE_REGISTER.md`
3. `MIGRATION_PLAN.md`
4. `DUPLICATE_CONTENT_REPORT.md`
5. `ORPHAN_FILE_REPORT.md`
6. `MIGRATION_REPORT.md`
7. `VALIDATION_REPORT.md`
8. `ARCH_002_COMPLETION_REPORT.md`
9. `LESSONS_LEARNED.md` when implementation produces observations for future architecture

---

# Mission and System Boundaries

The Repository Steward shall preserve these distinctions:

- **Finding My Wei** — Institutional Operating System / governance / standards / stewardship.
- **The Tao of Clinical Touch** — Tao-specific clinical intellectual property and publications.
- **Learn2Tape** — Education, CE, courses, student systems, and Learn2Tape-specific operations.
- **StitchCore** — Innovation, engineering, Sidekick Air, AeroStitch Core Technology, manufacturing, testing, and IP.
- **Freedman-Foundry** — Institutional consulting, client systems, and approved reusable client frameworks.
- **The Boston Bodyworker** — Founder professional identity and public gateway; not automatically a separate repository.
- **Learn2Tape Publishing System** — Shared operational publishing module; not synonymous with the Learn2Tape Mission Expression.

Freedman-Foundry may consume approved Finding My Wei standards and shared operational modules but may not redefine their canonical sources.

---

# Active Work Protection

Before touching a repository containing active work, verify:

- active branch,
- latest stable commit,
- uncommitted changes,
- audit / production / implementation status,
- safe base ref for ARCH-002.

If active work could be affected, either:

1. wait for a safe committed checkpoint, or
2. perform ARCH-002 from a separate clean branch or clone.

Document the method used.

---

# Reporting Standard

Each ARCH-002 report shall include enough evidence for future stewards to understand:

- what was observed,
- what changed,
- why it changed,
- what authority permitted it,
- what remains unresolved.

Reports become part of the institutional record.

---

# Success Criteria

ARCH-002 is complete when:

- Actual repository state has been inventoried rather than assumed.
- Canonical sources are identifiable.
- Existing validated architecture has been preserved unless change was justified and approved.
- Duplicates and orphans are documented.
- Approved migrations are traceable.
- Repository navigation is coherent.
- Active workstreams remain intact.
- Validation passes or documented exceptions are accepted by the Founder.
- The completion report is approved.

Uniformity is not the objective.

Clarity, continuity, and mission support are the objective.

---

# Founder Directive — Architecture Freeze

During ARCH-002 implementation, Foundation Canon v1.0 RC1 is frozen.

If implementation reveals an architectural weakness:

1. Record it in `LESSONS_LEARNED.md`.
2. Complete the current approved work where safe.
3. Surface the issue at the appropriate Founder review gate.
4. Do not modify Foundation Canon without explicit Founder authorization.

> **Architecture exists to accelerate the Mission, not delay it.**

---

# Architect Certification

This work order is a faithful execution order derived from:

- FC-001 — Master Repository Map
- FC-002 — Repository Architecture
- FC-003 — ARCH-002 Implementation Specification

The Repository Steward is authorized to execute ARCH-002 within the boundaries stated above.

No additional constitutional interpretation is required.

---

# Revision History

| Version | Date | Authority | Notes |
|---|---|---|---|
| 1.0.0-rc1 | August 7, 2026 | Founder + Architect | Initial Founder-approved Repository Steward work order |
