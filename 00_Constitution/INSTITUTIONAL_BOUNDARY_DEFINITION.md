# Institutional Boundary Definition

**Version:** 1.0  
**Status:** RATIFIED (Drew Freedman, Amendment 001)  
**Date Ratified:** July 5, 2026  
**Governance Layer:** Constitutional  
**Authority:** Drew Freedman (Steward)

---

# RATIFICATION NOTICE

This document incorporates Constitutional Amendment 001, which established:
- Five permanent asset classifications (Constitutional, Intellectual, Institutional, Development, Operational Support)
- Institutional lifecycle with review gates
- Stewardship principle (curate over accumulate)
- Graduation test for permanent assets
- Repository health standards
- Migration protection rule
- Repository-first workflow rule

Upon incorporation of these amendments, this document became Version 1.0 and permanent governance.

---

# Core Principle

**Finding My Wei preserves wisdom, not merely information.**

This distinction determines what belongs inside the estate and what remains external.

Wisdom is **understanding-that-compounds over time**. Information is **data-for-now**.

**Finding My Wei exists to preserve wisdom.**

It does not exist to preserve everything.

The responsibility of a steward is not accumulation.

It is thoughtful curation.

Future maintainers should inherit clarity rather than volume.

---

# The Central Question

**Should this knowledge remain discoverable and preserved for Drew Freedman's successors a decade from now?**

If YES → It belongs in Finding My Wei.  
If NO → It belongs in operational systems (Notion, Drive, email, business platforms).

---

# FIVE PERMANENT ASSET CLASSIFICATIONS

Every asset in Finding My Wei belongs to exactly ONE primary classification.

## 1. Constitutional

**Definition:** Documents governing the institution itself.

**Characteristics:**
- Permanent and unchanging (except through formal amendment)
- Defines how the system works
- Establishes authority and governance
- Shapes future decisions

**Examples:**
- Constitution.md
- Executive Directives
- Repository Governance
- Amendment Records
- Stewardship Model
- Charter.md documents
- Role Definitions

**Inclusion Rule:** Automatic (if governance is significant)

**Lifetime:** Permanent (may be amended, never deleted)

**Location:** 00_CONSTITUTION/

---

## 2. Intellectual

**Definition:** Original work intended to become part of the Intellectual Estate.

**Characteristics:**
- Teaches something enduring
- Represents Drew's cumulative learning
- Has compound value with other knowledge
- Survives the Graduation Test

**Examples:**
- Books and manuscripts
- Research papers
- Project Atlas investigations
- Engineering rationale and design decisions
- Clinical philosophy and frameworks
- Teaching methodologies and pedagogical innovation
- Inventions and patents
- Validated methodologies

**Inclusion Rule:** Must pass Graduation Test:
1. Does it teach something enduring? ✓
2. Does it preserve an important institutional decision? ✓
3. Does it represent original thinking? ✓
4. Will it likely remain valuable five years from now? ✓
5. Would Drew regret losing it? ✓

(All 5 must be YES or clear MAYBE; any NO → Consider Development instead)

**Lifetime:** Permanent (once graduated from Development)

**Location:** 02_PROJECT_ATLAS (in progress) → 03_INTELLECTUAL_ESTATE (completed)

---

## 3. Institutional

**Definition:** Records documenting how the institution evolved.

**Characteristics:**
- Preserves decision history (not just outcomes)
- Shows strategic thinking and rationale
- Informs future decisions
- Prevents repeating past mistakes
- Documents relationships and risk history

**Examples:**
- Decision logs with rationale
- Founder logs and reflections
- Strategic pivot records
- Relationship intelligence
- Risk assessments and lessons learned
- Executive reviews and synthesis
- Why-we-chose-X records

**Inclusion Rule:** Include if:
- Multiple people need to know about it, OR
- It affects future decisions, OR
- It's referenced repeatedly in strategic conversations, OR
- It represents more than one person's accumulated learning

**Lifetime:** Permanent (or until no longer strategically relevant)

**Location:** 03_INTELLECTUAL_ESTATE/DECISION_LOGS or appropriate domain history folder

---

## 4. Development

**Definition:** Work that has not yet earned permanent institutional status.

