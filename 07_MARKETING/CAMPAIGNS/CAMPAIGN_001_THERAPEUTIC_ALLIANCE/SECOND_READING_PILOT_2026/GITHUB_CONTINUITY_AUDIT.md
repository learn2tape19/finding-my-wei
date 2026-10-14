# GitHub continuity audit — October 14, 2026

## Repository state before continuity changes

Canonical remote: `https://github.com/learn2tape19/finding-my-wei.git`. Local checkout is an isolated clone in the Tao workspace, directory `finding-my-wei-review`.

Branch: `codex/tao-second-reading-pilot`. Initial review commit: `3bd062e3e61c25be022cf192468e845e5ca3931b`. Base and refreshed `origin/main`: `273535f9e6e45879c225048aa3177247df4e871d`. Fetch completed October 14; branch initially 0 commits behind and 1 ahead. Working tree was clean. Initial diff contains only 42 added files under this pilot directory. No original issue, asset, URL or existing standard was changed by that commit.

## Existing architecture to inherit

| Existing authority | Responsibility | Pilot relationship |
|---|---|---|
| `00_Constitution/DECISION_RECORD_STANDARD.md` and `DECISIONS/` | Authority, rationale, supersession, review trigger | Founder’s continuity requirement recorded there; pilot proposals remain proposals |
| `01_OPERATING_SYSTEM/PRODUCTION_PLAYBOOK.md` | Stages A–E, direction, production, primary publication, distribution, reconciliation | Governs this package unchanged |
| `01_OPERATING_SYSTEM/PUBLISHING/EDITORIAL_WORKFLOW.md` | Scientific review → distinct editorial review → Founder → preservation → publication → reflection | No review is waived or represented as complete |
| Campaign `ARCHITECTURE.md` | Single canonical article source, production derivatives | Original BLOG sources stay authoritative; no duplicate original manuscripts introduced as authority |
| Campaign `CURRENT_AUTHORITY_REGISTER.md` | Current rules and explicit issue exceptions | General 1080×1350 Feed applies unless approved otherwise; Issue 016 overrides remain bounded |
| `07_MARKETING/STANDARDS/CANONICAL_PUBLICATION_WORKFLOW.md` | Source/extraction/creative/deployment phases and Phase 7A | Existing completeness gate retained; CSV planning checks do not satisfy it |
| `07_MARKETING/STANDARDS/verify_production_completeness.py` | Deterministic asset/sequence/hash/Git/remote checks | Current five-day assumptions need a bounded compatibility review if reduced cadence is approved |
| `04_CAPABILITIES/PUBLISHING/TAO_PUBLISHING_EXECUTION_DOCTRINE.md` and `control_plane/` | WordPress REST; public media byte equality; Buffer GraphQL; Brevo; independent readback | Execution remains inside this system; no new scheduler, adapter or platform writes |
| Campaign `PUBLICATION_INDEX.md` | Evidence-based lifecycle ledger | Historical rows unchanged; add pilot navigation with unapproved status only |

Paths above are repository-relative.

## Gaps and disposition

1. **Local-only preservation:** original pilot commit had not reached GitHub. Founder now authorizes branch push after review. Remote ref equality and fresh retrieval are required before claiming remote preservation.
2. **Unrecorded continuity decision:** resolved with `DR-2026-10-14-TAO-SECOND-READING-GITHUB-CONTINUITY`. It approves continuity and reviewed branch push only.
3. **Apparent parallel gates:** the plan’s numbered gate table is a campaign checklist, subordinate to existing standards. This audit explicitly maps it; no new approval authority exists.
4. **Reduced cadence vs checker:** three feed days and one Monday Story sequence differ from current Monday–Friday expectations. Reduced cadence remains PENDING Founder approval. Do not weaken or bypass Phase 7A; after direction approval, declare the expected role counts in existing manifest form and adapt the existing checker narrowly if needed. No checker change or production-complete claim in this task.
5. **New reflection source vs canonical article:** `PILOT_COPY.md` is the working source for unapproved email/social reflections, not a replacement original article. `emails/` are assembled derivative review exports. Edits must originate in the working source and be reconciled into exports. Any new standalone WordPress reflection would require its own approved canonical BLOG source and is outside the present proposal.
6. **Draft asset CSV vs production manifest:** 36 masters are planned only. The CSV has no actual approved image hashes or approvals and cannot close the production gate. Approved originals must use the existing manifest/persistence chain before execution.
7. **Approvals and verification:** scientific, editorial, direction, copy, visuals, audience and release remain pending. Signed-in page checks are not anonymous HTTP proof; reporting transcriptions are not provider exports; GA4 attribution is incomplete. Those limits remain explicit.
8. **Discovery/index continuity:** link this area from existing publication/decision records as DRAFT, without updating original publication states or promoting pilot hypotheses into standards.
9. **Original commit naming:** the first draft commit did not use the legacy index’s bracketed category convention. Preserve its SHA/history; continuity follow-up uses `[Tao]`. Do not rewrite history simply to make an old commit fit a style convention.

## Platform dependency mapping

GitHub approved source → existing WordPress original-article/approved-media verification → Buffer distribution objects → Brevo approved email/audience → GA4 and provider reporting → GitHub evidence/retrospective. Buffer and Brevo are distribution branches using WordPress media, not a literal dependency in which email must consume Buffer output.

No new WordPress article is proposed. The existing article remains the primary publication dependency. Its preserved ID, canonical URL and media must pass the existing Stage C checks before downstream release. That does not authorize edits to the original. GA4 definitions remain campaign measurement proposals; no analytics settings or tags are changed.

## Status

Audit and documentation only. Reviewed branch push is authorized; merge and all public/external release actions are not. Commit, scan and remote readback evidence are recorded separately in `evidence/CONTINUITY_VERIFICATION.json`. No production execution has occurred, so production verification remains NOT PERFORMED rather than PASS.
