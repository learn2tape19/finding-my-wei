# MC-001: PUBLICATION MASTHEAD
## Complete Build Specification for Adobe Express

**Component ID:** MC-001  
**Version:** v1.0.0  
**Date:** July 29, 2026  
**Status:** Ready to Build  
**Estimated Build Time:** 15-20 minutes  

---

## DESIGN INTENT

MC-001 establishes the permanent editorial identity for The Tao of Clinical Touch.

Its purpose is not decoration.

Its purpose is immediate recognition.

The masthead should communicate:
- Editorial publication (not marketing)
- Clinical restraint (not florish)
- Permanence (not trend)
- Quiet authority (not loudness)

No element should compete with the article itself.

The masthead exists to orient the reader before disappearing.

When someone sees this component in 25 years, they should immediately know: "This is The Tao of Clinical Touch."

---

## NON-GOALS

MC-001 shall not:
- Become promotional
- Contain marketing language
- Include photography
- Include article titles
- Include author information
- Include decorative effects
- Vary between issues

Its sole responsibility is publication identity.

---

## CANVAS SETUP

### Coordinate System (Explicit)
- **Origin Point:** Top-left corner of canvas (0,0)
- **X-axis:** Horizontal, increases left to right
- **Y-axis:** Vertical, increases top to bottom
- **Unit:** Pixels (px)

**Principle:** Nothing critical is implied. All coordinates explicitly defined from this origin.

### Artboard Dimensions
- **Width:** 1600px (web standard)
- **Height:** 120px (fixed height, never compress)
- **Color Mode:** RGB
- **Background:** Transparent

### File Naming
Save immediately as: `MC-001_Publication_Masthead_v1.0`

---

## ELEMENT BREAKDOWN (In Layer Order, Top to Bottom)

### Element 1: Top Margin (Spacer)
**Type:** Rectangle (invisible, spacer)
- **Width:** 1600px
- **Height:** 20px
- **X Position:** 0
- **Y Position:** 0
- **Fill Color:** None / Transparent
- **Purpose:** Top padding
- **Status:** LOCKED (do not modify)

---

### Element 2: Enso Circle (Open Tao Brush)
**Type:** Image/Graphic
- **Source:** Open Tao Brush Circle (IA-001 source file)
- **Width:** 60px
- **Height:** 60px
- **X Position:** 40px (from left edge)
- **Y Position:** 20px (from top of canvas)
- **Opacity:** 100%
- **Rotation:** 0° (never rotate)
- **Fill:** Deep Clinical Navy #182633
- **Status:** LOCKED (position, size, color immutable)

**Visual Note:** The Enso appears on the left side of the masthead. It is the visual anchor.

---

### Element 3: Publication Title Text
**Type:** Text
- **Content:** "The Tao of Clinical Touch"
- **Font:** Garamond (or Cormorant Garamond if available)
- **Font Weight:** Regular (400)
- **Font Size:** 28px
- **Line Height:** 32px (1.14x)
- **Letter Spacing:** -0.5px
- **Color:** Deep Clinical Navy #182633
- **X Position:** 120px (from left edge, right of Enso)
- **Y Position:** 18px (from top of canvas)
- **Width:** 800px
- **Alignment:** Left
- **Status:** LOCKED (text, font, size, color, position immutable)

**Visual Note:** Publication title sits to the right of the Enso, starting 60px from left edge (40px Enso + 20px gap).

---

### Element 4: Issue Number Placeholder (EDITABLE)
**Type:** Text
- **Content:** "Issue [NUMBER]"
- **Font:** Garamond or Cormorant Garamond
- **Font Weight:** Regular (400)
- **Font Size:** 14px
- **Line Height:** 16px (1.14x)
- **Letter Spacing:** 0px
- **Color:** Charcoal #3a3a3a
- **X Position:** 120px (from left edge, aligned with title)
- **Y Position:** 58px (below the title text)
- **Width:** 200px
- **Alignment:** Left
- **Status:** EDITABLE (number can change per issue, but styling locked)

**Variable Text:** Replace "[NUMBER]" with actual issue number (e.g., "Issue 005")

**Visual Note:** Small subtitle below the main title. This is the ONLY field that changes per issue.

---

### Element 5: Gold Divider Rule
**Type:** Line / Rectangle
- **Width:** 1520px (full width minus margins)
- **Height:** 2px (thickness)
- **X Position:** 40px (from left edge)
- **Y Position:** 110px (from top of canvas)
- **Color:** Antique Gold #b8860b
- **Rotation:** 0° (horizontal)
- **Status:** LOCKED (position, thickness, color immutable)

