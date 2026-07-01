# Finding My Wei — Final Repository Architecture
## Version 2.0
## Constitutional Authority: Repository Constitution v2.0
## Implementation Authority: Implementation Directive
## Date: June 30, 2026
## Status: APPROVED FOR EXECUTION

---

# Repository Structure

```
finding-my-wei/
│
├── 00_CONSTITUTION/
│   ├── CONSTITUTION.md
│   ├── AMENDMENTS.md
│   ├── GOVERNANCE.md
│   └── AUTHORITY.md
│
├── 01_OPERATING_SYSTEM/
│   ├── README.md
│   ├── PRINCIPLES.md
│   ├── COLLABORATION.md (was SOUL.md)
│   │
│   ├── MEMORY/
│   │   ├── MEMORY.md
│   │   ├── project_*.md
│   │   ├── user_*.md
│   │   ├── feedback_*.md
│   │   └── reference_*.md
│   │
│   ├── AUTOMATION/
│   │   ├── HEARTBEAT.md
│   │   ├── SYNC_PROTOCOLS.md
│   │   └── TRIGGERS.md
│   │
│   ├── AI_GUIDELINES/
│   │   ├── CLAUDE_LIBRARIAN.md
│   │   ├── CHATGPT_RESEARCH.md
│   │   └── PROMPT_LIBRARY.md
│   │
│   ├── TOOLS/
│   │   ├── GITHUB_WORKFLOW.md
│   │   ├── NOTION_SYNC.md
│   │   └── (other tools)
│   │
│   ├── PREFERENCES/
│   │   └── USER.md
│   │
│   └── MARKETING/
│       ├── STRATEGY.md
│       ├── SYSTEMS.md
│       ├── TEMPLATES/
│       ├── BRAND_GUIDELINES.md
│       └── CAMPAIGNS/
│
├── 02_PROJECT_ATLAS/
│   ├── README.md
│   ├── ROADMAP.md
│   ├── INVESTIGATION_PROTOCOL.md
│   │
│   ├── 01_THERAPEUTIC_ALLIANCE/
│   │   ├── README.md
│   │   ├── FRAMEWORK.md
│   │   ├── research/
│   │   │   ├── notes.md
│   │   │   ├── sources.md
│   │   │   └── data/
│   │   ├── manuscript.md
│   │   └── assets/
│   │
│   ├── 02_STAND_ARCHITECTURE/
│   │   ├── README.md
│   │   ├── FRAMEWORK.md
│   │   ├── research/
│   │   ├── manuscript.md
│   │   └── assets/
│   │
│   ├── 03-05_FUTURE_PAPERS/
│   │   └── (Placeholder structure)
│   │
│   ├── marketing/
│   │   ├── CAMPAIGN_ROADMAP.md
│   │   ├── redirects.md
│   │   ├── redirect_log.md
│   │   └── ga4_repair.md
│   │
│   └── publications/
│       ├── books/
│       ├── papers/
│       ├── presentations/
│       └── courses/
│
├── 03_INTELLECTUAL_ESTATE/
│   ├── README.md
│   │
│   ├── BOOKS/
│   │   ├── The-Tao-of-Clinical-Touch/
│   │   │   ├── README.md
│   │   │   ├── manuscript-final.docx
│   │   │   ├── manuscript-final.pdf
│   │   │   ├── metadata.md
│   │   │   ├── publication-record.md
│   │   │   │
│   │   │   ├── cover/
│   │   │   ├── proofs/
│   │   │   ├── editions/
│   │   │   │   ├── 1st-edition-notes.md
│   │   │   │   └── (future editions)
│   │   │   │
│   │   │   └── marketing/
│   │   │       ├── messaging.md
│   │   │       ├── reviews/
│   │   │       └── social-assets/
│   │   │
│   │   └── (Future books)
│   │
│   ├── PAPERS/
│   │   ├── therapeutic-alliance/
│   │   ├── stand-architecture/
│   │   └── (future papers)
│   │
│   ├── FRAMEWORKS/
│   │   ├── clinical-reasoning/
│   │   ├── therapeutic-alliance/
│   │   ├── nervous-system-regulation/
│   │   └── permission-based-practice/
│   │
│   ├── METHODOLOGIES/
│   │   ├── clinical-teaching/
│   │   ├── course-design/
│   │   └── research-protocol/
│   │
│   ├── DECISION_LOGS/
│   │   ├── business-decisions.md
│   │   ├── clinical-decisions.md
│   │   ├── product-decisions.md
│   │   └── research-decisions.md
│   │
│   └── ARCHIVE/
│       ├── historical/
│       ├── retired-projects/
│       └── legacy-work/
│
├── 04_ENTITIES/
│   │
│   ├── DREW_FREEDMAN/
│   │   ├── README.md
│   │   ├── BIOGRAPHY.md
│   │   ├── PHILOSOPHY.md
│   │   ├── VISION_STATEMENT.md
│   │   ├── ORIGIN_STORY.md
│   │   │
│   │   ├── PERSONAL_WRITING/
│   │   │   ├── journals/
│   │   │   ├── essays/
│   │   │   ├── reflections/
│   │   │   └── notes/
│   │   │
│   │   ├── SPEAKING/
│   │   │   ├── presentations/
│   │   │   ├── talks/
│   │   │   ├── media-appearances/
│   │   │   └── interviews/
│   │   │
│   │   ├── PROJECTS/
│   │   │   ├── books/
│   │   │   │   └── (in-development books)
│   │   │   └── creative-work/
│   │   │
│   │   ├── RELATIONSHIPS/
│   │   │   ├── network.md
│   │   │   ├── mentors.md
│   │   │   └── collaborators.md
│   │   │
│   │   ├── DECISION_HISTORY/
│   │   │   ├── business-decisions.md
│   │   │   ├── career-pivots.md
│   │   │   └── strategic-choices.md
│   │   │
│   │   └── PERSONAL_LEGACY/
│   │       └── (legacy work + personal IP)
│   │
│   ├── THE_BOSTON_BODYWORKER/
│   │   ├── README.md
│   │   ├── CHARTER.md
│   │   ├── PHILOSOPHY.md
│   │   │
│   │   ├── WEBSITE/
│   │   │   ├── architecture.md
│   │   │   ├── seo-assets.md
│   │   │   └── (WordPress export if available)
│   │   │
│   │   ├── WRITING/
│   │   │   ├── ARTICLES/
│   │   │   │   ├── clinical-articles/
│   │   │   │   ├── educational-essays/
│   │   │   │   └── guest-contributions/
│   │   │   │
│   │   │   ├── NEWSLETTER/
│   │   │   │   └── archive/
│   │   │   │
│   │   │   └── PUBLICATIONS/
│   │   │       └── (Published works)
│   │   │
│   │   ├── MEDIA/
│   │   │   ├── images/
│   │   │   ├── video/
│   │   │   └── audio/
│   │   │
│   │   ├── AUTHORITY/
│   │   │   ├── testimonials.md
│   │   │   ├── credentials.md
│   │   │   └── timeline.md
│   │   │
│   │   ├── OPERATIONS/
│   │   │   ├── DECISION_LOG.md
│   │   │   └── MIGRATION_LOG.md
│   │   │
│   │   └── INTELLECTUAL_PROPERTY/
│   │       └── (IP assets)
│   │
│   ├── LEARN2TAPE/
│   │   ├── README.md
│   │   ├── CHARTER.md
│   │   │
│   │   ├── PRODUCTS/
│   │   │   ├── k-cuts/
│   │   │   │   ├── README.md
│   │   │   │   ├── SPECS.md
│   │   │   │   ├── CURRICULUM.md
│   │   │   │   └── marketing/
│   │   │   │
│   │   │   └── courses/
│   │   │       ├── README.md
│   │   │       └── (course structure)
│   │   │
│   │   ├── MARKETING/
│   │   │   ├── STRATEGY.md
│   │   │   ├── GOOGLE_ADS.md
│   │   │   ├── GTM_FUNNEL.md
│   │   │   ├── GTM_V26_FIX.md
│   │   │   ├── BREVO_WORKFLOW.md
│   │   │   ├── DIAGNOSTICS.md
│   │   │   │
│   │   │   ├── CAMPAIGNS/
│   │   │   │   └── ncb/
│   │   │   │       ├── WORKFLOW.md
│   │   │   │       ├── DATA/
│   │   │   │       │   ├── lists/
│   │   │   │       │   ├── zerobounce/
│   │   │   │       │   └── by-state/
│   │   │   │       ├── BATCHES/
│   │   │   │       └── SCRIPTS/
│   │   │   │
│   │   │   └── PERFORMANCE/
│   │   │       └── PHASE2_VALIDATION.md
│   │   │
│   │   ├── PLATFORM/
│   │   │   ├── LMS/
│   │   │   │   ├── ARCHITECTURE.md
│   │   │   │   └── PLUGIN_NOTES.md
│   │   │   │
│   │   │   ├── WOOCOMMERCE/
│   │   │   │   ├── PRODUCT_COPY.md
│   │   │   │   ├── PAYMENT_FIX.md
│   │   │   │   └── SECURITY_NOTES.md
│   │   │   │
│   │   │   └── INTEGRATIONS/
│   │   │       ├── DROPBOX.md
│   │   │       ├── PAYPAL.md
│   │   │       └── EMAIL.md
│   │   │
│   │   ├── OPERATIONS/
│   │   │   ├── DECISION_LOG.md
│   │   │   └── INCIDENT_LOG.md
│   │   │
│   │   └── STUDENTS/
│   │       └── (Metadata if applicable)
│   │
│   └── STITCHCORE/
│       ├── README.md
│       ├── CHARTER.md
│       ├── PLATFORM_DEFINITION.md
│       │
│       ├── AERO_STITCH_CORE/
│       │   └── TECHNOLOGY.md
│       │
│       ├── PRODUCTS/
│       │   ├── SIDEKICK_AIR/
│       │   │   ├── README.md
│       │   │   ├── BRIEF.md
│       │   │   ├── SPECS.md
│       │   │   │
│       │   │   ├── PRODUCT/
│       │   │   │   ├── concept.png
│       │   │   │   └── prototype-notes.md
│       │   │   │
│       │   │   ├── STRATEGY/
│       │   │   │   ├── ROADMAP.md
│       │   │   │   ├── CATEGORY.md
│       │   │   │   ├── VALIDATION.md
│       │   │   │   └── WAR_MAP.md
│       │   │   │
│       │   │   ├── PLATFORM/
│       │   │   │   └── (platform-specific docs)
│       │   │   │
│       │   │   ├── IP/
│       │   │   │   └── ARCHITECTURE.md
│       │   │   │
│       │   │   ├── LOGS/
│       │   │   │   ├── FOUNDER_LOG.md
│       │   │   │   └── DECISION_LOG.md
│       │   │   │
│       │   │   ├── MANUFACTURING.md
│       │   │   ├── OPEN_DECISIONS.md
│       │   │   │
│       │   │   └── PARTNERS/
│       │   │       ├── pacmar/
│       │   │       ├── dropstitch-technologies/
│       │   │       └── (other partners)
│       │   │
│       │   └── (FUTURE_PRODUCTS placeholder)
│       │
│       ├── ENGINEERING/
│       │   ├── STANDARDS.md
│       │   ├── DESIGN_DOCS.md
│       │   └── TESTING.md
│       │
│       ├── PATENTS/
│       │   ├── FILING_STRATEGY.md
│       │   └── DOCUMENTATION.md
│       │
│       ├── MANUFACTURING/
│       │   ├── SUPPLIERS.md
│       │   ├── PROCESSES.md
│       │   └── QUALITY.md
│       │
│       ├── OPERATIONS/
│       │   ├── DECISION_LOG.md
│       │   └── INVESTORS.md
│       │
│       └── OEM/
│           └── PARTNERSHIPS.md
│
├── README.md
├── .gitignore
├── LICENSE
└── .github/
    ├── workflows/
    └── PULL_REQUEST_TEMPLATE.md
```

