# Audit of originals and available results

**Snapshot: October 14, 2026.** Scope: all 19 current WordPress standard posts returned with `publish/future/draft`, corresponding content and featured-media metadata; Finding My Wei at HEAD `273535f9e6e45879c225048aa3177247df4e871d`; visible Buffer reporting for Sep 15–Oct 14; visible Brevo campaign listing page 1 (25 of 42, includes all visible July–October Tao issue sends); campaign 45 detail; GA4 Home and Pages and screens for the windows below. No platform writes or messages.

This is an issue/source/asset and available-results audit, not a retrospective claim that every historical social object or lifetime analytics record was recovered. Per-issue social metrics and historical GA4 attribution remain unestablished where not directly retrieved. Data gaps are not zeroes.

## Source hierarchy and discrepancies

Current WordPress post ID/status/title/link is the current publishing record. Repository sources establish issue lineage and approved-source history; old titles, proposed slugs and queue receipts do not override current live metadata. The publication ledger explicitly normalizes Week 01–04 as Issues 001–004, without renaming historical files. The editorial arc register still has old provisional Issue 007 statements; later receipts and live records take precedence.

- **Issue 001:** historical theme The Invisible Beginning. Five live July 6–10 posts exist, including the two foundational posts that the old arc register called planned gaps. Repository weekend articles Wu Wei in Clinical Practice and Integration and Next Steps have no matching post in the current standard-post inventory. Do not invent live URLs or roll them into a one-article original issue. The pilot's permission anchor is a deliberate editorial choice.
- **002:** original cycle and live article The Greet Is the First Clinical Intervention. The media filename “The Session Begins Before Touch” is not the live article title. Old ledger URL without year/month differs from the returned production link. Use the current link in `issue_inventory.csv`.
- **003:** cycle The Tao of Assessment: Perception Before Interpretation; live article What Are You Actually Assessing? WordPress supplies the recovered text; canonical BLOG source was missing in the historical ledger. The article includes duplicated wording about state and reaction. Log for review, preserve the original; do not silently copyedit during this pilot.
- **004:** cycle The Tao of Listening: Listening Before Explanation; live title Listening Before Explanation; WordPress date August 1, not the original planned Monday July 27. Historical production files do not replace the actual date.
- **005:** The Decision Before the Decision. Live post exists although the ledger's canonical BLOG source is missing. Preserve WordPress text as an evidence snapshot, not a newly approved replacement manuscript.
- **006:** theme Before Touch; live title The Work Before the Work. Historical theme, social Monday headline and live article are related but distinct fields.
- **007:** theme Permission Over Time; live title The Answer May Change Before It Is Spoken. Current published article resolves the older provisional arc, without rewriting its historical state.
- **008:** cycle The Plan Must Be Allowed to Change; live title Changing Course Is Clinical Reasoning. Published August 26. Brevo campaign 36 is sent, not merely queued as the original execution receipt recorded.
- **009:** Timing; proposed article The Clinical Intelligence of Timing. `ISSUE009_PUBLISHING_SCHEDULE.md` says blog HOLD because no approved full article exists. `PREFLIGHT_AND_EXECUTION_HOLD.md` records zero platform mutations in its preflight. No Issue 009 article appears among current WordPress posts. Treat article URL as **UNESTABLISHED**, not a guessed `/issue-009-timing/` link. The Issue 010 live introduction independently says no blog was published the prior week; this supports, but does not replace, the missing-post evidence.
- **010:** The Clinical Practice of Possibility, live `/blog/2026/09/issue-010-possibility/`.
- **011:** The Clinical Practice of Response, live `/blog/2026/09/issue-011-response/`.
- **012:** The Clinical Practice of Agency, live `/blog/2026/09/issue-012-agency/`; date Sep 21 11:45 in returned WP site-local field. Do not normalize all original posts to 7:45 AM.
- **013:** repository email calls article “The session is not the finish line.” and points to that historical slug; live title is The Clinical Practice of Continuity and current link ends `/the-clinical-practice-of-continuity/`. GA4 records traffic under multiple old paths/titles. Preserve current destination, inspect aliases before any future repair; no redirects changed.
- **014:** The Clinical Practice of Language, published Oct 5. Featured-media metadata says 1734×907 despite a landscape production role.
- **015:** The Clinical Practice of Restraint, published Oct 12; results are only two days old at audit.
- **016:** The Clinical Practice of Trust, WordPress ID 1924 **future**, Oct 19 07:45. API link is `https://taoclinicaltouch.com/?p=1924`, not proof of a published pretty permalink. The repository's planned pretty URL and any GA4 preview views do not establish live publication. Keep READY TO PUBLISH until anonymously verified after release.

