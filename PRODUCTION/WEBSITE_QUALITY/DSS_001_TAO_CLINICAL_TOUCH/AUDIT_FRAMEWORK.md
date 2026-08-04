# Audit Framework — Gate 1 Foundation
## Scope, Methodology, Evidence Standards, Definitions

**Date:** August 3, 2026  
**Gate:** Gate 1 — Understanding  
**Authority:** Founder Directive (August 3, 2026)  
**Status:** Foundational framework (precedes all audit deliverables)

---

## 1. Authoritative Page Inventory for Auditing

### Pages Under Audit (11 Total)

All publicly indexed pages in the DSS-001 baseline inventory.

| # | Page Name | Public URL | Status | Audit Scope |
|---|-----------|-----------|--------|------------|
| 1 | Homepage | `https://taoclinicaltouch.com/` | ACTIVE | Full audit |
| 2 | Book | `https://taoclinicaltouch.com/book/` | ACTIVE | Full audit |
| 3 | About | `https://taoclinicaltouch.com/about/` | ACTIVE | Full audit |
| 4 | Contact | `https://taoclinicaltouch.com/contact/` | ACTIVE | Full audit |
| 5 | Services | `https://taoclinicaltouch.com/services/` | ACTIVE | Full audit |
| 6 | Free Chapter | `https://taoclinicaltouch.com/chapter-1-the-tao-of-alliance/` | ACTIVE | Full audit |
| 7 | Share Perspective | `https://taoclinicaltouch.com/share-your-perspective/` | ACTIVE | Full audit |
| 8 | Blog (archive) | `https://taoclinicaltouch.com/blog/` | ACTIVE | Audit (canonical status TBD) |
| 9 | Tao Blog Page | `https://taoclinicaltouch.com/tao-blog-page/` | ACTIVE | Audit (canonical status TBD) |
| 10 | Sample Page | `https://taoclinicaltouch.com/sample-page/` | **MARKED FOR DELETION** | Audit only (no recommendations) |
| 11 | Tao Hero Banner | `https://taoclinicaltouch.com/tao-hero-banner/` | **MARKED FOR DELETION** | Audit only (no recommendations) |

### Blog Posts (9 Total)

Sample representative audit of 3-5 posts. Full audit of all 9 if patterns require.

Primary audits:
- `blog/2026/07/the-therapeutic-alliance/`
- `blog/2026/07/safety-is-the-first-intervention-understanding-physiological-safety-in-manual-therapy/`
- `blog/2026/08/listening-before-explanation/`

---

## 2. Evidence Citation Format

Every audit finding must cite evidence in this standardized format:

### Observation Citation
```
[OBSERVATION: {audit_document}]
Page: {page_name}
URL: {full_url}
Evidence: {specific_text_or_element_observed}
Screenshot: {path_if_captured}
Date Observed: {date}
```

### Example
```
[OBSERVATION: Editorial Audit]
Page: Homepage
URL: https://taoclinicaltouch.com/
Evidence: "This is not about doing more. It is about understanding what allows change."
Screenshot: EVIDENCE/screenshots/homepage_hero.png
Date Observed: 2026-08-03
```

### Inference Citation
```
[INFERENCE: {audit_document}]
Page: {page_name}
Observation: {direct_evidence}
Inferred meaning: {interpretation}
Confidence: {low/medium/high}
Alternative interpretations: {if applicable}
```

### Limitation Citation
```
[LIMITATION: {audit_document}]
Issue: {what_cannot_be_determined}
Reason: {requires_admin_access / cannot_be_inspected_publicly / depends_on_runtime_behavior}
Impact: {how_this_limits_finding}
```

---

## 3. Definitions: Observation vs. Inference vs. Risk vs. Recommendation

### OBSERVATION
**Definition:** Direct evidence perceived through public inspection.

**Characteristics:**
- Verifiable by any observer
- Present in page source, visible text, or public behavior
- Can be screenshotted, quoted, or documented
- Does not require interpretation

**Examples:**
- "Page title tag reads 'Sample Page – Tao of Clinical Touch'"
- "No meta description attribute present in page source"
- "11 images present on homepage"
- "Internal link to /book/ uses anchor text 'Buy on Amazon'"

**Citation:** `[OBSERVATION: {audit}] Direct evidence quoted`

---

### INFERENCE
**Definition:** Interpretation or meaning derived from observation.

**Characteristics:**
- Built on one or more observations
- Requires interpretation
- May have alternative explanations
- Confidence level varies

