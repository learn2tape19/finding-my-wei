# AI Collaboration Protocol

Formal specification of how AI collaborators (Claude, ChatGPT) and tools work together to serve Finding My Wei.

This is not aspirational. This is practical. It describes real workflows that have proven effective.

---

## Principle

AI collaborators are **complementary**, not competitive.

- Claude brings architecture, precision, documentation, synthesis
- ChatGPT brings exploration, creativity, strategic thinking, real-time coaching

Neither replaces the other. Both are used intentionally, not defaulted to arbitrarily.

---

## When Claude Is Used

### Claude's Responsibilities

**Repository Architecture & Management**
- File organization and naming standards
- Folder structure design
- GitHub workflow and git commits
- Repository maintenance and cleanup

**Documentation & Writing**
- Technical documentation
- Long-form synthesis and explanation
- Template creation
- Standards documentation
- README files and guides

**Knowledge Organization**
- Building and maintaining indices ([[MASTER_INDEX]], [[CONCEPT_INDEX]], etc.)
- Creating knowledge graph connections
- Organizing information hierarchically
- Creating navigation systems

**Implementation Planning**
- Breaking down complex projects into steps
- Creating templates and reusable structures
- Designing systems and workflows
- Building the operating system itself

**Precision Work**
- Code (Python, bash, markdown)
- Structured data and templates
- Anything requiring accuracy and consistency
- Anything that touches the permanent record

### How to Engage Claude

**Approach**: Bring Claude when you need:
- Architecture or structure
- Documentation or long-form writing
- Systems thinking or process design
- Implementation or building
- Precision and accuracy
- Something to persist in GitHub

**Workflow**:
1. You brief Claude with context and request
2. Claude proposes approach or builds directly
3. You review and iterate
4. Claude publishes to GitHub
5. You commit and deploy

**Example**: "Build the structure for the CE course documentation. Create folders for Phase 1 and Phase 2, with a README explaining how they connect."

---

## When ChatGPT Is Used

### ChatGPT's Responsibilities

**Strategic Thinking**
- Business decisions and planning
- Market analysis and positioning
- Long-term vision and direction
- Competitive strategy

**Creative Exploration**
- Ideation and brainstorming
- Content angles and approaches
- Problem-solving for novel challenges
- Novelty and innovation

**Real-time Coaching & Conversation**
- Thinking through a decision
- Processing emotions and challenges
- Exploring ideas in conversation
- Sounding board for thinking

**Teaching & Learning**
- Explaining concepts simply
- Creating teaching frameworks
- Designing learning experiences
- Answering "how do I teach this?" questions

**Business Development**
- Product positioning and messaging
- Customer insight and empathy
- Partnership strategy
- Go-to-market planning

### How to Engage ChatGPT

**Approach**: Bring ChatGPT when you need:
- Strategic thinking or planning
- Creative exploration or ideation
- Business or product thinking
- Teaching design or pedagogy
- Real-time conversation and coaching
- Something that needs novelty or different perspective

**Workflow**:
1. You bring a question or challenge to ChatGPT
2. ChatGPT explores, asks probing questions, offers perspectives
3. You think through possibilities together
4. You extract the key insight or decision
5. You (or Claude, following your direction) implement in GitHub

**Example**: "I'm thinking about the CE course pricing strategy. Should it be $299 one-time or $99/month subscription? What factors should I consider?"

---

## Tool Assignments

Beyond the AI collaborators, specific tools have specific purposes:

### GitHub
**Purpose**: Permanent source of truth for all intellectual assets

**When used**:
- Every decision is recorded (DECISION_INDEX.md)
- Every project has a README
- Every principle is documented
- Every completed work is archived
- Every lesson is recorded

**Who updates**: Claude (on your direction); you can edit directly

**Frequency**: Daily (commits), Weekly (major updates), Monthly (system updates)

---

### Adobe Express + Firefly
**Purpose**: Visual asset creation and design

**When used**:
- Creating social media graphics
- Designing presentation slides
- Building product mockups
- Creating visual explanations
- Refining brand assets

**Who updates**: You or designer; Claude can document approach

**Frequency**: As needed for publishing

---

### Buffer
**Purpose**: Content publishing and scheduling

**When used**:
- Publishing to social media platforms
- Scheduling content batches
- Organizing publishing calendar
- Tracking publishing metrics

**Who updates**: You or content coordinator

**Frequency**: Weekly (scheduling), Monthly (review metrics)

---

### Google Workspace (Email, Docs, Sheets)
**Purpose**: Collaboration and communication

**When used**:
- Strategic documents shared with collaborators
- Real-time collaboration
- Communication and coordination

