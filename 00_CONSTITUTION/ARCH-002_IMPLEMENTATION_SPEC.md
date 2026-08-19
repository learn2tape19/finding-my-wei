# FC-003 — ARCH-002_IMPLEMENTATION_SPEC.md

**Institution:** Finding My Wei  
**Document Number:** FC-003  
**Document Class:** Engineering Implementation Specification  
**Version:** 1.0.0-rc1  
**Status:** Founder Approved  
**Authority:** Derived from FC-001 and FC-002  
**Canonical Location:** `finding-my-wei/00_CONSTITUTION/ARCH-002_IMPLEMENTATION_SPEC.md`

---

# Article I — Purpose

This specification translates the constitutional architecture established by FC-001 and the repository engineering standard established by FC-002 into executable implementation work.

Its purpose is to remove interpretation from repository consolidation and organization.

The Repository Steward shall implement only what is authorized here and in the approved Foundation Canon package.

---

# Article II — Scope

ARCH-002 authorizes repository engineering only.

Included:

- Repository inventory
- Canonical source mapping
- Existing architecture assessment
- Navigation improvements
- Cross-repository references
- Migration planning
- Approved structural consolidation
- README updates
- Validation
- Migration and completion reporting

Excluded unless separately approved:

- Constitutional changes
- New governance concepts
- New repository creation
- Repository renaming
- Repository deletion or merger
- Editorial rewriting
- Website implementation
- Product development
- Publishing production
- Client delivery work

---

# Article III — Governing Constraints

The following constraints are binding:

1. **Integration over Reorganization.**
2. **Repository before Memory.** Institutional truth lives in version-controlled canonical sources.
3. **Understanding precedes intervention.** Inventory and map before moving.
4. Preserve useful existing architecture.
5. Do not create parallel structures solely for consistency.
6. No destructive action without Founder approval.
7. No force pushes or history rewrites.
8. No constitutional interpretation by the Repository Steward.
9. Active workstreams and audit branches must be protected from unrelated migration work.
10. Findings that suggest future architectural improvement are documented in `LESSONS_LEARNED.md`, not introduced into ARCH-002 without approval.

---

# Article IV — Phase A: Actual-State Inventory

Before any migration, the Repository Steward shall determine the actual current state of the institutional repository ecosystem.

The inventory shall identify, where accessible:

- Repository name
- Repository URL
- Mission Expression or institutional function
- Default branch
- Active branches relevant to current work
- Current top-level structure
- Canonical documents
- Governance documents
- Standards
- Active projects
- Production assets
- Archives
- Cross-repository dependencies
- Duplicate or potentially duplicate sources
- Orphaned or ambiguously placed files

No repository name, branch, local path, or remote state shall be assumed when it can be verified.

Deliverable:

`REPOSITORY_INVENTORY.md`

---

# Article V — Phase B: Canonical Source Register

The Repository Steward shall create a register identifying the authoritative source for institutional documents and systems.

The register shall include, at minimum:

- Artifact name
- Document class or function
- Canonical repository
- Canonical path
- Current version or status when known
- Known derivative or duplicate locations
- Recommended disposition of non-canonical copies

Deliverable:

`CANONICAL_SOURCE_REGISTER.md`

Conflicting canonical sources must be surfaced for Founder decision. They shall not be silently reconciled.

---

# Article VI — Phase C: Current-to-Target Mapping

Using FC-001 and FC-002, the Repository Steward shall map current state to the approved target architecture.

The mapping shall distinguish:

- No change required
- Navigation-only improvement
- Cross-reference improvement
- Safe move or rename candidate
- Duplicate requiring Founder decision
- Orphan requiring Founder decision
- Structural conflict requiring Architect review

The target state shall preserve existing validated naming and folder structures whenever they remain coherent.

Deliverable:

`MIGRATION_PLAN.md`

No destructive migration begins until the migration plan has been reviewed at the designated Founder approval gate.

---

# Article VII — Mission and System Distinctions

The Repository Steward shall preserve the distinctions established by FC-001 and FC-002.

## Finding My Wei

Institutional Operating System and canonical home for constitutional governance, institutional standards, stewardship, and cross-expression architecture.

## The Tao of Clinical Touch

Canonical home for Tao-specific clinical intellectual property, publications, clinical framework materials, Tao editorial sources, and related content.

## Learn2Tape

Canonical home for Learn2Tape education, courses, CE operations, student materials, and Learn2Tape-specific business/educational content.

## StitchCore

Canonical home for innovation, including Sidekick Air, AeroStitch Core Technology, engineering, manufacturing, testing, and related IP materials.

## Freedman-Foundry

Canonical home for institutional consulting systems, client work, approved reusable client frameworks, and engagement documentation.

## The Boston Bodyworker

The Founder's enduring professional identity and public gateway. It is not automatically a separate repository and shall not be made one without Founder authorization.

## Learn2Tape Publishing System

