# Issue 007 — Wednesday–Friday Founder-Approved Execution Handoff

**Publication:** The Tao of Clinical Touch  
**Issue:** 007 — Permission Over Time  
**Scope:** Wednesday, Thursday, Friday  
**Status:** FOUNDER APPROVED FOR EXECUTION PREP  
**Editorial authority:** Locked. Claude is executor, not author.  

## 1. Purpose

This handoff packages the Founder-approved Wednesday–Friday production for the next phase of the Issue 007 launch. Claude must execute from the approved copy and approved visual assets without rewriting, redesigning, filling gaps, changing headlines, inventing slogans, or substituting destinations.

The governing chain is:

> **Editorial Arc → Canonical Source → Approved Derivatives → Approved Native Assets → Execution Packet → BUILD_DRAFT → Independent Verification → Founder Review**

## 2. Governing read order

Read completely, in order:

1. `../TAO_EDITORIAL_ARC_REGISTER.md`
2. `FOUNDER_APPROVAL_GATE_0.md`
3. `WEDNESDAY/WEDNESDAY_CANONICAL_SOURCE.md`
4. `WEDNESDAY/FINAL_COPY_PACKAGE.md`
5. `THURSDAY/FINAL_COPY_PACKAGE.md`
6. `FRIDAY/FINAL_COPY_PACKAGE.md`
7. `WEDNESDAY/APPROVED_ASSET_MANIFEST.md`
8. `THURSDAY/APPROVED_ASSET_MANIFEST.md`
9. `FRIDAY/APPROVED_ASSET_MANIFEST.md`
10. `ASSETS/DECODE_APPROVED_ASSETS.py`
11. Current FREEDMAN-FOUNDRY execution standards on `main`, including credential, destination, idempotency, receipt, and Buffer connector authority.

If repository execution authority conflicts with this handoff, **the narrower authority wins** and execution stops for Founder review.

## 3. Locked editorial arc

- **Monday:** PERMISSION IS NOT A QUESTION. — A yes can begin an encounter.
- **Tuesday:** THE BODY CAN CHANGE ITS ANSWER. — The experience can change.
- **Wednesday:** THE ANSWER MAY CHANGE BEFORE IT IS SPOKEN. — Notice without assuming.
- **Thursday:** MAKE CHANGING THE ANSWER EASY. — Create room for another answer.
- **Friday:** PERMISSION IS A PRACTICE. — Notice → Invite → Listen → Respond.

The week resolves with:

> **Permission is not a moment we pass through on the way to treatment. It is part of the treatment.**

## 4. Approved Tao Buffer destinations

Authorized Tao destinations only:

- **Facebook — The Tao of Clinical Touch**: `6a3eb95f5ab6d2f106763fc9`
- **Instagram — taoclinicaltouch**: `6a3eb89f5ab6d2f106763ca0`

Explicitly unauthorized for this Issue 007 Tao execution:

- **Personal Instagram — drewdog19**: `6a3eba3f5ab6d2f106764339`

Canonical Buffer credential reference: `BUFFER_API_KEY`.

## 5. Current external authority ceiling

For Buffer, this handoff authorizes **BUILD_DRAFT only** under the already-merged Foundry controls.

Do **not**:

- publish;
- schedule;
- queue;
- delete;
- cancel;
- retry an ambiguous write;
- substitute another channel;
- mutate personal Instagram.

After each createPost draft mutation, independently fetch the created Buffer object and verify:

1. created ID == fetched ID;
2. state == `DRAFT` / Buffer-equivalent draft state;
3. destination channel == requested canonical Tao channel;
4. copy/media correspond to the approved packet.

Only after successful independent verification may the execution receipt be persisted.

## 6. WordPress / blog boundary

The **Issue 007 canonical weekly blog is Wednesday's canonical article**: `WEDNESDAY/WEDNESDAY_CANONICAL_SOURCE.md`.

Do not create independent Thursday or Friday blog articles. Their 1200×628 files are approved supporting/share assets, not authorization for duplicate articles.

Prepare the WordPress-ready Wednesday package from `WEDNESDAY/FINAL_COPY_PACKAGE.md`. Do not mutate WordPress unless current institutional authority independently authorizes that write.

## 7. Email boundary

Wednesday, Thursday, and Friday email derivatives are approved copy packages. Prepare them exactly as written. Do not send or schedule email. Do not create a Brevo external draft unless current Foundry/Brevo authority independently authorizes the requested mutation and all sender/account/list checks pass.

## 8. Approved visual asset reconstruction

Approved native JPEG assets are stored as encoded ZIP bundles under `ASSETS/ENCODED/` so the exact Founder-approved production can survive handoff through GitHub.

Run:

```bash
python3 07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_007/ASSETS/DECODE_APPROVED_ASSETS.py
```

The script must decode the three bundles and verify every SHA-256 checksum from each day's `ASSET_MANIFEST.json`. Checksum mismatch = **BLOCKED**.

Do not recreate the visuals with generative AI. Do not substitute a different ripple. Do not add drips, slogans, icons, or copy beyond what is already embedded in the approved files.

## 9. Buffer draft execution packets

Create separate deterministic execution packets for each authorized day/channel pair.

Recommended idempotency keys:

- `ISSUE007-WED-FB-001`
- `ISSUE007-WED-IG-001`
- `ISSUE007-THU-FB-001`
- `ISSUE007-THU-IG-001`
- `ISSUE007-FRI-FB-001`
- `ISSUE007-FRI-IG-001`

Use the approved **Feed 1080×1350** asset for the primary Facebook/Instagram feed draft. Story assets are preserved as approved production but are not automatically authorized for Buffer mutation unless the current Buffer connector explicitly supports the relevant Story operation under BUILD_DRAFT authority.

## 10. Preflight before each external mutation

Before any Buffer write:

1. Resolve `BUFFER_API_KEY` securely.
2. Authenticate and independently verify canonical account.
3. Independently resolve canonical organization.
4. Independently verify requested Tao channel.
5. Reject personal Instagram.
6. Verify exact approved asset exists and checksum passes.
7. Verify exact approved platform copy.
8. Check persistent ExecutionLedger for the packet idempotency key.
9. Confirm authority remains BUILD_DRAFT only.

Any mismatch, ambiguity, missing file, or duplicate = **BLOCKED**.

## 11. Ambiguous write handling

If a Buffer createPost call times out or returns an ambiguous transport outcome:

- issue no second mutation;
- do not infer failure from absence of a ledger receipt;
- return `AMBIGUOUS_WRITE`;
- escalate to Founder;
- stop that execution path.

## 12. Required completion report

Return:

- branch/commit used;
- decoded asset checksum result;
- exact packet IDs;
- exact destination channel IDs;
- draft IDs created;
- independent fetched IDs/states;
- ledger receipt IDs;
- any BLOCKED or NOT_RUN operations;
- explicit confirmation: no publish, schedule, queue, delete, or personal-Instagram mutation occurred.

## 13. STOP condition

After the authorized drafts are built and independently verified, **STOP FOR FOUNDER REVIEW**.

Do not continue into publication authority based on content approval or successful draft creation.
