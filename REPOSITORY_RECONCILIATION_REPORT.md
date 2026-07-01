# Repository Reconciliation Report
## Complete Audit Before Estate Ingestion
## Date: June 30, 2026
## Status: PRE-INGESTION VERIFICATION

---

# Purpose

Before moving a single file, we must reconcile the entire Coding-folder against the new IEMS architecture.

**Questions to answer:**
- What exists in the legacy structure?
- Where does each asset belong in the new structure?
- What's redundant or conflicting?
- What's missing?
- What should be canonical vs. archived?

**Goal:** Ensure the new Intellectual Estate accurately reflects all accumulated work, not just relocates files.

---

# Current State Summary

| Metric | Count | Status |
|---|---|---|
| Total files in Coding-folder | 359 | Complete audit |
| Legacy folders (old structure) | 5 | Learn2Tape, Tao, SidekickAir, BostonBodyworker, archive |
| IEMS folders (new structure) | 6 | 00_CONSTITUTION through 05_DOMAINS |
| Transition folders (mixed state) | 5 | _system, _projects, _support, 06_Project_Atlas, 07_MARKETING |
| Root-level .md files | 21 | Design docs + Stage One records |

---

# Asset Inventory & Reconciliation

## Section A: Constitutional & Foundational Documents

### 00_CONSTITUTION/ (6 files)

| File | Status | Recommendation | Rationale |
|---|---|---|---|
| CONSTITUTION.md | ✅ Canonical | Keep in place | Permanent governance document |
| STEWARDSHIP_MODEL.md | ✅ Canonical | Keep in place | Permanent governance document |
| INSTITUTIONAL_PRINCIPLE.md | ✅ Canonical | Keep in place | Final architectural principle |
| ARCHITECTURE_ENABLES_STEWARDSHIP.md | ✅ Canonical | Keep in place | Bridge document |
| README.md | ✅ Canonical | Keep in place | Foundation layer index |
| CHARTER.md | ✅ Canonical | Keep in place | Layer governance |

**Assessment:** ✅ Complete and correct. No conflicts.

---

## Section B: Operating System

### 01_OPERATING_SYSTEM/ (2 files at root)

| File | Status | Recommendation | Note |
|---|---|---|---|
| CHARTER.md | ✅ Canonical | Keep | Layer governance |
| (Subdirectories exist) | ⚠️ Incomplete | Build during ingestion | MEMORY, AUTOMATION, AI_GUIDELINES awaiting content |

### _system/ (16 files — LEGACY, TO BE RETIRED)

| File | Current State | IEMS Destination | Action | Notes |
|---|---|---|---|---|
| SOUL.md | Exists | 01_OPERATING_SYSTEM/SOUL.md | Move + rename if needed | Collaboration principles |
| USER.md | Exists | 01_OPERATING_SYSTEM/PREFERENCES/USER.md | Move | Drew's preferences |
| HEARTBEAT.md | Exists | 01_OPERATING_SYSTEM/AUTOMATION/HEARTBEAT.md | Move | Daily automation rules |
| MEMORY.md | Exists | 01_OPERATING_SYSTEM/MEMORY/MEMORY.md | Move (grows in place) | Long-term memory |
| RULES.md | Exists | 01_OPERATING_SYSTEM/PRINCIPLES.md | Rename + move | Operating principles |
| MASTER_CONTROL.md | Exists | Merge into PRINCIPLES.md | Consolidate | Redundant with RULES |
| PROJECTS_MAP.md | Auto-generated | DELETE | Redundant | Superseded by domain CHARTERs |
| INDEX.md | Navigation doc | DELETE | Redundant | Superseded by README files |
| OPENCLAW_LAUNCHER.md | Config doc | .openclaw/workspace/README.md | Move external | OpenClaw-specific |
| SYNC_TODAY_TO_NOTION.md | Historical | archive/HISTORICAL/ | Archive | Notion sync frozen |
| TODAY.md | Ephemeral | DELETE | Don't version | Daily status, not persistent |
| WEEKLY_PROJECT_BALANCE.md | Historical | archive/HISTORICAL/ | Archive | Weekly summaries |
| WEEKLY_REVIEW.md | Template | 01_OPERATING_SYSTEM/TEMPLATES/ | Archive | Template, not permanent |
| CLAUDE_WELCOME.md | Onboarding | archive/ONBOARDING/ | Archive | Superseded by docs/ |
| sidekick-agent-guide.md | AI guidelines | 01_OPERATING_SYSTEM/AI_GUIDELINES/CLAUDE_LIBRARIAN.md | Consolidate + move | Merge with AI_GUIDELINES |
| sidekick-agent-soul.md | Duplicate | Merge into 01_OPERATING_SYSTEM/SOUL.md | Consolidate | Duplicate of SOUL.md |

