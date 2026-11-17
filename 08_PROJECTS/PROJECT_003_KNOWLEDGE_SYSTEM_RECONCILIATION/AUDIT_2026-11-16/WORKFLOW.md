---
title: Proposed evidence-to-learning workflow
status: Draft
domain: Institutional stewardship
project: PROJECT_003_KNOWLEDGE_SYSTEM_RECONCILIATION
owner: Drew Freedman
created: 2026-11-16
updated: 2026-11-16
tags: [preservation, provenance, institutional-learning]
aliases: []
---

# Evidence-to-learning workflow

**Status:** Proposed cross-project implementation for Founder review. Applies existing doctrine; does not supersede it. No new recurring automation, standing administrative obligation or publication authority is established.

Authority: [Production Playbook](../../../01_OPERATING_SYSTEM/PRODUCTION_PLAYBOOK.md), [Decision Record Standard](../../../00_Constitution/DECISION_RECORD_STANDARD.md), [Knowledge Lifecycle](../../../01_OPERATING_SYSTEM/STANDARDS/KNOWLEDGE_LIFECYCLE.md), [Institutional Promotion Rule](../../../00_Constitution/INSTITUTIONAL_PROMOTION_RULE.md), and [Operating State](../../../OPERATING_STATE.md).

## 1. Capture at the meaningful event

The executing collaborator captures a record when a decision, deliverable, deployment, failure, material external response or measurable result changes the work. Use the [record template](RECORD_TEMPLATE.md) inside the existing project/campaign home. Link existing records instead of duplicating entire packages. Do not invent a new project tree for each chat.

Preserve event date separately from capture date. Give the event a stable ID and record source system/object ID, exact version, evidence class, uncertainty and relevant approval scope. A conversation is a source; it does not automatically become an approved decision.

For assets, preserve original/editable source, approved export, SHA-256, format/dimensions/runtime, copy/CTA, rights scope, derivative relationship and storage/recovery reference. A preview link or a source provider ID does not prove a backup. When bytes are unavailable, record metadata-only rather than inventing a hash.

## 2. Route the record to the right storage

Public GitHub: safe summaries, decision rationale approved for disclosure, manifests without private data, stable references and provenance. Protected storage: correspondence, drawings, contracts, customer/order data, licensed source material, unpublished sensitive drafts and recovery packages. Secrets: dedicated credential store only; never in either report or public Git history.

A protected source reference must specify authorized owner/access route, provider ID or path, version/hash where available, backup reference and last successful recovery check. Keep private locators in the protected register when even a filename or ID reveals sensitive information. Public records can state “protected evidence retained; access via Founder” with a stable nonsensitive record ID.

If storage is unavailable, preserve the local recovery package and mark remote preservation HOLD. Do not replace a durable source with a temporary download URL.

## 3. Keep independent states

Track these separately: production, approval, rights, release authorization, deployment/delivery, repository preservation and outcome verification. Approval of a draft does not authorize release. A commit does not prove delivery. Scheduling does not prove publication. A provider's payment record does not prove analytics attribution. Unknown is not zero.

Use the existing evidence classes: machine verified, Founder confirmed, inferred, unknown. Historical receipts retain their original timestamp and evidence class. Fresh verification is a new dated event.

## 4. Close the documentation change

Before marking preservation complete:

1. Reconcile expected deliverables and source identities; record unresolved evidence explicitly.
2. Update the project front door/current-status pointer and relevant parent index. Explain supersession; retain historical originals.
3. Review the diff for unintended changes and public disclosure. Validate local links and record fields.
4. Commit only scoped files to a review branch. Push and independently retrieve the exact remote commit/file identities.
5. Record branch, commit SHA, changed paths, validation and remote readback. A draft PR is remotely preserved for review, not merged canonical authority.
6. If a push, readback or source recovery fails, retain work and set the corresponding state HOLD with the smallest next action. Do not label the whole job PASS.

Run the scoped checker from repository root:

`python3 08_PROJECTS/PROJECT_003_KNOWLEDGE_SYSTEM_RECONCILIATION/AUDIT_2026-11-16/validate.py`

The checker validates this backlog and local Markdown file targets only. It cannot verify rights, approve decisions, check external links, certify all historical documents, or determine whether a platform actually delivered.

## 5. Review at the consequence, then learn

At delivery, a material result, the next partner/design gate or a meaningful failure, append a short retrospective: expected versus observed, changed assumptions, what worked/failed, remaining uncertainty and next experiment/decision. Link the exact measured window and source IDs. For marketing, distinguish revenue/payment/refunds from platform attribution and join only in protected reporting.

Record the reusable lesson and the operating document that would change. Pick the next real application and its check. Example: exact object identity prevents sequence errors; verify the next actual distribution by asset/object ID, not list position.

Local lessons can stay local. For cross-project promotion, supply actual-use evidence, a second useful application, conflict check and the smallest proposed doctrine change. Explicit Founder approval is required before promotion. Record approved/rejected/deferred, the decision ID, updated standard and evidence of subsequent use. Merely adding a lesson file is not proof the institution changed behavior.

## Responsibility and review triggers

The executing collaborator owns capture; the repository steward owns preservation/readback; Drew owns material decisions, release and institutional promotion. These are responsibilities, not claims that new staff assignments exist.

Use a brief cross-project exception review alongside an existing active-project review when there are open material gaps. It covers only uncaptured events, blocked preservation, unreconciled release/results and lessons awaiting a real decision. Dormant/sunset projects do not acquire monthly work merely because this template exists. A future automated reminder would require its own requested setup and a defined evidence source.

## Rollback and escalation

If this proposal is declined, close the review without merging; history remains available. If merged documentation later needs correction, append a correction or make a reviewed revert of the scoped change. Do not reset shared history, delete source branches or rewrite prior approvals. Escalate only the missing decision/access or consequential conflict; keep independent work moving.
