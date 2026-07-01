# RECOMMENDED REPOSITORY TREE — Finding My Wei Structure

**Date:** June 30, 2026  
**Status:** DRAFT — Based on migration map assumptions  
**Scope:** Target structure post-migration to GitHub

---

## DIRECTORY STRUCTURE

```
/ (root)
│
├── README.md                           # Master project overview + quick links
├── LICENSE                             # If publishing (recommend MIT or CC)
├── .gitignore                          # Version control exclusions
│   └── (node_modules/, .DS_Store, .claude/settings.local.json, etc.)
│
├── .github/
│   ├── workflows/                      # CI/CD automation
│   │   └── (GitHub Actions if used)
│   └── PULL_REQUEST_TEMPLATE.md        # PR guidelines
│
├── docs/                               # GitHub-native documentation
│   ├── README.md                       # Docs index
│   ├── ARCHITECTURE.md                 # Repo architecture + conventions
│   ├── CONTRIBUTING.md                 # Contribution guidelines
│   │
│   ├── SOUL.md                         # Collaboration + voice (from _system/)
│   ├── USER.md                         # Drew preferences + constraints
│   ├── HEARTBEAT.md                    # Daily brief automation rules
│   ├── RULES.md                        # Repository operating principles
│   │
│   ├── memory/                         # Long-term project memory (versioned)
│   │   ├── MEMORY.md                   # Master index
│   │   ├── project_*.md                # Project-specific memories
│   │   ├── user_*.md                   # User preferences + patterns
│   │   ├── feedback_*.md               # Decision records + learnings
│   │   └── reference_*.md              # External system mappings
│   │
│   ├── compliance/                     # Regulatory + legal docs
│   │   ├── 269-CMR-4.pdf               # MA continuing ed regulations
│   │   └── (other compliance docs)
│   │
│   └── support/                        # Supporting research + templates
│       ├── STITCHCORE_PARTNERS.md      # Manufacturer research
│       └── (other reference docs)
│
├── projects/                           # All active business projects
│   │
│   ├── sidekick-air/                   # Portable therapy table + StitchCore
│   │   ├── README.md                   # Project overview
│   │   │
│   │   ├── product/
│   │   │   ├── BRIEF.md                # Master product specification
│   │   │   └── SPECS.md                # Technical requirements
│   │   │
│   │   ├── strategy/
│   │   │   ├── ROADMAP.md              # Product roadmap + milestones
│   │   │   ├── CATEGORY.md             # Market positioning
│   │   │   ├── MILESTONES.md           # Validation gates + proof points
│   │   │   └── STITCHCORE_ROADMAP.md   # Platform-level roadmap
│   │   │
│   │   ├── platform/
│   │   │   ├── DEFINITION.md           # StitchCore platform charter
│   │   │   └── AEROSTITCH.md           # Core technology definition
│   │   │
│   │   ├── ip/
│   │   │   └── ARCHITECTURE.md         # IP strategy + patent tracking
│   │   │
│   │   ├── logs/
│   │   │   ├── FOUNDER_LOG.md          # Founder decision record
│   │   │   └── DECISION_LOG.md         # Technical decisions
│   │   │
│   │   ├── MANUFACTURING.md            # Manufacturer coordination + specs
│   │   ├── WAR_MAP.md                  # Competitive landscape + strategy
│   │   ├── OPEN_DECISIONS.md           # Unresolved issues + options
│   │   ├── AI_SETUP.md                 # AI assistant configuration
│   │   ├── context.yaml                # Project metadata
│   │   │
│   │   ├── partners/
│   │   │   ├── pacmar/
│   │   │   │   ├── 1_BUSINESS_PLAN.md
│   │   │   │   ├── 2_EXECUTIVE_SUMMARY.md
│   │   │   │   ├── 3_ONE_PAGE_BRIEF.md
│   │   │   │   ├── 4_TECHNICAL_APPENDIX.md
│   │   │   │   └── 5_ENGINEERING_ASSUMPTIONS.md
│   │   │   ├── dropstitch-technologies/
│   │   │   │   └── (spec + research)
│   │   │   └── (other potential manufacturers)
│   │   │
│   │   └── product/
│   │       ├── SKA_Prototype2_Concept.png
│   │       └── (CAD files when ready)
│   │
│   ├── learn2tape/                     # Online CE course platform
│   │   ├── README.md                   # Project overview
│   │   │
│   │   ├── product/
│   │   │   ├── COPY.md                 # Product page content
│   │   │   └── (course spec docs)
│   │   │
│   │   ├── marketing/
│   │   │   ├── GOOGLE_ADS.md           # Ad strategy + performance
│   │   │   ├── GTM_FUNNEL.md           # GTM conversion tracking setup
│   │   │   ├── GTM_V26_FIX.md          # Historical fix record
│   │   │   ├── BREVO_WORKFLOW.md       # Email infrastructure setup
│   │   │   ├── DIAGNOSTICS.md          # Performance analysis
│   │   │   ├── DIAGNOSTICS_20260417.md # Historical diagnostic
│   │   │   └── PHASE2_VALIDATION.md    # Phase completion report
│   │   │
│   │   ├── campaigns/
│   │   │   └── ncb/
│   │   │       ├── WORKFLOW.md         # List cleaning + segmentation process
│   │   │       ├── data/
│   │   │       │   ├── NCB_LIST_CLEANED.csv
│   │   │       │   ├── NCB_VALID_BREVO_READY.csv
│   │   │       │   ├── zerobounce-results/
│   │   │       │   │   ├── abuse/
│   │   │       │   │   ├── catch_all/
│   │   │       │   │   ├── invalid/
│   │   │       │   │   ├── spamtrap/
│   │   │       │   │   ├── valid/
│   │   │       │   │   └── overview.pdf
│   │   │       │   └── by-state/
│   │   │       │       ├── BREVO_CA_Batch*.csv
│   │   │       │       ├── BREVO_CO_Batch*.csv
│   │   │       │       ├── BREVO_FL_Batch*.csv
│   │   │       │       ├── BREVO_MA.csv
│   │   │       │       └── (other states)
│   │   │       ├── batches/
│   │   │       │   ├── NCB_MA_Batch_Day1.csv
│   │   │       │   ├── NCB_MA_Batch_Day2.csv
│   │   │       │   └── ... (Day 3-6)
│   │   │       └── scripts/
│   │   │           ├── brevo_import_lists.py
│   │   │           └── split_by_state.py
│   │   │
│   │   └── PHASE2_VALIDATION.md        # Phase completion
│   │
│   ├── tao/                            # The Tao of Clinical Touch
│   │   ├── README.md                   # Project overview
│   │   │
│   │   ├── book/
│   │   │   ├── MANUSCRIPT.docx         # Final approved manuscript
│   │   │   ├── MANUSCRIPT.pdf          # PDF proof
│   │   │   ├── METADATA.md             # ISBN + retail metadata
│   │   │   ├── KDP_RECORD.txt          # Publication log + sales tracking
│   │   │   │
│   │   │   ├── cover/
│   │   │   │   ├── Tao_Clinical_Touch_Cover_v4.png
│   │   │   │   ├── Tao_Clinical_Touch_Cover_v4.jpg
│   │   │   │   ├── Tao_Clinical_Touch_Cover_v4.psd
│   │   │   │   ├── Tao_Clinical_Touch_Cover_v4.pdf
│   │   │   │   ├── (other versions + iterations)
│   │   │   │   └── Tao_Back_Cover.jpg
│   │   │   │
│   │   │   ├── proofs/
│   │   │   │   └── KDP_PRINT_INTERIOR_SPREAD.pdf
│   │   │   │
│   │   │   ├── marketing-assets/
│   │   │   │   └── Tao_QR_Codes.docx
│   │   │   │
│   │   │   ├── scripts/
│   │   │   │   ├── build_main.js
│   │   │   │   ├── build_chapters.js
│   │   │   │   ├── build_interior.js
│   │   │   │   ├── build_backmatter.js
│   │   │   │   ├── build_symbols.js
│   │   │   │   ├── build_cover.jsx
│   │   │   │   ├── build_cover.py
│   │   │   │   ├── update_cover_guides.jsx
│   │   │   │   └── create_banner_page.py
│   │   │   │
│   │   │   └── assets/
│   │   │       └── symbols/
│   │   │           └── tao_symbols_v2_fixed/
│   │   │
│   │   ├── website/
│   │   │   ├── BUILD_GUIDE.md          # Landing page spec
│   │   │   ├── CONVERSION_SPEC.md      # Analytics + funnel
│   │   │   ├── DESIGN_SPEC.md          # Visual direction
│   │   │   │
│   │   │   ├── elementor/
│   │   │   │   ├── elementor_data.json
│   │   │   │   ├── elementor_native.json
│   │   │   │   ├── elementor_data_b64.txt
│   │   │   │   ├── elementor_blueprint_tao_home.md
│   │   │   │   ├── elementor_homepage_migration.md
│   │   │   │   │
│   │   │   │   └── scripts/
│   │   │   │       ├── generate_elementor.py
│   │   │   │       └── push_elementor.py
│   │   │   │
│   │   │   ├── plugins/
│   │   │   │   ├── tao-front-page-plugin/
│   │   │   │   └── tao-front-page-plugin.zip
│   │   │   │
│   │   │   ├── theme-files/
│   │   │   │   ├── front-page.php
│   │   │   │   ├── front-page.txt
│   │   │   │   └── front-page.zip
│   │   │   │
│   │   │   └── mockups/
│   │   │       ├── tao_landing_page.html
│   │   │       ├── tao_chapter1_free_chapter_seo.html
│   │   │       ├── tao_cover_mockup.html
│   │   │       ├── hero_preview.html
│   │   │       └── (other design mockups)
│   │   │
│   │   ├── marketing/
│   │   │   ├── MESSAGING.md            # Launch communication strategy
│   │   │   ├── REVIEWERS.md            # Review acquisition process
│   │   │   ├── SOCIAL.md               # Social media strategy
│   │   │   │
│   │   │   ├── social-assets/
│   │   │   │   └── social_images/
│   │   │   │
│   │   │   └── reviewer-assets/
│   │   │       └── Book Review Posts and images/
│   │   │
│   │   ├── ce-program/
│   │   │   ├── README.md               # Program charter
│   │   │   ├── PHASE1_BUILD_SPEC.md    # Phase 1 curriculum spec
│   │   │   └── (curriculum modules as they're built)
│   │   │
│   │   └── DECISION_LOG.md             # Historical decisions + phase notes
│   │
│   ├── atlas/                          # Finding My Wei / Project Atlas
│   │   ├── README.md                   # Research program charter
│   │   │
│   │   ├── 01-therapeutic-alliance/
│   │   │   ├── README.md               # Paper 1 overview
│   │   │   ├── BRIEF.md                # Clinical framework definition
│   │   │   ├── manuscript.md           # Paper text
│   │   │   ├── research/
│   │   │   │   └── (source materials, citations, data)
│   │   │   └── assets/
│   │   │       └── (figures, tables, visuals)
│   │   │
│   │   ├── 02-stand-architecture/
│   │   │   ├── README.md               # Paper 2 overview
│   │   │   ├── BRIEF.md                # Architecture definition
│   │   │   ├── manuscript.md           # Paper text
│   │   │   ├── research/
│   │   │   │   └── (source materials, citations, data)
│   │   │   └── assets/
│   │   │       └── (figures, tables, visuals)
│   │   │
│   │   ├── marketing/
│   │   │   ├── README.md               # Campaign strategy
│   │   │   ├── redirects.md            # Influencer redirect tracking
│   │   │   ├── redirect_log.md         # Deployment record
│   │   │   ├── task_007_ga4_repair.md  # GA4 setup notes
│   │   │   ├── asset_registry.md       # Asset inventory
│   │   │   └── phase_1_completion_report.md
│   │   │
│   │   └── PUBLICATION_ROADMAP.md      # 5-paper sequence + timeline
│   │
│   └── boston-bodyworker/              # LEGACY: IP estate (archive reference)
│       ├── README.md
│       └── (historical materials)
│
├── archive/                            # Historical files + backups
│   ├── diffs-20260312-070341/
│   ├── diffs-20260312-070401/
│   ├── root-duplicates-backup-20260312-070341/
│   ├── root-duplicates-backup-20260312-070401/
│   ├── root-duplicates-retired-20260312-070454/
│   └── (other retired materials)
│
└── .claude/
    ├── settings.json                   # Shared Claude Code settings (if any)
    ├── launch.json                     # Local launch config (DO NOT COMMIT)
    └── settings.local.json             # Local settings (DO NOT COMMIT)

```

