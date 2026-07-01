# Estate Ingestion Plan
## Stage Two: Systematic Knowledge Integration
## Date: June 30, 2026
## Status: DRAFT FOR REVIEW

---

# Purpose

Stage One established the constitutional architecture (frozen, permanent).

**Stage Two ingests all legacy knowledge into this architecture.**

This is **not file migration**. It is **knowledge mapping and integration**.

Every legacy folder contains intellectual work. That work must be:
1. Analyzed and understood
2. Decomposed into its components
3. Mapped to appropriate constitutional locations
4. Integrated into the permanent estate
5. Only then: original folder is retired

---

# Core Principle

**No legacy folder is considered complete until its knowledge has been successfully mapped into the constitutional architecture.**

Legacy folder retirement criteria:
- ✅ All knowledge has been mapped to appropriate domain/capability/estate
- ✅ No intellectual value has been lost
- ✅ All relationships have been preserved
- ✅ Asset lifecycle states have been assigned
- ✅ Constitutional destination is documented
- ✅ Original folder can be safely archived

---

# Legacy Folder Inventory & Ingestion Plan

---

## 1. Learn2Tape/ (50 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/Learn2Tape/`
- File count: 50
- Subdirectories: NCB_PHASE1_UNZIPPED/, state_splits/
- Key assets: Courses, marketing, campaigns, product copy, GTM tracking

### Knowledge Analysis
**What it contains:**
- Course materials and product specs
- Marketing campaigns (Google Ads, Brevo)
- Email list data (NCB campaign)
- WooCommerce product configuration
- GTM conversion funnel setup
- Analytics and performance tracking

### Destination Mapping

| File/Folder | Destination | Lifecycle State | Priority |
|---|---|---|---|
| PROJECT_CONTROL.md | 05_DOMAINS/EDUCATION_DOMAIN/README.md | STABLE | P1 |
| learn2tape_google_ads.md | 04_CAPABILITIES/MARKETING/GOOGLE_ADS.md | STABLE | P1 |
| google_ads_7_day_diagnostic.md | 04_CAPABILITIES/MARKETING/DIAGNOSTICS.md | VALIDATION | P2 |
| Brevo_Implementation_Workflow_Claude.md | 04_CAPABILITIES/PUBLISHING/BREVO_WORKFLOW.md | STABLE | P1 |
| woocommerce_product_page_copy.md | 05_DOMAINS/EDUCATION_DOMAIN/PRODUCTS/COPY.md | STABLE | P1 |
| NCB_LIST_*.csv | 05_DOMAINS/EDUCATION_DOMAIN/CAMPAIGNS/ncb/DATA/lists/ | STABLE | P2 |
| NCB_PHASE1_UNZIPPED/ | 05_DOMAINS/EDUCATION_DOMAIN/CAMPAIGNS/ncb/DATA/zerobounce/ | STABLE | P2 |
| state_splits/ | 05_DOMAINS/EDUCATION_DOMAIN/CAMPAIGNS/ncb/DATA/by-state/ | STABLE | P2 |
| NCB_MA_Batch_Day*.csv | 05_DOMAINS/EDUCATION_DOMAIN/CAMPAIGNS/ncb/BATCHES/ | STABLE | P3 |
| *.py scripts | 05_DOMAINS/EDUCATION_DOMAIN/CAMPAIGNS/ncb/SCRIPTS/ | STABLE | P2 |

### Additional Root-Level Files to Integrate
| File | Destination | Lifecycle State | Priority |
|---|---|---|---|
| GTM_CONVERSION_FUNNEL_SUMMARY.md | 04_CAPABILITIES/MARKETING/GTM_FUNNEL.md | STABLE | P1 |
| GTM_V26_ECOMMERCE_PAYLOAD_FIX.md | 04_CAPABILITIES/MARKETING/GTM_V26_FIX.md | VALIDATION | P2 |
| L2T_PHASE2_VALIDATION_REPORT.md | 05_DOMAINS/EDUCATION_DOMAIN/PHASE2_VALIDATION.md | STABLE | P1 |
| learn2tape_ads_diagnostic_2026-04-17.md | 04_CAPABILITIES/MARKETING/DIAGNOSTICS_20260417.md | VALIDATION | P2 |

