# Physical Cleanup Pass — September 29, 2026

## Status
Executed on `reconciliation-2026-09-29` only.

---

# Purpose

The earlier reconciliation passes established canonical successors and archive manifests. This pass begins removing clearly superseded live files so the repository becomes physically simpler, not merely better documented.

Exact deleted content remains recoverable from Git history and `archive/pre-reconciliation-2026-09-29`.

---

# Removed: parallel constitutional root

Deleted all four files from `00_CONSTITUTION/` after their disposition was established:

- `ARCH-002_IMPLEMENTATION_SPEC.md`
- `ARCH-002_WORK_ORDER.md`
- `MASTER_REPOSITORY_MAP.md`
- `REPOSITORY_ARCHITECTURE.md`

Canonical constitutional authority remains in `00_Constitution/`.

Durable repository-architecture doctrine now lives in:

`01_OPERATING_SYSTEM/STANDARDS/REPOSITORY_ARCHITECTURE.md`

Because Git does not preserve empty directories, `00_CONSTITUTION/` now disappears from the branch.

---

# Removed: legacy project status layer

Deleted the four already-reconciled `_projects/` snapshots:

- `tao.md`
- `sidekick-air.md`
- `learn2tape.md`
- `boston-bodyworker.md`

Their disposition and historical meaning remain documented in:

`archive/LEGACY_PROJECT_TRACKS_2026-03/README.md`

The `_projects/` directory therefore disappears from the branch.

---

# Removed: legacy support layer

Deleted:

- `_support/NOTION_SYNC_MAP.md`
- `_support/stitchcore-partners.md`

Their disposition remains documented in:

`archive/LEGACY_SUPPORT_2026-03/README.md`

The `_support/` directory therefore disappears from the branch.

---

# Removed: clearly retired `_system` machinery

Deleted the files already classified as RETIRE rather than historically valuable operating doctrine:

- `HEARTBEAT.md`
- `INDEX.md`
- `MASTER_CONTROL.md`
- `PROJECTS_MAP.md`
- `SYNC_TODAY_TO_NOTION.md`
- `TODAY.md`
- `WEEKLY_REVIEW.md`

Historical/disposition record:

`archive/LEGACY_SYSTEM_2026-03/README.md`

The remaining `_system/` files are intentionally held for a second physical pass because they contain richer historical AI/collaboration or Sidekick-specific material and should not be deleted merely to empty the directory.

---

# Removed: superseded `03_OPERATING_SYSTEM/STANDARDS`

Deleted the five standards whose durable doctrine has already been promoted/re-homed:

- `GOVERNANCE_PRINCIPLE.md`
- `KNOWLEDGE_LIFECYCLE.md`
- `KNOWLEDGE_PRODUCTION_PIPELINE.md`
- `PUBLICATION_SUCCESS_CRITERIA.md`
- `TAO_VISUAL_IDENTITY_SYSTEM_v1.0.md`

Canonical successors exist in `01_OPERATING_SYSTEM/STANDARDS/` and the Tao domain.

The `03_OPERATING_SYSTEM/BRAND_ASSETS/CHAPTER_SYMBOLS/` tree remains untouched because it contains the actual Tao SVG symbol assets. Those assets require a controlled move/copy rather than deletion.

---

# Result

This pass removes three complete obsolete live surfaces:

- `00_CONSTITUTION/`
- `_projects/`
- `_support/`

and materially shrinks two more:

- `_system/`
- `03_OPERATING_SYSTEM/`

No active Issue production files were modified.
