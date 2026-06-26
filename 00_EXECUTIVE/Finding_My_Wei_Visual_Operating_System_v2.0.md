# FINDING MY WEI VISUAL OPERATING SYSTEM v2.0
## 9-Layer Inheritance Architecture with Performance Intelligence Feedback Loop

**Status:** FROZEN — Effective June 26, 2026  
**Version:** 2.0 (Refined with Layer 00 + Layer 08)  
**Authority:** Creative Director (Design System)  
**Next Review:** Annual Strategic Review (December 2026)

---

## REFINED LAYER STRUCTURE

```
Layer 00: Constitution (Immutable Root)
  ↓ inherits
Layer 01: Principles (Design Philosophy)
  ↓ inherits
Layer 02: Tokens (Design Variables)
  ↓ inherits
Layer 03: Rules (Design Behavior)
  ↓ inherits
Layer 04: Components (Project Component Libraries)
  ↓ inherits
Layer 05: Compositions (Project Page Blueprints)
  ↓ inherits
Layer 06: Implementations (Software Renderers)
  ↓ inherits
Layer 07: Outputs (Export Formats)
  ↓ feeds into
Layer 08: Intelligence (Performance & Learning Loop)
  ↓ informs
Layer 00: Constitution (Feedback loop completes)
```

---

## COMPLETE INHERITANCE ARCHITECTURE

### Layer 00: CONSTITUTION (Immutable Root)

**Status:** Immutable — supreme law of visual system

**Defines:**
- The absolute values that govern all visual expression
- What Finding My Wei stands for visually
- Non-negotiable commitments

**Constitutional Values:**
- Finding My Wei exists to translate clinical knowledge
- Visual system serves ideas, not vice versa
- Design becomes invisible when it succeeds
- Authority through clarity, not decoration
- Scientific integrity is non-negotiable
- All projects serve the same intellectual estate

**Cannot be modified by:** Any other layer

**Change protocol:** Strategic review only, never operational reactivity

---

### Layer 01: PRINCIPLES (Design Philosophy & Values)

**Inherits from:** Layer 00 (Constitution)

**Defines:**
- How the Constitution is expressed visually
- Design philosophy that operationalizes constitutional values

**Principles:**
- Authority: Earned through consistency and clarity
- Curiosity: Visual system invites exploration
- Professionalism: No casual or trendy visual language
- Scientific Integrity: Data and claims are precise
- Clinical Humility: Know what we don't know
- Editorial Quality: Timeless, not current
- Accessibility: WCAG AA minimum, always
- White Space is Structural: Not wasted space
- Restraint Communicates Confidence: Less is more

**Cannot override:** Layer 00 (Constitution)

**Can be specialized by:** Layers 02-08

---

### Layer 02: TOKENS (Design Variables - IMMUTABLE)

**Inherits from:** Layer 00 + Layer 01

**Status:** LOCKED — No modifications by any layer

**Typography Tokens:**
- TYPE_H1: Cormorant Garamond, 72px, Bold, 1.2 lh
- TYPE_H2: Cormorant Garamond, 42px, Semibold, 1.2 lh
- TYPE_BODY: Inter, 30px, Regular, 1.5 lh
- TYPE_SUBHEADER: Inter, 30px, Regular, 1.4 lh
- TYPE_SUPPORTING: Inter, 24px, Regular, 1.4 lh
- TYPE_CITATION: Inter, 20px, Medium, 1.4 lh
- TYPE_LABEL: Inter, 18px, Regular, 1.3 lh

**Spacing Tokens (8px baseline):**
- SPACE_8, SPACE_16, SPACE_24, SPACE_32, SPACE_48, SPACE_64, SPACE_96, SPACE_128

**Color Tokens:**
- COLOR_PRIMARY_TEXT: #1F3A5F (Deep Navy — headlines)
- COLOR_SECONDARY_TEXT: #4A5568 (Slate Gray — body)
- COLOR_ACCENT: #7B9E87 (Sage Green — citations)
- COLOR_TERTIARY: #C6A15B (Gold — emphasis, rare)
- COLOR_BACKGROUND: #F7F4EE (Warm Ivory — canvas)

