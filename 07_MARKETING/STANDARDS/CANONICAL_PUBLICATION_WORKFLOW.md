# Canonical Publication Workflow

**Version:** 1.0  
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