**Characteristics:**
- Created to mature into Intellectual or Institutional work
- Under active review and refinement
- Direction is being determined
- May graduate, remain stable, or be intentionally discarded
- Is NOT permanent by default

**Examples:**
- Draft manuscripts and early research
- Brainstorming and exploratory work
- Prototype concepts and design iterations
- Working notes and rough drafts
- Early campaign material and positioning
- Exploratory research (no clear direction yet)
- In-progress course design
- Unfinished frameworks

**Inclusion Rule:** Include if:
- More than one week of active effort invested, OR
- Collaborators are involved (extends beyond Drew), OR
- Part of documented intention (not random exploration), OR
- Strategic investment is significant

**Lifetime:** Temporary (days to months); reviewed regularly

**Graduation Path:** Development → Review → Classification → (If passes Graduation Test) → Intellectual/Institutional → Permanent

**Location:** Domain PROJECTS/ folder or 02_PROJECT_ATLAS (with clear lifecycle state labeled)

**Special Rules:**
- Development material is intentionally fragile (can be discarded)
- Regular culling recommended (remove abandoned directions)
- Promotion to Intellectual/Institutional requires explicit review and approval

---

## 5. Operational Support

**Definition:** Material required to operate businesses but not to preserve institutional wisdom.

**Characteristics:**
- Temporary by nature
- Needed for current operations
- Can be recreated or is already backed up elsewhere
- Does not represent enduring learning

**Examples:**
- Daily task lists and project management
- Administrative and routine records
- Website operations and CMS content
- CRM and marketing automation exports
- Student enrollment records and transaction data
- Customer financial and personal information
- Credentials, API keys, and secrets
- Temporary working files and scratch work
- Routine business correspondence

**Inclusion Rule:** Generally EXCLUDE from Finding My Wei

**Exceptions:** Include Operational Support IF it documents:
- A decision or methodology (extract to Institutional)
- A business innovation (extract to Intellectual)
- Historical context (archive snapshot only)

**Lifetime:** Temporary (can be deleted when superseded)

**Location:** Notion, Google Drive, business systems (NOT GitHub repository)

**Security Rule:** Never include credentials, API keys, or secrets in repository. Externalize to secure credential management.

---

# INSTITUTIONAL LIFECYCLE

Every asset entering Finding My Wei follows this common lifecycle:

```
Capture
  ↓
Development
  ↓
Review
  ↓
Classification
  ↓
Founder Approval (when required)
  ↓
Permanent Repository
  ↓
Archive (if superseded)
```

## Lifecycle Stages Explained

### Capture
**What:** Work is created or discovered that might belong in Finding My Wei.

**Who Decides:** Creator or Claude

**Process:** Asset is noted; basic information collected

---

### Development
**What:** Work is actively being developed/refined.

**Who Decides:** Creator (in collaboration with Drew if strategic)

**Process:** 
- Work matures toward completion
- Direction becomes clear
- Quality standards are applied
- Feedback is gathered

**Duration:** Variable (days to months)

---

### Review
**What:** Work is examined against institutional standards.

**Who Decides:** Claude (with Drew approval for major pieces)

**Process:**
- Is this worth preserving?
- Does it meet quality standards?
- Should it remain in repository or move elsewhere?
- Does it conflict with other work?

**Required for:** All work intended to be permanent

---

### Classification
**What:** Work is assigned to Constitutional, Intellectual, Institutional, or Development category.

**Who Decides:** Claude (based on Graduation Test and guidelines)

**Process:**
- Apply Graduation Test
- Determine appropriate location
- Set lifecycle state (CREATION/REFINEMENT/STABLE/PUBLICATION/PRESERVATION)
- Identify relationships to other work

---

### Founder Approval
**What:** Drew explicitly approves permanent status.

**Who Decides:** Drew Freedman (required for)

**Required For:**
- Constitutional changes
- Intellectual work moving to PRESERVATION
- Major Institutional decisions (risk history, strategic pivots)
- Any work Drew wants to vet before permanence

**Optional For:**
- Development work (already in repo; not permanent yet)
- Routine Institutional decisions (can be archived without explicit approval)