A shared operational publishing module, not the same thing as the Learn2Tape Mission Expression. Its established source-before-derivative model shall be preserved. It may be governed or referenced through Finding My Wei while being used by approved Mission Expressions.

---

# Article VIII — Active Work Protection

ARCH-002 shall not interrupt or contaminate active institutional work.

Before migration in any repository containing active work, the Repository Steward shall verify:

- active branch,
- latest stable commit,
- uncommitted changes,
- current audit or production status,
- appropriate base ref for ARCH-002 work.

If active work is in progress, the Steward shall either:

1. wait for a safe committed checkpoint, or
2. perform ARCH-002 from a separate clean branch or clone.

The method used must be recorded in the migration report.

---

# Article IX — Duplicate Content Review

The Repository Steward shall identify materially duplicated institutional content.

Duplicates shall be classified as:

- Intentional derivative
- Historical copy
- Operational mirror
- Potential canonical conflict
- Obsolete candidate
- Unknown

Deliverable:

`DUPLICATE_CONTENT_REPORT.md`

No duplicate is deleted solely because a canonical source exists. Deletion requires Founder approval.

---

# Article X — Orphan Review

Files that do not have an obvious institutional home shall be documented.

Deliverable:

`ORPHAN_FILE_REPORT.md`

Each entry shall include:

- Current path
- Apparent purpose
- Likely Mission Expression or function
- Recommended canonical home
- Confidence or uncertainty
- Required Founder decision, if any

Orphans shall not be silently relocated when ownership is ambiguous.

---

# Article XI — Migration Execution

Only approved migrations shall be executed.

For each material move, record:

- Original path
- New path
- Reason
- Governing authority
- Commit or change reference
- Verification result

Prefer small logical commits.

Preserve Git history where practical.

Do not rewrite history.

Do not delete historical context merely to produce cosmetic uniformity.

Deliverable:

`MIGRATION_REPORT.md`

---

# Article XII — README and Navigation

Repository navigation shall be improved where needed so future stewards can orient themselves from canonical documentation.

README changes shall:

- explain repository purpose,
- identify canonical scope,
- identify governing references,
- point to active work,
- identify related repositories or systems,
- avoid duplicating constitutional text unnecessarily.

Navigation improvements are authorized when they do not alter institutional meaning.

---

# Article XIII — Validation

After approved implementation, the Repository Steward shall validate the resulting state.

Validation shall include, as applicable:

- Canonical source uniqueness
- Cross-reference integrity
- README navigation
- No untracked institutional assets lost
- No unapproved deletions
- No unapproved repository creation or renaming
- Git status clean after approved commits
- Existing CI/checks passing where present
- No introduced credentials or secrets
- Active work branches preserved
- Migration records complete

Deliverable:

`VALIDATION_REPORT.md`

---

# Article XIV — Required Deliverables

ARCH-002 requires the following implementation artifacts:

1. `REPOSITORY_INVENTORY.md`
2. `CANONICAL_SOURCE_REGISTER.md`
3. `MIGRATION_PLAN.md`
4. `DUPLICATE_CONTENT_REPORT.md`
5. `ORPHAN_FILE_REPORT.md`
6. `MIGRATION_REPORT.md`
7. `VALIDATION_REPORT.md`
8. `ARCH_002_COMPLETION_REPORT.md`

Where implementation reveals architectural observations that do not belong in the current migration:

9. `LESSONS_LEARNED.md`

---

# Article XV — Approval Gates

## Gate A — Inventory Complete

Submit actual-state inventory and canonical source register.

Pause for Founder/Architect review if conflicts or major unknowns are present.

## Gate B — Migration Plan Complete

Submit proposed current-to-target mapping, duplicate report, and orphan report.

No destructive or ambiguous migration proceeds without Founder approval.

## Gate C — Implementation Complete

Submit migration report and validation report.

Pause for Founder review.

## Gate D — Completion

Submit `ARCH_002_COMPLETION_REPORT.md`.

ARCH-002 closes only after Founder acceptance.

---

# Article XVI — Acceptance Criteria

ARCH-002 is complete when:

- Actual repository state has been inventoried rather than assumed.
- Canonical sources are identifiable.
- Existing validated architecture has been preserved unless change was justified and approved.
- Material duplicates and orphans are documented.
- Approved migrations are traceable.
- Navigation enables future steward orientation.
- Validation passes or outstanding exceptions are explicitly documented.
- No active workstream was damaged or contaminated.
- Founder accepts the completion report.

Uniformity is not an acceptance criterion.

Institutional clarity is.

---

# Founder Resolution

Implementation exists to faithfully realize approved architecture.

The Repository Steward shall improve clarity without changing constitutional intent.

When implementation reveals an architectural weakness, document it. Do not redesign Foundation Canon during the implementation merely because improvement is possible.

> **Architecture exists to accelerate the Mission, not delay it.**

---

# Revision History

| Version | Date | Authority | Notes |
|---|---|---|---|
| 1.0.0-rc1 | August 7, 2026 | Founder + Architect | Initial Founder-approved ARCH-002 implementation specification |
