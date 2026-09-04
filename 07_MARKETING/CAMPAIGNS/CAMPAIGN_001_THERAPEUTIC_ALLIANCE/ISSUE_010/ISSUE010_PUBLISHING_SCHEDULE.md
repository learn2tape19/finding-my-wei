# ISSUE 010 — PUBLISHING SCHEDULE
**Timezone:** America/New_York (ET, DST-aware). Week of Sept 7–11, 2026 is EDT, UTC−04:00.

## Exact dates — FOUNDER LOCKED
- Monday — September 7, 2026
- Tuesday — September 8, 2026
- Wednesday — September 9, 2026
- Thursday — September 10, 2026
- Friday — September 11, 2026

Day-of-week verified against the 2026 calendar. Week is EDT (UTC−04:00) throughout.

Monday Sept 7 is Labor Day (US). Founder has ruled that the holiday **does not alter the publishing cadence**. Run the canonical schedule as specified. Do not reopen this.

## Daily cadence
- 8:00 AM — Instagram feed
- 8:00 AM — Facebook feed
- 9:00 AM — Story 1 (IDEA)
- 11:00 AM — Story 2 (TENSION)
- 1:00 PM — Story 3 (APPLICATION)

**No Facebook Stories.** Established Tao precedent: Facebook receives feed posts only; Stories are Instagram only.

## Channels
- Instagram — `taoclinicaltouch` — `6a3eb89f5ab6d2f106763ca0`
- Facebook Page — The Tao of Clinical Touch — `6a3eb95f5ab6d2f106763fc9`
- Buffer organization — Drew Freedman — `6a3d317b545b077504a4771b`

## Object count
25 social objects: 5 Facebook feed + 5 Instagram feed + 15 Instagram Stories.

## Asset mapping
- Feed → `ISSUE010_{DAY}_FEED_1080x1350.png`
- Story 1 → `ISSUE010_{DAY}_STORY1_1080x1920.png`
- Story 2 → `ISSUE010_{DAY}_STORY2_1080x1920.png`
- Story 3 → `ISSUE010_{DAY}_STORY3_1080x1920.png`
- Blog/OG → `ISSUE010_{DAY}_BLOG_1200x628.png`
- Email header → `ISSUE010_{DAY}_EMAIL_1200x627.png`

## Execution method
Established Tuesday/Wednesday Issue 009 architecture: stage assets to WordPress media library → verify public URL anonymously (HTTP 200 + byte-identical SHA-256) → duplicate-check the destination window → create Buffer objects sequentially with `customScheduled` + `schedulingType: automatic` → verify each receipt via `get_post` before the next mutation → stop immediately on any failure → independently re-query at completion.

## Execution status
**ARCHITECTURE ONLY.** No assets produced. No WordPress staging. No Buffer objects. Nothing scheduled.

## Blog and Email status

**Blog body: NO LONGER HOLD.** The canonical article is Founder-approved and persisted verbatim at `ISSUE010_CANONICAL_BLOG_ARTICLE.md` — title *The Clinical Practice of Possibility*, canonical editorial slug `issue-010-possibility`.

**Production article URL authority:** `https://taoclinicaltouch.com/blog/2026/09/issue-010-possibility/` (site uses `/blog/YYYY/MM/{slug}/`). This is the CTA destination for all Issue 010 downstream execution. Featured/OG visual: `ISSUE010_MON_BLOG_OG_1200x628.png`. Email header: `ISSUE010_MON_EMAIL_HEADER_1200x627.png`. See `ISSUE010_ASSET_MANIFEST.md` for the full Founder resolution.

**Blog publication: NOT AUTHORIZED.** Publication remains a separate Founder gate. WordPress is out of scope.

**Email body: NO LONGER HOLD.** The canonical email is Founder-approved and persisted verbatim at `ISSUE010_EMAIL_COPY.md` — subject, preheader, headline, and CTA all Founder-supplied.

**Email campaign creation and scheduling: NOT AUTHORIZED.** Remains a separate Founder gate. Brevo is out of scope; list IDs and send pattern are still not established.

Editorial completeness is not publication authority. WordPress, Buffer, and Brevo all remain out of scope at this gate.
