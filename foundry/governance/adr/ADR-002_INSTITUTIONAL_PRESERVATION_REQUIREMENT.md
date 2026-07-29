# ADR-002: INSTITUTIONAL PRESERVATION REQUIREMENT

**Status:** Proposed  
**Date Proposed:** July 29, 2026  
**Owner:** Foundry Editorial System  
**Classification:** Constitutional Governance  
**Authority:** Founder Directive  

---

## CONTEXT

During the establishment of ADR-001 and MC-001, a critical operational discipline emerged:

**Architectural and specification work that remains in conversation is not institutional work.**

Foundry's purpose is to preserve institutional knowledge across time, people, and technology changes. Architectural decisions that exist only in chat transcripts or scratchpad files are at risk of being:
- Lost when conversations are archived
- Misremembered by future operators
- Inconsistently applied across components
- Undocumented for auditing and accountability

This ADR formalizes the discipline that emerged through MC-001's development: **No Foundry work session is complete until it is institutionally preserved.**

---

## DEFINITION OF TERMS

### Operational Completion
Work is operationally complete when:
- Specification is documented
- Decisions are recorded
- Design is ratified
- All planning is finished

Operationally complete work exists in files, documents, and designs. It is ready but not yet institutional.

### Institutional Preservation
Work is institutionally preserved when:
- Documentation exists in the canonical repository
- Changes are committed to Git
- Commits are pushed to GitHub
- Working tree is verified clean
- Commit SHA is recorded in the session log
- Foundation Closeout Report is generated

**Institutional preservation is mechanical.** It answers: "Is this work in the permanent institutional record?" 

Institutional preservation does NOT require Founder approval. It is the act of moving work from planning into the permanent institutional record. A piece of work can be institutionally preserved without being Founder-approved.

### Founder Acceptance
Work receives Founder acceptance when:
- Founder has reviewed the preserved work
- Founder has approved the approach, quality, or governance
- Founder has recorded their approval in the institutional record

**Founder acceptance is governance.** It answers: "Does the Founder approve this work as institutional law?"

Founder acceptance requires explicit Founder decision and is recorded independently from preservation.

### Institutional Completion
Work is institutionally complete when:
- Institutional preservation is accomplished AND
- Founder acceptance is recorded

Institutional completion represents the full lifecycle: work has been preserved AND approved.

---

## LIFECYCLE STATES

Foundry work sessions follow this lifecycle, where Institutional Preservation and Founder Acceptance are independent events:

### Phase 1: Operational Completion
```
Status:                    OPERATIONALLY COMPLETE
Institutional Preservation: N/A (not yet)
Founder Acceptance:        N/A (not yet required)
Example: Specification written, design finalized, ready for repository integration
```

At this point:
- ✓ Work is documented
- ✓ Decisions are explicit
- ✓ Plan is clear
- ❌ Work is not yet in the repository
- ❌ Work is not yet institutional

### Phase 2: Institutional Preservation (Independent)
```
Status:                    INSTITUTIONALLY PRESERVED
Institutional Preservation: COMPLETE
Founder Acceptance:        PENDING (independent decision)
Example: Documentation committed to repository, GitHub synchronized, work is permanent
```

At this point:
- ✓ Work is in the repository
- ✓ Changes are committed and pushed to GitHub
- ✓ Repository is clean
- ✓ Work is preserved for future operators
- ✓ Work is protected and permanent
- ⏳ Founder acceptance is a separate, independent decision

**Key Point:** Founder does not need to approve the work for it to be institutionally preserved. Preservation is the Repository Steward's responsibility. Acceptance is the Founder's responsibility.

### Phase 3: Founder Acceptance (Independent)
```
Status:                    INSTITUTIONALLY PRESERVED + FOUNDER ACCEPTED
Institutional Preservation: COMPLETE
Founder Acceptance:        APPROVED
Example: Founder has reviewed and approved the preserved work
```

At this point:
- ✓ Work is in the repository
- ✓ Work has been Founder-approved
- ✓ Work is constitutional law
- ✓ Preservation and acceptance are both recorded

### Phase 4: Institutional Completion
```
Status:                    INSTITUTIONALLY COMPLETE
Institutional Preservation: COMPLETE
Founder Acceptance:        APPROVED
Example: Full lifecycle: work is preserved and accepted
```

At this point, all governance requirements are satisfied.

---

## MANDATORY PRESERVATION STEPS

Every Foundry work session shall conclude with the following preservation steps, performed by the Repository Steward unless explicitly directed otherwise:

### Step 1: Directory Structure
Create or update the appropriate Foundry directory structure:
```
/finding-my-wei/foundry/
├── governance/       (ADRs, policies, rules)
├── editorial-systems/ (publication-specific components)
├── design-system/    (reusable design assets)
└── roles/           (role definitions and responsibilities)
```

### Step 2: Documentation Integration
Move all work from planning/scratchpad into canonical repository locations:
- Specifications → appropriate component directory
- ADRs → `/foundry/governance/adr/`
- Design documents → `/foundry/design-system/`
- Role definitions → `/foundry/roles/`

### Step 3: Cross-References
Update all indexes and cross-references:
- Update parent README files to reference new components
- Link related ADRs and specifications
- Create navigation trails for future operators