---

### Permanent Repository
**What:** Work is moved to final location in Finding My Wei.

**Who Decides:** Drew (after approval) or Claude (if pre-approved)

**Process:**
- Asset is indexed and cross-referenced
- Lifecycle state is marked
- Relationships are documented
- Location is committed to GitHub

**Permanence Rule:** Once here, work is protected under Migration Protection Rule

---

### Archive
**What:** Work is superseded, no longer strategically relevant, or intentionally preserved as historical.

**Who Decides:** Drew (for Constitutional/Intellectual/Institutional) or Claude (for Development)

**Process:**
- Asset is moved to ARCHIVE subdirectory
- Reason for archival is documented
- Cross-references are updated
- Historical copy remains accessible

**Permanence:** Archive records are permanent (not deleted)

---

## No Asset May Bypass Review

Every piece of work entering permanent status must pass Review stage.

This is non-negotiable.

---

# GRADUATION TEST

Before any asset becomes permanent, evaluate ALL five questions:

1. **Does it teach something enduring?**
   - Yes: This knowledge helps future work
   - No: This is transient or already captured elsewhere

2. **Does it preserve an important institutional decision?**
   - Yes: Future decisions depend on understanding this choice
   - No: This is routine or minor

3. **Does it represent original thinking?**
   - Yes: Drew's unique contribution; not readily available elsewhere
   - No: This is restatement or common knowledge

4. **Will it likely remain valuable five years from now?**
   - Yes: Timeless or important historical record
   - No: This will be outdated soon

5. **Would the Founder regret losing it?**
   - Yes: This represents significant work or learning
   - No: This can be recreated or is backed up elsewhere

### Passing Criteria

**If all five are YES or clear MAYBE:** Promote to Intellectual or Institutional status.

**If any five are clearly NO:** Consider keeping in Development instead.

**Edge Case:** If 4/5 are YES and 1 is NO → Founder decision (may still preserve for historical value).

### Examples

**Book Manuscript (Passes All 5)**
1. Teaches enduring clinical philosophy ✓
2. Preserves years of clinical thinking ✓
3. Original framework ✓
4. Will matter in 5 years ✓
5. Founder would regret losing it ✓
→ **PRESERVE in Intellectual Estate**

**Daily Task List (Fails Multiple)**
1. Does not teach anything enduring ✗
2. Does not preserve institutional decision ✗
3. Not original thinking ✗
4. Will not matter in 5 years ✗
5. Founder would not regret losing it ✗
→ **KEEP in Notion; DELETE after completion**

**Strategic Pivot Decision (Passes 4/5)**
1. Teaches enduring decision-making principle ✓
2. Preserves important strategic choice ✓
3. Documents original thinking ✓
4. Will matter in 5 years ✓
5. Would Founder regret losing it? Maybe (FOUNDER DECIDES)
→ **PRESERVE in Institutional/Decision Logs (unless Founder says no)**

---

# REPOSITORY HEALTH STANDARD

Repository quality shall be measured by **signal rather than volume**.

A healthy institution continually increases the proportion of enduring intellectual work relative to temporary operational material.

## Health Metrics

### Signal Quality
**Evaluate:** Are archived assets valuable or merely filling space?

**Ideal Ratio:** 80% Intellectual/Constitutional, 15% Institutional, 5% Development (minimal)

**Unhealthy Ratio:** 30% Intellectual, 60% Development/Operational, 10% Institutional

### Discoverability
**Evaluate:** Can future collaborators find what they need?

**Healthy:** Clear navigation; every asset is findable; related work is connected

**Unhealthy:** Duplicates exist; assets are "lost"; no clear relationships

### Governance
**Evaluate:** Are charters being followed?

**Healthy:** Assets in correct locations; lifecycle states accurate; relationships documented

**Unhealthy:** Misplaced content; unknown lifecycle state; orphaned assets

### Institutional Memory
**Evaluate:** Can future collaborators understand why decisions were made?

**Healthy:** Decision logs document rationale; risk history is preserved; relationships are clear

**Unhealthy:** Decisions are opaque; history is missing; context is lost

### Knowledge Preservation
**Evaluate:** Is enduring work actually preserved?