---

## FILE COUNT SUMMARY

| Folder | Est. Files | Type | Notes |
|---|---|---|---|
| docs/ | 25-30 | System | System files + memory + compliance |
| projects/sidekick-air/ | ~40 | Active | Product + strategy + partner materials |
| projects/learn2tape/ | ~55 | Active | Course + marketing + campaigns |
| projects/tao/ | ~680 | Active | Book (largest) + website + marketing |
| projects/atlas/ | ~50 | Active | Research papers + marketing |
| projects/boston-bodyworker/ | 1 | Legacy | Minimal legacy reference |
| archive/ | ~38 | Archive | Historical + backups |
| **.claude/** | 3 | Local | Local config (not committed) |
| **Total** | **~900** | — | — |

---

## KEY PRINCIPLES

1. **One project = one folder** — sidekick-air, learn2tape, tao, atlas, boston-bodyworker
2. **Meaningful subfolders** — product/, strategy/, marketing/, website/, book/, etc.
3. **Each project has a README.md** — acts as project hub + entry point
4. **No orphaned files at root** — everything belongs inside a project
5. **System files in docs/** — making them GitHub-visible for transparency
6. **Memory is curated** — lives in docs/memory/, grows over time
7. **Archive is read-only** — historical reference only
8. **.claude/ stays local** — development settings not version-controlled

---

## MOVING TO GITHUB

Once this structure is approved and files are migrated locally:

1. **Create repository** → `anthropics/drew-business` (or similar)
2. **Initialize git** in Coding-folder root
3. **Add .gitignore** (node_modules/, .DS_Store, .claude/settings.local.json, archive/, etc.)
4. **Initial commit** → "Initial commit: Finding My Wei structure v1.0"
5. **Push to GitHub** → This becomes source of truth
6. **Local Coding-folder** → Becomes a clone/working copy of GitHub

---

## NEXT STEPS

1. Review this recommended structure
2. Clarify decisions from UNRESOLVED_ITEMS.md
3. Execute migration (folder moves, file reorganization)
4. Generate git-ready structure
5. Push to GitHub
6. Update README.md with GitHub URL + collaboration guidelines