**Layout Tokens:**
- GRID_BASELINE: 8px
- CANVAS_WIDTH: 1080px
- CONTENT_MAX_WIDTH: 920px
- SAFE_AREA: 90px top/bottom, 80px sides
- BORDER_RADIUS_STANDARD: 20px

**Accessibility Tokens:**
- CONTRAST_MINIMUM: WCAG AA (4.5:1)
- FONT_SIZE_MINIMUM: 16px equivalent
- LINE_HEIGHT_MINIMUM: 1.4

**Cannot override:** Layer 01 + Layer 00

**Cannot be modified by:** Layers 03-08

---

### Layer 03: RULES (Design Behavior & Constraints)

**Inherits from:** Layers 02 + 01 + 00

**Defines:**
- How tokens must be used
- Constraints that preserve constitutional principles

**Typography Rules:**
- Headings never exceed two lines
- Body text maximum: 45 words per block
- Line height minimum: 1.4
- Never use font smaller than TYPE_LABEL (18px)
- All text must meet CONTRAST_MINIMUM (WCAG AA)
- Serif fonts only: Cormorant Garamond
- Sans-serif only: Inter

**Spacing Rules:**
- All margins must be multiples of SPACE_8
- Never use spacing values outside SPACING_TOKENS
- Never reduce spacing below SPACE_16 between text blocks
- White space must increase ~25% vs. social media layouts
- Safe areas (90px/80px) are inviolable

**Color Rules:**
- Only colors from COLOR_TOKENS
- No custom colors, no off-palette adjustments
- Deep Navy for primary text only
- Slate Gray for body text always
- Sage Green for citations and secondary information
- All color combinations must meet CONTRAST_MINIMUM
- No opacity below 70% (maintain legibility)

**Hierarchy Rules:**
- Reader's eye: idea → explanation → illustration
- Never interrupt text flow with scattered elements
- Visual emphasis follows information importance

**Component Rules:**
- Each component uses Layer 02 tokens only
- Component dimensions are multiples of SPACE_8
- Components never redefine Layer 02 typography
- All component relationships documented

**Page Composition Rules:**
- Only four master page types exist per project
- Pages assemble components; never redefine them
- All spacing between components from SPACING_TOKENS
- Safe area margins are inviolable

**Implementation Rules:**
- Software must render Layer 05 blueprints exactly
- No design decisions in implementation layer
- All tokens implemented as system variables/props

**Cannot override:** Layers 02 + 01 + 00

**Can be specialized by:** Layers 04-08 (add project-specific rules without breaking global rules)

---

### Layer 04: COMPONENTS (Reusable Blocks per Project)

**Inherits from:** Layers 03 + 02 + 01 + 00

**Uses:**
- All Layer 02 tokens (cannot change)
- All Layer 03 rules (cannot break)

**Specialization Allowed:**
- Component sizing
- Component arrangement
- Component emphasis
- Project-specific variations (within token/rule constraints)

**Cannot override:** Layers 03-00

**Tao Components (Example):**
- Header, Subheader, Hero
- Teaching Block (max 45 words)
- Key Insight, Clinical Example
- Reflection, Citation, Footer

**Atlas Components (Example):**
- Research Card, Citation Block
- Data Table, Formula Display
- Methods Section, Discussion

**Learn2Tape Components (Example):**
- Lesson Module, Quiz Question
- Progress Indicator, Achievement Badge
- Resource Link, Certificate

---

### Layer 05: COMPOSITIONS (Page Layouts per Project)

**Inherits from:** Layers 04 + 03 + 02 + 01 + 00

**Defines:**
- How Layer 04 components are assembled into pages
- Page layout blueprints per project

**Assembles:**
- Layer 04 components only
- All spacing from Layer 02 tokens
- All rules from Layer 03

**Specialization Allowed:**
- Component arrangement
- Component sequencing
- Page-specific emphasis

**Cannot override:** Layers 04-00

**Cannot modify:** Component specifications, token values

