# MIGRATION MAP — Coding-folder → Finding My Wei Structure

**Date:** June 30, 2026  
**Status:** DRAFT — Awaiting Drew review before execution  
**Scope:** Map all existing files/folders to Finding My Wei OS + GitHub-native structure

---

## SYSTEM FILES (_system/ → docs/)

These govern the operating system and should eventually move to docs/ for GitHub accessibility.

| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `_system/SOUL.md` | `docs/SOUL.md` | System | Keep | Assistant collaboration style — make GitHub-accessible |
| `_system/USER.md` | `docs/USER.md` | System | Keep | Drew preferences + constraints — reference in README |
| `_system/HEARTBEAT.md` | `docs/HEARTBEAT.md` | System | Keep | Daily brief automation rules |
| `_system/RULES.md` | `docs/RULES.md` | System | Keep | Repository operating principles |
| `_system/INDEX.md` | Deprecate | System | Archive | Redundant with MEMORY.md + README |
| `_system/MEMORY.md` | `docs/memory/MEMORY.md` | System | Keep | Long-term project + user memory (this grows in place) |
| `_system/MASTER_CONTROL.md` | `docs/ARCHITECTURE.md` | System | Refactor | Consolidate with project structure docs |
| `_system/PROJECTS_MAP.md` | Regenerate | System | Replace | Auto-generated from repo structure; remove manually-maintained version |
| `_system/OPENCLAW_LAUNCHER.md` | `.openclaw/workspace/README.md` | System | Move | OpenClaw-specific; lives outside repo |
| `_system/SYNC_TODAY_TO_NOTION.md` | Archive | Compliance | Archive | Historical; Notion sync frozen per README |
| `_system/TODAY.md` | Archive | Compliance | Archive | Daily status; ephemeral — not version-controlled |
| `_system/WEEKLY_PROJECT_BALANCE.md` | Archive | Compliance | Archive | Weekly summary; keep as historical record |
| `_system/WEEKLY_REVIEW.md` | Archive | Compliance | Archive | Weekly summary template |
| `_system/CLAUDE_WELCOME.md` | Archive | Support | Archive | Onboarding; superseded by docs/ structure |
| `_system/sidekick-agent-guide.md` | `docs/sidekick-agent-guide.md` | Support | Keep | Claude's operating charter for this project |
| `_system/sidekick-agent-soul.md` | Merge into SOUL.md | Support | Consolidate | Duplicate/specialized version of SOUL.md |

---

## PROJECT FILES (Active Projects → projects/)

