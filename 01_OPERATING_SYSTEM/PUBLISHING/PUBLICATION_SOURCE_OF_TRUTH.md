# Publication Source of Truth

**Location:** `01_OPERATING_SYSTEM/PUBLISHING/PUBLICATION_SOURCE_OF_TRUTH.md`

**Status:** Canonical Governance Document

**Authority:** Founder + Editorial Board

**Version:** 1.0

**Established:** July 9, 2026

---

## Purpose

Eliminate publication ambiguity forever by establishing one immutable principle:

**Every publication has exactly one canonical source.**

Everything else is derived from that source.

Never maintain two independent versions of the same article.

---

## The Single Source Principle

### Core Rule

One article = one location = one source of truth.

No duplication.

No competing versions.

No ambiguity about which version is authoritative.

### Why This Matters

The BLOG/PRODUCTION confusion of July 9 demonstrated the cost of ambiguous sources:

- Confusion about which file to edit
- Duplicate content in multiple locations
- Conflicting versions requiring reconciliation
- Wasted time resolving ambiguity

**Single-source publishing prevents this permanently.**

---

## Canonical Source Locations

### For Campaign Articles

**Canonical Source:** `/07_MARKETING/CAMPAIGNS/CAMPAIGN_XXX/BLOG/WEEK_XX/DAYNAME.md`

**Contains:**
- The published article (final, approved)
- Editorial history (revisions, changes)
- Final approved version only

**Example:**
```
/07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/BLOG/WEEK_01/FRIDAY.md
```

### For Project Atlas Publications

**Canonical Source:** `/02_PROJECT_ATLAS/PAPERS/PAPER_XXX/PAPER_XXX.md`

**Contains:**
- The published research paper
- Editorial history
- Final approved version

### For Long-Form Essays & Books

**Canonical Source:** `/05_INTELLECTUAL_ESTATE/BOOKS/BOOK_XXX/MANUSCRIPT.md`

**Contains:**
- The complete book manuscript
- Chapter files (if organized by chapter)
- Editorial history

### For Operating System Documents

**Canonical Source:** `/01_OPERATING_SYSTEM/[CATEGORY]/DOCUMENT.md`

**Contains:**
- The canonical institutional document
- Revision history
- Decision reasoning

---

## The Derivative Asset Principle

### What is Derivative?

Anything created FROM the canonical source is derivative:

- Social media copy
- WordPress metadata
- SEO descriptions
- Email newsletter text
- Firefly prompts
- Platform-specific adaptations

### Where Derivatives Live

Separate from the canonical source, never duplicating its content.

**Example:** Campaign 001 Friday

```
Canonical Source:
/BLOG/WEEK_01/FRIDAY.md (the article)

Derivatives:
/PRODUCTION/WEEK_01/FRIDAY.md (specs, metadata, social copy)
/PRODUCTION/WEEK_01/ASSETS/ (images, alt-text)
WordPress (published with metadata from PRODUCTION)
Social Media (copy from PRODUCTION)
Email Newsletter (copy from PRODUCTION)
```

### The Critical Rule

**Derivative files NEVER contain the article itself.**

They reference, adapt, and expand upon the canonical source.

But they never duplicate it.

---

## Publishing Architecture

```
CANONICAL ARTICLE
(Source of Truth)
│
│ ├─ Editorial Board review (in place)
│ ├─ Scientific review (in place)
│ ├─ Founder approval (in place)
│
▼
PRODUCTION SPECIFICATIONS
(Derivatives Only)
│
│ ├─ Social copy (extracted from article)
│ ├─ WordPress metadata (derived from article)
│ ├─ Firefly prompts (inspired by article)
│ ├─ Email copy (adapted from article)
│ ├─ Publishing checklist (workflow, not content)
│
▼
WORDPRESS
│
▼
PUBLISHED CONTENT

```

---

## Directory Responsibilities

### BLOG Directory

**Role:** Canonical publication source

**Contains:**
- Article text (final, approved)
- Revision history (all changes tracked)
- Editorial decisions (why changes were made)

**Responsibility:**
- Editorial Board owns the article
- All corrections apply here
- This is THE source

**Rules:**
- Never add production specifications
- Never add social media copy
- Never add WordPress metadata
- Article only

### PRODUCTION Directory

**Role:** Workflow specifications and derivatives

**Contains:**
- Social media copy (Facebook, Instagram, LinkedIn)
- WordPress metadata (title, description, keywords)
- Firefly prompts (image generation)
- Email newsletter adaptations
- Publishing checklist
- Production timeline

**Responsibility:**
- Production team uses this for workflow
- Derives from BLOG article, never duplicates it
- References BLOG as the source

**Rules:**
- Never contain the article itself
- Always reference BLOG for article content
- All specifications only
- Workflows and metadata

### WordPress & Platforms

**Role:** Published content

**Contains:**
- Article from BLOG (canonical source)
- Metadata from PRODUCTION (specifications)
- Images from PRODUCTION (generated assets)
- Social adaptations from PRODUCTION

**Responsibility:**
- Publishing teams use this for distribution
- Never modified after publication without tracking
- Links back to BLOG as source

---

## Publishing Rules

### Rule 1: One Canonical Location

Every article has exactly one home directory.

