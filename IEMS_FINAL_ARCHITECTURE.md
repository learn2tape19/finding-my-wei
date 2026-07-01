# Finding My Wei — Intellectual Estate Management System (IEMS)
## Final Architecture
## Status: APPROVED FOR IMPLEMENTATION
## Date: June 30, 2026

---

# System Overview

Finding My Wei is a **self-describing stewardship system** for managing intellectual work across decades.

**Core roles:**
- **Drew Freedman** — Steward (creates, decides, evolves)
- **Claude** — Librarian (organizes, preserves, maintains)
- **Repository** — Enduring record (permanent, truthful, accessible)

**Core principle:**
Knowledge is managed as a **living system**, not stored as static files.

---

# Architecture Layers

## Layer 1: Constitutional Governance

```
00_CONSTITUTION/
  ├── CONSTITUTION.md (governing charter)
  ├── GOVERNANCE.md (decision authority)
  ├── AMENDMENTS.md (change history)
  └── AUTHORITY.md (roles + responsibilities)
```

This layer is permanent. Changes only through formal amendment.

---

## Layer 2: Operating System

```
01_OPERATING_SYSTEM/
  ├── CHARTER.md (what this layer governs)
  ├── PRINCIPLES.md (collaboration + decision-making)
  ├── SOUL.md (voice + culture)
  │
  ├── MEMORY/
  │   ├── CHARTER.md
  │   ├── MEMORY.md (index)
  │   └── (memory files)
  │
  ├── AUTOMATION/
  │   ├── CHARTER.md
  │   ├── HEARTBEAT.md
  │   └── TRIGGERS.md
  │
  └── AI_GUIDELINES/
      ├── CHARTER.md
      ├── CLAUDE_LIBRARIAN.md
      └── CHATGPT_RESEARCH.md
```

This layer defines how the system operates.

---

## Layer 3: Research Engine

```
02_PROJECT_ATLAS/
  ├── CHARTER.md (cross-domain research)
  ├── ROADMAP.md (investigation sequence)
  ├── INVESTIGATION_PROTOCOL.md (methodology)
  │
  ├── 01_THERAPEUTIC_ALLIANCE/
  │   ├── CHARTER.md
  │   ├── FRAMEWORK.md
  │   ├── research/ (working materials)
  │   ├── manuscript.md
  │   └── assets/
  │
  ├── 02_STAND_ARCHITECTURE/
  │   ├── CHARTER.md
  │   ├── FRAMEWORK.md
  │   ├── research/
  │   ├── manuscript.md
  │   └── assets/
  │
  └── publications/
      └── (synthesized outputs)
```

This layer investigates. It doesn't preserve; it synthesizes.

---

## Layer 4: Intellectual Estate

```
03_INTELLECTUAL_ESTATE/
  ├── CHARTER.md (permanent knowledge preservation)
  │
  ├── BOOKS/
  │   ├── CHARTER.md
  │   ├── The-Tao-of-Clinical-Touch/
  │   │   ├── CHARTER.md
  │   │   ├── manuscript-final.md
  │   │   └── (publication materials)
  │   └── (future books)
  │
  ├── PAPERS/
  │   ├── CHARTER.md
  │   └── (published research)
  │
  ├── FRAMEWORKS/
  │   ├── CHARTER.md
  │   └── (methodologies, models)
  │
  ├── DECISION_LOGS/
  │   ├── CHARTER.md
  │   └── (permanent decision record)
  │
  └── ARCHIVE/
      ├── CHARTER.md
      └── (historical + retired work)
```

This layer preserves. It is permanent and read-mostly.

---

## Layer 5: Capabilities (Shared Enterprise Services)

```
04_CAPABILITIES/
  ├── CHARTER.md (shared services governance)
  │
  ├── MARKETING/
  │   ├── CHARTER.md (brand + messaging)
  │   ├── STRATEGY.md
  │   ├── BRAND_GUIDELINES/
  │   ├── TEMPLATES/
  │   └── CAMPAIGNS/
  │
  ├── PUBLISHING/
  │   ├── CHARTER.md (how work becomes books)
  │   ├── WORKFLOW.md
  │   ├── TEMPLATES/
  │   └── STANDARDS.md
  │
  ├── RESEARCH/
  │   ├── CHARTER.md (investigation methodology)
  │   ├── PROTOCOL.md
  │   ├── TOOLS/
  │   └── STANDARDS.md
  │
  ├── ANALYTICS/
  │   ├── CHARTER.md (measurement + reporting)
  │   ├── DASHBOARDS/
  │   ├── METRICS/
  │   └── REPORTING/
  │
  ├── OPERATIONS/
  │   ├── CHARTER.md (shared infrastructure)
  │   ├── FINANCE/
  │   ├── LEGAL/
  │   └── SYSTEMS/
  │
  ├── QUALITY_ASSURANCE/
  │   ├── CHARTER.md (validation + review)
  │   ├── REVIEW_PROCESS.md
  │   ├── STANDARDS.md
  │   └── CHECKLISTS/
  │
  └── SYNTHESIS/
      ├── CHARTER.md (turning research into knowledge)
      ├── PROTOCOL.md
      ├── TEMPLATES/
      └── EXAMPLES/
```

