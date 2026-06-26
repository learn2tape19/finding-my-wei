# System Architecture
## Sidekick Air Structural Support System (S4)

**Project:** Project Atlas 02 — Stand Architecture Initiative  
**Document Purpose:** Define all subsystems and their interfaces  
**Owner:** Engineering Lead (TBD)  
**Status:** Framework (to be populated during Phase 1)  
**Last Updated:** 2026-06-25

---

## System Context

The Sidekick Air Structural Support System (S4) is one subsystem within the broader Sidekick Air ecosystem.

```
SIDEKICK AIR ECOSYSTEM
├── Inflatable Platform (separate project)
├── Structural Support System (S4) ← This document
├── Interface System (connection between inflatable + structural)
├── Transport System (case, packaging)
└── Accessories Ecosystem (future)
```

This document focuses exclusively on the Structural Support System and its subsystems.

---

## S4 Subsystem Breakdown

### Subsystem 1: Primary Frame Structure

**Purpose:** Load-bearing architecture; supports inflatable platform and human load

**Components:**
- Main frame members (legs, crossbraces, trusses)
- Joint connections
- Fasteners
- Finish/coating

**Interface Points:**
- Connects to Inflatable Platform Interface subsystem
- Connects to Locking Mechanism subsystem

**Design Unknowns:**
- Material (aluminum vs. composite)
- Topology (truss, frame, shell)
- Number of legs (3, 4, 6?)

**Acceptance Criteria:**
- Supports 800+ lbs static load
- Deflection <0.25"
- Weight ≤22 lbs
- Deployment capable

---

### Subsystem 2: Deployment Mechanism

**Purpose:** Enables transition from collapsed to deployed state; actuates frame expansion

**Components:**
- Hinges/pivot points
- Spring elements (if spring-assisted)
- Actuator (manual, gravity, powered)
- Control linkages

**Interface Points:**
- Connects primary frame structure at joints
- May connect to locking mechanism

**Design Unknowns:**
- Deployment actuation method (gravity? manual? spring?)
- Number and location of hinges
- Spring vs. manual approach
- Active vs. passive deployment

**Acceptance Criteria:**
- Full deployment <90 seconds
- No tools required
- Quiet operation
- Repeatable (10,000+ cycles)

---

### Subsystem 3: Locking Mechanism

**Purpose:** Maintains structural rigidity in deployed state; prevents unintended collapse

**Components:**
- Latches or locks
- Locking hardware
- Release controls
- Feedback indicators (visual, audible)

**Interface Points:**
- Connects to primary frame at joint locations
- User interface (hand operation)

**Design Unknowns:**
- Locking approach (mechanical latches? friction locks? spring locks?)
- Release mechanism (lever? button? push-pin?)
- Redundancy approach
- Feedback signals

**Acceptance Criteria:**
- Maintains position under 800 lb load
- Visible confirmation of lock status
- Audible or tactile feedback
- Repeatable (10,000+ cycles)
- Tool-free operation

---

### Subsystem 4: Inflatable Platform Interface

**Purpose:** Connection between structural support system and inflatable platform; load transfer

**Components:**
- Interface geometry (connection points)
- Hardware (fasteners, connectors)
- Load distribution pads
- Alignment features

**Interface Points:**
- Primary Frame Structure (structural)
- Inflatable Platform (external subsystem)

**Design Unknowns:**
- Number of connection points (2? 4? 8?)
- Connection type (bolted? adhered? mechanical latches?)
- Load distribution approach
- Serviceability (can users disconnect/reconnect?)

**Acceptance Criteria:**
- Tool-free connection/disconnection
- Transfers full load to primary frame
- Aligns inflatable platform correctly
- Withstands 10,000+ connect/disconnect cycles
- No damage to inflatable platform

---

### Subsystem 5: Ground Contact System

**Purpose:** Interface with ground; prevents tipping, distributes load, adapts to uneven terrain

**Components:**
- Foot/pad geometry
- Material (rubber, plastic)
- Grip/friction characteristics
- Wear properties

**Interface Points:**
- Primary frame structure
- Ground/floor (external)

**Design Unknowns:**
- Foot geometry (flat? angled? pivoting?)
- Material selection
- Number of contact points (matches frame legs)
- Adjustability (leveling feet?)

**Acceptance Criteria:**
- Stable on ±2" terrain variation
- No sliding under 800 lb load
- Protects floors (no scratching)
- Replaceable when worn
- Quiet operation (no squeaking)

---

### Subsystem 6: Material & Finish System

**Purpose:** Corrosion protection, durability, biocompatibility, maintenance

**Components:**
- Base material (aluminum, composite, etc.)
- Protective coating (anodizing, paint, etc.)
- Fastener material (stainless steel)
- Compatibility with disinfectants

**Interface Points:**
- All structural components
- Environmental (temperature, humidity, chemicals)

