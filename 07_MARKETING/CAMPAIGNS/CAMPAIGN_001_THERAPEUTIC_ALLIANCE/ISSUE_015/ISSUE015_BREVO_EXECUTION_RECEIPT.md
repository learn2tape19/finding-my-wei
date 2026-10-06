# Issue 015 — Brevo Execution Receipt

**Issue:** 015 — RESTRAINT / The Clinical Practice of Restraint
**Campaign:** **45** — "Tao Issue 015 — The Clinical Practice of Restraint"
**Intended send:** Monday, October 12, 2026, 10:00 AM ET (`2026-10-12T10:00:00-04:00`)
**Receipt date:** October 6, 2026
**Verdict:** **HELD UNDER FOUNDER DIRECTIVE — NO BREVO MUTATION PERFORMED.**
**Founder directive, October 6, 2026:** subject and preheader **APPROVED**; **hold campaign 45 unchanged** until Brevo write access is restored; **do not create campaign 46**; Buffer remains closed PASS.

Buffer passed independent reconciliation and its receipt is committed
(`ISSUE015_BUFFER_DEPLOYMENT_RECEIPT.md`), so the Brevo gate was correctly open. Brevo execution
then stopped on a capability blocker rather than improvising around it, as the handoff directs.

**Campaign 45 is unchanged. Its status remains `draft`. Nothing was sent, scheduled, created, or
deleted in Brevo.**

---

## STOP condition 1 — no write path to an existing Brevo campaign

Campaign 45 cannot be modified from this environment. Both available paths are closed:

| Path | State |
|---|---|
| Brevo MCP connector | Exposes `create_email_campaign`, `get_email_campaign`, `get_email_campaigns` and read-only list/sender/contact/template tools. **There is no update, schedule, or status-mutation tool for email campaigns.** |
| Direct Brevo v3 REST | `BREVO_API_KEY` exists locally in `finding-my-wei/Learn2Tape/.env` (`xkeysib-` form, 89 chars, untracked by git — correctly outside the repository). `GET /v3/account` returns **HTTP 401 `{"message":"API Key is not enabled","code":"unauthorized"}`**. It is the only Brevo key present on this machine. |

`PUT /v3/emailCampaigns/45` is therefore unreachable.

### What was deliberately not done

**No second campaign was created.** `BREVO_V1_ADAPTER.md` lists *"Duplicate campaign for the
issue"* as an explicit STOP condition, and the handoff instructs STOP-and-report over
improvisation. Creating campaign 46 to work around a missing update capability would have left two
Issue 015 campaigns against the same list, with the live one determined by whichever was scheduled
— exactly the failure mode the doctrine prohibits. Nothing was deleted either.

## STOP condition 2 — campaign 45 currently holds Issue 014 content end to end

Independent readback of campaign 45 shows that only its **name** belongs to Issue 015. Every other
field is Issue 014, carried over verbatim from campaign 44:

| Field | Campaign 45 as read back | Required for Issue 015 |
|---|---|---|
| Subject | "What You Say Becomes Part of the Treatment" | Issue 014's subject |
| Preheader | "Words can protect regulation—or reintroduce threat." | Issue 014's preheader |
| Eyebrow | `ISSUE 014 · COMMUNICATION` | `ISSUE 015 · RESTRAINT` |
| Hero image | `2026/09/MONDAY_LANDSCAPE_1200x628.png` | `2026/10/ISSUE015_MON_LANDSCAPE.png` |
| Hero link | `…/the-clinical-practice-of-language/` | `…/the-clinical-practice-of-restraint/` |
| CTA href | `…/the-clinical-practice-of-language/` | `…/the-clinical-practice-of-restraint/` |
| CTA label | `READ ISSUE 014 — LANGUAGE` | `READ ISSUE 015 — RESTRAINT` |
| Body | Issue 014 *Language* editorial in full | Issue 015 *Restraint* editorial |
| `<title>` | Issue 014's subject | Issue 015's subject |