**Healthy:** Graduation Test applied; important work is permanent; nothing critical is lost

**Unhealthy:** Important work is in Development; critical knowledge is temporary; too much remains in Notion

### Signal-to-Noise Ratio
**Evaluate:** Is the repository getting smarter or just fuller?

**Healthy:** Each new asset connects with and enhances existing work; compound growth visible

**Unhealthy:** New assets are isolated; volume increases but connectivity decreases

## Repository Reviews

Repository reviews should evaluate these six metrics annually.

The objective is a repository that becomes increasingly valuable over decades.

---

# MIGRATION PROTECTION RULE

No intellectual asset may be:

* **Moved** (relocated to different folder)
* **Renamed** (filename or title changed)
* **Merged** (combined with other work)
* **Archived** (moved to archive status)
* **Deleted** (removed from repository)

**Until it has first been:**

1. **Identified** — What is this asset? What category? What's its purpose?
2. **Inventoried** — Record location, size, content summary, current relationships
3. **Indexed** — Create asset ID; list all cross-references
4. **Cross-Referenced** — Identify what other work depends on this asset
5. **Classified** — Assign permanent category (Constitutional/Intellectual/Institutional/Development/Operational Support)
6. **Approved** — Drew reviews and approves the proposed change (if significant)

**Only after these six steps:** Execute the move/rename/merge/archive/delete.

**Governing Principle:** Zero knowledge loss remains the guiding migration principle.