**Examples:**
- "The repeated carousel content suggests possible duplication in source code" ← inference (observation: content appears 3x in page text)
- "Page lacks meta description, which may impact search click-through" ← inference (observation: no meta description tag)
- "Services page terminology may conflict with institutional positioning" ← inference (observation: page title/content uses "Services" not "Clinical Education")

**Citation:** `[INFERENCE: {audit}] Observation → interpretation | Confidence: {level} | Alternative: {if applicable}`

---

### RISK
**Definition:** Potential negative consequence if current state is not addressed.

**Characteristics:**
- Based on observation or inference
- Identifies vulnerability or weakness
- Has probability and impact
- May be institutional, technical, or user-experience related

**Examples:**
- "Risk: Placeholder pages (sample-page, tao-hero-banner) dilute search index quality" (based on observation: pages are indexed)
- "Risk: 9 pages lacking meta descriptions reduce discoverability" (based on observation: 9 pages have no meta tags)
- "Risk: Two blog pages with similar content may confuse search engines about canonical source" (based on observation: /blog/ and /tao-blog-page/ both exist)

**Citation:** `[RISK: {audit}] Potential consequence | Probability: {estimate} | Impact: {estimate}`

---

### RECOMMENDATION
**Definition:** Proposed action to address an observation, inference, or risk.

**Characteristics:**
- Clearly separated from observation
- Based on evidence
- Includes rationale
- Does not include implementation work
- Requires Founder approval

**Examples:**
- "RECOMMENDATION: Delete /sample-page/ (approved by Founder)" 
- "RECOMMENDATION: Add meta descriptions to 9 pages (requires Founder approval)"
- "RECOMMENDATION: Evaluate /blog/ vs. /tao-blog-page/ canonical status and consolidate (requires Founder approval)"

**Citation:** `[RECOMMENDATION: {audit}] Proposed action | Rationale: {why} | Approval: {required/approved/declined}`

---

## 4. Finding Structure — Required Elements

Every audit finding must include these elements, clearly separated:

### 1. **SUBJECT**
What is being evaluated?
- Page name and URL
- Asset or element
- Feature or characteristic

### 2. **OBSERVATION**
What was directly observed?
- Specific evidence (text, code, behavior)
- How it was observed (screenshot, page source inspection, etc.)
- Date observed

### 3. **CLASSIFICATION**
Is this an observation or inference?
- Observation (directly verifiable)
- Inference (requires interpretation)
- If inference: confidence level and alternative interpretations

### 4. **INSTITUTIONAL STANDARD**
Which Tao standard or doctrine is relevant?
- Editorial Manual directive
- Brand Coherence principle
- North Star element
- Accessibility standard
- Technical requirement

### 5. **CONSEQUENCE or RISK**
What happens if this is not addressed?
- Institutional impact
- User experience impact
- Search visibility impact
- Technical impact

### 6. **RECOMMENDATION**
What should be done?
- Clearly separated from finding
- Includes rationale
- Identifies approval requirements
- Does not include implementation work

### 7. **CONFIDENCE LEVEL**
How confident is this assessment?
- HIGH (direct evidence, clear standard, low ambiguity)
- MEDIUM (evidence-based but requires interpretation, some ambiguity)
- LOW (limited evidence, multiple interpretations, significant uncertainty)

### 8. **UNRESOLVED UNCERTAINTY**
What additional information would change this assessment?
- Administrative access needed
- Runtime behavior unobservable
- User behavior unknown
- Requires stakeholder input

---

## 5. Completion Criteria — Each Deliverable

### Completion Definition
A Gate 1 deliverable is complete when:

1. **All authorized pages/assets are reviewed** (per scope for that audit)
2. **All findings follow the required structure** (subject, observation, classification, standard, consequence, recommendation, confidence, uncertainty)
3. **Evidence is cited for every finding** (using standardized citation format)
4. **Observations are distinguished from inferences** (labeled explicitly)
5. **Risks are identified and documented** (where applicable)
6. **Recommendations are separated from findings** (not mixed)
7. **Approval requirements are identified** (what needs Founder/Architect consensus)
8. **Limitations are documented** (what cannot be publicly inspected)
9. **Document includes purpose, methodology, findings, evidence, risks** (per Founder Directive)
10. **No implementation work is included** (no code changes, no WordPress access assumed)

### Per-Deliverable Completion Criteria

**02_EDITORIAL_AUDIT**
- All 11 pages reviewed for editorial alignment
- Each page assigned alignment score
- Strengths and weaknesses documented
- Risks identified
- Founder Consensus items flagged

