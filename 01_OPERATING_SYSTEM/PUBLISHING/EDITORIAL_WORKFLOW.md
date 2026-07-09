# Editorial Workflow

**Authority:** Editorial Board

**Applies To:** All publications requiring editorial oversight

---

## The Publishing Sequence

Every publication follows this workflow:

```
1. IDEA
    ↓
2. RESEARCH
    ↓
3. DRAFT
    ↓
4. SCIENTIFIC REVIEW
    ↓
5. EDITORIAL BOARD REVIEW
    ↓
6. FOUNDER REVIEW
    ↓
7. REVISION
    ↓
8. REPOSITORY COMMIT
    ↓
9. GITHUB PUSH
    ↓
10. PUBLICATION
    ↓
11. EDITORIAL REFLECTION
    ↓
12. STANDARDS UPDATE
```

---

## Stage 1: Idea

**Goal:** Identify a topic or question worth exploring.

**Questions:**

- What's the question we're exploring?
- Why does this matter to clinicians?
- How does this advance the institutional thinking?
- What's the potential reader impact?

**Deliverable:** A clear, one-sentence or one-paragraph statement of what you're exploring.

**Governance:** Founder approval for major topics. Editorial Board notified for all topics.

---

## Stage 2: Research

**Goal:** Gather evidence, read relevant research, collect clinical observation.

**Activities:**

- Read existing research on the topic
- Review related Finding My Wei publications
- Gather clinical examples or stories
- Identify supporting evidence
- Note areas of uncertainty or contradiction
- Collect expert sources if applicable

**Duration:** Varies by topic. Complex topics may require weeks of research.

**Review:** Researcher documents sources and notes findings.

**Governance:** Researcher drives this stage independently.

---

## Stage 3: Draft

**Goal:** Write a first complete draft following Editorial Standards.

**Process:**

- Write freely without self-editing
- Follow the Editorial Standards framework
- Include all supporting evidence and examples
- Identify areas of uncertainty
- Create a clear structure
- Use provisional headings

**Length:** Complete draft, even if rough.

**Key:** Never skip research just to start writing. Base writing on research, not guessing.

**Review:** Read through once. Note obvious gaps. Don't obsess over perfection.

**Governance:** Author drives this stage.

---

## Stage 4: Scientific Review

**Goal:** Verify scientific accuracy and appropriate claims proportional to evidence.

**Who Reviews:** Scientific reviewer (editorial board member with relevant expertise, or external expert for technical topics).

**Review Criteria:**

- ✓ Are research claims accurate?
- ✓ Are claims proportional to evidence?
- ✓ Is neuroscience language appropriate?
- ✓ Are citations complete and correct?
- ✓ Is uncertainty acknowledged where appropriate?
- ✓ Do evidence and interpretation stay separate?

**Reviewer Feedback:** Specific comments, line-by-line corrections, big-picture concerns.

**Duration:** 3-5 business days typical.

**Revisions:** Author incorporates scientific feedback, notes questions, resubmits if major changes needed.

**Gate:** Scientific review must be approved before moving to Editorial Board Review.

**Governance:** Scientific Reviewer has authority to block advancement if significant accuracy concerns exist.

---

## Stage 5: Editorial Board Review

**Goal:** Verify voice consistency, flow, adherence to Editorial Standards, and reader experience.

**Who Reviews:** Editorial Board member (not the scientific reviewer).

**Review Criteria:**

- ✓ Voice consistency (see VOICE_GUIDE.md)
- ✓ Flow and structure
- ✓ Paragraph length and pacing
- ✓ Heading clarity
- ✓ Reader experience (curiosity before certainty, observation before conclusion)
- ✓ Adherence to Editorial Standards
- ✓ Story before science
- ✓ Reflection before instruction
- ✓ No em dashes or punctuation errors
- ✓ Formatting consistency
- ✓ AI clichés removed

**Reviewer Feedback:** Holistic comments plus specific line edits.

**Duration:** 2-3 business days typical.

**Revisions:** Author makes requested changes, responds to editorial suggestions.

**Gate:** Editorial Board reviewer approves before forwarding to Founder.

**Governance:** Editorial Board Reviewer has authority to request revisions and delay advancement if standards aren't met.

---

## Stage 6: Founder Review

**Goal:** Final authority on institutional voice, strategy alignment, and publication decision.

**Founder Considers:**

- ✓ Strategic alignment with institutional goals
- ✓ Voice and representation of Finding My Wei
- ✓ Quality and lasting value
- ✓ Appropriateness for the intended platform
- ✓ Timing and context
- ✓ Overall institutional impact

**Founder May:**

- Approve for publication
- Request revisions
- Reject the publication (rare)
- Suggest significant restructuring

**Duration:** Founder-determined. May be same day or may require time for consideration.

**Authority:** Only Founder can approve publication.

**Governance:** Founder approval is the gate to publication.

---

## Stage 7: Revision

**Goal:** Incorporate all feedback from scientific review, editorial review, and Founder review.