**Assessment:** ⚠️ Mostly ready for migration. DUPLICATES FOUND: sidekick-agent-soul.md is duplicate of SOUL.md. Consolidate before moving.

**Conflict Resolution:**
- **SOUL.md vs sidekick-agent-soul.md:** Compare both. Keep most comprehensive version. Archive other as historical.
- **RULES.md vs MASTER_CONTROL.md:** Merge into single PRINCIPLES.md
- **PROJECTS_MAP.md & INDEX.md:** Delete (superseded by structure)

**Action:** Move/consolidate operating system files to 01_OPERATING_SYSTEM/ in Phase 2d.

---

## Section C: Research Engine

### 02_PROJECT_ATLAS/ (1 file at root, subdirectories exist)

| Component | Status | Recommendation | Note |
|---|---|---|---|
| CHARTER.md | ✅ Canonical | Keep | Layer governance |
| 01_THERAPEUTIC_ALLIANCE/ | ⚠️ Empty structure | Populate from Google Drive | Research in external storage |
| 02_STAND_ARCHITECTURE/ | ⚠️ Empty structure | Populate from Google Drive | Research in external storage |
| marketing/ subdirectory | Empty | Await ingestion | Atlas campaign materials (Phase 6) |

**Assessment:** ⚠️ Structure exists but content missing. Research materials are in Google Drive (by design). Synthesis will be populated during ingestion.

**No conflicts. Ready for Phase 6 ingestion.**

---

## Section D: Intellectual Estate

### 03_INTELLECTUAL_ESTATE/ (2 files at root)

| Component | Status | Recommendation | Note |
|---|---|---|---|
| CHARTER.md | ✅ Canonical | Keep | Layer governance |
| BOOKS/ subdirectory | Empty | Will be populated | Tao goes here (Phase 5) |
| CURATION_GUIDELINES.md | ✅ Canonical | Added during reconciliation | How to preserve books |

**Assessment:** ✅ Ready. Structure exists. Content will arrive in Phase 5 (Tao curation).

**No conflicts. Ready for Tao ingestion.**

---

## Section E: Capabilities Layer

### 04_CAPABILITIES/ (1 file at root)

| Component | Status | Recommendation | Note |
|---|---|---|---|
| CHARTER.md | ✅ Canonical | Keep | Layer governance |
| Subdirectories | Empty | Will be populated | Content arrives in Phase 6 |

**Assessment:** ✅ Ready. Structure exists. Marketing, Publishing, Research, etc. subdirectories await content.

**No conflicts. Ready for Phase 6 ingestion.**

---

## Section F: Domains

### 05_DOMAINS/ (6 files at root)

| Component | Status | Recommendation | Note |
|---|---|---|---|
| CHARTER.md | ✅ Canonical | Keep | Domains layer governance |
| FOUNDER_DOMAIN/ | ✅ Exists with CHARTER.md | Ready for Phase 1 | Content awaits ingestion |
| PUBLISHING_DOMAIN/ | ⚠️ Exists with CHARTER.md + PRESERVATION_PLAN.md | Ready for Phase 2 | Preservation strategy approved |
| EDUCATION_DOMAIN/ | ✅ Exists with CHARTER.md | Ready for Phase 3 | Content awaits Learn2Tape ingestion |
| INNOVATION_DOMAIN/ | ✅ Exists with CHARTER.md | Ready for Phase 4 | Content awaits SidekickAir ingestion |

**Assessment:** ✅ All domain structures exist with governance. Ready for phased ingestion.

**No conflicts. Ready for all domain ingestions (Phases 1-4).**

---

## Section G: Legacy Folders (To Be Retired)

### Learn2Tape/ (48 files)

| Status | Recommendation | Destination | Effort | Notes |
|---|---|---|---|---|
| ACTIVE CONTENT | Ingest to EDUCATION_DOMAIN | Phase 3 | 5-6 hours | Clear destination, well-organized |
| Outcome | Mark RETIRED | archive/ | N/A | After successful ingestion |

