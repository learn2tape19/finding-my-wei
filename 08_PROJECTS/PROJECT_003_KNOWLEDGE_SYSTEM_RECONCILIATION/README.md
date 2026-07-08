# PROJECT 003
## Knowledge System Reconciliation

**Status:** Approved (Awaiting Execution Authorization)  
**Authority:** Drew Freedman, Founder  
**Created:** July 8, 2026  
**Scope:** Institutional Initiative (Permanent)  

---

# Mission

Transform Finding My Wei into a unified institutional knowledge system spanning GitHub, Obsidian, and Notion while preserving all historical work and eliminating future ambiguity.

---

# Strategic Rationale

Finding My Wei will generate decades of intellectual work:

- The Tao of Clinical Touch (ecosystem)
- Project Atlas (investigations)
- Sidekick Air / StitchCore (product development)
- Let's Get Clinical (content and media)
- Books and publications
- Patents and IP
- Research collaborations
- Educational programs
- Strategic partnerships

This work requires a knowledge system that:

- **Preserves** institutional knowledge in permanent form (GitHub)
- **Reveals** connections and relationships (Obsidian)
- **Drives** execution and operations (Notion)

No single tool serves all three purposes equally well.

This project establishes the architecture for how all three work together.

---

# Objectives

1. **Audit existing Notion workspace** — Inventory every page, database, automation, template, and workflow
2. **Audit GitHub repository** — Identify duplication, orphan files, naming inconsistencies, outdated documents
3. **Design Obsidian implementation** — Create vault architecture, plugin strategy, template library
4. **Eliminate duplicate knowledge** — One canonical source for every concept
5. **Preserve historical assets** — Archive historical work with clear lineage
6. **Produce migration plan** — Phased approach from current state to unified system
7. **Build institutional standards** — Metadata, status values, domains, tags, linking
8. **Produce reusable templates** — Documents auto-conform to institutional standards
9. **Maintain backward compatibility** — Existing systems remain functional during transition

---

# Deliverables

```
08_PROJECTS/
└── PROJECT_003_KNOWLEDGE_SYSTEM_RECONCILIATION/
    ├── README.md (this file)
    │
    ├── 01_AUDIT/
    │   ├── GITHUB_AUDIT.md
    │   ├── NOTION_AUDIT.md
    │   └── OBSIDIAN_AUDIT.md
    │
    ├── 02_ARCHITECTURE/
    │   ├── KNOWLEDGE_ARCHITECTURE.md
    │   ├── SYSTEM_BOUNDARIES.md
    │   └── INFORMATION_LIFECYCLE.md
    │
    ├── 03_MIGRATION/
    │   ├── NOTION_MIGRATION_PLAN.md
    │   ├── OBSIDIAN_SETUP.md
    │   └── GITHUB_NORMALIZATION.md
    │
    ├── 04_STANDARDS/
    │   ├── OBSIDIAN_STANDARDS.md
    │   ├── METADATA_SCHEMA.md
    │   ├── TAG_TAXONOMY.md
    │   ├── LINKING_STANDARD.md
    │   └── TEMPLATE_LIBRARY.md
    │
    ├── 05_MAPS_OF_CONTENT/
    │   ├── HOME.md
    │   ├── TAO_MOC.md
    │   ├── PROJECT_ATLAS_MOC.md
    │   ├── SIDEKICK_MOC.md
    │   ├── STITCHCORE_MOC.md
    │   ├── RESEARCH_MOC.md
    │   ├── PEOPLE_MOC.md
    │   └── PUBLICATIONS_MOC.md
    │
    ├── 06_DASHBOARDS/
    │   ├── FOUNDER_DASHBOARD.md
    │   ├── RESEARCH_DASHBOARD.md
    │   ├── EDITORIAL_DASHBOARD.md
    │   └── OPERATIONS_DASHBOARD.md
    │
    └── 07_IMPLEMENTATION/
        ├── CHECKLIST.md
        ├── PHASE_1.md
        ├── PHASE_2.md
        └── PHASE_3.md
```

---

# Required Audit

Claude will conduct comprehensive audits of all three systems.

## GitHub Audit

**Inventory:**
- All folders and their purposes
- Duplication across files
- Naming consistency
- Orphan files (not referenced anywhere)
- Archive candidates
- Outdated documents
- Broken internal links

**Classification:**
- Permanent (institutional knowledge)
- Operational (temporary work)
- Archive (historical)
- Delete (obsolete)
- Merge (duplicated)
- Reference (pointer to external source)

