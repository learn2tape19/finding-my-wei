# Invitation 001 — Readiness Package

**Status:** **PREPARED. NOT CREATED. NOT SCHEDULED. NOT SENT.**
**Gate date:** September 18, 2026
**Authority:** `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`

No Brevo object exists for this campaign. No credits consumed. No WordPress mutation performed.
Campaign 41 untouched and still suspended.

---

## Founder-locked configuration

| Item | Value | State |
|---|---|---|
| Sender | **ID 2** — `Drew Freedman \| Learn2Tape <drew@mail.learn2tape.com>` | **LOCKED** |
| Reply-to | `drew@learn2tape.com` | LOCKED |
| Subject | `I've been working on something beyond technique.` | LOCKED — verbatim |
| Preheader | `This time, I'm asking you to opt in.` | LOCKED — verbatim |
| Body copy | `INVITATION_001_APPROVED_COPY.md` | LOCKED — 13/13 lines verified verbatim |
| Audience | lists **11** + **65** only | LOCKED |
| Unique recipients | **919** | verified |
| Blacklisted | **70** | verified |
| Unique mailable | **849** | verified |
| List 11 ∩ List 65 | **0** — all 15 list-65 contacts carry `listIds: [65]` only | verified |
| Attribution source | `l2t_invitation` | LOCKED |
| NCB lists `[2,5,6,7,8,10,44-59]` | **EXCLUDED** from Invitation 001 and from the canonical Tao publication audience | LOCKED |
| Sender ID 3 (Tao) | must **not** be used for this campaign | LOCKED |

Recipient counts are recorded as **deduplicated unique / mailable**, never as summed per-list
membership.

## Readiness by component

| Component | Status |
|---|---|
| Approved copy, subject, preheader | **READY** |
| Sender identity | **READY** — ID 2 locked |
| Audience + dedup reconciliation | **READY** — 919 / 849, overlap 0 |
| Signup component v1.0.0 | **READY** — live and proven |
| Server bridge `POST /wp-json/tao/v1/subscribe` | **READY** — live, POST-only, no client-side credential |
| Brevo DOI template **37** | **READY** — active, `tag: "optin"`, `doiTemplate: true` |
| Destination list **64** | **READY** — DOI flow proven end to end (`DOUBLE_OPT-IN = 1`) |
| Confirmation page `/subscription-confirmed/` | **READY** — page 1425, HTTP 200 |
| Analytics events | **READY** — all four present, PII-free |
| `l2t_invitation` destination | **BLOCKED** — see `L2T_INVITATION_SOURCE_IMPLEMENTATION.md` |
| Brevo send credits | **BLOCKED** — 5,754 credits, plan period ends 2026-09-20; consumption prohibited before reset |
| Campaign creation | **NOT AUTHORIZED** in this gate |

## Blockers

1. **`l2t_invitation` destination does not exist.** The component reads its source only from
   `data-signup-source` on the root element; it has no query-parameter support. One new placement
   is required. Credentials alone do not unblock it — Elementor renders from `_elementor_data`,
   not `post_content`, so REST page creation would not render. Recommended path: Founder creates
   the page in the Elementor UI, pastes the preserved v1.0.0 source, changes one attribute.
   Full plan and verification checklist in `L2T_INVITATION_SOURCE_IMPLEMENTATION.md`.

2. **Brevo plan reset.** Confirm renewal and replenished credits after **2026-09-20**. 849
   mailable is far below the 5,754 remaining, so credits are not a volume constraint for this
   campaign — but the Founder prohibition on consumption before the reset stands regardless.

Neither blocker may be worked around. In particular, the absence of WordPress credentials is not
permission to attribute Invitation 001 to an existing source.

## Funnel baseline — to be established, not forecast

Invitation 001 produces the first real measurement of this funnel. **No subscriber conversion
figure is a production KPI and none is predicted.** Record as observed:

```
unique mailable (849)
  → delivered
  → trackable engagement
  → CTA visits
  → signup submissions
  → DOI confirmations
  → List 64 additions
```

Measurement rules, per `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6 *Metric interpretation*:

- Request `statistics=globalStats` **explicitly**; it returns zeroed otherwise.
- **Never** sum per-list `campaignStats` — rows are attributions, not a partition.
- Report `trackableViewsRate`, never `opensRate`.
- Segment analytics by `signup_source = l2t_invitation`.

## Downstream consequence

Issue 013 and subsequent Tao publication emails address **confirmed List 64 subscribers only**,
unless a later Founder decision changes the architecture. List 64's membership at send time is the
readership.

## Next production gate required

**Gate A — `l2t_invitation` destination implementation and verification.**

Founder creates the placement (or authorizes a credentialed path), then the seven verification
steps in `L2T_INVITATION_SOURCE_IMPLEMENTATION.md` are executed, including a single controlled
end-to-end test submission — which needs its own authorization, since it creates a Brevo contact
and sends a DOI email.

Only after Gate A closes, and after the September 20 plan reset is confirmed, may a later gate
authorize **creation** of the Invitation 001 campaign object. Sending remains a separate
authorization after that.