**03_ACCESSIBILITY_AUDIT**
- Heading hierarchy mapped for 6 priority pages
- Semantic HTML issues identified (where observable)
- Image ALT text audited (all images with current + recommended)
- Link descriptiveness evaluated
- Button labels examined
- Limitations clearly labeled (e.g., "keyboard accessibility not fully testable without admin access")

**04_IMAGE_GOVERNANCE_AUDIT**
- Every meaningful public image inventoried
- Filename, purpose, current ALT, recommended ALT recorded
- Duplication investigated (not assumed)
- Dimensions and optimization opportunities noted
- Documentary alignment and editorial appropriateness assessed

**05_TECHNICAL_SEO_AUDIT**
- All 11 pages title tags examined
- Meta descriptions audited (presence/absence)
- Canonical tags reviewed (where observable)
- Robots directives checked
- Sitemap coverage verified
- Structured data opportunities identified
- Crawlability assessment made
- Separates confirmed vs. inferred vs. requires-admin

**06_LINK_INTEGRITY_AUDIT**
- Internal links reviewed (why do they exist?)
- External links examined (accuracy, relevance)
- Navigation pathways mapped
- Dead ends documented
- Orphan pages identified
- Circular navigation flagged
- CTA pathways traced

**07_REDIRECT_REGISTER**
- Each proposed redirect documented
- Old URL → Recommended Destination → Reason → SEO Impact → Risk → Approval
- No implementation

**08_KNOWLEDGE_GRAPH**
- Core Tao concepts mapped
- Relationships illustrated
- Current support assessed
- Missing links identified
- Strengthening opportunities noted

**09_TREATMENT_PLAN**
- All recommended interventions documented
- Organized by priority (Critical/High/Medium/Low)
- Each intervention: Observation → Evidence → Reasoning → Benefit → Risk → Rollback
- Approval requirements flagged
- No implementation

**10_LESSONS_LEARNED**
- Institutional observations captured
- Patterns documented
- Strengths and weaknesses noted
- Governance improvements identified
- Future Steward guidance included

**11_METADATA_REGISTER**
- Every indexable page inventoried
- Current title, meta description, character count recorded
- Recommended title, recommended meta, target intent proposed
- Reasoning documented
- Approval status tracked
- No implementation

**12_BRAND_COHERENCE_AUDIT**
- Institutional consistency evaluated across pages
- Typography consistency assessed
- Photography alignment reviewed
- CTA language evaluated (invitation vs. persuasion)
- Publication System integration examined
- North Star reinforcement assessed
- Not a visual design review

---

## 6. Pages/Systems/Evidence That Cannot Be Publicly Inspected

### Cannot Be Observed (Requires Administrative Access)

| Item | Why | Impact |
|------|-----|--------|
| WordPress plugin list | Admin panel only | Cannot assess plugin quality or conflicts |
| Database configuration | Admin panel only | Cannot assess optimization status |
| Server-side redirects | Server logs | Cannot assess redirect implementation |
| Analytics data | Requires authentication | Cannot assess traffic patterns |
| Search Console data | Requires authentication | Cannot assess index status or search queries |
| Caching configuration | SiteGround admin | Cannot assess caching strategy |
| File permissions | Server filesystem | Cannot assess security settings |
| Database size | Admin metrics | Cannot assess database optimization |
| Backup status | SiteGround admin | Cannot verify backup procedures |

### Limitations (Public Inspection Only)

| Capability | Limitation | Workaround |
|-----------|-----------|-----------|
| Image dimensions | Can infer from display, not precise | Document as inference with confidence level |
| File sizes | Not publicly available | Cannot audit compression without access |
| Load time | Can measure from public access | Represents one test condition, not comprehensive |
| JavaScript behavior | Limited to browser render | Cannot audit all runtime behavior |
| CSS cascade | Can inspect rendered styles | Cannot access uncompressed source |
| Mobile responsiveness | Can test resize, not all devices | Test at common breakpoints |
| Keyboard navigation | Can test tab order | Cannot access screen reader output |
| Form validation | Can test public forms | Cannot audit backend validation |
| Structured data | Can inspect JSON-LD in source | Cannot validate against real search crawler |

---

## 7. Emergent Findings Log

**Purpose:** Holding register for observations that do not fit the 11 authorized deliverables.

**Criteria for logging:**
- Observation fits none of the 11 defined audits
- Evidence is strong enough to document
- Requires Founder authorization to become a deliverable
- Will not expand Gate 1 scope

**Process:**
1. Create `EMERGENT_FINDINGS_LOG.md` only if items exist
2. Document observation with evidence
3. Label as pending Founder decision
4. Do not act on findings
5. Submit to Founder for guidance on integration

