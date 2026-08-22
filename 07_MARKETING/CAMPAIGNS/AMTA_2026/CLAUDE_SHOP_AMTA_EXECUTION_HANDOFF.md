# CLAUDE EXECUTION HANDOFF — AMTA 2026 SHOP

**Status:** Founder-approved for immediate execution  
**Project:** The Tao of Clinical Touch — AMTA National 2026 direct-sales campaign  
**Target public URL:** `https://taoclinicaltouch.com/shop-amta/`  
**Event:** AMTA National Convention, Denver, August 27–29, 2026  
**Authority:** Founder decision, August 22, 2026  

---

## 0. EXECUTIVE DIRECTIVE

Build a dedicated AMTA campaign storefront by duplicating the currently approved and production-verified Tao signed-book Shop experience.

This is a **fork, not a redesign**.

The existing production Shop is the commercial baseline and must remain untouched.

### Non-negotiable rule

> **DO NOT MODIFY THE EXISTING PRODUCTION SHOP PAGE OR ITS APPROVED VISUAL/CHECKOUT BEHAVIOR.**

Create an isolated AMTA variant whose only intentional commercial difference is fulfillment choice plus campaign attribution.

The AMTA page must retain the same design language, products, prices, personalization behavior, testimonials, bulk-order pathway, checkout mechanics, and proven analytics discipline unless this handoff explicitly states otherwise.

---

# 1. PRODUCTION BASELINE — TREAT AS READ-ONLY

The following commercial flow was production-verified before this work order:

- Tao signed-book Shop
- Signed book: **$19.99 + $5 shipping**
- Personalized + Signed book: **$24.99 + $5 shipping**
- US-only shipping
- Bulk-order inquiry pathway
- Bulk Orders canonical URL: `https://taoclinicaltouch.com/bulk-orders/`
- GTM container: `GTM-PP2CC4D6`
- Active GA4 property: `G-BEBQ6ENK69`
- Retired GA4 property `G-FW3PRHTX2P` must remain absent
- Existing Shop + Bulk Orders analytics were verified at network layer
- No PII is permitted in analytics payloads
- Existing Shop typography/design and approved CSS are considered locked unless required for the new AMTA fulfillment UI
- Existing Bulk Orders flow must continue functioning exactly as verified

The previously completed Bulk Orders production architecture included these hard-won implementation lessons and they remain authoritative:

1. Scope CSS semantically by zone.
2. Preserve approved CSS once visual QA passes.
3. Be alert to Elementor widget-wrapper/container sibling class placement.
4. Host-theme `!important` cascade can defeat local styling.
5. Resolve the actual Elementor form via `form.elementor-form`, not generic wrapper assumptions.
6. Elementor may clear fields before `submit_success`; snapshot needed analytics values before submission.
7. Verify analytics at the **network layer**, not only in console/dataLayer previews.
8. Never transmit PII through GA4/GTM.

---

# 2. FIRST ACTION — SOURCE RECOVERY / PREFLIGHT

Do not begin implementation by reconstructing the Shop from memory.

Locate and load the exact current production source used by the approved Shop.

Expected source indicator from prior implementation history:

- `tao-shop.js`

However, do not assume path or repository. Resolve the actual live source first.

### Preflight must report

Before code changes, output:

- repository name
- branch
- current commit SHA
- git status
- exact Shop source file path(s)
- any CSS file(s) or inline Elementor CSS governing the page
- page/template source relationship
- current production Shop URL
- confirmation that the existing Shop implementation is unchanged and readable
- current analytics event names emitted by the Shop

If the production source cannot be located, **stop implementation and report the missing source rather than recreating it from memory.**

---

# 3. AMTA PAGE — PUBLIC IDENTITY

Create an isolated campaign page at:

`https://taoclinicaltouch.com/shop-amta/`

Preferred WordPress page title:

**Shop — AMTA National 2026**

The page should be recognizably the same Tao Shop, not a separate microsite.

### Campaign identity

Use a subtle AMTA-specific intro/utility message near the purchase area. Do not visually overwhelm the approved Shop design.

