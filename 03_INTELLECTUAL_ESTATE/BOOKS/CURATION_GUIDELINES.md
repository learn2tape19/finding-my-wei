# Publication Archive Curation Guidelines
## How to Preserve Books as Intellectual Work
## Date: June 30, 2026

---

# Purpose

**Books are not folders to migrate. They are publication archives to curate.**

When a book is ingested into the Intellectual Estate, we are not simply copying files.

We are **documenting and preserving the entire arc of its creation**: philosophy, process, decisions, iterations, failures, successes, and final product.

---

# The Principle

**A publication archive should tell the story of how a work was created.**

Future readers should be able to:
- Understand the author's thinking
- See the design evolution
- Learn the publishing process
- Reuse the patterns
- Appreciate the effort

**Just dumping 661 files into a folder does none of this.**

---

# Example: The Tao of Clinical Touch

### What We're Preserving

Not just: "A book was published"

Rather: "Here is how this book was conceived, designed, marketed, published, and achieved impact"

---

## Section 1: The Manuscript

**What belongs here:**
- Final approved manuscript (markdown or docx)
- Final PDF (print-ready)
- All significant drafts (with dates)
- Personalized editions (if given to specific people)
- Metadata (ISBN, copyright, imprint)

**Why keep drafts?**
- Show thinking evolution
- Document revision process
- Help future authors learn from iterations

**Structure:**
```
manuscript/
├── final/
│   ├── the-tao-clinical-touch-final.docx
│   ├── the-tao-clinical-touch-final.pdf
│   └── metadata.md
├── editions/
│   ├── tao-edition-for-whitney-lowe.docx
│   ├── tao-edition-for-til-luchau.docx
│   └── README.md (documenting personalization)
└── revisions/
    ├── draft-v1.docx (with date)
    ├── draft-v2.docx (with date)
    └── notes-on-revisions.md
```

---

## Section 2: Cover Design

**What belongs here:**
- Final cover (all formats: jpg, png, pdf, psd)
- Design evolution (if documented)
- Design rationale
- Cover specifications (dimensions, bleed, safe zones)
- Marketing mockups

**Why show evolution?**
- Demonstrates design thinking
- Useful reference for future book covers
- Shows decision-making process

**Structure:**
```
cover/
├── final/
│   ├── the-tao-cover-final.png
│   ├── the-tao-cover-final.jpg
│   ├── the-tao-cover-final.psd
│   └── specifications.md
├── evolution/
│   ├── version-1-early-concept.png (with date)
│   ├── version-2-refined.png (with date)
│   ├── version-3-feedback.png (with date)
│   └── design-decisions.md (rationale)
└── back-cover/
    └── the-tao-back-cover.jpg
```

---

## Section 3: Publishing Process

**What belongs here:**
- Publishing timeline (concept → publication)
- KDP record (ISBN, pricing, sales data)
- Publishing decisions (self-published, Amazon KDP, etc.)
- Proof documents (print proofs, technical specs)
- Marketing strategy that supported launch

**Why preserve this?**
- Future authors can learn publishing workflow
- Decision record explains why certain choices were made
- Historical record of sales and impact

**Structure:**
```
publishing/
├── publication-record.md
│   (ISBN, pricing, launch date, sales metrics)
├── kdp-metadata.md
│   (KDP title ID, categories, keywords)
├── timeline.md
│   (conception → publication → current)
└── proofs/
    └── print-interior-spread.pdf
```

---

## Section 4: Website & Promotion

**What belongs here:**
- Website configuration (if custom-built)
- Landing page HTML/templates
- Promotional strategy and messaging
- WordPress theme customizations (for taoclinicaltouch.com)
- Elementor configurations (if used)

**Why preserve this?**
- Template for future book websites
- Shows promotional approach
- Reusable marketing patterns

**Structure:**
```
website/
├── landing-page.html
├── elementor-config.json
├── wordpress-theme-customizations/
│   └── (theme files)
├── website-strategy.md
└── promotional-messaging.md
```

---

## Section 5: Marketing & Launch

**What belongs here:**
- Launch messaging pack (emails, social posts)
- Marketing assets (graphics, copy)
- Influencer outreach (who was contacted, why)
- Social media strategy
- Reviewer outreach (results)
- Campaign performance

