# Engineering Risk Register
## Sidekick Air Structural Support System (S4)

**Project:** Project Atlas 02 — Stand Architecture Initiative  
**Document Purpose:** Track technical, manufacturing, supply chain, cost, schedule, regulatory, and market risks  
**Owner:** Program Manager (TBD) + Engineering Lead  
**Status:** Living Document (v1.0 — baseline risks identified)  
**Last Updated:** 2026-06-25

---

## Risk Register Methodology

Each risk includes:
- **ID:** Unique identifier
- **Category:** Risk type (technical, manufacturing, supply chain, cost, schedule, regulatory, market)
- **Risk Description:** What could go wrong?
- **Impact:** If it happens, what's the damage?
- **Probability:** How likely? (High/Medium/Low)
- **Severity:** How bad? (Critical/Major/Minor)
- **Priority:** Impact × Probability (determines urgency)
- **Mitigation Strategy:** How will we prevent/handle it?
- **Owner:** Who's responsible?
- **Status:** Identified / Monitoring / Mitigating / Resolved
- **Target Closure:** When should this risk be addressed?

---

## CRITICAL RISKS (Address Immediately)

### RISK #T-01: Airline Portability / Weight Target Unachievable

| | |
|---|---|
| **Category** | Technical |
| **Description** | A structural system supporting 800+ lbs cannot be engineered below 22 lbs within manufacturing feasibility constraints. |
| **Impact** | Product is too heavy to be portable; market viability destroyed. Either weight target increases (loses differentiator) or load capacity decreases (loses performance). |
| **Probability** | Medium (DARPA systems exist at similar ratios; but medical device manufacturing may have constraints) |
| **Severity** | Critical (product viability) |
| **Priority** | HIGH |
| **Mitigation** | Phase 1: CTD and Element 6 evaluate feasibility through concept studies. If unachievable at 22 lbs, escalate to product director for decision: weight relaxation or load reduction. |
| **Owner** | CTD / Element 6 engineers + product director |
| **Status** | IDENTIFIED (awaiting engineering investigation) |
| **Target Closure** | Week 6 of Phase 1 (end of concept studies) |
| **Notes** | This is the primary engineering risk. If unachievable, requires product strategy reassessment. |

---

### RISK #T-02: One-Person Deployment Mechanism Design Too Complex

| | |
|---|---|
| **Category** | Technical |
| **Description** | Achieving one-person deployment in <90 seconds requires a complex mechanism that increases weight, cost, failure modes, and manufacturing difficulty. |
| **Impact** | Deployment becomes cumbersome; product adoption suffers. Or complexity drives up cost beyond acceptable levels. Or mechanism unreliability creates safety concerns. |
| **Probability** | Medium (deployment mechanisms are well-understood, but constraint combination is tight) |
| **Severity** | Major (product market viability affected) |
| **Priority** | HIGH |
| **Mitigation** | Phase 1: CTD evaluates 3-5 deployment approaches (elastic memory, hinges, springs, active motors, hybrid). Trade-off analysis: complexity vs. weight vs. cost vs. reliability. Select optimal balance. |
| **Owner** | CTD mechanism designer |
| **Status** | IDENTIFIED (mechanism approach TBD) |
| **Target Closure** | Week 6 of Phase 1 |
| **Notes** | Multiple valid approaches exist. Engineering task is to identify the optimal trade-off. |

---

### RISK #T-03: Structural Confidence Cannot Be Achieved with Lightweight Design

| | |
|---|---|
| **Category** | Technical |
| **Description** | Users perceive the lightweight system (18-22 lbs) as insufficiently robust to support another human safely. Psychological confidence gap exists even if engineering margins are adequate. |
| **Impact** | Market rejects product due to perceived instability. Company liability exposure if users decline to place patients on the system. |
| **Probability** | Medium (lightweight platforms have succeeded in market; but this is premium therapeutic equipment with high safety expectations) |
| **Severity** | Critical (market viability) |
| **Priority** | HIGH |
| **Mitigation** | Phase 1: Design emphasizes visible structural rigidity (no flexible-looking components). Phase 2: User perception testing with prototype (confidence ratings before/after). If confidence insufficient, relax weight target to improve perceived robustness. |
| **Owner** | Design engineer + user research |
| **Status** | IDENTIFIED (design approach will emphasize confidence) |
| **Target Closure** | Week 12 of Phase 2 (user testing) |
| **Notes** | This is a design + perception challenge, not a pure engineering challenge. Industrial design critical. |

