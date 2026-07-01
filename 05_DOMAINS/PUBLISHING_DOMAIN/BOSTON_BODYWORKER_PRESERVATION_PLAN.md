# Boston Bodyworker Preservation Plan
## Active Publishing Platform — Incremental Approach
## Date: June 30, 2026
## Status: APPROVED

---

# Core Principle

**Boston Bodyworker is NOT legacy. It is an active, appreciating intellectual asset.**

30+ years of professional authority, domain expertise, educational writing, and clinical evolution.

**Preservation strategy:** Not one-time migration. **Continuous, incremental archival that keeps the platform active.**

---

# Current State

| Aspect | Status |
|---|---|
| Website | Active (bostonbodyworker.com, WordPress, external) |
| Domain authority | Very high (30+ years of history) |
| Content | Largely unversioned (lives on external server) |
| SEO equity | Significant (backlinks, search authority) |
| Revenue | Active (not measured) |
| Operations | Ongoing (posts published regularly) |

---

# Strategic Decision

**Don't move the website to Coding-folder.**

**The website is a public platform. It should stay external and live.**

**Instead: Preserve content incrementally while the platform remains active.**

---

# Preservation Architecture

## Layer 1: External Platform (Public)
- **Website:** bostonbodyworker.com (WordPress, active)
- **Purpose:** Live publishing platform
- **Audience:** Public (clinicians, students, practitioners)
- **Function:** Ongoing publication of new content

## Layer 2: Version Control Archive (Repository)
- **Location:** 05_DOMAINS/PUBLISHING_DOMAIN/WEBSITE/
- **Purpose:** Versioned archive of published content
- **Audience:** Internal reference, historical record
- **Function:** Track what was published, when, and with what impact

---

# Three-Phase Approach

## Phase 1: Historical Archive Capture (Weeks 1-3)
**Goal:** Capture 30+ years of existing content

**Work:**
1. Export all blog posts from WordPress
   - Publication date
   - Content
   - Author
   - Categories/tags
   - Images and media references

2. Archive media files
   - Professional photography
   - Video (if any)
   - Diagrams and illustrations
   - Historical assets

3. Document URL structure
   - Current permalinks
   - Any redirects in place
   - 404s that should be fixed

4. Create wayback machine snapshots
   - Archive.org captures at key dates
   - Visual timeline of design evolution

5. Export metadata
   - Google Analytics historical data
   - Page views and traffic patterns
   - Backlink data (if available)

**Output:**
```
05_DOMAINS/PUBLISHING_DOMAIN/WEBSITE/
├── archive/
│   ├── blog-posts/
│   │   ├── 2000-early-work.md
│   │   ├── 2005-practice-evolution.md
│   │   ├── 2010-clinical-framework.md
│   │   └── ...
│   ├── images/
│   │   └── (organized by decade or topic)
│   ├── media/
│   │   └── (videos, if any)
│   └── metadata/
│       ├── export-2026-06-30.json
│       ├── analytics-historical.csv
│       └── url-structure.md
└── README.md (explaining archive)
```

**Effort:** 10-15 hours (spread over 2-3 weeks)

---

## Phase 2: Live Sync (Ongoing)
**Goal:** New content automatically flows to version control**

**Process:**
1. When new post is published on bostonbodyworker.com
2. Export/sync to 05_DOMAINS/PUBLISHING_DOMAIN/WEBSITE/live-feed/
3. Document in version control
4. Metadata captured (date, traffic, impact)

**Automation:**
- WordPress export plugin (automated weekly)
- OR: Manual export when significant post published
- OR: RSS feed sync to markdown

**Output:**
```
WEBSITE/live-feed/
├── 2026-01-15-clinical-insights.md
├── 2026-02-20-practice-notes.md
├── 2026-03-10-professional-development.md
└── ...
```

**Effort:** 2-3 hours/month (automated)

---

## Phase 3: Metadata Tracking (Ongoing)
**Goal:** Understand impact and reach**

**What to track:**
- Publication date
- Topic/category
- Views/traffic over time
- Comments and engagement
- External links/references
- Impact on professional community

**Output:**
```
WEBSITE/analytics/
├── posts-by-topic.md
├── traffic-trends.md
├── external-impact.md
└── metadata-summary.md
```

**Effort:** 1-2 hours/month (manual review)

---

# Directory Structure