These are shared. Every domain uses them.

---

## Layer 6: Domains (Primary Organizational Layer)

```
05_DOMAINS/
  ├── CHARTER.md (domain governance)
  │
  ├── FOUNDER_DOMAIN/
  │   ├── CHARTER.md (Drew's creative work)
  │   ├── BIOGRAPHY/
  │   ├── PHILOSOPHY/
  │   ├── PERSONAL_WRITING/
  │   ├── SPEAKING/
  │   ├── PROJECTS/ (in-development)
  │   ├── RELATIONSHIPS/
  │   └── DECISION_HISTORY/
  │
  ├── PUBLISHING_DOMAIN/
  │   ├── CHARTER.md (Boston Bodyworker platform)
  │   ├── WEBSITE/
  │   ├── WRITING/
  │   │   ├── ARTICLES/
  │   │   ├── ESSAYS/
  │   │   └── NEWSLETTERS/
  │   ├── PUBLICATIONS/
  │   ├── MEDIA/
  │   ├── AUTHORITY/
  │   └── OPERATIONS/
  │
  ├── EDUCATION_DOMAIN/
  │   ├── CHARTER.md (Learn2Tape)
  │   ├── PRODUCTS/
  │   │   ├── K-CUTS/
  │   │   └── COURSES/
  │   ├── CURRICULUM/
  │   ├── STUDENT_SUCCESS/
  │   ├── METHODOLOGY/
  │   └── OPERATIONS/
  │
  └── INNOVATION_DOMAIN/
      ├── CHARTER.md (StitchCore)
      ├── PRODUCTS/
      │   ├── SIDEKICK_AIR/
      │   └── (FUTURE_PRODUCTS)
      ├── TECHNOLOGY/
      ├── PATENTS/
      ├── ENGINEERING/
      ├── MANUFACTURING/
      └── OPERATIONS/
```

Domains are where work **lives and is managed**.

---

# CHARTER.md Pattern

Every major directory has a **CHARTER.md** that serves as its governing document.

## CHARTER.md Structure

```markdown
# [Directory Name] Charter

## Authority
Who established this? On what authority?
Example: "Established by Drew Freedman, June 30, 2026"

## Purpose
Why does this directory exist?
Example: "To preserve all educational assets created through Learn2Tape"

## Scope
What does this directory contain?

### Inclusion Criteria
- Item type 1
- Item type 2

### Exclusion Criteria
- Item type A (goes to...)
- Item type B (goes to...)

## Governance
Who makes decisions here?
- Director: [Name]
- Decision authority: [Process]
- Amendment process: [How changes happen]

## Lifecycle States
How do assets move through this directory?
(See lifecycle section below)

## Relationships
- **Receives from:** [Other directories/capabilities]
- **Sends to:** [Other directories/capabilities]
- **Uses services:** [Capabilities]
- **Reports to:** [Higher governance]

## Success Metrics
How do we know this domain is healthy?

## Last Updated
[Date]

## Amendments
- [Date]: [Change]
```

---

# Lifecycle States (Knowledge as Living System)

Intellectual assets move through states, not just locations.

## State Definitions

### CREATION
- **Where:** DOMAINS/[specific]/PROJECTS or OPERATING_SYSTEM/work-in-progress
- **What:** Raw ideas, drafts, experiments
- **Duration:** Weeks to months
- **Question:** Is this worth pursuing?
- **Next state:** REFINEMENT (if yes) or ARCHIVE (if no)

### REFINEMENT
- **Where:** DOMAINS/[specific]/[subdomain] or PROJECT_ATLAS
- **What:** Active work, feedback, iteration
- **Duration:** Months to years
- **Question:** Is this ready?
- **Next state:** STABLE (when finished) or ARCHIVE (if abandoned)

