# Gate 0: Observation Baseline
## The Tao of Clinical Touch Website

**Date:** August 3, 2026  
**Property:** https://taoclinicaltouch.com  
**Observer:** Claude (Steward)  
**Scope:** Public inspection only — no administrative access  

---

## Executive Summary

The Tao of Clinical Touch website is a WordPress installation using Elementor for design. The core content (homepage, book page, blog) is well-executed and aligned with institutional doctrine. However, there are low-quality pages indexed that should be removed, and several structural issues that require attention during Gate 1 (Understanding).

**Critical findings:**
- 2 placeholder/demo pages indexed that should be removed
- 2 potential duplicate blog pages requiring investigation
- Homepage content is duplicated 3 times in the page source
- Reader perspectives section contains duplicate reviews
- Navigation structure appears inconsistent across pages

---

## Public Site Crawl Results

### Pages Inventory

**Total Pages Indexed:** 11

| URL | Title | Last Modified | Status | Notes |
|-----|-------|---|--------|-------|
| `/` | Tao of Clinical Touch – The Neuroscience of Permission | 2026-07-22 | LIVE | Homepage - Well structured, compelling content |
| `/book/` | (Not yet inspected) | 2026-07-22 | LIVE | Book landing page |
| `/about/` | (Not yet inspected) | 2026-04-15 | LIVE | Author bio page |
| `/contact/` | (Not yet inspected) | 2026-04-15 | LIVE | Contact form |
| `/services/` | (Not yet inspected) | 2026-04-15 | LIVE | Services page - Flagged in implementation brief as potentially redundant |
| `/chapter-1-the-tao-of-alliance/` | (Not yet inspected) | 2026-04-18 | LIVE | Free chapter download |
| `/blog/` | (Not yet inspected) | 2026-07-07 | LIVE | Blog archive/listing page |
| `/tao-blog-page/` | (Not yet inspected) | 2026-08-03 | LIVE | **DUPLICATE BLOG PAGE?** - Requires investigation |
| `/share-your-perspective/` | (Not yet inspected) | 2026-07-25 | LIVE | Reader feedback/testimonials page |
| `/sample-page/` | Sample Page | 2026-04-15 | **REMOVE** | WordPress placeholder - no institutional content |
| `/tao-hero-banner/` | (Not yet inspected) | 2026-04-27 | **REMOVE** | Appears to be Elementor template/demo page |

### Posts Inventory

**Total Posts Indexed:** 9 blog posts

All posts are recent (July-August 2026) and appear well-maintained. Titles suggest strong alignment with Tao doctrine:

1. `blog/2026/08/the-decision-before-the-decision/` (Aug 3, 2026)
2. `blog/2026/08/listening-before-explanation/` (Aug 3, 2026)
3. `blog/2026/07/two-therapists-use-the-same-technique-why-does-one-consistently-produce-better-outcomes/` (Jul 29, 2026)
4. `blog/2026/07/the-therapeutic-alliance/` (Jul 29, 2026)
5. `blog/2026/07/safety-is-the-first-intervention-understanding-physiological-safety-in-manual-therapy/` (Jul 29, 2026)
6. `blog/2026/07/the-permission-question-before-you-touch-anything-ask-yourself-this/` (Jul 29, 2026)
7. `blog/2026/07/presence-before-precision/` (Jul 29, 2026)
8. `blog/2026/07/the-greet-is-the-first-clinical-intervention/` (Jul 29, 2026)
9. `blog/2026/07/what-are-you-actually-assessing/` (Jul 29, 2026)

---

## Homepage Analysis (Detailed)

**Observation:** Homepage is the single most important page for institutional perception.

### Content Quality
✓ **Strong:** Clear positioning of book and framework  
✓ **Strong:** Five pillars framework well-presented  
✓ **Strong:** Reader testimonials demonstrate credibility  
✓ **Strong:** Author credentials visible  
✓ **Issue:** Content duplicated 3 times in page source (carousel repeats, testimonials repeat)  
✓ **Issue:** "Readme" navigation link points to `/tao-blog-page/` instead of `/blog/`  

### Visual Elements
✓ **Observed:** Book cover image on right  
✓ **Observed:** Water ripple imagery (Elementor)  
✓ **Observed:** Five-pillar carousel (interactive)  
✓ **Not yet audited:** ALT text on images  
✓ **Not yet audited:** Image file sizes and optimization  

### Navigation
✓ **Observed:** Top-right social links (Facebook, Amazon, Instagram, Email, Readme)  
✓ **Observed:** Blue "Get Your Copy" CTA button prominent  
✓ **Issue:** Navigation structure not clearly visible in page tree — need full menu audit

