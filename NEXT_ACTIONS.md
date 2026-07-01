# NEXT ACTIONS — Migration Execution Roadmap

**Date:** June 30, 2026  
**Status:** BLOCKED — Awaiting decisions on unresolved items  
**Scope:** Step-by-step migration plan once approved

---

## PHASE 0: DECISIONS & SETUP (Days 1-2)

### 0.1 Review & Clarify (Estimated time: 30 min)
**Action:** Review three documents:
- [ ] MIGRATION_MAP.md (what moves where)
- [ ] UNRESOLVED_ITEMS.md (decision points)
- [ ] RECOMMENDED_REPOSITORY_TREE.md (target structure)

**Output:** Go/no-go + clarifications on 6 critical decisions

---

### 0.2 Make Decisions (Estimated time: 30 min)
**Action:** Decide on these 6 items from UNRESOLVED_ITEMS.md:

1. **GitHub timing:** Set up repo now or after local migration?
   - [ ] Create GitHub repo first (anthropics/drew-business or similar)
   - [ ] Complete local migration, then push to GitHub as v1.0

2. **Boston Bodyworker:** Archive reference or active project?
   - [ ] Archive (keep for history only)
   - [ ] Keep minimal reference
   - [ ] Activate as separate project

3. **Project Atlas:** Where should it live?
   - [ ] projects/atlas/
   - [ ] research/
   - [ ] Keep as 06_Project_Atlas/

4. **Tao structure:** Single project or split into book + website?
   - [ ] Single projects/tao/
   - [ ] projects/tao/ with clear internal structure (book/, website/)

5. **Marketing:** Global folder or project-specific only?
   - [ ] No global; all inside projects
   - [ ] Create projects/_campaigns/ for cross-project initiatives

6. **System files:** Where should _system/ files live?
   - [ ] Move to docs/ (GitHub-visible)
   - [ ] Keep in _system/ (local-only)

**Output:** Clear decisions on all 6 items

---

### 0.3 Clean Up Pre-Migration (Estimated time: 30 min)
**Actions:**
- [ ] Delete `Tao/node_modules/` (npm cache, not needed)
- [ ] Delete `.tmp/` contents (temporary files)
- [ ] Create `.gitignore` with:
  ```
  node_modules/
  .DS_Store
  .tmp/
  archive/
  .claude/settings.local.json
  .claude/launch.json
  ```
- [ ] Delete orphaned `.DS_Store` files from all folders

**Output:** Clean working directory ready for migration

---

## PHASE 1: LOCAL MIGRATION (Days 2-4)

### 1.1 Create Target Folder Structure (Estimated time: 2 hours)
**Action:** Create empty folder hierarchy matching RECOMMENDED_REPOSITORY_TREE.md

**Script to run:**
```bash
# Create main folders
mkdir -p projects/{sidekick-air,learn2tape,tao,atlas,boston-bodyworker}
mkdir -p docs/memory docs/compliance docs/support
mkdir -p projects/sidekick-air/{product,strategy,platform,ip,logs,partners}
mkdir -p projects/learn2tape/{product,marketing,campaigns/ncb/{data,batches,scripts}}
mkdir -p projects/tao/{book/{cover,proofs,marketing-assets,scripts,assets},website/{elementor,plugins,theme-files,mockups},marketing,ce-program}
mkdir -p projects/atlas/{01-therapeutic-alliance,02-stand-architecture,marketing}
mkdir -p .github/workflows
```

**Verification:** Run `find projects -type d | wc -l` — should show ~40+ folders

---

### 1.2 Move Project Folders (Estimated time: 3 hours)
**Action:** Move each project folder to new structure

**Sidekick Air:**
```bash
# Create README
cp SidekickAir/sidekick_air_master_index.md projects/sidekick-air/README.md

# Move product files
cp SidekickAir/product/* projects/sidekick-air/product/
cp SidekickAir/strategy/* projects/sidekick-air/strategy/
cp SidekickAir/platform/* projects/sidekick-air/platform/
cp SidekickAir/ip/* projects/sidekick-air/ip/
cp SidekickAir/logs/* projects/sidekick-air/logs/

# Move root-level project files
cp SidekickAir/sidekick_air_*.md projects/sidekick-air/
cp SidekickAir/*.pdf projects/sidekick-air/partners/
cp -r "SidekickAir/Sidekick Air - PacMar Business Plan" projects/sidekick-air/partners/pacmar/
```

