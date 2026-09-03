# ISSUE 010 — ASSET MANIFEST

**Status:** ARCHITECTURE ONLY — no artwork generated, no assets produced.

Expected production set is 30 assets. Source originals will be retained in `SOURCE_APPROVED/`. Exact-dimension production derivatives belong in `APPROVED_ASSETS/`.

> **Directory note.** The canonical repository production directory is `APPROVED_ASSETS/`. Issue 009 carried a documentation drift where control files labelled this directory `ASSETS/`; that was corrected at archival. Issue 010 uses `APPROVED_ASSETS/` from the start, in prose and in the checksum authority path labels, so `shasum -c` validates natively from the packet root.

## Production specifications

| Surface | Dimensions | Count |
|---|---:|---:|
| Feed (Instagram + Facebook) | 1080×1350 | 5 |
| Blog / OG | 1200×628 | 5 |
| Email header | 1200×627 | 5 |
| Stories (3 per day) | 1080×1920 | 15 |
| **Total** | | **30** |

## Expected asset matrix

| Day | Asset | Production file | Production px |
|---|---|---|---:|
| MON | FEED | `ISSUE010_MON_FEED_1080x1350.png` | 1080×1350 |
| MON | BLOG | `ISSUE010_MON_BLOG_1200x628.png` | 1200×628 |
| MON | EMAIL | `ISSUE010_MON_EMAIL_1200x627.png` | 1200×627 |
| MON | STORY1 | `ISSUE010_MON_STORY1_1080x1920.png` | 1080×1920 |
| MON | STORY2 | `ISSUE010_MON_STORY2_1080x1920.png` | 1080×1920 |
| MON | STORY3 | `ISSUE010_MON_STORY3_1080x1920.png` | 1080×1920 |
| TUE | FEED | `ISSUE010_TUE_FEED_1080x1350.png` | 1080×1350 |
| TUE | BLOG | `ISSUE010_TUE_BLOG_1200x628.png` | 1200×628 |
| TUE | EMAIL | `ISSUE010_TUE_EMAIL_1200x627.png` | 1200×627 |
| TUE | STORY1 | `ISSUE010_TUE_STORY1_1080x1920.png` | 1080×1920 |
| TUE | STORY2 | `ISSUE010_TUE_STORY2_1080x1920.png` | 1080×1920 |
| TUE | STORY3 | `ISSUE010_TUE_STORY3_1080x1920.png` | 1080×1920 |
| WED | FEED | `ISSUE010_WED_FEED_1080x1350.png` | 1080×1350 |
| WED | BLOG | `ISSUE010_WED_BLOG_1200x628.png` | 1200×628 |
| WED | EMAIL | `ISSUE010_WED_EMAIL_1200x627.png` | 1200×627 |
| WED | STORY1 | `ISSUE010_WED_STORY1_1080x1920.png` | 1080×1920 |
| WED | STORY2 | `ISSUE010_WED_STORY2_1080x1920.png` | 1080×1920 |
| WED | STORY3 | `ISSUE010_WED_STORY3_1080x1920.png` | 1080×1920 |
| THU | FEED | `ISSUE010_THU_FEED_1080x1350.png` | 1080×1350 |
| THU | BLOG | `ISSUE010_THU_BLOG_1200x628.png` | 1200×628 |
| THU | EMAIL | `ISSUE010_THU_EMAIL_1200x627.png` | 1200×627 |
| THU | STORY1 | `ISSUE010_THU_STORY1_1080x1920.png` | 1080×1920 |
| THU | STORY2 | `ISSUE010_THU_STORY2_1080x1920.png` | 1080×1920 |
| THU | STORY3 | `ISSUE010_THU_STORY3_1080x1920.png` | 1080×1920 |
| FRI | FEED | `ISSUE010_FRI_FEED_1080x1350.png` | 1080×1350 |
| FRI | BLOG | `ISSUE010_FRI_BLOG_1200x628.png` | 1200×628 |
| FRI | EMAIL | `ISSUE010_FRI_EMAIL_1200x627.png` | 1200×627 |
| FRI | STORY1 | `ISSUE010_FRI_STORY1_1080x1920.png` | 1080×1920 |
| FRI | STORY2 | `ISSUE010_FRI_STORY2_1080x1920.png` | 1080×1920 |
| FRI | STORY3 | `ISSUE010_FRI_STORY3_1080x1920.png` | 1080×1920 |

## Source naming convention
`SOURCE_APPROVED/{DAY}_{SLOT}__{delivered-filename}.png` — carried forward from Issue 009. Source originals are retained unmodified; only the `APPROVED_ASSETS/` derivative is normalized to exact production pixels.

## Rules
- Every feed asset must carry the day's canonical Feed headline from `ISSUE010_MASTER_COPY.md`. Feed artwork is not built from Story copy.
- Story artwork must render the `ISSUE010_STORY_COPY_LOCK.md` text exactly, following the IDEA / TENSION / APPLICATION architecture.
- Do not crop, redraw, regenerate, substitute, recolor, or reinterpret an approved asset.
- Story 1/2/3 are discrete publishing objects for each weekday.
- Ripple rule: do not add or escalate droplets/splashes/ripples beyond the locked artwork.
- Brand doctrine per `ADOBE_BRAND_MANIFEST.md`: Deep Clinical Navy `#182633`, Antique Gold `#B8860B`, Charcoal `#3A3A3A`, Warm Ivory `#F7F4EE`; Cormorant Garamond editorial serif, Source Sans Pro supporting.
- Every image published to a platform requires objective accessibility alt text written from the actual rendered artwork.

## Verification gate (to run once assets exist)
30/30 present · 30/30 SHA-256 vs `ISSUE010_CHECKSUMS.sha256` · 30/30 exact dimensions · manifest ↔ authority agreement · source provenance for all 30.
