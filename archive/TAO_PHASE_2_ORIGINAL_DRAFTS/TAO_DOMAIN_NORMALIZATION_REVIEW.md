# TAO DOMAIN — Normalization Review

**Date:** July 5, 2026  
**Status:** Repository Review (Pre-Commitment)  
**Authority:** Claude (Chief of Staff)  
**Scope:** Determine canonical versions before permanent commitment to GitHub  

---

# OBJECTIVE

Identify which version of each Tao document should become permanent, ensuring:
- No duplicate active files in committed repository
- No loss of intellectual content
- Clear canonical source for each document
- Single source of truth for each concept

---

# INVENTORY

## File Locations Identified

**Location A (Old Flat Structure):**
- `05_DOMAINS/FOUNDER_DOMAIN/TAO_*.md` (8 files)
- File sizes: 12-19K each
- Status: Original Phase 2 curation work

**Location B (New Folder Structure):**
- `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_*.md` (9 files)
- File sizes: 4-15K each
- Status: Revised consolidated versions

---

# DETAILED FILE COMPARISON

| Document | Old Location | New Location | Old Size | New Size | Status | Version Type |
|----------|---|---|---|---|---|---|
| TAO_DOMAIN.md | Does not exist | TAO/TAO_DOMAIN.md | — | 13K | New | Canonical governing document |
| TAO_KNOWLEDGE_MAP.md | 14K | TAO/TAO_KNOWLEDGE_MAP.md | 14K | 15K | Both exist | Revised (consolidated) |
| TAO_PUBLICATION_ROADMAP.md | 12K | TAO/TAO_PUBLICATION_ROADMAP.md | 12K | 6.8K | Both exist | Revised (condensed) |
| TAO_CE_CURRICULUM.md | 19K | TAO/TAO_CE_CURRICULUM.md | 19K | 7.2K | Both exist | Revised (consolidated) |
| TAO_RESEARCH_PIPELINE.md | 17K | TAO/TAO_RESEARCH_PIPELINE.md | 17K | 8.2K | Both exist | Revised (consolidated) |
| TAO_SPEAKING_ROADMAP.md | 15K | TAO/TAO_SPEAKING_ROADMAP.md | 15K | 4.0K | Both exist | Revised (consolidated) |
| TAO_MOVEMENT_STRATEGY.md | 15K | TAO/TAO_MOVEMENT_STRATEGY.md | 15K | 4.1K | Both exist | Revised (consolidated) |
| TAO_RELATIONSHIP_MAP.md | 16K | TAO/TAO_RELATIONSHIP_MAP.md | 16K | 4.1K | Both exist | Revised (consolidated) |
| TAO_CURATION_COMPLETION_REPORT.md | 15K | TAO/TAO_DOMAIN_CONSOLIDATION_REPORT.md | 15K | 13K | Different names | Functionally equivalent |

---

# FILE ANALYSIS

## Type 1: New Document (No Duplicate)

