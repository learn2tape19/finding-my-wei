# Issue 013 — Founder Manual Bridge

**Purpose:** the bounded manual handoff for WordPress. Everything else in Issue 013 production is
built and waiting on the URLs this produces.
**Publication window:** September 28 – October 2, 2026
**Status:** awaiting Founder execution

---

## Why this exists

WordPress REST Application Password authentication returns `rest_not_logged_in` for all
credentials — the `Authorization` header is not reaching PHP. That is parked as a separate issue
and is **not** a reason to stop the pipeline. Media upload and article creation move to you; every
other Issue 013 object is complete and verified.

---

## Part 1 — Upload 25 media files

**Source directory (all 25, repository root of the Issue 013 package):**

```
07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_013/
```

**wp-admin → Media → Add New.** Upload all 25. Do not rename, resize, crop, or re-save any file —
they are Founder-approved binaries and their SHA-256 hashes are the verification key.

| # | Day | Role | File | SHA-256 (first 16) | Use | Alt text |
|---:|---|---|---|---|---|---|
| 1 | Monday | FEED | `ISSUE-013_MONDAY_FEED_1080x1350.png` | `07f3b2b850c4c8c6` | Feed post — Facebook + Instagram | Treatment room with a woman leaving through an open door into daylight |
| 2 | Monday | LANDSCAPE | `ISSUE-013_MONDAY_LANDSCAPE_1200x628.png` | `f62f62c42c801631` | Blog featured image / OG / email header | Treatment room with a woman leaving through an open door into daylight |
| 3 | Monday | STORY-01 | `ISSUE-013_MONDAY_STORY-01_1080x1920.png` | `67340bb4d291786b` | Instagram Story 1 | Treatment room with a woman leaving through an open door into daylight |
| 4 | Monday | STORY-02 | `ISSUE-013_MONDAY_STORY-02_1080x1920.png` | `6167be6b79064520` | Instagram Story 2 | Treatment room with a woman leaving through an open door into daylight |
| 5 | Monday | STORY-03 | `ISSUE-013_MONDAY_STORY-03_1080x1920.png` | `392e79f88fe33b1f` | Instagram Story 3 | Treatment room with a woman leaving through an open door into daylight |
| 6 | Tuesday | FEED | `ISSUE-013_TUESDAY_FEED_1080x1350.png` | `a6ee4eb2c0aca231` | Feed post — Facebook + Instagram | Clinician and patient in a warm, naturally lit treatment setting |
| 7 | Tuesday | LANDSCAPE | `ISSUE-013_TUESDAY_LANDSCAPE_1200x628.png` | `137a489592fe0c19` | Blog featured image / OG / email header | Clinician and patient in a warm, naturally lit treatment setting |
| 8 | Tuesday | STORY-01 | `ISSUE-013_TUESDAY_STORY-01_1080x1920.png` | `e6872bbfe29f6701` | Instagram Story 1 | Clinician and patient in a warm, naturally lit treatment setting |
| 9 | Tuesday | STORY-02 | `ISSUE-013_TUESDAY_STORY-02_1080x1920.png` | `c243389778c0c35f` | Instagram Story 2 | Clinician and patient in a warm, naturally lit treatment setting |
| 10 | Tuesday | STORY-03 | `ISSUE-013_TUESDAY_STORY-03_1080x1920.png` | `48c90cb139ef6d4d` | Instagram Story 3 | Clinician and patient in a warm, naturally lit treatment setting |
| 11 | Wednesday | FEED | `ISSUE-013_WEDNESDAY_FEED_1080x1350.png` | `e250ef3cef6eab08` | Feed post — Facebook + Instagram | A quiet moment of pause in a clinical or everyday setting |
| 12 | Wednesday | LANDSCAPE | `ISSUE-013_WEDNESDAY_LANDSCAPE_1200x628.png` | `d9e3222ba57a9d59` | Blog featured image / OG / email header | A quiet moment of pause in a clinical or everyday setting |
| 13 | Wednesday | STORY-01 | `ISSUE-013_WEDNESDAY_STORY-01_1080x1920.png` | `876df337591c29eb` | Instagram Story 1 | A quiet moment of pause in a clinical or everyday setting |
| 14 | Wednesday | STORY-02 | `ISSUE-013_WEDNESDAY_STORY-02_1080x1920.png` | `129cb07cecb592fd` | Instagram Story 2 | A quiet moment of pause in a clinical or everyday setting |
| 15 | Wednesday | STORY-03 | `ISSUE-013_WEDNESDAY_STORY-03_1080x1920.png` | `3e00a9604ae07267` | Instagram Story 3 | A quiet moment of pause in a clinical or everyday setting |
| 16 | Thursday | FEED | `ISSUE-013_THURSDAY_FEED_1080x1350.png` | `045a4df5e235fe39` | Feed post — Facebook + Instagram | A woman moving easily through ordinary daily life outdoors |
| 17 | Thursday | LANDSCAPE | `ISSUE-013_THURSDAY_LANDSCAPE_1200x628.png` | `cbb8a260542e75e6` | Blog featured image / OG / email header | A woman moving easily through ordinary daily life outdoors |
| 18 | Thursday | STORY-01 | `ISSUE-013_THURSDAY_STORY-01_1080x1920.png` | `eccc2d0b0d64f46e` | Instagram Story 1 | A woman moving easily through ordinary daily life outdoors |
| 19 | Thursday | STORY-02 | `ISSUE-013_THURSDAY_STORY-02_1080x1920.png` | `d930834eb16b7f67` | Instagram Story 2 | A woman moving easily through ordinary daily life outdoors |
| 20 | Thursday | STORY-03 | `ISSUE-013_THURSDAY_STORY-03_1080x1920.png` | `91c251987c3277f2` | Instagram Story 3 | A woman moving easily through ordinary daily life outdoors |
| 21 | Friday | FEED | `ISSUE-013_FRIDAY_FEED_1080x1350.png` | `4b68062ffc91e187` | Feed post — Facebook + Instagram | Two women walking a dog together in warm late-day light |
| 22 | Friday | LANDSCAPE | `ISSUE-013_FRIDAY_LANDSCAPE_1200x628.png` | `1d9910c6a6b954f4` | Blog featured image / OG / email header | Two women walking a dog together in warm late-day light |
| 23 | Friday | STORY-01 | `ISSUE-013_FRIDAY_STORY-01_1080x1920.png` | `135148a00a510977` | Instagram Story 1 | Two women walking a dog together in warm late-day light |
| 24 | Friday | STORY-02 | `ISSUE-013_FRIDAY_STORY-02_1080x1920.png` | `f9b1a4bdf1fb842c` | Instagram Story 2 | Two women walking a dog together in warm late-day light |
| 25 | Friday | STORY-03 | `ISSUE-013_FRIDAY_STORY-03_1080x1920.png` | `c347920d59197ad5` | Instagram Story 3 | Two women walking a dog together in warm late-day light |
**Alt text** is grouped by day because all five assets of a day share the same photographic scene.
Adjust freely — these are descriptive defaults, not approved copy.

