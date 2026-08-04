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

## 10. Four Categories of Institutional Observation

Not every inconsistency is a defect. Mature institutions contain deliberate exceptions, historical artifacts, transitional content, and intentional compromises. These are evidence of evolution, not necessarily errors.

Every finding must be categorized as one of four types:

### INSTITUTIONAL STRENGTH
**Definition:** An element that is working well and should be intentionally preserved.

**Characteristics:**
- Aligns with institutional mission
- Serves the reader or institution well
- Demonstrates institutional values
- Should not be "optimized away"

**Example:**
```
[INSTITUTIONAL STRENGTH: Editorial Audit]
Page: Homepage
Element: Reader testimonials section
Reason: Authentic voices of practitioners using the framework demonstrate real-world value
Recommendation: Preserve and strengthen; consider adding more voices
```

---

### INSTITUTIONAL DEBT
**Definition:** An element that is functional but imperfect; should eventually be improved but is not urgent.

**Characteristics:**
- Works adequately in current state
- Represents a compromise or transitional state
- Does not damage the institution
- Improvement would strengthen coherence
- Low priority; can wait for future sprints

**Example:**
```
[INSTITUTIONAL DEBT: Editorial Audit]
Page: About
Element: Author bio is minimal
Reason: Current biography lacks the institutional origin story as described in Founder Directive 005
Impact: Visitor doesn't understand the institutional context of Drew's work
Recommendation: Eventually replace with institutional origin story (not urgent for Sprint 001)
Impact Rating: MAJOR
Status: Deferred to future sprint
```

---

### INSTITUTIONAL DECISION
**Definition:** An intentional design choice that should not be "corrected" because it serves a purpose.

**Characteristics:**
- Deliberately chosen
- Serves a specific institutional function
- Might appear inconsistent if context is unknown
- Should be preserved even if it seems "wrong"
- May need clarification, not correction

**Example:**
```
[INSTITUTIONAL DECISION: Editorial Audit]
Page: Services
Element: Uses term "Services" rather than "Clinical Education"
Reason: Intentional pending Founder Directive 004 renaming (approved by Founder)
Status: Awaiting Gate 3 implementation
Recommendation: Do not correct; recognize as approved governance decision
```

---

### INSTITUTIONAL QUESTION
**Definition:** An uncertainty requiring Founder clarification before any recommendation can be made.

**Characteristics:**
- Multiple plausible interpretations
- Cannot determine intent from public inspection
- Requires Founder input to proceed
- Blocks recommendation until clarified
- Should not be assumed

**Example:**
```
[INSTITUTIONAL QUESTION: Editorial Audit]
Page: Services and About
Element: Placeholder content suspected but not confirmed
Question: Is current content intentionally minimal, or is it in transition?
Evidence: Both pages last modified April 15 (early in project)
Impact: Cannot recommend replacement without understanding current status
Required: Founder clarification before proceeding with content recommendations
```

---

## 11. Core Purpose Statement — Gate 1

**The purpose of Gate 1 is not to find problems.**

**The purpose of Gate 1 is to understand the institution well enough that any future intervention preserves—and never accidentally damages—its identity.**

This principle governs all audit work:

- Approach each page as a steward would, not as a critic
- Ask "How does this serve the institution?" not "What's wrong with this?"
- Identify strengths as carefully as you identify weaknesses
- Assume good intent; verify impact
- Distinguish between "imperfect," "intentional," and "harmful"
- Recommend only changes that strengthen institutional coherence
- **Preserve institutional memory rather than optimize it away**

Mature institutions contain deliberate exceptions, historical artifacts, transitional content, and intentional compromises. These are evidence of institutional evolution, not necessarily defects to be corrected.

If a finding does not directly affect institutional preservation, it should be marked MINOR or logged as emergent, not elevated to the Treatment Plan.

The institution's identity is not something to fix. It is something to understand, preserve, and strengthen.

---

## 12. Executive Summary — Per Audit Document

**Every Gate 1 audit deliverable must begin with an Executive Summary.**

**Purpose:** Institutional diagnosis before detailed findings. A narrative that captures institutional character, not a list of issues.

**Not:** "We found 12 problems with the homepage"  
**Yes:** "The homepage is an excellent expression of institutional positioning, anchored by authentic reader voices. It successfully communicates the North Star. It would benefit from..."

### Executive Summary Structure

**1. Institutional Diagnosis**
What kind of institution is this? What emerges from the evidence?

