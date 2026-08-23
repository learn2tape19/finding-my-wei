# Tao Publication Signup Infrastructure — Execution Receipt

## Status
Gate 3 PASS — All approved surfaces deployed and Founder-approved.

## Architecture

### Frontend Component
- **Source:** `tao-publication-signup.js` (v1.0.0)
- **Semantic root:** `#tao-publication-signup`
- **Source config:** `data-signup-source` attribute (per-surface — see Deployment Matrix)
- **Analytics:** `dataLayer` → GTM only. No `gtag()` calls.
- **PII boundary:** Email sent only via XHR to server endpoint. Never enters `dataLayer`, GA4, URLs, or logs.

### Server-Side Endpoint
- **Source:** `tao-subscribe-endpoint.php`
- **WordPress deployment:** Code Snippets plugin, Snippet ID 9
- **Route:** `POST /wp-json/tao/v1/subscribe`
- **Parameters:** `email` (required, sanitized), `source` (optional, sanitized)
- **Rate limiting:** Transient-based, 5 attempts per IP per 10 minutes
- **Secret boundary:** `TAO_BREVO_API_KEY` defined in `wp-config.php` (never client-side)

### Brevo Configuration
- **Publication list:** ID 64 ("Tao — Publication Subscribers")
- **DOI template:** ID 37 ("Tao — Publication Double Opt-In Confirmation")
- **DOI template tag:** `optin` (REQUIRED — see Lessons Learned)
- **Sender:** ID 3 — "Drew Freedman | Tao of Clinical Touch" <drew@mail.taoclinicaltouch.com>
- **Redirect URL:** https://taoclinicaltouch.com/subscription-confirmed/

### WordPress Pages
- **Subscription Confirmed:** Page 1425, slug `subscription-confirmed`, published
- **Gate 1 Test Page:** Page 1426, slug `signup-test` (can be deleted after Gate 3)

### Blog Template Injection
- **Template:** ID 863 ("Single Post — Tao / Campaign 001"), type `elementor_library`
- **Widget type:** `html` (NOT `text-editor`)
- **Insertion point:** Container `ffc5e24`, position [1] — after `theme-post-content`, before `post-comments`
- **Signup widget ID:** `b1a2c3d4`

## Analytics Event Contract

All events use `dataLayer.push()`. No PII in any event.

| Event | Fired When | Extra Params |
|---|---|---|
| `tao_email_signup_view` | Component renders | — |
| `tao_email_signup_submit` | Form submitted (after client validation) | — |
| `tao_email_signup_success` | Server returns success | `signup_code` |
| `tao_email_signup_error` | Server returns error or network failure | `error_code` |

Standard params on all events:
- `signup_source` (from `data-signup-source`)
- `component_version` (`"1.0.0"`)
- `page_path`
- `publication` (`"tao_clinical_touch"`)

## Production Deployment Matrix

| Surface | Page/Template | `signup_source` | Installed By | Status |
|---|---|---|---|---|
| Blog articles | Template 863 | `blog_footer` | Programmatic (REST API) | Gate 2 PASS |
| Book page | Page 493 | `about_book` | Programmatic (REST API) | Gate 3 PASS |
| Homepage | Page 51 | `homepage` | Programmatic (REST API) | Gate 3 PASS |
| Standard Shop | Page 1277 | `shop` | Founder (Elementor) | Gate 3 PASS |
| AMTA Shop | Page 1398 | `shop_amta` | Founder (Elementor) | Gate 3 PASS |
| Bulk Orders | Page 1291 | `bulk_orders` | Founder (Elementor) | Gate 3 PASS |
| About page | Page 33 | — | — | Excluded (legacy placeholder) |

### Additional `signup_source` values

| Value | Context |
|---|---|
| `gate1_test` | Gate 1 test page (Page 1426, can be deleted) |

## DOI Flow

1. Reader submits email → client-side validation
2. XHR POST to `/wp-json/tao/v1/subscribe`
3. Server validates, rate-limits, calls Brevo DOI endpoint
4. Brevo sends Template 37 confirmation email
5. Reader clicks "Confirm My Subscription"
6. Brevo confirms subscription, adds to List 64
7. Reader redirected to `/subscription-confirmed/`

## Self-Contained Presentation (Founder-Approved)

Component carries its own navy background (`#1a2a3a`) and contrast palette, eliminating dependency on host-page background:
- Background: `#1a2a3a` (navy, self-contained on component root)
- Headline: `#f5f0e8` (ivory)
- Description: `#c8cfd6` (light gray)
- Button: navy text on ivory background
- Footer: `#a0aab4`
- Border-top: `rgba(245, 240, 232, 0.25)`
- Validation error: `#e74c3c` (bright red for dark bg visibility)
- Inner wrapper: `.tao-signup-inner` (max-width 640px, centered)

## Rollback — Template 863

To restore Template 863 to its pre-signup state:

1. Load the original `_elementor_data` (4 top-level containers, container[1] has 4 children: `theme-post-content`, `post-comments`, `call-to-action`, `post-navigation`)
2. PUT to `/wp-json/wp/v2/elementor_library/863` with the original `_elementor_data` in meta
3. Open Template 863 in Elementor editor → click Update

