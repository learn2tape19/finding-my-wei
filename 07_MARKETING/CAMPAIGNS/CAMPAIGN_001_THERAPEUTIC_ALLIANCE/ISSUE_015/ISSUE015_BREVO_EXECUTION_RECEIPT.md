# Issue 015 — Brevo Execution Receipt

**Issue:** 015 — RESTRAINT / The Clinical Practice of Restraint
**Campaign:** **45** — "Tao Issue 015 — The Clinical Practice of Restraint"
**Status:** **`queued` (scheduled)**
**Scheduled send:** **Monday, October 12, 2026, 10:00:00 AM ET — `2026-10-12T10:00:00.000-04:00` (= `2026-10-12T14:00:00Z`)**
**Receipt date:** October 6, 2026
**Verdict:** **PASS — campaign 45 updated and scheduled, verified by independent readback.**

The hold recorded in the previous revision of this receipt is **released**. Brevo write access was
restored by the Founder; the already-approved `ISSUE015_BREVO_PREPARED_PAYLOAD.json` was applied to
**existing campaign 45**. No campaign 46 was created. Buffer was not reopened or modified.

Nothing has been sent. `statistics.globalStats.sent` = 0, `testSent` = false. The campaign sits in
the queue awaiting its scheduled time.

---

## 1. Authentication — PASS

| Gate | Result |
|---|---|
| Credential | `BREVO_API_KEY` read from the environment. **Never printed, logged, echoed, committed, or passed in a process argument list.** Supplied to `curl` via a `umask 077` config file held outside the repository in the session scratchpad and deleted at completion. |
| `GET /v3/emailCampaigns/45` | **HTTP 200** — read-only authentication confirmed before any mutation |
| `GET /v3/account` | **HTTP 200** — `organization_id` **`69e660956a08aaef49055093`**, account `drew@learn2tape.com` — identical to the organization recorded during the held pass |
| Plan eligibility | Starter subscription, **39,085** `sendLimit` credits, period 2026-09-20 → 2026-10-20. The October 12 send falls **inside** the current period, so the adapter's billing-boundary dependency does not apply. |

## 2. Campaign identity — PASS, with one recorded pre-state drift

Read-only readback before any write:

| Field | Value at resume |
|---|---|
| `id` | 45 |
| `type` | `classic` |
| `status` | `draft` |
| `scheduledAt` | `""` |
| `createdAt` | 2026-10-06T11:08:58.000-04:00 |
| `modifiedAt` | **2026-10-06T11:48:19.000-04:00** |
| Content | Issue 014 end to end — 0 occurrences of `ISSUE 015`, `RESTRAINT`, or the Issue 015 article slug; hero still `2026/09/MONDAY_LANDSCAPE_1200x628.png` |

**Recorded drift — not a STOP, disclosed in full.** The hold directive snapshotted campaign 45 at
`modifiedAt: 2026-10-06T11:31:49.000-04:00` with the name *"Tao Issue 015 — The Clinical Practice
of Restraint"*. At resume the campaign read `modifiedAt: 11:48:19` and the name
*"Tao Issue 015 — Restraint"*. Campaign 45 was therefore edited between the hold snapshot and this
resume — a rename only.

Proceeding was judged correct rather than improvisational because:

- the **material** state was exactly as the hold documented — `draft`, unscheduled, Issue 014
  content in full, with **no partial Issue 015 edit in flight that could be destroyed**;
- `name` is internal Brevo metadata, never visible to a recipient; and
- `name` is itself a Founder-approved field in the prepared payload, so applying the payload
  applies an approved value rather than a chosen one.

The approved long-form name was restored by the payload. **If the shorter name was a deliberate
Founder preference, it is the one field to re-set — it has no effect on the email itself.**

## 3. Payload integrity — PASS