**Example entry (should not exist unless warranted):**
```
[EMERGENT]
Observation: Instagram feed embed on homepage is not mobile-responsive
Evidence: Screenshot showing feed overflow on mobile viewport
Standard: Principle of Invitation (reduce friction)
Risk: Mobile users may experience poor UX
Status: Pending Founder guidance on mobile audit scope
```

---

## 8. Frozen Institutional Baseline — Authoritative Governing Documents

### Authority Hierarchy

Before evaluating a single page, the Steward must explicitly identify which governing document supports every standard, principle, and expectation.

**Authoritative Institutional Documents (frozen for DSS-001):**

1. **CONSTITUTION.md** — Institutional identity and foundational principles
   - How we are structured
   - What we stand for
   - Core operating principles

2. **EDITORIAL_MANUAL.md** — Voice, tone, and editorial standards
   - Editorial voice and tone requirements
   - Clarity and precision standards
   - Invitational vs. promotional language
   - Consistency requirements

3. **VISUAL_DOCTRINE.md** — Visual identity and design standards
   - Typography standards
   - Color usage
   - Visual hierarchy
   - Spacing and rhythm

4. **DOCUMENTARY_PHOTOGRAPHY_DOCTRINE.md** — Photography standards
   - Appropriate imagery
   - Documentary alignment
   - Authenticity over stock imagery

5. **BRAND_GOVERNANCE_STANDARD.md** — Brand consistency across properties
   - Brand voice consistency
   - Logo and wordmark usage
   - Visual coherence

6. **DIGITAL_STEWARDSHIP_STANDARD.md** (this framework)
   - Website governance principles
   - Stewardship standards
   - Institutional coherence in digital properties

7. **FOUNDER_DIRECTIVES.md (DSS-001)** — Specific decisions for this engagement
   - Approved governance decisions
   - Treatment approval status
   - Site-specific requirements

### How to Use This Baseline

**Every finding must cite which document supports the standard being evaluated.**

**Example:**
```
[OBSERVATION: Editorial Audit]
Page: About
Standard: Editorial voice consistency (EDITORIAL_MANUAL.md)
Governing Principle: "The voice is clear, precise, and invitational"
Finding: Current page text uses promotional language ("amazing", "incredible")
Institutional Standard Violated: Yes
Recommendation: Revise to align with Editorial Manual voice standards
```

**Forbidden approach:**
- Do not invent a standard and cite it as institutional doctrine
- Do not assume a standard without locating it in a governing document
- Do not treat reasonable assumptions as equivalent to documented standards

### Standards by Category

**Editorial Standards (from EDITORIAL_MANUAL.md)**
- Voice: Clear, precise, invitational
- Tone: Educational, not promotional
- Precision over persuasion
- Transparency about limitations
- Support for therapeutic alliance
- Respect for reader autonomy

**Institutional Philosophy (from CONSTITUTION.md, DIGITAL_STEWARDSHIP_STANDARD.md)**
- Understanding precedes intervention
- Safety before technique
- Permission as protocol
- Alliance as physiology
- Communication as care
- Wu Wei (non-imposition)

**The North Star (from FOUNDER_DIRECTIVES.md)**
A first-time visitor immediately understands:
1. What The Tao of Clinical Touch is
2. Who Drew Freedman is
3. Why the work is different
4. How the ideas connect
5. Where to go next

**Brand Coherence Standards (from BRAND_GOVERNANCE_STANDARD.md, DIGITAL_STEWARDSHIP_STANDARD.md)**
- Institutional consistency
- Visual rhythm
- Photography alignment
- Typography consistency
- CTA language (invitational, not transactional)
- Publication System integration

**Accessibility Standards** (from general institutional commitment to inclusion)
- WCAG 2.1 Level AA compliance where observable
- Clear heading hierarchy
- Descriptive link text
- Image alt text standards

---

## 9. Institutional Impact Rating

Not all findings are equal.

A typo is not equivalent to undermining institutional identity.

Every finding must be assigned an Institutional Impact rating that reflects whether it affects the institution's identity, communication, or user experience.

### Impact Rating Scale