Founder-approved messaging direction:

**Going to AMTA National?**  
Order your signed copy now and pick it up from Drew in Denver — no shipping charge.

Pickup detail:

**AMTA National Pickup — Denver, August 27–29**  
We’ll coordinate your pickup location at the convention.

Do not hard-code a booth, classroom, host exhibitor, or exact pickup time unless the Founder later approves one. Convention logistics may move.

---

# 4. PRODUCTS — PRESERVE CURRENT OFFER

Do not alter product pricing.

### Product A

**Signed Copy**  
Price: **$19.99**

### Product B

**Personalized + Signed Copy**  
Price: **$24.99**

Retain the existing personalization/inscription input and behavior exactly unless a technical change is required to support fulfillment.

Retain the existing featured/default treatment of Personalized + Signed if that is how the approved Shop currently behaves.

Retain Bulk Orders pathway.

---

# 5. FULFILLMENT — PRIMARY AMTA CHANGE

The AMTA page must add a required fulfillment choice.

### Option 1 — primary/default for this campaign

**Pick up at AMTA National — FREE**

Internal normalized value:

`amta_pickup`

Shipping charge:

`$0`

### Option 2

**Ship to me — $5**

Internal normalized value:

`shipping`

Shipping charge:

`$5`

### UX requirements

- AMTA pickup should appear first.
- The fulfillment choice must be explicit before payment.
- Total price must update correctly when fulfillment changes.
- Pickup cannot silently inherit a $5 shipping charge.
- Shipping cannot silently lose the $5 charge.
- Selection must survive all relevant state changes prior to successful purchase.
- Mobile interaction must be easy to tap quickly from a QR-code entry session.
- Accessibility: proper labels, keyboard operability, visible selected state, no color-only state indication.

### Address behavior

If the existing checkout architecture collects a shipping address as part of a hosted/payment flow, do not invent a fragile workaround.

Preferred behavior:

- `amta_pickup`: do not require an unnecessary shipping-address workflow if the current stack permits conditional suppression safely.
- `shipping`: retain the proven US shipping/address behavior.

If the payment platform requires an address regardless of fulfillment, preserve payment stability and clearly document that constraint rather than weakening checkout.

---

# 6. ORDER DATA / FULFILLMENT RECORD

Every successful AMTA-page transaction must make fulfillment unambiguous to Drew.

At minimum the operational order record must expose:

- product type
- quantity
- personalization text when applicable
- fulfillment method
- amount charged
- transaction/order identifier already provided by the payment system

For pickup orders, fulfillment must be visibly labeled:

**AMTA National Pickup**

Do not rely on analytics as the fulfillment record.

Analytics are measurement only. The commerce/order record remains the operational source of truth.

---

# 7. ANALYTICS — AMTA CAMPAIGN ATTRIBUTION

The page must be measurable as an AMTA-specific campaign without transmitting PII.

### Campaign constant

Use:

`shop_source = amta_2026`

### Fulfillment values

Use:

`fulfillment_method = amta_pickup`

or

`fulfillment_method = shipping`

### Required measurement principle

Preserve existing Shop event names wherever possible. Extend their parameters rather than creating unnecessary duplicate event families.

For every existing Shop interaction event emitted from `/shop-amta/`, add or ensure:

- `shop_source: "amta_2026"`
- `fulfillment_method` when a fulfillment method has been selected and is contextually relevant

Recommended additional event only if the existing taxonomy has no equivalent:

`tao_fulfillment_select`

Parameters:

- `shop_source`
- `fulfillment_method`
- `product_type` if already safely available and non-PII

### Purchase / success measurement

On successful purchase, ensure the success event includes, where supported by the current event contract:

- `shop_source = amta_2026`
- `fulfillment_method`
- non-PII product/order value fields already permitted by the existing Shop taxonomy

### Absolutely prohibited from analytics

Do not send:

- purchaser name
- email address
- phone number
- mailing address
- personalization/inscription text
- payment details
- any free-text user input

### Analytics QA

Verify in this order:

