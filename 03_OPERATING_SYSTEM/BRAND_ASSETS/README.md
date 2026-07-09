# Tao Brand Assets — Canonical Library

**Status:** Institutional Standard  
**Owner:** The Tao of Clinical Touch  
**Purpose:** Single source of truth for all Tao visual elements

---

## Directory Structure

```
03_OPERATING_SYSTEM/BRAND_ASSETS/
├── CHAPTER_SYMBOLS/           (9 canonical SVG symbols)
│   ├── 01_open_circle.svg
│   ├── 02_threshold_line.svg
│   ├── 03_eye.svg
│   ├── 04_arcs.svg
│   ├── 05_wave.svg
│   ├── 06_triangle.svg
│   ├── 07_parallel.svg
│   ├── 08_spiral.svg
│   ├── 09_radiating.svg
│   └── README.md
├── WATERMARK/                 (Ripple signature artwork)
│   ├── tao_ripple_watermark.png (canonical source)
│   └── README.md
└── README.md                  (this file)
```

---

## Chapter Symbols

**Status:** Complete and canonical  
**Location:** `/CHAPTER_SYMBOLS/`  
**Format:** SVG v2_fixed  
**Use:** Every Tao publication inherits its chapter symbol in upper-left corner

See `/CHAPTER_SYMBOLS/README.md` for complete reference.

---

## Ripple Watermark

**Status:** Canonical signature artwork  
**Location:** `/WATERMARK/`  
**Asset:** tao_ripple_watermark.png (high-resolution source)  
**Deployment:** Every hero image (5–8% opacity, integrated into photograph)

**Purpose:** Anti-theft editorial signature + brand recognition

**Usage in Images:**
- Extremely large (fills 40–60% of image)
- Cropped by canvas boundaries
- 5–8% opacity (visible only upon inspection)
- Integrated into photograph (not a separate layer)
- Present in all campaign images without exception

**Integration Notes for Claude:**
When generating Firefly prompts: "Integrate the canonical Tao ripple artwork as a large, subtle watermark (5–8% opacity), partially cropped into the composition as a permanent editorial signature."

---

## Color Palette

**Primary Palette (from Tao Visual Identity System):**
- Deep Navy: #1a1f2e
- Warm Linen: #f5e6d3
- Natural Oak: #a0826d
- Muted Sage: #7a9b8e
- Warm Charcoal: #3d3a33
- Soft White: #f9f8f7

**Accent Colors:**
- Bronze: #8b6f47
- Stone Gray: #9a9a9a
- Soft Moss: #8fa894
- Muted Earth: #a08968

---

## Typography

**Display Face (Headlines):** Garamond or similar classical serif  
**Body Face (Text):** Manrope (sans serif)  
**Utility Face (Captions/Data):** Manrope (same as body)

All faces available in the project or via Google Fonts.

---

## Governance

All assets in this directory are **institutional standards**.

- Never delete or modify without governance approval
- Version control is maintained in git
- Changes require evidence of material limitation from execution
- All derivatives (templates, prompts) reference canonical files
- No recreations or workarounds permitted

---

## For Claude AI Operations

When generating visual assets:

1. **Reference Chapter Symbols** → Use exact SVG from `/CHAPTER_SYMBOLS/[number]_[symbol].svg`
2. **Integrate Ripple Watermark** → Reference `/WATERMARK/tao_ripple_watermark.png` in Firefly prompts
3. **Apply Color Palette** → Use hex values from this directory
4. **Set Typography** → Manrope for body, Garamond for display
5. **Follow Placement Rules** → See Tao Visual Identity System v1.0

---

**Last Updated:** July 9, 2026  
**Canonical Repository:** `/Users/Drewdog19/finding-my-wei/03_OPERATING_SYSTEM/BRAND_ASSETS/`