Campaign 45 was created 2026-10-06 11:08 ET and last modified 11:31 ET. **If it were scheduled in
its current state it would send the Issue 014 email to list 64 on October 12 with a CTA pointing
at the wrong article.** That is the material risk this receipt exists to surface.

## Preflight results — everything verifiable passed

Executed read-only before the blocker was reached:

| Gate | Result |
|---|---|
| Authentication | **PASS** — organization `69e660956a08aaef49055093`, account drew@learn2tape.com |
| Send-credit / plan eligibility | **PASS** — Starter, paid, active; period 2026-09-20 → 2026-10-20; **39,085** `sendLimit` credits. The Oct 12 send falls inside the current period, so the adapter's manual billing-boundary dependency **does not apply to this issue** |
| Duplicate campaign check | **PASS** — campaign 45 is the only Issue 015 campaign; 44 (Issue 014) is `sent`, 43 (Issue 013) `sent` |
| Canonical article URL exists | Post 1877 `future`, scheduled Oct 12; article must exist before the 10:00 AM ET email — it publishes earlier the same morning |
| Hero image anonymously retrievable | **PASS** — HTTP 200, no auth header, no `Referer` |
| Hero image checksum rule | **PASS** — `531f8f5e…6092`, 1,122,807 bytes, 1200×628, identical to `issue015_verified_asset_manifest.csv` |
| Sender identity | **PASS** — ID **3**, drew@mail.taoclinicaltouch.com, reply-to drew@learn2tape.com, unchanged from Issues 007–014 |
| Recipient configuration | List **[64]**, no exclusions or segments — **as the Founder already configured it on campaign 45**, byte-identical to campaign 44 |
| `inlineImageActivation` | `false` — required by the external-media architecture; already correct on 45 |

### Recipient configuration — why this is not a third STOP

`TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6 states that *asserting* a recipient set for a new issue
is a STOP condition pending Founder resolution. No recipient set was asserted here. List 64 was
read back from the campaign the **Founder** created and configured, and it matches the
Founder-approved Issue 014 send. The prepared payload preserves it rather than choosing it.
List 64 reports **7** contacts (`remaining: 7`), up from 1 at the September 18 audit — the
publication opt-in list is now accumulating subscribers as the signup infrastructure standard
intends.

## Prepared, fully verified payload — one action to unblock

The complete campaign was composed and verified so that execution requires no further authoring:

- **`ISSUE015_BREVO_CAMPAIGN.html`** — the full campaign body.
  SHA-256 `7bb4c9c7962086962c8f0afdd3f47364566551aa79319616c5a9c37f8c34c248`, 5,317 bytes.
- **`ISSUE015_BREVO_PREPARED_PAYLOAD.json`** — the exact `PUT /v3/emailCampaigns/45` field set.

| Field | Prepared value |
|---|---|
| `subject` | More Intervention Is Not Automatically More Care |
| `previewText` | Knowing when to put our hands down is part of knowing how to use them. |
| `sender` | `{"id": 3}` |
| `replyTo` | drew@learn2tape.com |
| `recipients` | `{"lists": [64], "exclusionLists": [], "segments": [], "excludedSegments": []}` |
| `inlineImageActivation` | `false` |
| `mirrorActive` | `true` |
| `scheduledAt` | `2026-10-12T10:00:00-04:00` |

Scheduled time reproduces the established Monday 10:00 AM ET cadence exactly — Issue 014
(Oct 5), Issue 013 (Sept 28), Issue 011 (Sept 14), Issue 010 (Sept 7), Issue 008 (Aug 26) and
Issue 007 (Aug 20) all sent at `10:00:00-04:00`. EDT offset is correct for October 12; the Brevo
account timezone is `America/New_York`.

### Editorial provenance — zero invented prose

Layout, colours, typography, header, eyebrow, hero treatment, emphasised-term motif, arc line,
CTA button, signature and footer are preserved from campaign 44 structurally. Only the
issue-specific content changed, and **every editorial sentence in the body is verbatim from the
Founder-approved canonical article**, verified by automated string match against
`ISSUE015_CANONICAL_ARTICLE_DRAFT.md`:

- 11 of 11 body paragraphs matched the canonical article verbatim.
- The arc line *"Indication → Calibration → Reassessment → Decision → Completion"* is the
  Founder-approved weekly movement from `ISSUE015_FIVE_DAY_COPY_AND_VISUAL_DIRECTION.md`.
- `RESTRAINT.` mirrors Issue 014's `LANGUAGE.` emphasised-term slot.
- *"That is the idea at the center of this week's The Tao of Clinical Touch:"* is the established
  Issue 014 layout connective sentence, reused unchanged.
- No new claim, hashtag, emoji, hook, or rewritten passage was introduced.

### Subject line and preheader — FOUNDER APPROVED, October 6, 2026

**No Founder-approved Issue 015 subject line or preheader exists** in the canonical article, the
editorial brief, the five-day copy file, or the handoff. Issue 014's subject was authored during
that issue's production and is not a template.

Rather than author new copy under PRODUCTION ONLY, both were taken **verbatim from Founder-approved
Issue 015 language** — the Friday Feed/Landscape support and closing lines:

- Subject ← *"More intervention is not automatically more care."* (case adjusted to title case to
  match the established subject-line convention; **wording unchanged**)
- Preheader ← *"Knowing when to put our hands down is part of knowing how to use them."*
  (verbatim, unchanged)

This is reuse of approved language, not invention.

**Founder approved both values explicitly on October 6, 2026.** The subject line
*"More Intervention Is Not Automatically More Care"* and the preheader
*"Knowing when to put our hands down is part of knowing how to use them."* are now
Founder-approved Issue 015 copy and carry the same authority as the rest of the issue package.
The authority gap recorded above is **closed**. No further approval is required to apply them.

## Founder actions required

1. **Restore Brevo write access.** Enable a Brevo API key with campaign write scope (the local
   `BREVO_API_KEY` is disabled). The Founder has taken this item; execution resumes on his signal.
   Once enabled, this execution completes end to end with independent readback.
2. ~~Approve or replace the subject line and preheader.~~ **CLOSED — approved October 6, 2026.**
3. **Campaign 45 is on hold and must not be scheduled in its current state.** It would send
   Issue 014's email and article link. Held by Founder directive pending write access.
4. **Confirm post 1877's wp-admin time is before 8:00 AM ET on October 12** — carried from the
   Buffer receipt, and it must also precede the 10:00 AM ET email. **Still open.**

## Confirmations

- **No Brevo mutation of any kind was performed.** Campaign 45 remains `draft` and byte-unchanged;
  campaigns 44 and 43 were read-only; no campaign was created or deleted.
- No WordPress or Buffer object was touched in this pass.
- The Brevo key was confirmed by name, length and prefix form only. It was never printed, logged,
  committed, or passed in a process argument list. The prepared payload and campaign HTML contain
  no credential.

## Hold status — October 6, 2026

Campaign 45 is **held unchanged by Founder directive** until Brevo write access is restored.
Confirmed by readback at the time of this update: `status: draft`, `scheduledAt: ""`,
`modifiedAt: 2026-10-06T11:31:49.000-04:00` — unchanged since before this execution began.

**No campaign 46 will be created.** This is both the Founder's explicit instruction and the
standing adapter STOP condition on duplicate campaigns for an issue.

When write access is restored, the resume path is mechanical and requires no further authoring or
approval: apply `ISSUE015_BREVO_PREPARED_PAYLOAD.json` to campaign 45, then independently read
back sender, list, subject, preheader, body, CTA target, hero image URL and `scheduledAt`, and
record the result.

## Issue 015 Brevo: HELD

Buffer is complete and verified (**closed PASS** — see `ISSUE015_BUFFER_DEPLOYMENT_RECEIPT.md`;
not reopened or revisited by this update). Brevo is fully prepared, provenance-checked, and
Founder-approved on copy, held at a reported capability blocker with the material risk in
campaign 45 surfaced and no mutation performed.

**No final Issue 015 reconciliation record is produced, because the handoff conditions it on
Buffer and Brevo both passing.** It will be written when Brevo closes.
