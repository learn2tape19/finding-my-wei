# Web Commercial Architecture Standard

## Status
Founder-approved reusable institutional doctrine

## Origin
Promoted from the production-verified Tao Shop → Bulk Orders commercial flow completed August 21, 2026.

Reference implementation final SHA: `e60aa61fca34c9b5c7ecb53ece9ed5287353b0b5`

This standard supplements the Institutional Execution Standard. It exists to prevent future Tao, AREA, Learn2Tape, Boston Bodyworker, and other Finding My Wei web/commercial builds from rediscovering solved architecture and QA problems.

---

## 1. Architecture Before Styling

Define the complete customer path before building individual pages.

At minimum resolve:

`ENTRY → CTA → DESTINATION → FORM/CHECKOUT → DATABASE/TRANSACTION → COMMUNICATION → ANALYTICS → SUCCESS STATE`

A page is not complete because it looks correct. The commercial flow is complete only when the full public path is operational and verified.

---

## 2. Separate the QA Gates

Do not collapse visual, functional, delivery, analytics, and production QA into one review.

Use explicit gates:

1. Visual and responsive QA
2. Form or checkout configuration QA
3. Workflow and database/transaction QA
4. Email/delivery QA
5. Analytics staging QA
6. Production publication
7. Cross-link/navigation QA
8. Final network-layer regression verification

Once a gate passes, freeze it unless a later correction materially affects it. A form defect does not authorize redesigning approved CSS.

---

## 3. Smallest Scoped Remediation

After visual approval, remediation is not another build.

When QA finds a defect:

- identify the actual failing layer;
- change the smallest possible surface;
- do not refactor unrelated code;
- do not add cascading override layers without evidence they are necessary;
- re-test the corrected criterion and any directly affected dependencies;
- preserve already-approved criteria.

Repeated patches are a signal to diagnose selector, ownership, cascade, event timing, or architecture assumptions rather than adding more CSS or JavaScript.

---

## 4. Elementor / WordPress CSS Doctrine

### Scope semantically by zone
Commercial pages embedded in a host WordPress/Elementor theme must explicitly own their visual zones.

Typical zones include:

- editorial/light section;
- dark/navy section;
- white form card;
- CTA treatment;
- return/navigation section.

Do not assume host-theme global text/background rules are neutral.

### Respect host-theme cascade
Elementor kits and themes may apply global styles with `!important`. Diagnose the computed cascade before introducing overrides.

### Wrapper-class placement matters
Elementor may place custom classes on widget wrappers or container siblings rather than the inner semantic element expected by handwritten CSS/JS. Inspect the live DOM before relying on a class selector.

### Freeze approved CSS
Once visual and responsive QA pass, treat the approved CSS as frozen. Functional remediation must not reopen design unless the remediation demonstrably causes a visual regression.

---

## 5. Form Architecture Doctrine

### Resolve the real form element
Do not use a generic wrapper class when multiple Elementor widgets may carry that class.

Prefer resolving the actual form, e.g. `form.elementor-form`, then query fields relative to that form.

A selector that resolves successfully is not necessarily resolving the correct element.

### Validate required/optional semantics directly
Verify the served HTML and runtime browser validation, not only the Elementor editor panel.

Test at least:

- intended required fields;
- intended optional fields;
- email format;
- numeric minimums/maximums;
- dropdown options;
- success state;
- database/submission record.

### Elementor submission lifecycle
Elementor may clear form values before `submit_success` handlers consume them. Analytics values needed after submission should be captured/snapshotted before clearing.

However, diagnose selector correctness before assuming event timing is the cause.

---

## 6. Email Delivery Doctrine

A configured email action is not proof of delivery.

Verify separately:

- recipient address;
- sender address/authentication;
- requester confirmation address;
- Reply-To behavior;
- subject;
- success message;
- actual receipt of notification and confirmation messages.

Use a controlled test identity/address whenever possible so QA does not contact a real prospect.

Do not modify working email configuration after receipt is confirmed unless a new defect is observed.

---

## 7. Analytics Doctrine

### No PII
Never send personal form fields to analytics. Names, email addresses, phone numbers, organizations, city/state, free-text details, and similar personal data must remain outside GA4/GTM events.

### Stage before publishing
Prepare and validate GTM changes in a workspace before production publication. Record added/modified/deleted counts and avoid unrelated container changes.

### Verify at the network layer
The dataLayer is useful for debugging but is not final proof that analytics reached the intended property.

Production acceptance requires observing the actual GA4 network request and confirming:

- event name;
- intended measurement ID/property;
- expected parameters;
- expected ecommerce item cardinality;
- no retired property;
- no PII.

### GA4 transport details
Documented production behavior:

- numeric event parameters may be encoded with the `epn.` prefix rather than `ep.`;
- co-firing events may be batched in POST request bodies rather than visible in the query string.

Do not treat either as a failure without inspecting the full request.

### Validate cardinality
For ecommerce-style events, explicitly verify the number of items transmitted. A visually correct CTA can still send duplicate product objects.

---

## 8. Cross-Link Doctrine

Commercial architecture must define canonical destinations.

When a dedicated destination exists, all relevant CTAs should route to it rather than generic contact pages or legacy endpoints.

Verify links on the live public site after publication, including desktop and mobile where appropriate.

The Tao reference implementation established `/bulk-orders/` as the canonical destination for Tao multiple-copy inquiries.

---

## 9. Production Closeout Standard

A commercial flow may be marked PRODUCTION COMPLETE only after the observable public path has passed.

Minimum closeout evidence:

- public destination returns successfully;
- visual/responsive state approved;
- form/checkout behavior verified;
- database/transaction capture verified;
- required communications received;
- analytics published;
- analytics verified at network layer;
- no PII leakage;
- cross-links verified;
- existing analytics/functionality regression-tested;
- implementation documentation updated;
- final repository commit recorded.

Final verification should be performed against the live public system, not merely editor previews or local artifacts.

---

## 10. Reference Production Verification — Tao Shop → Bulk Orders

Completed August 21, 2026.

Canonical Bulk Orders URL: `https://taoclinicaltouch.com/bulk-orders/`

GTM: Version 3 — Tao Bulk Orders Analytics

Active GA4 measurement ID: `G-BEBQ6ENK69`

Retired measurement ID confirmed absent: `G-FW3PRHTX2P`

Verified events included:

- `page_view`
- `view_item_list`
- `select_item`
- `begin_checkout`
- `amazon_click`
- `faq_open`
- `bulk_inquiry_click`
- `bulk_form_view`
- `bulk_form_submit`

Bulk submission parameters verified included:

- `requested_quantity`
- `quantity_band`
- `intended_use`
- `submission_index`

Full attribution was present and zero PII was observed in analytics requests.

---

## 11. Future Build Acceleration

For future commercial architectures, begin from this sequence instead of rediscovering the workflow:

**A. Define customer journey and canonical URLs.**

**B. Define page zones and host-theme ownership.**

**C. Build the smallest complete interface.**

**D. Configure forms/checkout and communications before analytics closeout.**

**E. Define a privacy-safe event/parameter contract.**

**F. Stage GTM.**

**G. QA each layer independently.**

**H. Freeze passed layers.**

**I. Publish and verify the entire path at the network layer.**

**J. Capture the final architecture, defects, root causes, and commit SHA in the repository.**

The objective is not fewer tests. The objective is fewer repeated mistakes, smaller remediation loops, and faster movement from approved architecture to trustworthy production.