### Ingestion Effort
**Estimated effort: MEDIUM (4-6 hours)**

- File count: 50 files
- Complexity: Straightforward mapping (all clearly belong to Education Domain)
- Decision points: Few (clear ownership)
- Relationship preservation: Moderate (campaigns have interconnected data)

### Retirement Criteria for Learn2Tape/
- [ ] PROJECT_CONTROL.md extracted → EDUCATION_DOMAIN/README.md
- [ ] All marketing materials copied → 04_CAPABILITIES/MARKETING/
- [ ] All campaign data copied → EDUCATION_DOMAIN/CAMPAIGNS/ncb/
- [ ] All product specs copied → EDUCATION_DOMAIN/PRODUCTS/
- [ ] Lifecycle states assigned to all assets
- [ ] Relationships between assets documented
- [ ] Original folder backed up to archive/
- [ ] Symlink or reference created if needed for transition
- [ ] Verification: No files lost, all relationships preserved

### Decision Points
1. **Should we keep NCB campaign data active or archive it?** 
   - Current state: Campaign completed (April 2026)
   - Recommendation: Move to ARCHIVE, not ACTIVE
   
2. **Should GTM tracking stay in Learn2Tape or move to global Marketing?**
   - Current state: L2T-specific implementation
   - Recommendation: Keep in EDUCATION_DOMAIN but document pattern for other domains

---

## 2. Tao/ (661 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/Tao/`
- File count: 661 (largest legacy folder)
- Subdirectories: Multiple (book/, website/, marketing/, scripts/, assets/)
- Key assets: Book manuscript, cover design, website code, marketing materials

### Knowledge Analysis
**What it contains:**
- Published book (final manuscript + editions)
- Book cover design (multiple versions)
- Website/landing page (Elementor, WordPress)
- Marketing assets (social media, reviewer materials)
- Publishing metadata and records
- Build scripts (automation)
- QR codes and embedded materials

### Complexity Note
**The Tao is complex because it spans multiple constitutional layers:**
- **FOUNDER_DOMAIN** — Drew's creative work (manuscript drafts, philosophy)
- **03_INTELLECTUAL_ESTATE/BOOKS** — Published work (final manuscript, editions)
- **PUBLISHING_DOMAIN** — Authority platform aspect (if extended to website)
- **04_CAPABILITIES/PUBLISHING** — Publishing workflow (used by Tao)
- **04_CAPABILITIES/MARKETING** — Marketing materials and strategy

### Destination Mapping

| File/Folder | Destination | Lifecycle State | Notes |
|---|---|---|---|
| PROJECT_CONTROL.md | 04_DREW_FREEDMAN/PROJECTS/books/the-tao/README.md | STABLE | Project hub |
| tao_interior_final.docx | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/manuscript-final.docx | PRESERVATION | Final version |
| tao_interior_final.pdf | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/manuscript-final.pdf | PRESERVATION | PDF proof |
| tao_interior_final_*.docx | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/editions/ | PRESERVATION | Personalized editions |
| Tao_Clinical_Touch_Cover_*.* | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/cover/ | PRESERVATION | All versions |
| KDP_PRINT_INTERIOR_SPREAD.pdf | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/proofs/ | PRESERVATION | Print proof |
| KDP Launch & Publishing Record.txt | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/publication-record.md | PRESERVATION | Sales log |
| Launch Messaging Pack.md | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/messaging.md | PUBLICATION | Campaign messaging |
| Reviewer Outreach Tracker.md | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/reviews.md | PUBLICATION | Review strategy |
| Social Media Launch System.md | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/social.md | PUBLICATION | Social strategy |
| Book Review Posts and images/ | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/reviewer-assets/ | PUBLICATION | Reviewer materials |
| social_images/ | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/marketing/social-assets/ | PUBLICATION | Social graphics |
| elementor_*.json | 04_CAPABILITIES/PUBLISHING/WEBSITE_TEMPLATES/tao-elementor/ | STABLE | Website configuration |
| tao-front-page-plugin/ | 04_CAPABILITIES/PUBLISHING/PLUGINS/tao-front-page/ | STABLE | Custom plugin |
| front-page.php | 04_CAPABILITIES/PUBLISHING/THEME_CUSTOMIZATIONS/tao-front-page.php | STABLE | Theme file |
| build_*.js/jsx/py | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/scripts/build/ | STABLE | Automation scripts |
| tao_symbols_v2_fixed/ | 03_INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/assets/symbols/ | STABLE | Symbol library |
| tao_*.md files (various) | 04_DREW_FREEDMAN/PROJECTS/books/the-tao/ OR archive | ARCHIVE | Decision-dependent |
| package.json/package-lock.json | DELETE | N/A | Dependency cache |
| node_modules/ | DELETE | N/A | Dependency cache |

