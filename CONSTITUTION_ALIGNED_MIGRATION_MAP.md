# Constitution-Aligned Migration Map

**Date:** June 30, 2026  
**Status:** DRAFT — Awaiting Drew review  
**Governing Authority:** CONSTITUTION.md v2.0  
**Model:** Entity-driven, pillar-based architecture

---

# OVERVIEW

Previous migration plan was **project-centric** (wrong).

Constitutional mandate is **entity-centric** (correct).

This map reorganizes the entire estate around the 7 pillars + 4 organizations.

No files deleted. All knowledge preserved.

---

# PILLAR 00: CONSTITUTION

**Current state:**
- CONSTITUTION.md (just created)

**Target state:**
```
00_CONSTITUTION/
├── CONSTITUTION.md               ✅ Created
├── AMENDMENTS.md                 📋 Track changes over time
├── GOVERNANCE.md                 📋 Decision-making authority
└── LEGAL.md                       📋 IP ownership + agreements
```

**Status:** CREATED ✅

---

# PILLAR 01: OPERATING SYSTEM

**Current state:**
- `_system/` (17 files) — exists but misnamed

**Target state:**
```
01_OPERATING_SYSTEM/
├── README.md                     New: System overview
├── PRINCIPLES.md                 Consolidate from existing docs
├── COLLABORATION.md              Move: SOUL.md → collaboration
├── MEMORY.md                     Move: _system/MEMORY.md
│   └── (memory files grow here)
├── AUTOMATION/
│   ├── HEARTBEAT.md             Move: daily brief automation
│   ├── SYNC_PROTOCOLS.md         New: sync + capture rules
│   └── TRIGGERS.md               New: what kicks off workflows
├── AI_GUIDELINES/
│   ├── CLAUDE_LIBRARIAN.md       New: Chief Librarian role
│   ├── CHATGPT_RESEARCH.md       New: Chief Strategy role
│   └── PROMPT_LIBRARY.md         New: Reusable prompts
├── TOOLS/
│   ├── GITHUB_WORKFLOW.md        New: version control protocol
│   ├── NOTION_SYNC.md            Move: OPENCLAW_LAUNCHER.md
│   └── (other tools)
└── PREFERENCES/
    └── USER.md                   Move: _system/USER.md
```

**Migrations:**
| From | To | Action |
|---|---|---|
| `_system/SOUL.md` | `01_OPERATING_SYSTEM/COLLABORATION.md` | Rename + enhance |
| `_system/USER.md` | `01_OPERATING_SYSTEM/PREFERENCES/USER.md` | Move |
| `_system/HEARTBEAT.md` | `01_OPERATING_SYSTEM/AUTOMATION/HEARTBEAT.md` | Move |
| `_system/RULES.md` | `01_OPERATING_SYSTEM/PRINCIPLES.md` | Rename + consolidate |
| `_system/MEMORY.md` | `01_OPERATING_SYSTEM/MEMORY.md` | Move (grows in place) |
| `_system/INDEX.md` | DELETE | Redundant with README |
| `_system/MASTER_CONTROL.md` | `01_OPERATING_SYSTEM/PRINCIPLES.md` | Merge |
| `_system/PROJECTS_MAP.md` | DELETE | Auto-generate from structure |
| `_system/OPENCLAW_LAUNCHER.md` | `01_OPERATING_SYSTEM/TOOLS/NOTION_SYNC.md` | Rename + move |
| `_system/SYNC_TODAY_TO_NOTION.md` | Archive | Historical |
| `_system/TODAY.md` | DELETE | Ephemeral (not repo-tracked) |
| `_system/WEEKLY_*.md` | Archive | Historical summaries |
| `_system/CLAUDE_WELCOME.md` | Archive | Onboarding (superseded) |
| `_system/sidekick-agent-*.md` | `01_OPERATING_SYSTEM/AI_GUIDELINES/CLAUDE_LIBRARIAN.md` | Consolidate + rename |

**Status:** REQUIRES REORGANIZATION

---

# PILLAR 02: PROJECT_ATLAS

**Current state:**
- `06_Project_Atlas/` — empty folder
- `07_MARKETING/tracking/` — contains Atlas campaign files
- Research papers — in external Google Drive (not in repo)

