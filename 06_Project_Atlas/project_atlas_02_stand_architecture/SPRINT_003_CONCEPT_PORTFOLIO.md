# Sprint 003: Concept Architecture Portfolio
## Sidekick Air Structural Support System (S4) — Six Concept Families

**Project:** Project Atlas 02 — Stand Architecture Initiative  
**Phase:** Sprint 003 — Concept Architecture Development  
**Role:** Lead Concept Development Engineer  
**Date:** 2026-06-25  
**Status:** Concept Development (Pre-Engineering)

---

## Portfolio Overview

Six conceptual architectural families are presented for engineering evaluation.

Each concept solves the design challenge through different fundamental approaches.

Each concept introduces specific tradeoffs.

The purpose of this portfolio is to provoke intelligent engineering discussion and identify which concepts deserve detailed feasibility analysis.

---

## CONCEPT 1: SCISSOR-PLUS-SPRING

### Architecture Overview

A scissor mechanism with spring-assisted deployment and mechanical latch locking.

Four diagonal members cross at center hinges. Spring element assists opening. Mechanical latch at each hinge prevents collapse.

### Deployment Sequence

1. User pulls/squeezes grip at center (or releases spring catch)
2. Spring pushes diagonal members apart
3. Frame extends to full height (driven by spring)
4. User guides feet into position
5. Mechanical latches engage automatically as frame reaches full extension (detents or snap engagement)
6. Platform is ready for use

**Deployment Time:** 45-60 seconds (spring-assisted)

### Structural Load Path

```
LOAD ON PLATFORM
       ↓
FOUR CORNER INTERFACES
       ↓
FOUR DIAGONAL MEMBERS (compression + tension)
       ↓
FOUR CENTER HINGES (takes full load through shear and moment)
       ↓
FOUR FEET (distribute to ground)
```

**Critical Point:** Center hinges carry full load in shear. Hinge quality is mission-critical.

### Locking Philosophy

**Active Mechanical Latches:** Each hinge has integral latch that engages when frame reaches full extension. User can physically feel and see lock engagement (confidence signal).

**Redundant Locking:** If one latch fails, other three maintain load (no collapse).

**Release Mechanism:** Squeeze center grip or press button to release all latches simultaneously.

### Transport Configuration

**Folded Dimensions:** 24" × 6" × 3" (highly packable, fits luggage)

**Weight:** 7-9 lbs

**Transport Profile:** Flat suitcase-like package

### Platform Interface

**Connection Type:** Four bolted connection points at diagonal frame corners

**Tool-Free Attachment:** Quick-release pins or camlock fasteners (no wrenches)

**Interface Load Transfer:** Even distribution across four points

### User Interaction

1. Remove from case (unfold legs slightly if needed)
2. Squeeze center grip (spring drives extension)
3. Guide feet to floor (user provides directional control)
4. Release grip (latches engage with audible/tactile feedback)
5. Place platform on frame
6. Deploy complete

**Effort Required:** Moderate (spring does most of work; user guides)

**Noise Level:** Spring snap (loud but brief)

### Manufacturing Approach

**Prototype:** Aluminum extrusion for diagonals; steel hinges with integral latches; compression spring; aluminum frame for center joint

**Production:** Extrusion is standard; hinge manufacturing is precision work; spring sourcing straightforward; assembly is simple

**Estimated Tooling Cost:** Moderate. Hinge design is custom but uses standard manufacturing (machining/stamping).

### Concept Narrative

**Problem Solved:** Scissor mechanism is proven and compact. Spring assistance solves deployment speed requirement without user effort. Mechanical latches provide confidence through visible, audible locking.

**Why Exciting:** Combines proven scissor geometry with spring assistance and redundant locking. Very compact. Fast deployment. High user confidence.

**Key Tradeoff:** Spring mechanism adds complexity (spring selection, integration, maintenance). Hinge precision is critical (tolerances affect deployment).

**Highest Risk:** Hinge fatigue. 10,000 deployment cycles = 40,000 hinge cycles. Spring-loaded hinges see higher stress than passive hinges.

**Engineering Question:** Will COTS hinge + spring combination survive 10,000 cycles at acceptable fatigue margin? Custom hinge design required or sufficient with quality sourcing?

---

## CONCEPT 2: TELESCOPING-WITH-OUTRIGGERS

### Architecture Overview

Central telescoping column (extends vertically) with four outrigger legs that deploy automatically as column extends.

Legs swing out from compact transport position to stable base as column rises.

### Deployment Sequence

