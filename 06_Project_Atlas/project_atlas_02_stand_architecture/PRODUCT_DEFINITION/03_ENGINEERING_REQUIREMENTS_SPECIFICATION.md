# Engineering Requirements Specification (ERS)
## Sidekick Air Structural Support System (S4)

**Project:** Project Atlas 02 — Stand Architecture Initiative  
**Document Purpose:** Quantitative translation of product requirements into measurable engineering specifications  
**Owner:** Engineering Lead (TBD)  
**Status:** Living Document (Baseline v1.0)  
**Last Updated:** 2026-06-25

---

## Overview

This document converts the Product Definition Document (PDD) into measurable, testable engineering requirements.

Specifications include both **fixed targets** (non-negotiable) and **open parameters** (to be determined through engineering).

All specifications will be validated through testing during Phase 2-3.

---

## STRUCTURAL REQUIREMENTS

### Load Capacity

| Specification | Target | Confidence | Notes |
|---|---|---|---|
| **Static Vertical Load** | 800+ lbs | Baseline | Minimum; 1000 lbs recommended for safety margin |
| **Dynamic Load Factor** | 2.0x minimum | Requirement | Design safety factor; may be higher |
| **Load Distribution** | Even across supports | Requirement | <10% variance between legs |
| **Overload Capacity** | 1200 lbs (test limit) | Test Protocol | Prototype tested to 1.5x rated load |

### Deflection

| Specification | Target | Confidence | Notes |
|---|---|---|---|
| **Maximum Deflection (800 lb load)** | <0.25 inches | Baseline | User should perceive no sagging |
| **Lateral Deflection (rocking)** | <0.1 inches | Requirement | Stability perception critical |
| **Torsional Deflection** | <2 degrees under 200 lb torque | TBD | Requires engineering analysis |

### Durability

| Specification | Target | Confidence | Notes |
|---|---|---|---|
| **Deployment Cycle Life** | 10,000+ cycles minimum | Baseline | Equivalent to 5 years heavy use (5 deployments/day) |
| **Service Life** | 10+ years | Baseline | Continuous outdoor exposure acceptable |
| **Fatigue Testing** | No failure at 10,000 cycles at 800 lbs | Test Protocol | Will be validated in Phase 2 prototype testing |
| **Wear Component Life** | <1000 cycles before replacement recommended | TBD | Hinges, latches, feet may have shorter life |

---

## WEIGHT REQUIREMENTS

| Specification | Target | Confidence | Notes |
|---|---|---|---|
| **Total System Weight** | ≤18 lbs preferred, ≤22 lbs maximum | Baseline | Portability critical; structural confidence may require relaxation |
| **Weight Distribution** | TBD | Engineering Decision | Should distribution be symmetric? |
| **Transport Weight (with case)** | ≤30 lbs total | Baseline | TSA friendly for checking |

**Weight Budget (Preliminary):**
- Frame structure: 12-15 lbs
- Hinges/latches/mechanisms: 1-2 lbs
- Feet/contact points: 0.5-1 lb
- Hardware/fasteners: 0.5 lb
- **Total:** 14-19.5 lbs

*To be refined after concept design*

---

## DEPLOYMENT REQUIREMENTS

| Specification | Target | Confidence | Notes |
|---|---|---|---|
| **Deployment Time** | <90 seconds | Baseline | Full deployment from compact state |
| **Preferred Deployment Time** | <60 seconds | Goal | Market differentiator |
| **Collapse Time** | <2 minutes | Baseline | Must fit clinic transition time |
| **Setup Complexity** | One person, bare hands, no tools | Requirement | Non-negotiable |
| **Visible Locking** | All joints locked visibly | Requirement | User must confirm locking |
| **Audible Confirmation** | Audible click or snap on lock | Preferred | Additional confidence signal |

---

## STABILITY REQUIREMENTS

| Specification | Target | Confidence | Notes |
|---|---|---|---|
| **Rocking Resistance** | Operates on ±2 inch terrain variation | Requirement | Grass, concrete, uneven floors |
| **Tipping Prevention** | No tip-over under 800 lb centered load + leaning | Requirement | Must not tip when pressure applied off-center |
| **Wind Stability** | Resists 15 mph wind with platform loaded | Requirement | Outdoor use in light wind conditions |

---

## MATERIAL & ENVIRONMENTAL REQUIREMENTS

### Materials

| Specification | Preferred | Notes |
|---|---|---|
| **Primary Structure** | Aluminum 6061-T6 or 7075-T6 | Material selection TBD; composite alternative under review |
| **Hinges/Joints** | Stainless steel or aluminum | Corrosion resistance required |
| **Fasteners** | Stainless steel (no steel unless plated) | Medical device environment; avoiding corrosion |
| **Feet/Contact Points** | Rubber or polymeric | Grip, vibration damping, no scratch surfaces |
| **Finish** | Anodized aluminum (if aluminum) | Corrosion and wear resistance |

### Environmental Compatibility

| Specification | Requirement | Notes |
|---|---|---|
| **Temperature Range** | -10°F to +100°F operational | Performance may degrade; not failure |
| **Humidity Resistance** | 10-90% RH non-condensing | Outdoor use requires moisture resistance |
| **Corrosion Resistance** | Survives 500+ hours salt fog testing (ASTM B117) | Medical/coastal environments |
| **UV Resistance** | No material degradation after 5 years outdoor exposure | If used as outdoor equipment |
| **Chemical Resistance** | Tolerates hospital-grade disinfectants (bleach, IPA, quaternary ammonium) | Cleanliness protocol compatibility |
| **Sterilization Compatibility** | TBD | If medical-grade sterilization required (gamma, EtO, autoclave) |