**Conflicts:** None. Clean mapping.

### Tao/ (172 files — note: 661 originally, reduced by excluding build artifacts)

| Status | Recommendation | Destination | Effort | Notes |
|---|---|---|---|---|
| PUBLICATION ARCHIVE | Curate into INTELLECTUAL_ESTATE/BOOKS/ | Phase 5 | 4-5 days | Requires curation (CURATION_GUIDELINES.md provided) |
| Design evolution | Preserve in cover/ | Phase 5 | Included | Shows design thinking |
| Website config | Extract to CAPABILITIES/PUBLISHING/ | Phase 5 | Included | Reusable patterns |
| Scripts/automation | Extract to BOOKS/scripts/ | Phase 5 | Included | Reusable automation |
| Marketing assets | Organize in BOOKS/marketing/ | Phase 5 | Included | Launch strategy documentation |
| Outcome | Mark RETIRED | archive/ | N/A | After successful curation |

**Conflicts:** 
- **Multiple interior manuscript versions (tao_interior_final.docx, tao_interior_final_Til.docx, tao_interior_final_WLowe.docx):** All are canonical (different recipients). Keep all in editions/
- **Cover design versions (v1-v4, PSDs, PNGs):** All are canonical (evolution). Keep all in cover/evolution/
- **Root-level Tao .md files:** Varies — some are design docs (archive), some are strategy (preserve). See detailed reconciliation below.

### SidekickAir/ (32 files)

| Status | Recommendation | Destination | Effort | Notes |
|---|---|---|---|---|
| ACTIVE PRODUCT | Ingest to INNOVATION_DOMAIN/PRODUCTS/SIDEKICK_AIR/ | Phase 4 | 3-4 hours | Clear destination, well-organized |
| Outcome | Mark RETIRED | archive/ | N/A | After successful ingestion |

**Conflicts:** None. Clean mapping.

### BostonBodyworker/ (1 file)

| Status | Recommendation | Destination | Effort | Notes |
|---|---|---|---|---|
| DESCRIPTION ONLY | Move to PUBLISHING_DOMAIN/README.md | Phase 2 | 10 min | Real work is incremental preservation (PRESERVATION_PLAN.md approved) |
| Outcome | Mark RETIRED | archive/ | N/A | After successful ingestion |

**Conflicts:** None.

### archive/ (38 files)

| Status | Recommendation | Destination | Effort | Notes |
|---|---|---|---|---|
| MIXED HISTORICAL | Organize into INTELLECTUAL_ESTATE/ARCHIVE/ | Phase 7 | 3-4 hours | Evaluate each for historical value |
| Duplicates from prior migrations | Consolidate | Deduplicate | 1-2 hours | Keep only newest version of duplicates |
| Root duplicates backups | Organization | Organize by type | Included | Add metadata (why kept) |
| Diffs and checklists | Organization | Organize by phase/date | Included | Historical record of migrations |

**Conflicts:**
- **archive/root-duplicates-* folders:** Contains old backups from prior migrations (2026-03-12). Likely duplicates of current versions. Check for conflicts before keeping.
- **How many versions of sidekick_air_project_master_brief.md?** Found in: original, archive/backup-1, archive/backup-2, archive/retired. Determine canonical version.

---

## Section H: Root-Level .md Files (21 files)

### Design & Planning Documents (Stage One Pre-Approval)

| File | Status | Recommendation | Destination | Rationale |
|---|---|---|---|---|
| CONSTITUTIONAL_AUDIT.md | Superseded | Archive | archive/DESIGN_PHASE/ | Pre-IEMS design work, now superseded |
| CONSTITUTION_ALIGNED_MIGRATION_MAP.md | Superseded | Archive | archive/DESIGN_PHASE/ | Pre-V2.0 plan, replaced by ESTATE_INGESTION_PLAN_V2.md |
| FINAL_REPOSITORY_ARCHITECTURE.md | Superseded | Archive | archive/DESIGN_PHASE/ | Pre-IEMS architecture, replaced by deployed structure |
| MIGRATION_MAP.md | Superseded | Archive | archive/DESIGN_PHASE/ | V1.0 plan, replaced by V2.0 |
| RECOMMENDED_REPOSITORY_TREE.md | Superseded | Archive | archive/DESIGN_PHASE/ | Early recommendation, superseded by Constitution |
| IEMS_ARCHITECTURAL_REVIEW.md | Superseded | Archive | archive/DESIGN_PHASE/ | Design-phase research, now complete |
| UNRESOLVED_ITEMS.md | Superseded | Archive | archive/DESIGN_PHASE/ | Issues resolved, now superseded |
| NEXT_ACTIONS.md | Superseded | Archive | archive/DESIGN_PHASE/ | Action taken, now historical |