1. Remove from transport case (column is nested, legs folded inward)
2. Stand upright and pull column upward
3. As column extends, outrigger legs mechanically deploy (cam mechanism or linkage)
4. Legs automatically spread to stable quad position
5. Feet contact ground; base is stable
6. Column reaches full height; mechanical stop engages

**Deployment Time:** 30-45 seconds (gravity-assisted)

### Structural Load Path

```
LOAD ON PLATFORM
       ↓
CENTER TELESCOPING COLUMN (carries vertical load)
       ↓
FOUR OUTRIGGER FEET (provide lateral stability)
       ↓
GROUND REACTION FORCES
```

**Critical Point:** Column must resist bending from off-center loads. Outriggers must fully deploy to prevent tipping.

### Locking Philosophy

**Mechanical Limit Stops:** Column has end-of-stroke mechanical stop. Cannot extend beyond design height.

**Passive Gravity Locking:** Gravity keeps extension in place. No active latch needed (gravity is lock).

**Optional Active Lock:** Spring-loaded detent for additional security (prevents accidental collapse if bumped).

### Transport Configuration

**Folded Dimensions:** 28" × 8" × 6" (legs folded inward; column nested)

**Weight:** 5-7 lbs

**Transport Profile:** Compact cylinder with folded legs

### Platform Interface

**Connection Type:** Hub or ring at top of column; four or six attachment points around perimeter

**Tool-Free Attachment:** Platform drops onto column hub (gravity locks it on); two quick-pins prevent slipping

### User Interaction

1. Remove from case (already assembled, just needs deployment)
2. Stand upright
3. Pull column upward (feel legs deploy at midpoint)
4. Release (column extends fully with mechanical stop)
5. Verify legs are fully deployed (visual check)
6. Place platform on hub
7. Deploy complete

**Effort Required:** Minimal (gravity does work; user provides pull force)

**Noise Level:** Low (smooth extension, quiet mechanical stop)

### Manufacturing Approach

**Prototype:** Aluminum nested tubes for column; aluminum legs with mechanical deployment cams; simple hub joint; rubber feet

**Production:** Tube extrusion is standard; deployment cam is custom but simple machining; assembly is straightforward

**Estimated Tooling Cost:** Low-Moderate. Cam design is simple; no complex hinges.

### Concept Narrative

**Problem Solved:** Simplest possible mechanism. Minimal parts. Gravity-assisted deployment is fastest. Outrigger legs provide stability without complex geometry.

**Why Exciting:** Fewest moving parts of any concept. Fastest deployment potential (<30 sec). Lowest weight potential. Quiet operation. Intuitive for users (like tent pole).

**Key Tradeoff:** Central column is relatively weak in torsion (single member provides minimal rotational stiffness). Requires outrigger legs to add bracing. Off-center loads create bending in column.

**Highest Risk:** Column bending from off-center loads. If outrigger legs don't fully deploy, stability is lost.

