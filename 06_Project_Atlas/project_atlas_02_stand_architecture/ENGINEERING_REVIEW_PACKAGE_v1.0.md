# Sidekick Air Structural Support System (S4)
## Engineering Review Package v1.0

**Project:** Project Atlas 02 — Stand Architecture Initiative  
**Date:** June 25, 2026  
**Prepared for:** Engineering Partners (CTD, Element 6, Fathom, Remington Medical)  
**Duration:** 30-minute read for experienced mechanical engineers  
**Purpose:** Initiate engineering conversation on structural architecture selection

---

## EXECUTIVE SUMMARY

### The Problem

Portable therapeutic professionals (massage therapists, athletic trainers, physical therapists) operate in distributed settings: clinics, athletic facilities, disaster sites, and field conditions.

Current options: Heavy professional tables (50-80 lbs) or unstable budget alternatives (minimal confidence).

**The gap:** No portable system combines structural confidence with actual portability.

### The Vision

Create the world's most portable professional-grade therapeutic support platform capable of delivering the stability, confidence, and performance of a traditional treatment table while fitting into airline luggage.

### The Mission

Engineer a deployable structural platform that professionals trust with another human being.

The system must inspire confidence **before treatment begins**.

### The Opportunity

**Market:** 500,000+ licensed massage therapists, athletic trainers, and hands-on therapy professionals in North America alone.

**Current Market:** Fragmented. No dominant portable solution. Market leader would establish category standard.

**Competitive Advantage:** If engineered correctly, this becomes the reference point against which every portable therapeutic platform is measured.

**Business Model:** Premium positioning ($800-1200 retail) for professional market; pathway to medical/military variants.

### Why This Matters

This is not a standalone product. This is the **foundation of an ecosystem**.

Current design targets therapeutic use. Future variants: stretcher configuration (emergency medical), wider platform (surgical prep), military field deployment.

The structural architecture we select today must support this ecosystem expansion.

---

## PRODUCT DEFINITION SUMMARY

### Primary Users

- Massage Therapists (LMTs) — 1-3 deployments per hour, multiple clinics
- Athletic Trainers — High-frequency use in field conditions  
- Physical Therapists — Clinical settings with repetitive deployment
- Emergency Medical — Disaster relief and field triage (future)
- Military Medicine — Field deployment in austere conditions (future)

### Success Definition

Users consistently describe the system as:

✓ **Stable** — No rocking, no deflection under load, trustworthy  
✓ **Professional** — Appearance suitable for clinical settings  
✓ **Lightweight** — Portable between multiple locations  
✓ **Fast** — Rapid deployment (<60 seconds preferred)  
✓ **Trustworthy** — Inspires confidence before use  
✓ **Durable** — Years of daily use without failure  
✓ **Easy to Deploy** — Intuitive, one-person setup, no tools  

**Missing any one attribute damages market viability.**

### Functional Requirements

The system shall:

