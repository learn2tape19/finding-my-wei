# Founder Directives — DSS-001: Tao Clinical Touch
## Gate 0 Approval & Governance Decisions

**Date:** August 3, 2026  
**Approved by:** Drew Freedman (Founder)  
**Status:** Ratified and in effect  

---

## Gate 0 Review — Approved

The following documents have been reviewed and approved:

✓ **WEBSITE_GOVERNANCE_STANDARD.md** (renamed to Digital Stewardship Standard)  
✓ **00_OBSERVATION_BASELINE.md**  
✓ **01_CONTENT_INVENTORY.md**  
✓ **GATE_0_SUMMARY.md**  

Observation is complete and accurate. Proceed to Gate 1 — Understanding.

---

## Founder Directives

### Directive 001: Delete `/sample-page/`

**Action:** Delete immediately. No redirect required.

**Rationale:** WordPress default placeholder with no institutional value.

**Implementation note:** Remove from sitemap, delete page, verify removal from Google index.

---

### Directive 002: Delete `/tao-hero-banner/`

**Action:** Delete immediately. No redirect required.

**Rationale:** Elementor design template/demo page with no institutional content.

**Implementation note:** Remove from sitemap, delete page, verify removal from Google index.

---

### Directive 003: Canonical Blog Page Strategy

**Action (DSS-001):** Keep `/tao-blog-page/` if substantially richer. Evaluate `/blog/` redirect only if no SEO loss.

**Long-term Vision (Future DSS):** 
- Create `/publications/` with Issue 001, Issue 002, Issue 003, etc.
- `/blog/` becomes a redirect to `/publications/`

**Rationale:** Current blog content should live in a single location. Investigate image and content richness of tao-blog-page to determine if it's worth keeping. Avoid risky URL changes in Sprint 001.

**Do Not:** Make URL changes this sprint if there's any SEO risk. No risky consolidation. Better to keep both pages than lose search visibility.

---

### Directive 004: Services Page Renamed & Reconceptualized

**Current URL:** `/services/`  
**Conceptual Rename:** Clinical Education  
**Rationale:** The Tao is not selling massage. It is advancing clinical education.

**Content Within Clinical Education:**
- Workshops
- Speaking
- Continuing Education
- Consulting
- Innovation
- Sidekick Air

**Implementation note:** 
- Do not retire this page
- Reconceptualize its purpose and naming
- Update content to reflect clinical education mission
- Gate 1 audits should examine current content for alignment

---

### Directive 005: About Page — Write Institutional Origin Story

**Current Status:** Placeholder content (suspected)

**Action:** Completely replace placeholder content.

**Critical Instruction:** Do not write a biography. Write an institutional origin story.

**Origin Story Should Include:**
- 25+ years of clinical practice
- Founder of Boston Bodyworker
- Founder of Learn2Tape
- Author of The Tao of Clinical Touch
- Educator, inventor, mission
- **Institutional narrative** (not personal chronology)

**Rationale:** The About page represents the institution, not the individual. The story should answer: Why does this work exist? What problem does it solve? What is the institutional mission?

**Implementation note:** Gate 1 should audit this page and prepare complete content replacement for Gate 3 implementation.

---

### Directive 006: Contact Page — Expanded Scope

**Current Status:** Placeholder content (suspected)

**Action:** Completely replace placeholder content.

**Contact Channels to Support:**
- Media inquiries
- Podcast interviews
- Book club invitations
- Conference invitations
- Speaking opportunities
- Professional collaboration
- General reader feedback

**Implementation note:** Gate 1 should audit current content and prepare complete replacement for Gate 3 implementation.

---

### Directive 007: Create Metadata Register

**New Document:** `11_METADATA_REGISTER.md`

**Purpose:** Inventory and approve all page metadata before implementation.

**Do Not:** Write metadata yet. Inventory first, approve once, implement all.

**Structure for Each Page:**
- Current Title
- Current Meta Description
- Recommended Title
- Recommended Meta Description
- Character counts (for SEO standards)
- Reasoning for recommendation
- Approval status

**Rationale:** Metadata is foundational to discoverability. All metadata should be reviewed and approved once before implementation. No piecemeal changes.

**Implementation note:** Create during Gate 1. Present for approval before Gate 3.

---

### Directive 008: Image Investigation — Do Not Assume Duplication

**Observation:** Homepage has 41 images, Book page has 49 images.

**Instruction:** Do not assume duplication. Investigate first.

**Likely Explanations:**
- Instagram feeds embedded
- Testimonial carousels
- Book mockups and cover variations
- Hidden Elementor elements

**Principle:** Understanding precedes intervention. Do not optimize before understanding.

**Implementation note:** Gate 1 image governance audit should inventory all images, document their purpose, and only flag actual duplicates. Take screenshots and document findings before making any recommendations.

---

## Authorization for Gate 1

### Approved Scope
✓ Gate 1 — Understanding phase is authorized  
✓ All audit documents should be produced  
✓ Complete Treatment Plan should be prepared  
✓ Consensus gate review materials should be assembled  

### Not Authorized
❌ No WordPress access  
❌ No implementation  
❌ No modifications to production  
❌ No changes to live site  

### Operating Principles
- Continue distinguishing observations from assumptions
- Apply Principle of Minimal Necessary Change
- Investigate before recommending changes
- Document all findings with evidence

### Areas Requiring Additional Scrutiny in Gate 1
- Image duplication vs. legitimate usage (investigate all 41-49 images)
- Canonical strategy for `/blog/` vs `/tao-blog-page/` (richness evaluation)
- Internal linking architecture (where should links point?)
- Structured data opportunities (schema markup)
- Taxonomy redesign (categories, tags, organization)
- Accessibility beyond ALT text (heading hierarchy, semantic structure, ARIA)

---

## Gate 1 Deliverables Expected

At the conclusion of Gate 1 — Understanding, submit:

1. **Complete audit documents** (02-11 listed above)
2. **Comprehensive Treatment Plan** (09) with all recommended interventions
3. **Metadata Register** (11) with proposed metadata for all 11 pages
4. **Image Governance Report** (04) with complete inventory and assessment
5. **Consensus Package** — all materials needed for Founder/Architect approval before Gate 3 intervention

**No intervention occurs until Gate 2 — Consensus has been reached.**

---

## Process Note: New Consensus Gate

Effective immediately, Digital Stewardship engagements include a Consensus gate:

**Observation → Understanding → Consensus → Intervention → Reflection**

Consensus means:
- Founder approves direction, decisions, and Treatment Plan
- Architect validates governance and institutional alignment
- Steward confirms technical feasibility and proposes implementation sequence

**No changes are made to production until consensus is reached by all three roles.**

---

## References

- **Constitutional:** WEBSITE_GOVERNANCE_STANDARD.md (renamed to Digital Stewardship Standard, Version 1.0, Ratified)
- **Baseline:** 00_OBSERVATION_BASELINE.md
- **Inventory:** 01_CONTENT_INVENTORY.md
- **Summary:** GATE_0_SUMMARY.md
- **This Document:** FOUNDER_DIRECTIVES.md

---

**Status:** Gate 0 Complete. Gate 1 — Understanding now authorized.

**Next action:** Produce all Gate 1 understanding documents per the Founder Directives above.
