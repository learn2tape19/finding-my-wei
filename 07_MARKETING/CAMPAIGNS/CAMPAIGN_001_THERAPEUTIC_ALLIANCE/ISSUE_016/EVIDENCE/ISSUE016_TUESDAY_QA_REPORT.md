# ISSUE No. 016 — Tuesday Visual QA Report

**Status: FOUNDER APPROVED — October 12, 2026**  
**Date:** October 12, 2026  
**Scope:** Tuesday Feed Build 1 and Landscape Build 2 only. No Stories, other days, uploads, scheduling, or publishing.

## Deliverables and dimensional checks

| Final PNG | Required W×H | Canvas preflight | Export check: macOS image decoder | Independent PNG IHDR and full Pillow decode |
|---|---:|---|---|---|
| ISSUE016_TUE_FEED_BUILD1_1080x1380_v02_DRAFT.png | 1080×1380 | PASS — blank target canvas created, saved, reopened at 1080×1380 before generation | PASS — 1080×1380 | PASS — 1080×1380 |
| ISSUE016_TUE_LANDSCAPE_BUILD2_1200x628_v02_DRAFT.png | 1200×628 | PASS — blank target canvas created, saved, reopened at 1200×628 before generation | PASS — 1200×628 | PASS — 1200×628 |

Both final files are real PNGs; their full pixel data decoded successfully.

## Production method and exact-size export

Used the built-in image generation tool in two separate calls, with separate exact-size preflight canvases and format-specific compositions. Existing local Tuesday artwork served only as editorial style reference. No finished Feed image was supplied as a source for Landscape.

The generator did **not** preserve the requested native dimensions, despite the exact-size canvas references. This limitation was handled before delivering approval candidates:
- Feed generation: 1110×1417. Native-pixel outer bleed trimmed to the verified 1080×1380 target (top offset 18, left offset 0). No scaling or stretching. All approved text and visible hands remain intact.
- Landscape generation: 1734×907. This independent horizontal composition was proportionally downsampled by height to 628, producing exactly 1200×628. No separate axis stretching, no conversion from another format, and no Feed reuse.

Final output dimensions are exact, not approximations. Preflight canvas verification and post-export verification are separate completed steps. Final exported files were then reopened at original resolution for copy and visual inspection.

## Word-by-word rendered-copy proof

All seven approved strings were visually checked in both final exports, including capitalization, punctuation, final period, and line-wrap continuity.

| Exact approved string | Feed | Landscape |
|---|---|---|
| ISSUE No. 016 | PASS | PASS |
| THE CLINICAL PRACTICE OF | PASS | PASS |
| TRUST | PASS | PASS |
| Tuesday | PASS | PASS |
| Make the Next Step Understandable | PASS | PASS |
| The Tao of Clinical Touch | PASS | PASS |
| A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION. | PASS | PASS |

Landscape headline and tagline wrap across lines without changing words. Letter spacing is editorial styling, not added wording. No extra caption, CTA, hashtag, byline, or generated background lettering is present.

## Visual and hierarchy inspection

| Check | Feed | Landscape |
|---|---|---|
| TRUST is dominant and largest; Tuesday and daily headline follow | PASS | PASS |
| ISSUE No. 016 used exactly | PASS | PASS |
| Charcoal, teal, cream; established serif editorial/publication treatment | PASS against available local styling reference | PASS against available local styling reference |
| Female therapist demonstrates shoulder movement on herself | PASS | PASS |
| Fully clothed female patient observes with hands resting on her lap | PASS | PASS |
| Bright contemporary clinical setting and attentive expressions | PASS | PASS |
| Arms, shoulders, hands, posture, and faces visually plausible | PASS — no obvious deformity found | PASS — no obvious deformity found |
| No anatomical imagery, skeletons, charts, forced positioning, or hands-on treatment | PASS | PASS |
| Independent composition, no distortion or cross-format repurposing | PASS | PASS |
| All copy readable and uncut in the final export | PASS | PASS |

The available styling references are the existing local Tuesday files inspected in this workspace; this report does not claim an unavailable Monday image was independently inspected. Exact historical font files/color values were not supplied, so the match is visual rather than a certified font-token match.