Every current article's exact original title, current returned link, ID, site-local date and featured media appear in `issue_inventory.csv`. It includes five separate Issue 001 rows and a blank live URL for Issue 009. Full content and media snapshots are in `evidence/`.

## Existing assets and reuse readiness

The asset inventory records the existing campaign image files by original path, SHA-256 and bytes. It includes historical/archive material explicitly labeled as such, plus Issue 006's separate top-level PRODUCTION source family. It is a discovery index, not a blanket approval manifest. Old Friday/Monday filenames and export dimensions do not establish current permission or correct role.

Pilot featured images from current WordPress metadata:

| Original | WP media ID | Actual stored dimensions reported by WP | Original image name |
|---|---:|---|---|
| 001 permission anchor | 1239 | 1200×628 | Issue_001_The_Permission_Question.jpg |
| 002 | 1243 | 1200×628 | Issue_002_The_Session_Begins_Before_Touch.jpg |
| 003 | 1244 | 1200×628 | Issue_003_What_Are_You_Actually_Assessing.jpg |
| 004 | 1257 | 1200×628 | Issue_004_Listening_Before_Explanation.jpg |

Those sizes are metadata reads, not new independent pixel/visual QA or public-byte hash verification. Several other historical image names imply 1200×628 while metadata differs: 006 1734×907; 013 1733×907; 014 1734×907. Never infer dimensions from a filename. Do not regenerate or replace originals to repair these discrepancies during the pilot. New pilot assets need their own exact dimensions, visual approval, hashes and independent QA.

## Brevo: available campaign results

Direct source: authenticated campaign listing `https://app.brevo.com/campaigns/listing/email`, October 14. Values below are **UI labels as reported**, not deduplicated humans. Opens and clicks may include automation. “Recipients” is the listing's sent population; displayed percentages may use delivered denominators, which were not reconstructed.

| Issue / campaign | Send | Recipients label | Opens label | Clicks label | Displayed click rate | Unsubscribes |
|---|---|---:|---:|---:|---:|---:|
| 001 / 28, What actually creates clinical change? | Jul 7 | 11,661 | 744 | 68 | 0.59% | 33 |
| 002 / 31, The greet is the first intervention | Jul 16 | 6,796 | 682 | 28 | 0.42% | 23 |
| 003 / 32, What are you assessing? | Jul 23 | 11,540 | 360 | 31 | 0.27% | 14 |
| 003 related / 33, Learn2Tape variant | Jul 23 | 836 | 66 | 41 | 5.07% | 2 |
| 004–006 | No unambiguous corresponding send visible in inspected listing | — | — | — | — | — |
| 007 / 35 | Aug 20 | 11,510 | 5,499 | 38 | 0.33% | 9 |
| 008 / 36 | Aug 26 | 11,467 | 6,045 | 29 | 0.26% | 8 |
| 009 | No matching send visible; repository execution hold | — | — | — | — | — |
| 010 / 38 | Sep 7 | 11,443 | 17 | 42 | 0.38% | 51 |
| 011 / 40 | Sep 14 | 11,339 | 377 | 32 | 0.29% | 8 |
| Invitation / 42 | Sep 23 | 849 | 228 | 56 | 6.85% | 2 |
| 012 / 41 | Sep 23 | 4 | 3 | 0 | 0% | 0 |
| 013 / 43 | Sep 28 | 7 | 6 | 7 | 100% | 0 |
| 014 / 44 | Oct 5 | 7 | 6 | 7 | 100% | 0 |
| 015 / 45 | Oct 12 | 7 | 5 | 8 | 100% | 0 |
| 016 / 46 | Scheduled Oct 19 10 AM | Listing shows 0 before send; not an audience count | 0 pending | 0 pending | pending | pending |

Campaign 45 detailed overview explicitly reads **“Automated opens and clicks included.”** It confirms 7 delivered, 100% delivery, 5 opens, 8 clicks, displayed CTR 100%, 0 conversions, 0 unsubscribes, and list **#64 Tao subscriber list, 7 contacts**. Eight clicks are not eight unique people. Sender and reply-to are recorded in the plan.

The Home deliverability widget is account-wide (Learn2Tape workspace), score **31, Needs attention**, for Sep 14–Oct 13; do not attribute that entire score to the seven-person Tao list. Inspect campaign-level bounces, blocks, complaints, sender authentication and automation filtering before expanding reach. Do not mix the historic broad sends with the present opt-in cohort to claim improvement or decline. Invitation campaign clicks do not prove completed subscriptions.

## Buffer: current reporting snapshot

Direct sources: Insights and per-channel pages under `https://publish.buffer.com/insights/`. Window **Sep 15–Oct 14, 2026**, compared with Aug 16–Sep 14. It includes the partial current day and mixed posts, including Sidekick Air content on the Tao Facebook destination.

