# Engineering Assumptions Register
## Sidekick Air Structural Support System (S4)

**Project:** Project Atlas 02 — Stand Architecture Initiative  
**Document Purpose:** Track all engineering assumptions; document rationale, evidence, and downstream impacts  
**Owner:** Engineering Lead (TBD)  
**Status:** Living Document  
**Last Updated:** 2026-06-25

---

## How to Use This Register

Each assumption has the following fields:

| Field | Purpose |
|---|---|
| **ID** | Unique identifier for tracking |
| **Assumption** | Specific claim assumed to be true |
| **Rationale** | Why we believe this assumption |
| **Evidence** | What supports the assumption |
| **Confidence** | How confident are we? (High/Medium/Low) |
| **Owner** | Who owns validating this assumption? |
| **Validation Method** | How will we test/verify the assumption? |
| **Status** | Unvalidated / In Progress / Validated / Invalidated |
| **Downstream Impact** | What changes if this assumption is wrong? |
| **Notes** | Additional context |

---

## CRITICAL ASSUMPTIONS (Must Validate Immediately)

### S4-A1: Airline Portability is Achievable at Target Weight

| | |
|---|---|
| **Assumption** | A structural support system capable of supporting 800+ lbs can be designed, manufactured, and transported within airline luggage constraints (≤22 lbs) and standard checked baggage dimensions. |
| **Rationale** | Portability is core differentiator; market viability depends on clinicians being able to easily transport between locations. |
| **Evidence** | DARPA-funded deployable systems exist at similar weight/load ratios (TEMBO materials, CTD demonstrators). Professional portable tables exist in 25-35 lb range; S4 at 22 lbs is aggressive but feasible. |
| **Confidence** | Medium (requires engineering validation) |
| **Owner** | CTD (concept validation) + Element 6 (structural analysis) |
| **Validation Method** | Phase 1: Concept studies showing 3-5 approaches achieving weight/load targets. Phase 2: Prototype weight/capacity verification. |
| **Status** | UNVALIDATED (Engineering investigation in progress) |
| **Downstream Impact** | **If FALSE:** Project scope must expand (heavier system acceptable) or load capacity must reduce (800 lb target becomes 500 lbs). Business model affected (fewer portable practitioners). |
| **Notes** | This is the primary engineering risk. If unachievable, entire product direction may need reassessment. |

---

### S4-A2: One-Person Deployment is Achievable

