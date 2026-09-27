# Issue 014 — Buffer Deployment Receipt

**Issue:** 014 — COMMUNICATION / The Clinical Practice of Language
**Publication week:** October 5 – 9, 2026
**Status:** **ALL 25 BUFFER OBJECTS SCHEDULED AND INDEPENDENTLY VERIFIED. NOTHING PUBLICLY VISIBLE YET.**
**Receipt date:** September 27, 2026
**Verdict:** **PASS**

Execution scope was Buffer deployment only, under Founder directive
*EXECUTION MODE: PRODUCTION ONLY / NO CREATIVE DISCRETION.* No headline, caption, visual,
cadence, or asset was authored, rewritten, or substituted by Claude.

---

## Final production state

| Layer | State as of receipt | Verified |
|---|---|---|
| WordPress media | 25 assets live, anonymous HTTPS | 25/25 HTTP 200, SHA-256 recorded |
| WordPress article | Canonical URL not yet publicly resolvable | See *Open dependency* below |
| Buffer | 25 content items / 45 channel posts, all `scheduled` | 25/25 read back by ID |
| Brevo | Campaign **44** `queued` — Oct 5, 2026 10:00 AM ET, List 64, Sender ID 3 | Read-only confirmation; untouched |
| **Publication objects** | **51** (25 Buffer + 25 media + 1 email) | |

Brevo Campaign 44 pre-existed this deployment and was neither created nor modified here.
Campaign 43 (Issue 013 — Continuity) remains `queued` for Sept 28, 2026 10:00 AM ET.

## Architecture — 25 content items / 45 channel deliveries

Buffer's `createPost` mutation accepts a **singular** `channelId`, so 25 multi-channel objects
cannot be expressed through it without creating duplicate objects. The correct construct is
**`createContentItem`**, which accepts `posts: [CreatePostInput!]!` and groups the per-channel
posts under one shared `contentItemId`.

The queue therefore holds **25 content items** — one per approved creative object — delivering
across **45 channel posts**. The 45 is a delivery count, not an object count. No duplicate
objects were created to reach multi-channel distribution.

## Channel distribution

| Channel | Channel posts |
|---|---:|
| Instagram — The Tao of Clinical Touch | 20 |
| Instagram — drewdog19 | 20 |
| Facebook — The Tao of Clinical Touch | 5 |
| **Total** | **45** |

| Role | Items | Destination |
|---|---:|---|
| Feed 1080×1380 | 5 | both Instagram accounts |
| Landscape 1200×628 | 5 | Facebook only |
| Story 1080×1920 | 15 | both Instagram accounts |

**Facebook Stories: 0.** Facebook receives the Landscape object only, as directed.

## Schedule — five objects per day, Oct 5–9, 2026

| Role | ET | UTC | Channel posts per day |
|---|---|---|---:|
| Feed + Landscape | 8:00 AM | 12:00Z | 3 |
| Story 1 of 3 | 9:00 AM | 13:00Z | 2 |
| Story 2 of 3 | 11:00 AM | 15:00Z | 2 |
| Story 3 of 3 | 1:00 PM | 17:00Z | 2 |

Five content items and nine channel posts on each of the five dates. UTC offset is EDT
(UTC−4); Oct 5–9 falls before the Nov 2 DST transition, so no slot drifts.

## Canonical URL

`https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-language/`

- Carried by **5/5** Facebook Landscape captions
- Carried as the **native Story link on all 10 Story 3/3 channel posts**
- Instagram Feed captions use **"link in bio"** — 10/10, no raw URL in Instagram body copy

## Corrected Friday Feed asset

The Founder-approved Friday Feed carried a masthead typo reading `FRIDAYY`. Under explicit
Founder authorization the glyph block was corrected **using only pixels sampled from the
artwork's own navy background strip** — no regeneration, no re-render, no font substitution,
no crop, resize, or recompression. 10,686 pixels changed, all inside the issue chip.

Production URL in use:

`https://taoclinicaltouch.com/wp-content/uploads/2026/09/FRIDAY_FEED_1080x1380-1.png`