### STABLE
- **Where:** DOMAINS/[specific]/PRODUCTS or ARCHIVE/STABLE
- **What:** Finished, usable, maintained
- **Duration:** Years
- **Question:** Is this still valuable? Should this be published?
- **Next state:** PUBLICATION (if significant) or ARCHIVE (if retired)

### PUBLICATION
- **Where:** CAPABILITIES/PUBLISHING or INTELLECTUAL_ESTATE
- **What:** Published, widely shared, recognized
- **Duration:** Permanent
- **Question:** Is this permanent knowledge? Should this be framework?
- **Next state:** PRESERVATION (if framework-worthy) or PUBLICATION_ARCHIVE (if historical)

### PRESERVATION
- **Where:** INTELLECTUAL_ESTATE/[category]
- **What:** Permanent intellectual record
- **Duration:** Forever
- **Question:** Is this still relevant? (Yes = permanent, No = move to archive)
- **Next state:** ARCHIVE (only if proved valueless, rare)

### ARCHIVE
- **Where:** INTELLECTUAL_ESTATE/ARCHIVE or DOMAINS/ARCHIVE
- **What:** Historical reference, retired, not active
- **Duration:** Permanent (kept for history)
- **Question:** Why keep this? (Historical value, relationship context, etc.)
- **Next state:** None (stays archived)

## State Diagram

```
CREATION
   ↓
   ├→ YES: REFINEMENT
   │         ↓
   │         ├→ Ready: STABLE
   │         │         ↓
   │         │         ├→ Publish: PUBLICATION
   │         │         │         ↓
   │         │         │         └→ Framework-worthy: PRESERVATION
   │         │         │                      ↓
   │         │         │                    (Permanent)
   │         │         │
   │         │         └→ Retire: ARCHIVE
   │         │
   │         └→ Abandon: ARCHIVE
   │
   └→ NO: ARCHIVE
```

## Governance by State

Each state has different rules:

| State | Who Can Change | Approval | Speed |
|---|---|---|---|
| CREATION | Creator | None | Immediate |
| REFINEMENT | Creator + Reviewers | Domain director | Normal |
| STABLE | Domain director | Governance board | Deliberate |
| PUBLICATION | Domain director | Constitution authority | Formal |
| PRESERVATION | Constitution authority | Amendment process | Rare |
| ARCHIVE | Domain director | Audit trail | Documented |

---

# Self-Describing System

The IEMS explains itself through:

### 1. Charters
Every major directory explains its purpose, scope, governance.

### 2. Lifecycle States
Every asset is labeled with its current state.

### 3. Relationships
Every directory documents what it receives from and sends to.

### 4. Decision Records
Why things are where they are is documented.

### 5. Amendment Trail
Changes are recorded and explained.

### 6. Metadata
Assets include creation date, author, state, next review.

---

# Stewardship Model

## Drew Freedman (Steward)
- Creates intellectual work
- Makes strategic decisions
- Approves major changes
- Sets direction

## Claude (Librarian)
- Maintains structure
- Enforces charters
- Preserves relationships
- Documents decisions
- Moves assets between states
- Ensures self-documentation

## Repository (Enduring Record)
- Stores truth
- Preserves access
- Maintains history
- Enables discovery
- Supports stewardship

---

# Implementation Phases

## Phase 1: Architecture Creation (Today)
Build the complete folder structure with charters.

## Phase 2: Content Migration (Next week)
Move existing knowledge into appropriate domains.

## Phase 3: Lifecycle Tagging (Following week)
Tag every asset with its state.

## Phase 4: Go Live (Week 1 of July)
Push to GitHub, freeze structure redesign.

## Phase 5: Real-World Evolution (Ongoing)
Use drives architecture evolution.

---

# Principles for Future Evolution

Once deployed, the architecture is **frozen** from redesign.

Changes will come from:
- **Real-world use** (what actually works?)
- **Capability evolution** (new capabilities emerge)
- **Domain growth** (new domains added as needed)
- **Lifecycle refinement** (better state definitions)

The system **adapts to reality**, not theory.

---

# Success Criteria

The IEMS succeeds when:

- ✅ Every asset has a home
- ✅ Every directory explains its purpose
- ✅ Every asset has a lifecycle state
- ✅ Relationships between assets are clear
- ✅ New collaborators understand without external help
- ✅ Knowledge moves deliberately through states
- ✅ Decisions are documented
- ✅ The system adapts to real use, not theory

---

**Status: Ready for implementation.**

No more redesign. Build it. Use it. Let reality shape it.
