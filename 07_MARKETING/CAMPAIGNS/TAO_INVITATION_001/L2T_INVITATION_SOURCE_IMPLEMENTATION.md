# `l2t_invitation` Signup Source — Implementation Plan

**Status:** **BLOCKED — WordPress action required. Nothing was changed on WordPress.**
**Prepared:** September 18, 2026
**Authority:** `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`

Goal: give Invitation 001 a clean destination that attributes conversions to `l2t_invitation`,
reusing the already-proven signup component, bridge, and double-opt-in flow. **No component
change. No new credential path. No change to the attribution model.**

---

## Why a dedicated placement is required

The deployed component resolves its source from exactly one place — the root element attribute:

```js
CONFIG.source = root.getAttribute('data-signup-source') || CONFIG.source
```

Verified against the live v1.0.0 source: **no** `URLSearchParams`, **no** `location.search`,
**no** `utm_` handling. A `?source=l2t_invitation` link cannot work, and teaching the component to
read query parameters would be a code change to a proven component — larger and riskier than
adding one placement.

Existing placements and their sources (all verified live):

| Page | `data-signup-source` |
|---|---|
| `/` | `homepage` |
| `/shop/` | `shop` |
| blog article | `blog_footer` |
| `/about/` | component not injected |

None of these may be reused for Invitation 001.

## How the component is actually deployed

Each placement is an **Elementor HTML widget** (`data-widget_type="html.default"`) containing the
root div plus the inlined v1.0.0 script:

```html
<div id="tao-publication-signup" data-signup-source="homepage"></div>
<script> /* tao-publication-signup.js v1.0.0 … */ </script>
```

This matches doctrine: Elementor HTML belongs in the `html.default` widget, never `text-editor`,
which applies `wp_kses_post` and strips the code.

The exact deployed source is preserved at
`reference/tao-publication-signup_v1.0.0_AS_DEPLOYED.html` so the implementation needs no
re-scraping of the live site.

## The smallest implementation

**One new page. One changed attribute. Nothing else.**

1. Create a WordPress page — suggested slug **`/join/`** (alternatives: `/invitation/`,
   `/join-the-tao/`).
2. Add a single Elementor **HTML** widget.
3. Paste `reference/tao-publication-signup_v1.0.0_AS_DEPLOYED.html` verbatim.
4. Change **one attribute**:

   ```diff
   - <div id="tao-publication-signup" data-signup-source="homepage"></div>
   + <div id="tao-publication-signup" data-signup-source="l2t_invitation"></div>
   ```

5. Publish. Point the Invitation 001 CTA at that URL.

Nothing else changes. The bridge (`POST /wp-json/tao/v1/subscribe`), DOI template 37, list 64, and
`/subscription-confirmed/` are already live and proven, and the server-side secret boundary is
untouched.

## What is required to do it — and why credentials alone are not enough

| Requirement | State |
|---|---|
| `TAO_WP_USERNAME` / `TAO_WP_APP_PASSWORD` | **ABSENT** from the execution environment |
| WordPress REST reachable | yes — anonymous `Allow: GET` |
| Slug `/join/` free | **to be confirmed** at implementation time |

**Credentials would not by themselves unblock this.** Per doctrine §2, Elementor stores rendered
content in the `_elementor_data` postmeta, **not** `post_content`. A page created through
`POST /wp-json/wp/v2/pages` with `content` set would save the markup but **Elementor would not
render it**. Writing `_elementor_data` directly is possible but means hand-authoring Elementor's
internal JSON structure — fragile, and disproportionate to changing one attribute.

### Recommended path — Founder, in the Elementor UI (no credential needed)

Duplicate any existing page carrying the signup widget, change the one attribute to
`l2t_invitation`, set the slug, publish. Two minutes, uses the proven rendering path, and needs
nothing from this session.

### Alternative — non-Elementor page

A plain WordPress page using a Gutenberg **Custom HTML** block renders from `post_content` and so
*is* REST-creatable with credentials. Trade-off: it renders with theme defaults rather than the
Elementor layout, so it will not visually match the site. Acceptable for a single-purpose landing
page; a brand decision, not a technical one.

**Not authorized either way.** No WordPress mutation was attempted, and the absence of credentials
was not treated as permission to reuse an existing source.

## Verification required once implemented

1. Page returns HTTP 200.
2. Rendered HTML contains `data-signup-source="l2t_invitation"` — exactly once.
3. Component version in the placement reads `1.0.0`.
4. Page source contains **no** Brevo API key (`xkeysib-`) and no credential of any kind.
5. `tao_email_signup_view` fires with `signup_source: "l2t_invitation"`.
6. A single controlled end-to-end test submission — **requires its own authorization**, since it
   creates a Brevo contact and sends a DOI email — confirms: bridge 200 → DOI received →
   confirmation → contact lands in list 64 with `DOUBLE_OPT-IN = 1` → redirect to
   `/subscription-confirmed/`.
7. Attribution reconciles: the test appears under `l2t_invitation`, not another source.