| Field | Value |
|---|---|
| HTTP | 200, retrieved anonymously |
| Bytes | 1,965,546 |
| Dimensions | 1080 × 1380 |
| SHA-256 | `6896428d862b7633…` |
| OCR | `ISSUE 014 \| COMMUNICATION` / **`FRIDAY`** |

The superseded typo binary (SHA-256 `59ed1aa68bdaba2b…`, 1,941,638 bytes) still answers **HTTP 200**
at the original un-suffixed path despite attachment 1769 having been deleted from the Media
Library. It is referenced by **zero** Buffer objects and by no publication surface. Recorded as
an orphaned public file, same disposition as the Issue 013 Monday orphans: left untouched,
excluded programmatically, flagged for housekeeping.

## Story native-link verification

Buffer **does** support a native Instagram Story link. This was verified by readback, not by
submit-time acceptance:

```
type=story   shouldShareToFeed=false
link=https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-language/
```

4 of 4 Story 3/3 posts inspected returned the persisted link. No artwork was modified and no
workaround was invented to carry the link.

## Verification — object by object

All 25 content items were read back from Buffer after scheduling and reconciled against the
approved directive. **Zero exceptions.**

| Check | Result |
|---|---|
| Content items in Oct 5–9 window | 25/25 |
| Media attachment matches day and role | 25/25 |
| Filename day prefix matches scheduled date | 25/25 |
| Captions match approved copy verbatim | 25/25 |
| Scheduled time matches approved slot | 25/25 |
| Channel set matches approved destination | 25/25 |
| Facebook captions carry canonical URL | 5/5 |
| Instagram Feed captions use "link in bio" | 10/10 |
| Story objects carry no caption | 15/15 |
| Facebook Stories present | 0 |
| Duplicate post IDs | 0 |
| Duplicate (channel, time, media) combinations | 0 |
| Objects with mixed media | 0 |
| Status `scheduled` | 45/45 |
| Buffer warnings, failed media imports, channel exceptions | none |

All three channels were connected and unlocked throughout. 25 created, 0 failures.

Machine-readable evidence: `ISSUE014_BUFFER_OBJECTS.json` (content item IDs, post IDs,
channels, times, media, checksums), `ISSUE014_MEDIA_STATE.json` (anonymous retrieval state of
all 25 assets).

## Open dependency — canonical article not yet public

As of this receipt the canonical URL returns **HTTP 404** to anonymous retrieval. The Issue 013
article, Founder-confirmed as scheduled, returns 404 identically — so this is consistent with a
scheduled-but-unpublished post and does **not** by itself establish that the Issue 014 article
is absent. Authenticated WordPress REST access remains unavailable (see *Parked* below), so
scheduled-vs-absent cannot be distinguished from here.

**The URL must resolve before Oct 5, 12:00Z.** If it does not, 5 Facebook captions and 10 Story
links point at a 404 on the first publication morning. Requires Founder confirmation of the
article's status in WordPress.

## Confirmations

- No production system was modified by this receipt. Documentation only.
- No scheduled object was altered, rescheduled, or re-created after verification.
- No creative or scheduling variable was changed beyond the authorized Friday Feed correction.
- Issue 013's 25 Buffer objects (Sept 28 – Oct 2) were not touched. Org queue total: 70 scheduled posts.
- Monday Feed is Founder-confirmed intentional and was deployed as-is.
- No AI-generated replacement copy entered any object.

## Parked / housekeeping

1. **WordPress Application Password** — the `Authorization` header is not reaching PHP despite
   the `.htaccess` rewrite. SiteGround support question. Blocks authenticated media upload and
   authenticated post readback; the Manual Bridge remains the compensating control.
2. **Site timezone** — `gmt_offset: 0`. Change to `America/New_York` after Issue 013 closes,
   together with updating the Manual Bridge instruction to Eastern.
3. **Orphaned public files** — the superseded Friday Feed typo binary and the three Issue 013
   unregistered Monday files.

## Issue 014 Buffer deployment: PASS

PASS is granted on the basis that all 25 objects were read back from Buffer and verified
object by object with zero exceptions. It attests to the Buffer queue state only; the canonical
article dependency above is open and tracked.