### Additional Root-Level Files to Integrate
| File | Destination | Lifecycle State |
|---|---|---|
| (None currently at root) | - | - |

### Ingestion Effort
**Estimated effort: HIGH (12-16 hours)**

**Why high:**
- 661 files (largest legacy folder)
- Spans multiple constitutional layers (creates complexity)
- Many asset types (code, design, content, automation)
- Decision points: Multiple (what's creation vs. completion? What's tool vs. knowledge?)
- Relationship preservation: High (many cross-references)

### Retirement Criteria for Tao/
- [ ] Final manuscript copied to INTELLECTUAL_ESTATE/BOOKS/
- [ ] All editions and proofs copied to appropriate locations
- [ ] All book cover designs copied to INTELLECTUAL_ESTATE/BOOKS/cover/
- [ ] All marketing materials copied to INTELLECTUAL_ESTATE/BOOKS/marketing/
- [ ] Publishing metadata and records copied
- [ ] Elementor configuration backed up to CAPABILITIES/PUBLISHING/
- [ ] WordPress plugin backed up to CAPABILITIES/PUBLISHING/
- [ ] Build scripts archived to INTELLECTUAL_ESTATE/BOOKS/scripts/
- [ ] node_modules/ and .DS_Store deleted
- [ ] All lifecycle states assigned
- [ ] Relationships documented (which capability supports what asset)
- [ ] Original folder backed up to archive/
- [ ] Verification: No assets lost, all 661 files accounted for

### Critical Decision Points
1. **Where should working drafts go?**
   - Current: Mixed in Tao/ folder
   - Options: Archive as historical, or preserve in FOUNDER_DOMAIN/PROJECTS
   - Recommendation: Archive (completed work, creation phase is past)

2. **Should publishing infrastructure stay at root Capabilities or become book-specific?**
   - Current: Elementor config, plugin, scripts are Tao-specific
   - Recommendation: Move to CAPABILITIES/PUBLISHING/TEMPLATES/tao/ (so others can reuse pattern)

3. **What about the Tao website (taoclinicaltouch.com)?**
   - Current: WordPress, hosted externally
   - Question: Should we version-control website configuration/theme?
   - Recommendation: Back up theme customizations to CAPABILITIES/PUBLISHING, but website lives external

---

## 3. SidekickAir/ (34 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/SidekickAir/`
- File count: 34
- Subdirectories: product/, strategy/, platform/, ip/, logs/
- Key assets: Business plan, specs, patents, manufacturing strategy, partner research

### Knowledge Analysis
**What it contains:**
- Product briefs and specifications
- Strategy and roadmaps
- Patent documentation
- Manufacturing partnerships
- Partner research and overviews
- Decision logs and founder notes
- IP architecture

### Destination Mapping

| File/Folder | Destination | Lifecycle State | Priority |
|---|---|---|---|
| sidekick_air_master_index.md | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/README.md | STABLE | P1 |
| sidekick_air_project_master_brief.md | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/BRIEF.md | STABLE | P1 |
| sidekick_air_technical_specs.md | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/SPECS.md | STABLE | P1 |
| product/ subdirectory | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/PRODUCT/ | STABLE | P1 |
| strategy/ subdirectory | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/STRATEGY/ | STABLE | P1 |
| platform/ subdirectory | 05_DOMAINS/INNOVATION_DOMAIN/TECHNOLOGY/ | STABLE | P1 |
| ip/ subdirectory | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/IP/ | STABLE | P1 |
| logs/ subdirectory | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/LOGS/ | STABLE | P1 |
| Sidekick Air - PacMar Business Plan/ | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/PARTNERS/pacmar/ | STABLE | P1 |
| *.pdf partner research | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/PARTNERS/research/ | STABLE | P2 |
| project_context.yaml | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/context.yaml | STABLE | P3 |
| sidekick_air_ai_system_setup.md | 05_DOMAINS/INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/AI_SETUP.md | STABLE | P3 |