---

## INTERFACE REQUIREMENTS

### Inflatable Platform Interface

| Specification | Requirement | Notes |
|---|---|---|
| **Connection Type** | Tool-free attachment/detachment | User should not need wrenches |
| **Connection Points** | ≤4 major connection points | Simplicity and reliability |
| **Load Transfer** | Distributed across platform perimeter | Even load distribution |
| **Interface Documentation** | CAD of current inflatable interface locked | Enables interface design |

### Future Accessory Integration

| Specification | Requirement | Notes |
|---|---|---|
| **Mounting Points** | TBD | Future designs will define accessory attachment |
| **Load Capacity** | Must not exceed frame torsional limits | Accessories add loading |
| **Interface Standard** | Modular approach (details TBD) | Support ecosystem expansion |

---

## DIMENSIONAL REQUIREMENTS

| Specification | Target | Confidence | Notes |
|---|---|---|
| **Transport Case Dimensions** | ≤62" linear dimension | Requirement | TSA checked baggage standard |
| **Footprint (Deployed)** | TBD | Engineering Decision | Will be determined by inflatable platform size |
| **Height (Deployed)** | TBD | Engineering Decision | Must match inflatable platform height |
| **Collapsed Dimensions** | TBD | Engineering Decision | Compact as possible while maintaining strength |

---

## HUMAN FACTORS REQUIREMENTS

| Specification | Requirement | Validation Method |
|---|---|---|
| **Deployment Effort** | One person of 5'4", 140 lbs can deploy | Phase 2: User testing |
| **No Pinch Hazards** | No points where fingers can be pinched | Phase 1: Design review; Phase 2: User testing |
| **Quiet Operation** | <85 dB during deployment | Phase 2: Acoustic testing |
| **Professional Appearance** | Aesthetic acceptable in clinical setting | Phase 1: Design review; Phase 2: User feedback |
| **Intuitive Operation** | New users can deploy without instructions | Phase 2: User observation testing |
| **Grip/Tactile Feedback** | User can feel confidence in locking (not just hear) | Phase 2: User feedback |

---

## SAFETY REQUIREMENTS

| Specification | Requirement | Notes |
|---|---|---|
| **No Mechanical Faults Without Warning** | Design prevents undetected structural faults | Fail-safe design philosophy |
| **Redundant Locking** | Backup locking if primary lock fails | Mechanical redundancy |
| **Sharp Edges** | All edges radiused or covered | User safety during deployment/collapse |
| **Stability Under Loading** | No unexpected movement during use | User confidence requirement |
| **Documentation** | Clear assembly, use, maintenance instructions | Medical device requirement |

---

## MANUFACTURING REQUIREMENTS

| Specification | Requirement | Notes |
|---|---|---|
| **Repeatability** | ±0.1 inch tolerance tolerance stack | Quality consistency at scale |
| **Part Count** | <50 unique parts | Design for simplicity |
| **Assembly Time** | <30 minutes per unit (prototype) | Scales with automation |
| **Yield** | >95% first-pass yield | Quality target |
| **Traceability** | Serial number + lot tracking | Medical device requirement |

---

## REGULATORY REQUIREMENTS (PRELIMINARY)

| Specification | Requirement | Notes |
|---|---|---|
| **FDA Classification** | TBD (Class I, II, or III) | Remington Medical to determine |
| **Quality System** | ISO 13485:2016 compliant | Medical device manufacturing standard |
| **Risk Analysis** | ISO 14971 FMEA completed | Medical device requirement |
| **Biocompatibility** | ISO 10993 series (if applicable) | Depends on patient contact |
| **Labeling** | Clear instructions, warnings, specifications | Regulatory requirement |
| **Post-Market Surveillance** | Process defined | Medical device requirement |

---

## VERIFICATION MATRIX

| Requirement | Verification Method | Phase | Status |
|---|---|---|---|
| Load Capacity (800 lbs) | Static load testing | Phase 2 | Planned |
| Deflection (<0.25") | Measurement during load test | Phase 2 | Planned |
| Deployment (<90 sec) | Timing with user | Phase 2 | Planned |
| Weight (≤22 lbs) | Scale measurement | Phase 1 | Planned |
| Cycle Life (10,000 cycles) | Accelerated fatigue testing | Phase 2 | Planned |
| Environmental (temperature, humidity) | Environmental chamber testing | Phase 2 | Planned |
| Safety (no pinch hazards) | Design review + user testing | Phase 1-2 | Planned |
| Corrosion Resistance | Salt fog testing (ASTM B117) | Phase 2 | Planned |
| Manufacturing (repeatability) | Production tolerance stack | Phase 3 | Planned |

---

## SPECIFICATION STATUS & NEXT STEPS

**Current Status:** Version 1.0 — Baseline specifications from PDD

**Phase 1 Actions:**
- Engineering partners will provide feedback on specification feasibility
- Unknowns will be resolved through concept studies
- Specification values may be refined based on engineering analysis

**Phase 2 Actions:**
- All specifications will be tested through prototype
- Revised specifications based on prototype results
- Version 2.0 issued post-prototype (Production specifications)

**Phase 3 Actions:**
- Production specifications finalized
- Manufacturing quality metrics defined
- Version 3.0 issued (Production specifications)

---

**Owner:** Engineering Lead (TBD)  
**Next Review:** Weekly during Phase 1; biweekly during Phase 2; monthly during Phase 3  
**Changes Tracked:** All changes logged with rationale and impact assessment

---

See also:
- Product Definition Document
- Engineering Assumptions Register
- Risk Register
- Verification & Validation Plan