**Tao Compositions (Example):**
- Cover Page (Header + Subheader + Hero + Footer)
- Educational Page (Subheader + Teaching Block(s) + Key Insight + Citation(s))
- Reflection Page (Subheader + Reflection + Hero + Footer)
- Call to Action (Subheader + Hero + Teaching Block + Footer)

---

### Layer 06: IMPLEMENTATIONS (Software Renderers)

**Inherits from:** Layers 05 + 04 + 03 + 02 + 01 + 00

**Renders:**
- Layer 05 compositions exactly as specified
- Layer 04 components exactly as specified
- All Layer 02 tokens precisely
- All Layer 03 rules honored

**Tool Examples:**
- Adobe Express (Tao compositions)
- Figma (Atlas compositions)
- PowerPoint (L2T compositions)
- Web (Multi-project compositions)
- PDF (Print compositions)

**Specialization Allowed:**
- Tool-specific optimization
- File format selection
- Tool-specific rendering techniques

**Cannot override:** Layers 05-00

**Cannot modify:** Blueprints, components, rules, tokens

**Constraint:** No design decisions in implementation layer

---

### Layer 07: OUTPUTS (Final Exports)

**Inherits from:** Layers 06-00

**Renders:**
- Layer 06 implementations to final format
- No modification of rendered content

**Examples:**
- Instagram posts (1080×1350px PNG)
- LinkedIn articles (PDF)
- Website pages (HTML)
- Email newsletters (HTML)
- Printed books (PDF)
- PDF eBooks

**Constraint:** Outputs are immutable distributions

---

### Layer 08: INTELLIGENCE (Performance & Learning Loop)

**Inherits from:** Layers 07-00

**Gathers:**
- Performance metrics (views, engagement, clarity, accessibility)
- Component usage patterns (which work best)
- User feedback (is system effective?)
- Implementation friction (which tools work best)
- Evolution data (what changed, what improved)

**Analyzes:**
- Are principles being honored?
- Are tokens serving the work?
- Are rules preventing problems?
- Do components match their purpose?
- Do compositions work in practice?

**Informs (Evidence-Based Recommendations):**
- Layer 01 refinement (Principles still valid?)
- Layer 02 refinement (Token adjustments)
- Layer 03 refinement (Rule clarifications)
- Layer 04 refinement (Component improvements)
- Layer 05 refinement (Composition adjustments)
- Layer 06 refinement (Implementation improvements)

**Cannot override:** Layer 00 (Constitution is sacred)

**Feeds back to:** Layer 00 (completes feedback loop)

**Change protocol:** Proposals flow upward through hierarchy; changes filter downward

---

## COMPLETE INHERITANCE & CONSTRAINT MATRIX

| Layer | Inherits From | Must Honor | Can Specialize | Cannot Override | Feedback Role |
|-------|---------------|-----------|---|---|---|
| 00 | — | — | — | — | Sacred (annual review only) |
| 01 | 00 | Constitution | — | 00 | Receives intelligence refinement |
| 02 | 01 | Principles | — | 01, 00 | IMMUTABLE (locked globally) |
| 03 | 02 | Tokens | Per-project rules | 02, 01, 00 | Receives intelligence clarifications |
| 04 | 03 | Rules | Component variations | 03-00 | Receives intelligence improvements |
| 05 | 04 | Components | Page arrangements | 04-00 | Receives intelligence optimizations |
| 06 | 05 | Compositions | Tool optimizations | 05-00 | Receives intelligence tool improvements |
| 07 | 06 | Implementation | Export format | 06-00 | Generates data for Intelligence |
| 08 | 07 | All outputs | Evidence-based proposals | 00 (Constitution sacred) | Drives next iteration |

---

## SPECIALIZATION PERMISSION MATRIX