Example canonical locations:
- `/BLOG/WEEK_01/FRIDAY.md` (this is THE location)
- `/PAPERS/PAPER_001/PAPER_001.md` (this is THE location)
- `/BOOKS/BOOK_001/MANUSCRIPT.md` (this is THE location)

All other locations are derivatives.

### Rule 2: Never Duplicate

Never maintain the same article in two locations.

**Forbidden:**
```
❌ BLOG/WEEK_01/FRIDAY.md (article version 1)
❌ PRODUCTION/WEEK_01/FRIDAY.md (article version 2)
```

**Correct:**
```
✅ BLOG/WEEK_01/FRIDAY.md (the article)
✅ PRODUCTION/WEEK_01/FRIDAY.md (specifications only)
```

### Rule 3: Derive, Never Duplicate

Create derivatives from the canonical source.

Never maintain independent versions.

**Forbidden:**
```
❌ Email version of the article (separate file)
❌ Social media version of the article (separate file)
❌ WordPress version of the article (separate file)
```

**Correct:**
```
✅ Email copy adapted from canonical article
✅ Social copy extracted from canonical article
✅ WordPress uses canonical article + metadata
```

### Rule 4: Single Edit Location

Edit the article only in its canonical location.

**Forbidden:**
```
❌ Editing article in PRODUCTION
❌ Editing article on WordPress directly
❌ Maintaining article in multiple places
```

**Correct:**
```
✅ Edit only in /BLOG/WEEK_01/FRIDAY.md
✅ All changes in one place
✅ Derivatives automatically reflect changes
```

### Rule 5: Metadata Consistency

All metadata about an article lives in PRODUCTION or WordPress, never split.

**Forbidden:**
```
❌ Some metadata in BLOG
❌ Some metadata in PRODUCTION
❌ Some metadata in WordPress
```

**Correct:**
```
✅ BLOG has article content only
✅ PRODUCTION has all metadata and specs
✅ WordPress pulls metadata from PRODUCTION
```

---

## Anti-Patterns

### Anti-Pattern 1: Competing Versions

**Forbidden:** Same article in multiple locations maintained independently

**Why:** Causes confusion about which is authoritative, leads to conflicting updates

**Solution:** One canonical location, everything else derives from it

### Anti-Pattern 2: Duplicate Content

**Forbidden:** Article content in both BLOG and PRODUCTION

**Why:** When article is revised, must remember to update both (one will be forgotten)

**Solution:** Article in BLOG only, PRODUCTION references BLOG

### Anti-Pattern 3: Invisible Metadata

**Forbidden:** Metadata scattered across multiple files without clear ownership

**Why:** Hard to update consistently, easy to miss critical fields

**Solution:** Standardized metadata location (PRODUCTION or manifest file)

### Anti-Pattern 4: Platform-Specific Versions

**Forbidden:** Maintaining separate article versions for Twitter, LinkedIn, email, etc.

**Why:** Each version requires independent updates; one always falls behind

**Solution:** One article, multiple adaptations derived from it

### Anti-Pattern 5: Post-Publication Edits

**Forbidden:** Editing article only on WordPress, forgetting to update canonical source

**Why:** Repository no longer reflects published content; history is lost

**Solution:** Edit canonical source only, WordPress pulls from repository

---

## Examples

### Example 1: Campaign Article (Correct)

```
Step 1: Write and approve in canonical location
/BLOG/WEEK_01/FRIDAY.md ← article

Step 2: Specify production workflow
/PRODUCTION/WEEK_01/FRIDAY.md ← specs, not article

Step 3: Derive for distribution
- Social copy extracted from article
- Email copy adapted from article
- WordPress metadata from PRODUCTION
- Images generated using PRODUCTION prompts

Step 4: Publish
WordPress receives article + metadata
Published with proper attribution
Repository remains source of truth

Step 5: Update canonical source if needed
Edit /BLOG/WEEK_01/FRIDAY.md
All derivatives automatically reflect change
Repository history preserved
```

### Example 2: Atlas Paper (Correct)

```
Step 1: Research and write
/PAPERS/PAPER_001/PAPER_001.md ← canonical article

Step 2: Editorial review
All changes to /PAPERS/PAPER_001/PAPER_001.md
Never to derivatives

Step 3: Generate derivatives
- Blog post version (adapted for audience)
- Twitter thread (extracted summary)
- Email announcement (key findings)
- All reference /PAPERS/PAPER_001/ as source

Step 4: Publish
All versions link back to canonical paper
Repository is authoritative
History is preserved
```

---

## Governance

### Who Enforces

- **Editorial Board:** Ensures canonical source is maintained
- **Publishing Team:** Never duplicates article content
- **Repository:** Reflects single source for each publication

### When Enforced

- Before publication: Check for competing versions
- During revision: Edit canonical source only
- After publication: Updates happen in repository first

### Consequences of Violation

- Wasted reconciliation work
- Conflicting versions in publication
- Lost history and audit trail
- Confusion about authoritative source

---

## Constitutional Commitment

This principle is permanent and non-negotiable.

Every publication shall have exactly one canonical source.

Everything else is derived from that source.

This protects institutional clarity and prevents the ambiguity that plagued the BLOG/PRODUCTION confusion of July 9, 2026.

---

**Established:** July 9, 2026  
**Authority:** Founder + Editorial Board  
**Status:** Permanent Governance  
**Enforcement:** Mandatory before publication