**Engineering Question:** Can column wall thickness be optimized to meet deflection target (<0.25") while staying under weight budget? Are outrigger deployment cams reliable over 10,000 cycles?

---

## CONCEPT 3: QUAD-TRIPOD WITH DIAGONAL BRACING

### Architecture Overview

Four legs (or three + center post) meeting at central hub, with diagonal X-bracing connecting legs for torsional rigidity.

Legs hinge at center; spread outward during deployment; lock in position with mechanical pins or latches.

### Deployment Sequence

1. Unfold legs from compact transport bundle
2. Rotate/spread each leg to deployed angle (approximately 45 degrees from vertical)
3. Slide mechanical pins or engage latches at each leg connection
4. Verify all four legs are locked (visual check of pins)
5. Legs are now in quad-stance position
6. Place platform on central hub

**Deployment Time:** 45-75 seconds (mechanical spreading)

### Structural Load Path

```
LOAD ON PLATFORM
       ↓
CENTRAL HUB
       ↓
FOUR LEG MEMBERS (pure compression with minimal bending)
       ↓
DIAGONAL X-BRACING (resists torsion and lateral movement)
       ↓
FOUR FEET (distribute load, prevent tipping)
```

**Critical Point:** Legs carry primarily axial (compression) loads. Bracing carries shear and torsional forces. Load distribution is efficient.

### Locking Philosophy

**Mechanical Pins Through Hub:** Each leg has locking pin that passes through hub. Pin is secured in locked position (cannot fall out).

**Redundant Geometry:** Four legs provide inherent stability. X-bracing adds redundancy.

**Release Mechanism:** Pull pins; legs rotate down to compact position.

### Transport Configuration

**Folded Dimensions:** 30" × 10" × 8" (legs bundled together with hinges at center)

**Weight:** 6-8 lbs

**Transport Profile:** Compact bundle tied together

### Platform Interface

**Connection Type:** Ring or hub at center; circumferential bolts or quick-release pins distribute load to legs

**Tool-Free Attachment:** Platform has mounting ring that slides onto central hub; two pins prevent rotation

### User Interaction

1. Remove bundle from transport case
2. Loosen holding strap; spread legs outward
3. Insert locking pins through each leg (one pin per leg, feels like tabletop legs)
4. Verify pins are fully seated (audible click or visual confirmation)
5. Place platform on central hub
6. Deploy complete

**Effort Required:** Moderate (mechanical spreading and pinning)

**Noise Level:** Moderate (leg spreading might creak slightly; pins lock with click)

### Manufacturing Approach

**Prototype:** Aluminum tube legs; aluminum central hub with four pin holes; stainless steel locking pins; aluminum diagonal bracing members

**Production:** Extrusion-based legs are simple; hub is precision-machined; pins are standard fasteners; assembly is straightforward

**Estimated Tooling Cost:** Moderate. Hub machining is precision but standard operation.

### Concept Narrative

**Problem Solved:** Quad-tripod combines proven stability with efficient load distribution. Diagonal bracing adds torsional rigidity without significant weight. Mechanical pin locking is simple and visible.

**Why Exciting:** Four-point base is inherently stable. Legs in compression (not bending) means minimal deflection. X-bracing adds confidence. Familiar pattern (looks like professional tripod).

**Key Tradeoff:** Multiple locking pins (four) must be inserted correctly. User must remember to lock all four. Slightly longer deployment than simpler mechanisms.

**Highest Risk:** Pin retention. If pin is inserted incorrectly or falls out, leg could collapse. Requires good pin design with safety tether or keeper chain.

**Engineering Question:** Can pin locking be foolproof? Should pins be captive (tethered) or free? What's the fatigue life of pin holes in aluminum hub after 10,000 cycles?

---

## CONCEPT 4: DOUBLE-SCISSOR (NESTED SCISSOR)

### Architecture Overview

Two scissor mechanisms nested together: outer scissor for primary frame; inner scissor for secondary bracing.

Double mechanism provides redundancy and additional torsional rigidity.

### Deployment Sequence

1. Release latch holding mechanism in transport position
2. Pull/squeeze center control point
3. Spring drives first scissor open
4. Second scissor follows mechanically (linkage couples them)
5. Both scissors reach full extension simultaneously
6. Latches engage on both mechanisms
7. Structure is fully rigid

**Deployment Time:** 50-70 seconds (dual scissor deployment)

### Structural Load Path

```
LOAD ON PLATFORM
       ↓
OUTER SCISSOR FRAME
       ↓
INNER SCISSOR BRACING (adds torsional rigidity)
       ↓
GROUND REACTION FORCES
```

**Critical Point:** Dual load path provides redundancy. If outer scissor partially fails, inner scissor may provide temporary support.

### Locking Philosophy

**Dual Mechanical Latches:** Both scissor mechanisms must lock. Requires all latches to engage for full rigidity.

**Coupled Deployment:** Inner and outer scissor move together. Cannot have one locked and other loose.

**Visual Confirmation:** User sees both scissor mechanisms extend and lock.

### Transport Configuration

**Folded Dimensions:** 26" × 7" × 4" (nested scissor mechanism folds compactly)

**Weight:** 8-10 lbs (heavier due to dual mechanism)

**Transport Profile:** Compact package

### Platform Interface

**Connection Type:** Four connection points on outer scissor frame

**Load Transfer:** Primary load through outer scissors; inner scissors are backup path

### User Interaction

1. Remove from case
2. Squeeze center control (feels like single mechanism from user perspective)
3. Spring drives both mechanisms open
4. Release squeeze; both latches engage
5. Visual/audible confirmation of full deployment
6. Place platform on frame
7. Deploy complete

**Effort Required:** Minimal (spring-driven)

**Noise Level:** Two snap events (loud but acceptable)

### Manufacturing Approach

**Prototype:** Dual scissor frame assembly; linkage coupling both mechanisms; shared spring; dual latches

**Production:** More complex than single scissor but still assembly-based; additional hinge required for inner scissor

**Estimated Tooling Cost:** Moderate-High. Coupling linkage adds complexity.

### Concept Narrative

**Problem Solved:** Redundancy through dual mechanism. If one scissor fails, other provides some support. Inner scissor adds torsional bracing that single scissor lacks.

**Why Exciting:** Engineered redundancy for safety. More torsional rigidity than single scissor. Still faster than tripod. Visually impressive (users see two mechanisms deploy).

**Key Tradeoff:** Increased weight and complexity. More hinges = higher fatigue risk. Coupled linkage between mechanisms is precision point.

**Highest Risk:** Coupling linkage must work perfectly. If coupling fails, mechanisms deploy independently (catastrophic if unbalanced).

**Engineering Question:** Is redundancy necessary? (Single scissor with high-quality hinges may be sufficient.) Can coupling linkage be simplified without losing benefit?

---

## CONCEPT 5: HYBRID SCISSOR-COLUMN WITH ADJUSTMENT

### Architecture Overview

Scissor frame for lateral stability + telescoping column in center for height adjustment.

User can deploy base first (scissor), then adjust height (column), then lock.

### Deployment Sequence

1. Deploy scissor frame (spring-assisted like Concept 1)
2. Once frame is locked, column begins extending (gravity-assisted)
3. User pulls column to desired height
4. Mechanical stop prevents over-extension
5. Column lock engages
6. Structure is fully deployed at desired height

**Deployment Time:** 60-90 seconds (two mechanisms)

### Structural Load Path

```
LOAD ON PLATFORM
       ↓
SPLIT BETWEEN SCISSOR FRAME + CENTER COLUMN
       ↓
SCISSOR: lateral stability and four-point ground contact
COLUMN: primary vertical support
       ↓
GROUND REACTION FORCES
```

**Critical Point:** Load is shared. Column carries axial load; scissor provides lateral constraint.

### Locking Philosophy

**Scissor Latch:** Mechanical latch like Concept 1

**Column Mechanical Stop:** End-of-stroke limit; passive gravity lock supplemented by spring detent

**Dual-Mechanism Lock:** Both must be engaged for full rigidity

### Transport Configuration

**Folded Dimensions:** 28" × 7" × 5" (scissor folded; column nested)

**Weight:** 7-9 lbs

**Transport Profile:** Scissor-like but with column nested in center

### Platform Interface

**Connection Type:** Central hub (top of column) + four scissor frame corners

**Load Distribution:** Primary through column; secondary through scissor corners

### User Interaction

1. Remove from case
2. Deploy scissor frame (spring-assisted, 45-60 sec)
3. Once scissor latches engage, pull center column upward
4. Release column; gravity-assisted extension continues
5. Column reaches desired height; mechanical stop prevents further extension
6. Verify both scissor and column are locked
7. Place platform on interface points
8. Deploy complete

**Effort Required:** Moderate (scissor is automatic; column is manual adjustment)

**Noise Level:** Moderate (scissor snap + column extension)

### Manufacturing Approach

**Prototype:** Scissor mechanism like Concept 1; telescoping column added to center; coupling between mechanisms

**Production:** Combines two proven mechanisms; coupling is new element; more complex assembly

**Estimated Tooling Cost:** Moderate-High. Two mechanisms + coupling.

### Concept Narrative

**Problem Solved:** Combines scissor's stability with column's height adjustability. Allows clinician to set optimal height for each patient.

**Why Exciting:** Addressable height adjustment (feature, not just mechanism). Users can optimize working height. Hybrid approach uses proven mechanisms.

**Key Tradeoff:** Height adjustment complicates mechanism. Two locking systems must both engage. Heavier than single mechanism.

**Highest Risk:** Interface between scissor and column must be robust. If coupling fails, mechanisms can operate independently (bad).

**Engineering Question:** Is height adjustment actually needed? (Initial spec assumes fixed height.) If yes, what's the practical height range (28-36 inches typical)?

---

## CONCEPT 6: ORIGAMI-INSPIRED PANEL FRAME

### Architecture Overview

Flat folding panels connected by hinges in pattern inspired by origami/paper-folding engineering.

Three or four panels fold and unfold to create rigid frame when fully deployed.

### Deployment Sequence

1. Remove flat package from case
2. Unfold first panel (reveals cross bracing)
3. Unfold second panel (creates triangulation)
4. Unfold third panel (if needed, creates redundancy)
5. All hinges lock automatically as panels reach full extension
6. Frame forms rigid structure through geometric locking
7. Place platform on frame

**Deployment Time:** 45-60 seconds (sequential unfolding)

### Structural Load Path

```
LOAD ON PLATFORM
       ↓
MULTIPLE PANEL MEMBERS
       ↓
DISTRIBUTED THROUGH PANEL NETWORK (multiple load paths)
       ↓
GROUND CONTACT POINTS
```

**Critical Point:** Panels are thin members. Rigidity comes from geometry (folding pattern), not section size.

### Locking Philosophy

**Geometric Locking:** Panel edges align and interlock when fully deployed. Hinges lock automatically through mechanical detents (no separate latches needed).

**Self-Aligning:** Panels guide themselves into correct position during deployment (hard to deploy incorrectly).

**Fail-Safe:** If one panel hinge fails, others provide load path (inherent redundancy).

### Transport Configuration

**Folded Dimensions:** 30" × 12" × 2" (very thin; like book)

**Weight:** 4-6 lbs (lightweight structure possible)

**Transport Profile:** Flat suitcase; minimal thickness

### Platform Interface

**Connection Type:** Four or six attachment points around perimeter; platform clamps to top of frame

**Load Transfer:** Distributed across panel perimeter

### User Interaction

1. Remove flat package from case
2. Stand package upright
3. Unfold panels one at a time (sequence is obvious from design)
4. Feel panels lock into place at each step
5. After last panel unfolds, structure is rigid
6. Place platform on frame
7. Deploy complete

**Effort Required:** Low (unfolding is easy; panels are self-guiding)

**Noise Level:** Low (folding hinges are quiet; geometric locking is silent)

### Manufacturing Approach

**Prototype:** Aluminum sheet panels with precision hinges; design requires CAD and FEA to verify panel thickness

**Production:** Panel cutting is standard operation; hinge placement is critical; assembly is simple (panels self-assemble)

**Estimated Tooling Cost:** Moderate. Panel cutting tools are standard; hinge placement requires precision but is not complex.

### Concept Narrative

**Problem Solved:** Origami-inspired approach provides redundancy and lightweight structure. Geometric locking is elegant and foolproof. Compact transport.

**Why Exciting:** Novel approach. Panels create beautiful geometry when deployed. Self-aligning panels are user-friendly. Potential for significant weight reduction.

**Key Tradeoff:** Design is complex (requires sophisticated FEA). Manufacturing precision is critical (hinge placement must be exact). Failure of one hinge affects whole structure differently than other concepts.

**Highest Risk:** Design complexity. Geometry must be precisely engineered. Small errors in panel thickness or hinge placement could cause failure. FEA validation is essential before prototype.

**Engineering Question:** Can panel thickness be optimized to meet deflection and weight targets? What's the fatigue life of panel hinges? Is geometric locking robust enough for clinical use?

---

## CONCEPT COMPARISON MATRIX

| Criterion | Scissor+Spring | Telescoping+Outriggers | Quad+Bracing | Double-Scissor | Hybrid S-C | Origami-Panel |
|---|---|---|---|---|---|---|
| **Deployment** | | | | | | |
| Speed | 8 (45-60 sec) | 9 (<45 sec) | 6 (45-75 sec) | 7 (50-70 sec) | 6 (60-90 sec) | 8 (45-60 sec) |
| Ease | 9 (spring does work) | 10 (gravity does work) | 7 (mechanical pinning) | 9 (automatic) | 7 (two mechanisms) | 9 (self-guiding panels) |
| User Effort | Low | Minimal | Moderate | Minimal | Moderate | Low |
| Noise | 7 (snap) | 5 (low) | 6 (pinning clicks) | 6 (dual snap) | 6 (two events) | 10 (quiet) |
| | | | | | | |
| **Structural** | | | | | | |
| Load Path Clarity | 9 | 8 | 9 | 8 | 7 | 7 |
| Deflection (<0.25") | 7 | 6 | 8 | 8 | 8 | 6 |
| Torsional Rigidity | 6 | 3 | 8 | 8 | 7 | 7 |
| Redundancy | 5 | 2 | 6 | 9 | 6 | 8 |
| Perceived Confidence | 9 | 5 | 9 | 9 | 8 | 7 |
| | | | | | | |
| **Weight & Transport** | | | | | | |
| Weight | 6 (7-9 lbs) | 9 (5-7 lbs) | 7 (6-8 lbs) | 4 (8-10 lbs) | 6 (7-9 lbs) | 9 (4-6 lbs) |
| Transport Compactness | 8 | 8 | 7 | 8 | 8 | 10 (flat) |
| | | | | | | |
| **Manufacturing** | | | | | | |
| Prototype Simplicity | 7 | 8 | 8 | 6 | 5 | 6 |
| Production Simplicity | 7 | 8 | 8 | 5 | 5 | 6 |
| Precision Required | 8 (hinges) | 7 | 8 | 9 | 7 | 9 |
| Tooling Cost | 6 (moderate) | 5 (low-mod) | 6 (moderate) | 7 (mod-high) | 7 (mod-high) | 6 (moderate) |
| | | | | | | |
| **Risk & Durability** | | | | | | |
| Hinge/Joint Fatigue | 6 | 7 | 6 | 5 (dual risk) | 5 (dual risk) | 7 |
| Deployment Reliability | 7 | 8 | 6 | 8 | 6 | 7 |
| Field Serviceability | 8 | 7 | 8 | 6 | 7 | 5 |
| User Error Tolerance | 6 | 9 | 5 (pins must lock) | 9 | 7 | 9 |
| | | | | | | |
| **Innovation & Novelty** | | | | | | |
| Technical Novelty | 6 | 4 | 5 | 7 | 6 | 9 |
| Patent Potential | 6 | 3 | 4 | 7 | 6 | 9 |
| Market Differentiation | 6 | 5 | 7 | 7 | 7 | 8 |

---

## RECOMMENDATIONS FOR ENGINEERING FEASIBILITY STUDIES

### Tier 1: Recommended for Immediate Feasibility Analysis

**#1 TELESCOPING-WITH-OUTRIGGERS**
- **Why:** Lightest weight, fastest deployment, simplest mechanism
- **Concern:** Torsional weakness must be addressed through outrigger design
- **Feasibility Task:** FEA analysis of column bending and outrigger deployment reliability
- **Timeline:** 2-3 weeks to feasibility assessment

**#2 SCISSOR-PLUS-SPRING**
- **Why:** Proven mechanism, good balance, high user confidence
- **Concern:** Hinge fatigue at 10,000 cycles
- **Feasibility Task:** Hinge selection/specification; fatigue analysis; prototype hinge testing
- **Timeline:** 2-3 weeks to feasibility assessment

**#3 QUAD-TRIPOD-WITH-BRACING**
- **Why:** Excellent stability, inherent redundancy, familiar design pattern
- **Concern:** Pin locking must be foolproof; hub design is precision point
- **Feasibility Task:** Hub design analysis; pin retention design; load distribution verification
- **Timeline:** 2-3 weeks to feasibility assessment

### Tier 2: Conditional Development

**#4 HYBRID SCISSOR-COLUMN**
- **Status:** Develop only if height adjustment is confirmed as product requirement
- **Question:** Is fixed height sufficient, or is adjustment necessary?

**#5 ORIGAMI-INSPIRED PANEL**
- **Status:** Develop only if weight must be <5 lbs (current concepts meet <10 lbs)
- **Challenge:** Requires sophisticated panel FEA; highest design complexity

### Tier 3: Not Recommended for Further Development (At This Time)

**#6 DOUBLE-SCISSOR**
- **Reason:** Complexity and weight exceed benefits. Single scissor with high-quality hinges is simpler and achieves same goals.

---

## CONCEPT PORTFOLIO SUMMARY

### Engineering Families Represented

1. **Spring-Assisted Scissor:** Proven mechanism + elegant spring integration
2. **Gravity-Assisted Column:** Simplest possible approach; relies on outrigger stability
3. **Mechanical Tripod:** Familiar pattern; four-point mechanical assembly
4. **Redundant Dual Mechanism:** Over-engineered for safety; complexity not justified
5. **Hybrid Integration:** Feature-rich but complex; conditional recommendation
6. **Geometric Innovation:** Novel approach; requires highest engineering rigor

### Design Principles Observed Across Concepts

✓ **Simplicity Wins:** Concepts 2 (telescoping) and 3 (quad) score highest on manufacturability and user confidence despite different approaches

✓ **Mechanism Selection is Critical:** Spring vs. gravity vs. manual deployment has enormous impact on weight, cost, and user experience

✓ **Redundancy Has Cost:** Double-scissor shows that redundancy adds weight and complexity without proportional reliability gain

✓ **User Confidence is Structural:** Concepts that "feel" stable (quad, scissor) score higher than mechanically equivalent but unfamiliar designs (panel)

✓ **Compactness is Tradeoff:** Telescoping is lightest but weakest in torsion; quad is heavier but stronger; panel is flattest but most complex

### Unresolved Engineering Questions

1. **Is height adjustment necessary?** (Changes design if yes)
2. **What's acceptable hinge fatigue risk?** (Determines hinge specification)
3. **Must mechanism be foolproof?** (Determines pin vs. latch vs. automatic locking)
4. **What's the torsional loading in real use?** (Determines rigidity requirements)
5. **What's the target weight?** (Constrains material and mechanism choices)

---

## NEXT STEPS FOR ENGINEERING TEAM

1. **Select Top Three Concepts** (likely Telescoping, Scissor, Quad based on scores)

2. **Conduct FEA Analysis** for each selected concept:
   - Load distribution under 800 lb centered and off-center loads
   - Deflection analysis (target <0.25")
   - Torsional analysis (how much twist?)
   - Hinge/joint stress and fatigue prediction

3. **Design Interface Details** for each concept:
   - How does platform connect?
   - How are feet designed?
   - How does deployment mechanism lock?

4. **Prototype Planning:**
   - Which concept to prototype first?
   - What's the success criteria?
   - What testing will validate concept?

5. **User Research** (parallel to engineering):
   - Does height adjustment matter?
   - Do users prefer loud/visible locking or quiet/hidden?
   - What's acceptable deployment effort?
   - What builds user confidence?

---

## ARCHITECTURE BOARD VISUAL GUIDES

[SVG diagrams for each concept follow below]

---

## CONCEPT VISUAL: #1 SCISSOR-PLUS-SPRING

```
TRANSPORT (FOLDED):                DEPLOYED:
     _____                         __|__
    |     |                       / O O \
    |_____|                      |  ***  |
    5 lbs                       / |     | \
                              /  |  **  |  \
                             |   |_***_|   |
                             
    Spring inside             Four diagonal
    Center hinges             members at 45°
    Mechanical               angles
    latches

DEPLOYMENT SEQUENCE:
1. Squeeze → Release spring catch
2. Spring pushes diagonals apart
3. Feet spread → stable quad base
4. Latches engage with snap
5. Framework is rigid

LOAD PATH:
Load → Platform edges → 4 corner hinges 
→ Diagonal compression/tension members 
→ Ground feet
```

---

## CONCEPT VISUAL: #2 TELESCOPING-WITH-OUTRIGGERS

```
TRANSPORT:                    DEPLOYED (side view):
    |||||                          |||||
    |||||  4 lbs                   |||||  Legs out
    |||||                          /|||\
                                  / ||| \
                              ----  |||  ----
                            
    Nested tubes            Central column + 4
    Legs folded            outrigger legs
    inside

DEPLOYMENT SEQUENCE:
1. Stand upright
2. Pull column → gravity extends
3. Legs mechanically deploy as column rises
4. Mechanical stop at top → locked
5. Framework is rigid

LOAD PATH:
Load → Platform hub → Central column
(vertical) + 4 outrigger legs
(lateral stability) → Ground feet
```

---

## CONCEPT VISUAL: #3 QUAD-TRIPOD-WITH-BRACING

```
TRANSPORT (bundle):          DEPLOYED (top view):
    ////                          ___/___
    ////  7 lbs                 /    O    \
    ////                        |  O   O   |  Four legs
                                \___O____/    in quad
                                    X-brace
                                    between

    Hinged legs              Each leg pinned
    bundled in              through central
    center joint            hub with mechanic
                           pin/latch

DEPLOYMENT SEQUENCE:
1. Unbundle legs
2. Spread each leg outward (45° angle)
3. Insert locking pins (one per leg)
4. Verify all four pins locked
5. Framework is rigid

LOAD PATH:
Load → Platform hub → 4 legs in compression
→ X-bracing for torsion → Ground feet
```

---

## CONCEPT VISUAL: #4 DOUBLE-SCISSOR

```
TRANSPORT:                  DEPLOYED:
    |||||                     /\__/\
    |||||  8 lbs             /  **  \  Outer scissor
    |||||                   |  /\/\  | Inner scissor
                            \  \  /  /  (nested for
                             \  **  /   bracing)
                              \/  \/

DEPLOYMENT SEQUENCE:
1. Release main latch
2. Squeeze center → spring activates
3. Both scissors open in parallel
4. Both latches engage simultaneously
5. Framework is rigid with redundancy

LOAD PATH:
Load → Platform → Outer scissor frame
→ Inner scissor (coupled linkage)
→ Dual load paths → Ground
```

---

## CONCEPT VISUAL: #5 HYBRID SCISSOR-COLUMN

```
TRANSPORT:                  DEPLOYED:
    __|__                       | (column extended)
   /  |  \  7 lbs              /|   Column
  |   |   |                    | O platform hub
  \ _|_ /                     / \___
   Scissor                   Scissor base
   frame
   (folded)

DEPLOYMENT SEQUENCE:
1. Deploy scissor frame (spring-assisted)
2. Once locked, pull center column
3. Gravity extends column
4. Mechanical stop at desired height
5. Column lock engages
6. Framework is rigid

LOAD PATH:
Load → Platform hub → Split between:
- Central column (vertical support)
- 4 scissor corners (lateral stability)
→ Ground feet
```

---

## CONCEPT VISUAL: #6 ORIGAMI-INSPIRED PANEL

```
TRANSPORT (flat):          DEPLOYED:
  ____________             /\  /\
 |            |  4 lbs    |  \/  |  Three or
 |____________|           \  /\  /  four panels
                           \/  \/   fold into
 Flat like                        rigid structure
 notebook                         through geometric
                                 interlocking

DEPLOYMENT SEQUENCE:
1. Stand flat package upright
2. Unfold panel 1 (creates base)
3. Unfold panel 2 (adds bracing)
4. Unfold panel 3 (adds redundancy)
5. Each hinge locks automatically
6. Framework is rigid

LOAD PATH:
Load → Platform → Distributed across
all panel members → Multiple load
paths through geometry → Ground feet
```

---

## TRADEOFF SUMMARY TABLE

### Fast Deployment vs. Lightweight vs. High Confidence

| Concept | Deployment Speed | Weight Potential | User Confidence | Complexity | Manufacturability |
|---|---|---|---|---|---|
| **Telescoping+Outriggers** | ⭐⭐⭐ (fastest) | ⭐⭐⭐ (lightest) | ⭐⭐ (lowest) | ⭐⭐ (simplest) | ⭐⭐⭐ (easiest) |
| **Scissor+Spring** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ (highest) | ⭐⭐⭐ (moderate) | ⭐⭐ |
| **Quad+Bracing** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ (highest) | ⭐⭐⭐ (moderate) | ⭐⭐ |
| **Double-Scissor** | ⭐⭐ | ⭐ (heaviest) | ⭐⭐⭐ | ⭐⭐⭐⭐ (complex) | ⭐ (hardest) |
| **Hybrid S-C** | ⭐ (slowest) | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ (complex) | ⭐⭐ |
| **Origami-Panel** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ (most) | ⭐ |

**Key Tradeoff:** Speed + Simplicity (Telescoping) vs. Confidence + Stability (Scissor or Quad)

---

## ENGINEERING QUESTIONS FOR DEVELOPMENT TEAM

### Critical Questions (Must Answer Before Prototype Selection)

1. **What is the acceptable hinge/joint fatigue life for the mechanism?**
   - Target 10,000+ deployment cycles?
   - Or is 5,000 cycles acceptable?
   - Affects hinge specification and cost

2. **Is height adjustment a feature requirement?**
   - If yes: Hybrid or Telescoping concept
   - If no: Scissor or Quad concept

3. **What is the acceptable torsional loading in clinical use?**
   - Do therapists apply significant twisting forces?
   - Or is torsion a secondary concern?

4. **What deployment speed is actually necessary?**
   - Is <90 seconds sufficient?
   - Or is <60 seconds a market requirement?

5. **How important is user confidence relative to weight?**
   - Is 5 lb vs. 8 lb significant?
   - Or is four-point visible stability worth extra weight?

### Design Validation Questions (After Concept Selection)

6. **Can hinges be sourced COTS or require custom design?**
7. **What's the outrigger leg deployment reliability for telescoping concept?**
8. **Can quad-tripod pin retention be foolproof without tethering?**
9. **Can panel hinge placement tolerance be held in production?**

---

## CONCEPT PORTFOLIO CONCLUSION

Six fundamentally different approaches to the S4 design challenge have been presented.

**Top three concepts for immediate engineering feasibility analysis:**
1. Telescoping-with-Outriggers
2. Scissor-Plus-Spring
3. Quad-Tripod-with-Bracing

Each concept represents a different engineering philosophy:
- Telescoping: Speed + Simplicity
- Scissor: Balance + Confidence
- Quad: Stability + Familiar Pattern

Further development will reduce uncertainty on feasibility, weight, manufacturing, and user acceptance.

The purpose of this portfolio is to initiate intelligent engineering discussion, not to declare a winner.

Every rejected concept increases confidence in the remaining concepts.

---

**Portfolio Status:** COMPLETE — Ready for Engineering Review  
**Next Action:** Engineering team selects top 3 concepts for FEA and detailed feasibility analysis  
**Timeline:** 2-3 weeks to feasibility reports

---

**Created by:** Lead Concept Development Engineer  
**Date:** 2026-06-25  
**Purpose:** Provoke intelligent engineering discussion through multiple competing concepts