| Layer | Can Specialize | Method | Example |
|-------|---|---|---|
| 01 | ✓ | Add clarifications within Constitution | Tao emphasizes clinical warmth |
| 02 | ✗ | Tokens are immutable | All projects use same TYPE_H1 |
| 03 | ✓ | Add project-specific rules (enforce global rules more strictly) | Tao: max 45 words per Teaching Block |
| 04 | ✓ | Component variations using Layer 02 tokens | Tao Teaching Block vs. Atlas Research Card |
| 05 | ✓ | Page arrangements using existing components | Tao 4 page types vs. Atlas 6+ page types |
| 06 | ✗ | Tool optimization only | Adobe Express optimizations only |
| 07 | ✗ | Platform-specific distribution only | Export to Instagram or PDF |
| 08 | ✓ | Project-specific analytics | Tao engagement vs. Atlas engagement |

---

## PROHIBITED OVERRIDES

**Layer 02 Tokens:**
- ✗ Cannot change TYPE_H1 size
- ✗ Cannot change SPACE_32 value
- ✗ Cannot introduce colors outside palette
- ✗ No "special cases"

**Layer 03 Rules:**
- ✗ Cannot violate WCAG AA
- ✗ Cannot use unapproved colors
- ✗ Cannot break spacing grid
- ✗ Cannot ignore white space requirement

**Layers 04-07:**
- ✗ Cannot redefine parent layer elements
- ✗ Cannot change inherited specifications
- ✗ Cannot override inherited rules

---

## FEEDBACK LOOP MECHANISM

```
Layer 07 (Outputs)
    ↓ generates data
Layer 08 (Intelligence)
    ├─ Collects metrics
    ├─ Analyzes patterns
    └─ Generates evidence-based recommendations
         ↓
         ├─→ Layer 01 (Principles refinement)
         │   "Editorial restraint helps clarity"
         │   
         ├─→ Layer 02 (Never — LOCKED)
         │   
         ├─→ Layer 03 (Rules clarification)
         │   "Add: Citations require WCAG AAA contrast"
         │   
         ├─→ Layer 04 (Components improvement)
         │   "Reflection component model effective"
         │   
         ├─→ Layer 05 (Compositions optimization)
         │   "Reflection placement drives engagement"
         │   
         └─→ Layer 06 (Implementation improvement)
             "Adobe Express needs macro support"

        NEXT ITERATION (Loop repeats)
        Layers refined, Constitution unchanged
```

---

## SYSTEM INTEGRITY VERIFICATION

**Upward Validation:**
- Does Layer 04 component use only Layer 02 tokens? (Yes/No)

**Downward Consistency:**
- Does Layer 08 only propose changes, never override? (Yes/No)

**Horizontal Isolation:**
- Does Layer 03 Rule implementation require only Layer 02 tokens? (Yes/No)

**Feedback Loop:**
- Does Layer 08 Intelligence data feed back to Layer 00? (Yes/No)

**Specialization Boundaries:**
- Are all project specializations reinforcing (not contradicting) Layer 00-01? (Yes/No)

---

## PLATFORM STATUS

✅ Layer 00 (Constitution): DEFINED  
✅ Layer 01 (Principles): FROZEN  
✅ Layer 02 (Tokens): LOCKED GLOBALLY  
✅ Layer 03 (Rules): FROZEN  
✅ Layer 04 (Components): OPERATIONAL  
✅ Layer 05 (Compositions): OPERATIONAL  
✅ Layer 06 (Implementations): OPERATIONAL  
✅ Layer 07 (Outputs): OPERATIONAL  
🟡 Layer 08 (Intelligence): READY (data collection begins July 8)

---

## FINAL DECLARATION

**Finding My Wei Visual Operating System v2.0 is FROZEN.**

The 9-layer inheritance architecture is complete, documented, and operational.

Effective June 26, 2026:
- ✅ All design specifications LOCKED
- ✅ All inheritance relationships DEFINED
- ✅ All constraints DOCUMENTED
- ✅ Feedback loop mechanism ESTABLISHED
- ✅ Annual review protocol DEFINED

**No changes to Layers 00-07 until Annual Strategic Review (December 2026).**

Layer 08 (Intelligence) will operate continuously to gather feedback for future iterations.

---

**Approved by:** Drew Freedman, Editor-in-Chief  
**Documented by:** Chief of Staff (Claude)  
**Date:** June 26, 2026  
**Status:** 🟢 VOS FROZEN — EXECUTION PHASE BEGINS