---

## HIGH PRIORITY RISKS

### RISK #M-01: Manufacturing at Scale Introduces Unacceptable Cost

| | |
|---|---|
| **Category** | Manufacturing / Cost |
| **Description** | Prototype can be hand-fabricated efficiently. But scaling to medium volume (1000+ units/year) requires tooling, automation, or subcontracting that increases unit cost above target. |
| **Impact** | Retail price exceeds market expectation (e.g., $1200+ vs. $800-1000 target); market resistance. Or company absorbs cost and profitability becomes unachievable. |
| **Probability** | Medium (complex deployable systems often have manufacturing challenges at scale) |
| **Severity** | Major (profitability affected; may become business non-viable) |
| **Priority** | HIGH |
| **Mitigation** | Phase 1: DFM analysis identifies cost drivers. Phase 2: Prototype with manufacturing cost modeling. Phase 3: Supplier quotes and tooling cost analysis. Early cost modeling prevents surprises at production ramp. |
| **Owner** | Manufacturing engineer + Remington Medical |
| **Status** | IDENTIFIED (DFM analysis in Phase 2) |
| **Target Closure** | Week 16 of Phase 2 (cost modeling) |

---

### RISK #S-01: Supply Chain Disruption (Single-Source Components)

| | |
|---|---|
| **Category** | Supply Chain |
| **Description** | If critical components (special hinges, latches, materials) are available from only one supplier, supply disruption halts production. |
| **Impact** | Production stoppage; customer delivery delays; lost revenue. |
| **Probability** | Medium (specialized deployable system components may have limited suppliers) |
| **Severity** | Major (production impact) |
| **Priority** | HIGH |
| **Mitigation** | Phase 3: Supplier strategy develops dual-sourcing for critical components. Qualify backup suppliers. Build strategic inventory of long-lead items. Design allows component substitution if needed. |
| **Owner** | Zane (supply chain) + Remington Medical (supplier management) |
| **Status** | IDENTIFIED (supplier strategy TBD) |
| **Target Closure** | Week 30 of Phase 3 (supplier qualification) |

---

### RISK #R-01: FDA Classification Requires More Than 510(k)

| | |
|---|---|
| **Category** | Regulatory |
| **Description** | If FDA classifies S4 as Class III (high-risk) device, approval requires full PMA (Pre-Market Approval) instead of simpler 510(k). Dramatically increases timeline and cost. |
| **Impact** | 12+ month FDA approval timeline; $100k+ additional compliance cost; market launch delayed. |
| **Probability** | Low-Medium (depends on predicate device availability and clinical claims) |
| **Severity** | Major (timeline impact) |
| **Priority** | HIGH |
| **Mitigation** | Phase 1: Remington Medical determines FDA classification early. If Class III risk identified, escalate. Develop regulatory strategy to minimize classification risk (e.g., claims positioning, predicate device selection). |
| **Owner** | Remington Medical (regulatory) |
| **Status** | IDENTIFIED (classification TBD in Phase 1) |
| **Target Closure** | Week 4 of Phase 1 |

---

### RISK #Sch-01: Engineering Timeline Slip in Phase 1

| | |
|---|---|
| **Category** | Schedule |
| **Description** | Engineering partners (CTD, Element 6) may require longer than estimated 6 weeks for feasibility analysis. Concept studies may iterate longer than planned. |
| **Impact** | Phase 1 extends beyond 8 weeks; Phase 2 start delayed; overall timeline slips 4-6 weeks. |
| **Probability** | Medium (engineering projects frequently extend estimates) |
| **Severity** | Minor-Major (depends on criticality of timeline) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 1: Tight project management with weekly status checks. Aggressive schedule with buffer built in. If slips occur, escalate early (week 2-3) to adjust downstream phases. |
| **Owner** | Program manager |
| **Status** | IDENTIFIED (schedule management in progress) |
| **Target Closure** | Ongoing (weekly reviews) |

---

## MEDIUM PRIORITY RISKS

### RISK #T-04: Mechanism Wear / Durability Unproven

