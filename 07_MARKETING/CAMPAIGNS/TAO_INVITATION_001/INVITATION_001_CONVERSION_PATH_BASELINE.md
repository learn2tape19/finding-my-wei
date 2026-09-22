# Invitation 001 — Conversion-Path Baseline

**Status:** **LOCKED AND VERIFIED**
**Recorded:** September 22, 2026
**Authority:** `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`

The verified end-to-end state of the path Invitation 001 traffic will follow. Every value below is
an observed live response, cache-busted (`cf-cache-status: DYNAMIC`), not an inference.

---

## 1. Destination — `/join/`

| Property | Value |
|---|---|
| URL | `https://taoclinicaltouch.com/join/` |
| WordPress page | **1644**, `status: publish` |
| Last modified | 2026-09-22T19:15:49-04:00 |
| HTTP | 200 |
| Attribution source | `data-signup-source="l2t_invitation"` |
| Component version | **1.0.0** |
| Component bytes | 10,939 |
| Component SHA-256 | `e96b13de6cd122541335a83e1a194154a0aee913243abfd2b458102143bb1483` |
| **Functional-surface hash** | **`71dcd2dab122b6b03ecc79c2fb205f2e`** |

## 2. Approved post-submission copy — live

> **One more step.**
>
> Check your inbox and confirm your subscription to *The Tao of Clinical Touch*. Once confirmed,
> the next issue will come to you directly.

Deployed literals:

```js
resultBox.innerHTML =
  '<p class="tao-signup-success-headline">One more step.</p>' +
  '<p>Check your inbox and confirm your subscription to <em>The Tao of Clinical Touch</em>. Once confirmed, the next issue will come to you directly.</p>';
```

The superseded copy — "One more step" / "The next issue … will come to you directly" — announced
completion and never referenced the confirmation email. Because a double-opt-in subscriber is not
subscribed until they click, that wording suppressed the exact step the funnel measures. It is
gone from `/join/`.

## 3. Functional surface — unchanged by the copy correction

Verified after deployment:

| Check | Result |
|---|---|
| Functional-surface hash | **`71dcd2dab122b6b03ecc79c2fb205f2e`** — unchanged |
| Diff vs pre-edit | exactly **2 lines out, 2 lines in** — the authorized literals only |
| `data-signup-source` | `l2t_invitation` |
| Endpoint | `/wp-json/tao/v1/subscribe` |
| Form, email input, CTA label | unchanged |
| Success-panel class | `tao-result-success` — unchanged |
| Analytics events | all four present |
| Email in `dataLayer` payload | none |
| Credentials client-side | none |

## 4. The verified path

```
Invitation 001  (sender ID 2 — Drew Freedman | Learn2Tape)
  → /join/            data-signup-source="l2t_invitation"
  → POST /wp-json/tao/v1/subscribe     build:gate-c-v1, server-side allowlist
  → Brevo DOI template 37              "Confirm My Subscription"
  → confirmation
  → List 64            SIGNUP_SOURCE = l2t_invitation, DOUBLE_OPT-IN = 1
  → /subscription-confirmed/           page 1425, HTTP 200
```

Every hop proven in production: attribution write and no-overwrite guard at Gate C
(`GATE_C_ATTRIBUTION_EVIDENCE.md`), destination and copy here.

## 5. Measurement baseline at lock

| | |
|---|---|
| List 64 membership | **2** |
| Contacts carrying `SIGNUP_SOURCE` | **0** |
| Members | `drew@taoclinicaltouch.com` (12914), `drew@learn2tape.com` (1) — both predate the attribute |
| Gate B/C test artifacts | deleted (12915, 12916) |

**Any List 64 contact carrying `SIGNUP_SOURCE = l2t_invitation` from this point forward is an
Invitation 001 conversion.** The baseline is a clean zero; the two existing members are
structurally excluded because they cannot carry the attribute.

## 6. Funnel stages to record

```
unique mailable (849)
  → delivered
  → trackable engagement
  → CTA visits
  → signup submissions
  → DOI confirmations
  → List 64 additions carrying SIGNUP_SOURCE = l2t_invitation
```

Per `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6: request `statistics=globalStats` explicitly, never
sum per-list `campaignStats`, report `trackableViewsRate` rather than `opensRate`. No conversion
figure is forecast; this campaign exists to establish the real one.

## 7. Scope note

This correction was applied to **`/join/` only**, per Founder authorization. The other five
placements — `/`, `/shop/`, `/book/`, `/bulk-orders/`, `/signup-test/` — retain the earlier
"You're in." copy. They are outside the Invitation 001 conversion path. Aligning them is optional
future work and has no bearing on this campaign's measurement.