---

## Notion Audit

**Inventory of every element:**
- Pages and their purposes
- Databases and their schemas
- Dashboards and their metrics
- Automations and their workflows
- Templates and their structure
- Kanban boards and their status
- Calendar events and their purpose
- CRM records and their types
- Documents and their ownership

**Classification:**
- Permanent (essential to institutional knowledge)
- Operational (daily/weekly work)
- Archive (historical)
- Delete (no longer used)
- Merge (duplicated across systems)
- Reference (link to external source)

---

## Obsidian Audit

**Design assessment:**
- Current vault structure (if it exists)
- Plugin ecosystem and rationale
- Template availability
- Graph connectivity
- Maps of Content quality
- Dashboard functionality
- Daily note practices
- Bookmark organization

**Recommendations:**
- Optimal vault structure
- Essential plugins
- Template hierarchy
- MOC strategy
- Dashboard architecture

---

# Institutional Rules

Claude will establish permanent standards for all future knowledge creation.

## Metadata Schema

Every permanent document receives YAML frontmatter:

```yaml
---
title: Document Title
status: [Draft|Working|Review|Approved|Canonical|Archived]
domain: [Constitution|Operating System|Project Atlas|Intellectual Estate|Library|Marketing|Research|Engineering|Business|Personal]
project: [Project name or null]
owner: [Owner name]
created: YYYY-MM-DD
updated: YYYY-MM-DD
reviewed: YYYY-MM-DD or null
tags:
  - #domain/tao
  - #topic/therapeutic-alliance
  - #status/canonical
aliases:
  - Alternative name
  - Common reference
---
```

## Status Values

- **Draft** — Early exploration, not yet stable
- **Working** — Active development, subject to change
- **Review** — Ready for expert review, pending approval
- **Approved** — Reviewed and approved, ready for publication
- **Canonical** — Permanent institutional knowledge
- **Archived** — Historical, superseded, no longer active

## Domains

- **Constitution** — Governance, directives, institutional principles
- **Operating System** — Processes, workflows, systems
- **Project Atlas** — Research investigations, synthesis
- **Intellectual Estate** — Books, papers, frameworks, theory
- **Library** — Reference materials, research sources, external knowledge
- **Marketing** — Campaign materials, positioning, communications
- **Research** — Active investigations, findings, data
- **Engineering** — Technical work, specifications, prototypes
- **Business** — Operations, partnerships, strategic decisions
- **Personal** — Individual work, not institutional

## Tag Taxonomy

Controlled vocabulary replacing ad hoc tags:

### Domain Tags
```
#domain/tao
#domain/projectatlas
#domain/sidekickai
#domain/stitchcore
#domain/learn2tape
#domain/bostonbodyworker
#domain/personal
```

### Topic Tags
```
#topic/therapeutic-alliance
#topic/nervous-system
#topic/pain-science
#topic/teaching
#topic/research
#topic/neuroscience
#topic/clinical-reasoning
#topic/manufacturing
#topic/ip-strategy
```

### Status Tags
```
#status/draft
#status/working
#status/review
#status/approved
#status/canonical
#status/archived
```

### Publication Tags
```
#publication/book
#publication/paper
#publication/article
#publication/course
#publication/podcast
#publication/social
#publication/presentation
```

### Person Tags
```
#person/whitney-lowe
#person/doug-nelson
#person/josh-smith
#person/zane
#person/[name]
```

### Campaign Tags
```
#campaign/001
#campaign/tao-launch
#campaign/atlas-phase1
```

---

# Maps of Content

Every major domain receives a curated Map of Content.

## The Tao MOC

```
- Books
  - The Tao of Clinical Touch (published)
  - Permission Interview (planned)
  - Teaching Permission (planned)
  - Alliance in Research (planned)
  
- Research
  - Therapeutic Alliance studies
  - Permission assessment
  - Nervous system regulation
  - Teaching effectiveness
  
- Continuing Education
  - Level I: Introductory
  - Level II: Applied
  - Level III: Advanced
  - Level IV: Instructor
  - Level V: Master
  
- Campaign
  - Campaign 001
  - Speaking engagements
  - Podcasts
  - Social media
  
- Presentations
  - Conference keynotes
  - Workshop materials
  - Video content
  - Interview transcripts
  
- Chapters
  - Permission (Chapter excerpts)
  - Alliance (Chapter excerpts)
  - Teaching (Chapter excerpts)
  
- Quotes
  - Key passages
  - Foundational statements
  - Teaching moments
  
- Future Ideas
  - Book 2 outline
  - Book 3 outline
  - Research questions
  - Speaking opportunities
  
- References
  - Key authors (Whitney Lowe, etc.)
  - Research papers
  - Related theories
  - External resources
  
- Related Papers
  - Academic publications
  - Journal articles
  - White papers
  
- Movement
  - Professional adoption
  - Educator network
  - Community building
  - Field influence strategy
```

