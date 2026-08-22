# TAO PUBLICATION SIGNUP INFRASTRUCTURE

## Status
Founder-approved infrastructure initiative. Permanent capability, not campaign-specific.

## Objective
Build one canonical, reusable email subscription component for *The Tao of Clinical Touch* publication and inject that same component across selected Tao pages without creating divergent Elementor forms.

Core principle:

> Build once. Verify once. Inject everywhere.

## Founder Intent
The form is for readers who want to receive future Tao essays, clinical reflections, and publication emails. It should feel like an extension of the publication, not a generic marketing opt-in.

Preferred public-facing concept:

**Stay in the conversation.**

*The Tao of Clinical Touch explores the neuroscience of permission, therapeutic alliance, and the conditions that allow skilled touch to matter.*

Email field only.

Primary CTA: **Receive New Issues**

Supporting line: *New essays and clinical reflections. No noise. Unsubscribe anytime.*

Success state:

**You're in.**

*The next issue of The Tao of Clinical Touch will come to you directly.*

Copy may be tuned for layout, but do not turn this into promotional or high-pressure marketing language.

## Architectural Requirements

### 1. One canonical component
Create one reusable, versioned component, proposed name:

`tao-publication-signup.js`

Semantic root:

`#tao-publication-signup`

The component must support source/context configuration so the same implementation can be injected into multiple pages without duplication.

Examples:

- `blog_footer`
- `homepage`
- `shop`
- `shop_amta`
- `bulk_orders`
- `about_book`

Do not create separate independent Elementor forms per page.

### 2. Elementor lesson from Shop
Any code-driven WordPress/Elementor deployment must preserve the proven rendering architecture:

- correct page/template context
- Elementor **HTML widget**, not Text Editor
- raw component source preserved without `wp_kses_post` sanitization

Do not deploy code-driven markup through Elementor Text Editor widgets.

### 3. Brevo is the subscription system of record
Create or identify a dedicated publication list with a clear canonical name, recommended:

`Tao — Publication Subscribers`

Do not mix publication subscribers into unrelated marketing/customer lists unless Founder explicitly approves.

### 4. Double opt-in
Use Brevo double opt-in for this publication list.

Required flow:

Reader submits email → secure server-side bridge → Brevo double-opt-in request → confirmation email → confirmed subscriber added to publication list.

Do not silently downgrade to single opt-in.

### 5. Security boundary
Brevo API credentials must never be exposed in browser JavaScript, Elementor page source, GitHub, GA4, dataLayer, query parameters, or client-visible HTML.

The browser must submit to a server-side WordPress endpoint or equivalent secure bridge.

Before implementing, recover and inspect any existing Brevo/API bridge infrastructure already used by the site/repo. Reuse proven patterns where appropriate rather than inventing a second credential architecture.

If no safe server-side bridge exists, propose one and stop for Founder review before exposing credentials or deploying an insecure workaround.

### 6. Data minimization
Initial signup requires **email only**.

Do not require first name, last name, profession, phone, or other profile data.

The email address is PII and must stay within the secure subscription transaction path.

### 7. Analytics — zero PII
Analytics should describe behavior, not identity.

Proposed events:

- `tao_email_signup_view`
- `tao_email_signup_submit`
- `tao_email_signup_success`
- `tao_email_signup_error`

Recommended non-PII parameters:

- `signup_source`
- `component_version`
- `page_path`
- `publication: "tao_clinical_touch"`

Never send the email address, hashes of the email address, name, Brevo contact ID, or confirmation token into `dataLayer`, GTM, or GA4.

Preserve the site's current analytics discipline: `dataLayer` → GTM; do not add direct `gtag()` calls.

### 8. UX behavior
The component must include:

- accessible email field and label
- clear submit CTA
- disabled/loading state while submitting
- inline validation
- inline success state
- inline error state with retry guidance
- no unnecessary redirect after signup
- keyboard accessibility
- appropriate `aria-live` handling for result states
- responsive desktop/mobile layout

Do not expose raw API/Brevo error messages to the reader.

