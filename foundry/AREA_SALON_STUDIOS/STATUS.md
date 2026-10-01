# AREA Salon Studios — Status Record

**Mission Expression:** Freedman-Foundry  
**Status:** Prospect OS architecture authorized; AREA HQ positioned as system of record; occupancy-first marketing remains active  
**Last Updated:** October 1, 2026  
**Authority:** Drew Freedman

---

## Current Phase

AREA has moved beyond basic occupancy-first marketing execution into the design of a unified prospect and operating workflow centered on **AREA HQ**.

The October 1, 2026 working session with Mark Ohanian established the next operating direction:

> **AREA HQ should become the single source of truth from first inquiry through qualification, pipeline, tour/reservation, licensee conversion, and onboarding.**

The Business Fit Calculator is now treated as the front door to an emerging **AREA Prospect OS**, not merely a website form.

Occupancy-first marketing remains active, but the lead-handling architecture is changing materially.

---

## Prospect OS — Authorized Direction

### Core architecture

```
Website / Social / QR
        ↓
Business Fit Calculator
        ↓
AREA HQ Prospect Record
        ↓
Qualification / Fit State
        ↓
Pipeline / Follow-up
        ↓
Tour / Reservation
        ↓
Licensee Conversion
        ↓
Onboarding
```

### Design principles

- AREA HQ becomes the persistent prospect record.
- Returning prospects should be recognized and appended to an existing history rather than treated as anonymous new inquiries.
- Qualification should identify readiness without discarding people who may become viable prospects later.
- Prospect information should not be repeatedly re-keyed across forms, spreadsheets, email, and HQ.
- The system should preserve privacy for prospects who have not publicly announced a move.
- Tour scheduling should reflect real demand and operating efficiency without stacking prospects physically on top of each other.

---

## Business Fit Calculator

The calculator remains intentionally short. Mark Ohanian supported the current scale of roughly **eight questions**.

### Current intent

The opening questions establish financial/business readiness, including:

- years in practice,
- weekly service revenue,
- weekly client volume,
- current work model,
- and related indicators of independence readiness.

The calculator should not simply return a vague narrative. Every completed path should communicate a clear state.

Recommended result-state framework:

- **Strong Business Fit**
- **Building Toward Independence**
- **Early Exploration**

These states should guide internal follow-up while keeping future prospects in the system rather than rejecting them.

### Immediate UX refinement

A first-use test during the October 1 call exposed one issue: the weaker-fit path did not feel sufficiently conclusive to the user. The underlying qualification logic can remain largely intact, but the result-state presentation should become clearer.

---

## Prospect Schema — Design Before Build

Before changing AREA HQ, the prospect model should be mapped offline.

The intended prospect record should include:

1. **Identity**
   - prospect ID
   - first name
   - last name
   - email
   - phone

2. **Business profile**
   - profession / service category
   - years in practice
   - current work model
   - weekly revenue
   - weekly client volume

3. **Qualification**
   - raw calculator inputs
   - derived fit state
   - readiness notes
   - business-risk / development indicators

4. **Location / opportunity interest**
   - preferred AREA location(s)
   - profession-specific space needs
   - vacancy match
   - future-opportunity match

5. **Pipeline**
   - new
   - qualified
   - nurture / future prospect
   - tour
   - reservation / deposit
   - converted
   - closed / inactive

6. **Interaction history**
   - inquiry dates
   - calculator submissions
   - calls
   - texts
   - tours
   - follow-up activity

7. **Outcome**
   - converted licensee
   - future nurture
   - no-fit / closed
   - merged duplicate

### Required behavior

- deduplicate or reconcile repeat inquiries,
- allow a returning prospect to retain prior context,
- preserve interaction history,
- support location matching,
- support future follow-up,
- and convert/attach to an existing licensee without creating unnecessary duplicates.

---

## AREA HQ — Next Technical Gate

Mark is moving private dependencies away from personal accounts and toward AREA-controlled identity so Drew can receive proper backend access.

Before making schema changes:

1. inventory the current data model,
2. inspect existing prospect fields,
3. inspect current forms,
4. inspect pipeline/status logic,
5. inspect automations,
6. inspect API/webhook capabilities,
7. identify what already exists,
8. then add only the missing pieces.

Do **not** begin by rebuilding functionality AREA HQ already provides.

The Prospect OS should be mapped before using HQ's AI builder so implementation is deliberate rather than iterative credit-burning experimentation.

---

## Superseded Lead Architecture

The September 17 status described the following as the primary unresolved lead infrastructure:

```
Squarespace → Zapier → Google Sheets
```

That path had tested successfully once but was not production-stable.

As of October 1, this is no longer the target architecture.

The Google Sheet may remain useful as a temporary audit/reference artifact, but the strategic direction is now:

```
Business Fit Calculator / Intake → AREA HQ
```

AREA HQ, not Google Sheets, is intended to become the durable system of record.

This supersedes the prior "Known Gap — Lead Automation" framing from September 17.

---

## Occupancy-First Direction — Still Active

Marc Harris and Ed Champy previously confirmed alignment with occupancy as the immediate marketing priority.

Approved positioning remains centered on:

- ownership,
- independence,
- profitability,
- freedom,
- and selective fit rather than generic "suite for rent" advertising.

The four-week social rollout and broader vacancy-generation work remain valid.

Primary conversion logic should now evolve from:

**Visibility → Inquiry → Tour → Tenant**

to:

**Visibility → Inquiry → Qualification → Prospect Record → Follow-up → Tour → Reservation → Licensee**

---

## Vacancy Inventory — Historical Reference