| | |
|---|---|
| **Category** | Technical |
| **Description** | Deployment hinges, latches, and springs must withstand 10,000 cycles. If wear mechanisms not fully understood, latches may fail prematurely. |
| **Impact** | Warranty failures; user safety concerns; market reputation damage; recall potential. |
| **Probability** | Medium (deployment mechanisms have known wear modes; engineering can mitigate) |
| **Severity** | Major (safety + reputation) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 2: Accelerated fatigue testing (1000+ cycles in lab) with component inspection. Material/finish selection optimized for wear resistance. Wear components designed as replaceable (prevents full system failure). |
| **Owner** | Mechanical engineer + test lab |
| **Status** | IDENTIFIED (testing planned in Phase 2) |
| **Target Closure** | Week 22 of Phase 2 |

---

### RISK #T-05: Material Corrosion in Clinical Environment

| | |
|---|---|
| **Category** | Technical |
| **Description** | Repeated exposure to hospital disinfectants (bleach, IPA, quaternary ammonium) may corrode aluminum, fasteners, or finish faster than expected. |
| **Impact** | Premature corrosion; cosmetic degradation; safety concerns if fastener corrosion is severe; warranty claims. |
| **Probability** | Low-Medium (depends on material/finish selection; proper anodizing prevents this) |
| **Severity** | Medium (durability issue) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 2: Material compatibility testing with hospital disinfectants. Prototype exposed to harsh cleaning; inspect for degradation. Specify stainless fasteners; specify anodized aluminum if selected. |
| **Owner** | Materials engineer |
| **Status** | IDENTIFIED (testing planned in Phase 2) |
| **Target Closure** | Week 18 of Phase 2 |

---

### RISK #H-01: User Pinch Hazard During Deployment

| | |
|---|---|
| **Category** | Safety |
| **Description** | The deployment mechanism may create pinch points where user fingers could be caught during deployment, especially during force application. |
| **Impact** | User injury; liability exposure; product recall; market credibility damage. |
| **Probability** | Medium (deployment mechanisms have known pinch-point risks) |
| **Severity** | Critical (safety) |
| **Priority** | CRITICAL |
| **Mitigation** | Phase 1: Design review for pinch points; guarding design into mechanism. Phase 2: User observation testing for hazards; video analysis for near-misses. If pinch hazard exists, redesign mechanism with guards. |
| **Owner** | Safety engineer + design engineer |
| **Status** | IDENTIFIED (design review in Phase 1) |
| **Target Closure** | Week 2 of Phase 1 (design review) |

---

### RISK #C-01: Cost Overrun Due to Material Selection

| | |
|---|---|
| **Category** | Cost |
| **Description** | If carbon fiber is selected for weight optimization, material cost may be 3-5x higher than aluminum, driving unit cost above target. |
| **Impact** | Retail price exceeds budget; either company absorbs cost (reduces margin) or retail price increases (loses market competitiveness). |
| **Probability** | Medium (depends on material trade-off decision) |
| **Severity** | Medium (cost impact) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 1: Material trade-off analysis comparing cost, weight, manufacturing. Evaluate cost impact at different production volumes. Select material optimizing cost/weight/manufacturing balance. Phase 2: Supplier quotes confirm cost assumptions. |
| **Owner** | Materials engineer + manufacturing engineer |
| **Status** | IDENTIFIED (material selection TBD) |
| **Target Closure** | Week 6 of Phase 1 |

---

### RISK #M-02: Assembly Complexity Higher Than Estimated

| | |
|---|---|
| **Category** | Manufacturing |
| **Description** | Prototype assembly may take longer than estimated (e.g., 30 min/unit vs. 15 min target). Increases labor cost and reduces production efficiency. |
| **Impact** | Unit cost higher than budget; production capacity lower than planned; timeline to profitability extended. |
| **Probability** | Medium (assembly complexity often underestimated) |
| **Severity** | Medium (cost impact) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 2: Time prototype assembly multiple times with different technicians. Identify bottlenecks. Phase 3: Design for assembly (DFA) optimization reduces assembly time. Prototype assembly process with target operators. |
| **Owner** | Manufacturing engineer |
| **Status** | IDENTIFIED (timing validation in Phase 2) |
| **Target Closure** | Week 20 of Phase 2 |

---

## LOWER PRIORITY RISKS

### RISK #T-06: Vibration / Oscillation During Use