| | |
|---|---|
| **Assumption** | A single person of average strength (5'4", 140 lbs) can deploy the complete structural system in <90 seconds with zero tools and no assistance. |
| **Rationale** | Clinical workflow requires single practitioner to set up in transition between clients. Two-person deployment creates adoption friction. |
| **Evidence** | Many portable systems (camping tents, portable massage tables) achieve one-person deployment. Deployment mechanism design is mature. |
| **Confidence** | High (well-established engineering capability) |
| **Owner** | Industrial designer + human factors engineer |
| **Validation Method** | Phase 1: Human factors engineering assessment. Phase 2: User testing with actual clinicians. |
| **Status** | UNVALIDATED (Design not finalized) |
| **Downstream Impact** | **If FALSE:** Marketing differentiator lost. Product becomes heavier, more complex. May require two-person setup (major workflow impact). |
| **Notes** | Mechanism design is critical. CTD feedback will determine feasibility. |

---

### S4-A3: 800+ lbs Static Load is Adequate for All Use Cases

| | |
|---|---|
| **Assumption** | A static load capacity of 800+ lbs is sufficient for all primary users (massage therapist + patient + dynamic loads) with acceptable safety margins. |
| **Rationale** | Typical user scenario: 180 lb clinician + 200 lb patient = 380 lbs; 2x safety factor = 760 lbs minimum. 800 lbs provides 2.1x margin. |
| **Evidence** | Professional massage tables typically rated for 500-800 lbs. Athletic treatment tables rated for 600-1200 lbs. 800 lbs covers typical use cases. |
| **Confidence** | Medium-High (typical practice; may need validation in extreme cases) |
| **Owner** | Structural engineer |
| **Validation Method** | Phase 1: Load analysis for each primary user (clinician weight, patient weight, dynamics). Phase 2: Prototype load testing. |
| **Status** | UNVALIDATED (Requires structural analysis) |
| **Downstream Impact** | **If FALSE (too low):** Load target increases (800 → 1000 lbs), adding weight and cost. Market may expand to users requiring higher capacity. **If TRUE but conservative:** May allow weight reduction. |
| **Notes** | Future military/medical variants may require 1000+ lbs. Design should allow scaling. |

---

### S4-A4: Current Inflatable Platform Dimensions are Fixed

| | |
|---|---|
| **Assumption** | The current inflatable platform dimensions (length, width, height) are locked and will not change during S4 development. The structural system must interface with current inflatable design. |
| **Rationale** | Inflatable platform development is proceeding in parallel; changing dimensions would create coordination complexity and delay both projects. |
| **Evidence** | Inflatable platform is in advanced prototype stage with locked geometry. |
| **Confidence** | High (documented in project baseline) |
| **Owner** | Drew (product director) |
| **Validation Method** | Confirm dimension baseline with inflatable platform team at project kickoff. |
| **Status** | UNVALIDATED (Requires confirmation at phase start) |
| **Downstream Impact** | **If FALSE:** S4 design must be reworked to accommodate new inflatable dimensions. Timeline extends 4-6 weeks. Interface design must be redone. |
| **Notes** | Critical assumption. Must verify at Phase 1 kickoff. |

---

### S4-A5: Structural Confidence Outweighs Minimum Weight

| | |
|---|---|
| **Assumption** | If engineering analysis reveals that achieving 18 lb target requires design compromises that reduce structural confidence, the weight target can be increased to 22 lbs while maintaining structural confidence. Weight is subordinate to confidence. |
| **Rationale** | A 20 lb platform that inspires absolute confidence outperforms an 18 lb platform that creates doubt. Market viability depends on professional trust. |
| **Evidence** | Market research with clinicians consistently identifies "stability" and "trustworthiness" as primary purchase drivers. Weight is secondary concern. |
| **Confidence** | High (user research validated) |
| **Owner** | Product director (Drew) |
| **Validation Method** | Engineering partners will present design trade-offs; product director will prioritize confidence over weight. |
| **Status** | UNVALIDATED (Design trade-offs will reveal this) |
| **Downstream Impact** | **If FALSE (weight prioritized over confidence):** Product fails in market (users perceive instability). Company liability exposure (confidence failures lead to accidents). |
| **Notes** | This is a strategic product decision, not an engineering assumption. Included here to align engineering team with product philosophy. |

---

## IMPORTANT ASSUMPTIONS (Should Validate Phase 1)

### S4-A6: Modular Expansion is Required

| | |
|---|---|
| **Assumption** | The current S4 design should be architected to support future variants (wider platform, stretcher configuration, military variant, medical variant, accessory ecosystem) without requiring complete redesign. |
| **Rationale** | Long-term Sidekick Air strategy depends on ecosystem expansion. S4 is foundation; constraining current design limits future growth. |
| **Evidence** | Product vision document emphasizes ecosystem approach. Future platforms are planned (stretcher, medical, military). |
| **Confidence** | High (documented in product strategy) |
| **Owner** | Engineering lead (mechanical systems integration) |
| **Validation Method** | Phase 1: Identify interface points and subsystems. Verify that current design doesn't create hard constraints on future variants. Phase 2: Confirm modularity with prototype. |
| **Status** | UNVALIDATED (Design not finalized) |
| **Downstream Impact** | **If FALSE (current design constrains future):** Ecosystem expansion becomes difficult. Future products require complete redesign. Strategic roadmap becomes infeasible. |
| **Notes** | This is a strategic architecture assumption. Engineering must understand modularity vision. |

---

### S4-A7: Deployment Speed <90 Seconds is Achievable

| | |
|---|---|
| **Assumption** | A mechanical deployment system (hinges, latches, springs) can achieve full deployment in <90 seconds. Preferred target is <60 seconds. |
| **Rationale** | Clinical workflow has 5-10 minute transitions between clients. 90-second setup fits workflow. 60-second deployment enhances market appeal. |
| **Evidence** | Camping tent deployment: 30-90 seconds. Professional portable tables: 60-120 seconds. Target is achievable with good mechanism design. |
| **Confidence** | Medium-High (mechanism design dependent) |
| **Owner** | Mechanism designer (CTD) |
| **Validation Method** | Phase 1: Timing estimates from concept designs. Phase 2: Prototype timing validation with clinicians. |
| **Status** | UNVALIDATED (Requires design) |
| **Downstream Impact** | **If FALSE (>120 seconds):** Market perception suffers. Clinicians may perceive setup as cumbersome. Preferred <60 sec becomes even more important differentiator. |
| **Notes** | Timing is easy to verify in Phase 2. Design must account for this requirement. |

---

### S4-A8: No Special Tools Required

| | |
|---|---|
| **Assumption** | The structural system can be deployed and collapsed entirely without tools (no wrenches, screwdrivers, hex keys, etc.). Latches, hinges, and mechanisms operate with bare hands. |
| **Rationale** | Clinician should never need to carry tools. Tool requirement adds weight, creates forgetting risk, complicates setup. |
| **Evidence** | Modern camping equipment, portable furniture achieves this standard. Mechanism design can achieve tool-free operation. |
| **Confidence** | High (well-established design approach) |
| **Owner** | Mechanism designer + industrial designer |
| **Validation Method** | Phase 1: Design review verifying all mechanisms are hand-operated. Phase 2: User testing with clinicians. |
| **Status** | UNVALIDATED (Design not finalized) |
| **Downstream Impact** | **If FALSE (tools required):** Clinician friction increases. Setup becomes more complex. May lose market differentiator. |
| **Notes** | Non-negotiable product requirement. Design must enforce this. |

---

## TECHNICAL ASSUMPTIONS (Validate During Engineering)

### S4-A9: Aluminum Alloys Provide Best Weight/Cost/Durability Balance

| | |
|---|---|
| **Assumption** | Aluminum (6061-T6 or 7075-T6) offers better overall value than carbon fiber composites or other advanced materials for the primary structural frame. |
| **Rationale** | Aluminum: mature manufacturing, cost-effective at scale, proven medical device material, recyclable, good strength-to-weight, corrosion-resistant. Carbon fiber: lighter but higher cost, manufacturing complexity, supply chain constraints. |
| **Evidence** | Professional portable tables predominantly use aluminum. Aerospace experience confirms aluminum suitable for repeated deployment. |
| **Confidence** | Medium (material selection requires engineering analysis) |
| **Owner** | Materials engineer + structural engineer |
| **Validation Method** | Phase 1: Material trade-off study (aluminum vs. composite vs. titanium). Prototype to validate choice. |
| **Status** | UNVALIDATED (Material selection pending) |
| **Downstream Impact** | **If FALSE (carbon fiber better):** Weight reduces further (potential <15 lbs). Cost increases 30-50%. Manufacturing complexity increases. Supply chain risk increases. May be justified if weight critical. |
| **Notes** | Material selection will be key Phase 1 decision. Cost and manufacturing must be evaluated alongside weight. |

---

### S4-A10: Four-Point Contact (Legs) is Optimal

| | |
|---|---|
| **Assumption** | A four-legged structure (or four-point contact system) provides optimal balance of stability, weight, and deployability. Three-legged or six-legged alternatives are less optimal. |
| **Rationale** | Four-point contact: stable on uneven terrain (tripod would rock easily), lighter than six-leg, simpler than multi-leg designs. |
| **Evidence** | Standard tables use four legs. Professional portable equipment typically uses four legs. |
| **Confidence** | Medium (requires engineering evaluation) |
| **Owner** | Structural engineer + mechanical designer |
| **Validation Method** | Phase 1: Engineering analysis comparing 3-leg, 4-leg, 6-leg approaches. Prototype validation. |
| **Status** | UNVALIDATED (Design not finalized) |
| **Downstream Impact** | **If FALSE (three legs optimal):** Weight reduces, complexity reduces. Stability on uneven terrain may suffer. **If FALSE (six legs optimal):** Weight increases, complexity increases, but ultra-stability achieved. |
| **Notes** | This is an engineering trade-off decision. Multiple valid approaches exist. |

---

### S4-A11: Mechanical Locking (Not Gravity or Friction Locks) is Required

| | |
|---|---|
| **Assumption** | The deployed structure should use mechanical locking (latches, pins, or equivalent) rather than relying on gravity or friction to maintain positioning. Active locking provides more confidence. |
| **Rationale** | Mechanical locks are visible, audible, and reassuring. Friction or gravity locks create doubt if clinician isn't certain system is locked. Patient safety requires high confidence. |
| **Evidence** | Professional tables use mechanical locks. Deployable aerospace systems use mechanical locks. High-confidence systems don't rely on passive methods. |
| **Confidence** | High (safety-driven decision) |
| **Owner** | Mechanical designer + safety engineer |
| **Validation Method** | Phase 1: Design review. Phase 2: User testing for confidence perception. |
| **Status** | UNVALIDATED (Design not finalized) |
| **Downstream Impact** | **If FALSE (passive locking sufficient):** Weight/complexity reduces. User confidence may suffer (critical risk). |
| **Notes** | Safety-driven non-negotiable. Design must include visible, audible mechanical locks. |

---

### S4-A12: Collapsible Frame (vs. Breakaway Frame) is Optimal

| | |
|---|---|
| **Assumption** | A continuously-connected frame that folds/collapses is preferable to a breakaway frame that disconnects into multiple pieces. Fewer handling requirements, lower loss risk, simpler deployment. |
| **Rationale** | Continuous frame: user doesn't lose pieces, less error-prone assembly, fewer steps. Breakaway: potentially lighter, more compact, higher complexity and loss risk. |
| **Evidence** | Modern portable furniture favors continuous fold/collapse design. Breakaway designs (like tripods) have higher user error and piece-loss risk. |
| **Confidence** | Medium (design trade-off) |
| **Owner** | Mechanical designer |
| **Validation Method** | Phase 1: Compare collapsible vs. breakaway approaches (cost, weight, complexity, user error). Phase 2: User testing for preference. |
| **Status** | UNVALIDATED (Design not finalized) |
| **Downstream Impact** | **If FALSE (breakaway better):** May achieve lighter weight. More complexity and user error potential. |
| **Notes** | This is a design trade-off. Both approaches are viable. Engineering should evaluate trade-offs. |

---

## COMMERCIAL ASSUMPTIONS (Validate Through Discussions)

### S4-A13: Target Market Will Accept 18-22 lb Weight

| | |
|---|---|
| **Assumption** | Target users (massage therapists, athletic trainers, mobile practitioners) will perceive 18-22 lbs as "portable" and acceptable for frequent transport. Significantly heavier (>25 lbs) would face market resistance. |
| **Rationale** | Professional massage tables weigh 20-35 lbs. Sidekick Air positioned as lighter alternative. 22 lbs is significant weight reduction. |
| **Evidence** | Product market research indicates weight is important differentiator. Clinicians transport equipment frequently; 22 lbs is manageable. |
| **Confidence** | Medium-High (user research supported; final validation through market testing) |
| **Owner** | Product director (Drew) |
| **Validation Method** | Phase 2: User testing with prototype weight. Market feedback. |
| **Status** | UNVALIDATED (Requires prototype and user feedback) |
| **Downstream Impact** | **If FALSE (market wants <15 lbs):** Weight target reduces. Engineering complexity increases significantly. Cost increases. **If FALSE (market accepts >25 lbs):** Weight constraint relaxes. Design becomes easier. Cost may reduce. |
| **Notes** | User testing in Phase 2 will provide definitive answer. |

---

### S4-A14: Price Point Supports Premium Positioning

| | |
|---|---|
| **Assumption** | The structural system will be positioned and priced as a premium product (estimated $800-1200 retail), not a budget alternative. Users will pay for confidence and quality. |
| **Rationale** | Sidekick Air brand is premium. Structural confidence is non-negotiable. Budget positioning (e.g., $300-400) would require cost optimization that risks confidence. |
| **Evidence** | Professional massage tables cost $1500-3000. Portable specialty equipment commands premium pricing. Clinicians pay for quality. |
| **Confidence** | Medium (market testing required) |
| **Owner** | Product director (Drew) + financial planning |
| **Validation Method** | Phase 2-3: Pricing testing with target market. Production cost analysis. |
| **Status** | UNVALIDATED (Market testing required) |
| **Downstream Impact** | **If FALSE (market wants budget pricing):** Cost targets must reduce significantly. Design must be optimized for cost, not confidence (major risk). **If TRUE:** Premium positioning supports R&D investment and quality. |
| **Notes** | Pricing is critical strategic decision. Engineering should understand price positioning drives design philosophy. |

---

## Assumption Status Summary

| Assumption | Category | Confidence | Status | Critical? |
|---|---|---|---|---|
| Airline portability achievable | Technical | Medium | Unvalidated | YES |
| One-person deployment achievable | Technical | High | Unvalidated | YES |
| 800 lbs load sufficient | Technical | Medium-High | Unvalidated | YES |
| Inflatable dimensions fixed | Commercial | High | Unvalidated | YES |
| Confidence > Weight | Strategic | High | Unvalidated | YES |
| Modular expansion required | Strategic | High | Unvalidated | No |
| <90 sec deployment | Technical | Medium-High | Unvalidated | No |
| No tools required | Technical | High | Unvalidated | No |
| Aluminum best material | Technical | Medium | Unvalidated | No |
| Four-leg optimal | Technical | Medium | Unvalidated | No |
| Mechanical locks required | Safety | High | Unvalidated | No |
| Collapsible frame optimal | Technical | Medium | Unvalidated | No |
| Market accepts 18-22 lbs | Commercial | Medium-High | Unvalidated | No |
| Premium pricing supported | Commercial | Medium | Unvalidated | No |

---

## Validation Timeline

**Phase 1 (Weeks 1-8):** Validate critical assumptions through engineering analysis
- S4-A1: Airline portability achievable (concept studies)
- S4-A2: One-person deployment (human factors assessment)
- S4-A3: Load capacity adequate (structural analysis)
- S4-A4: Inflatable dimensions confirmed (project baseline check)

**Phase 2 (Weeks 9-24):** Validate through prototyping and testing
- All critical assumptions tested through prototype
- User feedback on assumptions validated

**Phase 3 (Weeks 25+):** Market validation
- Commercial assumptions tested through production and market introduction

---

**Document Status:** ACTIVE  
**Next Review:** Weekly during Phase 1; monthly during Phase 2-3  
**Escalation:** Any "Low Confidence" assumptions becoming unfounded should trigger immediate escalation to product director

---

See also:
- Product Definition Document (01_SIDEKICK_AIR_S4_PDD_v1.0.md)
- Engineering Requirements Specification
- Risk Register