---

# Key Design Principles

## 1. Entity-Driven

Organizations (entities) are primary.

Projects belong to organizations.

No orphaned projects.

## 2. Relationships Preserved

Every asset's relationships to other assets are preserved through folder structure.

Example: The Tao appears in both:
- `04_ENTITIES/DREW_FREEDMAN/PROJECTS/books/` (creation)
- `03_INTELLECTUAL_ESTATE/BOOKS/` (completion)

## 3. 20-Year Test

Every folder should make sense 20 years from now.

Folder names describe what the asset is, not when it was created.

## 4. Preservation Principle

No folder is deleted.

Historical material is archived, not discarded.

## 5. Horizontal Systems

Marketing, automation, and tools are horizontal layers that serve all entities.

They don't belong to a single organization.

## 6. Clear Authority

Each folder has clear ownership:
- Drew Freedman entity owns his creative work
- Learn2Tape entity owns education products
- StitchCore entity owns innovation products
- Project Atlas owns cross-organizational research
- Intellectual Estate owns permanent knowledge

## 7. Scalability

Architecture accommodates growth:
- Future entities can be added to `04_ENTITIES/`
- Future products can be added to `STITCHCORE/PRODUCTS/`
- Future papers can be added to `PROJECT_ATLAS/`
- Future books can be added to `DREW_FREEDMAN/PROJECTS/books/` and `INTELLECTUAL_ESTATE/BOOKS/`

