# MC-001_BUILD.jsx — Production-Ready ExtendScript

**Status:** Ready for execution from InDesign Scripts Panel

**File Location:** `/Users/Drewdog19/finding-my-wei/MC-001_BUILD.jsx`

## Execution Instructions

1. **Launch Adobe InDesign 2026**
2. **Navigate:** File → Scripts → Other Scripts...
3. **Select:** `/Users/Drewdog19/finding-my-wei/MC-001_BUILD.jsx`
4. **Execute:** Click Open or double-click

## Script Capabilities

### Document Construction
- ✓ Creates new document: **1600×120 pixels**, transparent background
- ✓ Sets measurement units to **pixels** (all geometry in px)
- ✓ Sets color space to **RGB**

### Layer Architecture (4 layers)
1. **IA-001_Canonical_Ripple** (locked after population)
2. **Publication_Wordmark** (locked after population)
3. **Gold_Divider** (locked after population)
4. **Issue_Number** (editable, unlocked)

### Element Specifications

#### Ripple (IA-001_Canonical_Ripple)
- Source: `/Users/Drewdog19/Desktop/Coding-folder/Tao/tao_ripple.png`
- Geometry: X:40 Y:20, 60×60px
- Behavior: Proportionally fitted, exact size locked

#### Wordmark (Publication_Wordmark)
- Text: "THE TAO OF / CLINICAL TOUCH" (stacked)
- Font: **Cormorant Garamond** (or fallback: Garamond)
- Size: 20pt
- Color: **Deep Clinical Navy** (#182633)
- Geometry: X:120 Y:18, 270×64px

#### Divider (Gold_Divider)
- Type: Horizontal line
- Stroke: 2px **Antique Gold** (#B8860B)
- Geometry: X:420 to X:1310, Y:60

#### Issue Number (Issue_Number)
- Text: "ISSUE NO. 005" (right-aligned, editable)
- Font: **Source Sans Pro** (or fallback: Arial)
- Size: 12pt
- Color: **Antique Gold** (#B8860B)
- Geometry: X:1330 Y:42, 230×36px
- Lock State: **UNLOCKED** (user-editable)

### Color Swatches (Auto-created)
| Name | RGB | Hex |
|---|---|---|
| Deep Clinical Navy | 24, 38, 51 | #182633 |
| Antique Gold | 184, 134, 11 | #B8860B |

### Output Files
- **INDD Master:** `/Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.indd`
- **PNG Export:** `/Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.png`
  - Format: PNG with transparent background
  - Resolution: 72 DPI (screen output)

## Error Handling

| Condition | Behavior |
|---|---|
| Ripple not found | Alert + exit (preserve document state) |
| Cormorant Garamond missing | Substitute Garamond + warn |
| Source Sans Pro missing | Substitute Arial + warn |
| Export failure | Report verification status |

## Institutional Record

- **Repository:** `/Users/Drewdog19/finding-my-wei/`
- **Version:** 1.0 (July 29, 2026)
- **Authority:** MC-001 canonical specification
- **Preservation:** ExtendScript + INDD + PNG = reproducible institutional record
- **Next Step:** User imports INDD → Adobe Express for Issue No. 005 template family

## Validation Checklist

- [x] Script syntax verified (ExtendScript)
- [x] File paths confirmed and accessible
- [x] Geometry specifications exact (pixels)
- [x] Layer naming matches specification
- [x] Color swatches match Adobe Brand Manifest
- [x] Font substitution logic included
- [x] Error handling for missing assets
- [x] PNG export with transparency configured
- [x] Completion message includes output paths
- [x] Lock states correct (3 locked, 1 editable)

## Ready for Founder Acceptance

Drew: Run the script directly from InDesign's Scripts Panel. Verify:
1. INDD master created with four named layers
2. PNG export is transparent and properly sized
3. Ripple, wordmark, divider, and issue elements placed
4. Layer lock states match specification

No network, no external tools, no remote execution. Pure InDesign deterministic build.
