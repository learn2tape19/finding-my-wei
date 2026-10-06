# Issue 015 — Final Reconciliation Record

**Issue:** 015 — RESTRAINT / The Clinical Practice of Restraint
**Publication week:** October 12–16, 2026
**Canonical article:** https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-restraint/
**Record date:** October 6, 2026
**Verdict:** **PASS — with two open Founder confirmations, both recorded below and neither blocking.**

Produced under the `ISSUE015_CLAUDE_EXECUTION_HANDOFF.md` final-reconciliation requirement, which
conditions this record on Buffer and Brevo both passing. Both have now passed independent readback.

---

## 1. Summary

| System | Object | State | Verdict |
|---|---|---|---|
| WordPress | post **1877** | `future`, scheduled October 12, 2026 | **PASS** (exact hour open — §2) |
| WordPress media | **25** assets | live, anonymously retrievable, checksum-reconciled | **PASS** |
| Buffer | **25** content items / **45** channel posts | all `scheduled`, Oct 12–16 | **PASS** (closed; not reopened) |
| Brevo | campaign **45** | `queued` for 2026-10-12 10:00:00 ET | **PASS** (from-name open — §5) |

**Nothing has been published or sent.** Every object is in a scheduled, pre-delivery state.

## 2. WordPress article

| Field | Value | Source |
|---|---|---|
| Post ID | 1877 | authenticated readback, handoff-established |
| Title | *The Clinical Practice of Restraint* | authenticated readback |
| Slug | `the-clinical-practice-of-restraint` | authenticated readback |
| Status | `future` | authenticated readback |
| Scheduled date | October 12, 2026 | authenticated readback |
| Featured media | 1870 — `ISSUE015_MON_LANDSCAPE.png` | authenticated readback |
| Body | matches Founder-approved canonical manuscript | verified against `ISSUE015_CANONICAL_ARTICLE_DRAFT.md` |

Confirmed in this pass: anonymous `GET /wp-json/wp/v2/posts/1877` returns **HTTP 401** and the
canonical URL returns **HTTP 404**. This is **correct pre-publication behavior** — WordPress serves
a `future` post to nobody — and it reproduces the state recorded in the Buffer receipt.

**OPEN — carried forward, not newly discovered.** The article's exact scheduled *hour* has never
been verified by this agent. `TAO_WP_APP_PASSWORD` is **unset**, so no authenticated WordPress read
was possible in this pass. The site has a documented history of a 7:45 ET / 11:45 UTC scheduling
trap.

**Founder action:** confirm in wp-admin that post 1877 publishes **before 8:00 AM ET** on October 12.
It must precede both the 8:00 AM ET social launch and the 10:00 AM ET email, because both link to it.
This is the single highest-value remaining check in Issue 015 — if the article publishes late, 45
scheduled social posts and one email point at a 404.

## 3. WordPress media — 25/25

| Gate | Result |
|---|---|
| Assets live | 25/25 |
| HTTP 200 on anonymous retrieval | 25/25 |
| Dimensions correct (Feed 1080×1350, Landscape 1200×628, Story 1080×1920) | 25/25 |
| SHA-256 == canonical `issue015_verified_asset_manifest.csv` | 25/25 |
| Filename day prefix matches scheduled date | 25/25 |
| WordPress-generated resized derivatives used | **0** — every URL a full-size original |

Per-asset bytes, dimensions and both checksums recorded in `ISSUE015_MEDIA_STATE.json`.

The Monday landscape was **re-verified independently in this Brevo pass** as the email hero:
HTTP 200 anonymous, no `Referer`, 1,122,807 bytes, 1200×628,
SHA-256 `531f8f5e80994482df8f18dc7bfc5f214b382e8089f4cd15abfb401f538c6092` — identical to the
manifest value and to the Buffer-pass reading.

## 4. Buffer — 25 content items / 45 channel deliveries

**Closed PASS. Not reopened, re-read, or modified in the Brevo pass**, per Founder directive.

| Gate | Result |
|---|---|
| Content items in Oct 12–16 window | 25/25 |
| Channel posts read back by ID | 45/45 |
| Independent window query == created set | 45/45, 0 extras, 0 missing |
| Status `scheduled` | 45/45 |
| Facebook Landscapes | 5/5 |
| Instagram Feeds | 10/10 |
| Instagram Stories | 30/30 |
| Facebook Stories | **0** |
| Story 3 posts carrying canonical native link | 10/10 |
| Facebook captions carrying canonical URL | 5/5 |
| Instagram Feed captions using "link in bio" | 10/10 |
| Story content items with no caption | 15/15 |
| Captions verbatim against approved copy | 45/45 |
| Media URL matches day and role | 45/45 |
| Duplicate IDs / duplicate (channel,time,media) | **0 / 0** |
| Failed imports or channel warnings | **0** |

Full detail in `ISSUE015_BUFFER_DEPLOYMENT_RECEIPT.md` and `ISSUE015_BUFFER_OBJECTS.json`.

## 5. Brevo — campaign 45

