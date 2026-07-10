# Campaign 001 Directory Architecture

**Status:** Permanent Institutional Standard  
**Established:** July 9, 2026  
**Authority:** Editorial Board + Founder  

---

## Critical Distinction

Campaign 001 contains two separate directory structures with distinctly different purposes. Confusion between them creates duplicate files and conflicting sources of truth.

**THERE IS ONE CANONICAL ARTICLE SOURCE. NOT TWO.**

---

## Directory Roles

### BLOG/WEEK_01/

**Purpose:** Publishing source of truth for all editorial content

**Contains:**
- `FRIDAY.md` — The actual published blog article (one file per day)
- Raw article text intended for WordPress publication
- Final, approved, copyedited content
- Editorial Board reviewed and cleared for publication

**File Structure:**
```
BLOG/
└── WEEK_01/
    ├── FRIDAY.md (the published article)
    ├── SATURDAY.md (the published article)
    ├── SUNDAY.md (the published article)
    └── etc.
```

**Responsibility:**
- Contains ONLY the final article text
- No production specifications
- No metadata (that's in PRODUCTION)
- No duplicate content elsewhere

**Governance:**
- Editorial Board reviews → BLOG file is updated with approved content
- Em dash audit → BLOG file is corrected
- Scientific integrity check → BLOG file is verified
- All corrections apply to BLOG file ONLY

---

### PRODUCTION/WEEK_01/

**Purpose:** Workflow specification and metadata guide for all production tasks

**Contains:**
- `FRIDAY.md` — Production specifications for Friday article
- Social media copy (Facebook, Instagram, LinkedIn)
- Creative briefs and Firefly prompts
- WordPress metadata (title, meta description, SEO keywords, tags)
- Hashtags, CTA strategy, platform-specific details
- Image requirements and deployment notes
- Publishing checklist and timeline

**File Structure:**
```
PRODUCTION/
└── WEEK_01/
    ├── FRIDAY.md (production spec ONLY)
    ├── SATURDAY.md (production spec ONLY)
    ├── SUNDAY.md (production spec ONLY)
    ├── WEEK_01_STATUS.md (campaign tracking)
    ├── ASSETS/ (image placeholders, etc.)
    └── etc.
```

**Responsibility:**
- Contains ONLY production workflow and specifications
- No article text
- No actual blog content
- References BLOG/WEEK_01/FRIDAY.md for article content

**Governance:**
- Production team uses this file for workflow guidance
- Social media copy extracted from this file
- Firefly prompts used for image generation
- Never contains duplicate article content

---

## The Relationship

```
BLOG/WEEK_01/FRIDAY.md (Source of Truth)
    ↓ Editorial Board approval ↓
    ↓ (Frozen article content) ↓
    
PRODUCTION/WEEK_01/FRIDAY.md (Workflow Specification)
    ↓ Used by production team ↓
    ├→ Social media content extracted
    ├→ Firefly prompts used for images
    ├→ WordPress metadata configured
    └→ Publishing checklist executed
```

**Flow:**
1. Article is written and approved in BLOG/WEEK_01/FRIDAY.md
2. Production team references BLOG file for article content
3. Production team uses PRODUCTION/WEEK_01/FRIDAY.md for workflow specifications
4. Social media, images, and WordPress metadata drawn from PRODUCTION specs and BLOG article
5. No duplication occurs; no competing sources of truth

---

## Canonical Article Path

**THE ARTICLE LIVES HERE:**
```
/07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/BLOG/WEEK_01/FRIDAY.md
```

**NOT HERE:**
```
❌ /07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/PRODUCTION/WEEK_01/FRIDAY.md
   (This is specifications only)
```

---

## Rules

### For Editorial Board

1. **Locate articles in BLOG directory**
   - Review: `/BLOG/WEEK_01/FRIDAY.md`
   - Never edit or add content to `/PRODUCTION/WEEK_01/FRIDAY.md`

2. **Apply corrections to BLOG only**
   - Em dash removal
   - Voice refinements
   - Scientific integrity checks
   - All revisions go to BLOG file

3. **Never duplicate content**
   - Article exists in ONE location
   - PRODUCTION file references BLOG file, never duplicates it

### For Production Team

1. **Use PRODUCTION for workflow guidance**
   - Extract social copy from PRODUCTION
   - Use Firefly prompts from PRODUCTION
   - Follow publishing checklist from PRODUCTION

2. **Reference BLOG for actual article content**
   - When you need the article text, pull from BLOG
   - Never copy article into PRODUCTION
   - Treat BLOG as the source of truth

### For Campaign Managers

1. **Publishing source is BLOG**
   - Campaign Index references BLOG location
   - Publication Index references BLOG content
   - All final articles live in BLOG

2. **Status tracking uses PRODUCTION location reference**
   - PRODUCTION file documents production workflow
   - BLOG file contains approved content
   - Both are required; they have distinct roles

---

## Example Workflow

### Step 1: Editorial Board Reviews Article

```
Read: /BLOG/WEEK_01/FRIDAY.md
Task: Apply Editorial Board standards
Edit: /BLOG/WEEK_01/FRIDAY.md only
```

### Step 2: Production Team Prepares Publishing

```
Read: /PRODUCTION/WEEK_01/FRIDAY.md (for specs)
Read: /BLOG/WEEK_01/FRIDAY.md (for article content)
Extract: Social copy from PRODUCTION
Create: Firefly images using prompts from PRODUCTION
Configure: WordPress metadata from PRODUCTION
```

### Step 3: Publishing

```
Source: /BLOG/WEEK_01/FRIDAY.md (the article)
Platform: WordPress (using PRODUCTION metadata)
Social: (using PRODUCTION social copy)
```

---

## Prevention of Future Confusion

This architecture document is:
- ✅ Canonical institutional standard
- ✅ Referenced in Editorial Workflow  
- ✅ Checked during Publication Index creation
- ✅ Verified in Pre-Flight Publication Check
- ✅ Enforced by Editorial Board

**Before editing ANY Friday file, determine its location:**
- `BLOG/WEEK_01/FRIDAY.md` → Article source; apply Editorial Board corrections
- `PRODUCTION/WEEK_01/FRIDAY.md` → Specifications only; never add article content

---

## Governance

This distinction is permanent and non-negotiable.

Any future campaign using this structure must follow this same architecture.

The goal: One article, one location, no confusion.

---

**Created:** July 9, 2026  
**Authority:** Editorial Board + Founder  
**Status:** Permanent Institutional Standard
