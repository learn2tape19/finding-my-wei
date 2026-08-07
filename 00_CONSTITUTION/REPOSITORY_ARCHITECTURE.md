# FC-002 — REPOSITORY_ARCHITECTURE.md

**Institution:** Finding My Wei  
**Document Number:** FC-002  
**Document Class:** Engineering Specification  
**Version:** 1.0.0-rc1  
**Status:** Founder Approved  
**Authority:** Derived from FC-001  
**Canonical Location:** `finding-my-wei/00_CONSTITUTION/REPOSITORY_ARCHITECTURE.md`

---

# Article I — Purpose

FC-001 defines **what** the institution is.

FC-002 defines **how** the institution is implemented.

Its purpose is to ensure that every repository follows one engineering standard while preserving the existing validated architecture of each repository.

This specification governs repository implementation.

It does not redefine constitutional authority.

---

# Article II — Architectural Philosophy

Repositories exist to reduce complexity.

They are operational environments, not filing cabinets.

Every repository shall be understandable by a new steward without requiring undocumented institutional knowledge.

Good architecture minimizes explanation.

The governing implementation principle is:

> **Integration over Reorganization.**

Existing validated structures are preserved unless a documented conflict with constitutional ownership, canonical integrity, or operational clarity requires change.

ARCH-002 shall not impose a parallel architecture simply for the sake of uniformity.

---

# Article III — Repository Standards

Every institutional repository shall clearly define:

- Purpose
- Canonical scope
- Owner
- Relationship to Finding My Wei
- Current status
- Canonical sources
- Navigation entry point

Every repository shall maintain an authoritative `README.md` that enables orientation without requiring undocumented Founder knowledge.

Additional files and directories shall be implemented according to actual repository need rather than empty structural compliance.

---

# Article IV — Existing Architecture Preservation

Before creating, moving, renaming, or consolidating repository content, the Repository Steward shall inventory the actual repository state.

The Steward shall identify:

- Current directories
- Existing governance structures
- Existing standards
- Active workstreams
- Canonical documents
- Historical archives
- Branches containing active work
- Cross-repository dependencies

No existing validated architecture shall be replaced with a generic folder model without documented evidence that the current structure creates a constitutional or operational conflict.

---

# Article V — Canonical Functional Domains

Repository structures may vary, but institutional content generally belongs to one of the following functional domains:

- Constitution / governing authority
- Governance
- Architecture
- Standards
- Active projects
- Publications
- Operations
- Marketing / distribution
- Assets
- Reference / research
- Archive

These are functional categories, not mandatory top-level folders.

The Repository Steward shall map existing repository structures to these functions before proposing structural changes.

---

# Article VI — Canonical Rules

Every document has one canonical home.

Cross-reference instead of uncontrolled duplication.

Where operational copies are necessary, they shall identify the canonical source.

Conflicting canonical documents are prohibited.

Institutional truth shall reside in version-controlled repositories rather than AI memory, local-only notes, or undocumented conversation history.

---

# Article VII — Naming Standard

Existing naming conventions shall be preserved when they are coherent and already established.

For new institutional Markdown documents, the preferred convention is:

```text
UPPER_SNAKE_CASE.md
```

Examples:

```text
MASTER_REPOSITORY_MAP.md
EDITORIAL_MANUAL.md
DIGITAL_STEWARDSHIP_STANDARD.md
```

Meaningless names such as `misc`, `new`, `final-final`, or equivalent ambiguous labels shall not be introduced.

Existing directory capitalization or numbering shall not be changed solely to satisfy cosmetic consistency.

---

# Article VIII — Repository README

Every repository README shall answer, directly or by canonical reference:

- What is this repository?
- What institutional purpose does it serve?
- Who owns its purpose?
- What content is canonical here?
- How is the repository organized?
- What work is active?
- What related repositories or governing documents matter?
- What is the repository's current status?

The README is a navigation surface, not a replacement for canonical governance.

---

