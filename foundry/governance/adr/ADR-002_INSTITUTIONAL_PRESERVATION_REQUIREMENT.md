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

Institutional preservation is the act of moving work from planning into the permanent institutional record.

### Institutional Completion
Work is institutionally complete when:
- Institutional preservation is accomplished
- Founder has reviewed and approved the result
- The work has been marked as Approved in the institutional record

Institutional completion includes both preservation and approval.

---

## LIFECYCLE STATES

Every Foundry work session follows this lifecycle:

### Phase 1: Operational Completion
```
Status: OPERATIONALLY COMPLETE
Founder Approval: NOT YET REQUIRED
Example: Specification written, design finalized, ready for implementation
```

At this point:
- ✓ Work is documented
- ✓ Decisions are explicit
- ✓ Plan is clear
- ❌ Work is not yet in the repository
- ❌ Work is not yet institutional

### Phase 2: Institutional Preservation
```
Status: INSTITUTIONALLY PENDING
Founder Approval: PENDING
Example: Documentation committed to repository, GitHub synchronized
```

At this point:
- ✓ Work is in the repository
- ✓ Changes are committed and pushed
- ✓ Repository is clean
- ✓ Work is preserved for future operators
- ❌ Work has not yet received Founder approval

### Phase 3: Institutional Completion
```
Status: INSTITUTIONALLY COMPLETE
Founder Approval: APPROVED
Example: Founder has reviewed and approved the preserved work
```

At this point:
- ✓ Work is in the repository
- ✓ Work has been approved
- ✓ Work is constitutional law

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
═══════════════════════════════════════════════════════════════
FOUNDATION CLOSEOUT REPORT

Session:                   [Session Name/Date]
Repository Updated:        YES / NO
Git Commit Created:        YES / NO  
GitHub Synchronized:       YES / NO
Working Tree Clean:        YES / NO

Commit Information:
  Short SHA:             [7-character SHA]
  Full SHA:              [40-character SHA]
  Message:               [Commit message]
  Remote:                [GitHub URL]

Institutional Status:      OPERATIONALLY COMPLETE / INSTITUTIONALLY PENDING / INSTITUTIONALLY COMPLETE
Founder Approval Required: YES / NO
Founder Approval Status:   Pending / Approved / N/A

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

═══════════════════════════════════════════════════════════════
```

**Note:** This report is the institutional record of what was preserved. It is not optional. Every Foundry session concludes with this report.

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

## INSTITUTIONAL PRINCIPLE

**No Foundry work is complete until it is institutionally preserved.**

This is not bureaucracy. This is institutional continuity.

When a Founder retires, when a Repository Steward moves on, when a technology changes — the institutional knowledge must survive. It survives because it is documented, committed, preserved, and approved.

Work that stays in conversation disappears. Work that is institutionally preserved survives.

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