### 9. Styling
The component should visually belong to The Tao of Clinical Touch publication.

Requirements:

- scoped CSS under the semantic root
- no global typography/color leakage
- compatible with the established Tao navy/ivory/editorial visual language
- restrained, publication-first presentation
- no popup behavior in v1
- no modal in v1
- no aggressive urgency/coupon framing

The blog placement should feel like the natural final paragraph of the publication experience, not an ad.

## Initial Deployment Order

### Phase 1 — Build + verify
Create the canonical component and secure Brevo subscription bridge.

### Phase 2 — First injection
Inject into the canonical blog/article experience, immediately after article content and before the general site footer when technically appropriate.

This is the first production proving ground.

### Phase 3 — Propagation only after proof
Once blog signup is proven end-to-end, selectively inject the same canonical component into:

1. Homepage
2. Standard Shop
3. AMTA Shop if still operational/relevant
4. Bulk Orders
5. About/Book pages

Do not propagate until Phase 2 passes functional, visual, analytics, and subscription verification.

## Preflight — Claude Must Report Before Implementation

Before writing or deploying code, report:

1. Repository, branch, commit SHA, git status.
2. Existing Brevo-related source/config/docs discovered in the repo or WordPress stack.
3. Existing server-side mechanism available for authenticated Brevo API calls.
4. Current GTM/dataLayer convention to reuse.
5. Blog rendering architecture/template and safest injection point.
6. Whether the existing WordPress application-password bridge is required for deployment.
7. Exact Elementor widget type/template requirements for any injected code.
8. Proposed Brevo list name and whether it already exists.
9. Proposed double-opt-in template/flow and any Founder action required in Brevo.
10. Security review confirming no credential or subscriber PII will reach the client analytics layer.

Stop after preflight if any security or Brevo capability is uncertain.

## Functional Acceptance Criteria

The first blog implementation must prove all of the following:

1. Component renders correctly desktop/mobile.
2. Email field is the only required subscriber field.
3. Invalid email is rejected client-side without network submission.
4. Valid submission reaches the secure server-side endpoint.
5. API credential is not visible in browser source/network payload.
6. Brevo receives the double-opt-in request.
7. Subscriber receives the confirmation email.
8. Subscriber is not treated as confirmed until double opt-in is completed.
9. Confirmation places subscriber into the canonical Tao publication list.
10. Duplicate/already-subscribed handling is graceful and does not leak account state unnecessarily.
11. Success/error states work without page redirect.
12. `tao_email_signup_*` events reach dataLayer with source attribution.
13. No subscriber email or other PII appears in dataLayer/GA4.
14. Existing page functionality remains unchanged.
15. No global CSS leakage.

## Gate Structure

### Gate 0 — Preflight
Architecture and security findings only. No deployment.

### Gate 1 — Controlled test
Component and backend wired in a non-public or narrowly controlled test context. Founder reviews visual treatment and functional flow.

### Gate 2 — Blog production
Inject canonical component into blog/article production experience. Verify end-to-end double opt-in with a real test address and analytics/network proof.

### Gate 3 — Propagation
Only after Gate 2 Founder approval, inject the same component into additional Tao pages using source configuration rather than cloned code.

## Regression Protection

Do not modify production `/shop/`, `/shop-amta/`, Stripe checkout logic, or commerce analytics while building the signup infrastructure unless a separate Founder-approved change is required.

Do not redesign the Tao website or article template as part of this work.

## Documentation Requirements

At completion, record:

- canonical component source path
- backend endpoint/source path
- Brevo list name + list ID (ID may be documented internally; do not expose it client-side unless harmless and necessary)
- double opt-in template/config reference
- component version
- supported `signup_source` values
- analytics event contract
- injection locations
- deployment and rollback steps
- credential handling rules
- Elementor HTML-widget requirement where applicable
- lessons learned from Gate testing

## Founder Approval Boundary
Claude may perform investigation, implementation in controlled test state, and verification. Do not broadly propagate the component or alter unrelated production systems without the relevant Founder gate approval.