**Captions:** none required. Leave blank.

**Featured image:** `ISSUE-013_MONDAY_LANDSCAPE_1200x628.png` — set as the article's featured image.

---

## Part 2 — Create the article

| Field | Value |
|---|---|
| **Title** | `Continuity` |
| **Slug** | `the-session-is-not-the-finish-line` |
| **Permalink** | `https://taoclinicaltouch.com/blog/2026/09/the-session-is-not-the-finish-line/` |
| **Status** | **Scheduled** (`future`) — do not publish immediately |
| **Publish date/time** | **Monday, September 28, 2026 — 7:45 AM ET** |
| **Featured image** | Monday Landscape (above) |
| **Category / template** | match Issue 012 (`issue-012-agency`) exactly |

**Body content:** use `ISSUE013_CANONICAL_BLOG_ARTICLE.md` in this directory, from the
`# Continuity` heading down. Everything above it is provenance metadata and must not be published.

All 38 body paragraphs are verbatim from the approved gate, verified character-for-character.
Preserve the line breaks — they carry rhythm in this publication's style.

### SEO fields

| Field | Value |
|---|---|
| SEO title | `Continuity — The Tao of Clinical Touch, Issue 013` |
| Meta description | `A change observed is real. But a change observed is not yet a change integrated.` |
| Excerpt | `The session creates an opening. Life determines what happens next. Our role is to set the conditions for that possibility.` |

Meta description and excerpt are **verbatim approved Monday copy**. The SEO title follows the
Issue 012 pattern. Amend any of them freely — they are not locked.

---

## Part 3 — Return these to Claude

Once uploads and the article are saved, paste back:

**A. The 25 public media URLs.** Media → list view → each item's File URL. Format:

```
ISSUE-013_MONDAY_FEED_1080x1350.png      https://taoclinicaltouch.com/wp-content/uploads/2026/09/...
ISSUE-013_MONDAY_LANDSCAPE_1200x628.png  https://taoclinicaltouch.com/wp-content/uploads/2026/09/...
...
```

Filename plus URL, one per line. Order does not matter — they are matched by filename.

**B. The canonical article URL** — the permalink, and its post ID if visible.

**C. Confirmation** that the article is **scheduled**, not published, for Sept 28 7:45 AM ET.

---

## What happens the moment you return those

Automatically, no further authorization needed for the read-only steps:

1. **Retrieve all 25 URLs anonymously** and SHA-256 each against the canonical repository hash.
   Any mismatch is a STOP condition — it would mean WordPress transformed an approved master.
2. **Verify the article** — slug, title, scheduled status, timestamp, featured image, body copy
   against the canonical source.
3. **Build 25 Buffer objects** from `ISSUE013_SOCIAL_CAPTIONS.md` — captions, destinations,
   timestamps and metadata are already complete. *(Creation requires your authorization.)*
4. **Compose the Brevo campaign** to List 64 from `ISSUE013_EMAIL_COPY.md`. *(Requires your
   approval of subject and preheader first, plus the flagged connective line.)*
5. **Reconcile all 52 objects** against the publishing schedule and write the execution receipt.

---

## Still needing your decision, independent of WordPress

1. **Email subject and preheader** — no approved values exist for Issue 013. Proposals are in
   `ISSUE013_EMAIL_COPY.md`.
2. **One connective line** in the email body, flagged inline as not approved.
3. **Article register** — this issue's article is an assembly of approved copy, not Founder-authored
   prose like Issue 012. Publishable as-is; if you want it to match Issue 012's voice it needs
   connective writing only you can supply.
4. **List 64 size** — currently 2 confirmed subscribers. Whatever Campaign 42 converts before
   Monday is the Issue 013 readership. That is the permission architecture working as designed,
   but it is worth deciding deliberately rather than discovering on Monday.
