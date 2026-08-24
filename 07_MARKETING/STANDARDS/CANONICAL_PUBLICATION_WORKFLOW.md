# Canonical Publication Workflow

**Version:** 1.1  
**Effective Date:** July 8, 2026  
**Scope:** All campaigns, brands, and Project Atlas publications  
**Governance:** This is an institutional standard. All future campaigns inherit this workflow.

---

## Core Principle

**The blog is the canonical publication. Every other channel is an adaptation for its audience and format.**

Social media is not rewritten from scratch. It is deliberately extracted from the published article, preserving the core idea while respecting platform constraints and audience expectations.

---

## Production Workflow

```
QUESTION / HYPOTHESIS
        ↓
Research
        ↓
Editorial Brief
        ↓
BLOG ARTICLE (Canonical Publication)
        ↓
──────────────────────────────────────────────
Editorial Extraction Layer
        ↓
Facebook
Instagram
Instagram Story
LinkedIn
Threads
Email
        ↓
Creative Production Layer
        ↓
Firefly Prompt
Adobe Express Layout
Images
Graphics
        ↓
Deployment Layer
        ↓
Buffer
Brevo
Website
Analytics
Archive
```

---

## Phase 1: Research & Editorial Brief

**Deliverable:** `EDITORIAL.md`

Document:
- Research question or hypothesis
- Key sources or references
- Angle/perspective
- Target audience
- Core argument (3–5 key points)
- Tone and voice guidelines
- Word count target
- Deadline

---

## Phase 2: Canonical Blog Article

**Deliverable:** `BLOG/[DAY].md`

Requirements:
- 700–1,200 words (unless otherwise specified)
- Opening hook or clinical vignette
- Core argument developed with evidence/examples
- Practical takeaway or challenge
- Call to action
- All sources attributed
- Ready for direct WordPress publication

**This is the source. Everything else traces back here.**

---

## Phase 3: Editorial Extraction Layer

**Deliverable:** `EDITORIAL_EXTRACTION.md`

Before creating any platform-specific content, explicitly identify:

### Structural Elements
- **Strongest opening hook** — The first 1–2 sentences that work on every platform
- **Key insight** — The central idea that must survive every adaptation
- **Best quote** — A 1–2 sentence quote (from article or attributed source) that stands alone
- **Practical takeaway** — The actionable element readers can implement
- **Call to action** — What should the reader do next?
- **Visual metaphor** — An image concept that embodies the core idea

### SEO & Discovery
- **Focus keyword** — Primary search term this article targets
- **Secondary keywords** — 3–5 related keywords
- **Internal links** — Previous articles to reference (strengthens SEO + keeps readers in ecosystem)
- **External references** — Credible sources to cite (builds authority)

### Platform Optimization
- **Facebook hook** — What makes someone stop scrolling? (different from blog opening)
- **Instagram hook** — What works in Stories and feed? (visual-first thinking)
- **LinkedIn angle** — How does this connect to professional growth?
- **Email subject line** — What gets opens?
- **Threads angle** — How does this work as a threaded conversation?

---

## Phase 4: Social Extraction (Platform-Specific Adaptation)

**Deliverables:** 
- `SOCIAL/[DAY]/facebook.md`
- `SOCIAL/[DAY]/instagram.md`
- `SOCIAL/[DAY]/instagram_story.md`
- `SOCIAL/[DAY]/linkedin.md`
- `SOCIAL/[DAY]/threads.md`
- `SOCIAL/[DAY]/email.md`

Each platform gets:

### Facebook
- Opening hook (different from blog)
- 2–3 key insights (excerpt format, not full copy)
- Call to action
- Link to full article
- 3–5 primary hashtags

### Instagram
- Primary caption (150–200 chars, mobile-first)
- 5–6 carousel slides (each with distinct insight)
- Call to action
- 8–10 hashtags (rotated daily)
- Story copy (text overlay)
- Story sticker/poll (engagement)

### Instagram Story
- Hook text (3–5 words)
- Core insight (brief visual text)
- Call to action (link or text prompt)

