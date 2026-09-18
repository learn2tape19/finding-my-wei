# Tao Invitation 001 — Campaign Spec

**Status:** **PREPARED — NOT CREATED, NOT SCHEDULED, NOT SENT**
**Prepared:** September 18, 2026
**Authority:** `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`

No Brevo object exists for this campaign. Nothing has been created in any platform.

---

## Configuration — ready to submit unchanged

| Field | Value |
|---|---|
| Campaign name | `Tao Invitation 001 — Join The Tao of Clinical Touch` |
| Sender | **ID 2 — `Drew Freedman \| Learn2Tape <drew@mail.learn2tape.com>`** — Founder-locked |
| Reply-to | `drew@learn2tape.com` |
| Subject | `I've been working on something beyond technique.` |
| Preheader | `This time, I'm asking you to opt in.` |
| Recipient lists | **11** and **65** only |
| Exclusion lists | none required (overlap verified 0) |
| Unique recipients | **919** |
| Unique mailable | **849** (70 blacklisted on list 11) |
| CTA target | Tao signup carrying `data-signup-source="l2t_invitation"` — **Founder-locked**, see below |
| `inlineImageActivation` | `false` if any image is used (external WordPress media pattern) |
| utmCampaign | `tao invitation 001` |
| Sender ID 3 (Tao) | **MUST NOT be used** |

Body copy: `INVITATION_001_APPROVED_COPY.md`, verbatim.

## CTA destination — Founder-locked

Invitation 001 **must** attribute to the dedicated source `l2t_invitation`. Attributing these
conversions to `blog_footer`, `homepage`, `shop`, or any other existing source is prohibited.

Required flow:

```
Invitation 001 CTA
  → Tao signup instance with data-signup-source="l2t_invitation"
  → POST /wp-json/tao/v1/subscribe   (server-side; no client-side credential)
  → Brevo DOI template 37
  → confirmation → List 64
  → /subscription-confirmed/
```

The live component resolves its source **only** from the root element attribute:

```js
CONFIG.source = root.getAttribute('data-signup-source') || CONFIG.source
```

Verified: the component has **no** query-parameter support — no `URLSearchParams`, no
`location.search`, no `utm_` handling. A `?source=` link therefore cannot produce
`l2t_invitation`, and adding that capability would be a component change, not the smallest path.
**A dedicated placement is required.** See `L2T_INVITATION_SOURCE_IMPLEMENTATION.md`.

Status: **BLOCKED — WordPress action required.** The attribution model must not be changed to
work around it.

## Execution order when authorized

1. Confirm Brevo plan reset after **2026-09-20** and replenished send credits.
2. Confirm sender identity choice (ID 1 or ID 2).
3. Confirm CTA destination (option 1 or 2).
4. Duplicate-check: no existing `Tao Invitation` campaign in the account.
5. Create the campaign from the approved copy; attach lists 11 and 65.
6. Independently read the campaign back by ID and reconcile: sender, reply-to, subject,
   preheader, recipient lists, scheduled timestamp, CTA target.
7. **Record the unique recipient count, never the sum of list memberships.**
8. Write the execution receipt.

## Reporting requirements

Per the metric-interpretation rule in `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6:

- Request `statistics=globalStats` explicitly. Without it the field returns zeroed.
- **Never sum per-list `campaignStats`.** Rows are attributions, not a partition.
- Report `trackableViewsRate`, not `opensRate`.
- The success metric for this campaign is **confirmed opt-ins landing in list 64** — not opens.

### Funnel baseline — establish, do not forecast

Invitation 001 exists to produce the **first real measurement** of this funnel. No subscriber
conversion figure is a production KPI, and none is predicted here. Record each stage as observed:

| Stage | Source of truth |
|---|---|
| Unique mailable | this spec — 849 |
| Delivered | Brevo `globalStats.delivered` (request `statistics=globalStats` explicitly) |
| Trackable engagement | Brevo `globalStats.trackableViews` / `trackableViewsRate` |
| CTA visits | GA4 / GTM — `tao_email_signup_view` where `signup_source = l2t_invitation` |
| Signup submissions | `tao_email_signup_submit` where `signup_source = l2t_invitation` |
| DOI confirmations | `tao_email_signup_success`, reconciled against Brevo |
| List 64 additions | Brevo list 64 membership delta, contacts carrying `DOUBLE_OPT-IN = 1` |

Report the measured funnel. Do not annotate it against a target that does not exist.

## Hard boundaries

- Do not rewrite the Founder-approved copy.
- Do not send to the NCB lists (`2,5,6,7,8,10,44-59`).
- Do not add anyone to list 64 directly. Double opt-in is the only path in.
- Do not resume Campaign 41.
- Do not consume Brevo credits before the September 20, 2026 reset.
- Do not create, schedule, or send this campaign. Creation requires its own explicit
  Founder authorization in a later gate.
- Do not email, invite, migrate, or otherwise act on the NCB acquisition lists during this gate.
- Do not attribute Invitation 001 conversions to any source other than `l2t_invitation`.
- Do not expose a Brevo API credential client-side. The server-side boundary
  (`TAO_BREVO_API_KEY` in `wp-config.php`) is preserved as-is.