The modification was a single widget insertion at container[1] position [1]. Removing it restores the original template exactly.

## Lessons Learned

### Brevo DOI `optin` tag requirement
Templates used with `POST /v3/contacts/doubleOptinConfirmation` MUST have the `optin` tag set in Brevo's template Advanced Settings. Without it, the API returns `400 invalid_parameter: "An active DOI template does not exist"` — even when the template is active (`isActive: true`) and contains the `{{ doubleoptin }}` confirmation link.

The Brevo MCP tool's `doiTemplate: true` flag is a client-side inference based on content inspection, not a reflection of server-side DOI eligibility. The `optin` tag is the server-side eligibility mechanism.

**Brevo's own documentation describes this tag as optional in the context of forms created inside Brevo** (where the form system has its own internal linking mechanism). For the API endpoint — which is the architecture used here — the tag is mandatory.

### Elementor HTML widget requirement
Same lesson as AMTA 2026 Shop: Elementor `text-editor` widgets apply `wp_kses_post` sanitization, stripping CSS properties and `<script>` tags. Code-driven components must use `html` widget type. When Elementor editor opens a page, it may convert programmatically-set `html` widgets back to `text-editor` — verify widget type after each editor save.

### Elementor template render cache
REST API updates to `_elementor_data` do not trigger Elementor's render cache rebuild. After any programmatic template modification, the template must be re-saved in Elementor editor to take effect.

### CSS duplication audit must account for canonical responsive selectors
The canonical component JS contains multiple `#tao-publication-signup` selectors — one in the main CSS block and one inside the `@media (max-width: 480px)` responsive rule. Duplication tests that count raw selector occurrences will produce false positives. Future audits must distinguish between separate canonical selectors (expected) and duplicated component/style payloads (defect).

### Host-page background must be judged from rendered production surface
WordPress CSS custom properties (e.g. `--wp--preset--color--base: #FFFFFF`) may not reflect the actual rendered background. Elementor container styles, theme overrides, and inherited section backgrounds can produce a completely different visual context. Always verify against the live rendered page, not preset/variable inspection alone. (Discovered during Book page 493 deployment — preset reported white, production surface rendered navy.)

## Gate Evidence

### Gate 0 — Preflight
- Repository, branch, Brevo capability, analytics convention, blog template architecture assessed
- Security review confirmed no credential exposure in client layer

### Gate 1 — Controlled Test
- DOI endpoint returns `doi_sent` for valid email
- Invalid email rejected with user-friendly message (no Brevo diagnostics leaked)
- Rate limiting functional
- Confirmation email received (Template 37)
- Confirmation click → redirect to `/subscription-confirmed/`
- Contact confirmed on List 64 with `DOUBLE_OPT-IN: "1"`
- Clean endpoint: response contains only `status`, `code`, `message`
- No PII in analytics layer

### Gate 2 — Blog Production
- Component renders on live article after post content, before comments
- Single instance (no duplicates)
- `signup_source: blog_footer`
- Widget type: `html` (correct)
- Contrast correction applied and Founder-approved
- Template 863 integrity preserved (all existing widgets intact)
- GTM container `GTM-PP2CC4D6` present
- Retired GA4 `G-FW3PRHTX2P` absent
- No credential or PII leakage

### Gate 3 — Multi-Surface Propagation

All surfaces verified against canonical `tao-publication-signup.js` (v1.0.0).

**Book Page 493** (`about_book`)
- Single instance, canonical JS exact match
- Self-contained background renders correctly on navy host page
- Structural integrity 7/7, all analytics events, security PASS

**Homepage 51** (`homepage`)
- Single instance, canonical JS exact match
- Cloudflare email-decode script injected between div and script (no functional impact)
- Structural integrity 7/7, all analytics events, security PASS
- Header/footer/personalization content intact

**Standard Shop 1277** (`shop`)
- Founder-installed in Elementor, technically verified
- Source attribution corrected from `about_book` → `shop` (copy-paste artifact)
- Canonical JS exact match, structural integrity 7/7, security PASS
- Commerce regression: shop JS, Stripe checkout, personalization, bulk orders link, GTM — all intact

**AMTA Shop 1398** (`shop_amta`)
- Founder-installed in Elementor, technically verified
- Source attribution corrected from `about_book` → `shop_amta` (copy-paste artifact)
- Underscore convention enforced (`shop_amta` not `shop-amta`)
- Canonical JS exact match, structural integrity 7/7, security PASS
- Commerce regression: shop JS, Stripe checkout, personalization, bulk orders link, GTM — all intact

**Bulk Orders 1291** (`bulk_orders`)
- Founder-installed in Elementor, technically verified
- Canonical JS exact match, structural integrity 7/7, security PASS
- Bulk order form byte-identical to pre-deployment state (5 fields, submission JS, return-to-shop CTA)

**About Page 33** — intentionally excluded (legacy placeholder content)

## Branch
- Branch: `tao-publication-signup`
- Starting SHA: `9f790b8`