| | |
|---|---|
| **Category** | Technical |
| **Description** | Lightweight frame may oscillate or vibrate during use (e.g., when clinician applies dynamic force). User perceives instability even if structurally safe. |
| **Impact** | User confidence loss; product perceived as "shaky"; market rejection possible. |
| **Probability** | Low-Medium (depends on frame stiffness design) |
| **Severity** | Medium (perception issue) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 1: FEA analyzes natural frequencies and resonance risk. Phase 2: User testing observes for vibration complaints. If vibration exists, design refinement adds stiffness or damping. |
| **Owner** | Structural engineer |
| **Status** | IDENTIFIED (FEA analysis in Phase 1) |
| **Target Closure** | Week 8 of Phase 1 |

---

### RISK #Sch-02: Test Facility Availability Delays Phase 2

| | |
|---|---|
| **Category** | Schedule |
| **Description** | Required test facilities (load testing, fatigue testing, environmental chamber) may have long lead times or booking delays. |
| **Impact** | Phase 2 testing extends; schedule slips 2-4 weeks. |
| **Probability** | Low-Medium (depends on test facility availability) |
| **Severity** | Minor (schedule slip only) |
| **Priority** | LOW |
| **Mitigation** | Phase 2 planning: Reserve test facilities early (Week 1 of Phase 2). Identify backup facilities. Prioritize testing (critical tests first). |
| **Owner** | Program manager |
| **Status** | IDENTIFIED (facilities planning in Phase 2 kickoff) |
| **Target Closure** | Week 1 of Phase 2 |

---

### RISK #Market-01: Market Demand Lower Than Projected

| | |
|---|---|
| **Category** | Market |
| **Description** | Target market (mobile therapists) may have lower demand than business plan projected. Adoption slower than forecast. |
| **Impact** | Revenue lower than budget; business model becomes unviable. May require price reduction or market focus change. |
| **Probability** | Medium (all new product launches face demand risk) |
| **Severity** | Critical (business viability) |
| **Priority** | MEDIUM |
| **Mitigation** | Phase 2-3: User testing and market feedback validates demand assumptions. Early market signals inform business plan adjustment. Pre-launch surveys measure market interest. |
| **Owner** | Product director + marketing |
| **Status** | IDENTIFIED (market validation in Phase 2) |
| **Target Closure** | Ongoing (Phase 2+) |

---

## Risk Status Summary

| ID | Risk | Priority | Status | Owner | Target Closure |
|---|---|---|---|---|---|
| T-01 | Weight/portability unachievable | CRITICAL | Identified | CTD/Element 6 | Week 6 P1 |
| T-02 | Deployment too complex | HIGH | Identified | CTD | Week 6 P1 |
| T-03 | Confidence perception gap | HIGH | Identified | Design/UX | Week 12 P2 |
| M-01 | Manufacturing cost at scale | HIGH | Identified | MFG/Remington | Week 16 P2 |
| S-01 | Supply chain disruption | HIGH | Identified | Zane/Remington | Week 30 P3 |
| R-01 | FDA Class III possibility | HIGH | Identified | Remington | Week 4 P1 |
| Sch-01 | Phase 1 timeline slip | MEDIUM | Identified | PM | Ongoing |
| T-04 | Mechanism wear | MEDIUM | Identified | MFG/Lab | Week 22 P2 |
| T-05 | Material corrosion | MEDIUM | Identified | Materials | Week 18 P2 |
| H-01 | Pinch hazard | CRITICAL | Identified | Safety/Design | Week 2 P1 |
| C-01 | Cost overrun | MEDIUM | Identified | Materials/MFG | Week 6 P1 |
| M-02 | Assembly complexity | MEDIUM | Identified | MFG | Week 20 P2 |
| T-06 | Vibration | MEDIUM | Identified | Structural | Week 8 P1 |
| Sch-02 | Test facility delays | LOW | Identified | PM | Week 1 P2 |
| Market-01 | Demand lower | MEDIUM | Identified | Product/Marketing | Ongoing P2+ |

---

## Risk Review Cadence

- **Phase 1:** Weekly risk reviews (tight schedule; risks evolve rapidly)
- **Phase 2:** Bi-weekly risk reviews (testing reveals new risks)
- **Phase 3:** Monthly risk reviews (manufacturing brings new risks)

---

**Document Owner:** Program Manager (TBD)  
**Status:** ACTIVE — Risk register will be updated weekly  
**Next Review:** Week 1 of Phase 1 (June 26, 2026)

---

See also:
- Engineering Requirements Specification
- Verification & Validation Plan
- Product Definition Document