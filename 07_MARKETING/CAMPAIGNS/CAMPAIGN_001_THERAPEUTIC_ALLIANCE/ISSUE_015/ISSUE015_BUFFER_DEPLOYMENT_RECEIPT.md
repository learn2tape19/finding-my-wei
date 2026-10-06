# Issue 015 — Buffer Deployment Receipt

**Issue:** 015 — RESTRAINT / The Clinical Practice of Restraint
**Publication week:** October 12 – 16, 2026
**Status:** **ALL 25 BUFFER CONTENT ITEMS SCHEDULED AND INDEPENDENTLY VERIFIED. NOTHING PUBLICLY VISIBLE YET.**
**Receipt date:** October 6, 2026
**Verdict:** **PASS**

Executed under Founder authorization of October 6, 2026 and the directive
*EXECUTION MODE: PRODUCTION ONLY / NO CREATIVE DISCRETION.* No headline, caption, visual,
cadence, destination, or asset was authored, rewritten, cropped, resized, regenerated, or
substituted during this deployment. Buffer was the only system mutated.

---

## Final production state

| Layer | State as of receipt | Verified |
|---|---|---|
| WordPress media | 25 assets live, anonymous HTTPS | 25/25 HTTP 200, dimensions and SHA-256 reconciled |
| WordPress article | post 1877, `future`, scheduled Oct 12, 2026 | Handoff-established authenticated readback; exact hour pending Founder confirmation |
| Buffer | 25 content items / 45 channel posts, all `scheduled` | 45/45 read back by ID + independent window query |
| Brevo | Not started — gated behind this receipt | — |

## Architecture — 25 content items / 45 channel deliveries

Buffer's `createPost` mutation accepts a **singular** `channelId`, so multi-channel objects
cannot be expressed through it without creating duplicate objects. The correct construct is
**`createContentItem`**, which accepts `posts: [CreatePostInput!]!` and groups the per-channel
posts under one shared `contentItemId`. This reproduces the Issue 014 architecture exactly.

The queue holds **25 content items** delivering across **45 channel posts**. The 45 is a delivery
count, not an object count. No duplicate objects were created to reach multi-channel distribution.

## Channel distribution

| Channel | Channel ID | Channel posts |
|---|---|---:|
| Instagram — The Tao of Clinical Touch | `6a3eb89f5ab6d2f106763ca0` | 20 |
| Instagram — drewdog19 | `6a3eba3f5ab6d2f106764339` | 20 |
| Facebook — The Tao of Clinical Touch | `6a3eb95f5ab6d2f106763fc9` | 5 |
| **Total** | | **45** |

| Role | Items | Destination |
|---|---:|---|
| Feed 1080×1350 | 5 | both Instagram accounts |
| Landscape 1200×628 | 5 | Facebook only |
| Story 1080×1920 | 15 | both Instagram accounts |

**Facebook Stories: 0.** Facebook receives the Landscape object only, as directed.

All three destinations resolved by explicit ID — never by list position, service type, or name
substring — and each asserted `isDisconnected:false` / `isLocked:false` before mutation and again
on readback. LinkedIn `bostonbodyworker` (`6aa07201cd8b9c702c305cf3`) is present in the
organization and `isLocked:true`; it is not a Tao destination and received nothing.

## Governance resolution — drewdog19 destination

The handoff flagged a potential conflict and required a STOP-and-report rather than a silent
choice. It was resolved by date of authority, not by preference:

| Authority | Date | Position on drewdog19 |
|---|---|---|
| `BUFFER_V1_ADAPTER.md` v1.0 | September 13, 2026 | "never publish Tao content to them" |
| `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` (last modified Sept 23) | September 13, 2026 | "Also connected but **not Tao**" |
| `ISSUE014_BUFFER_DEPLOYMENT_RECEIPT.md` — Founder-approved production | **September 27, 2026** | **20 Instagram channel posts deployed to drewdog19** |

A full repository review of every commit after September 27, 2026 found **no** newer Founder
directive addressing Tao destinations. The only post-014 governance commits concern Issue 015
editorial/visual development and unrelated repository reconciliation. Issue 014 therefore stands
as the immediate production precedent, exactly as the handoff instructs, and Issue 015 reproduces
its distribution. **No STOP condition.** The adapter's warning predates the Founder-approved
production receipt that supersedes it; recorded here so the next issue does not re-litigate it.

## Schedule — five objects per day, Oct 12–16, 2026

| Role | ET | UTC | Channel posts per day |
|---|---|---|---:|
| Feed + Landscape | 8:00 AM | 12:00Z | 3 |
| Story 1 of 3 | 9:00 AM | 13:00Z | 2 |
| Story 2 of 3 | 11:00 AM | 15:00Z | 2 |
| Story 3 of 3 | 1:00 PM | 17:00Z | 2 |