```
05_DOMAINS/PUBLISHING_DOMAIN/
├── CHARTER.md (Boston Bodyworker publishing platform)
├── README.md (Platform overview)
│
├── WEBSITE/
│   ├── README.md (preservation approach explained)
│   │
│   ├── archive/
│   │   ├── README.md (what's here and why)
│   │   ├── blog-posts/
│   │   │   ├── 2000-2004/
│   │   │   ├── 2005-2009/
│   │   │   ├── 2010-2014/
│   │   │   ├── 2015-2019/
│   │   │   └── 2020-2024/
│   │   ├── images/
│   │   │   ├── professional-photos/
│   │   │   └── clinical-diagrams/
│   │   └── metadata/
│   │       ├── export-20260630.json
│   │       ├── analytics-export.csv
│   │       └── url-structure.md
│   │
│   ├── live-feed/
│   │   ├── 2026-01-15-post-title.md
│   │   ├── 2026-02-20-post-title.md
│   │   └── 2026-03-10-post-title.md
│   │
│   ├── analytics/
│   │   ├── posts-by-topic.md
│   │   ├── traffic-trends.md
│   │   └── impact-assessment.md
│   │
│   ├── wordpress-theme/
│   │   └── (theme customizations if documented)
│   │
│   └── wayback-snapshots/
│       ├── snapshot-2000.md
│       ├── snapshot-2010.md
│       ├── snapshot-2020.md
│       └── README.md (explaining snapshots)
│
├── WRITING/
│   └── (individual articles, organized for reference)
│
└── OPERATIONS/
    ├── hosting.md (GoDaddy domain, SiteGround hosting)
    ├── wordpress-version.md (version tracking)
    ├── plugins.md (active plugins documented)
    └── maintenance-log.md (when updates were made)
```

---

# Phase 1: Initial Archive (Weeks 1-3)

### Week 1: Export & Organize
- [ ] Export all WordPress content via plugin
- [ ] Categorize by decade/period
- [ ] Organize in /archive/blog-posts/
- [ ] Verify nothing lost

### Week 2: Media & Metadata
- [ ] Export all images and media
- [ ] Organize by type
- [ ] Document metadata
- [ ] Export analytics data

### Week 3: Documentation & Verification
- [ ] Write README explaining archive
- [ ] Document URL structure
- [ ] Create wayback snapshots
- [ ] Spot-check content completeness

### Output: 30+ years of content versioned, documented, searchable

---

# Phase 2: Live Sync (Starting Week 4, Ongoing)

### Monthly Process
1. Export new posts from WordPress
2. Save to /live-feed/
3. Commit to version control
4. Document in analytics

### Automated Option
- Set up weekly WordPress export plugin
- Auto-commit new posts
- Minimal manual intervention

**Effort:** 15 minutes/week to monitor

---

# Phase 3: Metadata Tracking (Starting Month 2, Ongoing)

### Monthly Review
1. Analyze traffic patterns
2. Track external impact
3. Update impact assessment
4. Record learnings

**Effort:** 1-2 hours/month

---

# Why This Approach

### ✅ Preserves without disrupting
- Website stays active and public
- No downtime or disruption
- Content remains published

### ✅ Creates searchable archive
- Version control makes content discoverable
- History is preserved
- Can track changes over time

### ✅ Enables analysis
- Can measure impact over decades
- Understand what resonates
- Learn from historical publishing

### ✅ Provides template
- Shows how to preserve active platforms
- Can be applied to future platforms
- Documents publishing evolution

### ✅ Supports ongoing business
- Content keeps generating traffic
- SEO equity preserved
- Platform remains independent

---

# Integration with Other Domains

### Tao of Clinical Touch
- Boston Bodyworker promotes the book
- Book links back to platform
- Symbiotic relationship documented

### Learn2Tape
- Boston Bodyworker establishes authority
- Learn2Tape provides education platform
- Different functions, same brand

### Project Atlas
- Research about clinical topics feeds Boston Bodyworker
- Publishing platform shares insights
- Bidirectional knowledge flow

---

# Success Criteria

### Archive Capture Complete
- [ ] All posts exported (30+ years)
- [ ] Metadata captured
- [ ] Images organized
- [ ] Verification: Nothing lost

### Live Sync Established
- [ ] Process documented
- [ ] Automation in place (if chosen)
- [ ] Monthly review schedule set
- [ ] Integration with version control working

### Preservation Active
- [ ] Content versioned in repository
- [ ] Analytics tracked
- [ ] Impact measured
- [ ] Platform remains active

---

# Timeline

| Phase | Duration | Start | End |
|---|---|---|---|
| 1: Archive Capture | 3 weeks | Week 1 | Week 3 |
| 2: Live Sync Setup | 1 week | Week 3 | Week 4 |
| 3: Analytics | Ongoing | Week 5+ | Forever |

**Concurrent with Phase 2-4 of main Estate Ingestion**

---

# Ongoing Maintenance

### Monthly
- New posts exported and versioned
- Traffic/impact reviewed
- Metadata updated

### Quarterly
- Archive quality check
- Analytics summarized
- Learnings documented

### Annually
- Impact assessment
- Platform health review
- Strategy adjustment if needed

**Estimated effort: 3-4 hours/month**

---

# Long-term Value

**In 5 years:** Complete archive of 35 years of professional publishing

**In 10 years:** Rare historical record of clinical thinking evolution

**In 20 years:** Comprehensive documentation of a professional's lifetime work

**The Boston Bodyworker becomes a teaching tool, not just a website.**

---

# Integration with Constitution

**Lifecycle state:** PUBLICATION (active platform)

**Domain:** PUBLISHING_DOMAIN

**Governance:** Drew Freedman steward, incremental preservation ongoing

**Success metric:** Preservation doesn't disrupt; platform remains active

---

**Status: APPROVED**

**Next step: Begin Phase 1 archive capture (Week 1 of Stage Two)**

**Outcome: Active publishing platform preserved incrementally, forever**