## File integrity

- Feed SHA-256: `c541d5d4cdc2f08770620019b57105e3c16923fa119645c0cea108fbf56f7f00`
- Landscape SHA-256: `1238b0764f2085bfa60e6f927c34ee45b3fce231352b1926e8ca8c6fc4a2daef`

## Approval gate

Drew explicitly approved both delivered Tuesday v02 assets with the message “approved” on October 12, 2026. Approved copies are byte-identical to the reviewed DRAFT files; the SHA-256 values above apply to both.

- `ISSUE016_TUE_FEED_BUILD1_1080x1380_v02_APPROVED.png`
- `ISSUE016_TUE_LANDSCAPE_BUILD2_1200x628_v02_APPROVED.png`

Both assets are **FOUNDER APPROVED**. Original reviewed DRAFT files remain retained for provenance. This approval does not authorize publishing. No additional production or publishing was performed when recording approval.

## Prompt record — built-in image generation

### Feed
```text
Use case: ads-marketing. Create only Tuesday Feed Build 1. Image 1 is exact verified 1080x1380 blank target canvas: preserve its pixel dimensions EXACTLY, don't upscale. Image 2 is typography/palette reference ONLY, not an edit target. Compose a NEW editorial photographic artwork at exactly 1080 pixels wide by 1380 pixels tall. Cream charcoal teal palette and elegant high-contrast serif editorial typography like reference. Top approximately 460px reserved for editorial text, photographic clinical scene middle, bottom publication branding.
Exact text ONLY, case and punctuation exactly:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Tuesday
Make the Next Step Understandable
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Hierarchy: small issue identifier and small uppercase THE CLINICAL PRACTICE OF; huge dominant TRUST on its own line, by far the largest text, then teal Tuesday, then daily headline subordinate to TRUST. Bottom masthead serif and tagline uppercase with final period.
Scene: female therapist wearing teal demonstrates a SIMPLE shoulder movement ON HERSELF raising one arm gently out to the side to shoulder level with relaxed elbow, palm naturally forward. Attentive fully clothed female patient in cream sits watching with BOTH her hands RESTING ON HER LAP, not demonstrating or receiving treatment. Bright contemporary clinic, natural daylight, calm engaged expressions, patient choice. Realistic hands/arms and relaxed posture. No contact between them, no hands-on treatment, no skeleton, anatomical imagery, anatomy posters, charts, force, diagrams. Independent new vertical composition, don't reuse existing photo. Export PNG 1080x1380 exactly.
```

### Landscape
```text
Use case: ads-marketing. Create Tuesday LANDSCAPE Build 2 ONLY. Image 1 is independently established 1200x628 blank canvas; preserve EXACTLY width 1200 height 628 pixels. Image 2 is editorial branding/typography reference ONLY; do not reuse its composition or photograph. New independent horizontal editorial design. Cream charcoal teal palette, elegant high-contrast serif. Text column left roughly 48% width, fresh photographic scene right 52%. Keep safe inset at least 40 px around all text and all hands, with cream bleed border. TRUST must be by far largest word around 105px and its own line.
Exact text, verbatim with case/punctuation:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Tuesday
Make the Next Step Understandable
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Issue small top; THE CLINICAL PRACTICE OF small uppercase one line or two, TRUST enormous charcoal, Tuesday teal subordinate, daily headline serif in two lines subordinate. Bottom left publication masthead and uppercase tagline with final period, fully readable, can wrap into two lines.
Scene right: female therapist wearing teal demonstrates gentle simple shoulder movement ON HERSELF, one arm lifted to the side at shoulder height, softly bent elbow and normal relaxed open hand wholly within frame. Fully clothed female patient wearing cream observes attentively with BOTH hands RESTING on her lap, not moving, no contact. Both facing one another, bright contemporary clinical setting, calm conversation, natural daylight. Plausible anatomy, five fingers per visible hand, no fused hands. No anatomical imagery, posters, skeletons, charts, diagrams, force, hands-on treatment. Use a fresh wide scene distinct from vertical Feed. Return exact-size PNG 1200x628 pixels, no upscale, no stretching, no resize from another format.
```