**Learn2Tape:**
```bash
# Create README
cp Learn2Tape/PROJECT_CONTROL.md projects/learn2tape/README.md

# Move marketing files
cp Learn2Tape/learn2tape_google_ads.md projects/learn2tape/marketing/GOOGLE_ADS.md
cp Learn2Tape/google_ads_7_day_diagnostic.md projects/learn2tape/marketing/DIAGNOSTICS.md
cp Learn2Tape/Brevo_Implementation_Workflow_Claude.md projects/learn2tape/marketing/BREVO_WORKFLOW.md
cp Learn2Tape/woocommerce_product_page_copy.md projects/learn2tape/product/COPY.md

# Move campaign data
cp -r Learn2Tape/NCB_* projects/learn2tape/campaigns/ncb/data/
cp Learn2Tape/NCB_MA_Batch_Day*.csv projects/learn2tape/campaigns/ncb/batches/
cp Learn2Tape/state_splits/* projects/learn2tape/campaigns/ncb/data/by-state/
cp Learn2Tape/*.py projects/learn2tape/campaigns/ncb/scripts/
```

**The Tao:**
```bash
# Create README
cp Tao/PROJECT_CONTROL.md projects/tao/README.md

# Move book files
cp Tao/tao_interior_final* projects/tao/book/
cp Tao/KDP* projects/tao/book/
cp Tao/Tao_Clinical_Touch_Cover* projects/tao/book/cover/
cp Tao/KDP_PRINT_INTERIOR_SPREAD.pdf projects/tao/book/proofs/

# Move website files
cp Tao/TAO_LANDING_PAGE_BUILD_GUIDE.md projects/tao/website/BUILD_GUIDE.md
cp Tao/elementor_* projects/tao/website/elementor/
cp Tao/generate_elementor.py projects/tao/website/elementor/scripts/
cp -r Tao/tao-front-page-plugin* projects/tao/website/plugins/

# Move marketing files
cp Tao/Launch\ Messaging\ Pack.md projects/tao/marketing/MESSAGING.md
cp Tao/Reviewer\ Outreach\ Tracker.md projects/tao/marketing/REVIEWERS.md
cp -r Tao/social_images projects/tao/marketing/social-assets/

# Move book scripts
cp Tao/build_*.js Tao/build_*.jsx Tao/build_*.py projects/tao/book/scripts/
```

**Boston Bodyworker:**
```bash
cp BostonBodyworker/the-boston-bodyworker.md projects/boston-bodyworker/README.md
```

---

### 1.3 Move System Files to docs/ (Estimated time: 1 hour)
**Action:** Move system files from `_system/` to `docs/`

```bash
cp _system/SOUL.md docs/
cp _system/USER.md docs/
cp _system/HEARTBEAT.md docs/
cp _system/RULES.md docs/
cp _system/MEMORY.md docs/memory/
# Keep _system/MEMORY.md as is (or create symlink)

# Move compliance docs
cp 269-cmr-4-continuing-education.pdf docs/compliance/

# Move support docs
cp _support/stitchcore-partners.md docs/support/STITCHCORE_PARTNERS.md
```

---

### 1.4 Move Root-Level Project Files (Estimated time: 30 min)
**Action:** Move orphaned files from root into appropriate projects

```bash
# Learn2Tape GTM files
cp GTM_CONVERSION_FUNNEL_SUMMARY.md projects/learn2tape/marketing/GTM_FUNNEL.md
cp GTM_V26_ECOMMERCE_PAYLOAD_FIX.md projects/learn2tape/marketing/GTM_V26_FIX.md
cp L2T_PHASE2_VALIDATION_REPORT.md projects/learn2tape/PHASE2_VALIDATION.md
cp learn2tape_ads_diagnostic_2026-04-17.md projects/learn2tape/marketing/DIAGNOSTICS_20260417.md
```

---

### 1.5 Rewrite Root README.md (Estimated time: 1 hour)
**Action:** Create new GitHub-native README.md