**Visual Note:** Horizontal line spanning the width of the component, appearing below the text elements. This anchors and closes the masthead.

---

### Element 6: Bottom Margin (Spacer)
**Type:** Rectangle (invisible, spacer)
- **Width:** 1600px
- **Height:** 10px
- **X Position:** 0
- **Y Position:** 110px (below divider)
- **Fill Color:** None / Transparent
- **Purpose:** Bottom padding
- **Status:** LOCKED (do not modify)

---

## COLOR REFERENCE

| Element | Color Name | HEX | RGB | Usage |
|---|---|---|---|---|
| Enso Circle | Deep Clinical Navy | #182633 | RGB(24, 38, 51) | Primary mark |
| Title Text | Deep Clinical Navy | #182633 | RGB(24, 38, 51) | Publication name |
| Issue Number | Charcoal | #3a3a3a | RGB(58, 58, 58) | Secondary text |
| Divider Rule | Antique Gold | #b8860b | RGB(184, 134, 11) | Accent line |

---

## TYPOGRAPHY REFERENCE

| Text | Font | Size | Weight | Line Height | Letter Spacing | Color |
|---|---|---|---|---|---|---|
| Publication Title | Garamond | 28px | Regular (400) | 32px | -0.5px | #182633 |
| Issue Number | Garamond | 14px | Regular (400) | 16px | 0px | #3a3a3a |

---

## SPACING SUMMARY

| Measurement | Value | Purpose |
|---|---|---|
| Canvas Width | 1600px | Web standard |
| Canvas Height | 120px | Fixed (locked) |
| Left Margin | 40px | Enso and text positioning |
| Right Margin | 40px | Balance |
| Enso Size | 60×60px | Fixed mark size |
| Enso to Title Gap | 20px | Breathing room |
| Top Text Padding | 18px | Enso vertical alignment |
| Title to Issue Gap | 40px | Vertical spacing |
| Divider Y Position | 110px | Below all text |
| Divider Thickness | 2px | Subtle rule |

---

## VISUAL LAYOUT (Text Reference)

```
[Enso Circle]  "The Tao of Clinical Touch"
(60×60)        (28px Garamond, Navy)
               "Issue [NUMBER]"
               (14px Garamond, Charcoal)

═══════════════════════════════════════════════════
(2px Gold Rule, 1520px wide)
```

---

## ASSET AUDIT (Before Building)

Every asset referenced in MC-001 must exist and be identifiable. No placeholders. No recreated assets.

### Asset 1: Enso Circle (IA-001)
- **Asset ID:** IA-001
- **Name:** Canonical Enso Circle (Open Tao Brush)
- **Version:** 1.0
- **Repository Location:** `/finding-my-wei/foundry/assets/institutional/IA-001/`
- **Format:** PNG or equivalent image file
- **Source:** Founder-provided, July 29, 2026
- **Checksum:** [To be calculated upon archival]
- **Status:** Approved ✓
- **Display Specifications in MC-001:**
  - Size: 60×60px
  - Position: 40px left, 20px top
  - Color: #182633 (Deep Clinical Navy)
  - Opacity: 100%
  - Rotation: 0° (never rotate)
- **Verification:** Enso file exists and is accessible before build begins

### Asset 2: Typography System (TS-001)
- **Asset ID:** TS-001
- **Name:** Garamond Editorial Serif Family
- **Version:** 1.0
- **Repository Location:** Adobe Fonts library or Google Fonts
- **Font Name:** Garamond (or Cormorant Garamond if Adobe Express offers superior quality)
- **Status:** Approved ✓
- **Font Weights Used:** Regular (400)
- **Verification:** Font installed and rendering correctly in Adobe Express before build begins

### Asset 3: Color System (CS-001)
- **Asset ID:** CS-001
- **Name:** Tao Editorial Color Palette v1.0
- **Version:** 1.0
- **Repository Location:** `/finding-my-wei/foundry/design-system/CS-001/`
- **Approval Gate:** Gate 1 (July 29, 2026)
- **Status:** Approved ✓
- **Colors Used in MC-001:**
  - **Deep Clinical Navy:** #182633 (RGB 24, 38, 51)
  - **Antique Gold:** #b8860b (RGB 184, 134, 11)
  - **Charcoal:** #3a3a3a (RGB 58, 58, 58)
- **Verification:** All color values confirmed in Gate 1 approval

