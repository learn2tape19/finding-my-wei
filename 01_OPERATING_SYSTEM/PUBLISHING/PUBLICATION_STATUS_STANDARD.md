# Publication Status Standard

**Location:** `01_OPERATING_SYSTEM/PUBLISHING/PUBLICATION_STATUS_STANDARD.md`

**Status:** Canonical Status Definitions

**Authority:** Editorial Board

**Version:** 1.0

**Established:** July 9, 2026

---

## Standardized Publication States

Every publication has exactly one status from this list.

No custom statuses are invented.

No ambiguous status descriptions.

---

## Status Progression

```
DRAFT
  ↓
IN REVIEW
  ↓
EDITORIAL APPROVED
  ↓
FOUNDER APPROVED
  ↓
REPOSITORY UPDATED
  ↓
GIT VERIFIED
  ↓
READY TO PUBLISH
  ↓
PUBLISHED
  ↓
ARCHIVED
```

---

## Status Definitions

### DRAFT
**Meaning:** Initial version written, not yet reviewed

**Criteria:**
- First complete draft exists
- Not submitted for editorial review
- Author may still be revising

**Action Items:**
- Complete all sections
- Perform self-review
- Ready for editorial submission

**Duration:** Until author declares ready for review

---

### IN REVIEW
**Meaning:** Submitted for editorial and/or scientific review

**Criteria:**
- Article submitted to Editorial Board or Scientific Reviewer
- Awaiting feedback
- Not yet approved

**Action Items:**
- Editorial Board reviews voice, structure, flow
- Scientific Reviewer audits claims and evidence
- Reviewers provide constructive feedback

**Duration:** 2-5 days typical

---

### EDITORIAL APPROVED
**Meaning:** Editorial Board has verified and approved article

**Criteria:**
- Editorial review complete
- Scientific review complete
- All editorial feedback addressed
- Ready for Founder review

**Action Items:**
- Submit to Founder for final approval
- Prepare for publication workflow

**Duration:** Until Founder approval received

---

### FOUNDER APPROVED
**Meaning:** Founder has given final approval for publication

**Criteria:**
- Founder reviewed article
- Strategic alignment confirmed
- Voice consistency confirmed
- Publication authorized

**Action Items:**
- Move article to /BLOG canonical location
- Create production specifications
- Prepare for repository commit

**Duration:** Until repository updated

---

### REPOSITORY UPDATED
**Meaning:** Article and specifications committed to git repository

**Criteria:**
- Article in /BLOG location
- Specifications in /PRODUCTION location
- Changes staged and committed
- Commit message clear and complete

**Action Items:**
- Run post-flight checks
- Push to origin/main
- Verify push successful

**Duration:** Until push confirmed

---

### GIT VERIFIED
**Meaning:** Changes pushed to origin/main, repository integrity verified

**Criteria:**
- Git push successful
- origin/main shows latest commit
- Repository in clean state
- No uncommitted changes

**Action Items:**
- Approve for publication
- Generate any final assets
- Prepare publishing workflow

**Duration:** Until publication decision made

---

### READY TO PUBLISH
**Meaning:** All pre-publication checks passed, ready for platform launch

**Criteria:**
- All pre-flight checks passed
- Images generated and verified
- Social copy prepared
- WordPress metadata configured
- Publishing team ready

**Action Items:**
- Coordinate publication timing
- Execute publication workflow
- Monitor for successful publishing

**Duration:** Until article published

---

### PUBLISHED
**Meaning:** Article is live on intended platform

**Criteria:**
- Article accessible at published URL
- All images loaded correctly
- All links working
- Metadata correct
- Social posts scheduled

**Action Items:**
- Monitor engagement
- Respond to comments
- Gather initial feedback
- Schedule editorial reflection

**Duration:** Until reflection completed (typically 1 week)

---

### ARCHIVED
**Meaning:** Publication has completed full lifecycle and is in institutional archive

**Criteria:**
- Article remains published
- Editorial reflection completed
- Standards updated based on learning
- Institutional knowledge captured
- No further changes anticipated

**Action Items:**
- Maintain for historical reference
- Link from future related articles
- Reference in institutional memory

**Duration:** Permanent

---

## Status Transitions

**Valid Transitions:**

```
DRAFT → IN REVIEW (always)
IN REVIEW → EDITORIAL APPROVED (when ready)
IN REVIEW → DRAFT (if major revision needed)
EDITORIAL APPROVED → FOUNDER APPROVED (when Founder approves)
FOUNDER APPROVED → REPOSITORY UPDATED (when committed)
REPOSITORY UPDATED → GIT VERIFIED (when pushed)
GIT VERIFIED → READY TO PUBLISH (when approved)
READY TO PUBLISH → PUBLISHED (when live)
PUBLISHED → ARCHIVED (after reflection)
```

**Invalid Transitions:**

```
❌ DRAFT → PUBLISHED (must go through reviews)
❌ IN REVIEW → PUBLISHED (must get Founder approval)
❌ FOUNDER APPROVED → PUBLISHED (must update repository first)
❌ Any status → DRAFT (never revert to draft)
```

---

## Status Queries

### Current Status Lookup

Every publication has a definitive current status.

**Example:** "Campaign 001 Friday article is READY TO PUBLISH"

Never use:
- "almost published"
- "mostly approved"
- "mostly done"

Always use one of the nine standardized statuses.

---

## Governance

Status changes are recorded in:
- PUBLICATION_INDEX.md (campaign-level tracking)
- Individual publication files (git commit history)
- Editorial Board records (workflow documentation)

No publication changes status without documented reason.

---

**Established:** July 9, 2026  
**Authority:** Editorial Board  
**Status:** Mandatory for all publications