### LinkedIn
- Professional framing (connect to workplace, growth, clinical excellence)
- Excerpt (300–400 chars)
- Thought leadership angle
- Call to action
- 3–5 professional hashtags

### Threads
- Thread concept (thread the article's main points as 3–6 connected posts)
- Opening post (hook)
- Supporting posts (each with one insight)
- Closing post (call to action)

### Email
- Subject line (40–50 chars, curiosity-driven)
- Preview text (55 chars, reinforces subject)
- Opening hook (different from blog)
- Teaser (first 2–3 paragraphs or key insight)
- Call to action (link to blog)
- Unsubscribe footer

**Rule:** No platform copy is written without reference to the Editorial Extraction document. All copy is adapted, not created independently.

---

## Phase 5: SEO Package

**Deliverable:** `WEBSITE/seo.md`

Every article includes:

```yaml
seo_title: "Exact H1 for article (50–60 chars)"
meta_description: "What shows in search results (155–160 chars)"
url_slug: "/url-slug-format/"
focus_keyword: "primary search term"
secondary_keywords:
  - "related term 1"
  - "related term 2"
  - "related term 3"
excerpt: "Brief summary for archive/category pages (155 chars)"
featured_image_alt: "Descriptive alt text (125 chars, includes keyword)"
internal_links:
  - url: "/previous-article-url/"
    anchor: "Anchor text that makes sense contextually"
  - url: "/related-article-url/"
    anchor: "Anchor text"
external_references:
  - title: "Source Name"
    url: "https://..."
  - title: "Source Name"
    url: "https://..."
categories:
  - "Primary Category"
tags:
  - "tag-1"
  - "tag-2"
  - "tag-3"
schema_type: "Article"
publish_date: "YYYY-MM-DD"
publish_time: "HH:00 ET"
```

**This makes WordPress publishing automatic.** No guessing, no forgotten fields.

---

## Phase 6: Website Package

**Deliverable:** `WEBSITE/` folder

```
WEBSITE/
├── article.md              (the published blog article)
├── seo.md                  (SEO metadata + WordPress specs)
├── featured_image.md       (image specifications)
└── schema.md               (structured data for rich snippets)
```

### featured_image.md
```yaml
filename: "descriptive-filename.jpg"
dimensions: "1200x628px (Facebook), 1080x1350px (Instagram)"
source: "Firefly-generated / Owned asset / External"
alt_text: "Descriptive alt text (125 chars, includes keyword)"
caption: "Optional caption for image"
credit: "Attribution if required"
```

### schema.md
```yaml
schema_type: "Article"
headline: "Article Title"
description: "Brief description"
author: "Drew Freedman"
datePublished: "YYYY-MM-DDT00:00:00Z"
dateModified: "YYYY-MM-DDT00:00:00Z"
image: "URL to featured image"
keywords: "keyword1, keyword2, keyword3"
```

---

## Phase 7: Creative Production Layer

**Deliverable:** `CREATIVE/[DAY]/` folder

### Creative Brief
```
CREATIVE_BRIEF.md
├── Hero Image Concept
├── Carousel Concepts
├── Story Concept
├── Pull Quote Graphic
├── Thumbnail
├── Adobe Express Specifications
├── Brand Colors
├── Typography
└── Accessibility Considerations
```

### Hero Image Concept
- **Firefly Prompt** — Generated from article's visual metaphor
- **Negative Prompt** — What to avoid (brand-specific exclusions)
- **Specifications** — Size, format, color palette
- **Accessibility** — Contrast ratio, alt text requirements

### Carousel Concepts (Instagram)
- Slide 1: Opening hook
- Slide 2–5: One insight per slide (copy + visual direction)
- Slide 6: Call to action

Each slide specifies:
- Text (the extracted insight)
- Visual direction (what should the design communicate?)
- Color/typography (derived from brand standards)
- Contrast ratio (WCAG AA minimum)

### Story Concept
- Hook (3–5 words)
- Core insight
- Call to action
- Brand color + typography specifications

### Pull Quote Graphic
- Quote extracted from article
- Designer guidelines (font, color, background)
- Size options (Story 1080x1920, Feed 1080x1350, Carousel slide)
- Accessibility (contrast, readability on small screens)

### Adobe Express Specifications
```yaml
template: "Social Media Post / Story / Carousel"
dimensions: "1080x1350px (Instagram) / 1080x1920px (Story)"
color_palette: "Extracted from Tao Visual Language"
typography: 
  headline: "Font, size, weight"
  body: "Font, size, weight"
brand_elements: "Logo placement, brand mark, color"
layout_notes: "Specific positioning, hierarchy, whitespace"
accessibility: "Minimum contrast ratios, readable font sizes"
```

### Accessibility Considerations
- Text contrast minimum WCAG AA (4.5:1 for small text, 3:1 for large)
- Alt text for all images (descriptive, includes keyword when relevant)
- Font sizes minimum 12px for body text
- Color should not be the only way to convey information
- Consider colorblind-safe palettes

---

## Phase 7A: Production Completeness Gate

**Deliverable:** a passing run of `07_MARKETING/STANDARDS/verify_production_completeness.py`

Phase 7 produces creative. Phase 7A proves the production is actually complete and
actually persisted before Phase 8 deploys anything. No issue or production day may be
declared complete until this Gate closes.

**Origin:** Issue 008. Canonical assets were correctly produced, Founder-approved, and
hash-verified locally, then reported as complete while remaining absent from the remote
canonical repository. Local existence was mistaken for institutional completeness.

### Asset Persistence Rule

An asset is not institutionally complete because it exists on a workstation. Every
required asset must reach all eight states:

```
Produced → Founder Approved → Canonically Named → Manifested
        → Hash Verified → Committed → Pushed → Remote Verified
```

A local-only approved asset is an **incomplete production state**. For any multi-asset
deliverable, every member of the set must complete all eight states independently.

### Core Roles

Every Monday–Friday production day must account for the standard core asset roles:

| Role | Dimensions | Purpose |
|---|---|---|
| `FEED` | 1080×1350 | Instagram / Facebook feed |
| `STORY` | 1080×1920 | Story (see sequence rule below) |
| `BLOGOG` | 1200×628 | Blog / social-link header |
| `EMAILHEADER` | 1200×627 | Email-header role |

The 1200×627 email-header role is **required for every production day**, including days
with no scheduled Brevo campaign. Wednesday remains the normal email publication day
unless Founder direction changes. **Email scheduling and asset completeness are separate
concerns** — a day does not lose its email-header requirement because nothing is being
sent that day.

### Conditional Roles

Required only when the approved production plan calls for them:

- multi-frame Story sequences beyond a single frame
- Instagram carousels
- additional campaign-specific graphics
- event or promotional variants
- other Founder-approved derivative assets

Once a conditional role is specified or approved for a production, **it is required for
that production**. It cannot later drop out of the Gate on the grounds that it is not
part of every week's standard set.

### Stories Are Sequences, Not Single Files

`1080×1920 Story` does not mean one asset. Therapeutic Alliance regularly runs multi-frame
Story sequences of one, two, three, four, or more frames. **The production brief and
manifest determine the expected frame count for that day.**

If a day calls for three frames, completeness requires Story 1 **and** Story 2 **and**
Story 3. Finding one valid 1080×1920 file does not satisfy the Story Gate.

Story assets use deterministic sequence naming so order cannot become ambiguous — for
example `..._STORY_01_1080x1920` or the established `..._STORY_FRAME01_1080x1920`.
**Preserve existing canonical naming where already established; do not rename approved
historical assets to fit a newer convention.**

### Carousels Are Sets

Instagram carousel production is a set, not an individual feed asset. When a carousel is
specified, the brief and manifest declare the expected number and order of slides
(e.g. `Carousel — 5 slides`), and completeness requires every slide.

A carousel fails the Gate if a slide is missing, slide order is ambiguous, any slide is
unapproved, any slide is absent from the manifest, any approved slide remains local-only,
or remote persistence cannot be verified.

**Do not treat a carousel as a feed asset because its slides share the 1080×1350
dimension. Asset dimensions do not define a production role. The manifest defines the
role.**

### Manifest as Expected-State Authority

The manifest is not a post-hoc record of what was produced. It is the authority on what is
*supposed to exist*, so the Gate can compare expected state against actual state.

Each day's `ASSET_MANIFEST.md` carries an `## Expected Production Set` table:

```
| Role | Dimensions | Expected | Sequence |
|---|---|---|---|
| FEED | 1080x1350 | 1 | no |
| BLOGOG | 1200x628 | 1 | no |
| EMAILHEADER | 1200x627 | 1 | no |
| STORY | 1080x1920 | 3 | yes |
| CAROUSEL | 1080x1350 | 5 | yes |
```

followed by the approved-asset rows (filename, role, dimensions, SHA-256). Together these
let the Gate evaluate, per role:

```
ROLE → EXPECTED COUNT → ACTUAL COUNT → APPROVED → HASH VERIFIED → REMOTE VERIFIED
```

Manifests without an expected-set table are still checked, with expected counts derived
from the declared rows; the Gate reports when it is operating in derived mode. A simple
dimension check is never sufficient.

### The Gate — fifteen checks

Before an issue or day is declared complete:

1. All expected asset roles are known.
2. Expected asset count for each role is known.
3. All expected files exist.
4. Multi-frame Stories contain every required frame.
5. Carousels contain every required slide.
6. Sequence order is deterministic.
7. Filenames follow canonical convention.
8. Files reside under the correct `APPROVED_ASSETS/<DAY>/` location.
9. Every required asset appears in the manifest.
10. Hash verification passes.
11. Every asset is tracked by Git.
12. A commit containing each asset exists.
13. That commit has been pushed.
14. Every asset is remotely retrievable.
15. Local HEAD and remote HEAD agree at final handoff.

**If any required asset — or any member of a multi-asset set — remains local-only or
missing, THE PRODUCTION GATE REMAINS OPEN.**

Completeness is never inferred from the existence of a ZIP, a production packet, a
Downloads folder, or a local working-tree file.

### Running the check

```
git fetch origin main
python3 07_MARKETING/STANDARDS/verify_production_completeness.py \
    07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_0XX
```

Exit `0` = gate closed. Exit `1` = gate open, with every failure named. The check fails
loudly whenever expected state and actual state differ.

### Extension Point — Emerging Platform Roles

The role table above is deliberately extensible. Recognized future channels include
**Reels, TikTok, Threads**, and other short-form/video/social formats.

These are **not current Gate requirements**. No specifications, cadence, dimensions,
naming conventions, or publishing workflows are invented for them here. When Founder
direction defines their production doctrine, they are added as core or conditional roles
in this section and in the checker's role table — without redesigning the surrounding
architecture.

### Issue-Level Handoff Standard

Every issue-completion receipt reports:

| Field | Values |
|---|---|
| Core asset completeness | PASS / FAIL |
| Story sequence completeness | PASS / FAIL / N/A |
| Carousel completeness | PASS / FAIL / N/A |
| Conditional asset completeness | PASS / FAIL / N/A |
| Manifest / hash verification | PASS / FAIL |
| Git tracking | PASS / FAIL |
| Remote persistence | PASS / FAIL |
| Working tree | CLEAN / DIRTY |
| Local/remote HEAD parity | PASS / FAIL |
| Final SHA | `<sha>` |

Multi-asset productions also report expected versus actual counts, for example
`Wednesday Stories: 3 expected / 3 verified` and `Tuesday Carousel: 5 expected / 5
verified`.

**Do not report an issue as production-complete unless every applicable Gate passes.**

---

## Phase 8: Deployment Layer

**Deliverable:** `DEPLOYMENT/` folder

```
DEPLOYMENT/
├── WEBSITE.md
├── BUFFER.md
├── BREVO.md
├── FACEBOOK.md
├── INSTAGRAM.md
├── LINKEDIN.md
├── THREADS.md
├── ANALYTICS.md
└── CHECKLIST.md
```

### WEBSITE.md
- WordPress publishing steps
- Publish date/time
- Featured image upload specifications
- Category & tag assignment
- Internal link anchor text verification
- SEO preview check
- Publish confirmation

### BUFFER.md
- Instagram scheduling time (7:00 AM ET)
- Instagram copy (caption + hashtags)
- Instagram media (image/carousel)
- Facebook scheduling time (8:00 AM ET)
- Facebook copy
- Facebook media
- LinkedIn scheduling time (8:30 AM ET)
- LinkedIn copy
- LinkedIn media

### BREVO.md
- Email teaser content
- Subject line
- Preview text
- Scheduling date/time
- Segmentation (if applicable)
- Unsubscribe link verification

### FACEBOOK.md
- Post copy
- Image specifications
- Scheduling time
- Ad boost recommendation (Y/N)
- Comment moderation guidelines

### INSTAGRAM.md
- Post copy
- Image/carousel specifications
- Story copy + timing
- Story sticker/poll
- Engagement expectations (comments to reply to)

### LINKEDIN.md
- Post copy
- Media specifications
- Engagement strategy (expected comment types, reply approach)

### THREADS.md
- Thread posts (in order)
- Images/media per post
- Engagement CTA

### ANALYTICS.md
- Key metrics to track (impressions, engagement rate, click-through, conversions)
- Tools (Buffer, Meta Business Suite, Google Analytics)
- Reporting date (when to review)
- Success benchmarks (what constitutes a successful post?)

### CHECKLIST.md
```
Publication Checklist — [Article Title]

WEBSITE
  [ ] WordPress article published
  [ ] Featured image uploaded + alt text verified
  [ ] SEO title/meta description present
  [ ] Internal links added (minimum 2)
  [ ] Categories assigned
  [ ] Tags assigned
  [ ] URL slug correct
  [ ] Mobile preview checked
  [ ] Links verified (no broken links)

PRODUCTION COMPLETENESS GATE (Phase 7A — required before any deployment)
  [ ] verify_production_completeness.py exits 0 for this issue
  [ ] Story/carousel expected vs actual counts recorded
  [ ] Local HEAD == remote HEAD; working tree clean

BUFFER
  [ ] Instagram post scheduled (7:00 AM ET)
  [ ] Instagram carousel ready (6 slides)
  [ ] Instagram story scheduled
  [ ] Facebook post scheduled (8:00 AM ET)
  [ ] LinkedIn post scheduled (8:30 AM ET)
  [ ] All hashtags verified

BREVO
  [ ] Email teaser drafted
  [ ] Subject line (40–50 chars) verified
  [ ] Preview text verified
  [ ] Scheduling time set
  [ ] Unsubscribe link working

CREATIVE
  [ ] Firefly images generated
  [ ] Adobe Express layouts completed
  [ ] Carousel images created
  [ ] Story images created
  [ ] All images have alt text
  [ ] Contrast ratios verified (WCAG AA)

ANALYTICS
  [ ] Google Analytics goals set for article
  [ ] Facebook pixel firing on article page
  [ ] UTM parameters in social links (utm_campaign, utm_source, utm_medium)
  [ ] Buffer tracking enabled
  [ ] Baseline metrics documented

FINAL VERIFICATION
  [ ] All copy reviewed for brand voice
  [ ] All links tested
  [ ] All images optimized for web
  [ ] Mobile preview of all platforms checked
  [ ] Spelling/grammar check complete
  [ ] Call-to-action is clear on every platform
  [ ] Timing verified (no publishing during outages/blackouts)
  [ ] Archive: All files organized in campaign folder structure
```

---

## Folder Structure

Every campaign using this workflow should organize files as:

```
CAMPAIGN_[NAME]/
├── RESEARCH/
│   └── [Research notes, competitor analysis, source materials]
│
├── EDITORIAL/
│   └── WEEK_0X/
│       ├── MONDAY.md (editorial brief)
│       ├── TUESDAY.md (editorial brief)
│       ├── [etc.]
│
├── BLOG/
│   └── WEEK_0X/
│       ├── MONDAY.md (canonical article)
│       ├── TUESDAY.md (canonical article)
│       ├── WEDNESDAY.md (canonical article)
│       ├── THURSDAY.md (canonical article)
│       ├── FRIDAY.md (canonical article)
│       ├── SATURDAY.md (canonical article)
│       └── SUNDAY.md (canonical article)
│
├── SOCIAL/
│   └── WEEK_0X/
│       ├── MONDAY/
│       │   ├── EDITORIAL_EXTRACTION.md
│       │   ├── facebook.md
│       │   ├── instagram.md
│       │   ├── instagram_story.md
│       │   ├── linkedin.md
│       │   └── email.md
│       ├── THURSDAY/
│       │   └── [same structure]
│
├── WEBSITE/
│   └── WEEK_0X/
│       ├── MONDAY/
│       │   ├── seo.md
│       │   ├── featured_image.md
│       │   └── schema.md
│       ├── THURSDAY/
│       │   └── [same structure]
│
├── CREATIVE/
│   └── WEEK_0X/
│       ├── MONDAY/
│       │   ├── CREATIVE_BRIEF.md
│       │   ├── firefly_prompt.md
│       │   ├── adobe_express_specs.md
│       │   └── accessibility.md
│       ├── THURSDAY/
│       │   └── [same structure]
│
├── DEPLOYMENT/
│   └── WEEK_0X/
│       ├── MONDAY/
│       │   ├── CHECKLIST.md
│       │   ├── WEBSITE.md
│       │   ├── BUFFER.md
│       │   ├── BREVO.md
│       │   ├── FACEBOOK.md
│       │   ├── INSTAGRAM.md
│       │   ├── LINKEDIN.md
│       │   └── ANALYTICS.md
│       ├── THURSDAY/
│       │   └── [same structure]
│
└── ARCHIVE/
    └── [Published/completed articles, performance reports]
```

---

## Governance

**This workflow is mandatory for:**
- Campaign 001: Therapeutic Alliance (Project Atlas)
- The Tao of Clinical Touch (book marketing)
- Learn2Tape campaigns
- Sidekick Air / StitchCore communications
- AREA Salon Studios (when launched)
- All future Project Atlas publications

**Responsibilities:**
- Editorial: Ensures article quality, research accuracy, audience fit
- Creative: Ensures visual consistency, brand alignment, accessibility
- Deployment: Ensures all channels receive content, analytics track results

**Review Schedule:**
- Week 1 of every campaign: Full workflow review, adjustments as needed
- Monthly: Campaign performance review against benchmarks
- Quarterly: Workflow optimization, process improvements

---

## Principles

1. **The blog is permanent.** Social media is temporary. Archive the article; repurpose the insight.
2. **Extraction before adaptation.** Never write platform-specific copy without an Editorial Extraction document.
3. **Traceability.** Every social post, email, and graphic should reference the article it came from.
4. **Consistency over novelty.** Same idea across channels reinforces authority and recall.
5. **Ownership first.** Your website is your asset. Social platforms are distribution channels.
6. **SEO compounds.** A well-optimized article continues to drive traffic years later.
7. **Accessibility is non-negotiable.** Every image needs alt text. Every design needs WCAG AA contrast.

---

**Version History:**
- v1.0 — July 8, 2026 — Initial institutional standard, derived from Campaign 001 best practices
- v1.1 — August 21, 2026 — Added Phase 7A: Production Completeness Gate. Establishes the
  eight-state asset persistence rule, core vs. conditional roles, Story-sequence and
  carousel set completeness, manifest-as-expected-state, the fifteen-check Gate, the
  Reels/TikTok/Threads extension point, and the issue-level handoff reporting standard.
  Origin: Issue 008 local-only asset persistence gap.