### Asset Audit Checklist
Before beginning construction, verify:
- [ ] IA-001 (Enso) file exists and is accessible
- [ ] IA-001 is the correct version (1.0)
- [ ] TS-001 (Garamond) font is installed in Adobe Express
- [ ] CS-001 color palette is locked and verified
- [ ] No placeholder assets exist
- [ ] No assets are recreated from memory or approximation
- [ ] All asset IDs are documented and traceable

**Audit Status:** All assets identified. No gaps. Ready to build.

---

## BUILD CHECKLIST (As You Work)

- [ ] Canvas created: 1600×120px, RGB, transparent background
- [ ] File saved as: MC-001_Publication_Masthead_v1.0
- [ ] Enso circle placed: 40px left, 20px top, 60×60px
- [ ] Enso colored: Deep Clinical Navy #182633
- [ ] Publication title text added: "The Tao of Clinical Touch"
- [ ] Title positioned: 120px left, 18px top
- [ ] Title styled: Garamond 28px, Navy #182633, -0.5px tracking
- [ ] Issue number field added: "Issue [NUMBER]"
- [ ] Issue number positioned: 120px left, 58px top
- [ ] Issue number styled: Garamond 14px, Charcoal #3a3a3a
- [ ] Gold divider line created: 1520px wide, 2px thick
- [ ] Divider positioned: 40px left, 110px top
- [ ] Divider colored: Antique Gold #b8860b
- [ ] All locked elements verified (Enso, title, divider)
- [ ] Issue number field confirmed as ONLY editable element
- [ ] Export preview generated

---

## VALIDATION CHECKLIST (When Complete)

Answer "yes" to each:

- [ ] Enso circle is clearly visible on left side
- [ ] Publication title reads "The Tao of Clinical Touch" clearly
- [ ] Issue number is positioned below title
- [ ] Gold divider is visible at bottom, spanning nearly full width
- [ ] Colors match specification (navy, gold, charcoal)
- [ ] Component feels balanced and proportional
- [ ] Typography hierarchy is clear (large title, smaller issue number)
- [ ] Component looks editorial and restrained (not busy)
- [ ] Component is reusable (could be copied into any issue design)

---

## LAYER LOCKING (In Adobe Express)

Once complete, lock all layers EXCEPT Issue Number field:

**LOCK THESE:**
- ✓ Enso Circle
- ✓ Publication Title Text
- ✓ Gold Divider Rule
- ✓ Top Margin Spacer
- ✓ Bottom Margin Spacer

**LEAVE EDITABLE:**
- ○ Issue Number Placeholder (only layer that changes per issue)

---

## EXPORT SPECIFICATION

### Preview Export (For Founder Review)
- **Format:** JPG
- **Quality:** Maximum (90-100%)
- **Size:** 1600×120px
- **Color Space:** RGB
- **Filename:** `MC-001_Publication_Masthead_v1.0_preview.jpg`

### Component Export (For Reuse)
- **Format:** Adobe Express native (.design file or exported component)
- **Preserves:** All locked properties, editable Issue Number field
- **Filename:** `MC-001_Publication_Masthead_v1.0.design`

---

## WHAT TO EXPECT

When complete, MC-001 should:
- ✓ Feel like a professional publication masthead
- ✓ Communicate quiet confidence (not flashy)
- ✓ Support the editorial aesthetic of the book cover
- ✓ Be instantly reusable for Issue 006, 007, etc.
- ✓ Maintain the "silence and emergence" principle (simple, clear, one primary element: the Enso)

---

## IF YOU GET STUCK

**Common Issues:**

**Q: "The Enso doesn't look right"**
A: Verify it's 60×60px, positioned at 40px left / 20px top, colored #182633, and not rotated.

**Q: "The title text doesn't align with the Enso"**
A: Title should start at 120px left (40px margin + 60px Enso + 20px gap) and 18px top (to align with Enso center vertically).

**Q: "The issue number seems off"**
A: It should be 40px below the title text (at 58px Y position total). It's meant to be secondary, smaller.

**Q: "The divider looks too thick/thin"**
A: Should be exactly 2px. If it looks wrong, check your zoom level (may be optical illusion at certain zoom percentages).

---

## NOTES

- This component is **locked and immutable** except for the Issue Number field
- Future issues will copy this component and change only the issue number
- The design should feel effortless when complete—if it feels fussy, simplify
- The component is NOT about being beautiful; it's about being clear and reusable

---

**Build Specification Version:** 1.0  
**Status:** Ready to Execute  
**Estimated Time:** 15-20 minutes  
**Difficulty:** Low (straightforward layout with 5 elements)