---

# Relationships Between Layers

## Creation → Completion Flow

```
04_DREW_FREEDMAN/PROJECTS/books/
        ↓
    (Writing, editing, evolution)
        ↓
03_INTELLECTUAL_ESTATE/BOOKS/
        ↓
    (Published, finalized, preserved)
```

## Investigation → Publication Flow

```
02_PROJECT_ATLAS/01_THERAPEUTIC_ALLIANCE/
        ↓
    (Research, notes, analysis)
        ↓
02_PROJECT_ATLAS/publications/
        ↓
    (Synthesized knowledge)
        ↓
03_INTELLECTUAL_ESTATE/
        ↓
    (Permanent record)
```

## Entity → Intellectual Estate Flow

```
04_ENTITIES/LEARN2TAPE/PRODUCTS/
        ↓
    (Course development)
        ↓
03_INTELLECTUAL_ESTATE/FRAMEWORKS/
        ↓
    (Methodology documented)
```

---

# Stage One Execution

### Immediate Actions (Next 2-3 hours)

1. ✅ Create 00_CONSTITUTION/ folder + CONSTITUTION.md
2. ✅ Rename _system/ → 01_OPERATING_SYSTEM/ + reorganize
3. ✅ Create 02_PROJECT_ATLAS/ structure (empty but organized)
4. ✅ Create 03_INTELLECTUAL_ESTATE/ structure (empty but organized)
5. ✅ Create 04_ENTITIES/ folder structure
   - ✅ DREW_FREEDMAN/
   - ✅ THE_BOSTON_BODYWORKER/
   - ✅ LEARN2TAPE/
   - ✅ STITCHCORE/

### Deferred Actions (Stage Two)

- Content migration (gradual)
- Historical document evaluation
- External content capture (Boston Bodyworker website, Google Drive papers)
- Relationship preservation and linking

---

# Repository Success Criteria

Finding My Wei succeeds when:

- ✅ Knowledge is never lost
- ✅ Entities remain primary organizational units
- ✅ Projects are clearly owned by entities
- ✅ Relationships between assets are preserved
- ✅ Architecture makes sense 20 years from now
- ✅ Every meaningful asset has a permanent home
- ✅ Future collaborators understand the structure without explanation

This is a permanent architecture, not a temporary organizing system.

---

**Status: Ready for Stage One Execution**

**Authority: Claude (Chief Librarian), approved by Drew Freedman**

**Next step: Create the constitutional architecture**