**Why preserve this?**
- Marketing playbook for future publications
- Shows what worked (or didn't)
- Reviewer feedback and results
- Social media strategy patterns

**Structure:**
```
marketing/
├── launch-messaging.md
├── social-media-strategy.md
├── reviewer-outreach.md
│   (who received it, response rates, feedback)
├── social-assets/
│   ├── instagram-graphics/
│   ├── twitter-images/
│   └── linkedin-posts/
├── email-campaigns/
│   └── (launch email sequence)
└── performance.md
    (what worked, what didn't, metrics)
```

---

## Section 6: Technical Implementation

**What belongs here:**
- Build scripts (if automated)
- Automation tools used
- Technical decisions made
- Implementation notes

**Why preserve this?**
- Reusable automation for future books
- Technical patterns others can learn from
- Implementation decision record

**Structure:**
```
scripts/
├── build-cover.jsx (with comments)
├── build-interior.js (with comments)
├── generate-elementor.py (with comments)
└── README.md (explaining automation)
```

---

## Section 7: Evolution & Impact

**What belongs here:**
- Foreword (if there is one)
- Reviews received
- Author interviews about the book
- Updates to later editions
- Sales history and milestones
- Influence it created

**Why preserve this?**
- Shows book's life in the world
- Documents impact
- Shows how books evolve post-publication

**Structure:**
```
evolution/
├── foreword.md (Whitney Lowe, etc.)
├── reviews/
│   ├── review-1.md
│   ├── review-2.md
│   └── summary.md
├── interviews/
│   └── (if author discusses the book)
├── editions/
│   └── (if revised or updated)
└── impact.md
    (sales milestones, citations, influence)
```

---

# Curation Decision Framework

### For each file or asset:

**Question 1:** Does this tell part of the story?

**Question 2:** Could a future author learn from this?

**Question 3:** Is this the final version or a working draft?

**Question 4:** Does this represent a significant decision?

**Question 5:** Is there a relationship to another part of the archive?

### If yes to any of these → Include it

### If no to all → Consider archiving or deleting

---

# Example: Tao Curation Decisions

**Keep:**
- ✅ Final manuscript (the published work)
- ✅ Cover design evolution (shows design thinking)
- ✅ Publishing metadata (how it was published)
- ✅ Marketing strategy that worked (reusable pattern)
- ✅ Reviewer outreach results (feedback on reception)
- ✅ Build scripts (reusable automation)

**Archive (keep but separate):**
- 📦 Early drafts with heavy annotations (historical, but not essential)
- 📦 Rejected design concepts (interesting but not final direction)

**Delete (no ongoing value):**
- ❌ node_modules/ (dependency cache, not intellectual work)
- ❌ Temporary .tmp files (working clutter)
- ❌ Duplicate versions (keep only significant milestones)

---

# Process for Tao Curation

### Step 1: Categorize (1-2 hours)
Review all 661 files and sort into:
- Manuscript & versions
- Design files
- Website code & config
- Marketing materials
- Automation scripts
- Build artifacts
- Temporary/working files

### Step 2: Structure (1 hour)
Create the archive structure:
```
The-Tao-of-Clinical-Touch/
├── manuscript/
├── cover/
├── publishing/
├── website/
├── marketing/
├── scripts/
└── evolution/
```

### Step 3: Selective Copy (1-2 hours)
- Copy final manuscript → manuscript/final/
- Copy significant drafts → manuscript/revisions/ (with dates)
- Copy cover evolution → cover/ (with decision notes)
- Copy website config → website/
- Copy marketing assets → marketing/
- Copy scripts → scripts/
- Document why each was kept

### Step 4: Extract Patterns (1 hour)
Identify reusable patterns:
- Website template → Extract to CAPABILITIES/PUBLISHING/
- Build scripts → Extract to CAPABILITIES/PUBLISHING/SCRIPTS/
- Marketing strategy → Extract to CAPABILITIES/MARKETING/
- Design patterns → Extract to CAPABILITIES/PUBLISHING/DESIGN/

### Step 5: Document (1 hour)
Create README explaining:
- Why archive is structured this way
- What each section represents
- Key decisions and rationale
- Patterns extracted for reuse
- How future authors can use this as template

### Total: 4-5 hours (curated archive)

**NOT:** 12-16 hours of mechanical file moving

---

# Result

When complete, the Tao archive will:

✅ Show the complete publication story  
✅ Preserve design and marketing decisions  
✅ Document the publishing process  
✅ Provide template for future books  
✅ Extract reusable patterns  
✅ Be navigable without explanation  
✅ Demonstrate publication as intellectual work  

**The archive itself becomes a guide for how to publish intentionally.**

---

# Applying This to Future Books

**When another book is published:**

Use the same curation framework:

1. Tell the story of its creation
2. Preserve significant decisions
3. Document the process
4. Extract reusable patterns
5. Make it a learning resource

This transforms the Intellectual Estate into a repository of publishing wisdom, not just a filing system.

---

**Status: Curation guidelines established**

**Application: Tao ingestion (Phase 5 of Stage Two)**

**Outcome: Publication archive demonstrates how books are created intentionally**
