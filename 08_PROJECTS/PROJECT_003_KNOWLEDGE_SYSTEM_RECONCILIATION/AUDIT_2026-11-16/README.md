---
title: Cross-project preservation audit
status: Recorded
domain: Institutional stewardship
project: PROJECT_003_KNOWLEDGE_SYSTEM_RECONCILIATION
owner: Drew Freedman
created: 2026-11-16
updated: 2026-11-16
tags: [preservation, provenance, institutional-learning]
aliases: []
---

# Cross-project preservation audit — November 16, 2026

**Finding:** substantial standards and production evidence exist, but portfolio-wide completeness is not established. Discovery, current authority, release evidence and demonstrated learning are uneven. Do not certify the estate as fully reconciled.

**Scope:** recent work from October 1–November 16, with older records consulted for authority. Repository baseline: [`64720b81a422e9e0fc3d0bceeded1347d3907538`](https://github.com/learn2tape19/finding-my-wei/tree/64720b81a422e9e0fc3d0bceeded1347d3907538). This audit is evidence and a proposed implementation, not a constitutional amendment or authorization to publish, spend or deploy.

## What was inspected

- Current remote `main`, its 1,056 tracked paths, recent commit history, and 22 remote branch tips (excluding the symbolic origin/HEAD alias).
- Branch ancestry and complete path/blob inventories, with deeper content inspection of the two recent Tao branches below.
- Constitutional precedence, decision/promotion standards, production playbook, current operating state, legacy indexes, project records and selected receipts/runbooks.
- GitHub pull-request collection and recently updated issue records, including [AREA follow-through #8](https://github.com/learn2tape19/finding-my-wei/issues/8) and [staging recovery #9](https://github.com/learn2tape19/finding-my-wei/issues/9).

Path inventory is comprehensive at those tips; content review is selective. Historical deleted commits, every binary, every conversation, every external account and every backup were not exhaustively audited. No secret scan, rights certification, legal/IP status audit, live production audit or disaster-recovery test is claimed.

## Evidence language

**Verified repository fact:** directly read from the stated Git revision or GitHub endpoint. **Recorded historical claim:** a receipt says a check happened; that is not a fresh check of the external system. **Recovered local evidence:** bytes/records were inspected outside GitHub; remote preservation remains a separate question. **Unverified:** insufficient evidence, inaccessible source or unperformed check. Missing here means not located within the stated search scope, not proof the work never happened.

## Coverage and gaps

| Area | Verified repository evidence | Gap and next action |
| --- | --- | --- |
| AREA Salon Studios | [Front door](../../../foundry/AREA_SALON_STUDIOS/README.md), [Nov 13 review](../../../foundry/AREA_SALON_STUDIOS/REVIEW_2026-11-13.md), [content index](../../../foundry/AREA_SALON_STUDIOS/CONTENT_INDEX.md), release and preservation receipts are on main. The review distinguishes source records, checked packages and publication claims. | Protected source links are locators, not independent backups. Current/native publication, exact approval-to-export matching, native Story additions and measured HQ outcomes remain open in that review. Reconcile existing objects; do not recreate them from a calendar. |
| Learn2Tape | [Oct 8 decision/measurement record](../../../05_DOMAINS/EDUCATION_DOMAIN/LEARN2TAPE_2026-10-08_DECISION_AND_MEASUREMENT_RECORD.md) distinguishes reported work from independent inspection and holds Ads restart for explicit authorization. | Later website, policy and measurement work needs a dated successor record with exact page/product versions, approvals, release/rollback evidence and commercial results. An old paused-Ads instruction cannot establish today's ad state. Reconcile actual records before updating current authority. |
| Tao Issue 016 | [Issue front door](../../../07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_016/README.md), approved originals, QA/manifests, scheduling and remote preservation receipts exist on main. The Oct 12 closeout explicitly separates production closure from future delivery. | Scheduled is not delivered. Fresh post/send status, native identifiers/permalinks and comparable-age results/retrospective are not established by the scheduling receipt. Keep production closure intact; append delivery evidence separately. |
| Tao later editorial work | [Second Reading/resend branch](https://github.com/learn2tape19/finding-my-wei/tree/ee4093c1e6a7f96e5deee970e09b2089a4606751/07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE) preserves decisions, approvals, source inventories and later execution receipts. | At the audited tips this branch has 39 commits absent from main, while main has 12 absent from it. The October 20 resend README changes the earlier opening; read the later dated execution receipts too. Preserve and reconcile selectively; do not merge all branch content or reactivate superseded Issue 017 plans by assumption. |
| Tao book-sales campaign | [Discovery branch](https://github.com/learn2tape19/finding-my-wei/tree/8866359f3a20245f416e8f1050a69932a10d1d18/07_MARKETING/CAMPAIGNS/TAO_BOOK_SALES_001) preserves strategy, pivot, selection, source and rights records. | Six branch commits are absent from main; 12 main commits are absent from it. The branch's October 22 state cannot certify later approval, release or current campaign state. Reconcile later masters, exact approval, usage rights, release and results with protected sources. |
| Sidekick Air / StitchCore | [Operating state](../../../OPERATING_STATE.md) identifies this as primary active innovation work. Engineering definition, assumptions, V&V/risk documents, [advisors](../../STITCHCORE/ADVISORS.md) and September decisions exist. | No Oct 1–Nov 16 commits were found under `08_PROJECTS/STITCHCORE` or the `project_atlas_02_stand_architecture` product-definition subtree at any inspected branch tip. Later partner/engineering work needs a protected source register and decision-to-drawing-to-test trace. This path-scoped finding does not exclude differently located records. June specifications and a September unresolved load-claim record cannot certify present fabrication readiness. |
| Boston Bodyworker | [Project track](../../../BostonBodyworker/the-boston-bodyworker.md) and later [operating state](../../../OPERATING_STATE.md) recognize closure/preservation. | The [June preservation plan](../../../05_DOMAINS/PUBLISHING_DOMAIN/BOSTON_BODYWORKER_PRESERVATION_PLAN.md) and knowledge map still describe active publishing. No tracked `05_DOMAINS/PUBLISHING_DOMAIN/WEBSITE/` export tree was found on main. Locate any private backups, inventory URLs/media and prove recoverability before claiming archival completeness. Do not reactivate monthly publishing work. |

## Governance and learning findings

1. **Existing doctrine is sufficient for the core job.** [Canonical precedence](../../../00_Constitution/CANONICAL_PRECEDENCE.md), [decision standard](../../../00_Constitution/DECISION_RECORD_STANDARD.md), [promotion rule](../../../00_Constitution/INSTITUTIONAL_PROMOTION_RULE.md) and the [production playbook](../../../01_OPERATING_SYSTEM/PRODUCTION_PLAYBOOK.md) already require intent, evidence, preservation and approved promotion. Add an operational capture loop, not another constitution.
2. **Navigation can overstate freshness.** `DECISION_INDEX.md` and `ASSET_INDEX.md` identify June 25 as their last update and include dated price, tracking and role claims. They are historical summaries, not live verification. This change adds explicit navigation notices without rewriting their original entries.
3. **A proposal is not ratified authority.** `foundry/governance/adr/ADR-002_INSTITUTIONAL_PRESERVATION_REQUIREMENT.md` ends as Proposed/Awaiting Founder Approval despite mandatory language in its body. Use later canonical preservation requirements; do not infer ratification from forceful wording.
4. **Learning exists but is uneven.** Issue 016's October 12 decision and playbook update demonstrate actual integration of lessons. AREA's November 13 review inherits that lesson. The engineering `LESSONS_LEARNED.md` still contains an unfinished June Sprint 001 and placeholders. Do not count a template as a completed retrospective or an engineering target as a test result.
5. **Current authority can lag exceptions.** The campaign authority register describes default feed dimensions, while Issue 016 records an approved 1080×1380 exception. Future checks must read issue-specific approvals rather than normalize/regenerate approved work.
6. **Technical enforcement is limited.** The GitHub branch endpoint reported main `protected: false`; no `.github/` paths were present in the baseline tree. This does not prove absence of all account-level controls. Protection/required-review changes are proposals only and were not applied.
7. **Public storage is a real boundary.** GitHub reports this repository public. Some existing records contain personal or business-sensitive narrative. Review access and historical exposure separately with Drew; this patch does not reproduce those details or alter visibility/history. Private correspondence, customer/order rows, engineering originals and credentials belong in protected storage with safe reference records.

## Recommended order

1. Recover recent Sidekick and Learn2Tape evidence into a protected register; prepare source-linked successor records before the next material decision.
2. Reconcile the Tao branches and later packages with main, preserving all history and explicitly identifying supersession and release scope.
3. Complete AREA and Tao delivery/outcome reconciliation at the next consequential reporting/reuse point.
4. Locate Boston Bodyworker exports/backups and run one bounded restoration check; retire obsolete active-work instructions through explicit lineage.
5. Review root indexes and public/private storage exposure. Consider branch protection only after deciding the desired review process.

Each item is tracked in [BACKLOG.json](BACKLOG.json) with a closure test. Suggested responsibility is not an assigned commitment or invented due date.

## Implementation in this change

This folder provides a [proposed capture/review workflow](WORKFLOW.md), [reusable record](RECORD_TEMPLATE.md), seeded backlog and a structural validator. Parent navigation and historical-index notices make it discoverable. Existing campaigns, standards, source files and approvals remain intact. No automatic schedule or institutional promotion is created. The workflow becomes adopted policy only through the approval required by existing governance.

**Audit status:** findings recorded; reconciliation HOLD. **Workflow:** proposed, exercised on this audit. **Live systems:** not modified. **Founder acceptance:** pending review, distinct from whether this change has been preserved on a remote branch.