**Exception:** Development work can be discarded without approval (it's not permanent by default).

---

# REPOSITORY-FIRST WORKFLOW RULE

For every Finding My Wei task, Claude shall follow this sequence:

1. **Synchronize** — Pull latest from GitHub repository (learn2tape19/finding-my-wei)
2. **Read Governance** — Review Constitution, Executive Directives, Amendments
3. **Read Executive** — Read 00_EXECUTIVE/ files for current strategic state
4. **Determine State** — What is the current institutional state per GitHub?
5. **Surface Conflicts** — If GitHub differs from Notion or memory, identify the conflict
6. **Only Then Proceed** — Provide recommendations based on authoritative GitHub state

## Source of Truth Hierarchy

1. **GitHub Repository** = Enduring institutional record (permanent)
2. **Notion Workspace** = Operational workspace (temporary, collaborative)
3. **Gmail / Calendar / Drive** = Signal sources (context only)
4. **Chat History** = Supporting context (not authoritative)

## Conflict Resolution

**When GitHub and Notion conflict:**
- Do NOT silently resolve in Claude's favor
- Surface the conflict to Drew
- Recommend resolution based on institutional principles
- Await Drew's decision before proceeding

**Principle:** Neither system shall silently overwrite the other.

---

# I. WHAT BELONGS IN FINDING MY WEI

## Always Include (Non-Negotiable)

### Constitutional Knowledge
- **Definition:** Governance structures, principles, decision authority, amendment records
- **Examples:** Constitution.md, Charters, Stewardship Model, Role Definitions, Amendment History
- **Rationale:** Future maintainers must understand the system itself; constitution is permanent

### Intellectual Work
- **Definition:** Original thinking, research, frameworks, clinical philosophy, design rationale, teaching methodology
- **Examples:** Books, research papers, frameworks, methodologies, clinical insights, strategic thinking
- **Rationale:** Represents Drew's cumulative learning; has enduring value beyond current projects

### Institutional Decisions
- **Definition:** Why significant choices were made; who decided; what evidence informed the decision; what alternatives were considered
- **Examples:** Decision logs, strategic pivots, project scoping decisions, architectural choices, risk assessments
- **Rationale:** Future decisions build on understanding of past decisions; context matters more than outcome alone

### Completed Knowledge Products
- **Definition:** Work that has moved through CREATION → REFINEMENT → STABLE → PUBLICATION → PRESERVATION
- **Examples:** Published books, finalized research papers, validated frameworks, completed course curricula, validated methodologies
- **Rationale:** These are enduring assets; they compound in value over time

### Relationships Between Domains
- **Definition:** How different organizations, projects, and ideas connect and influence each other
- **Examples:** Cross-domain research, shared methodologies, inherited frameworks, dependencies
- **Rationale:** Helps future work understand the ecosystem and avoid reinventing solutions

---

## Conditionally Include (Evaluation Required)

### In-Progress Intellectual Work (Development)
- **Definition:** Research, manuscripts, frameworks, courses in CREATION or REFINEMENT phases
- **Inclusion Rule:** Include if:
  - More than one month of active work, OR
  - Involves collaboration with others, OR
  - Part of a planned publication sequence, OR
  - Involves significant financial/strategic investment
- **Location:** 02_PROJECT_ATLAS (research) or appropriate domain PROJECTS/ folder
- **Rationale:** Preserves work in progress for continuity; protects investment in intellectual effort
- **Example:** Therapeutic Alliance paper (active investigation, being co-developed with Campaign 001, publication planned)

### Business Operations With Intellectual Merit
- **Definition:** Operational records that reveal thinking, decision-making, or methodology
- **Inclusion Rule:** Include if:
  - Records decision history (not just transaction data), OR
  - Documents a methodology or process innovation, OR
  - Captures learning from success or failure, OR
  - Reveals strategic thinking behind operational choices
- **Location:** Appropriate domain folder or 03_INTELLECTUAL_ESTATE/DECISION_LOGS/
- **Rationale:** Operations inform thinking; thinking informs future operations
- **Example:** Learn2Tape curriculum design documents, pricing strategy decisions, student success frameworks

### Historical Context for Future Decisions
- **Definition:** Records that help understand how something came to be
- **Inclusion Rule:** Include if:
  - Multiple people need to know about it, OR
  - It affects future decisions, OR
  - It's referenced repeatedly in strategic conversations, OR
  - It represents more than one person's accumulated learning
- **Location:** Appropriate historical or decision location
- **Rationale:** Avoids repeating past mistakes; builds on past learning
- **Example:** Earlier pricing experiments, previous course designs that were abandoned, strategy pivots

---

# II. WHAT DOES NOT BELONG IN FINDING MY WEI

## Always Exclude

### Temporary Working Files
- **Definition:** Scratch work, experimental drafts, early-stage exploration without direction
- **Examples:** First drafts, brainstorming notes, abandoned directions, single-use files
- **Rationale:** Repository stores refined knowledge; scratch work is intermediate
- **Storage:** Keep in Notion, local drive, or working folders

### Raw Operational Data
- **Definition:** Transactional data, individual records, unprocessed information
- **Examples:** Individual student enrollment records, transaction logs, raw email lists, unanalyzed data dumps
- **Rationale:** Business systems are the source of truth for operational data
- **Storage:** Keep in LMS, Brevo, Google Analytics, payment systems

### Credentials and Secrets
- **Definition:** API keys, passwords, authentication tokens, private credentials
- **Examples:** .env files with secrets, auth tokens, database passwords, account credentials
- **Rationale:** Security risk; repository may be public or semi-public
- **Storage:** Externalize to secure credential management (1Password, HashiCorp Vault, etc.)

### Live Website Content
- **Definition:** Content that exists on active, published websites
- **Examples:** WordPress posts on bostonbodyworker.com, current landing pages, live site content
- **Rationale:** Website is source of truth for published content; repository mirrors (old snapshots)
- **Storage:** Keep on live platforms; archive snapshots only if historical preservation needed

### Redundant Duplicates
- **Definition:** Exact copies of content that exists elsewhere in the repository
- **Examples:** Multiple copies of the same document in different folders
- **Rationale:** Repository is single source of truth; duplicates create confusion and maintenance burden
- **Storage:** Keep single authoritative copy; reference from other locations if needed

### Vendor Dependencies and Build Artifacts
- **Definition:** Generated files, compiled output, vendored third-party code
- **Examples:** node_modules/, compiled binaries, pip caches, build outputs
- **Rationale:** Can be regenerated; bloats repository; not meaningful intellectual content
- **Storage:** Exclude from version control; manage via package managers

---

# III. GITHUB VS. NOTION VS. DRIVE BOUNDARY

## GitHub (Finding My Wei Repository)
**Belongs Here:**
- Constitutional documents (permanent governance)
- Completed intellectual work (books, papers, frameworks)
- Institutional decision records (why we chose X)
- Published content and final versions
- System architecture and charters
- Permanent historical records

**Characteristics:**
- Permanent; versioned; publicly archivable
- Intended to last decades
- Every change is logged and reversible
- Suitable for formal publication

---

## Notion (Operational Workspace)
**Belongs Here:**
- Active work in progress (drafts, iterations)
- Project tracking and task management
- Team coordination and collaboration
- Working notes and brainstorming
- Temporary decision tracking
- Current status dashboards

**Characteristics:**
- Flexible; easily reorganized
- Collaborative; real-time updates
- Temporary nature accepted (can be archived or deleted)
- Best for "what are we doing now"

---

## Google Drive (Document Collaboration & Archives)
**Belongs Here:**
- Document collaboration (multiple editors needed)
- Large binary files (images, videos, designs)
- Private correspondence and confidential materials
- External partner sharing and collaboration
- Backup archives of important work
- Historical snapshots (before publishing)

**Characteristics:**
- Secure; shareable; collaborative
- Good for confidential materials
- External partnerships can access
- Can archive instead of delete

---

## Business Systems (LMS, Brevo, Analytics, etc.)
**Belongs Here:**
- Operational transaction data (student records, orders, etc.)
- Live marketing data (subscriber lists, campaign status)
- Customer information and credentials
- Real-time analytics and dashboards
- Secure authentication and payment data

**Characteristics:**
- Source of truth for operational state
- Subject to compliance and privacy rules
- Not intended for historical preservation
- Access controlled by business requirements

---

## Email (Ephemeral Record)
**Use For:** Communication; not permanent storage  
**Archive:** Move important decisions to Decision Log (03_INTELLECTUAL_ESTATE) when they mature

---

# IV. BUSINESS ASSET EVALUATION FRAMEWORK

### Learn2Tape Assets

**INCLUDE in Finding My Wei:**
- Curriculum design documents (methodology)
- Teaching frameworks and innovation (intellectual)
- Course structure decisions and rationale (institutional)
- Student success methodologies (intellectual)
- Learning science research and frameworks (intellectual)
- Strategic pricing and business model decisions (institutional)
- Historical marketing strategy and lessons learned (institutional)

**EXCLUDE from Finding My Wei:**
- Individual student records (operational data)
- Transaction logs (business operational data)
- Raw email marketing lists (data dump)
- Daily task lists and workflows (temporary operational)
- Routine customer service interactions (temporary)
- Current course enrollment data (business system source of truth)

**Special Rule:** Course content (actual lessons) belongs in 05_DOMAINS/EDUCATION_DOMAIN/PRODUCTS/ but raw working files belong in Notion/Drive.

---

### Tao (The Tao of Clinical Touch) Assets

**INCLUDE in Finding My Wei:**
- Published book (03_INTELLECTUAL_ESTATE/BOOKS/)
- Clinical philosophy and frameworks (03_INTELLECTUAL_ESTATE or 05_DOMAINS/FOUNDER_DOMAIN)
- Design decisions and rationale (institutional)
- Marketing strategy and lessons (institutional)
- Build process documentation (operational support ONLY if methodology innovation)

**EXCLUDE from Finding My Wei:**
- Early drafts (keep in working folder; archive old versions only when published)
- PSD files and design iterations (bulky binary; keep only final cover art)
- node_modules and build artifacts (regenerate from package.json)
- Raw content ideas and brainstorms (keep in Notion until refined)
- Social media posts and promotional copies (keep with marketing operations)

**Special Rule:** Published book and its design/strategy journey stay in repo. Development chaos stays in working folders.

---

### Sidekick Air / StitchCore Assets

**INCLUDE in Finding My Wei:**
- Patent documentation and IP (03_INTELLECTUAL_ESTATE and 05_DOMAINS/INNOVATION_DOMAIN)
- Product specification and engineering rationale (institutional + intellectual)
- Manufacturing partnerships and strategy (institutional)
- Technology decisions and architecture (intellectual)
- Go-to-market strategy and pivots (institutional)

**EXCLUDE from Finding My Wei:**
- Raw CAD files (keep with engineering team; archive finalized designs only)
- Partner communications and emails (confidential; keep in Drive shared with partners)
- Current supplier quotes and negotiations (temporary/operational)
- In-progress engineering work (keep in branch/working folders; archive milestones)
- Financial transactions and invoices (business system source of truth)

**Special Rule:** Strategic decisions and lessons stay in repo. Operational execution details stay with operations teams.

---

### Boston Bodyworker / Publishing Domain Assets

**INCLUDE in Finding My Wei:**
- Published articles and clinical writing (03_INTELLECTUAL_ESTATE/PAPERS or 05_DOMAINS/PUBLISHING_DOMAIN/)
- Clinical philosophy and educational content (intellectual)
- Publishing strategy and brand decisions (institutional)
- Historical timeline showing 30+ years of evolution (institutional)
- SEO and authority-building insights (institutional)

**EXCLUDE from Finding My Wei:**
- Live website content (keep on bostonbodyworker.com; archive only major historical snapshots)
- Individual blog post metadata (operational; live site is source of truth)
- Raw email subscriber lists (business operational data)
- Current WordPress configurations (keep with hosting platform)
- Routine website maintenance tasks (temporary/operational)

**Special Rule:** Publish major historical milestones (e.g., "30-Year Evolution Summary") but keep detailed blog operations in WordPress.

---

### Founder Domain / Personal Assets

**INCLUDE in Finding My Wei:**
- Philosophy and principles (constitutional or intellectual)
- Books and major writings (intellectual)
- Decision logs and strategic thinking (institutional)
- Speaking engagements and interviews (intellectual + institutional)
- Life lessons and reflections (institutional)
- Relationships and mentorship records (institutional)

**EXCLUDE from Finding My Wei:**
- Personal daily journal entries (unless published reflection)
- Private correspondence (unless historically significant)
- Personal calendar and scheduling (operational/temporary)
- Financial records and personal accounting (business systems)
- Medical or private personal information (confidential)

**Special Rule:** Founder work is at the heart of Finding My Wei, but private is private. Publish or reflect first; then archive.

---

# PERMANENT STEWARDSHIP PRINCIPLE

Repository health improves when:
- Volume of Development/Operational material decreases proportionally
- Signal quality increases (asset relationships grow stronger)
- Institutional memory deepens (decision history is more complete)
- Intellectual work compounds (new ideas build on old wisdom)

Repository health declines when:
- Volume increases without corresponding quality increase
- Development/Operational material accumulates without graduation
- Signal gets lost in noise
- Institutional memory becomes scattered

---

# V. IMPLEMENTATION CHECKLIST

Before proceeding with any migration or ingestion:

- [ ] This document (v1.0) has been reviewed and ratified by Drew
- [ ] Five-category framework is understood (Constitutional/Intellectual/Institutional/Development/Operational Support)
- [ ] Graduation Test is understood and will be applied consistently
- [ ] GitHub/Notion/Drive boundaries are established and will be maintained
- [ ] Lifecycle stages are clear (Capture → Development → Review → Classification → Approval → Permanent → Archive)
- [ ] Migration Protection Rule will be followed for every asset move
- [ ] Repository-First Workflow will guide Claude's decision-making
- [ ] Business asset classification has been approved
- [ ] Edge case handling has been approved
- [ ] Team understands that future work must follow these classifications
- [ ] Repository reviews will evaluate signal quality and health metrics annually

---

# NEXT PHASE

With Institutional Boundary Definition ratified, Foundation Phase is complete.

Future work shall prioritize:

1. **Production** — Creating enduring intellectual assets
2. **Preservation** — Stewarding what has been created
3. **Stewardship** — Maintaining clarity and quality over time

Rather than:
- Continued architectural expansion
- System redesign (unless real-world experience demonstrates need)
- Theoretical optimization

---

**Document Status:** Version 1.0 RATIFIED  
**Authority:** Drew Freedman (Steward)  
**Effective Date:** July 5, 2026  
**Amendment Record:** Amendment 001 incorporated (7 amendments adopted)  
**Next Review:** December 31, 2026 (annual strategic review)