1. UI interaction
2. dataLayer/event construction
3. GTM trigger/tag behavior
4. GA4 network request
5. correct measurement ID = `G-BEBQ6ENK69`
6. retired ID `G-FW3PRHTX2P` absent
7. no PII in request payload

Network-layer evidence is required for final sign-off.

---

# 8. QR / CAMPAIGN ENTRY READINESS

The page will become the destination for an AMTA QR code used in:

- pre-convention social
- Stories
- convention signage where permitted
- Drew’s phone/device
- possible physical tabletop collateral

The page must therefore be optimized for direct mobile entry.

### Public URL to encode

Use the clean canonical URL:

`https://taoclinicaltouch.com/shop-amta/`

Do not encode a long ugly public-facing URL as the primary printed QR destination.

If campaign query parameters are useful for specific distribution channels, they may be added to channel-specific QR variants, but `/shop-amta/` itself remains the canonical landing page.

Recommended UTM convention if implemented later:

- `utm_source=amta`
- `utm_medium=qr`
- `utm_campaign=amta_2026`

Do not block launch on additional UTM complexity; the page-level `shop_source=amta_2026` attribution is the minimum requirement.

---

# 9. VISUAL / COPY CHANGE BOUNDARY

This is **not** permission to redesign the Shop.

Preserve:

- layout
- typography
- colors
- book imagery
- testimonials
- CTA hierarchy
- product card styling
- personalization UX
- bulk CTA
- responsive behavior

Only introduce the minimum new UI needed for:

1. AMTA campaign context
2. fulfillment choice
3. pickup explanation

Do not add Sidekick Air promotion to this page during this work order.

Do not turn the page into an AMTA event poster.

Commerce clarity wins.

---

# 10. IMPLEMENTATION ARCHITECTURE

Preferred architecture is explicit isolation from production.

### Requirement

The AMTA implementation must not create conditional logic that risks changing `/shop/` simply because shared JavaScript is loaded globally.

Safe patterns include:

- dedicated AMTA page root class/data attribute
- isolated initialization guard tied to the AMTA page
- duplicated configuration with a shared stable core only if the shared core can remain behaviorally identical for production

Example semantic guard concept:

```js
const isAmtaShop = document.body.classList.contains('...') ||
  document.querySelector('[data-tao-shop-campaign="amta_2026"]');
```

Do not copy this literally unless it matches the live DOM. Resolve the actual Elementor/page structure first.

### Preferred configuration pattern

If the current code permits clean configuration without production regression, favor a campaign config object such as:

```js
const shopConfig = {
  source: 'amta_2026',
  fulfillment: {
    default: 'amta_pickup',
    options: {
      amta_pickup: { fee: 0 },
      shipping: { fee: 5 }
    }
  }
};
```

This is an architectural direction, not permission to rewrite working production code.

**Smallest safe change wins.**

---

# 11. FAILURE MODES TO PREVENT

Explicitly test against these regressions:

- `/shop/` accidentally shows AMTA pickup
- `/shop/` pricing changes
- shipping disappears from standard Shop
- AMTA pickup still charges $5
- AMTA shipping charges $0
- switching product type resets fulfillment incorrectly
- switching fulfillment clears personalization
- personalization submission is lost
- duplicate click handlers fire
- duplicate analytics events fire
- purchase fires before confirmed success
- Elementor clears required state before success analytics snapshot
- bulk-order link breaks
- mobile CTA becomes obscured by new fulfillment UI
- PII enters dataLayer or GA4
- old GA4 ID reappears
- styling leaks to unrelated Elementor widgets

---

# 12. QA MATRIX — REQUIRED BEFORE PUBLISH

Test on desktop and mobile.

## A. Production regression

- `/shop/` loads normally
- standard products/prices unchanged
- standard shipping unchanged
- personalization unchanged
- bulk-order pathway unchanged
- existing analytics unchanged

## B. AMTA Signed + Pickup

Expected total:

**$19.99**

Verify:

- pickup selected
- no $5 shipping charge
- order record says AMTA National Pickup
- success behavior correct
- analytics carries `amta_2026` + `amta_pickup`