| Field | Value |
|---|---|
| Campaign ID | **45** |
| Name | Tao Issue 015 — The Clinical Practice of Restraint |
| Status | **`queued`** |
| Scheduled | **2026-10-12T10:00:00.000-04:00** (Monday, EDT) = `2026-10-12T14:00:00Z` |
| Subject | More Intervention Is Not Automatically More Care |
| Preheader | Knowing when to put our hands down is part of knowing how to use them. |
| Sender | ID 3 — drew@mail.taoclinicaltouch.com |
| Reply-to | drew@learn2tape.com |
| Recipients | list **[64]** — `Tao subscriber list`, 7 subscribers; no exclusions, no segments |
| Hero | `…/uploads/2026/10/ISSUE015_MON_LANDSCAPE.png` |
| CTA | `…/blog/2026/10/the-clinical-practice-of-restraint/` — `READ ISSUE 015 — RESTRAINT` |
| `inlineImageActivation` | `false` |
| `mirrorActive` | `true` |
| Sent | **0** — `testSent` false, nothing dispatched |

Every field above confirmed by independent `GET` after the write, not from mutation responses.
Full detail in `ISSUE015_BREVO_EXECUTION_RECEIPT.md`.

**OPEN — sender display name.** Campaign 45 reports `sender.name` as `""` where the sent Issue 014
precedent reports the placeholder `[DEFAULT_FROM_NAME]`. Sender 3 is registered and active as
`Drew Freedman | Tao of Clinical Touch`, which is what should resolve at send time, but the API
cannot settle which string a recipient sees. No corrective write was improvised.
**Founder action:** confirm the *From name* on campaign 45 in the Brevo UI.

## 6. Canonical URL consistency

One URL across every surface:

```
https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-restraint/
```

| Surface | Occurrences | Verdict |
|---|---|---|
| WordPress post 1877 slug | `the-clinical-practice-of-restraint` | **consistent** |
| Buffer — Facebook Landscape captions | 5/5 | **consistent** |
| Buffer — Story 3 native links | 10/10 | **consistent** |
| Buffer — Instagram Feed captions | "link in bio", raw URL absent by design | **consistent** |
| Brevo — hero link and CTA href | sole non-unsubscribe href in the body | **consistent** |
| Issue 014 URL residue anywhere in Issue 015 | **0** | **clean** |

## 7. Checksums of record

| Artifact | SHA-256 | Bytes |
|---|---|---|
| `ISSUE015_BREVO_CAMPAIGN.html` (repository) | `7bb4c9c7962086962c8f0afdd3f47364566551aa79319616c5a9c37f8c34c248` | 5,317 |
| Campaign 45 `htmlContent` (as stored by Brevo) | `025298802970194bae9cc9346ce8e97bbe5a399899032cf702a927c9e33e2d6f` | 5,316 |
| `ISSUE015_MON_LANDSCAPE.png` (email hero) | `531f8f5e80994482df8f18dc7bfc5f214b382e8089f4cd15abfb401f538c6092` | 1,122,807 |
| 25 campaign assets | per-asset in `ISSUE015_MEDIA_STATE.json` | per-asset |

## 8. Exceptions register

Every deviation encountered across Issue 015 execution, disclosed:

| # | Exception | Classification | Status |
|---|---|---|---|
| 1 | Campaign 45 `modifiedAt` was 11:48:19 at resume vs 11:31:49 in the hold snapshot; name had been shortened to "Tao Issue 015 — Restraint" | Pre-state drift, rename only; material state (draft, unscheduled, Issue 014 content) exactly as documented | **Disclosed; approved payload name applied** |
| 2 | Brevo rejected the approved `recipients` object twice — write schema requires `listIds`, and rejects `exclusionListIds: []` as absent | API transport-format asymmetry, not a value change | **Resolved** — readback confirms list 64, no exclusions, no segments |
| 3 | Brevo strips the trailing newline after `</html>`; stored body is 5,316 bytes vs 5,317 local | Server-side storage normalization; single-opcode diff, first 5,316 bytes identical | **Characterized, both checksums recorded** |
| 4 | `sender.name` reads `""` vs `[DEFAULT_FROM_NAME]` on the Issue 014 precedent | Representation divergence in a recipient-visible field | **OPEN — Founder confirm (§5)** |
| 5 | Post 1877's exact scheduled hour never verified; `TAO_WP_APP_PASSWORD` unset | Verification gap, carried from the Buffer pass | **OPEN — Founder confirm (§2)** |
| 6 | Buffer adapter warns against Tao publishing to `drewdog19`, superseded by the Issue 014 Founder-approved precedent | Governance conflict resolved by precedent, as the handoff directs | **Disclosed in Buffer receipt** |

Nothing in this register was silently reconciled away.

## 9. Scope confirmations

- Systems mutated across Issue 015: **Buffer** (25 items / 45 posts) and **Brevo campaign 45**. Nothing else.
- **No campaign 46 was created.** No campaign was deleted.
- **WordPress was never modified** — read-only throughout.
- Issue 014 and all earlier issue objects were **never touched**; campaigns 44 and 43 were read-only.
- No editorial copy was authored, rewritten, regenerated, cropped, substituted, or renamed. Every
  deployed string traces to a Founder-approved source.
- No credential was printed, logged, committed, or passed in a process argument list.

## Issue 015: PASS

WordPress article scheduled, 25 media assets verified, 25 Buffer content items delivering 45
scheduled channel posts across October 12–16, and Brevo campaign 45 queued for Monday, October 12,
2026 at 10:00:00 AM ET — all reconciled against Founder-approved sources by independent readback.

**Two Founder confirmations remain open and neither blocks the schedule:** post 1877's publish hour
(§2) and campaign 45's From name (§5).