**Content:**
```markdown
# Finding My Wei — Command Center

Central hub for Drew Freedman's business operations, research, and IP.

**Permanently active projects:**
- **[Sidekick Air / StitchCore](projects/sidekick-air/)** — Portable inflatable therapy table + product platform
- **[Learn2Tape](projects/learn2tape/)** — Online continuing education for massage therapists
- **[The Tao of Clinical Touch](projects/tao/)** — Published book + CE program
- **[Project Atlas](projects/atlas/)** — Clinical research program (therapeutic alliance + architecture)

**Legacy / Reference:**
- **[The Boston Bodyworker](projects/boston-bodyworker/)** — IP estate (inactive)

---

## Quick Links

- **[System & Collaboration](docs/SOUL.md)** — How we work together
- **[Repository Architecture](docs/ARCHITECTURE.md)** — Folder structure + conventions
- **[Project Memory](docs/memory/MEMORY.md)** — Long-term context + decisions
- **[Contributing](docs/CONTRIBUTING.md)** — How to collaborate

---

## Structure

- `docs/` — System documentation, memory, compliance
- `projects/` — Active business projects
- `archive/` — Historical files + backups

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed structure.

---

**Latest update:** [Your date]  
**Source of truth:** GitHub  
**Local working copy:** ~/Desktop/Coding-folder
```

---

### 1.6 Create Supporting Docs (Estimated time: 2 hours)
**Action:** Create key reference documents

**docs/ARCHITECTURE.md:**
```markdown
# Repository Architecture

This repository follows the Finding My Wei operating system structure.

## Core Principles

1. **One project = one folder** — Clear ownership and organization
2. **GitHub is source of truth** — Local Coding-folder is a working copy
3. **Meaningful subfolders** — product/, strategy/, marketing/, website/, etc.
4. **Each project has a README.md** — Acts as entry point
5. **Memory is curated** — docs/memory/ grows over time
6. **Archive is read-only** — Historical reference only

## Folder Glossary

- **docs/** — System + collaboration documentation
  - **memory/** — Long-term project memory (version-controlled)
  - **compliance/** — Regulatory + legal reference
  - **support/** — Research + templates

- **projects/** — Active business projects
  - Each project is self-contained with subfolders
  - product/, strategy/, marketing/, website/, etc.
  - Each has a README.md as entry point

- **archive/** — Historical files + backups
  - Read-only reference
  - Not maintained or updated

## File Naming Conventions

- Project READMEs: `projects/<project>/README.md`
- Decision logs: `DECISION_LOG.md` or `OPEN_DECISIONS.md`
- Specifications: `SPEC.md`, `BRIEF.md`
- Implementation guides: `BUILD_GUIDE.md`, `WORKFLOW.md`
- Strategies: `ROADMAP.md`, `STRATEGY.md`

See individual project README files for specifics.
```

**docs/CONTRIBUTING.md:**
```markdown
# Contributing Guide

This repository contains Drew Freedman's active business projects and IP.

## Before You Start

Read these files in order:
1. [SOUL.md](SOUL.md) — How we collaborate
2. [ARCHITECTURE.md](ARCHITECTURE.md) — Repository structure
3. Project-specific README in `projects/<project>/`

## General Principles

- **Preserve project history** — Don't delete files; archive if retired
- **Meaningful commits** — Describe the WHY, not just the WHAT
- **GitHub is source of truth** — All work flows through GitHub
- **Memory is sacred** — Keep docs/memory/ accurate and curated

## Working on a Project

1. Read the project README (`projects/<project>/README.md`)
2. Check OPEN_DECISIONS.md for current context
3. Check DECISION_LOG.md for historical decisions
4. Make changes on a branch
5. Create PR with summary of changes + WHY

## Contact

Questions? See [USER.md](USER.md) for contact + preferences.
```

---

### 1.7 Verify Migration (Estimated time: 1 hour)
**Action:** Run verification checks

```bash
# Count files before + after
find . -type f -not -path './archive/*' -not -path './.git/*' -not -path '*/.DS_Store' | wc -l

# Check for orphaned files at root (should be mostly gone)
find . -maxdepth 1 -type f -name "*.md" -o -name "*.txt" -o -name "*.csv" -o -name "*.xlsx"

# Verify project structure
find projects -name README.md | sort

# Check for missing critical files
ls docs/SOUL.md docs/USER.md docs/HEARTBEAT.md projects/*/README.md
```