Five content items and nine channel posts on each of the five dates. Issue 015 falls during EDT
(UTC−4), before the November 1 DST transition, so no slot drifts. All 45 `dueAt` values were
read back and matched the approved slot exactly.

## Canonical URL

`https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-restraint/`

- Carried by **5/5** Facebook Landscape captions
- Carried as the **native Instagram Story link on all 10 Story 3/3 channel posts**
  (`type=story`, `shouldShareToFeed=false`, `link=<canonical>` — confirmed by readback, not by
  submit-time acceptance)
- Instagram Feed captions use **"link in bio"** — 10/10, with **zero** raw canonical URLs
  anywhere in Instagram body copy (verified negatively across all 40 Instagram posts)

## Caption construction — approved language only

Feed and Landscape captions consist of the Founder-approved Issue 015 headline, support line and
closing line verbatim, followed by the established Issue 014 link treatment read back from live
production. Nothing else was added.

Instagram Feed and Landscape:

```
<APPROVED HEADLINE>

<approved support line>

<approved closing line>

Read the full issue → link in bio
```

Facebook Landscape substitutes the link treatment:

```
Read the full issue:
https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-restraint/
```

**Recorded interpretation — hashtags excluded.** Issue 014's live captions carried a five-hashtag
block and a day-specific long-form body derived from that article. The Issue 015 handoff instead
specifies, per day, *"Feed/Landscape approved text only"* followed by exactly three lines, and
constrains platform adaptation to *"the established Issue 014 link treatment above; no new claims,
hashtags, emojis, hooks, or rewritten prose."* No Founder-approved Issue 015 hashtag set exists in
`ISSUE015_FIVE_DAY_COPY_AND_VISUAL_DIRECTION.md` or the handoff. Selecting one — whether invented
or carried over from Issue 014's different theme — would be creative discretion, which this
execution mode prohibits. Captions therefore contain the approved language and the link treatment
only. **This is a deliberate, documented divergence from the Issue 014 caption surface and is
flagged for Founder review.** It is reversible without touching media or schedule.

Story objects carry **no caption** — 15/15 content items, 30/30 channel posts with empty `text`.

## Media verification — 25/25

All 25 publication assets were anonymously retrieved from
`https://taoclinicaltouch.com/wp-content/uploads/2026/10/` before any Buffer mutation. No
WordPress-generated resized derivative was used; every URL is a full-size original.

| Check | Result |
|---|---|
| HTTP 200 on anonymous retrieval | 25/25 |
| Dimensions — Feed 1080×1350 | 5/5 |
| Dimensions — Landscape 1200×628 | 5/5 |
| Dimensions — Story 1080×1920 | 15/15 |
| SHA-256 == canonical `issue015_verified_asset_manifest.csv` `output_sha256` | 25/25 |
| Filename day prefix matches scheduled date | 25/25 |

Per-asset bytes, dimensions and both checksums are recorded in `ISSUE015_MEDIA_STATE.json`. The
checksum rule from `BUFFER_V1_ADAPTER.md` — canonical repository SHA-256 == anonymously retrieved
SHA-256 — held for all 25 before attachment.

## Duplicate preflight

The Oct 12–16 scheduled window was queried across the full paginated organization queue before
mutation and contained **zero** objects. The pre-existing 29 scheduled posts were all Issue 014
(Oct 6–9) and were not read, altered, rescheduled, or deleted.

## Verification — object by object

A mutation response is not proof of scheduled state. Every one of the 45 channel posts was
retrieved independently by ID via `post(input:{id})` after creation, and the Oct 12–16 window was
re-queried as a second independent check.

| Check | Result |
|---|---|
| Content items in Oct 12–16 window | 25/25 |
| Channel posts independently read back by ID | 45/45 |
| Independent window query returns exactly the created set | 45/45, 0 extras, 0 missing |
| Status `scheduled` | 45/45 |
| `shareMode` `customScheduled` / `isCustomScheduled` true | 45/45 |
| `schedulingType` `automatic` | 45/45 |
| `contentItemId` matches parent content item | 45/45 |
| Scheduled time matches approved slot | 45/45 |
| Channel set matches approved destination | 45/45 |
| Exactly one image asset attached | 45/45 |
| Media URL matches day and role | 45/45 |
| Captions match approved copy verbatim | 45/45 |
| Facebook captions carry canonical URL | 5/5 |
| Instagram Feed captions use "link in bio" | 10/10 |
| Raw canonical URL in Instagram body copy | 0/40 |
| Instagram Feed `type=post`, `shouldShareToFeed=true` | 10/10 |
| Instagram Story `type=story`, `shouldShareToFeed=false` | 30/30 |
| Story 3/3 native canonical link persisted | 10/10 |
| Story 1/3 and 2/3 native link absent | 20/20 |
| Facebook `type=post` | 5/5 |
| Story content items with no caption | 15/15 |
| Facebook Stories present | 0 |
| Duplicate post IDs | 0 |
| Duplicate content item IDs | 0 |
| Duplicate (channel, time, media) combinations | 0 |
| Objects with mixed media | 0 |
| Channels disconnected or locked on readback | 0 |
| Buffer post errors, failed media imports, channel warnings | none |