# Article IX — Shared Operational Systems

A shared operational system may support multiple Mission Expressions without becoming a separate Mission Expression.

The **Learn2Tape Publishing System** is such a shared operational module.

It is distinct from **Learn2Tape LLC / the Learn2Tape Mission Expression**.

Its established production principle is:

```text
BLOG / canonical source
        ↓
PRODUCTION / derivatives
        ↓
Social / Email / Distribution
```

The publishing system may be governed or referenced from Finding My Wei while being used by Tao, Learn2Tape, or other approved expressions.

Freedman-Foundry may reuse approved institutional modules in client work but may not redefine their canonical standards.

---

# Article X — Cross-Repository References

Repositories communicate through explicit references rather than copied governance.

A cross-repository reference should identify, where practical:

- Source repository
- Canonical document
- Relevant version or status

Mission-specific repositories inherit institutional governance from Finding My Wei by reference.

They do not maintain competing constitutional copies.

---

# Article XI — Version Control

Material institutional documents shall declare sufficient metadata to identify their status and authority.

For constitutional and architecture documents this includes:

- Document number
- Version
- Status
- Authority
- Canonical location

Revision history shall be used where it materially aids institutional continuity.

---

# Article XII — Branching

`main` is the authoritative integrated branch unless a repository explicitly documents another model.

Active work shall use branches when doing so protects canonical work or enables review.

Branch strategy shall remain minimal.

ARCH-002 does **not** require creation of `develop`, `release/*`, `hotfix/*`, or other branch classes unless the repository already uses them or a demonstrated operational need exists.

No force push or history rewrite is authorized by FC-002.

Active audit or implementation branches shall be protected from unrelated repository migration work.

---

# Article XIII — Active Work Protection

Repository consolidation shall not contaminate an active project or audit.

Where active work exists on a dedicated branch, the Repository Steward shall either:

1. wait until that work reaches a stable committed checkpoint, or
2. perform ARCH-002 from a clean branch or clean clone based on the appropriate canonical ref.

The Steward shall document the chosen method.

---

# Article XIV — Repository Steward

The Repository Steward shall:

- inventory actual state before intervention,
- preserve canonical content,
- maintain navigation accuracy,
- identify duplication,
- identify orphaned material,
- document proposed migrations,
- validate references,
- prepare logical commits,
- record lessons learned separately from current architecture.

The Repository Steward shall not redefine constitutional architecture.

---

# Article XV — Migration Rules

Every material move shall be traceable.

Migration documentation shall identify:

- Original location
- Proposed or completed new location
- Reason
- Authority
- Verification state

No destructive migration is authorized without Founder approval.

No repository creation, repository renaming, repository merger, or repository deletion is authorized without Founder approval.

---

# Article XVI — Validation

Repository validation shall confirm, as applicable:

- Canonical sources are unique and identifiable
- README navigation is accurate
- Cross-references resolve
- No active assets or documents were lost
- No unapproved destructive changes occurred
- Git history remains intact
- Repository status is clean after approved commits
- Secrets or credentials were not introduced
- Existing CI or validation checks pass where relevant

Validation shall be documented.

---

# Article XVII — Definition of Done

A repository is architecturally sound when:

- its purpose is clear,
- canonical ownership is clear,
- navigation is understandable,
- active work can proceed without architectural confusion,
- existing useful structure has been preserved,
- unnecessary duplication has been identified,
- future stewards can orient themselves without undocumented institutional memory.

Uniformity is not the goal.

Clarity is the goal.

---

# Founder Resolution

Repository architecture exists to reduce friction and preserve continuity.

The best architecture is the smallest architecture that makes the work easier to understand, maintain, and advance.

> **Integration over Reorganization.**

> **Architecture exists to accelerate the Mission, not delay it.**

---

# Revision History

| Version | Date | Authority | Notes |
|---|---|---|---|
| 1.0.0-rc1 | August 7, 2026 | Founder + Architect | Initial Founder-approved release candidate |
