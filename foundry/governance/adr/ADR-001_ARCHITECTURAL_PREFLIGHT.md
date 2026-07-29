# ADR-001: ARCHITECTURAL PREFLIGHT REQUIREMENT

**Status:** Proposed → Upon MC-001 Integration: Accepted  
**Date Proposed:** July 29, 2026  
**Date Accepted:** [Upon MC-001 Repository Integration]  
**Owner:** Foundry Editorial System  
**Classification:** Constitutional Governance  
**Authority:** Founder Directive  

---

## CONTEXT

As Foundry evolves from a collection of projects into an institution, implementation quality can no longer depend upon individual judgment during production.

Historically, implementation often began while architecture was still evolving. This resulted in:
- Moving specifications
- Undocumented assumptions
- Silent design decisions
- Repository drift
- Inconsistent component behavior

The MC-001 Publication Masthead development demonstrated that architectural verification should occur **before implementation begins**, not during.

Without this gate, implementers become architects. Without architects being architects, institutions become inconsistent.

---

## DECISION

**Every Foundry component shall complete an Architectural Preflight before implementation is authorized.**

Architectural Preflight verifies that the specification is sufficiently complete for faithful implementation without requiring the implementer to make architectural decisions.

**Implementation begins only after successful completion of the preflight.**

A component receives authorization to build when the Architectural Preflight reports: `AUTHORIZED TO BUILD`

---

## CONSTITUTIONAL REQUIREMENTS

Every Architectural Preflight shall verify, at minimum:

### 1. Component Identity
The component shall possess:
- Component ID (e.g., MC-001, IA-001)
- Version (e.g., v1.0.0)
- Owner (which institutional system owns this?)
- Status (Production, Draft, Deprecated)
- Dependencies (what must exist before this component?)
- Consumers (who will use this component?)

### 2. Variable Classification
Every element shall be explicitly classified as either:
- **Locked** (immutable, cannot change without architectural review)
- **Editable** (intentionally variable per use case)

No implicit variables are permitted. Ambiguity is resolved before implementation.

### 3. Coordinate System
The specification shall explicitly define:
- Coordinate origin (e.g., top-left at 0,0)
- Canvas dimensions (width, height)
- Spacing system (margins, gaps, gutters)
- Alignment rules (left/center/right)
- Measurement units (pixels, percentages, etc.)

**Principle:** Nothing critical shall remain implied. If implementation depends on it, it shall be documented.

### 4. Asset Identity
Every referenced asset shall include:
- Asset ID (e.g., IA-001, TS-001, CS-001)
- Name (full, unambiguous name)
- Version (e.g., 1.0)
- Repository location (where does it live?)
- Approval status (approved, pending, deprecated)

Canonical assets shall never be inferred or recreated. If an asset is required, it must be identified with precision.

### 5. Future Compatibility
The component shall demonstrate that it remains usable beyond the immediate project.

**Test:** Can this component be used for its intended purpose 25 years from now without redesign?

Foundry components are **institutional assets**, not campaign assets. They must survive institutional changes, technology shifts, and personnel turnover.

### 6. Export Definition
Required deliverables shall be explicitly documented before implementation begins.

Example:
- Working file (.design, .fig, etc.)
- Preview image (JPG, PNG, etc.)
- Version artifacts
- Documentation

### 7. Documentation
Metadata requirements shall be defined before construction begins.

Example:
- Build date format
- Builder identification
- Repository location
- Version history format
- Validation checklist structure

---

## AUTHORIZATION RULE

**Implementation shall not begin until Architectural Preflight reports:**

```
✓ AUTHORIZED TO BUILD
```

If the preflight reports issues, implementation does not start. The specification is revised, the preflight is re-run, and authorization is re-evaluated.

---

## IMPLEMENTATION PRINCIPLE

```
Repository Stewards implement.
Architects design.
Founders approve.

These responsibilities shall remain independent.
```

- **Architect** produces the specification with sufficient completeness that a Repository Steward can implement without making design decisions.
- **Repository Steward** verifies the specification is complete (Architectural Preflight), then implements faithfully without redesign.
- **Founder** approves the result and maintains constitutional authority.

---

## CONSEQUENCES

### Benefits
- Repeatable, deterministic implementation
- Reduced ambiguity during production
- Improved repository integrity
- Institutional continuity across components
- Reduced founder review cycles (fewer surprises)
- Clear separation of concerns

### Trade-offs
- Additional upfront review (1-2 hours per component)
- Slightly longer planning phase

**Evaluation:** The additional review is accepted because it significantly reduces downstream correction, rework, and institutional debt.

---

## FOUNDRY RULE

**Architectural decisions shall occur before implementation.**

**Implementation shall never become architecture.**

If the implementation reveals gaps in the specification, work stops and returns to the architect. The specification is completed, the preflight is re-run, and the component is re-authorized before implementation continues.

---

## CONSTITUTIONAL PRINCIPLE

### Nothing Critical Is Implied

If the institution depends upon it, it shall be documented.

Implied assumptions are the root of institutional drift. Every assumption should be made explicit so that:
- Future operators can understand the decision
- Change can be evaluated consciously rather than accidentally
- Institutional knowledge is preserved rather than lost

---

## FIRST COMPONENT: MC-001

**MC-001: Publication Masthead** is the first Foundry component developed under the Architectural Preflight protocol.

MC-001 demonstrates that:
- ✓ Specification completeness can be systematically verified
- ✓ Ambiguities can be identified and resolved before implementation
- ✓ Separated responsibilities (architect, steward, founder) produce better results
- ✓ Constitutional governance enables faithful implementation

---

## SCOPE

ADR-001 applies to:
- All Foundry components (MC-*, IA-*, TS-*, CS-*, PG-*)
- All editorial systems (Tao, Learn2Tape, AREA, Sidekick Air, future institutions)
- All architectural artifacts that will be reused

ADR-001 does NOT apply to:
- One-time operational work (specific issue, campaign, etc.)
- Experimental or prototype work
- Internal process documents

---

## RELATED DOCUMENTS

- MC-001_BUILD_SPECIFICATION.md (first component to pass ADR-001 preflight)
- FOUNDER_REVIEW_PROTOCOL.md (approval workflow)
- CHANGE_CONTROL.md (governance of changes to locked components)

---

## ADOPTION

**Upon successful integration of MC-001 into the Foundry repository:**

1. ADR-001 becomes constitutional governance
2. All future Foundry components shall follow the Architectural Preflight protocol
3. Historical components shall be evaluated for ADR-001 compliance and updated where necessary
4. The adoption date shall be recorded in the Foundry constitutional changelog

---

## ARCHITECTURAL DECISION HISTORY

| ADR | Date | Status | Component(s) |
|---|---|---|---|
| ADR-001 | 2026-07-29 | Proposed | MC-001 (inaugural) |

---

**ADR-001 Version:** 1.0  
**Status:** Proposed (Awaiting MC-001 Integration)  
**Authority:** Founder Directive  
**Constitutional Classification:** Governance  
**Next Review:** Upon MC-001 Repository Integration