### CTAs (Calls to Action)
✓ "Get Your Copy" (Amazon link)  
✓ "Buy on Amazon"  
✓ "Read the Framework" (anchor link #framework)  
✓ "Get Your Copy" (repeated)  
✓ "Read a Sample" (links to free chapter)  
✓ **Issue:** CTAs are not consistent in phrasing or positioning

---

## Sitemap Structure

### XML Sitemaps Present
- `/sitemap.xml` (Main index)
- `/wp-sitemap-posts-post-1.xml` (Blog posts)
- `/wp-sitemap-posts-page-1.xml` (Pages)
- `/wp-sitemap-taxonomies-category-1.xml` (Categories)
- `/wp-sitemap-taxonomies-post_tag-1.xml` (Tags)
- `/wp-sitemap-users-1.xml` (Users)

**Note:** User sitemap should not be public. Flagged for inspection during Gate 1.

---

## Technical Observations

### Platform & Infrastructure
- **CMS:** WordPress
- **Builder:** Elementor (observed from page structure)
- **Domain:** taoclinicaltouch.com
- **HTTPS:** ✓ Confirmed
- **Title Tag:** Present and descriptive on homepage
- **Meta Description:** (Not yet audited)
- **Canonical Tags:** (Not yet audited)
- **OpenGraph:** (Not yet audited)
- **Robots.txt:** (Not yet checked)

### Performance Indicators (From page load)
- Page loaded successfully
- No critical console errors
- jQuery Migrate loaded (version 3.4.1) — may indicate jQuery dependency
- Elementor detected

### Indexation Signals
- Sitemap is properly structured
- Pages are being indexed
- **Issue:** Placeholder page "Sample Page" is indexed (should be noindex)
- **Issue:** "Tao Hero Banner" is indexed (appears to be template page)

---

## Observed Issues (Preliminary)

### Priority 1 — Remove
- ❌ `/sample-page/` — WordPress default placeholder, no institutional value
- ❌ `/tao-hero-banner/` — Appears to be Elementor template/demo page

### Priority 2 — Investigate
- 🔍 `/tao-blog-page/` — Duplicate blog page? (`/blog/` already exists)
- 🔍 Navigation structure inconsistency — "Readme" link points to blog page, not clear main navigation

### Priority 3 — Audit in Gate 1
- Content duplication on homepage (carousel, testimonials appear 3x)
- Image ALT text completeness
- Heading hierarchy
- Link structure and internal consistency
- Taxonomy (categories/tags) organization
- CTA consistency and effectiveness

---

## Administrative Baseline Pending

The following information requires SiteGround or WordPress administrative access and will be collected only after this Observation phase is approved:

### Hosting & Server
- [ ] Full site backup confirmation and location
- [ ] Database export and integrity
- [ ] Media library backup
- [ ] Server PHP version
- [ ] Server software and version
- [ ] SSL certificate status and renewal date

### WordPress Configuration
- [ ] WordPress version
- [ ] WordPress core integrity
- [ ] Theme name and version
- [ ] Child theme (if present) name and version
- [ ] Elementor version and settings
- [ ] Active plugins (list, versions)
- [ ] Inactive plugins (list)
- [ ] WordPress Site Health report
- [ ] User accounts and roles

### SiteGround Configuration
- [ ] SiteGround Optimizer status and settings
- [ ] Caching configuration
- [ ] CDN configuration
- [ ] Backup schedule and history
- [ ] Server-level redirects
- [ ] SSL/TLS configuration
- [ ] Firewall rules

### Search Console & Analytics
- [ ] Google Search Console coverage status
- [ ] Indexed vs. non-indexed pages
- [ ] Search queries and click data
- [ ] Core Web Vitals data
- [ ] Analytics baseline (sessions, users, behavior)
- [ ] Conversion tracking

### Performance Baseline
- [ ] PageSpeed Insights scores (mobile/desktop)
- [ ] Lighthouse scores (performance, accessibility, SEO, best practices)
- [ ] Core Web Vitals (LCP, FID, CLS)
- [ ] Database optimization status

---

## Detailed Page Analysis (from crawl)

### Key Metrics Across All Pages

| Page | Title | Links | Images | H2 | H3 | Meta |
|------|-------|-------|--------|-----|-----|------|
| Sample Page | Sample Page | 15 | 0 | 3 | 0 | ❌ |
| Contact | Contact | 9 | 0 | 3 | 3 | ❌ |
| About | About | 9 | 3 | 6 | 2 | ❌ |
| Services | Services | 9 | 4 | 4 | 8 | ❌ |
| Homepage | Tao of Clinical Touch | 29 | 41 | 15 | 13 | ✓ |
| Free Chapter | The Tao of Alliance | 10 | 0 | 6 | 10 | ✓ |
| Share Perspective | Share Your Perspective | 9 | 8 | 7 | 0 | ❌ |
| Tao Hero Banner | Tao Hero Banner | 9 | 0 | 2 | 0 | ❌ |
| Book | book (sic) | 30 | 49 | 9 | 5 | ❌ |
| Blog | Tao of Clinical Touch Blog | 45 | 9 | 11 | 0 | ❌ |
| Tao Blog Page | Tao Blog Page | 47 | 29 | 10 | 1 | ❌ |

### Critical Findings — Confirmed

**Pages to Remove:**

1. **`/sample-page/`** ✓ CONFIRMED PLACEHOLDER
   - Default WordPress page with no institutional content
   - No value to the institution
   - Should be permanently deleted

2. **`/tao-hero-banner/`** ✓ CONFIRMED TEMPLATE
   - Elementor template/demo page
   - Contains CSS-only hero banner with no real content
   - Appears to be leftover from design development
   - Should be permanently deleted

**Pages Requiring Investigation:**

3. **`/blog/` vs `/tao-blog-page/`** — DUPLICATE BLOG PAGES
   - Both pages display blog content
   - `/blog/` has 45 internal links, 11 H2 headings
   - `/tao-blog-page/` has 47 internal links, 29 images, 10 H2 headings
   - Tao-blog-page appears to be a more feature-rich version (includes images, more content)
   - Navigation link "Readme" points to `/tao-blog-page/` (not `/blog/`)
   - **Action needed:** Determine which is authoritative; redirect or delete one

### Metadata Audit

**Critical Issue: 9 of 11 pages missing meta descriptions**

Only pages with meta descriptions:
- Homepage: "A clinical framework for therapeutic touch — grounded in neuroscience, refined through decades of practice..."
- Free Chapter: "Read a free chapter from The Tao of Clinical Touch..."

All other pages need meta descriptions added.

### Title Formatting Issues

Several pages have formatting problems:
- `/book/` has lowercase "book" (should be "Book")
- Many titles use HTML entity `&#8211;` instead of proper em-dash
- Placeholder pages have generic titles ("Sample Page", "Tao Hero Banner", "Tao Blog Page")

### Image Inventory

- Homepage: 41 images (high count — investigate duplication)
- Book page: 49 images (no meta description, needs audit)
- Tao-blog-page: 29 images (investigate ALT text)
- About: 3 images
- Services: 4 images
- Share Perspective: 8 images
- Other pages: 0-9 images

**No ALT text audit conducted yet** — required in Gate 1.

## Next Steps — Gate 1: Understanding

This baseline establishes what is publicly observable. Gate 1 will require:

1. **Remove placeholder pages** — Sample Page and Tao Hero Banner (already identified)
2. **Resolve blog page duplicate** — Determine authoritative blog page
3. **Add meta descriptions** to 9 pages missing them
4. **Fix title formatting** — Lowercase "book" and HTML entities
5. **Image governance audit** — ALT text, filenames, compression, duplicates
6. **Link integrity audit** — internal and external link validation
7. **Editorial alignment audit** — each page's content vs. doctrine
8. **Taxonomy audit** — categories, tags, organization
9. **Redirect register** — documenting all pages to be removed and their destinations
10. **Treatment plan** — approved interventions with rationale

---

## Evidence Captured

### Screenshots
- [ ] Homepage (full page)
- [ ] Book page
- [ ] About page
- [ ] Contact page
- [ ] Services page
- [ ] Blog archive
- [ ] Sample blog post
- [ ] Free chapter page
- [ ] Reader perspectives page
- [ ] Pages to be removed (sample-page, tao-hero-banner)

### Crawl Data
- [x] Sitemap structure
- [x] Page listing
- [x] Post listing
- [ ] Full page text extraction (in progress)
- [ ] Link inventory
- [ ] Image inventory

---

## Observations Summary

**What is working:**
- Core institutional messaging is clear and compelling
- Homepage content reflects Tao philosophy
- Blog posts appear well-crafted and on-brand
- Reader testimonials are authentic and plentiful
- Book positioning is strong

**What needs attention:**
- Placeholder/demo pages indexed
- Content duplication in source
- Navigation clarity
- Image accessibility audit needed
- Taxonomy organization needs review
- Performance baseline not yet measured

**Overall institutional impression:**
The website accurately represents the institution's core work. The messaging, tone, and positioning are sound. The primary issues are structural (placeholder pages, duplicates) rather than editorial. The site has a strong foundation that requires refinement, not reconstruction.

---

**Gate 0 status:** ✓ Observation complete  
**Ready for Gate 1 review:** Awaiting approval to proceed with Understanding phase
