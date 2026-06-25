# Decision Engine

The framework for documenting important decisions so they compound over time, not repeat.

The Decision Engine answers: **Context? Alternatives? Reasoning? Tradeoffs? Outcome? Lessons? Review Date?**

---

## Why Document Decisions?

Most people make decisions then forget them. Years later, they face the same decision again with no memory of why they chose differently before.

The Decision Engine prevents this.

Every important decision is recorded with:
- **Why** you decided
- **What** you considered
- **What** you learned
- **When** to revisit

Over time, this becomes a decision library that makes you smarter.

---

## Decision Record Template

Every decision follows this structure:

```markdown
# Decision: [Title]

**Date**: YYYY-MM-DD  
**Owner**: [Who made the decision]  
**Status**: [Active/Archived/Revisited]  
**Review Date**: YYYY-MM-DD (when to revisit)

---

## Context

**Situation**: [What was true that forced this decision?]

**Constraints**: 
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

**Stakeholders**: [Who is affected?]

**Urgency**: [Timeline for decision]

---

## Alternatives Considered

### Alternative 1: [Option A]
**Description**: [What is this option?]  
**Pros**: 
- [Pro 1]
- [Pro 2]

**Cons**: 
- [Con 1]
- [Con 2]

**Why not chosen**: [Reasoning]

---

### Alternative 2: [Option B]
**Description**: [What is this option?]  
**Pros**: 
- [Pro 1]
- [Pro 2]

**Cons**: 
- [Con 1]
- [Con 2]

**Why not chosen**: [Reasoning]

---

### Alternative 3: [Option C]
**Description**: [What is this option?]  
**Pros**: 
- [Pro 1]
- [Pro 2]

**Cons**: 
- [Con 1]
- [Con 2]

**Why not chosen**: [Reasoning]

---

## Decision

**Chosen**: [Option X]

**Final Reasoning**:
[2-3 paragraphs explaining why this is the best option given the context]

---

## Tradeoffs

**We gained**:
- [What becomes possible now?]
- [What improves?]
- [What becomes easier?]

**We sacrificed**:
- [What becomes impossible?]
- [What we gave up?]
- [What becomes harder?]

**Acceptable?**: [Yes/No — is this tradeoff worth it?]

---

## Expected Outcome

**If everything goes as planned**: [What should happen?]

**How we'll know it's working**: [Metrics or signals]

**Timeline**: [When will we see results?]

---

## Actual Outcome

*(Updated at review date)*

**What actually happened**: [Facts]

**Did it work as expected?**: [Yes/No/Partially]

**What surprised us?**: [Unexpected results]

**What changed in the meantime?**: [Context shift since decision]

---

## Lessons Learned

**What did this teach us?**:
1. [Lesson 1]
2. [Lesson 2]
3. [Lesson 3]

**How does this change our thinking?**:
[What principle emerged from this decision?]

**What would we do differently?**:
[If we faced this today, what would change?]

**What should we never do again?**:
[Hard lessons]

---

## Integration

**Affected Projects**: [[project-name]]  
**Affected Principles**: [[principle-name]]  
**Related Decisions**: [[DECISION_INDEX.md#related-decisions]]  
**Influenced Future Decisions**: [What decisions did this enable or block?]

---

## Review Schedule

**Review Date**: YYYY-MM-DD  
**Revisit Reason**: [When should we check if this decision still holds?]

**Options if revisiting**:
- [ ] Keep the decision (still optimal)
- [ ] Refine the decision (same direction, better execution)
- [ ] Reverse the decision (new context changed everything)
- [ ] Archive and learn (decision worked, now obsolete)

---

## Status

**Decision**: [Active / Archived / Superseded]

**If Archived**: [Why is this decision no longer relevant?]

**If Superseded**: [What decision replaced this? Why?]

```

---

## Decision Categories

Different types of decisions get different review schedules:

### Strategic Decisions (Annual Review)
- Business direction
- Long-term partnerships
- Major product pivots
- Technology platform choices

**Review**: Every year  
**Storage**: `04_Decision_Framework/strategic/`

---

### Project Decisions (Quarterly Review)
- Project scope and timeline
- Resourcing allocation
- Feature prioritization
- Team structure

**Review**: At project end or quarterly  
**Storage**: `04_Decision_Framework/projects/`

---

### Operational Decisions (Monthly Review)
- Process changes
- Tool selections
- Workflow refinements
- Administrative decisions

**Review**: Monthly or when context changes  
**Storage**: `04_Decision_Framework/operations/`

---

### Personal Decisions (Weekly Review)
- What to focus on
- Time allocation
- Learning priorities
- Relationship commitments

**Review**: Weekly; check if still serving you  
**Storage**: `04_Decision_Framework/personal/`

---

## Decision Chains

Decisions don't exist in isolation. One decision enables or constrains others.

The Decision Engine documents these chains:

```
Decision A (2024-01-15): Choose GitHub as source of truth
  ↓
Enables Decision B (2024-02-01): Build Finding My Wei repository
  ↓
Enables Decision C (2024-06-25): Create UIP and operating system
  ↓
Constrains Decision D (future): Will always use GitHub; can't move to proprietary platform
```

Document these chains so you understand why you're locked into certain choices.

---

## Integration with Other Systems

**Universal Insight Processor** → Step 5 (Decide) uses this framework  
**Reflection Engine** → Reflections update decision records  
**Knowledge Graph** → Decisions connect to projects, people, concepts  
**Daily Workflow** → Decisions guide daily priorities  

---

## Decision Library

Over time, the Decision Engine becomes a **decision library** you can learn from.

When facing a new decision, you can:
1. Search existing decisions for similar contexts
2. Understand what worked before
3. Adapt previous reasoning to new situation
4. Avoid repeating mistakes

The Decision Engine is how you become smarter over time.

---

## Rules for Decision Records

1. **Record decisions when made**  
   Not afterwards. Memory is unreliable.

2. **Include reasoning**  
   "We chose X" is not enough. "We chose X because [reasoning]" is valuable.

3. **Document tradeoffs honestly**  
   Every decision sacrifices something. Name it.

4. **Plan reviews upfront**  
   When will this decision be revisited? Write it down now.

5. **Update with actual outcomes**  
   Go back to your decision records; fill in what actually happened.

6. **Extract lessons**  
   Each decision teaches something. Make it explicit.

7. **Connect everything**  
   Link decisions to projects, principles, people, and concepts.

---

## Example: Decision Record (Filled)

See `DECISION_INDEX.md` for completed examples from active projects (Tao pricing, manufacturing partnerships, marketing approaches, etc.)

---

## Purpose

The Decision Engine makes you **cumulatively smarter**.

Each decision you document:
- ✓ Prevents repetition of old mistakes
- ✓ Preserves reasoning for future reference
- ✓ Reveals patterns in your decision-making
- ✓ Compounds as a resource library
- ✓ Teaches you about yourself

---

**Status**: Operating system core component  
**Last Updated**: 2026-06-25  
**Template Storage**: `/21_Templates/decision-template.md`