**Design Unknowns:**
- Specific material selections
- Coating approach (anodizing? paint? natural?)
- Fastener standards
- Disinfectant/cleaning compatibility

**Acceptance Criteria:**
- Survives 500+ hours salt fog testing
- Compatible with hospital disinfectants
- No corrosion after 5 years outdoor exposure
- Maintains appearance through use

---

## Subsystem Interfaces

### Critical Interface #1: Primary Frame ↔ Deployment Mechanism

| Aspect | Requirement |
|---|---|
| **Connection Points** | Must be rigid (no slop) in locked state |
| **Stress Transfer** | Hinges must transfer full loads to frame |
| **Repeatability** | Must function identically after 10,000 cycles |
| **Tolerance Stack-up** | Frame alignment must maintain lock functionality |

### Critical Interface #2: Primary Frame ↔ Platform Interface

| Aspect | Requirement |
|---|---|
| **Load Transfer** | Distributed across interface points |
| **Alignment** | Platform must sit level on frame |
| **Disconnection** | Must be tool-free and repeatable |
| **Stress Concentration** | Interface points must not create stress hotspots |

### Critical Interface #3: Locking Mechanism ↔ Primary Frame

| Aspect | Requirement |
|---|---|
| **Engagement** | Latches must fully engage in locked state |
| **Release** | Must release cleanly without binding |
| **Feedback** | User must perceive lock/unlock confirmation |
| **Reliability** | Must not fail or slip from locked state |

### Critical Interface #4: Frame ↔ Ground Contact

| Aspect | Requirement |
|---|---|
| **Stability** | Four-point or equivalent contact |
| **Leveling** | Adapts to ±2" terrain variation |
| **Grip** | No sliding under load |
| **Wear** | Replaceable without frame damage |

---

## Subsystem Interaction Diagram

```
USER
  ↓
[Deployment Mechanism] ← triggers
  ↓
[Primary Frame Structure] ← supports → [Ground Contact System]
  ↓
[Locking Mechanism] ← secures
  ↓
[Platform Interface] → [Inflatable Platform]
  ↓
[Material & Finish] ← protects (entire system)
```

---

## Modular Expansion Architecture

The S4 is designed as a foundation for ecosystem expansion. Future variants will likely:

### Variant 1: Wider Platform
- Wider inflatable platform requires stronger frame
- Longer spans require more cross-bracing
- May add intermediate legs
- Interface subsystem accommodates wider geometry

### Variant 2: Stretcher Configuration
- Longer, narrower platform
- Different load distribution
- Different interface geometry
- Same deployment/locking mechanism (likely)

### Variant 3: Military Variant
- Higher load capacity (1000+ lbs)
- Rugged materials
- Outdoor durability enhanced
- Same basic architecture (scaled)

### Variant 4: Medical Platform
- Motorized height adjustment
- Accessory mounting points
- Sterilization-compatible materials
- Electrical integration

**Architecture Principle:** The core subsystems (frame structure, deployment, locking) should remain conceptually the same across variants. Scaling and material changes allow adaptation.

---

## Subsystem Development Timeline

| Subsystem | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| **Primary Frame** | Concept studies | Design + prototype | Production engineering |
| **Deployment Mechanism** | Concept + feasibility | Prototype + testing | Production validation |
| **Locking Mechanism** | Design + FEA | Prototype + testing | Production validation |
| **Platform Interface** | Design studies | Prototype + compatibility testing | Production documentation |
| **Ground Contact** | Design studies | Prototype + testing | Production documentation |
| **Material & Finish** | Material selection | Prototype + testing | Production specification |

---

## Integration Risks

| Risk | Mitigation | Responsibility |
|---|---|---|
| Frame deflection affects locking | FEA tolerance stack-up analysis; prototype testing | Structural engineer |
| Interface geometry changes | Lock inflatable dimensions early; design interface robustly | Product director |
| Mechanism complexity increases weight | Iterative design optimization; prototype weight validation | Mechanical engineer |
| Corrosion in hinges/latches | Stainless fasteners; protective coatings | Materials engineer |
| Assembly complexity increases cost | Design for assembly (DFA) reviews; cost modeling | Manufacturing engineer |

---

## Document Status

**Current Phase:** Framework definition (v1.0)

**Phase 1 Deliverables (Engineering Design):**
- Detailed subsystem specifications
- Interface control documents (ICDs)
- Subsystem design selections

**Phase 2 Deliverables (Prototype):**
- Subsystem CAD models
- Assembly drawings
- Updated interface documentation

**Phase 3 Deliverables (Production):**
- Production engineering drawings
- Manufacturing procedures
- Quality inspection criteria

---

**Owner:** Engineering Lead (TBD)  
**Next Review:** Weekly during Phase 1  
**Updates:** As subsystem designs are finalized

---

See also:
- Product Definition Document
- Engineering Requirements Specification
- Risk Register