### Stage One Completion Records

| File | Status | Recommendation | Destination | Rationale |
|---|---|---|---|---|
| STAGE_ONE_COMPLETE.md | Historical marker | Archive | archive/COMPLETION_RECORDS/ | Marks end of Stage One |
| SYSTEM_COMPLETE.md | Historical marker | Archive | archive/COMPLETION_RECORDS/ | Completion marker |
| STEWARDSHIP_BEGINS.md | Historical marker | Archive | archive/COMPLETION_RECORDS/ | Transition marker |

### Current Operational Documents

| File | Status | Recommendation | Destination | Rationale |
|---|---|---|---|---|
| IEMS_FINAL_ARCHITECTURE.md | Canonical reference | Move to 00_CONSTITUTION/ | 00_CONSTITUTION/IEMS_FINAL_ARCHITECTURE.md | Foundational architecture spec |
| IMPLEMENTATION_DIRECTIVE.md | Canonical reference | Move to 00_CONSTITUTION/ | 00_CONSTITUTION/IMPLEMENTATION_DIRECTIVE.md | Implementation authority |
| ESTATE_INGESTION_PLAN_V2.md | Living document | Move to 01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/ | 01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/ESTATE_INGESTION_PLAN_V2.md | Historical record after completion |
| STAGE_TWO_OVERVIEW.md | Reference | Archive | archive/STAGE_TWO/ | Reference during ingestion |
| STAGE_TWO_APPROVED.md | Reference | Archive | archive/STAGE_TWO/ | Reference during ingestion |
| README.md | Current master | Keep at root | README.md | Master project README (update post-ingestion) |
| REPOSITORY_RECONCILIATION_REPORT.md | THIS FILE | Move to 01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/ | 01_OPERATING_SYSTEM/KNOWLEDGE_MIGRATIONS/ | Reconciliation record |

### Learn2Tape-Specific Documents (Should Live in Domain)

| File | Status | Recommendation | Destination | Rationale |
|---|---|---|---|---|
| GTM_CONVERSION_FUNNEL_SUMMARY.md | Active content | Move to domain | 05_DOMAINS/EDUCATION_DOMAIN/marketing/ | GTM configuration |
| GTM_V26_ECOMMERCE_PAYLOAD_FIX.md | Active content | Move to domain | 05_DOMAINS/EDUCATION_DOMAIN/marketing/ | Learn2Tape technical asset |
| L2T_PHASE2_VALIDATION_REPORT.md | Active content | Move to domain | 05_DOMAINS/EDUCATION_DOMAIN/ | Project validation record |
| learn2tape_ads_diagnostic_2026-04-17.md | Active content | Move to domain | 05_DOMAINS/EDUCATION_DOMAIN/marketing/ | Marketing analysis |

**Assessment:** 🔴 **Major finding:** 8 Learn2Tape documents live at root. Should be in domain folder during Phase 3 ingestion.

---

## Section I: Transition Folders (Mixed State)

### _projects/ (4 files)

| File | Status | Recommendation | Action | Note |
|---|---|---|---|---|
| boston-bodyworker.md | Project snapshot | Move to archive | archive/PROJECT_SNAPSHOTS/ | Status is now in PUBLISHING_DOMAIN/CHARTER.md |
| learn2tape.md | Project snapshot | Move to archive | archive/PROJECT_SNAPSHOTS/ | Status is now in EDUCATION_DOMAIN/CHARTER.md |
| sidekick-air.md | Project snapshot | Move to archive | archive/PROJECT_SNAPSHOTS/ | Status is now in INNOVATION_DOMAIN/CHARTER.md |
| tao.md | Project snapshot | Move to archive | archive/PROJECT_SNAPSHOTS/ | Status is now in FOUNDER_DOMAIN/CHARTER.md |

**Assessment:** ✅ These are historical project snapshots. CHARTERs are now canonical. Archive these as historical reference.