**Field-level exceptions: 0.** 25 created, 0 failures, nothing fixed forward, no duplicate created
to repair a mismatch.

Machine-readable evidence: `ISSUE015_BUFFER_OBJECTS.json` (content item IDs, all 45 post IDs,
channels, times, media URLs, checksums, bytes, per-post readback state),
`ISSUE015_MEDIA_STATE.json` (anonymous retrieval state of all 25 assets).

## WordPress article state

| Field | Value |
|---|---|
| Post ID | 1877 |
| Title | *The Clinical Practice of Restraint* |
| Slug | `the-clinical-practice-of-restraint` |
| Status | `future` |
| Scheduled date | October 12, 2026 |
| Featured media | 1870 |
| Canonical URL | `https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-restraint/` |

Verified independently in this pass:

- Featured media 1870 resolves to `ISSUE015_MON_LANDSCAPE.png`, the Founder-approved Monday
  landscape, at the expected production path.
- The canonical URL returns **HTTP 404** to anonymous retrieval. This is expected
  pre-publication behavior, not a defect — WordPress serves scheduled posts to nobody and the
  REST API refuses `status=future` to unauthenticated callers (`rest_forbidden`, 401). Issues 013
  and 014 404'd identically while Founder-confirmed as scheduled. **Not a production blocker.**

### Site timezone trap — now structurally closed

The historical 7:45 ET / 11:45 UTC scheduling trap arose because the site ran on `gmt_offset: 0`.
Read-only verification in this pass returns:

```
timezone_string: America/New_York
gmt_offset:      -4
```

Confirmed against live data: media 1870 reports `date 2026-10-03T08:01:48` against
`date_gmt 2026-10-03T12:01:48` — a true −4 offset. Issue 014 parked housekeeping item 3 has been
completed. wp-admin now displays and accepts Eastern time directly, so a field reading `7:45`
means 7:45 AM ET. **The trap that fired on Issue 013 can no longer fire.** No change was made to
WordPress.

### Outstanding Founder verification — article hour

The handoff requires confirming the article's scheduled time is safely ahead of the 8:00 AM ET
social launch. **That verification could not be completed from this environment and is not
claimed.** No WordPress credential is present (`TAO_WP_APP_PASSWORD` unset), and the Issue 014
parked blocker — the `Authorization` header not reaching PHP on SiteGround — remains open, so
authenticated readback is unavailable; anonymous REST refuses `status=future`.

What is established: the handoff records an authenticated readback confirming `future`, scheduled
October 12, with body matching the Founder-approved canonical manuscript. What is unverified: the
literal hour and minute.

This affects only the article's own publication hour, never the Buffer queue, and it is the same
category of open item Issue 014 carried to PASS. **Founder action: confirm in wp-admin that post
1877 is scheduled before 8:00 AM ET on October 12, 2026.** Six days of margin remain.

## Confirmations

- Buffer was the only system mutated. WordPress, Brevo, and all media were read-only.
- Issue 014's objects (Oct 6–9) and every earlier issue were not touched. Organization queue now
  holds 74 scheduled posts: 29 Issue 014 remaining plus 45 Issue 015.
- No scheduled object was altered, rescheduled, or re-created after verification.
- No AI-generated or substituted copy entered any object; no asset was cropped, resized,
  regenerated, renamed, or recompressed.
- The Buffer credential was read from local config by name and length only. It was never printed,
  logged, committed, or passed in a process argument list.

## Parked / housekeeping

1. **Confirm post 1877's wp-admin scheduled time is before 8:00 AM ET**, per the section above.
   The only outstanding verification for Issue 015 Buffer.
2. **Caption hashtag divergence** — documented interpretation above; Founder review requested.
   Reversible without touching media or schedule.
3. **WordPress Application Password** — `Authorization` header still not reaching PHP. Carried
   forward from Issue 014 parked item 2. SiteGround support question.
4. **Site timezone** — Issue 014 parked item 3 is **closed**; the site is now `America/New_York`.
   Any Manual Bridge instruction still phrased in UTC should be restated in Eastern.
5. **Orphaned public files** — the superseded Issue 014 Friday Feed typo binary and the three
   Issue 013 unregistered Monday files remain public and unreferenced. Unchanged this pass.

## Issue 015 Buffer deployment: PASS

PASS is granted because all 25 content items and all 45 channel posts were read back from Buffer
independently of their mutation responses and reconciled field by field against the Founder-approved
directive with zero exceptions, all 25 media objects reconciled by checksum and dimension before
attachment, and an independent window query returned exactly the created set with no extras and
nothing missing.

**Brevo gate is now open.** The two outstanding items above are a Founder confirmation and a
documented copy interpretation; neither is a Buffer defect.