As of September 17, 2026:

- **AREA 56:** 1 vacant suite
- **AREA 58:** 4 vacant suites — 2 hair, 2 medical/aesthetic
- **Total:** 5 vacant suites

This inventory is retained as historical context and should not be assumed current without re-verification.

---

## Digital Infrastructure

- GA4/GTM: live.
- Google Search Console: live.
- Google Business Profile work: active.
- Website/location cleanup: ongoing.
- AREA 58 Kent Street Membership Suite experience: live.
- Squarespace remains the current public website platform.
- HQ may eventually absorb more website/lead functionality if that produces a cleaner operating architecture.

---

## Google Business Profiles

GBP execution work from September 17 remains part of the AREA record.

The dedicated execution package and result files remain authoritative for what was applied, what was pending Google review, and what remained unresolved at that time.

Do not infer current GBP status solely from those records without a fresh check.

---

## AREA 115 / AREA 129

Mark Ohanian indicated that the single studio currently associated with 115 is intended to be rolled into **AREA 129** operationally/reporting-wise rather than maintained as a separate standalone structure.

Working concept:

- AREA 115 becomes effectively an annex / suite under AREA 129.
- This reduces unnecessary separate LLC/accounting overhead.
- Future reporting should reflect that consolidation once formally completed.

---

## Butterfly / Access Operations

The October 1 call also transferred additional operational knowledge.

Key principles:

- licensees are generally responsible for providing correct information for their people,
- Butterfly tenant records should preserve privacy when a licensee is not yet public,
- business units should align with studio numbers,
- access groups should be assigned consistently,
- visitor access and personal access PINs should be distinguished,
- pre-public businesses may use anonymous presentation settings until launch.

Mark's atypical nail-team setup should be treated as an exception, not the standard onboarding model.

---

## UniFi / Studio Wi-Fi

Drew now has working knowledge of the studio-level UniFi configuration process.

Operational rules discussed:

- AREA-controlled studio Wi-Fi networks are pre-created by studio,
- network identity should stay tied to the physical studio,
- if a business moves, the business should move to the correct studio network rather than carrying the old studio network forward,
- business-facing SSID names may remain generic/private until the business is public,
- AP broadcasting should be checked against physical studio location and coverage.

---

## Door / Access Code Operations

For Quick Lock-style studio doors:

- factory reset may be preferable before assigning a new tenant,
- AREA retains a master/admin code,
- tenant-specific code is then added,
- onboarding records should be used as the source for the tenant code,
- physical changes should be documented so access state is not held only in one person's memory.

---

## Quo / Communications

Quo remains the current phone/text collaboration platform.

Current issue:

- texting/webhook behavior was disrupted after a messaging incident,
- texting through the app is currently impaired,
- Quo itself has not yet been shown to be the wrong platform.

Decision:

> Audit Quo's backend capabilities and configuration before replacing it.

Google Voice and RingCentral may be compared, but migration should only happen if another platform materially improves collaboration, shared texting, routing, or integration.

---

## Maintenance Intake — Secondary Opportunity

A future maintenance workflow was identified:

```
QR / Text Link
      ↓
Guided Maintenance Intake
      ↓
Basic Troubleshooting Questions
      ↓
Structured Request
      ↓
AREA HQ / Maintenance Workflow
      ↓
Tracked Resolution
```

This should remain secondary until the Prospect OS is functioning.

Do not build Prospect OS and Maintenance OS in parallel.

---

## Website Licensee Profiles — Future Enhancement

The current static logo/business presentation can evolve into richer AREA business profiles.

Potential profile content:

- business name,
- specialty,
- short story,
- portfolio/gallery,
- AREA location,
- controlled booking/contact action.

Goal:

> Make AREA look like a collection of legitimate independent businesses, not simply rooms being rented.

Avoid unnecessarily exposing easily harvested contact information or sending visitors away from AREA's site without purpose.

---

## Operating Principle

Drew is now working across a growing stack:

- AREA HQ
- Squarespace
- Google Business Profiles
- Google Analytics / Search Console
- Butterfly
- UniFi
- physical access systems
- Quo
- on-site operations

The system must be documented so Drew does not become the undocumented integration layer.

Operational knowledge should become process, not tribal memory.

---

## Current Priority Order

1. Obtain proper AREA HQ backend access.
2. Freeze the Business Fit Calculator logic except for result-state clarity and already-authorized location cleanup.
3. Map the Prospect OS schema and state machine offline.
4. Audit AREA HQ against that design.
5. Connect calculator → AREA HQ natively.
6. Test with dummy prospects, including a returning prospect / duplicate scenario.
7. Document Butterfly, UniFi, access-code, and onboarding procedures.
8. Audit Quo.
9. Evaluate guided maintenance intake.
10. Build richer licensee/business profiles.

---

## Known Issue — Sitemap

Squarespace Support previously escalated AREA's sitemap-update problem to engineering and applied a manual refresh described as a temporary workaround.

Treat as an open platform issue unless later evidence establishes resolution.

---

## Historical Records Retained

The following September 17 records remain part of the AREA institutional record:

- `GBP_EXECUTION_PACKAGE_2026-09-17.md`
- `GBP_EXECUTION_RESULT_2026-09-17.md`

They should remain intact as execution history.

---

## Strategic Summary

AREA's next stage is not another isolated marketing tactic.

It is the construction of a connected operating system:

> **Generate attention → qualify intelligently → remember every prospect → manage opportunity → convert deliberately → onboard consistently.**

The immediate institutional build is **AREA Prospect OS**, centered on AREA HQ.
