# ISSUE 011 — PUBLISHING SCHEDULE
**Timezone:** America/New_York — EDT (UTC−04:00) throughout the publication week.

## Exact dates
- Monday — September 14, 2026
- Tuesday — September 15, 2026
- Wednesday — September 16, 2026
- Thursday — September 17, 2026
- Friday — September 18, 2026

Day-of-week verified against the 2026 calendar. Consecutive with the Issue 010 week (Sept 7–11).

## Publication calendar

### Monday — September 14
| ET | Object |
|---|---|
| 7:45 AM | Weekly article (WordPress) |
| 8:00 AM | Facebook + Instagram Feed |
| 9:00 AM | Instagram Story 1 |
| **10:00 AM** | **Issue-level Brevo email** |
| 11:00 AM | Instagram Story 2 |
| 1:00 PM | Instagram Story 3 |

### Tuesday September 15 – Friday September 18
| ET | Object |
|---|---|
| 8:00 AM | Facebook + Instagram Feed |
| 9:00 AM | Instagram Story 1 |
| 11:00 AM | Instagram Story 2 |
| 1:00 PM | Instagram Story 3 |

**Facebook Stories: NONE.**

The email sends 2h15m after the article publishes, so the CTA destination is live before any object references it.

## Channels
- Instagram — `taoclinicaltouch` — `6a3eb89f5ab6d2f106763ca0`
- Facebook Page — The Tao of Clinical Touch — `6a3eb95f5ab6d2f106763fc9`
- Buffer organization — Drew Freedman — `6a3d317b545b077504a4771b`

## Platform authority

**WordPress.** One canonical weekly article. The Monday Blog/OG visual is the weekly featured/OG authority.

**Brevo.** One issue-level email, Monday 10:00 AM ET, linking to the already-live weekly article. The Monday Email Header is the issue-level email visual authority.

**Buffer.** 5 Facebook feeds + 5 Instagram feeds + 15 Instagram Stories = **25 scheduled social objects.** No Facebook Stories.

**Tue–Fri Blog/OG and Email Header derivatives** may be retained in the standard 30-asset production inventory for archival consistency, but do **not** establish additional article or email execution authority.

## Object count
25 social objects + 1 weekly article + 1 issue-level email.

## Expected production inventory (Visual Production Gate)
30 assets: 5 Feed 1080×1350 · 15 Story 1080×1920 · 5 Email header 1200×627 · 5 Blog/OG 1200×628 — six per weekday.

## Execution method
Established Issue 010 architecture: stage assets to the WordPress media library → verify each public URL anonymously (HTTP 200 + byte-identical SHA-256 against the checksum authority) → duplicate-check the destination window → build reversible objects → verify each receipt before the next mutation → stop immediately on any failure → independently re-query at completion.

## Gate status

**Status: FOUNDER APPROVED — EDITORIALLY LOCKED**

| Gate | Status |
|---|---|
| Gate 0 — Editorial Architecture | **CLOSED / FOUNDER APPROVED** |
| Gate 1 — Editorial Completeness | **CLOSED / FOUNDER APPROVED** |
| Visual Production | **HOLD — NOT YET AUTHORIZED** |
| External Execution | **HOLD — NOT AUTHORIZED** |

**Gate 1 completeness:** 5/5 feed concepts and canonical captions · 15/15 Story frames · 1/1 weekly article · 1/1 issue-level email · subject, preheader, headline, CTA · SEO and metadata · canonical slug/permalink architecture · publication calendar · platform-role authority. Editorial completeness is closed before visual production begins.

**Visual Production — HOLD.** No artwork produced. Asset manifest, visual production brief, checksum authorities, `APPROVED_ASSETS/`, and `SOURCE_APPROVED/` are deliberately deferred to the Visual Production Gate.

**External Execution — HOLD.** No WordPress, Buffer, or Brevo objects. Nothing scheduled or published.

> **Founder approval is not publication authority.** Editorial approval, canonical persistence, visual approval, and publication are distinct gates. Do not collapse them. Carried forward from Issue 010.

## Slug vs production permalink
| | |
|---|---|
| Canonical editorial slug | `issue-011-response` |
| Proposed production permalink | `/blog/2026/09/issue-011-response/` |

The production site uses a `/blog/YYYY/MM/{slug}/` permalink architecture. A September 2026 publication resolves the proposed permalink consistently. Confirm against the live site at execution; do not alter the site's permalink architecture.