**Target state:**
```
02_PROJECT_ATLAS/
├── README.md                     New: Research engine charter
├── ROADMAP.md                    New: 5-paper publication sequence
├── DECISION_LOG.md               New: Investigation decisions
├── INVESTIGATION_PROTOCOL.md     New: How investigations flow
│
├── 01_THERAPEUTIC_ALLIANCE/
│   ├── README.md                 New: Paper 1 overview
│   ├── FRAMEWORK.md              New: Clinical framework definition
│   ├── research/
│   │   ├── notes.md              New: Investigation notes
│   │   ├── sources.md            New: Source materials
│   │   └── data/
│   ├── manuscript.md             📋 Needs capture: Paper 1 text
│   └── assets/
│       └── figures/
│
├── 02_STAND_ARCHITECTURE/
│   ├── README.md                 New: Paper 2 overview
│   ├── FRAMEWORK.md              New: Architecture definition
│   ├── research/
│   │   ├── notes.md
│   │   ├── sources.md
│   │   └── data/
│   ├── manuscript.md             📋 Needs capture: Paper 2 text
│   └── assets/
│
├── (03-05_FUTURE_PAPERS)/
│   └── (Placeholder structure for future investigations)
│
├── marketing/
│   ├── CAMPAIGN_ROADMAP.md       Move: 07_MARKETING/tracking/
│   ├── redirects.md              Move: redirect tracking
│   ├── redirect_log.md           Move: deployment record
│   └── ga4_repair.md             Move: GA4 setup notes
│
└── publications/
    ├── books/
    ├── papers/
    ├── presentations/
    └── courses/
```

**Migrations:**
| From | To | Action |
|---|---|---|
| `07_MARKETING/tracking/redirects.md` | `02_PROJECT_ATLAS/marketing/redirects.md` | Move |
| `07_MARKETING/tracking/redirect_log.md` | `02_PROJECT_ATLAS/marketing/redirect_log.md` | Move |
| `07_MARKETING/tracking/task_007_ga4_repair.md` | `02_PROJECT_ATLAS/marketing/ga4_repair.md` | Move |
| `07_MARKETING/tracking/asset_registry.md` | `02_PROJECT_ATLAS/marketing/asset_registry.md` | Move |
| `07_MARKETING/tracking/phase_1_completion_report.md` | `02_PROJECT_ATLAS/marketing/phase_1_completion.md` | Move |
| Google Drive research | `02_PROJECT_ATLAS/01_THERAPEUTIC_ALLIANCE/research/` | 📋 Capture needed |
| Google Drive papers | `02_PROJECT_ATLAS/01_THERAPEUTIC_ALLIANCE/manuscript.md` | 📋 Capture needed |

**Note:** Project Atlas research materials currently live in Google Drive. These should be migrated to the repo or symlinked if they're actively edited in Google Workspace.

**Status:** REQUIRES POPULATION + STRUCTURAL CREATION

---

# PILLAR 03: INTELLECTUAL_ESTATE

**Current state:**
- No dedicated folder
- Book (Tao) scattered in root `Tao/`
- Papers external
- Frameworks mixed in projects
- Decision logs fragmented

**Target state:**
```
03_INTELLECTUAL_ESTATE/
├── README.md                     New: Estate overview
│
├── BOOKS/
│   ├── The-Tao-of-Clinical-Touch/
│   │   ├── README.md
│   │   ├── manuscript-final.md
│   │   ├── cover/
│   │   ├── proofs/
│   │   ├── metadata.md
│   │   ├── amazon-record.txt
│   │   ├── publishing-notes.md
│   │   └── marketing/
│   │       ├── messaging.md
│   │       ├── reviews/
│   │       └── social-assets/
│   │
│   └── (future books)
│
├── PAPERS/
│   ├── therapeutic-alliance/
│   ├── stand-architecture/
│   └── (future papers)
│
├── FRAMEWORKS/
│   ├── clinical-reasoning/
│   ├── therapeutic-alliance/
│   ├── nervous-system-regulation/
│   └── permission-based-practice/
│
├── METHODOLOGIES/
│   ├── clinical-teaching/
│   ├── course-design/
│   └── research-protocol/
│
├── DECISION_LOGS/
│   ├── business-decisions.md      New: Consolidated log
│   ├── clinical-decisions.md      New: Consolidated log
│   ├── product-decisions.md       New: Consolidated log
│   └── research-decisions.md      New: Consolidated log
│
└── ARCHIVE/
    ├── historical/
    ├── retired-projects/
    └── legacy-work/
```

