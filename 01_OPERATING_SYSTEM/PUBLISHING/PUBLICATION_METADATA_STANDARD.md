# Publication Metadata Standard

**Location:** `01_OPERATING_SYSTEM/PUBLISHING/PUBLICATION_METADATA_STANDARD.md`

**Status:** Canonical Metadata Requirements

**Authority:** Editorial Board

**Version:** 1.0

**Established:** July 9, 2026

---

## Purpose

Every publication shall contain consistent, complete metadata.

This standard prevents missing information and enables tracking.

Metadata answers "what is this publication" and "where does it fit in the institution".

---

## Required Metadata

Every article must include all fields below.

No optional metadata; all fields are mandatory.

```yaml
---
# IDENTIFICATION
Title: <full article title>
Subtitle: <optional secondary headline>
Publication ID: <CAMP_001_W01_FRI or similar>
Campaign: <Campaign title if applicable>
Week: <week number if applicable>
Day: <day name if applicable>
Theme: <core theme of article>
Type: <Article | Paper | Essay | Chapter | etc.>

# CONTENT PROPERTIES
Word Count: <actual word count>
Reading Time: <minutes>
Estimated Reading Level: <4-6 min read>
Outline: <brief section list>

# STATUS & APPROVAL
Status: <DRAFT | IN REVIEW | EDITORIAL APPROVED | FOUNDER APPROVED | PUBLISHED | ARCHIVED>
Draft Date: <YYYY-MM-DD>
Submitted for Review: <YYYY-MM-DD>
Editorial Board Review: <YYYY-MM-DD>
Scientific Review: <YYYY-MM-DD>
Founder Approval: <YYYY-MM-DD>
Publication Date: <YYYY-MM-DD>

# LOCATION & SOURCING
Canonical Source: </BLOG/WEEK_01/FRIDAY.md>
Production Specs: </PRODUCTION/WEEK_01/FRIDAY.md>
Git Commit: <commit hash>
GitHub URL: <github.com/learn2tape19/finding-my-wei/...>

# EDITORIAL PROPERTIES
Voice: <matches Tao standards>
Scientific Integrity: <verified>
Em Dash Compliance: <0 em dashes>
Story Before Explanation: <confirmed>
Curiosity Before Certainty: <confirmed>
Relationship Before Technique: <confirmed>

# PUBLICATION PROPERTIES
Category: <Therapeutic Alliance | Research | Clinical | etc.>
Tags: <comma-separated tags>
Internal Links: <links to related articles>
Related Articles: <references to companion pieces>
SEO Description: <160 characters>
Meta Keywords: <comma-separated keywords>

# PRODUCTION PROPERTIES
Featured Image: <filename>
Image Alt Text: <descriptive alt text>
Social Media Copy: </PRODUCTION/WEEK_01/>
Email Copy: <if applicable>
Firefly Prompt: <if applicable>

# INSTITUTIONAL PROPERTIES
Contributed To Project: <Project Atlas Paper 1 | etc. if applicable>
Influenced Standards Update: <which standards updated>
Institutional Learning: <key lessons captured>
Reviewed By: <names of reviewers>
Approved By: <Founder name>

# ARCHIVE PROPERTIES
Archived: <yes/no>
Archive Date: <YYYY-MM-DD if archived>
Superseded By: <newer article if applicable>
Historical Note: <context for future readers>
---
```

---

## Metadata Location

### For Campaign Articles
Metadata in `/PRODUCTION/WEEK_01/FRIDAY.md` at top of file in YAML frontmatter

### For Project Atlas Publications
Metadata in `/PAPERS/PAPER_001/PAPER_001.md` at top of file in YAML frontmatter

### For Long-Form Essays & Books
Metadata in `/BOOKS/BOOK_001/MANUSCRIPT.md` at top of file in YAML frontmatter

### For Operating System Documents
Metadata in the document header (frontmatter-style)

---

## Field Descriptions

**Title:** The exact article title as it will appear in publication

**Campaign:** Name of campaign if article is part of campaign series

**Week/Day:** For serialized content, which week and day

**Theme:** The core topic or question the article addresses

**Type:** What kind of publication (Article, Paper, Essay, Chapter, etc.)

**Word Count:** Exact word count of article (no metadata)

**Reading Time:** Estimated reading time in minutes

**Status:** Current status from PUBLICATION_STATUS_STANDARD.md

**Canonical Source:** Path to the ONE true source file for this article

**Git Commit:** Hash of the commit that created/last updated this publication

**Voice, Scientific Integrity, etc.:** Checkboxes verifying Editorial Board standards

**Category:** How this publication is categorized (for indexing and related articles)

**Internal Links:** What other Finding My Wei articles this links to

**SEO Description:** 160-character meta description for search engines and social sharing

---

## Metadata Validation

Before publication, verify:

- [ ] All required fields present
- [ ] No fields left blank (use N/A if not applicable)
- [ ] Dates in YYYY-MM-DD format
- [ ] Word count is accurate
- [ ] Reading time is realistic
- [ ] Git commit hash is correct and pushed
- [ ] Canonical source path is correct
- [ ] All status dates are accurate

---

## Example: Complete Metadata

```yaml
---
Title: Presence Before Precision; Why Your Nervous System State Is Your Primary Clinical Tool
Campaign: Campaign 001 Therapeutic Alliance
Week: 01
Day: Friday
Theme: Clinician Regulation
Type: Article

Word Count: 791
Reading Time: 4-5 minutes

Status: PUBLISHED
Draft Date: 2026-07-09
Editorial Board Review: 2026-07-09
Founder Approval: 2026-07-09
Publication Date: 2026-07-10

Canonical Source: /BLOG/WEEK_01/FRIDAY.md
Production Specs: /PRODUCTION/WEEK_01/FRIDAY.md
Git Commit: 053caff
GitHub URL: github.com/learn2tape19/finding-my-wei/tree/main/07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/BLOG/WEEK_01

Voice: ✓ Matches Tao standards
Scientific Integrity: ✓ Verified
Em Dash Compliance: ✓ 0 em dashes
Story Before Explanation: ✓ Confirmed

Category: Therapeutic Alliance
Tags: clinician-presence, nervous-system-regulation, therapeutic-presence, clinical-preparation
Internal Links: [Safety Is the First Intervention](./wednesday.md), [Permission Question](./thursday.md)
SEO Description: Clinician presence matters more than technique. Learn how nervous system regulation becomes your most powerful therapeutic intervention.

Featured Image: friday-firefly-presence.png
Social Copy: /PRODUCTION/WEEK_01/FRIDAY.md
Email Copy: campaign-001-week-01-newsletter.md

Archived: No
---
```

---

## Governance

Metadata is mandatory.

Every publication must have complete metadata before publication.

Post-publication, metadata can be updated only in canonical source, never on platforms.

---

**Established:** July 9, 2026  
**Authority:** Editorial Board  
**Status:** Mandatory for all publications