**2. Philosophical Coherence**
What philosophy or principles consistently emerge across pages? What values are visible?

**3. Institutional Strengths**
Where is the institution strongest? What should be intentionally preserved?

**4. Institutional Coherence Gaps**
Where is it least coherent? What breaks the narrative?

**5. Institutional Surprises**
What surprised the auditor? What was unexpected?

**6. What Should Never Change**
What is core to institutional identity and must be preserved?

**7. Overall Assessment**
One or two sentences summarizing the institutional health and readiness for intervention.

### Example Executive Summary (Editorial Audit)

```
## EXECUTIVE SUMMARY — Editorial Audit

### Institutional Diagnosis
The Tao of Clinical Touch presents as a mature clinical framework being translated into institutional form. 
The core pages (Homepage, Book, Free Chapter, Blog) embody the philosophy of the work. Transitional pages 
(About, Contact, Services) represent governance decisions in progress rather than finalized expressions.

### Philosophical Coherence
Across strong pages, a consistent philosophy emerges: understanding precedes intervention. Precision over 
persuasion. Alliance and permission as foundations. Invitational rather than promotional language. 
This philosophy is visible and consistent.

### Institutional Strengths
- Homepage: Excellent positioning with authentic practitioner voices
- Free Chapter: Clear, educational, aligned with doctrine
- Blog: Consistently strong conceptual work
- Reader Testimonials: Authentic institutional credibility

### Coherence Gaps
- About: Minimal content; institutional origin story not yet expressed
- Contact: Placeholder language; scope not yet articulated
- Services: Conceptual rename (to "Clinical Education") approved but not yet reflected
- Metadata: 9 pages lack meta descriptions; reduces discoverability but doesn't affect core voice

### Institutional Surprises
The depth of reader engagement (14+ authentic testimonials) suggests the framework is resonating 
at scale. The minimal About page suggests intentional focus on the work, not the founder—a deliberate 
choice that aligns with the philosophy.

### What Should Never Change
- The invitational, educational voice across all pages
- The prominence and authenticity of reader perspectives
- The focus on understanding over technique
- The North Star clarity (what/who/why/how/where)

### Overall Assessment
The institution is strong at its core and coherent in its philosophy. Transitional elements (About, Contact, Services) 
are governance decisions in progress, not institutional failures. The work is ready for clarity-focused intervention 
that strengthens existing strengths without disrupting working architecture.
```

---

## 13. Finding Template with Four Categories

Every finding shall include:

**CATEGORY** (one of four):
- [ ] Institutional Strength (preserve and strengthen)
- [ ] Institutional Debt (improve eventually)
- [ ] Institutional Decision (intentional, do not correct)
- [ ] Institutional Question (requires Founder clarification)

**SUBJECT**
- Page name and URL

**OBSERVATION**
- Direct evidence

**CLASSIFICATION**
- Observation or Inference

**GOVERNING DOCUMENT**
- Which authority supports this standard

**INSTITUTIONAL STANDARD**
- The principle or doctrine

**CONSEQUENCE/RISK**
- What happens if unaddressed

**RECOMMENDATION**
- Clearly separated from finding
- Only if category is Debt or requires clarification

**INSTITUTIONAL IMPACT RATING**
- Critical / Major / Moderate / Minor

**CONFIDENCE LEVEL**
- High / Medium / Low

**UNRESOLVED UNCERTAINTY**
- What would change this assessment

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
- [ ] Deliverable begins with Executive Summary (institutional diagnosis, not issue list)
- [ ] Executive Summary includes: diagnosis, philosophy, strengths, gaps, surprises, what should never change
- [ ] Deliverable includes: purpose, methodology, findings, evidence, risks
- [ ] Finding structure is consistent across all entries
- [ ] Every finding categorized as Strength / Debt / Decision / Question
- [ ] No running accounts or progress narratives
- [ ] Structured artifact with complete, finished findings

**INSTITUTIONAL MEMORY**
- [ ] Strengths are identified and explicitly marked for preservation
- [ ] Institutional Debt is distinguished from institutional defects
- [ ] Intentional decisions are recognized, not "corrected"
- [ ] Questions are flagged, not answered by assumption
- [ ] Recommendations preserve institutional evolution, not erase it

---

## Authority and Sign-Off

This framework establishes the standards for all Gate 1 work.

Approved by: Founder (Directive, August 3, 2026)

Implemented by: Claude (Steward)

Effective immediately.

Understanding precedes intervention.

Scope governs recommendation.

Evidence justifies action.
