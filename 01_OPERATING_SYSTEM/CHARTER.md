# Operating System Layer Charter

## Authority
Established by Drew Freedman under the Repository Constitution v2.0.

## Purpose
This layer defines **how the IEMS operates**.

It governs:
- Collaboration principles and culture
- Memory systems and knowledge capture
- Automation and daily operations
- AI assistant guidelines and roles
- Production playbooks and proven recurring workflows
- Tools and technical infrastructure

## Scope

### Inclusion Criteria
- Collaboration principles (SOUL.md, PRINCIPLES.md)
- Memory systems (MEMORY/, memory capture protocols)
- Automation and triggers (HEARTBEAT.md, TRIGGERS.md)
- AI assistant guidelines (CLAUDE_LIBRARIAN.md, CHATGPT_RESEARCH.md)
- Canonical operating playbooks, including PRODUCTION_PLAYBOOK.md
- Operational tools and infrastructure
- System preferences and settings

### Exclusion Criteria
- Domain-specific operations → go to 05_DOMAINS/[domain]/
- Capability standards → go to 04_CAPABILITIES/[service]/
- Research → goes to 02_PROJECT_ATLAS
- Permanent knowledge → goes to 03_INTELLECTUAL_ESTATE
- Governance and amendments → go to 00_CONSTITUTION

## Governance

**Authority:** Drew Freedman (final approval), Claude (maintenance)

**Decision Process:**
1. Operational changes are proposed by Claude, ChatGPT, or Drew
2. Impact on other layers is assessed
3. Changes are implemented in subordinate files
4. Constitutional layer is consulted for conflicts
5. Proven real-world operating patterns may be promoted into canonical playbooks without redesigning the constitutional architecture

**Amendment Speed:** As-needed (operational layer is dynamic)

## Subdirectories

### MEMORY/
- **Purpose:** Long-term knowledge about projects, users, patterns
- **CHARTER.md:** Defines what gets remembered and why
- **Governance:** Claude maintains, Drew reviews
- **Lifecycle:** Living, continuously updated when meaningful

### AUTOMATION/
- **Purpose:** Automated behaviors (daily brief, triggers, workflows)
- **CHARTER.md:** Defines what automations exist and their rules
- **Governance:** Claude implements, Drew approves changes
- **Lifecycle:** Evolves with operational needs

### AI_GUIDELINES/
- **Purpose:** How Claude and ChatGPT operate within the system
- **CHARTER.md:** Defines roles, responsibilities, boundaries
- **Governance:** Drew sets guidelines; AI collaborators follow them
- **Lifecycle:** Refined through use

## Canonical Playbooks

### PRODUCTION_PLAYBOOK.md
Defines the reusable production pattern proven through live publication cycles. Issue-specific receipts remain with their campaigns as evidence; the playbook captures the operating doctrine.

## Lifecycle States
- **CREATION** → New operational procedure
- **REFINEMENT** → Testing and feedback
- **STABLE** → Established and documented
- **DORMANT** → Intentionally inactive; preserved without recurring maintenance until a meaningful trigger reactivates it
- **ARCHIVE** → Retired procedure retained for historical value

Dormancy is a valid healthy state. The existence of a process or project does not create an obligation to generate activity.

## Relationships
- **Serves:** All other layers (source of operational consistency)
- **Receives from:** Domains and active production (feedback on what actually works)
- **Uses:** Shared capabilities and tools
- **Reports to:** 00_CONSTITUTION (must comply)

## Success Metrics
- Collaborators know how to work within the system
- Memory captures learning without degradation
- Automation reduces friction without introducing errors
- AI assistants understand their roles and boundaries
- Proven workflows become simpler and more repeatable over time
- Dormant work can remain quiet without generating administrative burden
- Operations run smoothly day-to-day

## Last Updated
September 29, 2026

## Amendments
- September 29, 2026 — Recognized canonical production playbooks and DORMANT as a healthy operational lifecycle state based on real-world use.