| Artifact | Expected | Verified |
|---|---|---|
| `ISSUE015_BREVO_CAMPAIGN.html` SHA-256 | `7bb4c9c7962086962c8f0afdd3f47364566551aa79319616c5a9c37f8c34c248` | **match** |
| `ISSUE015_BREVO_CAMPAIGN.html` bytes | 5,317 | **match** |
| Hero image, anonymous HTTPS, no `Referer` | HTTP 200 | **HTTP 200** |
| Hero bytes | 1,122,807 | **match** |
| Hero SHA-256 | `531f8f5e80994482df8f18dc7bfc5f214b382e8089f4cd15abfb401f538c6092` | **match** |
| Hero dimensions | 1200×628 | **match** (read from PNG IHDR) |
| Recipient list 64 | exists, populated | `Tao subscriber list`, **7** subscribers, 0 blacklisted |
| Sender 3 | registered, active | `Drew Freedman \| Tao of Clinical Touch` / drew@mail.taoclinicaltouch.com, active |
| Oct 12, 2026 is a Monday | yes | **confirmed** |
| `-04:00` is correct EDT offset for Oct 12, 2026 | yes | **confirmed** |

## 4. Mutation log — three requests, one effective write

Content and schedule were applied as **two separate steps** so that every editorial field could be
reconciled *before* the campaign was ever placed in a sendable state.

| # | Request | Result | Effect |
|---|---|---|---|
| 1 | `PUT /v3/emailCampaigns/45` — payload `recipients` verbatim (`lists`/`exclusionLists`/`segments`) | **HTTP 400** `missing_parameter: Either the listIds or segmentIds are mandatory in recipients` | **None.** Rejected atomically — confirmed by readback: `modifiedAt` still 11:48:19, subject still Issue 014's. |
| 2 | Same, `recipients: {listIds:[64], exclusionListIds:[]}` | **HTTP 400** `missing_parameter: exclusionListIds are missing` | **None.** Brevo rejects an empty array as absent. |
| 3 | Same, `recipients: {listIds:[64]}` | **HTTP 204** | **Content applied.** |
| 4 | `PUT /v3/emailCampaigns/45` — `{"scheduledAt":"2026-10-12T10:00:00-04:00"}` | **HTTP 204** | **Scheduled.** |

**On the recipient remap.** Brevo's read schema returns `recipients.lists`; its write schema
requires `recipients.listIds`. This is a transport-format asymmetry in the Brevo API, not a change
of approved value. The recipient set applied is **list 64, no exclusions, no segments** — byte-identical
in meaning to the approved payload, and confirmed by readback in §5 to have produced exactly
`{"lists":[64],"exclusionLists":[],"segments":[],"excludedSegments":[]}`.

## 5. Independent readback reconciliation — PASS

Re-fetched with a fresh `GET /v3/emailCampaigns/45` after the write. **No field below is taken from
a mutation response.**

| Field | Approved value | Read back | |
|---|---|---|---|
| `id` | 45 | 45 | PASS |
| `name` | Tao Issue 015 — The Clinical Practice of Restraint | identical | PASS |
| `subject` | More Intervention Is Not Automatically More Care | identical | PASS |
| `previewText` (preheader) | Knowing when to put our hands down is part of knowing how to use them. | identical | PASS |
| `sender.id` | 3 | 3 | PASS |
| `sender.email` | drew@mail.taoclinicaltouch.com | identical | PASS |
| `replyTo` | drew@learn2tape.com | identical | PASS |
| `recipients.lists` | `[64]` | `[64]` | PASS |
| `recipients.exclusionLists` | `[]` | `[]` | PASS |
| `recipients.segments` | `[]` | `[]` | PASS |
| `recipients.excludedSegments` | `[]` | `[]` | PASS |
| `inlineImageActivation` | `false` | `false` | PASS |
| `mirrorActive` | `true` | `true` | PASS |
| `type` | `classic` | `classic` | PASS |
| `<title>` | More Intervention Is Not Automatically More Care | identical | PASS |
| CTA / article href | `…/blog/2026/10/the-clinical-practice-of-restraint/` | identical, sole non-unsubscribe href | PASS |
| CTA label | `READ ISSUE 015 — RESTRAINT` | identical | PASS |
| Hero image `src` | `…/uploads/2026/10/ISSUE015_MON_LANDSCAPE.png` | identical, sole `<img>` | PASS |
| Eyebrow | `ISSUE 015` present | present | PASS |
| Issue 014 residue | 0 | **0** occurrences of `ISSUE 014`, `the-clinical-practice-of-language`, `MONDAY_LANDSCAPE_1200x628` | PASS |
| `htmlContent` | 5,317 bytes / `7bb4c9c7…c248` | 5,316 bytes / `02529880…2d6f` | **normalized — see below** |