1. Securely support the inflatable platform
2. Distribute load evenly (no stress concentration)
3. Minimize structural deflection (<0.25 inches under 800 lb load)
4. Prevent rocking (stable on uneven terrain)
5. Resist torsional movement (rigid under twisting forces)
6. Deploy rapidly (<90 seconds, preferred <60)
7. Collapse quickly (<2 minutes)
8. Require no tools (one person, bare hands)
9. Fit airline baggage constraints (~62" linear dimension)
10. Perform on uneven terrain (grass, concrete, floors, ±2" elevation)
11. Support future accessory integration
12. Interface cleanly with inflatable platform (minimal connection points)

---

## CRITICAL PERFORMANCE TARGETS

| Requirement | Target | Rationale |
|---|---|---|
| **Load Capacity** | 800+ lbs static | Support 200+ lb clinician + 200+ lb patient + safety margin |
| **Deflection** | <0.25 inches | User should perceive zero sagging under load |
| **Weight** | ≤22 lbs (preferred ≤18 lbs) | Portable for mobile practitioners; TSA-friendly |
| **Deployment** | <90 sec (preferred <60 sec) | Fits clinic transition time between clients |
| **Stability** | Uneven terrain ±2 inches | Grass, concrete, outdoor surfaces |
| **Service Life** | 10+ years | Daily clinical use |
| **Deployment Cycles** | 10,000+ | Equivalent to 5 years heavy use (5 deployments/day) |

---

## ENGINEERING CONSTRAINTS

### Hard Constraints (Non-Negotiable)

1. **Weight Budget:** ≤22 lbs for entire system (including inflatable interface and feet)
2. **Deployment Time:** <90 seconds from compact to fully deployed and locked
3. **Load Capacity:** 800+ lbs minimum static load
4. **Portability:** Must fit checked airline baggage (62" linear dimension)
5. **No Tools:** Complete deployment without any tools or external equipment
6. **User Confidence:** Must inspire absolute trust (safety perception is requirement)

### Design Constraints

7. **Medical Device:** Must comply with FDA pathway for class II device (likely)
8. **Scalability:** Architecture must support ecosystem expansion (stretcher, wider platform, military variants)
9. **Interface:** Must connect to current inflatable platform (dimensions, load points fixed)
10. **Outdoor Capable:** Must operate in temperature range -10°F to +100°F; humidity 10-90%
11. **Clinical Cleanability:** Must tolerate hospital-grade disinfectants without degradation

### Manufacturing Constraints

12. **Scaling Path:** Design must transition from prototype (1-10 units) to low volume (100-1000) to medium volume (10,000+)
13. **Precision Tolerance:** Cannot require excessively tight tolerances that limit production
14. **Supply Chain:** Minimize single-source component risk
15. **Assembly Simplicity:** Complex assembly increases cost and error rate

---

## CONCEPT PORTFOLIO SUMMARY

Six fundamentally different structural architectures have been developed through engineering analysis.

### TIER 1: RECOMMENDED FOR FEASIBILITY ANALYSIS

**CONCEPT A: SCISSOR-PLUS-SPRING**

Architecture: Spring-assisted scissor mechanism with mechanical latches  
Deployment: 45-60 seconds (spring-driven)  
Weight: 7-9 lbs  
Confidence: High (proven mechanism, visible locking)  
Key Risk: Hinge fatigue at 10,000 cycles  
Why Recommended: Combines proven design with elegant spring integration and high user confidence  

**CONCEPT B: TELESCOPING-WITH-OUTRIGGERS**

Architecture: Central column with automatic leg deployment  
Deployment: <45 seconds (gravity-assisted)  
Weight: 5-7 lbs (lightest)  
Confidence: Moderate (unfamiliar to some users)  
Key Risk: Torsional weakness; outrigger deployment reliability  
Why Recommended: Fastest, lightest, simplest manufacturing; addresses primary constraints  

**CONCEPT C: QUAD-TRIPOD-WITH-BRACING**

Architecture: Four mechanical legs with diagonal X-bracing  
Deployment: 45-75 seconds (mechanical assembly)  
Weight: 6-8 lbs  
Confidence: High (familiar pattern, inherent stability)  
Key Risk: Pin locking must be foolproof  
Why Recommended: Best balance of stability, user confidence, and manufacturability  

### TIER 2: CONDITIONAL DEVELOPMENT

**CONCEPT D: HYBRID SCISSOR-COLUMN** — Height-adjustable variant; pursue only if height adjustment is confirmed as requirement

**CONCEPT E: ORIGAMI-INSPIRED PANEL** — Innovative geometric approach; pursue only if weight must be <5 lbs

### NOT RECOMMENDED AT THIS TIME

**CONCEPT F: DOUBLE-SCISSOR** — Redundancy adds weight and complexity without proportional benefit; single scissor with quality hinges is superior

---

## ENGINEERING QUESTIONS FOR PARTNER REVIEW

### Architectural Questions

1. **Which architecture aligns best with your manufacturing capabilities?** Scissor? Telescoping? Quad-tripod?

2. **Where do you anticipate fatigue failure in each concept?** Which concept's failure mode concerns you most?

3. **What hinge specification would you recommend for 10,000+ cycle life?** COTS vs. custom design?

4. **Can outrigger deployment (telescoping concept) be engineered reliably?** What reliability concerns you?

5. **How would you approach pin locking foolproofing (quad concept)?** Captive pins? Tethered? Keeper chains?

### Load & Deflection

6. **Which concept best handles off-center loading?** (800 lb concentrated at platform edge vs. center)

7. **What's your FEA prediction for maximum deflection in each concept?** Can it meet <0.25" target?

8. **How much torsional loading would you predict in clinical use?** (Does therapist twist/rotate platform?)

9. **Do you see structural redundancy as necessary, or is single load path acceptable with inspection protocols?**

### Weight & Materials

10. **Can we achieve 22 lb system weight with aluminum primary structure?** Or does concept require composite/carbon fiber?

11. **What material thickness would you specify for each concept?** Weight vs. deflection tradeoff analysis?

12. **Are there material options we haven't considered?** (Magnesium? Advanced aluminum alloys? Hybrid approaches?)

13. **How would you approach corrosion resistance for clinical environment?** (Anodizing? Stainless fasteners? Alternative finishes?)

### Manufacturing & Cost

14. **Which concept has the lowest tooling cost for production scale?**

15. **What's your estimate of unit cost at 1,000 units/year for each concept?** (With target margin assumption)

16. **How would you approach assembly automation?** Which concept scales easiest to automated assembly?

17. **What supply chain risks do you anticipate?** Where are single-source dependencies?

### Deployment & User Interaction

18. **Is <60 second deployment realistic, or is 90 seconds the practical limit?** What drives your answer?

19. **For the telescoping concept: how reliable is automatic leg deployment?** Mechanical linkage vs. spring vs. motorized?

20. **What user experience factors matter most?** (Noise level? Visual locking confirmation? Effort required? Professional appearance?)

### Strategic Questions

21. **If we had to choose between lighter weight and higher confidence, which would you prioritize for medical device market?**

22. **How would you think about the ecosystem expansion?** Does today's architecture choice constrain future variants?

23. **What's your experience with similar deployable systems?** Any cautionary tales or best practices?

24. **Where do you see the highest technical risk in our approach?** What would you investigate first?

---

## DESIRED ENGINEERING DELIVERABLES

We are seeking the following from the engineering review:

### 1. Concept Recommendation

Which of the three concepts (Scissor, Telescoping, Quad) should be prototyped first?  
**Reasoning:** Why this choice over the other two? What analysis supports it?

### 2. Risk Assessment

For the recommended concept:
- Structural risks (load, deflection, fatigue)
- Manufacturing risks (precision, tooling, assembly)
- User interaction risks (deployment reliability, locking foolproofing)
- Supply chain risks (sourcing, single-source dependencies)

### 3. Alternative Concepts

Are there structural approaches we missed? Variants of our three concepts that might perform better?

### 4. Structural Analysis Plan

What FEA analysis should validate the concept?
- Load cases to model
- Deflection targets
- Fatigue analysis approach
- Torsional analysis requirements

### 5. Prototype Strategy

If we prototype this concept, what validation tests are essential?
- Load testing protocol
- Deployment cycle testing
- Material compatibility testing (disinfectants, outdoor exposure)
- User interaction observation

### 6. Manufacturing Strategy

Path from prototype to production:
- Tooling requirements
- Assembly approach
- Quality control checkpoints
- Scaling assumptions

### 7. Patent Observations

Are there novel design elements worth patenting?  
Any existing patents we should research?  
What prior art concerns you?

---

## WORKING ASSUMPTIONS (Please Challenge These)

### Assumption 1: Mechanical Locking is Required
We assume the mechanism must have visible, audible mechanical locking (not passive gravity locks).  
**Question:** Is this necessary, or can passive locking be acceptable with clear operational guidelines?

### Assumption 2: One-Person Deployment is Mandatory
We assume complete deployment by one person (no two-person setup).  
**Question:** Is this market requirement, or could two-person deployment be acceptable?

### Assumption 3: 800 lbs Load is Sufficient
We target 800 lbs static load; future medical/military variants may require 1000+ lbs.  
**Question:** Should we design for 1000 lbs today to support ecosystem?

### Assumption 4: Weight Budget is Tighter Than Load Budget
We assume weight constraint (22 lbs) is more limiting than load capacity (800 lbs).  
**Question:** Would you prioritize differently? Is 25 lbs acceptable if it improves stability?

### Assumption 5: Platform Dimensions Are Fixed
We assume inflatable platform dimensions are locked (cannot change during S4 development).  
**Question:** How flexible is the inflatable interface design?

---

## PROJECT TIMELINE

**Current Phase:** Concept selection and architecture validation (YOU ARE HERE)

**Phase 1:** Engineering feasibility studies (FEA, risk assessment, prototype planning)  
Timeline: 2-3 weeks

**Phase 2:** Prototype design and fabrication  
Timeline: 4-6 weeks

**Phase 3:** Prototype validation testing  
Timeline: 2-3 weeks

**Phase 4:** Production engineering and manufacturing transition  
Timeline: 4-8 weeks

---

## WHAT THIS IS NOT

This package is **not** a final design recommendation.

This is **not** a request to validate our preferred concept.

This is **not** a predetermined outcome waiting for engineering blessing.

## What This IS

This is an **invitation to expertise**.

We have frameworks, analysis, and multiple approaches. You have experience, intuition, and access to engineering principles we may be missing.

This conversation should reveal:
- Which concept aligns with proven practices
- Where our assumptions need validation
- What we're overlooking
- Whether our constraints are realistic
- What risks we're underestimating

---

## NEXT STEPS

**Immediate (This Week):**
1. Engineering team reviews this package
2. Initial reaction and high-level questions

**Near-term (Next 2-3 Weeks):**
1. Detailed FEA analysis of top concept
2. Risk assessment and risk mitigation strategy
3. Prototype planning and validation test strategy
4. Manufacturing approach recommendation

**Medium-term (Weeks 4-8):**
1. Prototype design and CAD
2. Component specification and sourcing
3. Prototype fabrication
4. Prototype validation testing

---

## CONTACT & NEXT CONVERSATION

**Project Director:** Drew Freedman  
**Engineering Lead (TBD):** [Partner contact]  
**Next Meeting:** [Schedule engineering review discussion]

---

## APPENDIX: FULL CONCEPT DETAILS

[Six concept families with detailed specifications, load paths, deployment sequences, manufacturing approaches, and tradeoff analyses available in attached SPRINT_003_CONCEPT_PORTFOLIO.md]

[Full Product Definition Document, Engineering Requirements Specification, and Risk Register available in PRODUCT_DEFINITION/ directory]

---

**This is the beginning of an engineering conversation, not the end of a planning process.**

We are seeking to reduce uncertainty through expert analysis and intelligent challenge.

The concepts are ready for rigorous engineering evaluation.

---

**Engineering Review Package v1.0**  
**Prepared:** June 25, 2026  
**Status:** Ready for Partner Review  
**Purpose:** Initiate engineering conversation on structural architecture selection