# UNRESOLVED ITEMS — Migration Review Points

**Date:** June 30, 2026  
**Status:** Awaiting Drew decisions on flagged items

These items require clarification or decision before migration can proceed.

---

## 🔴 CRITICAL DECISIONS

### 1. GitHub as Permanent Source of Truth
**Status:** Blocked pending clarification
**Question:** Should we set up GitHub NOW and start syncing from day 1, or complete the Coding-folder migration first, then migrate to GitHub?

**Context:**
- Memory says "GitHub will become the permanent source of truth"
- Currently all work lives in Coding-folder on local disk
- Some projects (Notion sync, .openclaw) reference external systems

**Decision needed:**
- [ ] Set up repo on anthropics/drew-business (or similar) **before** executing file moves
- [ ] Keep Coding-folder as local cache, GitHub as source of truth
- [ ] OR: Complete local migration first, then push to GitHub as a single "v1.0" commit

**Recommendation:** Set up the GitHub repo NOW. It'll be your source of truth from day 1, and you can pull the migrated structure into it once approved.

---

### 2. Boston Bodyworker Status
**Status:** Needs clarification
**Question:** Is Boston Bodyworker truly legacy, or does it have active intellectual property/revenue streams?

**Current state:**
- Lives in `BostonBodyworker/the-boston-bodyworker.md` (1 file only)
- Memory classification: "legacy/intellectual estate unless otherwise marked active"
- No recent activity in Learn2Tape audit

**Decision needed:**
- [ ] Keep as archival reference (low maintenance)
- [ ] Activate as a separate business project (needs expansion)
- [ ] Retire completely and archive into historical records

**Recommendation:** Keep as-is for now (reference only). If you activate it later, we'll lift it out of archive.

---

### 3. Project Atlas Structure
**Status:** Placeholder exists; content TBD
**Question:** Should Project Atlas live as `projects/atlas/` or as a separate `research/` folder?

**Current state:**
- Memory references "Finding My Wei / Project Atlas" as an active research + publication initiative
- Therapeutic Alliance framework finalized
- 5-paper publication sequence locked
- Two sub-projects: 01-therapeutic-alliance, 02-stand-architecture
- But `06_Project_Atlas/` folder is empty (except .DS_Store)

**Decision needed:**
- [ ] Create `projects/atlas/` (groups it with business projects)
- [ ] Create `research/` folder (separates it as intellectual work)
- [ ] Keep under `06_Project_Atlas/` (honors existing numbering scheme)

**Recommendation:** Create `projects/atlas/` — it's a business initiative with publication revenue potential. The numbering (06_) can stay for organizational context if you want, but it should have a proper project structure with README, phases, and papers.

---

### 4. Tao vs. Learn2Tape Separation
**Status:** Structural clarity needed
**Question:** Should Tao book website (taoclinicaltouch.com) live inside `projects/tao/` or separately?

**Current state:**
- Tao folder has 661 files (book + website + marketing + assets)
- Memory says: "separate brand from Learn2Tape"
- Website is hosted on taoclinicaltouch.com (WordPress / Elementor Pro)
- Book marketing assets, landing page, Brevo infrastructure all mixed in

**Decision needed:**
- [ ] Keep as single `projects/tao/` (simplest structure)
- [ ] Split: `projects/tao/book/` + `projects/tao/website/`
- [ ] Separate: `projects/tao-book/` + `projects/tao-website/`

**Recommendation:** Keep as single `projects/tao/` with internal subfolders (book/, website/, marketing/, ce-program/). The folder structure should be clear, but one project parent makes sense since they're coordinated.

---

### 5. Marketing Assets: Global vs. Project-Specific
**Status:** Organization question
**Question:** Should there be a top-level `marketing/` folder for shared assets, or should all marketing live inside project folders?

**Current state:**
- `07_MARKETING/tracking/` has Atlas campaign infrastructure (redirects, GA4, etc.)
- Learn2Tape has its own `marketing/` subfolder (Google Ads, Brevo, email templates)
- Tao has marketing mixed with book assets (social images, reviewer outreach)
- Boston Bodyworker has none

**Decision needed:**
- [ ] Keep all marketing inside project folders (no global marketing/)
- [ ] Create `marketing/` at root level for cross-project campaigns
- [ ] Create `marketing/` but keep it minimal (only shared templates/brand)

**Recommendation:** No top-level `marketing/` folder. Keep marketing inside each project (it's owned by that project). BUT: if you create cross-project campaigns (e.g., influencer partnerships spanning multiple products), create a campaign subfolder inside `projects/` (e.g., `projects/_campaigns/`).

---

### 6. System Files in docs/ vs. Root
**Status:** Accessibility question
**Question:** Should `_system/` files move to `docs/` for GitHub visibility, or stay in `_system/` for local-only clarity?

**Current state:**
- `_system/` contains: SOUL.md, USER.md, HEARTBEAT.md, RULES.md, MEMORY.md
- These are currently machine-readable for Claude Code
- GitHub would make them visible to collaborators

**Decision needed:**
- [ ] Move to `docs/` (GitHub-native, visible to anyone with repo access)
- [ ] Keep in `_system/` (private, local-only)
- [ ] Split: system files in `docs/`, operational files in `_system/`

**Recommendation:** Move system files to `docs/` so they're part of GitHub. They define how the project works and should be shared with any future collaborators. Keep `_system/MEMORY.md` (it's special — it grows and is curated).