### Sidekick Air / StitchCore
| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `SidekickAir/sidekick_air_master_index.md` | `projects/sidekick-air/README.md` | Active | Reorganize | Project hub — becomes the entry point |
| `SidekickAir/product/sidekick_air_project_master_brief.md` | `projects/sidekick-air/product/BRIEF.md` | Active | Keep | Core product spec |
| `SidekickAir/product/sidekick_air_technical_specs.md` | `projects/sidekick-air/product/SPECS.md` | Active | Keep | Engineering requirements |
| `SidekickAir/strategy/sidekick_air_roadmap.md` | `projects/sidekick-air/strategy/ROADMAP.md` | Active | Keep | Product roadmap |
| `SidekickAir/strategy/sidekick_air_category_creation.md` | `projects/sidekick-air/strategy/CATEGORY.md` | Active | Keep | Market positioning |
| `SidekickAir/strategy/sidekick_air_validation_milestones.md` | `projects/sidekick-air/strategy/MILESTONES.md` | Active | Keep | Validation gates |
| `SidekickAir/strategy/stitchcore_product_family_roadmap.md` | `projects/sidekick-air/strategy/STITCHCORE_ROADMAP.md` | Active | Keep | Platform-level roadmap |
| `SidekickAir/platform/stitchcore_platform_definition.md` | `projects/sidekick-air/platform/DEFINITION.md` | Active | Keep | Platform charter |
| `SidekickAir/platform/aerostitch_core_technology_definition.md` | `projects/sidekick-air/platform/AEROSTITCH.md` | Active | Keep | Core tech spec |
| `SidekickAir/ip/sidekick_air_ip_architecture.md` | `projects/sidekick-air/ip/ARCHITECTURE.md` | Active | Keep | IP strategy + patent tracking |
| `SidekickAir/logs/founder_log.md` | `projects/sidekick-air/logs/FOUNDER_LOG.md` | Active | Keep | Founder decision record |
| `SidekickAir/logs/sidekick_air_decision_log.md` | `projects/sidekick-air/logs/DECISION_LOG.md` | Active | Keep | Technical decisions |
| `SidekickAir/sidekick_air_manufacturing_brief.md` | `projects/sidekick-air/MANUFACTURING.md` | Active | Keep | Manufacturer coordination |
| `SidekickAir/sidekick_air_war_map.md` | `projects/sidekick-air/WAR_MAP.md` | Active | Keep | Competitive landscape + strategy |
| `SidekickAir/sidekick_air_open_decisions.md` | `projects/sidekick-air/OPEN_DECISIONS.md` | Active | Keep | Unresolved issues |
| `SidekickAir/sidekick_air_ai_system_setup.md` | `projects/sidekick-air/AI_SETUP.md` | Support | Keep | AI assistant configuration |
| `SidekickAir/project_context.yaml` | `projects/sidekick-air/context.yaml` | Support | Keep | Project metadata |
| `SidekickAir/Sidekick Air - PacMar Business Plan/*` | `projects/sidekick-air/partners/pacmar/` | Active | Reorganize | Partner submission packet |
| `SidekickAir/*.pdf` (partner overviews) | `projects/sidekick-air/partners/` | Research | Keep | Supplier research |

### Learn2Tape
| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `Learn2Tape/PROJECT_CONTROL.md` | `projects/learn2tape/README.md` | Active | Reorganize | Project hub |
| `Learn2Tape/learn2tape_google_ads.md` | `projects/learn2tape/marketing/GOOGLE_ADS.md` | Active | Keep | Ad strategy + performance |
| `Learn2Tape/google_ads_7_day_diagnostic.md` | `projects/learn2tape/marketing/DIAGNOSTICS.md` | Active | Keep | Performance analysis |
| `Learn2Tape/Brevo_Implementation_Workflow_Claude.md` | `projects/learn2tape/marketing/BREVO_WORKFLOW.md` | Support | Keep | Email infrastructure setup |
| `Learn2Tape/Google Ads Performance Manager – Learn2Tape.md` | Archive | Support | Archive | Likely superseded or historical |
| `Learn2Tape/woocommerce_product_page_copy.md` | `projects/learn2tape/product/COPY.md` | Active | Keep | Product page content |
| `Learn2Tape/NCB_LIST_*.{csv,xlsx,zip}` | `projects/learn2tape/campaigns/ncb/data/` | Active | Keep | Email list + segmentation |
| `Learn2Tape/NCB_MA_Batch_Day*.csv` | `projects/learn2tape/campaigns/ncb/batches/` | Active | Keep | Campaign wave structure |
| `Learn2Tape/NCB_PHASE1_UNZIPPED/*` | `projects/learn2tape/campaigns/ncb/data/zerobounce-results/` | Active | Keep | List validation results |
| `Learn2Tape/NCB_LIST_CLEANING_WORKFLOW.md` | `projects/learn2tape/campaigns/ncb/WORKFLOW.md` | Active | Keep | Data cleaning process |
| `Learn2Tape/state_splits/*.csv` | `projects/learn2tape/campaigns/ncb/data/by-state/` | Active | Keep | Geographic segmentation |
| `Learn2Tape/brevo_import_lists.py` | `projects/learn2tape/campaigns/ncb/scripts/` | Support | Keep | Automation script |
| `Learn2Tape/split_by_state.py` | `projects/learn2tape/campaigns/ncb/scripts/` | Support | Keep | Segmentation script |