| Destination | Posts | Followers | Reactions | Comments | Reported engagement rate | Other observed metrics |
|---|---:|---:|---:|---:|---:|---|
| Tao Instagram | 85 | 95 (+4) | 26 | 0 | 10.93% | 926 views, 503 reach, 0 shares, 0 saves, 0 follows gained from posts |
| Drew Instagram | 67 | 368 (+3) | 56 | 0 | 5.29% | 2,491 views, 1,663 reach, 0 shares, 1 save, 0 follows gained from posts; mixed content |
| Tao Facebook | 34 | 103 (+2) | 14 | 3 | 3.24% | 925 impressions, 9 clicks, 4 shares |
| All connected channels | 186 | 566 (+9) | 96 | 3 | 6% | 4 shares |

Do not add follower counts to create a unique audience. Posts include Stories and other formats; engagement denominators differ by platform and must not be pooled. Facebook's top visible post (Sep 15 Sidekick Air/Denver) has 3 reactions, 3 comments, 59 impressions and 16.95% reported engagement. That means the channel's three comments cannot be credited to the weekly Tao series. A Sep 23 Agency post has 2 reactions, 0 comments, 113 impressions. Oct 12 Restraint has 1 reaction, 0 comments, 4 impressions at this early snapshot; 25% there is a tiny denominator, not evidence of a winning treatment.

Current queue sidebar shows 72 scheduled posts across channels (32 Drew IG, 32 Tao IG, 8 FB); these are existing queue counts, not new pilot objects or proof every schedule is correct. Resolve collisions and object-level readback before future execution. No posts or replies changed.

## GA4: what is and is not measured

Authenticated property **537759538**, account **394864671**, Tao of Clinical Touch / taoclinicaltouch.com. Pages and screens, **Sep 16–Oct 13, 2026**, all users, 100% available data indicator: **206 views, 17 active users, 563 events, 2m30s average engagement per active user, 0 key events, $0 reported revenue**. These are site-wide totals, not issue-reader counts. Home's Oct 7–13 window separately shows 8 active users, 48 views, 163 events, 0 key events.

Path-based rows for the 28-day window:

| Article/path | Views | Active users | Avg engagement / active user |
|---|---:|---:|---|
| 012 Agency, current path | 13 | 3 | 21s |
| 013 Continuity, current path | 6 | 3 | 1s |
| 011 Response, current path | 2 | 2 | 5s |
| 015 Restraint, current path | 2 | 1 | 0s |
| 016 Trust, future planned path | 2 | 1 | 0s |
| 014 Language, current path | 1 | 1 | 19s |
| `/blog/2026/09/issue-013-continuity/` | 1 | 1 | 18s |
| `/blog/2026/09/the-session-is-not-the-finish-line/` | 1 | 1 | 3s |

Issues 001–008 and 010 have no matching path row in this inspected window. That is not a lifetime zero or proof nobody read them. Issue 009's absence does not itself prove no historical traffic. Use a full-lifetime path export if a later decision requires it.

Measurement contamination is visible: `/signup-test/` has 9 views from 1 active user; title-based reporting contains template/preview titles; future Trust path appears before release; Home sources include `app.brevo.com`, `my.siteground.com` and Brevo tracking referrals. These support a concern about operator/test traffic and fragmented attribution, not identification of any specific visitor as Drew. Title-based rows differ from path-based rows; do not sum them together or equate titles with articles.

`/subscription-confirmed/` has 5 views, 3 active users in the 28-day report; those are page views/users, not three verified new subscribers. Confirmed list membership is the subscription source of truth. GA4 $0 and zero key events do not prove zero book sales. No purchase reconciliation, identity deduplication, consent completeness or event configuration verification occurred in this relaunch audit.

## Consequence for the pilot

The evidence supports a small, observable participation test and cleaner attribution. It does not support a blanket claim that sixteen fully delivered articles failed, nor a forecast that repetition will grow sales. Keep the four original links, use separate pilot UTMs, capture real replies and confirmed subscriptions, and evaluate the audience actually reached. The first four mappings are strong enough for draft production; release remains gated on the approvals and live QA listed in TRACKING_AND_QA.md.

## Front-end verification supplement

On October 14, the browser loaded all four pilot originals. Each displayed the expected H1 and a self-referencing canonical matching the preserved URL in the inventory. This browser was signed into WordPress as Drew, so this is authenticated front-end verification, not anonymous HTTP verification. The independent web reader could not access the four URLs. Anonymous status/canonical and tracking-query preservation remain release checks. The permission article displays one historical comment; it is not evidence of a deduplicated series-wide audience. No comment was posted or replied to. These audit page visits may create October 14 analytics activity and must not be counted as pilot engagement.