---

## 🟡 CLEANUP DECISIONS

### 7. Tao node_modules
**Status:** Should delete
**Question:** Delete `Tao/node_modules/` before migrating?

**Context:** Node dependency cache (not code). Typically excluded from version control.

**Decision needed:**
- [ ] Delete it now
- [ ] Delete it during migration
- [ ] Keep it (unlikely)

**Recommendation:** Delete before migration. Add `node_modules/` to `.gitignore`.

---

### 8. Archive Folder Structure
**Status:** Needs review
**Question:** Should we audit the `archive/` folder and consolidate duplicates, or leave it as-is?

**Current state:**
- `archive/` contains ~38 files
- Subdirectories: `diffs-*`, `root-duplicates-backup-*`, `root-duplicates-retired-*`
- May contain duplicates or outdated versions

**Decision needed:**
- [ ] Audit + consolidate (clean it up)
- [ ] Leave as-is (it's already retired, so complexity is OK)
- [ ] Compress into a single `archive.tar.gz`

**Recommendation:** Leave as-is for now. It's already in archive/, so it's not in the working path. If you need to recover something, it'll be there. Compress to tar later if storage is a concern.

---

### 9. Orphaned Root Files
**Status:** Needs decision
**Question:** These files live at root but belong to projects. Should we move them during migration?

**Files:**
- `GTM_CONVERSION_FUNNEL_SUMMARY.md` → `projects/learn2tape/marketing/`
- `GTM_V26_ECOMMERCE_PAYLOAD_FIX.md` → `projects/learn2tape/marketing/`
- `L2T_PHASE2_VALIDATION_REPORT.md` → `projects/learn2tape/`
- `learn2tape_ads_diagnostic_2026-04-17.md` → `projects/learn2tape/marketing/`

**Decision needed:**
- [ ] Move all to appropriate project folders
- [ ] Keep orphaned at root (easier reference)
- [ ] Move but create symlinks at root (complicated, not recommended)

**Recommendation:** Move them to project folders. They'll be easier to find and won't clutter root.

---

### 10. .claude/settings.local.json + launch.json
**Status:** Clarification needed
**Question:** Should `.claude/` be version-controlled, or should it stay local-only?

**Current state:**
- `.claude/settings.local.json` — local Claude Code configuration (should NOT be version-controlled)
- `.claude/launch.json` — launch configuration (possibly should NOT be version-controlled)

**Decision needed:**
- [ ] Add `.claude/` to `.gitignore` (local-only, not synced to GitHub)
- [ ] Keep `.claude/` in repo but mark as local-only docs
- [ ] Version-control `settings.json` (shared config) but NOT `.local.json`

**Recommendation:** Add to `.gitignore`. These are local developer settings and should never sync to GitHub. Create a `.claude/settings.template.json` if you want to share a template.

---

## 🟢 CLARIFYING QUESTIONS (Low Priority)

### 11. Should Project README files be duplicated in `_projects/`?
**Status:** Optional
**Question:** Currently `_projects/learn2tape.md`, `_projects/tao.md`, etc. exist. Should they stay?

**Recommendation:** During migration, replace `_projects/*.md` with symlinks or Git pointers to `projects/*/README.md`. Or retire `_projects/` entirely once the project structure is clear. This is low priority — can refactor post-migration.

---

### 12. Tao Book Interior Versions
**Status:** Storage question
**Question:** Multiple versions of `tao_interior_*.docx` exist. Keep all, or just the final version?

**Current state:**
- `tao_interior.docx` (original)
- `tao_interior_refined.docx`
- `tao_interior_final.docx` (current)
- `tao_interior_final_Til.docx` (Til Luchau version)
- `tao_interior_final_WLowe.docx` (Whitney Lowe version)

**Decision needed:**
- [ ] Keep all (full version history for reference)
- [ ] Keep final + personalized versions only
- [ ] Keep only current final version

**Recommendation:** Keep all. They're small, and you might want to reference what went to specific reviewers.

---

### 13. Tao Cover Versions
**Status:** Storage question
**Question:** Multiple cover design iterations exist. Keep all PSDs?

**Current state:**
- ~15 variations of cover files (jpg, png, psd, pdf)

**Decision needed:**
- [ ] Keep all (design history)
- [ ] Keep only final versions
- [ ] Archive design iterations

**Recommendation:** Keep all in `projects/tao/book/cover/`. They're part of your design evolution and don't take much space.

---

## NEXT STEP

**Blocked on:** 6 critical decisions (#1-6)

Once you clarify those, the migration can proceed automatically. I'd recommend:
1. **GitHub setup:** Should we create the repo now?
2. **Project scope:** Tao/Learn2Tape separation, Atlas structure
3. **System files:** docs/ vs. _system/ split
4. **Cleanup:** node_modules, orphaned files at root

Indicate your preference on these, and I'll generate the final recommended tree + automated migration steps.