**Migrations:**
| From | To | Action |
|---|---|---|
| `Tao/tao_interior_final.docx` | `03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/manuscript-final.docx` | Move |
| `Tao/Tao_Clinical_Touch_Cover_*` | `03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/cover/` | Move |
| `Tao/Launch Messaging Pack.md` | `03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/messaging.md` | Move |
| `Tao/Reviewer Outreach Tracker.md` | `03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/reviews.md` | Move |
| `Tao/Social Media Launch System.md` | `03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/social.md` | Move |
| Google Drive papers | `03_INTELLECTUAL_ESTATE/PAPERS/*/` | 📋 Capture needed |
| Project decision logs | `03_INTELLECTUAL_ESTATE/DECISION_LOGS/` | Consolidate + organize |
| `archive/` | `03_INTELLECTUAL_ESTATE/ARCHIVE/` | Move |

**Status:** REQUIRES MAJOR MIGRATION + CONTENT CAPTURE

---

# ORGANIZATION 04: DREW_FREEDMAN

**Current state:**
- Scattered across root + other folders
- No dedicated organization folder

**Target state:**
```
04_DREW_FREEDMAN/
├── README.md                     New: Founder bio + vision
├── BIOGRAPHY.md                  📋 Needs creation
├── PHILOSOPHY.md                 📋 Consolidate + expand
├── VISION_STATEMENT.md           📋 Needs creation
├── ORIGIN_STORY.md               📋 Needs creation
│
├── PERSONAL_WRITING/
│   ├── journals/                 📋 Needs capture
│   ├── essays/                   📋 Needs capture
│   ├── reflections/              📋 Needs capture
│   └── notes/
│
├── SPEAKING/
│   ├── presentations/            📋 Needs capture
│   ├── talks/                    📋 Needs capture
│   ├── media-appearances/        📋 Needs capture
│   └── interviews/               📋 Needs capture
│
├── PROJECTS/
│   └── books/
│       └── the-tao-of-clinical-touch/
│           └── (symlink to 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao/
│               OR move there permanently)
│
├── RELATIONSHIPS/
│   ├── network.md                📋 Needs creation
│   ├── mentors.md                📋 Needs creation
│   └── collaborators.md          📋 Needs creation
│
└── DECISION_HISTORY/
    ├── business-decisions.md     📋 Consolidate
    ├── career-pivots.md          📋 Needs creation
    └── strategic-choices.md      📋 Needs creation
```

