# Brevo V1 Adapter — Email Campaign

**Status:** CURRENT AUTHORITY — verified against live production September 13, 2026
**Parent doctrine:** `04_CAPABILITIES/PUBLISHING/TAO_PUBLISHING_EXECUTION_DOCTRINE.md`

---

## Account and sender identity

| Property | Value |
|---|---|
| Account | drew@learn2tape.com |
| Organization | `69e660956a08aaef49055093` |
| Plan | Starter — Marketing, paid, active |
| Sender | ID **3** — "Drew Freedman \| Tao of Clinical Touch" <drew@mail.taoclinicaltouch.com> |
| Reply-to | drew@learn2tape.com |

Sender ID and recipient lists must be asserted against the approved issue plan before scheduling.
A mismatch is a STOP condition.

**Recipient configuration is an open Founder decision.** List 64's actual Brevo name is
"Tao subscriber list", and it holds 1 subscriber with no campaign history. Every Tao issue send to
date used 22 NCB acquisition lists `[2,5,6,7,8,10,44-59]`, which is historical behavior rather
than established intent. See `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6 for the verified state and
the conflicting Founder records. Do not assert a recipient set until the Founder resolves it.

---

## External-media architecture — the core finding

**Brevo delivers externally hosted WordPress HTTPS media directly. No Brevo image-library upload
is required.**

Campaign HTML may reference the Founder-approved WordPress-hosted master by public URL:

```html
<img src="https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE0XX_..._1200x628.png"
     alt="..." width="600"
     style="display:block; width:100%; height:auto;" />
```

Set `inlineImageActivation: false`. Brevo then stores and delivers the raw external URL without
proxying, rewriting, or inlining it.

### Precedent

Campaign **36** (Issue 008, status `sent`, 2026-08-26) used exactly this pattern.
Result: **11,341 delivered**, 11,467 sent, 13 hard bounces, 1 complaint.

The delivery figure is the evidence. Campaign 36's reported 53.28% open rate is **not** an
engagement benchmark — its `uniqueViews` exceed `trackable + appleMppOpens` by 5,597 and exceed
the sum of its own per-list rows by 7x. Use `trackableViewsRate` (0.74% here). Never sum per-list
`campaignStats`; request `statistics=globalStats` explicitly for deduplicated figures. See
`TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6 *Metric interpretation*.

This retires the former belief that a Brevo image-upload capability was required for Tao email
execution. It was not, and is not.

### Asset eligibility

The referenced URL must first pass the checksum rule:

```
canonical repository SHA-256  ==  anonymously retrieved SHA-256
```

and must return HTTP 200 anonymously — no auth header, no `Referer`. Verify before composing.

---

## Reusable-master doctrine

### Template 39 is not presently a neutral master

Template 39, currently named **"Tao — Weekly Issue Master"**, is **not** a reusable shell. It
holds Issue 011-specific content end to end:

- subject line specific to Issue 011
- `ISSUE 011 · RESPONSE` eyebrow
- the full Issue 011 body
- a CTA hard-linked to that issue's canonical article

It is a copy of Issue 011 that carries the word "Master" in its name. Editing it in place would
also mutate the object Issue 011's queued campaign was built from.

**Do not modify template 39. Do not delete it. Do not treat it as a shell.**

### Current doctrine

- Stable Tao branding and layout **may** form a neutral master.
- Issue-specific editorial content belongs in the **issue campaign object**, composed from the
  approved issue copy — never baked into the master.
- The issue-specific CTA **must** resolve to that issue's canonical WordPress article URL. That
  URL must exist before the campaign is composed.
- Compatible email imagery **may reference the approved WordPress-hosted 1200×628 Landscape
  master directly**.
- **A separate Brevo image-library upload is not required** when external HTTPS media is used.

### Controlled-mutation boundary

Creating a neutral reusable master is a **controlled Brevo mutation** requiring its own explicit
authorization. Documentation of this doctrine does not authorize it.

---

## Required execution sequence

Brevo runs **last**, only after the canonical WordPress article URL exists.

1. **Authenticate** — account read returns the expected organization.
2. **Verify send eligibility** — see the billing dependency below.
3. **Duplicate-check** — confirm no campaign already exists for the issue.
4. **Compose** the issue-specific campaign from approved copy and structure.
5. **Verify before scheduling:**
   - sender ID and reply-to
   - recipient lists and any exclusions
   - subject line and preheader against approved copy
   - CTA target resolves to the issue's canonical article
   - image URL anonymously retrievable and checksum-verified
   - scheduled timestamp matches the approved publishing schedule, with correct timezone offset
6. **Read the campaign back** and reconcile every field above.

A mutation response is not proof of queued state.

---

## Subscription and send-credit eligibility — manual dependency

The Brevo account endpoint exposes the **current plan period only**. It carries **no**
`autoRenew`, `renewalDate`, `nextBillingDate`, or `cancelAtPeriodEnd` field. The API therefore
**cannot** distinguish automatic renewal from lapse.

Plan period on record: **2026-08-20 → 2026-09-20 17:31 UTC** (13:31 ET).

When an issue's email falls after a plan boundary, a **Founder or manual billing check is
required** before scheduling: Brevo → Billing → My Plan → confirm renewal and replenished send
credits.

This is a **billing dependency, not a technical infrastructure failure.** Do not classify it as
one, and do not change the subscription programmatically.

---

## Platform notes

- Double opt-in templates used with `POST /v3/contacts/doubleOptinConfirmation` must carry the
  `optin` tag in Advanced Settings. Without it the API returns "An active DOI template does not
  exist" even when `isActive: true`. The MCP `doiTemplate` flag is client-side inference from
  content, not server-side eligibility.
- The tag feature is not available on the current plan.
- DOI template: ID 37; redirect `https://taoclinicaltouch.com/subscription-confirmed/`.
- The Brevo secret boundary for server-side subscribe is `TAO_BREVO_API_KEY` in `wp-config.php`
  (`xkeysib-` format). A JWT-form key is not a v3 REST key.

---

## STOP conditions specific to this adapter

- Authentication failure
- Sender ID or recipient-list mismatch against the approved plan
- CTA target does not resolve to the issue's canonical article
- Image URL not anonymously retrievable, or failing checksum reconciliation
- Scheduled timestamp or timezone mismatch
- Duplicate campaign for the issue
- Unresolved subscription or send-credit eligibility
- Any requirement to modify Founder-approved copy

---

## Revision history

- **v1.0 — September 13, 2026** — Established from live verification. Records external-media
  architecture, template 39 status, and the manual billing dependency.