**Output:** Checklist of what moved successfully

---

## PHASE 2: GIT INITIALIZATION (Day 5)

### 2.1 Initialize Git Repository
```bash
cd /Users/Drewdog19/Desktop/Coding-folder
git init
git config user.name "Drew Freedman"
git config user.email "drew@learn2tape.com"
```

---

### 2.2 Create .gitignore
```bash
cat > .gitignore << 'EOF'
# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes

# Local development
.claude/settings.local.json
.claude/launch.json
.claude/*.local.*

# Dependencies
node_modules/
__pycache__/
*.pyc
.venv/
venv/

# Temporary files
.tmp/
*.swp
*.swo
*~

# Archive (keep locally but don't commit)
archive/

# IDE
.vscode/
.idea/
*.swp

# Build outputs
dist/
build/
.next/
EOF
```

---

### 2.3 Initial Commit
```bash
git add -A
git commit -m "Initial commit: Finding My Wei structure v1.0

- Reorganized projects into /projects folder
- Moved system files to /docs for GitHub visibility
- Consolidated Learn2Tape, Sidekick Air, Tao, and Project Atlas
- Established memory system in docs/memory/
- Created project-specific README files as entry points

Structure:
- docs/: System documentation + memory
- projects/: Active business projects (sidekick-air, learn2tape, tao, atlas)
- archive/: Historical reference

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### 2.4 Create GitHub Repository
**Action:** On GitHub (or internal git server)

```bash
# Create repo: anthropics/drew-business (or similar)
# Initialize with empty repo (no README)

# Add remote
git remote add origin https://github.com/anthropics/drew-business.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## PHASE 3: POST-MIGRATION CLEANUP (Day 5-6)

### 3.1 Update References
- [ ] Update `CLAUDE.md` to point to GitHub repo
- [ ] Update `.claude/CLAUDE.md` reference in local settings
- [ ] Update any CI/CD or external systems to use GitHub URLs

### 3.2 Archival of Old Structure
- [ ] Move old `SidekickAir/`, `Learn2Tape/`, `Tao/` folders to archive if migration is complete
- [ ] OR: Keep side-by-side during transition (safe, but adds clutter)

### 3.3 Update Local Memory
- [ ] Add memory file: `migration_completed.md` with date + summary
- [ ] Update `MEMORY.md` index to reflect new structure

---

## ESTIMATED TIMELINE

| Phase | Duration | Status |
|---|---|---|
| Phase 0: Decisions & Setup | 2-3 hours | **BLOCKED** |
| Phase 1: Local Migration | 12-15 hours | Awaiting Phase 0 |
| Phase 2: Git Init + GitHub | 1-2 hours | Awaiting Phase 1 |
| Phase 3: Cleanup | 2-3 hours | Awaiting Phase 2 |
| **TOTAL** | **~20-25 hours** | — |

---

## ROLLBACK PLAN

If something goes wrong:

1. **Before starting Phase 1:** Create full backup
   ```bash
   tar -czf ~/Coding-folder_backup_20260630.tar.gz ~/Desktop/Coding-folder/
   ```

2. **If migration fails:** Restore from backup
   ```bash
   rm -rf ~/Desktop/Coding-folder
   tar -xzf ~/Coding-folder_backup_20260630.tar.gz -C ~/Desktop/
   ```

3. **If GitHub push fails:** Don't panic
   - Delete `.git/` folder
   - Start Phase 2 over
   - Previous local files are safe

---

## RUNNING AUTOMATED MIGRATION

Once decisions are made, I can automate Phases 1-2:

```bash
# I can run this script to execute all moves
bash /path/to/automated_migration.sh
```

This would save 12-15 hours of manual work and eliminate human errors.

---

## NEXT STEP

**You decide:**

1. **Review the three migration documents** (MAP, UNRESOLVED, TREE)
2. **Make decisions** on the 6 critical items in UNRESOLVED_ITEMS.md
3. **Say "Go"** and I'll execute the automated migration

Or: **Pick any item** and we dive deeper before deciding.

Once you're ready, let me know and I'll kick off Phase 0.2 (decisions).