### Ingestion Effort
**Estimated effort: LOW (2-3 hours)**

- File count: 34 (manageable)
- Mapping: Straightforward (all clearly belong to Innovation Domain → Sidekick Air product)
- Decision points: Minimal (clear ownership)
- Relationship preservation: Low (contained within product)

### Retirement Criteria for SidekickAir/
- [ ] Master index copied → INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/README.md
- [ ] All product specs, strategy, platform docs copied
- [ ] Patent and IP documentation copied
- [ ] Manufacturing partner materials copied
- [ ] Logs and decision records copied
- [ ] Partner research archived
- [ ] Lifecycle states assigned to all assets
- [ ] Original folder backed up to archive/
- [ ] Verification: All 34 files accounted for, no loss

### Decision Points
1. **Should partner research PDFs stay in product folder or go to separate Partners/research/ location?**
   - Recommendation: Separate Partners/research/ folder (clean organization, reusable pattern)

2. **Is AeroStitch technology separate from Sidekick Air or part of it?**
   - Current: Documented separately in platform/
   - Recommendation: Keep separate in TECHNOLOGY/ (multiple products may use it)

---

## 4. BostonBodyworker/ (1 file)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/BostonBodyworker/`
- File count: 1
- Content: Single markdown file with description

### Knowledge Analysis
**What it contains:**
- Brief description of Boston Bodyworker project
- Mostly placeholder; actual website content lives external

### Destination Mapping

| File | Destination | Lifecycle State |
|---|---|---|
| the-boston-bodyworker.md | 05_DOMAINS/PUBLISHING_DOMAIN/README.md | STABLE |

### Ingestion Effort
**Estimated effort: TRIVIAL (10 minutes)**

- File count: 1
- Complexity: None (simple README)
- The actual work is capturing 30+ years of website content (separate Stage 2 sub-phase)

### Retirement Criteria for BostonBodyworker/
- [ ] README file copied to PUBLISHING_DOMAIN/
- [ ] Note created: "Website content migration is separate initiative (see PUBLISHING_DOMAIN/WEBSITE/)"
- [ ] Original folder backed up to archive/

### Critical Note
**This folder is incomplete.** The Boston Bodyworker is a 30+ year authority asset, but almost no content is versioned in the Coding-folder. The real work is:
- Website archive capture
- Blog post collection
- Article versioning
- Historical content preservation

This is a **Phase 2 sub-initiative**, not part of legacy folder retirement.

---

## 5. _system/ (17 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/_system/`
- File count: 17
- Content: Operating system files (SOUL, MEMORY, HEARTBEAT, etc.)

### Knowledge Analysis
**What it contains:**
- Collaboration principles (SOUL.md)
- User preferences (USER.md)
- Daily automation (HEARTBEAT.md)
- Memory management (MEMORY.md)
- Operational rules
- Onboarding guides
- AI assistant notes

### Destination Mapping

| File | Destination | Lifecycle State | Action |
|---|---|---|---|
| SOUL.md | 01_OPERATING_SYSTEM/SOUL.md | STABLE | Symlink old location → new |
| USER.md | 01_OPERATING_SYSTEM/PREFERENCES/USER.md | STABLE | Move + symlink |
| HEARTBEAT.md | 01_OPERATING_SYSTEM/AUTOMATION/HEARTBEAT.md | STABLE | Move + symlink |
| MEMORY.md | 01_OPERATING_SYSTEM/MEMORY/MEMORY.md | STABLE | Move + symlink (grows in place) |
| RULES.md | 01_OPERATING_SYSTEM/PRINCIPLES.md | STABLE | Rename + move |
| MASTER_CONTROL.md | Merge into PRINCIPLES.md or archive | ARCHIVE | Consolidate |
| PROJECTS_MAP.md | DELETE | N/A | Redundant with new structure |
| INDEX.md | DELETE | N/A | Redundant with README files |
| OPENCLAW_LAUNCHER.md | .openclaw/workspace/README.md | STABLE | Move to external |
| SYNC_TODAY_TO_NOTION.md | archive/HISTORICAL/ | ARCHIVE | Historical record |
| TODAY.md | DELETE | N/A | Ephemeral (not versioned) |
| WEEKLY_*.md | archive/HISTORICAL/ | ARCHIVE | Historical records |
| CLAUDE_WELCOME.md | archive/ONBOARDING/ | ARCHIVE | Superseded by docs/ |
| sidekick-agent-*.md | Merge into 01_OPERATING_SYSTEM/AI_GUIDELINES/ | STABLE | Consolidate |
| Memory subdirectories | 01_OPERATING_SYSTEM/MEMORY/ | STABLE | Integrated |