## C. AMTA Personalized + Pickup

Expected total:

**$24.99**

Verify:

- personalization retained
- pickup selected
- no $5 shipping charge
- operational order contains personalization
- analytics contains no personalization text

## D. AMTA Signed + Shipping

Expected total:

**$24.99**

Verify:

- shipping selected
- $5 charge applied once
- shipping requirements present
- order record says shipping
- analytics carries `amta_2026` + `shipping`

## E. AMTA Personalized + Shipping

Expected total:

**$29.99**

Verify all fields/state/order/analytics.

## F. State transitions

Repeatedly toggle:

- pickup → shipping
- shipping → pickup
- Signed → Personalized
- Personalized → Signed

Verify totals and state on every transition.

## G. Failure/cancel paths

Verify:

- failed payment does not emit purchase success
- canceled payment does not emit purchase success
- retry does not duplicate handlers or amounts

---

# 13. FOUNDER APPROVAL GATES

Do not publish immediately after implementation.

### Gate 1 — local/staging functional proof

Provide:

- screenshot desktop
- screenshot mobile
- Signed + Pickup total
- Personalized + Pickup total
- Signed + Shipping total
- Personalized + Shipping total
- analytics network evidence
- production Shop regression evidence

### Gate 2 — Founder visual approval

Founder reviews the AMTA page appearance and fulfillment UX.

### Gate 3 — production publish

After Founder approval:

- publish `/shop-amta/`
- run live purchase-path QA without creating unnecessary real charges if safe test tooling exists
- verify live network analytics
- verify canonical Bulk Orders link
- verify production Shop remains unchanged

---

# 14. DELIVERABLES

Claude must return a completion report containing:

1. repository and branch used
2. starting SHA
3. ending SHA
4. files created/modified
5. public/staging URL
6. exact fulfillment implementation
7. exact analytics event/parameter changes
8. proof production `/shop/` is unchanged
9. proof all four price combinations are correct
10. proof no PII is transmitted to analytics
11. GA4 network verification
12. known limitations, if any
13. rollback instructions

If code is committed, commits should be narrowly scoped and clearly named.

Suggested branch:

`amta-2026-shop-pickup`

Suggested commit family:

- `feat(shop): add isolated AMTA campaign storefront`
- `feat(shop): add AMTA pickup fulfillment option`
- `feat(analytics): attribute AMTA shop and fulfillment`
- `test(shop): verify AMTA fulfillment and production regression`

Do not combine unrelated campaign/social work into these commits.

---

# 15. DEFINITION OF DONE

This work order is complete only when:

- `/shop-amta/` exists
- it visually matches the approved production Shop
- Signed = $19.99
- Personalized + Signed = $24.99
- AMTA Pickup = $0
- Shipping = $5
- correct totals are displayed/charged
- fulfillment is present in the operational order record
- personalization works
- Bulk Orders still works
- `/shop/` is unchanged
- `shop_source = amta_2026` is measurable
- fulfillment method is measurable
- no PII is sent to analytics
- GA4 requests use `G-BEBQ6ENK69`
- `G-FW3PRHTX2P` is absent
- desktop/mobile QA passes
- Founder approves before production publication

---

# 16. CLAUDE START COMMAND

Use this exact operating intent when beginning:

> **AMTA Shop Build — Controlled Fork.** Load this handoff as the execution authority. Recover the exact current production Tao Shop source before modifying anything. Treat the existing production Shop as read-only and regression-protected. Build `/shop-amta/` as an isolated clone whose only intentional commercial changes are AMTA campaign context and a required fulfillment selector: `Pick up at AMTA National — FREE` or `Ship to me — $5`. Preserve the approved visual system, products, personalization, bulk-order path, checkout, and analytics discipline. Add `shop_source=amta_2026` and non-PII fulfillment attribution, verify GA4 at the network layer, and stop at the Founder visual/functional approval gate before publishing. Do not improvise architecture when the live source can be inspected. Smallest safe change wins.

---

**Founder directive:** Build now for AMTA National. Keep the proven Shop sacred. Fork, isolate, measure, verify.