**Who updates**: You and collaborators

**Frequency**: Daily (email), As needed (collaborative docs)

---

## Decision Framework: Which Tool/Collaborator?

```
QUESTION: What work needs to happen?

├─ Building/implementing → USE CLAUDE
│  └─ What: Creating structure, documentation, systems
│  └─ Example: "Build the Tao project folder structure"
│
├─ Thinking strategically → USE CHATGPT
│  └─ What: Planning, positioning, exploring options
│  └─ Example: "Help me think through CE course pricing strategy"
│
├─ Creating visuals → USE ADOBE/FIREFLY
│  └─ What: Social graphics, presentations, mockups
│  └─ Example: "Design a social media graphic for the Tao announcement"
│
├─ Publishing content → USE BUFFER
│  └─ What: Scheduling posts, organizing calendar
│  └─ Example: "Schedule this week's social media posts"
│
├─ Documenting decisions → USE GITHUB
│  └─ What: Recording why, outcomes, lessons
│  └─ Example: "I need to document the Sidekick Air manufacturer decision"
│
└─ Collaborating with others → USE GOOGLE WORKSPACE
   └─ What: Sharing, real-time collaboration, communication
   └─ Example: "Share this research with the team"
```

---

## Workflow Patterns

### Pattern 1: Ideation → Implementation

1. **ChatGPT**: Explore idea, think through options, refine concept
2. **You**: Decide on direction
3. **Claude**: Build the structure, create templates, implement
4. **GitHub**: Commit and record decision
5. **Buffer**: Publish if audience-facing
6. **You**: Reflect and extract learning

---

### Pattern 2: Research → Synthesis → Teaching

1. **You**: Gather research and raw material
2. **ChatGPT**: Help think through findings, explore implications
3. **Claude**: Synthesize into documentation, create teaching outlines
4. **Adobe/Firefly**: Create visual explanations
5. **GitHub**: Archive research and synthesis
6. **Buffer**: Publish relevant pieces

---

### Pattern 3: Decision Making

1. **You**: Recognize a decision point
2. **ChatGPT**: Think through alternatives, explore tradeoffs
3. **You**: Decide
4. **Claude**: Document in DECISION_ENGINE format
5. **GitHub**: Commit decision record
6. **You**: Execute and later reflect on outcome

---

### Pattern 4: Project Completion & Learning

1. **You**: Complete project, gather raw observations
2. **ChatGPT**: Process emotions, celebrate, think through learnings
3. **Claude**: Document in archive, create project summary
4. **You**: Reflect using REFLECTION_ENGINE
5. **GitHub**: Commit archive and reflection
6. **Claude**: Update relevant indices and principles based on learning

---

## Guardrails

### What Claude Never Does
- Strategic business decisions (that's ChatGPT's role)
- Creative ideation without direction (that's ChatGPT's role)
- Decides what's important (you do)

### What ChatGPT Never Does
- Implements or builds technical solutions
- Maintains repository structure
- Creates precision documentation
- Handles the permanent record

### What You Always Do
- Make final decisions
- Direction-setting
- Extracting meaning from collaborative work
- Choosing what becomes permanent in GitHub

---

## Quality Standards

### Claude's Outputs
- Correct and accurate
- Well-structured and organized
- Well-linked and connected
- Ready for publication/archive
- Future-proof (will make sense in 5 years)

### ChatGPT's Outputs
- Thought-provoking and novel
- Clear and actionable
- Grounded in your specific context
- Push you to think differently
- Generate real insights

### Both
- Transparent about limitations
- Clear about reasoning
- Open to iteration
- Respectful of your direction

---

## Communication

### With Claude
- Be specific about structure and requirements
- Provide context for implementation
- Be clear about audience and purpose
- Iterate on outputs
- Trust Claude to organize and implement well

### With ChatGPT
- Bring your real thinking and challenges
- Be honest about context and stakes
- Ask probing questions
- Explore uncertainty together
- Extract actionable insights

---

## Expansion

As Finding My Wei grows, this protocol may expand to include:
- Specialized researchers
- Graphic designers
- Video producers
- Course instructors
- Subject matter experts

**Principle**: Each collaborator (human or AI) has a clear domain. No overlap. No ambiguity.

---

## Purpose

This protocol ensures:
1. **Clarity** — Everyone knows when they're used
2. **Efficiency** — Right tool for every task
3. **Quality** — Work plays to each collaborator's strength
4. **Permanence** — The right outputs end up in GitHub
5. **Growth** — The system scales without chaos

---

**Status**: Operating system core component  
**Last Updated**: 2026-06-25  
**Owner**: Drew Freedman (with Claude and ChatGPT as collaborators)