### Ingestion Effort
**Estimated effort: LOW (2-3 hours)**

- File count: 17
- Mapping: Already partially done (original files were copies to new locations during Stage One)
- Decision points: Few (clear destinations)
- Action: Mostly cleanup and consolidation

### Retirement Criteria for _system/
- [ ] SOUL.md symlinked or moved to 01_OPERATING_SYSTEM/
- [ ] USER.md moved to 01_OPERATING_SYSTEM/PREFERENCES/
- [ ] HEARTBEAT.md moved to 01_OPERATING_SYSTEM/AUTOMATION/
- [ ] MEMORY.md moved to 01_OPERATING_SYSTEM/MEMORY/
- [ ] Operating procedures consolidated
- [ ] Ephemeral files (TODAY.md) deleted
- [ ] Historical records archived
- [ ] Original _system/ folder can be deleted or kept as reference
- [ ] Verification: No loss of operational knowledge

---

## 6. _projects/ (5 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/_projects/`
- File count: 5
- Content: Project track files (status snapshots)

### Knowledge Analysis
**What it contains:**
- boston-bodyworker.md
- learn2tape.md
- sidekick-air.md
- tao.md
- (possibly others)

**These are project status snapshots**, now superseded by domain CHARTERs and README files.

### Destination Mapping

| File | Destination | Action | Rationale |
|---|---|---|---|
| learn2tape.md | Archive → INTELLECTUAL_ESTATE/ARCHIVE/project-snapshots/ | Archive | Status is now in EDUCATION_DOMAIN |
| tao.md | Archive → INTELLECTUAL_ESTATE/ARCHIVE/project-snapshots/ | Archive | Status is now in FOUNDER_DOMAIN |
| sidekick-air.md | Archive → INTELLECTUAL_ESTATE/ARCHIVE/project-snapshots/ | Archive | Status is now in INNOVATION_DOMAIN |
| boston-bodyworker.md | Archive → INTELLECTUAL_ESTATE/ARCHIVE/project-snapshots/ | Archive | Status is now in PUBLISHING_DOMAIN |

### Ingestion Effort
**Estimated effort: TRIVIAL (30 minutes)**

- File count: 5
- Complexity: None (simple archival)
- No relationship preservation needed (information is superseded)

### Retirement Criteria for _projects/
- [ ] Project status files moved to INTELLECTUAL_ESTATE/ARCHIVE/project-snapshots/
- [ ] Note created explaining migration to domain CHARTERs
- [ ] Original _projects/ folder can be deleted
- [ ] Verification: Files preserved in archive

### Strategic Note
**These files are historical snapshots.** The live status for each project is now in:
- EDUCATION_DOMAIN/CHARTER.md (Learn2Tape)
- FOUNDER_DOMAIN/PROJECTS (Tao)
- INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/CHARTER.md
- PUBLISHING_DOMAIN/CHARTER.md

The old project files are now redundant. Archive for history, but the source of truth moves to CHARTERs.

---

## 7. _support/ (2 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/_support/`
- File count: 2
- Content: Supporting research and configuration

### Knowledge Analysis
**What it contains:**
- NOTION_SYNC_MAP.md — Notion sync configuration
- stitchcore-partners.md — Partner research

### Destination Mapping

| File | Destination | Lifecycle State | Action |
|---|---|---|---|
| stitchcore-partners.md | 04_CAPABILITIES/OPERATIONS/PARTNERS/ or 05_DOMAINS/INNOVATION_DOMAIN/PARTNERS/ | STABLE | Move to appropriate location |
| NOTION_SYNC_MAP.md | .openclaw/workspace/README.md | STABLE | Move to external config |

