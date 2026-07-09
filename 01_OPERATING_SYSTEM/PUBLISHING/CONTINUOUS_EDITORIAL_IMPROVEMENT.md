# Continuous Editorial Improvement

**How the Institution Learns and Improves**

---

## Core Principle

Every publication teaches the institution something.

Every lesson learned becomes part of the institutional standards.

Future publications inherit these improvements automatically.

No editorial mistake should need to be corrected twice.

---

## The Learning Cycle

### Stage 1: Publication

A piece of writing is published and reaches an audience.

### Stage 2: Feedback Collection

Gather feedback from:

- Readers (direct responses, social media, email)
- Stakeholders (team members, clinicians, experts)
- Founder observations
- Author's own reflection
- Editorial Board observations

**Timing:** During and immediately after publication. Ongoing as feedback arrives.

### Stage 3: Pattern Recognition

Identify what feedback reveals:

- What resonated strongly with readers?
- What was confusing?
- What generated clinical discussion?
- What fell flat?
- What was unexpected?

Look for patterns across multiple pieces of feedback, not isolated comments.

### Stage 4: Root Cause Analysis

For each pattern, ask why:

- "Readers were confused about X. Was it unclear writing, incorrect structure, or false assumption about reader knowledge?"
- "Readers responded strongly to the clinical story. Does this mean we should always lead with observation?"
- "The scientific explanation was questioned. Was the evidence insufficiently clear, or was the claim overstated?"

### Stage 5: Institutional Learning

Translate each insight into a lesson:

- "Stories create connection. Lead with observation, not explanation."
- "Readers need context for research claims. Always explain why the research matters before citing it."
- "Uncertainty is acceptable. Acknowledge limits of knowledge."

### Stage 6: Standards Update

Incorporate the lesson into Editorial Standards:

- Update EDITORIAL_STANDARDS.md if it's a core principle
- Update STYLE_GUIDE.md if it's formatting or craft
- Update VOICE_GUIDE.md if it's voice consistency
- Update SCIENTIFIC_INTEGRITY_STANDARD.md if it's about claims and evidence
- Update appropriate document and commit the change

**Example:**

After publication, readers consistently noted that the clinical story at the beginning was the most valuable part.

**Learning:** Lead with observation and clinical story. Science explanation should follow, not precede.

**Update:** Add to EDITORIAL_STANDARDS.md: "Story before explanation is non-negotiable."

---

## Editorial Reflection Process

**Timing:** Within 2 weeks of publication

**Participants:** Author + Editorial Board reviewer (at minimum)

**Format:** Structured reflection document or discussion notes

### Questions to Answer

1. **What Improved**
   - Did editorial feedback improve the piece?
   - What was the most valuable revision?
   - What editorial suggestion most strengthened the work?

2. **What Worked**
   - What sections generated strongest reader response?
   - What did we do well?
   - What felt natural and right?

3. **What Was Challenging**
   - What was hardest to write?
   - Where did multiple revisions happen?
   - What feedback conflicted or created tension?

4. **Reader Response**
   - Did readers respond as expected?
   - What surprised you?
   - What generated clinical discussion?

5. **What Should Change**
   - What will we do differently next time?
   - What should become a standing practice?
   - What standard should we update?

6. **Questions for Next Publication**
   - What did this raise that should be explored?
   - What topic or angle should we pursue?
   - What reader question should we address?

---

## Documentation

Every editorial reflection should be documented:

### Option 1: Reflection File
Create a reflection document in the same directory as the publication:

`01_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/PRODUCTION/WEEK_01/EDITORIAL_REFLECTION.md`

### Option 2: Commit Message
Include reflection in the commit that updates standards:

```
Update EDITORIAL_STANDARDS.md based on Campaign 001 Week 01 reflection

Learning: Readers responded most strongly to specific clinical stories.
- Lead with observation, not explanation
- Clinical examples create connection before science matters
- Readers want to recognize themselves in the writing

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### Option 3: Editorial Board Log
Maintain a running log of all reflections and learnings:

`01_OPERATING_SYSTEM/PUBLISHING/EDITORIAL_IMPROVEMENTS_LOG.md`

---

## Standards Update Process

### What Warrants an Update

**Update the standards if:**
- The lesson is significant enough to change behavior
- The lesson applies to future publications (not just this one)
- Multiple publications confirm the pattern

**Don't update if:**
- It's an isolated comment or unusual situation
- It conflicts with established principles without strong evidence
- It's preference rather than principle

### How to Update

1. Identify which standard document needs updating
2. Find the relevant section
3. Add or revise the relevant principle
4. Include the date and reasoning (in comments or commit message)
5. Commit the change with reference to what generated the update

### Example Update

**Original (EDITORIAL_STANDARDS.md):**
"Avoid overstating neuroscience."

**After receiving reader feedback that language was still too speculative:**

"Avoid overstating neuroscience. Use 'may,' 'might,' or 'appears to' rather than 'does' or 'creates.' Every neuroscience claim should include a hedge word."

**Commit:** "Refine neuroscience language standards based on feedback from Paper 1"

---

## Version Control

Standards documents should be versioned:

```
# Editorial Standards

**Version:** 2.0
**Last Updated:** July 9, 2026
**Updates Since v1.0:** 
- Added prohibition on em dashes
- Clarified story-before-explanation principle
- Refined scientific integrity standards
```

Track what changed and why.

---

## The Improvement Archive

Maintain a public record of how standards evolved:

**File:** `01_OPERATING_SYSTEM/PUBLISHING/STANDARDS_EVOLUTION.md`

Document each major update:

| Date | Document | Change | Reason |
|------|----------|--------|--------|
| 7/9/26 | EDITORIAL_STANDARDS.md | Added story-first principle | Reader feedback on Paper 1 |
| 7/15/26 | SCIENTIFIC_INTEGRITY_STANDARD.md | Clarified five certainty levels | Campaign feedback on neuroscience clarity |

This shows the institution's learning journey.

---

## Preventing Regression

### The Two-Step Rule

Never remove a standard or principle.

Add to it, clarify it, or evolve it.

If a principle no longer applies, mark it as deprecated and explain why, rather than deleting it.

**Example:**
```
DEPRECATED (v2.0): "Always provide academic citations"

Reason: Clinic observation is valid without research backing. 
Changed to: "Cite research when available; acknowledge clinical 
observation when research doesn't yet address the topic."
```

### Institutional Memory

All changes are tracked in git history.

Future team members can see why principles evolved.

This prevents re-learning the same lessons.

---

## Scaling the Learning

As the institution publishes more:

1. **More data** — patterns become clearer with more publications
2. **Stronger standards** — with more evidence, standards become more specific and useful
3. **Predictable outcomes** — good standards predict good writing
4. **Lower friction** — new writers inherit proven principles

---

## The Goal

A living, improving editorial system that:

- Captures what works
- Documents why it works
- Prevents repeating mistakes
- Builds on success
- Becomes stronger with each publication

The institution doesn't just publish.

The institution learns how to publish better.

Every publication makes the next publication better.

That is continuous improvement.
