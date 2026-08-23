# Tao Publication Signup Infrastructure — Execution Receipt

## Status
Gate 2 PASS — Founder-approved. Live on blog template.

## Architecture

### Frontend Component
- **Source:** `tao-publication-signup.js` (v1.0.0)
- **Semantic root:** `#tao-publication-signup`
- **Source config:** `data-signup-source` attribute (currently: `blog_footer`)
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

## Supported `signup_source` Values

| Value | Context |
|---|---|
| `blog_footer` | Blog article template (live) |
| `gate1_test` | Gate 1 test page |
| `homepage` | Future — Phase 3 |
| `shop` | Future — Phase 3 |
| `about_book` | Future — Phase 3 |

## DOI Flow

1. Reader submits email → client-side validation
2. XHR POST to `/wp-json/tao/v1/subscribe`
3. Server validates, rate-limits, calls Brevo DOI endpoint
4. Brevo sends Template 37 confirmation email
5. Reader clicks "Confirm My Subscription"
6. Brevo confirms subscription, adds to List 64
7. Reader redirected to `/subscription-confirmed/`

## Contrast Correction (Founder-Approved)

Component styled for dark (navy) blog background:
- Headline: `#f5f0e8` (ivory)
- Description: `#c8cfd6` (light gray)
- Button: navy text on ivory background
- Footer: `#a0aab4`
- Border-top: `rgba(245, 240, 232, 0.25)`
- Validation error: `#e74c3c` (bright red for dark bg visibility)

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

## Branch
- Branch: `tao-publication-signup`
- Starting SHA: `9f790b8`