### TAO_DOMAIN.md
- **Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_DOMAIN.md`
- **Status:** Canonical governing document (NEW)
- **Content Type:** Constitutional-level domain definition
- **Duplicate Exists:** NO
- **Action:** KEEP in TAO/ folder (this is the new foundational document)

---

## Type 2: Pair with Old Location Larger (Original) and New Location Smaller (Revised)

For all other documents, the pattern is consistent:

### TAO_KNOWLEDGE_MAP.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_KNOWLEDGE_MAP.md` (14K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_KNOWLEDGE_MAP.md` (15K)
- **Content Analysis:** New version adds explicit references to TAO_DOMAIN.md, removes redundant domain definitions, adds Pillar mapping
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (standalone framework)

### TAO_PUBLICATION_ROADMAP.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_PUBLICATION_ROADMAP.md` (12K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_PUBLICATION_ROADMAP.md` (6.8K)
- **Content Analysis:** New version removes standalone publishing philosophy, adds explicit research question mapping, shows how publications serve domain
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (standalone framework)

### TAO_CE_CURRICULUM.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_CE_CURRICULUM.md` (19K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_CE_CURRICULUM.md` (7.2K)
- **Content Analysis:** New version removes standalone CE philosophy, adds Pillar mapping to each level, shows how curriculum serves domain, adds teaching standards requiring TAO_DOMAIN.md reference
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (standalone framework)

### TAO_RESEARCH_PIPELINE.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_RESEARCH_PIPELINE.md` (17K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_RESEARCH_PIPELINE.md` (8.2K)
- **Content Analysis:** New version removes standalone research philosophy, explicitly states that it operationalizes TAO_DOMAIN.md Research Agenda, adds Research Question mapping
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (standalone framework)

### TAO_SPEAKING_ROADMAP.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_SPEAKING_ROADMAP.md` (15K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_SPEAKING_ROADMAP.md` (4.0K)
- **Content Analysis:** New version is significantly condensed, removes standalone philosophy, focuses on how speaking serves domain, maintains core tier structure but removes detailed descriptions
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (extensive but redundant)
- **Note:** Content loss is minimal; core strategic structure preserved

### TAO_MOVEMENT_STRATEGY.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_MOVEMENT_STRATEGY.md` (15K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_MOVEMENT_STRATEGY.md` (4.1K)
- **Content Analysis:** New version removes standalone philosophy, reframes success around domain adoption, maintains 4-phase timeline and stakeholder strategies but condensed
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (extensive but redundant)
- **Note:** Core strategic elements preserved; detailed implementation guidance removed

### TAO_RELATIONSHIP_MAP.md
- **Old Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_RELATIONSHIP_MAP.md` (16K)
- **New Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_RELATIONSHIP_MAP.md` (4.1K)
- **Content Analysis:** New version maps collaborators to specific Pillars, removes standalone philosophy, positions as ecosystem supporting domain
- **Recommendation:** Keep NEW version (consolidated, aligned to domain)
- **Retire:** OLD version (less structured)
- **Note:** Loss of collaborator detail; primary collaborators and gap analysis retained

---

## Type 3: Different Names, Functionally Equivalent

### TAO_CURATION_COMPLETION_REPORT.md vs. TAO_DOMAIN_CONSOLIDATION_REPORT.md
- **Old Name/Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO_CURATION_COMPLETION_REPORT.md` (15K)
- **New Name/Location:** `05_DOMAINS/FOUNDER_DOMAIN/TAO/TAO_DOMAIN_CONSOLIDATION_REPORT.md` (13K)
- **Content Analysis:** New version provides clearer documentation of consolidation process, alignment verification
- **Recommendation:** Keep NEW version (better name reflects actual purpose)
- **Retire:** OLD version (outdated name)

---

# CONTENT LOSS ASSESSMENT

## Minimal Loss (Acceptable)

**TAO_SPEAKING_ROADMAP.md:**
- Old: 15K (extensive regional opportunity details)
- New: 4.0K (core tier structure maintained)
- Loss: Detailed conference/workshop listings, regional specifics
- Mitigation: Core strategy preserved; details can be added back if needed during implementation

**TAO_MOVEMENT_STRATEGY.md:**
- Old: 15K (extensive stakeholder and timeline details)
- New: 4.1K (core phases and adoption strategy)
- Loss: Detailed implementation metrics, year-by-year breakdowns
- Mitigation: Core structure preserved; metrics can be expanded during implementation

**TAO_RELATIONSHIP_MAP.md:**
- Old: 16K (detailed collaborator information)
- New: 4.1K (primary collaborators + gaps)
- Loss: Some secondary collaborator detail
- Mitigation: Primary relationships preserved; gaps documented for future outreach

## No Significant Loss

All other document pairs retain core intellectual content while removing redundancy and improving alignment to domain.

---

# PROPOSED CANONICAL STRUCTURE

After normalization, the committed repository will contain:

```
05_DOMAINS/
└── FOUNDER_DOMAIN/
    └── TAO/
        ├── TAO_DOMAIN.md                          (Canonical Governing Document)
        ├── TAO_KNOWLEDGE_MAP.md                   (Expression: Knowledge Architecture)
        ├── TAO_PUBLICATION_ROADMAP.md             (Expression: Scholarship Strategy)
        ├── TAO_CE_CURRICULUM.md                   (Expression: Education Strategy)
        ├── TAO_RESEARCH_PIPELINE.md               (Expression: Research Strategy)
        ├── TAO_SPEAKING_ROADMAP.md                (Expression: Communication Strategy)
        ├── TAO_MOVEMENT_STRATEGY.md               (Expression: Field Adoption Strategy)
        ├── TAO_RELATIONSHIP_MAP.md                (Expression: Collaboration Ecosystem)
        └── TAO_DOMAIN_CONSOLIDATION_REPORT.md     (Documentation of Consolidation)
```

**Result:**
- ✓ Single canonical version of each document
- ✓ No duplicate active files
- ✓ Clear folder organization
- ✓ No loss of core intellectual content
- ✓ Improved alignment and governance

---

# ACTIONS REQUIRING FOUNDER APPROVAL

## Before Normalization Can Proceed

1. **Approve NEW versions as canonical**
   - Decision: Are the consolidated versions in TAO/ folder the versions to commit?
   - Impact: Old flat-location files will be retired

2. **Approve content loss mitigation**
   - Loss: Speaking roadmap, movement strategy, relationship map have reduced detail
   - Mitigation: Details can be re-added during implementation phase
   - Decision: Accept this trade-off for architectural clarity?

3. **Approve structure finalization**
   - Structure: Single TAO/ folder becomes canonical
   - No other Tao files outside this folder
   - Decision: Proceed with this structure?

4. **Approve deletion plan**
   - Delete: All 8 files from `05_DOMAINS/FOUNDER_DOMAIN/` flat location
   - Keep: 9 files in `05_DOMAINS/FOUNDER_DOMAIN/TAO/` folder
   - Decision: Authorize deletion of old flat location files after commit?

---

# REPOSITORY VERIFICATION

## Proposed Committed State

**Will Result In:**
- ✓ Single canonical Tao folder: `05_DOMAINS/FOUNDER_DOMAIN/TAO/`
- ✓ Single canonical version of each document
- ✓ No duplicate active files
- ✓ No loss of governing intellectual content
- ✓ All 9 core domain documents present
- ✓ Clear hierarchy and relationships

**Will NOT Result In:**
- ✗ Orphaned files
- ✗ Conflicting versions
- ✗ Missing intellectual content
- ✗ Ambiguous structure

---

# RECOMMENDATION SUMMARY

| Action | Document | From | To | Status |
|--------|----------|------|-----|--------|
| KEEP | TAO_DOMAIN.md | — | TAO/ | Canonical governing |
| KEEP | TAO_KNOWLEDGE_MAP.md | OLD 14K | NEW 15K | Consolidated, aligned |
| KEEP | TAO_PUBLICATION_ROADMAP.md | OLD 12K | NEW 6.8K | Consolidated, aligned |
| KEEP | TAO_CE_CURRICULUM.md | OLD 19K | NEW 7.2K | Consolidated, aligned |
| KEEP | TAO_RESEARCH_PIPELINE.md | OLD 17K | NEW 8.2K | Consolidated, aligned |
| KEEP | TAO_SPEAKING_ROADMAP.md | OLD 15K | NEW 4.0K | Consolidated, aligned |
| KEEP | TAO_MOVEMENT_STRATEGY.md | OLD 15K | NEW 4.1K | Consolidated, aligned |
| KEEP | TAO_RELATIONSHIP_MAP.md | OLD 16K | NEW 4.1K | Consolidated, aligned |
| RENAME | TAO_CURATION_COMPLETION_REPORT | OLD name | TAO_DOMAIN_CONSOLIDATION_REPORT | Better reflects purpose |
| RETIRE | Old flat location files | 05_DOMAINS/FOUNDER_DOMAIN/TAO_*.md | (delete after approval) | Superseded by consolidated versions |

---

# NEXT STEPS

**Upon Founder Approval:**

1. Approve the NEW versions in `/TAO/` folder as canonical
2. Approve content loss mitigation approach
3. Authorize deletion of OLD flat location files
4. Authorize commit of consolidated domain
5. Authorize commit message and permanent marking

**Then:**

Stage all files in `/TAO/` folder for commit.

Delete all files from flat location.

Commit as permanent domain milestone.

Push to GitHub.

---

# PERMANENT RULE VERIFICATION

✓ **Intellectual Review:** Domain passed — consolidated, aligned, coherent

✓ **Repository Review:** In progress — this document

**Status:** Ready for Founder approval to proceed to commitment phase.

---

**Prepared by:** Claude, Chief of Staff  
**Date:** July 5, 2026  
**Authority:** Awaiting Founder approval  
**Next:** Normalization execution (upon approval)