### Step 4: Git Commit
Create a descriptive commit:
- Use present tense, imperative mood
- Reference component IDs and ADR numbers
- Include status information (Proposed, Build Authorized, etc.)
- Co-author with Founder where applicable

Example:
```
Establish Foundry Architectural Preflight governance (ADR-001) 
and MC-001 component specifications

Status: ADR-001 Proposed, MC-001 Build Authorized
```

### Step 5: GitHub Push
Push the commit to the origin remote:
```bash
git push origin main
```

### Step 6: Verification
Verify the working tree is clean:
```bash
git status  # Should show no staged or unstaged changes for Foundry work
```

### Step 7: Foundation Closeout Report
Generate the mandatory Foundation Closeout Report (detailed below).

---

## FOUNDATION CLOSEOUT REPORT (Mandatory)

Every Foundry work session shall conclude with this report format:

```
═══════════════════════════════════════════════════════════════════════════
FOUNDATION CLOSEOUT REPORT

Session:                      [Session Name/Date]
Repository Updated:           YES / NO
Git Commit Created:           YES / NO  
GitHub Synchronized:          YES / NO
Working Tree Clean:           YES / NO

Commit Information:
  Short SHA:                [7-character SHA]
  Full SHA:                 [40-character SHA]
  Message:                  [Commit message]
  Remote:                   [GitHub URL]

Institutional Preservation:   COMPLETE / PENDING
Founder Acceptance:           APPROVED / PENDING / NOT YET REQUIRED

Files Added:
  - [file 1]
  - [file 2]
  - [file N]

Institutional Changes:
  1. [Change 1]
  2. [Change 2]
  3. [Change N]

Outstanding Actions:
  1. [Action 1]
  2. [Action 2]
  - [Action N]

═══════════════════════════════════════════════════════════════════════════
```

**Note:** This report is the institutional record of what was preserved. It is not optional. Every Foundry session concludes with this report.

**Key:** Institutional Preservation and Founder Acceptance are independent fields. Preservation is mechanical (yes/no). Acceptance is governance (approved/pending/not required).

---

## DEFINITION OF DONE (For Repository Steward)

A Foundry work session is NOT complete until ALL of the following are true:

1. ✓ Documentation exists
2. ✓ Repository is updated with new/modified files
3. ✓ Cross-references and indexes updated
4. ✓ Git commit created with descriptive message
5. ✓ Changes pushed to GitHub (origin/main)
6. ✓ Working tree verified clean (`git status`)
7. ✓ Commit SHA recorded in the Foundation Closeout Report
8. ✓ Foundation Closeout Report generated and approved by Founder
9. ✓ Institutional status is INSTITUTIONALLY COMPLETE

If any step is incomplete, the session remains: `INSTITUTIONALLY PENDING`

---

## RELATED ADRs AND DOCUMENTS

- **ADR-001** — Architectural Preflight Requirement (governs specification quality)
- **ADR-002** — This document (governs institutional preservation discipline)
- **FOUNDER_REVIEW_PROTOCOL.md** — How Founder approves work
- **CHANGE_CONTROL.md** — How changes to locked components are governed

---

## CONSTITUTIONAL PRINCIPLES

### Institutional Preservation
**No Foundry work is complete until it is institutionally preserved.**

This is not bureaucracy. This is institutional continuity. When a Founder retires, when a Repository Steward moves on, when a technology changes — the institutional knowledge must survive. It survives because it is documented, committed, preserved, and approved.

Work that stays in conversation disappears. Work that is institutionally preserved survives.

### Preservation and Acceptance
**Institutional preservation protects the work. Founder acceptance governs the work. These are complementary but independent events.**

- **Institutional Preservation** is the Repository Steward's responsibility. It is mechanical and deterministic. Either the work is in the repository or it is not.
- **Founder Acceptance** is the Founder's responsibility. It is governance. Either the work is approved or it is not.

A work session can be institutionally preserved without Founder acceptance. But no work session is complete without institutional preservation, regardless of Founder acceptance status.

In practice:
- Repository Steward preserves all completed Foundry work (mandatory)
- Founder reviews and accepts work according to governance needs (as required)
- These responsibilities remain independent and do not block each other

### Separation of Duties
**Repository Steward certifies preservation. Founder certifies acceptance. Neither role certifies the responsibilities of the other.**

This separation prevents rubber-stamping and ensures that:
- Repository Steward cannot declare work Founder-approved (not their role)
- Founder cannot declare work mechanically preserved (relies on Repository Steward verification)
- Each role owns their certification and is accountable for its accuracy

Founder Acceptance requires independent review of the institutional artifacts themselves, not automatic approval based on a report that work was completed.

---

## ADOPTION

Upon Founder approval:

1. ADR-002 becomes constitutional law
2. All Repository Steward responsibilities include preservation by default
3. Every future Foundry session concludes with Foundation Closeout Report
4. No session is marked complete until institutional status is achieved

---

**ADR-002 Version:** 1.0  
**Status:** Proposed (Awaiting Founder Approval)  
**Constitutional Classification:** Governance  
**First Application:** This session (July 29, 2026)