### The Tao of Clinical Touch
| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `Tao/PROJECT_CONTROL.md` | `projects/tao/README.md` | Active | Reorganize | Project hub |
| `Tao/tao_interior_final.docx` | `projects/tao/book/MANUSCRIPT.docx` | Active | Keep | Final approved manuscript |
| `Tao/tao_interior_final.pdf` | `projects/tao/book/MANUSCRIPT.pdf` | Active | Keep | PDF proof |
| `Tao/KDP Launch & Publishing Record.txt` | `projects/tao/book/KDP_RECORD.txt` | Active | Keep | Publication log |
| `Tao/KDP_PRINT_INTERIOR_SPREAD.pdf` | `projects/tao/book/PROOFS/` | Active | Keep | Print specification |
| `Tao/Tao_Clinical_Touch_Cover_*.{jpg,png,psd,pdf}` | `projects/tao/book/cover/` | Active | Keep | Cover design files |
| `Tao/Tao_QR_Codes.docx` | `projects/tao/book/MARKETING_ASSETS/` | Active | Keep | Embedded QR codes |
| `Tao/Launch Messaging Pack.md` | `projects/tao/marketing/MESSAGING.md` | Active | Keep | Launch communication strategy |
| `Tao/TAO_LANDING_PAGE_BUILD_GUIDE.md` | `projects/tao/website/BUILD_GUIDE.md` | Active | Keep | Landing page spec |
| `Tao/Reviewer Outreach Tracker.md` | `projects/tao/marketing/REVIEWERS.md` | Active | Keep | Review acquisition process |
| `Tao/Social Media Launch System.md` | `projects/tao/marketing/SOCIAL.md` | Active | Keep | Social strategy |
| `Tao/tao_metadata_package.md` | `projects/tao/book/METADATA.md` | Active | Keep | ISBN + retail metadata |
| `Tao/tao_project_log.md` | `projects/tao/DECISION_LOG.md` | Active | Keep | Historical decisions |
| `Tao/tao_phase1_decision_note.md` | Archive | Support | Archive | Historical phase decision |
| `Tao/tao_site_conversion_upgrade.md` | `projects/tao/website/CONVERSION_SPEC.md` | Support | Keep | Analytics + funnel spec |
| `Tao/tao_visual_environment_upgrade.md` | `projects/tao/website/DESIGN_SPEC.md` | Support | Keep | Visual direction |
| `Tao/tao_final_lock.md` | Archive | Support | Archive | Historical lock note |
| `Tao/tao_hero_alignment_final.md` | Archive | Support | Archive | Historical design iteration |
| `Tao/tao_kdp_readiness.md` | Archive | Support | Archive | Pre-launch checklist (completed) |
| `Tao/elementor_*.{json,md,py}` | `projects/tao/website/elementor/` | Support | Keep | Page builder configuration |
| `Tao/generate_elementor.py` | `projects/tao/website/elementor/scripts/` | Support | Keep | Automation script |
| `Tao/push_elementor.py` | `projects/tao/website/elementor/scripts/` | Support | Keep | Deployment script |
| `Tao/tao-front-page-plugin/` | `projects/tao/website/plugins/` | Support | Keep | Custom WordPress plugin |
| `Tao/build_*.{js,jsx,py}` | `projects/tao/book/scripts/` | Support | Keep | Build automation |
| `Tao/front-page.{php,txt,zip}` | `projects/tao/website/theme-files/` | Support | Keep | Theme customization |
| `Tao/tao_symbols_v2_fixed/` | `projects/tao/book/assets/symbols/` | Support | Keep | Symbol library |
| `Tao/social_images/` | `projects/tao/marketing/social-assets/` | Marketing | Keep | Social media graphics |
| `Tao/Book Review Posts and images/` | `projects/tao/marketing/reviewer-assets/` | Marketing | Keep | Reviewer package materials |
| `Tao/node_modules/` | Delete | Support | Clean | Dependency cache — not version-controlled |
| `Tao/*.ics` (calendar) | Archive | Support | Archive | Historical calendar/schedule |