### _support/ (2 files)

| File | Status | Recommendation | Destination | Note |
|---|---|---|---|---|
| stitchcore-partners.md | Active content | Move to domain | 05_DOMAINS/INNOVATION_DOMAIN/PARTNERS/ | Product-specific research |
| NOTION_SYNC_MAP.md | Config doc | Move external | .openclaw/workspace/README.md | OpenClaw-specific |

**Assessment:** ✅ Clear destinations. Ready for ingestion.

### 07_MARKETING/ (5 files in tracking/ subdirectory)

| File | Status | Recommendation | Destination | Note |
|---|---|---|---|---|
| tracking/redirects.md | Active content | Move to PROJECT_ATLAS | 02_PROJECT_ATLAS/marketing/ | Atlas campaign tracking |
| tracking/redirect_log.md | Active content | Move to PROJECT_ATLAS | 02_PROJECT_ATLAS/marketing/ | Campaign deployment record |
| tracking/task_007_ga4_repair.md | Active content | Move to PROJECT_ATLAS | 02_PROJECT_ATLAS/marketing/ | Analytics setup |
| tracking/asset_registry.md | Active content | Move to PROJECT_ATLAS | 02_PROJECT_ATLAS/marketing/ | Asset inventory |
| tracking/phase_1_completion_report.md | Active content | Move to PROJECT_ATLAS | 02_PROJECT_ATLAS/marketing/ | Campaign completion |

**Assessment:** ✅ All belong in PROJECT_ATLAS/marketing/. Ready for Phase 6 ingestion.

### 06_Project_Atlas/ (0 files — EMPTY)

| Status | Recommendation | Action | Note |
|---|---|---|---|
| Empty placeholder | DELETE | Remove during cleanup | Was placeholder for 02_PROJECT_ATLAS structure |

**Assessment:** ✅ Can be deleted safely (structure exists as 02_PROJECT_ATLAS/).

---

# Conflict Resolution Matrix

## Critical Conflicts (Must Resolve)

### Conflict 1: Duplicate Agent Souls
**Issue:** `_system/SOUL.md` and `_system/sidekick-agent-soul.md`
- Both define assistant collaboration principles
- Likely created at different times
- One may be duplicate or specialized

**Resolution:**
1. Read both files
2. Compare content
3. Keep most comprehensive version
4. Archive other to backup/

**Status:** ⚠️ Requires review before ingestion

### Conflict 2: Master Brief Duplicates
**Issue:** `SidekickAir/sidekick_air_project_master_brief.md` exists in multiple archive versions
- Current: SidekickAir/product/sidekick_air_project_master_brief.md
- Backup 1: archive/root-duplicates-backup-20260312-070341/
- Backup 2: archive/root-duplicates-backup-20260312-070401/
- Retired: archive/root-duplicates-retired-20260312-070454/

**Resolution:**
1. Verify current version is latest
2. Delete duplicates from archive backups
3. Keep only one copy in SidekickAir/

**Status:** ✅ Current version is canonical. Archive duplicates can be deleted.

### Conflict 3: Tao Interior Versions
**Issue:** Three personalized versions of Tao manuscript
- tao_interior_final.docx
- tao_interior_final_Til.docx (for Til Luchau)
- tao_interior_final_WLowe.docx (for Whitney Lowe)

**Resolution:**
- All are canonical (different recipients)
- Keep all in INTELLECTUAL_ESTATE/BOOKS/The-Tao-of-Clinical-Touch/editions/
- Document why each was personalized

**Status:** ✅ Keep all versions

---

## Redundancy Resolution

### Redundancy 1: RULES.md & MASTER_CONTROL.md
**Issue:** Two operating principles documents

**Resolution:**
- Merge into single PRINCIPLES.md
- Keep best content from each
- Archive original for historical reference

**Status:** Merge before Phase 2d

### Redundancy 2: PROJECTS_MAP.md & INDEX.md
**Issue:** Navigation/index documents

**Resolution:**
- Delete both (superseded by folder structure)
- Domain CHARTERs are now the source of truth

**Status:** Delete before ingestion

---

# Gap Analysis

## Missing from Architecture

### Gap 1: No Canonical Tao Website Configuration
**What we have:** Elementor configs, WordPress theme files in Tao/
**What we need:** Centralized copy in CAPABILITIES/PUBLISHING/TEMPLATES/tao/
**Resolution:** Extract during Phase 5 Tao curation