**Process:**

- Address each piece of feedback
- Make changes or explain pushback
- Re-read thoroughly
- Verify standards still met
- Check for unintended consequences of revisions
- Polish final version

**Resubmission:** If major changes, resubmit to Editorial Board. If minor changes, can proceed directly to repository.

**Duration:** 1-3 business days typical.

**Governance:** Author drives, but must address all feedback. Can request clarification if feedback unclear.

---

## Stage 8: Repository Commit

**Goal:** Stage and commit the final publication to the canonical repository.

**Process:**

1. Verify current directory is `/Users/Drewdog19/finding-my-wei`
2. Move or create the publication file in appropriate location
3. Run `git status` to verify correct files
4. Run `git add [filename]`
5. Run `git commit -m "[clear message]"`
6. Verify commit succeeded

**Commit Message Format:**

```
[Topic]: [Brief description of publication]

[Optional: more details about what's included or why it matters]

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**Example:**
```
Project Atlas Paper 1: Therapeutic Alliance Framework

- Complete first paper in five-paper sequence
- Introduces core framework for alliance-centered practice
- Includes research synthesis and clinical implications

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**Governance:** Author or designated team member performs commit.

---

## Stage 9: GitHub Push

**Goal:** Push committed changes to origin/main.

**Process:**

1. Run `git push origin main`
2. Verify push succeeded
3. Confirm origin/main is up to date

**Governance:** Same person who committed or designated team member.

---

## Stage 10: Publication

**Goal:** Make the publication available to intended audience.

**Platforms:**

- Finding My Wei website (taoclinicaltouch.com or designated site)
- Email newsletter
- LinkedIn
- Social media
- Book publishing platforms
- PDF distribution
- Other as appropriate

**Coordinator:** Designated publication team member or Founder.

**Documentation:** Record publication date, platform, and URL.

**Governance:** Founder or designated publication coordinator.

---

## Stage 11: Editorial Reflection

**Goal:** Capture lessons learned from this publication.

**Timing:** Within 1 week of publication.

**Questions to Answer:**

1. What improved during the editorial process?
2. What were the biggest challenges?
3. What feedback did readers or stakeholders provide?
4. What did we do well?
5. What should we do differently next time?
6. Did reader response match expectations?
7. What surprised us?
8. How did this publication advance institutional thinking?

**Format:** Notes recorded in publication record or separate reflection document.

**Participants:** Author + Editorial Board reviewer + Founder (optional).

**Governance:** Editorial Board coordinator facilitates.

---

## Stage 12: Standards Update

**Goal:** Improve Editorial Standards based on what was learned.

**Process:**

1. Review editorial reflection
2. Identify lessons that should become permanent
3. Update appropriate Editorial Standard documents
4. Commit updates to repository
5. Notify team of changes

**Examples:**

- "Next time, start with clinical story rather than research context."
- "Readers responded strongly to specific examples; prioritize these."
- "Scientific language in this section confused readers; revise that section of SCIENTIFIC_INTEGRITY_STANDARD.md"

**Timing:** Within 2 weeks of publication.

**Governance:** Editorial Board director makes final calls on standard updates.

---

## Parallel Processing and Shortcuts

### Research While Other Articles Review

You can start research on the next publication while earlier articles are in review.

### Small Updates Don't Need Full Workflow

Minor corrections or updates to existing publications can skip some stages:

- Typo fixes: Commit directly
- Science clarification: Scientific review only
- Voice refinement: Editorial Board review only

### Expedited Timeline

For urgent publications (breaking news, immediate response needed):

- Compress research stage
- Scientific and Editorial reviews happen simultaneously
- Founder fast-tracks review
- Must still meet all standards

---

## Timeline Expectations

### Fast Track
Idea → Research (2 days) → Draft → Reviews (concurrent, 3 days) → Revision → Publication

**Total: ~2 weeks minimum**

### Standard Track
Idea → Research (1-2 weeks) → Draft → Scientific Review (3-5 days) → Editorial Review (2-3 days) → Founder Review (2-5 days) → Revision (2-3 days) → Publication

**Total: ~3-4 weeks typical**

### Major Project (Paper, Book)
Idea → Research (weeks) → Draft → Scientific Review (1-2 weeks) → Editorial Review (1 week) → Founder Review (1+ week) → Revision → Publication

**Total: 2-3 months+**

---

## Who Reports to Whom

```
AUTHOR
  ↓
SCIENTIFIC REVIEWER (reports back to author)
  ↓
EDITORIAL BOARD REVIEWER (reports back to author)
  ↓
FOUNDER (final authority)
  ↓
PUBLICATION COORDINATOR
  ↓
AUDIENCE
```

Feedback flows down, revisions flow up.

---

## Checkpoint Verification

Before advancing each stage:

- [ ] All previous stage requirements met
- [ ] Feedback addressed or documented
- [ ] Files in correct location
- [ ] Standards being followed
- [ ] Next reviewer ready to proceed
