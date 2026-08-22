# AMTA 2026 Shop — Execution Receipt

**Status:** LIVE — Founder-approved, published
**URL:** https://taoclinicaltouch.com/shop-amta/
**WordPress Page ID:** 1398
**WordPress Media ID (AMTA artwork):** 1402

---

## What was built

Isolated AMTA campaign storefront forked from the production Tao signed-book Shop (`/shop/`).

### Commercial changes from production
- Required fulfillment selector: **Pick up at AMTA National — FREE** (default) or **Ship to me — $5**
- Campaign attribution: `shop_source = amta_2026`
- AMTA context banner: "Going to AMTA National? Order now and pick up your signed copy from Drew in Denver — no shipping charge."
- AMTA 2026 Denver artwork decal in hero (sticker treatment, -5deg rotation)
- AMTA pickup FAQ entry

### Products (unchanged from production)
- Signed Copy: $19.99
- Personalized + Signed: $24.99

### Stripe Payment Links (4 total)
| Combination | Total | Stripe URL fragment |
|------------|-------|-------------------|
| Signed + Pickup | $19.99 | `...btv8egakGfUQ03` |
| Personalized + Pickup | $24.99 | `...cxzgKMdwSfUQ02` |
| Signed + Shipping | $24.99 | `...apr0LO9gCfUQ00` (production) |
| Personalized + Shipping | $29.99 | `...bJeeVd26X413dyA1OafUQ01` (production) |

### Analytics events
All existing Shop events preserved with added parameters:
- `shop_source: "amta_2026"` on every event
- `fulfillment_method` on checkout and fulfillment events
- New event: `tao_fulfillment_select`
- Transport: dataLayer only → GTM-PP2CC4D6 → GA4
- No PII transmitted
- Retired GA4 ID G-FW3PRHTX2P absent

---

## Production regression
`/shop/` (Page 1277) verified unchanged: 17/17 checks PASS.
Zero AMTA contamination in production source.

## Gate results
- Gate 1 (functional proof): 101/101 PASS
- Gate 2 (Founder visual approval): APPROVED
- Gate 3 (analytics source verification): ALL PASS
- Final production regression: 17/17 PASS
- Network-layer GA4 verification: requires browser DevTools (documented)

---

## Files

| File | Purpose |
|------|---------|
| `CLAUDE_SHOP_AMTA_EXECUTION_HANDOFF.md` | Founder execution directive |
| `tao-shop-amta.js` | AMTA shop source (self-contained IIFE, 1019 lines) |
| `ASSETS/AMTA_2026_DENVER.png` | Official AMTA artwork (Media ID 1402) |
| `EXECUTION_RECEIPT.md` | This file |

## WordPress assets
- Page 1398: `/shop-amta/` — Elementor HTML widget, Elementor Full Width template
- Media 1402: AMTA 2026 Denver artwork (1200x1200 PNG)

---

## Lessons learned

### 1. Elementor widget type matters critically
The Elementor `text-editor` widget applies `wp_kses_post` sanitization to rendered output, stripping CSS properties like `position`, `transform`, `z-index`, `pointer-events`, `box-shadow`, and `clamp()`. It also mangles `<img>` tags inside JS template literals.

**The Tao Shop must always use the Elementor `html` widget (not `text-editor`).**

Production `/shop/` uses `html.default`. The AMTA page was initially created with `text-editor.default`, causing silent CSS stripping that produced dark-typography rendering bugs and prevented the decal from appearing.

Fix: change `widgetType` from `text-editor` to `html` and settings key from `editor` to `html` in `_elementor_data`.

### 2. Elementor dual-storage architecture
Elementor stores widget content in `_elementor_data` postmeta, NOT in `post_content`. Updating `post_content` via REST API does not change what Elementor renders. To update Elementor content programmatically:
1. Read `_elementor_data` via REST API (`context=edit`)
2. Parse as JSON, navigate to the widget, update `settings.html`
3. Write back via REST API `meta._elementor_data`
4. The page MUST be re-saved from the Elementor editor to trigger render cache regeneration

### 3. Elementor page template requirement
New pages default to the theme template, not Elementor Full Width. The production Shop uses `page-template-elementor_header_footer`. New Tao commerce pages must be set to **Elementor Full Width** page layout to match production rendering.

### 4. Stripe Payment Links for fulfillment variants
Each fulfillment method × product combination requires its own Stripe Payment Link. Pickup links have no shipping fee baked in; shipping links include $5. The checkout URL is selected dynamically based on `currentFulfillment` state.