### Ingestion Effort
**Estimated effort: TRIVIAL (15 minutes)**

- File count: 2
- Complexity: None
- Decisions: One (where does partner research live?)

### Retirement Criteria for _support/
- [ ] Files copied to appropriate locations
- [ ] Original _support/ folder can be deleted
- [ ] Verification: No loss

### Decision Point
**Where should stitchcore-partners.md live?**
- Option A: 05_DOMAINS/INNOVATION_DOMAIN/PARTNERS/research/
- Option B: 04_CAPABILITIES/OPERATIONS/PARTNER_RELATIONS/
- Recommendation: Option A (product-specific research belongs in product domain)

---

## 8. archive/ (38 files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/archive/`
- File count: 38
- Content: Historical records, backups, diffs from prior migrations

### Knowledge Analysis
**What it contains:**
- Consolidation maps from prior reorganizations
- Merge checklists
- Backup copies of root duplicates
- Historical diffs

**This folder already IS archival.** The question is whether to:
1. Keep as-is (minimal effort)
2. Reorganize into constitutional archive structure
3. Evaluate each file for historical value

### Destination Mapping

| Content | Destination | Action | Rationale |
|---|---|---|---|
| Consolidation maps | 03_INTELLECTUAL_ESTATE/ARCHIVE/migration-history/ | Keep | Historical record of prior migrations |
| Root duplicates backups | 03_INTELLECTUAL_ESTATE/ARCHIVE/backups/ | Keep | Backup safety |
| Diffs from prior work | 03_INTELLECTUAL_ESTATE/ARCHIVE/diffs/ | Keep | Historical context |
| (Evaluate each) | Organize by type or archive-date | Archive | Systematic organization |

### Ingestion Effort
**Estimated effort: MEDIUM (3-4 hours)**

- File count: 38
- Complexity: Medium (requires categorization)
- Decision points: Multiple (is each file historically valuable?)

### Retirement Criteria for archive/
- [ ] Each file evaluated for historical value
- [ ] Files organized into INTELLECTUAL_ESTATE/ARCHIVE/
- [ ] Metadata added (why was this saved? what does it document?)
- [ ] Original archive/ folder can be kept as-is or consolidated
- [ ] Verification: No loss of historical context

### Strategic Note
**The archive folder is already in the right place (archival).** The ingestion work is organizational and meta-documentation (adding context to why each item was saved).

---

## 9. Root-Level Markdown Files (7 files)

### Current State
- Various .md files at root level (not in folders)
- Examples: README.md, CONSTITUTION_ALIGNED_MIGRATION_MAP.md, etc.

### Analysis
**Pre-Stage One files:**
- MIGRATION_MAP.md → Archive (superseded by IEMS)
- CONSTITUTION_ALIGNED_MIGRATION_MAP.md → Archive (superseded by IEMS)
- FINAL_REPOSITORY_ARCHITECTURE.md → Archive (superseded by IEMS)
- UNRESOLVED_ITEMS.md → Archive (decisions resolved)
- RECOMMENDED_REPOSITORY_TREE.md → Archive (superseded)
- NEXT_ACTIONS.md → Archive (action taken)
- IEMS_ARCHITECTURAL_REVIEW.md → Archive (design phase doc)

**Stage One completion files:**
- README.md → Keep (updated master README)
- STAGE_ONE_COMPLETE.md → Archive (historical marker)
- IEMS_FINAL_ARCHITECTURE.md → 00_CONSTITUTION/ (part of foundation)
- IMPLEMENTATION_DIRECTIVE.md → 00_CONSTITUTION/ (part of foundation)
- STEWARDSHIP_BEGINS.md → Archive (marker file)
- SYSTEM_COMPLETE.md → Archive (marker file)
- ESTATE_INGESTION_PLAN.md → Keep at root OR move to 00_CONSTITUTION/ (living document)

### Destination Mapping

| File | Destination | Action |
|---|---|---|
| README.md | Keep at root | Master project README |
| Pre-Stage-One .md files | archive/DESIGN_PHASE/ | Archive |
| Stage-One completion files | 00_CONSTITUTION/ or archive/ | Archive |
| Foundation documents | 00_CONSTITUTION/ | Already placed |
| ESTATE_INGESTION_PLAN.md | Root or 00_CONSTITUTION/ | Living document (decision needed) |