**Note:** The Tao book may belong here (Drew's personal project) or in 03_INTELLECTUAL_ESTATE. Constitutional clarification needed from Drew.

**Status:** REQUIRES STRUCTURAL CREATION + CONTENT CAPTURE

---

# ORGANIZATION 05: THE_BOSTON_BODYWORKER

**Current state:**
- Minimal (1 file only)
- Website external (bostonbodyworker.com)
- Content not versioned
- Misclassified as "legacy" (Constitution says "appreciating intellectual asset")

**Target state:**
```
05_THE_BOSTON_BODYWORKER/
├── README.md                     New: Publishing platform charter
├── PHILOSOPHY.md                 New: Clinical + professional philosophy
│
├── WEBSITE/
│   ├── architecture.md           📋 Website structure
│   ├── seo-assets.md             📋 SEO tracking
│   └── (WordPress export if available)
│
├── WRITING/
│   ├── ARTICLES/
│   │   ├── clinical-articles/    📋 Archive blog posts
│   │   ├── educational-essays/   📋 Archive essays
│   │   └── guest-contributions/  📋 Archive external writing
│   │
│   ├── NEWSLETTER/
│   │   └── archive/              📋 Newsletter backlog
│   │
│   └── PUBLICATIONS/
│       └── (Published works)
│
├── MEDIA/
│   ├── images/                   📋 Professional photos
│   ├── video/                    📋 Recorded content
│   └── audio/                    📋 Podcast/recorded interviews
│
├── AUTHORITY/
│   ├── testimonials.md           📋 Client testimonials
│   ├── credentials.md            📋 Certifications + authority
│   └── timeline.md               📋 30-year evolution
│
└── DECISION_LOG.md               📋 Strategic decisions
```

**Note:** This requires large-scale content migration from external website. Should be prioritized as secondary to pillars.

**Status:** REQUIRES STRUCTURAL CREATION + EXTERNAL CONTENT MIGRATION

---

# ORGANIZATION 06: LEARN2TAPE

**Current state:**
- `Learn2Tape/` folder (50 files)
- Well-organized relative to others
- Some orphaned root files (GTM, diagnostics)

**Target state:**
```
06_LEARN2TAPE/
├── README.md                     Move: PROJECT_CONTROL.md
│
├── PRODUCTS/
│   ├── k-cuts/
│   │   ├── README.md
│   │   ├── SPECS.md
│   │   ├── CURRICULUM.md         📋 Needs structure
│   │   └── marketing/
│   │
│   └── courses/
│       └── (course structure)
│
├── MARKETING/
│   ├── STRATEGY.md               New: Overall strategy
│   ├── GOOGLE_ADS.md             Move: learn2tape_google_ads.md
│   ├── GTM_FUNNEL.md             Move: GTM_CONVERSION_FUNNEL_SUMMARY.md
│   ├── GTM_V26_FIX.md            Move: GTM_V26_ECOMMERCE_PAYLOAD_FIX.md
│   ├── BREVO_WORKFLOW.md         Move: Brevo_Implementation_Workflow_Claude.md
│   ├── DIAGNOSTICS.md            Move: google_ads_7_day_diagnostic.md
│   ├── DIAGNOSTICS_20260417.md   Move: learn2tape_ads_diagnostic_2026-04-17.md
│   │
│   ├── CAMPAIGNS/
│   │   └── ncb/
│   │       ├── WORKFLOW.md       Move: NCB_LIST_CLEANING_WORKFLOW.md
│   │       ├── DATA/
│   │       │   ├── lists/        Move: NCB_*.csv, NCB_VALID_*.csv
│   │       │   ├── zerobounce/   Move: NCB_PHASE1_UNZIPPED/
│   │       │   └── by-state/     Move: state_splits/
│   │       ├── BATCHES/
│   │       │   └── NCB_MA_Batch_Day*.csv
│   │       └── SCRIPTS/
│   │           ├── brevo_import_lists.py
│   │           └── split_by_state.py
│   │
│   └── PERFORMANCE/
│       └── PHASE2_VALIDATION.md  Move: L2T_PHASE2_VALIDATION_REPORT.md
│
├── PLATFORM/
│   ├── LMS/
│   │   ├── ARCHITECTURE.md
│   │   └── PLUGIN_NOTES.md
│   │
│   ├── WOOCOMMERCE/
│   │   ├── PRODUCT_COPY.md       Move: woocommerce_product_page_copy.md
│   │   ├── PAYMENT_FIX.md        📋 Incident log
│   │   └── SECURITY_NOTES.md     📋 reCAPTCHA incident
│   │
│   └── INTEGRATIONS/
│       ├── DROPBOX.md            📋 Video transfer
│       ├── PAYPAL.md             📋 Payment processing
│       └── EMAIL.md              📋 Brevo + email ops
│
├── OPERATIONS/
│   ├── DECISION_LOG.md
│   └── INCIDENT_LOG.md           New: Track issues
│
└── STUDENTS/
    └── (Metadata if applicable)
```

**Migrations:**
| From | To | Action |
|---|---|---|
| `Learn2Tape/PROJECT_CONTROL.md` | `06_LEARN2TAPE/README.md` | Rename + move |
| `Learn2Tape/learn2tape_google_ads.md` | `06_LEARN2TAPE/marketing/GOOGLE_ADS.md` | Rename + move |
| `GTM_CONVERSION_FUNNEL_SUMMARY.md` | `06_LEARN2TAPE/marketing/GTM_FUNNEL.md` | Move |
| `GTM_V26_ECOMMERCE_PAYLOAD_FIX.md` | `06_LEARN2TAPE/marketing/GTM_V26_FIX.md` | Move |
| `L2T_PHASE2_VALIDATION_REPORT.md` | `06_LEARN2TAPE/marketing/PHASE2_VALIDATION.md` | Move |
| `learn2tape_ads_diagnostic_2026-04-17.md` | `06_LEARN2TAPE/marketing/DIAGNOSTICS_20260417.md` | Move |
| (All NCB files) | `06_LEARN2TAPE/marketing/CAMPAIGNS/ncb/` | Move + organize |

**Status:** MOSTLY ALIGNED — REQUIRES CONSOLIDATION + ORPHANED FILE MIGRATION

---

# ORGANIZATION 07: STITCHCORE

**Current state:**
- `SidekickAir/` folder (34 files)
- Well-organized + documented
- Constitutional question: Is this StitchCore or just Sidekick Air?

**Target state (Constitutional Clarification Needed):**

**Option A: StitchCore as parent organization**
```
07_STITCHCORE/
├── README.md                     New: StitchCore charter
├── PLATFORM_DEFINITION.md        Move: stitchcore_platform_definition.md
├── AERO_STITCH_CORE/
│   └── TECHNOLOGY.md             Move: aerostitch_core_technology_definition.md
│
├── PRODUCTS/
│   └── sidekick-air/
│       ├── README.md             Move: sidekick_air_master_index.md
│       ├── BRIEF.md              Move: sidekick_air_project_master_brief.md
│       ├── SPECS.md              Move: sidekick_air_technical_specs.md
│       │
│       ├── PRODUCT/
│       │   ├── concept.png
│       │   └── prototype-notes.md
│       │
│       ├── STRATEGY/
│       │   ├── ROADMAP.md        Move: sidekick_air_roadmap.md
│       │   ├── CATEGORY.md       Move: sidekick_air_category_creation.md
│       │   ├── VALIDATION.md     Move: sidekick_air_validation_milestones.md
│       │   └── WAR_MAP.md        Move: sidekick_air_war_map.md
│       │
│       ├── PLATFORM/
│       │   └── (platform-specific docs)
│       │
│       ├── IP/
│       │   └── ARCHITECTURE.md   Move: sidekick_air_ip_architecture.md
│       │
│       ├── LOGS/
│       │   ├── FOUNDER_LOG.md    Move: founder_log.md
│       │   └── DECISION_LOG.md   Move: sidekick_air_decision_log.md
│       │
│       ├── MANUFACTURING.md      Move: sidekick_air_manufacturing_brief.md
│       ├── OPEN_DECISIONS.md     Move: sidekick_air_open_decisions.md
│       │
│       └── PARTNERS/
│           ├── pacmar/
│           │   ├── BUSINESS_PLAN.md
│           │   ├── EXECUTIVE_SUMMARY.md
│           │   └── (other materials)
│           ├── dropstitch-technologies/
│           │   └── (tech spec + research)
│           └── (other potential manufacturers)
│
├── ENGINEERING/
│   ├── STANDARDS.md              📋 Needs creation
│   ├── DESIGN_DOCS.md            📋 CAD + technical drawings
│   └── TESTING.md                📋 Needs creation
│
├── PATENTS/
│   ├── FILING_STRATEGY.md        📋 Provisional patent record
│   └── DOCUMENTATION.md          📋 Patent materials
│
└── OPERATIONS/
    ├── DECISION_LOG.md
    └── INVESTORS.md              📋 Investor relationships
```

**Option B: Sidekick Air as standalone (if StitchCore is undefined)**
```
07_SIDEKICK_AIR/
├── (same structure as Option A, but at organization level)
```

**Status:** MOSTLY ALIGNED — REQUIRES CLARIFICATION ON StitchCore scope + consolidation

---

# HORIZONTAL SYSTEMS (Not organizations, not pillars)

## Marketing

Marketing serves all organizations.

**Current state:**
- `07_MARKETING/` folder (mostly empty except tracking/)
- Marketing assets scattered in projects

**Target state:**
```
01_OPERATING_SYSTEM/
└── MARKETING/
    ├── STRATEGY.md               New: Global marketing charter
    ├── SYSTEMS.md                New: Shared marketing systems
    ├── TEMPLATES/
    ├── BRAND_GUIDELINES.md
    └── CAMPAIGNS/
        └── (Cross-org campaigns like Atlas marketing)
```

Individual organizations keep local marketing (Learn2Tape/marketing/, etc.), but global strategy lives in operating system.

---

# DEPRECATED FOLDERS (To be retired)

| Folder | Fate | Reason |
|---|---|---|
| `_system/` | Rename to `01_OPERATING_SYSTEM/` | Pillar alignment |
| `06_Project_Atlas/` (empty) | Populate as `02_PROJECT_ATLAS/` | Pillar alignment |
| `07_MARKETING/` | Integrate into `01_OPERATING_SYSTEM/MARKETING/` | Operating system layer |
| `_projects/` | Retire or convert to symlinks | Rendered obsolete by org structure |
| `_support/` | Integrate into `01_OPERATING_SYSTEM/` | Operating system asset |
| `archive/` | Move to `03_INTELLECTUAL_ESTATE/ARCHIVE/` | Estate preservation |

---

# EXECUTION PHASES

## Phase 1: Pillars (Days 1-3)
- Create 00_CONSTITUTION (done ✅)
- Rename/reorganize 01_OPERATING_SYSTEM
- Populate 02_PROJECT_ATLAS (core structure)
- Create 03_INTELLECTUAL_ESTATE (core structure)

## Phase 2: Organizations (Days 3-5)
- Create 04_DREW_FREEDMAN structure
- Activate 05_THE_BOSTON_BODYWORKER structure
- Consolidate 06_LEARN2TAPE
- Clarify + reorganize 07_STITCHCORE

## Phase 3: Content Migration (Days 5+)
- Move Tao book → 03_INTELLECTUAL_ESTATE/BOOKS/ or 04_DREW_FREEDMAN/projects/books/
- Migrate Project Atlas research from Google Drive → 02_PROJECT_ATLAS/
- Consolidate Learn2Tape orphaned files
- Capture Boston Bodyworker historical content from website

## Phase 4: Archive & Cleanup (Day 6)
- Move archive → 03_INTELLECTUAL_ESTATE/ARCHIVE/
- Delete ephemeral files
- Create .gitignore
- Generate initial GitHub repo

---

# BLOCKED DECISIONS FOR DREW

Before Phase 2 execution, clarification needed:

### Decision 1: The Tao Book
**Question:** Does The Tao belong in:
- [ ] `04_DREW_FREEDMAN/projects/books/the-tao/` (founder's personal project)
- [ ] `03_INTELLECTUAL_ESTATE/BOOKS/the-tao/` (enduring publication)
- [ ] Both (with symlink)?

**Impact:** Determines whether it lives under founder or estate.

### Decision 2: StitchCore Scope
**Question:** Is StitchCore currently:
- [ ] Defined as an organization (with multiple future products)?
- [ ] Just Sidekick Air (Sidekick Air IS the product)?
- [ ] Placeholder for future innovation org?

**Impact:** Determines if we create 07_STITCHCORE or 07_SIDEKICK_AIR.

### Decision 3: Boston Bodyworker Priority
**Question:** Should we prioritize capturing Boston Bodyworker content:
- [ ] High priority (active appreciating asset, needs systematic capture)
- [ ] Medium priority (post-launch project, lower urgency)
- [ ] Low priority (external website sufficient for now)?

**Impact:** Determines Phase 2 vs. Phase 3 vs. backlog.

### Decision 4: Project Atlas Content
**Question:** Should we migrate Project Atlas research from Google Drive to GitHub:
- [ ] Yes, move everything (make GitHub source of truth)
- [ ] Partial, move papers only (keep research in Drive)
- [ ] Link/symlink (reference Drive from repo)?

**Impact:** Determines integration depth + external dependency.

---

# SUMMARY

Constitution-aligned migration is **entity-centric** instead of project-centric.

This repositions:
- Organizations as primary (entities outlive projects)
- Pillars as structural anchors
- Projects as children of organizations
- Knowledge as permanent estate

**Current constitutional alignment: ~38%**

**Target alignment post-migration: ~90%+**

**No files deleted. All knowledge preserved.**

Next: Await Drew decisions, then execute Phase 1 (pillars).