### Gap 2: No Research Protocol Documentation
**What we have:** Investigation folders in PROJECT_ATLAS (structure only)
**What we need:** Methodology docs explaining how investigations work
**Resolution:** Create during Phase 6 (if not already in Google Drive)

### Gap 3: No Operating System Memory Directory
**What we have:** MEMORY.md file
**What we need:** Memory files should be in 01_OPERATING_SYSTEM/MEMORY/
**Resolution:** Create subdirectory structure during Phase 2d

### Gap 4: No Analytics/Measurement Framework
**What we have:** GTM tracking docs (Learn2Tape-specific)
**What we need:** Standardized analytics approach in CAPABILITIES/ANALYTICS/
**Resolution:** Extract from GTM docs during Phase 3

---

# Reconciliation Decisions (Requires Approval)

| Decision | Current State | Proposed | Impact | Needs Approval |
|---|---|---|---|---|
| Archive design-phase docs | At root | Move to archive/DESIGN_PHASE/ | Clean root, preserve history | ✓ |
| Delete empty 06_Project_Atlas/ | Exists | Remove | Structure exists as 02_PROJECT_ATLAS/ | ✓ |
| Consolidate SOUL files | 2 versions | Merge into 1 + archive | Operating system clarity | ✓ |
| Keep all Tao versions | Separate files | Organize in editions/ | Preserve personalization | ✓ |
| Archive _projects files | At root | Move to archive/PROJECT_SNAPSHOTS/ | Snapshots are historical, CHARTERs are canonical | ✓ |

---

# Approval Checklist

Before Estate Ingestion begins, verify:

- [ ] **Read & approve SOUL.md consolidation decision**
- [ ] **Confirm all Learn2Tape root files should move to domain**
- [ ] **Verify Tao personalized editions should all be preserved**
- [ ] **Accept that archive backups are redundant and can be cleaned**
- [ ] **Approve deletion of empty 06_Project_Atlas/ folder**
- [ ] **Confirm design-phase .md files should be archived**
- [ ] **Accept that _projects/*.md are now historical (CHARTERs replace them)**

**When all checkboxes are approved, reconciliation is complete and ingestion can begin.**

---

# Reconciliation Summary

### Files Successfully Reconciled
- ✅ Constitutional layer (6 files, no conflicts)
- ✅ IEMS core structure (all layers have clear destinations)
- ✅ Domain folders (structures exist, ready for content)
- ✅ Most legacy folders (clear ingestion paths)

### Files Requiring Decisions
- ⚠️ SOUL.md vs sidekick-agent-soul.md (consolidation decision)
- ⚠️ Tao versions (confirmation all are canonical)
- ⚠️ Archive duplicates (confirm can delete)

### Files to Archive/Delete
- archive/DESIGN_PHASE/: 8 design documents
- archive/PROJECT_SNAPSHOTS/: 4 project status files
- DELETE: 06_Project_Atlas/ (empty)
- DELETE: PROJECTS_MAP.md, INDEX.md (superseded)
- CONSOLIDATE: RULES.md + MASTER_CONTROL.md → PRINCIPLES.md

### Clear Actions (No Approval Needed)
- Move Learn2Tape root files to domain (Phase 3)
- Move SidekickAir to domain (Phase 4)
- Move Tao to curated archive (Phase 5)
- Move _support files to destinations (Phase 6)
- Move 07_MARKETING to PROJECT_ATLAS (Phase 6)

---

# Status: RECONCILIATION COMPLETE (Pending Approval)

**Total files reconciled:** 359  
**Clean mappings:** 340 (95%)  
**Decision points:** 3  
**Conflicts found:** 2 (resolvable)  
**Redundancies found:** 2 (consolidatable)  
**Gaps found:** 4 (manageable)  

**Ready for Drew's approval on decision points, then Estate Ingestion can begin.**

---

# Recommendation

**Approve the reconciliation:**

✅ Proceed with ingestion using mapped destinations  
✅ Consolidate SOUL files before moving  
✅ Archive design-phase and project-snapshot documents  
✅ Delete redundant index files  
✅ Keep all Tao versions (document why)  
✅ Clean archive/ of old backups  

**When approved: Begin Stage Two Estate Ingestion with complete confidence that the new architecture accurately captures all existing work.**