| Rating | Meaning | Example | Consequence |
|--------|---------|---------|------------|
| **CRITICAL** | Undermines institutional identity or trust | Placeholder content suggesting the work is unfinished; messaging contradicting Tao philosophy; false claims | Damages credibility; confuses visitor about institutional mission; **must address before launch** |
| **MAJOR** | Weakens communication or consistency | Missing meta descriptions reducing discoverability; inconsistent editorial voice across pages; broken internal links disrupting reader journey | Reduces effectiveness of institutional communication; creates friction; **should address in this sprint** |
| **MODERATE** | Creates friction or ambiguity | Unclear CTA language; inconsistent typography; ALT text missing on illustrative images | Affects user experience or accessibility; minor inconsistency; **should address if capacity allows** |
| **MINOR** | Cosmetic improvement only | Filename optimization; metadata character count fine-tuning; CSS polish with no functional impact | No impact on institutional identity or user experience; **optional; consider for future sprints** |

### How to Assign Impact Rating

Ask these questions in order:

1. **Does this affect institutional identity or trust?** → If YES: **CRITICAL**
2. **Does this weaken communication or consistency?** → If YES: **MAJOR**
3. **Does this create friction or ambiguity for the visitor?** → If YES: **MODERATE**
4. **Is this purely cosmetic?** → If YES: **MINOR**

### Application Rule

**Do not assign CRITICAL or MAJOR impact based on assumptions.** 

Only assign high impact if:
- Direct evidence supports the impact claim
- The institutional standard is explicitly documented
- The consequence affects institutional identity or core communication

### In Treatment Plan

The Treatment Plan will be organized by Institutional Impact, not by page or category.

- CRITICAL findings → must address
- MAJOR findings → should address
- MODERATE findings → may address if capacity allows
- MINOR findings → consider for future sprints

This ensures recommendations focus on institutional preservation, not optimization theater.

---

## 10. Core Purpose Statement — Gate 1

**The purpose of Gate 1 is not to find problems.**

**The purpose of Gate 1 is to understand the institution well enough that any future intervention preserves—and never accidentally damages—its identity.**

This principle governs all audit work:

- Approach each page as a steward would, not as a critic
- Ask "How does this serve the institution?" not "What's wrong with this?"
- Identify strengths as carefully as you identify weaknesses
- Assume good intent; verify impact
- Distinguish between "imperfect" and "harmful"
- Recommend only changes that strengthen institutional coherence

If a finding does not directly affect institutional preservation, it should be marked MINOR or logged as emergent, not elevated to the Treatment Plan.

The institution's identity is not something to fix. It is something to preserve and strengthen.

---

## 11. Founder Consensus Items

Findings that require explicit Founder approval before proceeding to Consensus gate:

Examples of items that WILL require approval:
- Recommended redirects or URL changes
- Content replacement recommendations
- Deletion recommendations
- Structural changes to navigation
- Classification changes (e.g., rename Services to Clinical Education)
- New features or content additions

Items flagged in each audit should identify:
- What decision is required
- What options exist
- What evidence supports each option
- Timeline for decision

---

## 12. Quality Assurance Checklist

Before submitting any Gate 1 deliverable:

**SCOPE**
- [ ] All authorized pages/assets for this audit have been reviewed
- [ ] No scope expansion beyond authorized deliverable
- [ ] Limitations are documented

**EVIDENCE**
- [ ] Every finding cites evidence in standardized format
- [ ] Evidence is verifiable by another observer
- [ ] Screenshots or quotes provided (where applicable)

**CLASSIFICATION**
- [ ] Observations labeled as observations (directly verifiable)
- [ ] Inferences labeled as inferences with confidence levels
- [ ] Risks clearly identified and separated from findings
- [ ] Recommendations clearly separated from findings

**IMPACT RATING**
- [ ] Every finding assigned Institutional Impact rating (Critical/Major/Moderate/Minor)
- [ ] Impact rating based on institutional preservation, not optimization
- [ ] High-impact ratings supported by direct evidence
- [ ] Cosmetic findings correctly marked MINOR

**STANDARDS**
- [ ] Each finding cites a governing document (Constitution, Editorial Manual, etc.)
- [ ] Standard is not invented; it is documented in an authoritative source
- [ ] Consequence or risk identified
- [ ] Unresolved uncertainties documented
- [ ] Every standard is justifiable from a governing document, not assumption

**APPROVAL**
- [ ] Founder Consensus items clearly flagged
- [ ] No assumptions about authorization
- [ ] No implementation work included

**COMPLETENESS**
- [ ] Deliverable includes: purpose, methodology, findings, evidence, risks
- [ ] Finding structure is consistent across all entries
- [ ] No running accounts or progress narratives
- [ ] Structured artifact with complete, finished findings

---

## Authority and Sign-Off

This framework establishes the standards for all Gate 1 work.

Approved by: Founder (Directive, August 3, 2026)

Implemented by: Claude (Steward)

Effective immediately.

Understanding precedes intervention.

Scope governs recommendation.

Evidence justifies action.