### The one-byte difference, characterized exactly

A character-level diff of the local file against the stored content returns **exactly one opcode**:

```
delete: local[5316:5317] = '\n'   remote[5316:5316] = ''
```

Brevo strips the single trailing newline following `</html>`. Every one of the first 5,316 bytes is
identical, and `sha256(local_file.rstrip('\n'))` == `02529880…2d6f` == the stored content hash
exactly. Trailing whitespace after the closing tag is insignificant to every mail renderer.

This is **server-side storage normalization, not a content discrepancy**, and it is recorded here
rather than silently reconciled away. Both checksums are preserved above so the delta stays auditable.

**Editorial reconciliation: 0 mismatches.**

## 6. Scheduling verification — PASS

Verified by a **third** independent `GET` issued after the scheduling write:

| Check | Result |
|---|---|
| `status` | **`queued`** — scheduled, not sent, not draft |
| `scheduledAt` | **`2026-10-12T10:00:00.000-04:00`** |
| Parsed instant equals approved `2026-10-12T10:00:00-04:00` | **exact match** |
| UTC equivalent | `2026-10-12T14:00:00+00:00` |
| Weekday | **Monday** |
| UTC offset | **−04:00**, correct EDT for October 12, 2026 |
| Cadence | Matches Issues 007, 008, 010, 011, 013, 014 — all `10:00:00-04:00` Monday |
| `testSent` | `false` |
| `statistics.globalStats.sent` | **0** — nothing dispatched |
| Content survived scheduling | `htmlContent` SHA-256 still `02529880…2d6f` | 

No scheduling ambiguity arose: the account timezone is `America/New_York`, the offset was supplied
explicitly in the request rather than inferred, and the stored value was read back and re-parsed.

## 7. Open item carried forward — sender display name

**This is a verification gap, not a known defect, and it is not being passed off as verified.**

The approved payload specifies `sender: {"id": 3}`, and that is exactly what was sent. Before the
write, campaign 45 reported `sender.name` as the Brevo placeholder `[DEFAULT_FROM_NAME]` (inherited
when it was duplicated from campaign 44). After the write it reports `sender.name` as `""`.

- Sender **3** is registered and active as **`Drew Freedman | Tao of Clinical Touch`**, so the
  from-name resolves from the sender record at send time — the expected consequence of addressing a
  sender by `id`, which is what the approved payload instructs.
- Campaign 44 — the sent Issue 014 precedent — reads `[DEFAULT_FROM_NAME]`, so this is a
  **divergence in representation from the precedent**, in a recipient-visible field.

`[DEFAULT_FROM_NAME]` is a read-side placeholder token, not a writable value; writing that literal
string would set the from-name to that literal. **No corrective write was improvised.** The API
cannot settle which string a recipient will see.

**Founder action — 30 seconds in the Brevo UI:** open campaign 45 and confirm the *From name* field
shows **Drew Freedman | Tao of Clinical Touch** and not a blank. If blank, set it there; the
campaign stays scheduled either way, and there are six days of margin.

## 8. Confirmations

- Only **campaign 45** was mutated. **No campaign 46 was created.** Nothing was deleted.
- **Buffer was not reopened, read, or modified** — it remains closed PASS per
  `ISSUE015_BUFFER_DEPLOYMENT_RECEIPT.md`.
- WordPress was not modified. Media were read-only.
- Campaigns 44 and 43 were read-only, for precedent comparison.
- No editorial copy was authored, altered, or regenerated in this pass. The applied body is the
  Founder-approved `ISSUE015_BREVO_CAMPAIGN.html`, unchanged.
- `BREVO_API_KEY` was never printed, logged, committed, or placed in a process argument list. The
  transient curl config holding it lived outside the repository under `umask 077` and was deleted.
  This receipt, the prepared payload, and the campaign HTML contain no credential.

## Issue 015 Brevo: PASS

Campaign **45** is scheduled and verified for **Monday, October 12, 2026 at 10:00:00 AM ET**, to
list **64**, from sender **3**, with the Founder-approved Issue 015 subject, preheader, body, hero
image and canonical CTA — every field confirmed by independent readback, with one documented
trailing-newline normalization and one open from-name confirmation for the Founder.