### Ingestion Effort
**Estimated effort: LOW (1 hour)**

- File count: 7
- Complexity: Simple (decision per file)
- Action: Mostly archival

---

## 10. 06_Project_Atlas/ (empty except .DS_Store)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/06_Project_Atlas/`
- Content: Empty (was placeholder)
- Status: Superseded by 02_PROJECT_ATLAS/ created in Stage One

### Action
**DELETE** (was placeholder, now redundant with 02_PROJECT_ATLAS/)

---

## 11. 07_MARKETING/ (minimal, 5 tracking files)

### Current State
- Location: `/Users/Drewdog19/Desktop/Coding-folder/07_MARKETING/`
- File count: 5 (mostly in tracking/ subdirectory)
- Content: Atlas campaign tracking

### Destination Mapping

| File | Destination | Lifecycle State |
|---|---|---|
| tracking/redirects.md | 02_PROJECT_ATLAS/marketing/redirects.md | STABLE |
| tracking/redirect_log.md | 02_PROJECT_ATLAS/marketing/redirect_log.md | STABLE |
| tracking/task_007_ga4_repair.md | 02_PROJECT_ATLAS/marketing/ga4_repair.md | VALIDATION |
| tracking/asset_registry.md | 02_PROJECT_ATLAS/marketing/asset_registry.md | STABLE |
| tracking/phase_1_completion_report.md | 02_PROJECT_ATLAS/marketing/phase_1_completion.md | STABLE |

### Ingestion Effort
**Estimated effort: TRIVIAL (30 minutes)**

---

# Ingestion Sequence & Timeline

## Phase 2a: Quick Wins (Week 1)
Low-effort, high-clarity ingestions:

**Priority 1 — Core domains (no dependencies):**
- [ ] SidekickAir/ → INNOVATION_DOMAIN (2-3 hours)
- [ ] BostonBodyworker/ → PUBLISHING_DOMAIN (10 minutes)
- [ ] 07_MARKETING/ → PROJECT_ATLAS/ (30 minutes)
- [ ] 06_Project_Atlas/ (delete, 5 minutes)

**Estimated: 3-4 hours, Day 1-2**

## Phase 2b: Medium Ingestions (Week 1-2)
Moderate effort, clear destinations:

**Priority 2:**
- [ ] Learn2Tape/ → EDUCATION_DOMAIN (4-6 hours)
- [ ] _projects/ → archive/ (30 minutes)
- [ ] _support/ → appropriate locations (15 minutes)

**Estimated: 5-7 hours, Day 3-4**

## Phase 2c: Heavy Lifting (Week 2-3)
Highest effort, most complexity:

**Priority 3:**
- [ ] Tao/ → Multiple destinations (12-16 hours)
  - Book to INTELLECTUAL_ESTATE/BOOKS/
  - Marketing to BOOKS/marketing/
  - Website config to CAPABILITIES/PUBLISHING/
  - Scripts to BOOKS/scripts/
  - Design files organized by type
  - **This is 3-4 days of careful work**

**Estimated: 12-16 hours, Day 5-8**

## Phase 2d: Operational Systems (Week 2)
Low effort but systematic:

**Priority 4:**
- [ ] _system/ → 01_OPERATING_SYSTEM/ (2-3 hours)
  - Symlink or move files
  - Consolidate redundant docs
  - Archive ephemeral files

**Estimated: 2-3 hours, (parallel with Phase 2c)**

## Phase 2e: Historical Archival (Week 3)
Organizational and metadata work:

**Priority 5:**
- [ ] Root-level .md files → appropriate archival (2-3 hours)
- [ ] archive/ organization → INTELLECTUAL_ESTATE/ARCHIVE/ (3-4 hours)
- [ ] Metadata documentation (why each item was kept)

**Estimated: 5-7 hours, Day 9-10**

---

# Total Ingestion Effort Estimate

| Phase | Hours | Days |
|---|---|---|
| Phase 2a (Quick wins) | 3-4 | 1-2 |
| Phase 2b (Medium) | 5-7 | 1-2 |
| Phase 2c (Tao heavy lifting) | 12-16 | 3-4 |
| Phase 2d (Operating system) | 2-3 | 1 (parallel) |
| Phase 2e (Archival) | 5-7 | 2 |
| **TOTAL** | **27-37 hours** | **8-11 days** |

