# Estate Ingestion Plan — Version 2.0
## Institutional Importance Sequencing
## Date: June 30, 2026
## Status: APPROVED & REVISED

---

# Strategic Revision

**Original approach:** Prioritize by technical simplicity (quick wins first)

**Revised approach:** Prioritize by institutional importance (what matters most first)

The Intellectual Estate's value comes from what it preserves, not how easy it is to migrate.

**New sequencing:**

1. **Founder Domain** — Core to everything (Drew's work)
2. **Publishing Domain** — 30+ year authority platform
3. **Education Domain** — Active business operation
4. **Innovation Domain** — Products and IP
5. **Intellectual Estate** — Publications and frameworks
6. **Legacy Materials** — Archive and historical

---

# Core Modifications

## 1. The Tao: Curated Publication Archive (Not Folder Migration)

**The Tao is the estate's crown jewel.** It deserves curatorial care, not mechanical file moving.

### What This Means

**Tao ingestion is not:** Copy 661 files into INTELLECTUAL_ESTATE/BOOKS/

**Tao ingestion is:** Carefully curate a publication archive that demonstrates:
- Publishing process and evolution
- Design decisions and iterations
- Marketing strategy and results
- Technical implementation
- Permanent record of how this work was created

### Ingestion Process for Tao

**Phase 1: Curation** (1-2 days)
- Review all 661 files
- Categorize by type (manuscript, design, website, marketing, automation)
- Identify what's permanent knowledge vs. temporary working materials
- Decide what tells the story of this publication

**Phase 2: Archive Structure** (1 day)
- Create curated structure in INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/
  - manuscript/ (all versions with dates)
  - cover/ (design evolution documented)
  - website/ (Elementor config + theme customizations)
  - marketing/ (strategy + assets + results)
  - scripts/ (automation that can be reused)
  - metadata/ (publishing info, sales, reviews)
  - evolution/ (how this book was created)

**Phase 3: Documentation** (1 day)
- Write README explaining curation decisions
- Document why certain versions were kept
- Show decision-making process
- Create timeline of publication evolution

**Phase 4: Capability Extraction** (1 day)
- Extract reusable patterns to CAPABILITIES/PUBLISHING/
  - Elementor website templates
  - Book cover design workflow
  - Marketing asset templates
  - Automation scripts (build systems)

**Total effort: 4-5 days (not 12-16 hours)**

**Tao is treated as **curation project**, not folder migration**

### Outcomes

✅ Final manuscript in INTELLECTUAL_ESTATE  
✅ Complete design evolution preserved  
✅ Publication process documented  
✅ Reusable patterns extracted to Capabilities  
✅ Publication archive tells the story of creation  

---

## 2. Boston Bodyworker: Active Publishing Platform (Incremental Preservation)

**Boston Bodyworker is not legacy. It's an active, appreciating intellectual asset.**

### Current State
- Website: External (bostonbodyworker.com, WordPress)
- Content: 30+ years, largely unversioned
- Authority: High domain authority, backlinks, SEO equity
- Status: Active (not archived)

### Preservation Strategy (Not Migration)

**Don't move the website to Coding-folder.**

**Instead: Incremental preservation project**

### Phase 1: Archive Capture (2-3 weeks)
- Export all blog posts from WordPress
- Capture publish dates and metadata
- Archive images and media
- Document URL structure and redirects
- Create wayback snapshots

### Phase 2: Versioning Key Content (Ongoing)
- Version clinical articles (markdown)
- Version essays and newsletters (markdown)
- Version media metadata (images, dates, context)
- Track publication history

### Phase 3: Live Sync (Ongoing)
- New content flows to 05_DOMAINS/PUBLISHING_DOMAIN/ as published
- Website remains at external URL
- Repo contains versioned archive + living feed

### Placement in Architecture

**05_DOMAINS/PUBLISHING_DOMAIN/WEBSITE/**
- website-export/ (historical archive)
- live-content/ (current feed)
- media/ (images, videos)
- operations/ (domain, hosting, analytics)

### Effort

**Month 1:** Initial archive capture (10-15 hours)  
**Month 2+:** Ongoing sync as new content publishes (2-3 hours/month)

**Not a one-time migration. A continuous preservation process.**

---

## 3. Research: Keep Source in Google Drive, Synthesis in Project Atlas

**Working materials stay where they work. Completed knowledge moves to permanent estate.**

### Architecture

**Google Drive:**
- Raw research notes
- Interview recordings
- Data files
- Working papers
- Experimental analysis

**Project Atlas (02_PROJECT_ATLAS/):**
- Synthesized findings
- Validated frameworks
- Published research
- Reusable methodologies

**Intellectual Estate (03_INTELLECTUAL_ESTATE/):**
- Permanent research outputs
- Published papers
- Frameworks that became doctrine

### Rationale

**Why not move everything to repo?**
- Keeps large files (video, audio) in specialized storage
- Preserves natural workflow (Google Drive is better for active research)
- Separates working materials from permanent knowledge
- Reduces repo bloat

**Why move synthesis to Project Atlas?**
- Synthesis is knowledge, not raw material
- Needs to be discoverable in the estate
- Should feed other domains
- Is part of the permanent record

### Example

**Therapeutic Alliance Investigation:**
- Raw materials: Google Drive (interviews, notes, experimental data)
- Synthesis: 02_PROJECT_ATLAS/01_THERAPEUTIC_ALLIANCE/ (framework.md, findings.md)
- Publication: 03_INTELLECTUAL_ESTATE/PAPERS/therapeutic-alliance.md (when published)

---

## 4. RETIRED Lifecycle State

**New state: RETIRED (for legacy folders after successful ingestion)**

### Lifecycle States (Updated)

```
CREATION
  ↓
REFINEMENT
  ↓
STABLE
  ↓
PUBLICATION
  ↓
PRESERVATION
  ↓
RETIRED ← NEW STATE
  ↓
ARCHIVE
```

### RETIRED State Definition

**Used for:** Legacy folders after successful ingestion and verification

**Meaning:** "This folder has been successfully ingested into the constitutional architecture. All knowledge has been mapped. The folder is no longer active but is kept as historical reference."

**Governance:** 
- Original folder is backed up
- Can be deleted or kept as readonly reference
- Not actively maintained
- Documented in INGESTION_LOG.md

**Examples:**
- Learn2Tape/ → RETIRED (after ingestion to EDUCATION_DOMAIN)
- SidekickAir/ → RETIRED (after ingestion to INNOVATION_DOMAIN)
- _system/ → RETIRED (after consolidation to 01_OPERATING_SYSTEM)

### Difference from ARCHIVE

**ARCHIVE state:** Old work *within* a domain (e.g., EDUCATION_DOMAIN/ARCHIVE/old-courses/)

**RETIRED state:** Legacy folder structure *after successful ingestion* (e.g., Learn2Tape/ folder is RETIRED after content moves to EDUCATION_DOMAIN)

---

# Revised Sequencing by Institutional Importance

## Phase 1: Founder Domain (Days 1-3)
**Priority: CRITICAL**

**Why first:** Everything originates here. Drew's work, thinking, decision-making.

### What gets ingested:
- Personal philosophy and writings
- Speaking and interviews (from legacy if captured)
- Decision history
- Creative projects in development

### Sources:
- FOUNDER_DOMAIN existing structure
- Any personal materials in legacy folders
- Historic decision logs

### Effort: 3-4 hours
### Outcome: Founder Domain fully populated with personal work

---

## Phase 2: Publishing Domain (Days 3-5)
**Priority: VERY HIGH**

**Why second:** 30+ year authority asset that compounds over time.

### What gets ingested:
- Boston Bodyworker description (from BostonBodyworker/1 file)
- Initial website archive capture
- Sample of historical content

### Preservation approach:
- **Not a one-time migration**
- Incremental project that continues over weeks/months
- Live sync with external website
- Versioning of new content as published

### Effort: 
- Initial setup: 2-3 hours
- Ongoing sync: 2-3 hours/month

### Outcome: Publishing Domain established as active platform with preservation plan

---

## Phase 3: Education Domain (Days 5-7)
**Priority: HIGH**

**Why third:** Active business operation with clear structures.

### What gets ingested:
- Learn2Tape/ (50 files) → EDUCATION_DOMAIN
- Course materials
- Marketing campaigns (NCB campaign)
- Product specs (K-Cuts)
- Performance data

### Effort: 5-6 hours
### Outcome: Education Domain fully populated with all course materials and operations

### Retirement: Learn2Tape/ folder marked RETIRED

---

## Phase 4: Innovation Domain (Days 7-9)
**Priority: HIGH**

**Why fourth:** Active product development, patents, IP.

### What gets ingested:
- SidekickAir/ (34 files) → INNOVATION_DOMAIN
- Product briefs and specs
- Manufacturing partnerships
- Patent strategy and documentation
- Decision logs

### Effort: 3-4 hours
### Outcome: Innovation Domain fully populated with product and IP strategy

### Retirement: SidekickAir/ folder marked RETIRED

---

## Phase 5: Intellectual Estate - Publications (Days 9-14)
**Priority: HIGH**

**The Tao requires curatorial care, not mechanical migration.**

### What gets ingested:
- Tao/ (661 files) → Curated archive in INTELLECTUAL_ESTATE/BOOKS/
- Manuscript (all versions with dates)
- Cover design evolution
- Website configuration and theme customizations
- Marketing materials and strategy documentation
- Automation scripts (extracted to CAPABILITIES/PUBLISHING/)
- Publication record and sales data

### Approach: Curated archive (4-5 days)
**Day 1-2:** Review and categorize all 661 files  
**Day 3:** Structure archive in INTELLECTUAL_ESTATE  
**Day 4:** Extract reusable patterns to CAPABILITIES  
**Day 5:** Document curation decisions and publication evolution

### Effort: 4-5 days (significant, but intentional)
### Outcome: Tao publication archive demonstrates publishing process and becomes template for future books

### Retirement: Tao/ folder marked RETIRED

---

## Phase 6: Project Atlas & Capabilities (Days 14-16)
**Priority: MEDIUM**

**What gets ingested:**
- Project Atlas research materials (synthesis, frameworks)
- Marketing infrastructure
- Root-level operational files
- Operating system consolidation

### Note: Research source materials stay in Google Drive
**Only synthesis moves to Project Atlas**

### Effort: 3-4 hours
### Outcome: Research engine populated with synthesized knowledge

---

## Phase 7: Legacy Materials (Days 16-18)
**Priority: MEDIUM**

**What gets ingested:**
- Archive/ folder (38 files)
- Root-level historical .md files
- Project track files (for history)
- Operating system historical materials

### Effort: 3-4 hours
### Outcome: Historical materials organized with metadata explaining preservation

---

# Total Sequencing

| Phase | Domain/Focus | Days | Hours | Lifecycle Result |
|---|---|---|---|---|
| 1 | Founder Domain | 1-3 | 3-4 | Active |
| 2 | Publishing Domain | 3-5 | 2-3 (initial) | Active + Ongoing |
| 3 | Education Domain | 5-7 | 5-6 | Active → RETIRED |
| 4 | Innovation Domain | 7-9 | 3-4 | Active → RETIRED |
| 5 | Publications (Tao) | 9-14 | 12-16 | PRESERVATION → RETIRED |
| 6 | Project Atlas & Capabilities | 14-16 | 3-4 | Active |
| 7 | Legacy Materials | 16-18 | 3-4 | ARCHIVE |
| **TOTAL** | | **~18 days** | **31-41 hours** | **Estate fully ingested** |

---

# INGESTION_LOG.md Framework

Every migration is recorded. The evolution of the Intellectual Estate becomes part of its permanent history.

### Log Structure

**File location:** `01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/INGESTION_LOG.md`

**Entry template:**

```markdown
## [Domain Name] Ingestion
**Date:** YYYY-MM-DD  
**Duration:** X hours  
**Source folder:** [Original legacy folder]  
**Files processed:** [Count]  
**Key assets ingested:**
- [Asset 1]
- [Asset 2]

**Curation decisions:**
- [Decision 1 + rationale]
- [Decision 2 + rationale]

**Files moved:**
[Table of source → destination mappings]

**Files archived:**
[What was retired or deleted + why]

**Lifecycle states assigned:**
[Count of each state]

**Relationships documented:**
- [Key relationship 1]
- [Key relationship 2]

**Verification:**
- [ ] File count verified
- [ ] No content loss
- [ ] Relationships preserved
- [ ] Lifecycle states assigned

**Legacy folder status:**
- [ ] Backed up to archive/
- [ ] Original marked RETIRED
- [ ] Can be safely deleted

**Notes:**
[Observations, challenges, learnings]
```

### Purpose

✅ **Traceability** — Track what moved where and when  
✅ **Decision record** — Document why choices were made  
✅ **Verification** — Confirm completeness  
✅ **Learnings** — Record what worked, what didn't  
✅ **History** — Estate's evolution becomes part of its story  

---

# Lifecycle States (Revised)

## CREATION
- Idea is born
- Drafts exist
- Not yet refined

## REFINEMENT
- Work is being improved
- Feedback gathered
- Iteration happening

## STABLE
- Finished work
- Ready for use
- Well-documented

## PUBLICATION
- Work is published
- Widely shared
- Impact being measured

## PRESERVATION
- In Intellectual Estate
- Permanent record
- Canonical reference

## RETIRED ← NEW
- Legacy folder after successful ingestion
- All knowledge has been mapped
- Original folder backed up or deleted
- Documented in INGESTION_LOG

## ARCHIVE
- Old work within a domain (ARCHIVE/ subdirectories)
- Historical reference
- Not actively used

---

# Ingestion Log Example

Once created, INGESTION_LOG.md will show the complete evolution:

```markdown
# Intellectual Estate Ingestion Log

## Founder Domain Ingestion
**Date:** 2026-07-01
**Duration:** 3.5 hours
**Source:** Personal materials, legacy docs
**Files processed:** ~40
**Status:** Complete
**Verification:** All confirmed

## Publishing Domain Ingestion (Initial)
**Date:** 2026-07-05
**Duration:** 2.5 hours
**Source:** BostonBodyworker/ folder + archive capture
**Files processed:** 50
**Status:** Complete + Ongoing incremental sync
**Note:** Active preservation project, not one-time migration

## Education Domain Ingestion
**Date:** 2026-07-07
**Duration:** 5.5 hours
**Source:** Learn2Tape/ folder
**Files processed:** 50
**Status:** Complete
**Legacy folder:** Marked RETIRED
**Verification:** All confirmed

## Innovation Domain Ingestion
**Date:** 2026-07-09
**Duration:** 3.5 hours
**Source:** SidekickAir/ folder
**Files processed:** 34
**Status:** Complete
**Legacy folder:** Marked RETIRED
**Verification:** All confirmed

## Publications: Tao Curation & Archive
**Date:** 2026-07-09 to 2026-07-14
**Duration:** 15 hours (curated archive, not mechanical migration)
**Source:** Tao/ folder (661 files)
**Curation decisions:** [See INGESTION_LOG entry for detailed decisions]
**Extracted to Capabilities:** Website templates, build scripts, design patterns
**Status:** Complete
**Legacy folder:** Marked RETIRED
**Verification:** All confirmed

...and so on for each phase
```

---

# Moving Plan to Operating System (Post-Stage-2)

**When Stage Two is complete:**

This document (ESTATE_INGESTION_PLAN_V2.md) moves to:

`01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/ESTATE_INGESTION_PLAN_V2.md`

**With companion document:**

`01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/INGESTION_LOG.md` (complete historical record)

**This preserves the implementation knowledge for future reference:**
- How was the estate ingested?
- What decisions were made?
- What patterns worked?
- What took longer than expected?
- What can be reused for future integrations?

---

# Criteria for Completing Stage Two

### Completion means:

✅ All 7 phases completed  
✅ ~820 files ingested  
✅ All domains populated  
✅ All active legacy folders marked RETIRED  
✅ Publication Domain has preservation plan  
✅ Research architecture (Google Drive + Project Atlas) established  
✅ Complete INGESTION_LOG.md created  
✅ Zero loss of intellectual value  
✅ All relationships documented  
✅ Estate ready for GitHub deployment  

### Verification:

- [ ] Each domain fully populated
- [ ] Legacy folders accounted for (backed up or archived)
- [ ] INGESTION_LOG complete and accurate
- [ ] No files lost in migration
- [ ] All relationships preserved
- [ ] Lifecycle states assigned
- [ ] RETIRED folders documented
- [ ] Estate is navigable and coherent

---

# Next Phase (Stage Three)

**After Stage Two completion:**

1. **Move ESTATE_INGESTION_PLAN_V2.md** to 01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/
2. **Create INGESTION_LOG.md** to 01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/
3. **Push entire estate to GitHub** (source of truth established)
4. **Begin living stewardship** (real-world use drives evolution)

---

**Status: APPROVED WITH STRATEGIC MODIFICATIONS**

**Core principle: Institutional importance, not technical simplicity**

**Timeline: ~18 days of intentional ingestion**

**Outcome: Fully ingested, curated, preserved Intellectual Estate ready for GitHub**