Similar MOCs created for:
- Project Atlas
- Sidekick Air / StitchCore
- Research initiatives
- People and collaborators
- Publications and media
- Business operations

---

# Dashboards

**Role-specific views** of the knowledge system.

## Founder Dashboard

Surfaces:
- Current investigations and status
- Current writing projects and progress
- Pending reviews and decisions
- Recent GitHub commits and changes
- Editorial queue (books, papers, articles)
- Open research questions
- Manufacturing status (Sidekick Air)
- Speaking schedule and proposals
- Campaign status
- Daily priorities and next actions

## Research Dashboard

Surfaces:
- Newest papers added
- Open investigations
- Atlas research questions
- Pending synthesis work
- Citation library
- Collaborative opportunities
- Publication pipeline

## Editorial Dashboard

Surfaces:
- Books in progress
- Articles being written
- Social media queue
- Podcast episodes
- Newsletter content
- Publishing schedule
- Review status for each piece

## Operations Dashboard

Surfaces:
- Project status
- Team tasks
- Deadlines
- Meetings and calendar
- Action items
- Commitments and deliverables

---

# Migration Rules

**Permanent principles for where knowledge lives.**

## Canonical Home

Every piece of knowledge receives exactly one permanent home.

### GitHub (Permanent Institutional Knowledge)
- Constitutional documents
- Intellectual frameworks
- Published work
- Research synthesis
- Historical record
- Decision documentation

### Notion (Operational Execution)
- Project management
- Task tracking
- Calendars and schedules
- CRM and relationships
- Workflow automation
- Team coordination
- Daily operations

### Obsidian (Personal Knowledge Connection)
- Daily thinking and reflection
- Connection maps
- Query and exploration
- Personal note-taking
- Unstructured synthesis
- Graph visualization
- Cross-domain linking

## No Duplication

No document exists in more than one permanent home.

References point to canonical source.

Operational copies (Notion) link to permanent source (GitHub).

Personal copies (Obsidian) link to both.

---

# Success Criteria

The project is complete only when ALL of the following are met:

✓ **Every document has a defined owner** — Responsibility is clear

✓ **Every knowledge asset has one canonical location** — No ambiguity about source of truth

✓ **Obsidian can navigate the entire intellectual estate through MOCs and backlinks** — The knowledge graph is complete and navigable

✓ **Notion contains only operational information** — No permanent knowledge duplicated in operational system

✓ **GitHub contains only canonical institutional knowledge** — The permanent record is complete and organized

✓ **Claude can create any future document that conforms automatically to institutional standards** — Templates ensure consistency without manual effort

✓ **A new contributor could understand the entire system from the documentation alone** — The system is self-documenting and requires no oral transmission

---

# Key Strategic Insight

> "If we execute this well, you'll end up with something that is uncommon even among research organizations: a single, coherent intellectual ecosystem where GitHub preserves knowledge, Obsidian reveals connections, and Notion drives execution."

This is scalability at the meta-level.

Not just scaling the work itself, but scaling the system that manages the work.

---

# Permanent Institutional Initiative

This project is **not a one-time cleanup.**

The knowledge system itself becomes a maintained institutional asset.

As Finding My Wei grows:
- The Tao ecosystem expands
- Project Atlas investigations multiply
- Sidekick Air / StitchCore develops
- Books and publications accumulate
- Patents and IP multiply
- Research collaborations grow
- Educational programs expand
- Strategic partnerships deepen

The knowledge system **evolves through documented standards** rather than ad hoc changes.

This architecture is **scalable enough to support decades of intellectual work.**

---

# Authorization

This project awaits Founder approval to begin execution.

**Ready to commence Phase 1: Audits** upon authorization.

---

**Authority:** Drew Freedman, Founder  
**Created:** July 8, 2026  
**Status:** Approved (Awaiting Execution Authorization)  
**Scope:** Permanent Institutional Initiative  