**With 3-4 hours/day effort: 2-2.5 weeks (realistic timeline)**

---

# Ingestion Success Criteria

### For Each Legacy Folder

✅ **Knowledge captured:** All intellectual content identified  
✅ **Mapped destinations:** Decided where each piece goes  
✅ **Lifecycle states:** All assets tagged with current state  
✅ **Relationships documented:** Dependencies and connections recorded  
✅ **Retirement decision:** Criteria for original folder archival met  
✅ **No loss:** Every meaningful file accounted for  
✅ **Verification:** Spot-checks confirm no gaps  

### For the Complete Ingestion

✅ **All 11 legacy folders processed**  
✅ **~850 total files ingested into constitutional architecture**  
✅ **Zero loss of intellectual value**  
✅ **All relationships preserved**  
✅ **Source of truth shifted to constitutional architecture**  
✅ **Legacy folders retired to archive**  
✅ **Estate is cohesive and navigable**  

---

# Risk Mitigation

### Risk: Files are lost during ingestion

**Mitigation:**
- Before moving anything, create backup of entire Coding-folder
- Use verified copy operations (not moves)
- Spot-check each domain after ingestion
- Maintain file count inventory

### Risk: Relationships are broken

**Mitigation:**
- Document relationships in each file's header or companion doc
- Note cross-references in CHARTER.md files
- Create relationship maps showing dependencies

### Risk: Decisions are made inconsistently

**Mitigation:**
- Create decision checklist for each file type
- Document reasoning for each placement decision
- Review decisions before retiring folder

### Risk: Ingestion stalls on difficult files

**Mitigation:**
- Flag uncertain files immediately (don't let them block progress)
- Create "TRIAGE" folder for files needing review
- Get Drew's decision on ambiguous cases

---

# Decision Points Requiring Drew Input

Before ingestion begins, clarification needed on:

1. **Should Tao website stay external or be version-controlled?**
   - Current: taoclinicaltouch.com (external WordPress)
   - Question: Back up theme customizations to Capabilities?
   - Decision: [Drew to decide]

2. **Is Boston Bodyworker website content a Phase 2 priority?**
   - Current: Almost no content versioned
   - Question: Should we archive website (requires external work)?
   - Decision: [Drew to decide] — likely Phase 2b sub-project

3. **What's the status of Project Atlas investigations?**
   - Current: Research papers in Google Drive (external)
   - Question: Should we migrate research to repo or keep external?
   - Decision: [Drew to decide]

4. **Should legacy folders be deleted or kept as reference?**
   - Current: Proposal is archive + retire
   - Options: Delete entirely, keep as readonly reference, symlink
   - Decision: [Drew to decide]

5. **Is ESTATE_INGESTION_PLAN.md a living document?**
   - Should it stay at root for ongoing reference during ingestion?
   - Or move to 00_CONSTITUTION/ when complete?
   - Decision: [Drew to decide]

---

# Success Handoff Criteria

When Phase 2 is complete, the system should:

✅ **All legacy content is in constitutional locations**  
✅ **Nothing is lost**  
✅ **Relationships are preserved**  
✅ **Lifecycle states are assigned**  
✅ **Source of truth has shifted to constitutional architecture**  
✅ **Estate is navigable without legacy folders**  
✅ **Ready for Phase 3: GitHub deployment**  

---

# Next Steps

1. **Review this plan** — Drew validates destinations and timeline
2. **Clarify decision points** — Get Drew's guidance on ambiguous cases
3. **Begin Phase 2a** — Start with quick wins (SidekickAir, etc.)
4. **Track progress** — Update this document as ingestion proceeds
5. **Verify each stage** — Spot-checks ensure no loss
6. **Document learnings** — Note what works, what's inefficient
7. **Retire folders incrementally** — Only after successful ingestion

---

**Status: READY FOR REVIEW & EXECUTION**

**Estimated timeline: 2-2.5 weeks of careful ingestion**

**Risk: LOW (with proper backup and verification)**

**Next phase: GitHub deployment and publication**