### Project Atlas (Finding My Wei Research)
| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| Empty placeholder | `projects/atlas/README.md` | Research | Create | Therapeutic alliance research + publication roadmap |
| (Empty) | `projects/atlas/01-therapeutic-alliance/` | Research | Create | Paper 1 + supporting materials |
| (Empty) | `projects/atlas/02-stand-architecture/` | Research | Create | Paper 2 + supporting materials |
| `07_MARKETING/tracking/` | `projects/atlas/marketing/` | Marketing | Migrate | Atlas campaign infrastructure |

---

## ROOT-LEVEL FILES → projects/ or docs/

| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `README.md` | Rewrite as `README.md` | System | Refactor | Consolidate into GitHub-native format; link to docs/ |
| `GTM_CONVERSION_FUNNEL_SUMMARY.md` | `projects/learn2tape/marketing/GTM_FUNNEL.md` | Active | Move | Learn2Tape tracking configuration |
| `GTM_V26_ECOMMERCE_PAYLOAD_FIX.md` | `projects/learn2tape/marketing/GTM_V26_FIX.md` | Active | Move | Historical fix record |
| `L2T_PHASE2_VALIDATION_REPORT.md` | `projects/learn2tape/PHASE2_VALIDATION.md` | Support | Move | Phase completion report |
| `learn2tape_ads_diagnostic_2026-04-17.md` | `projects/learn2tape/marketing/DIAGNOSTICS_20260417.md` | Support | Move | Historical diagnostic |
| `269-cmr-4-continuing-education.pdf` | `docs/compliance/269-CMR-4.pdf` | Compliance | Move | MA continuing ed regulations — reference document |

---

## LEGACY / ARCHIVE FILES

| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `BostonBodyworker/the-boston-bodyworker.md` | `projects/boston-bodyworker/README.md` | Legacy | Keep | IP estate; not active but preserve history |
| `archive/*` | Keep in place | Archive | Keep | Historical records + backups — do not migrate |
| `.claude/settings.local.json` | Keep in place | System | Keep | Local Claude Code configuration |
| `.claude/launch.json` | Keep in place | System | Keep | Claude launch configuration |
| `.DS_Store` | Delete | System | Clean | macOS metadata — add to .gitignore |
| `.tmp/*` | Delete | System | Clean | Temporary files — do not version-control |

---

## SUPPORT FOLDER

| Current Path | Recommended Destination | Classification | Status | Notes |
|---|---|---|---|---|
| `_support/stitchcore-partners.md` | `docs/support/STITCHCORE_PARTNERS.md` | Research | Keep | Partner research + evaluation |
| `_support/NOTION_SYNC_MAP.md` | `.openclaw/README.md` | Support | Move | OpenClaw-specific configuration |

---

## SUMMARY

**Total items to migrate:** ~150+ files/folders

**By category:**
- **Keep in place:** 80+ files (projects that are organized well)
- **Reorganize:** ~40 files (restructure into projects/ hierarchy)
- **Archive:** ~20 files (move to archive/ as historical)
- **Delete:** ~10 files (temp files, caches, OS metadata)
- **Create new:** 4-5 project README files + docs structure

**Major changes:**
1. Create `projects/` folder with subfolders for each active project
2. Create `docs/` folder for system + reference docs (GitHub-native)
3. Consolidate root-level orphaned files into appropriate projects
4. Move system files to docs/ for GitHub accessibility
5. Migrate Project Atlas placeholder structure
6. Clean up caches (.DS_Store, node_modules, .tmp)

**Not changing:**
- `archive/` — keep as-is for historical reference
- `.claude/` — local settings, not version-controlled to GitHub
- Individual project tracking files in `_projects/` — can refactor post-migration
