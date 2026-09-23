# Invitation 001 — Readiness Package

**Status:** **SENT — Campaign 42, 2026-09-23T09:45:54-04:00.**
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
| Subject | `An invitation to stay in the conversation` | **LOCKED** — Founder-approved 2026-09-22, supersedes prior value |
| Preheader | `The Tao of Clinical Touch is becoming an ongoing publication. You're invited to join it.` | **LOCKED** — Founder-approved 2026-09-22, supersedes prior value |
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
| `l2t_invitation` destination | **READY** — `/join/` live (page 1644), source verified |
| `SIGNUP_SOURCE` attribution | **READY** — Gate C closed, see `GATE_C_ATTRIBUTION_EVIDENCE.md` |
| Conversion-path copy + baseline | **READY** — locked, see `INVITATION_001_CONVERSION_PATH_BASELINE.md` |
| Brevo send credits | **BLOCKED** — 5,754 credits, plan period ends 2026-09-20; consumption prohibited before reset |
| Campaign creation | **DONE** — Brevo campaign **42**, QA PASS |
| **Send** | **EXECUTED 2026-09-23T09:45:54-04:00** — see `INVITATION_001_SEND_RECEIPT.md` |
| Monitoring baseline | **ESTABLISHED** — see `INVITATION_001_MONITORING_BASELINE.md` |

## Blockers

1. ~~**`l2t_invitation` destination does not exist.**~~ **RESOLVED.** `/join/` published as page
   1644 carrying `data-signup-source="l2t_invitation"`, verified live.

2. ~~**Brevo plan reset.**~~ **RESOLVED.** The 2026-09-20 boundary has passed. 849 mailable sits
   far below available credits; credits are not a volume constraint for this campaign.

3. ~~**Attribution does not persist to Brevo.**~~ **RESOLVED at Gate C**, September 22, 2026.
   Confirmed opt-ins now carry `SIGNUP_SOURCE`, and existing provenance cannot be overwritten.
   Full evidence in `GATE_C_ATTRIBUTION_EVIDENCE.md`.

### Outstanding before release

- **Test-artifact cleanup.** Contacts 12915 and 12916 are Gate B/C test records inside List 64 and
  will otherwise inflate the Invitation 001 baseline. Deletion is manual — this session's Brevo
  connector has no contact-delete capability. Target post-cleanup List 64 baseline: **2**.
- ~~**`/join/` post-submit copy.**~~ **RESOLVED** September 22, 2026. The success panel now reads
  "One more step. / Check your inbox and confirm your subscription to *The Tao of Clinical Touch*.
  Once confirmed, the next issue will come to you directly." Verified live with the functional
  surface unchanged. See `INVITATION_001_CONVERSION_PATH_BASELINE.md`.

## Deliverability — Campaign 42

**Authentication: VERIFIED PASS.** Headers from the Campaign 42 test message, read
September 23, 2026:

| | Result |
|---|---|
| SPF | **PASS** |
| DKIM | **PASS** — signed by `mail.learn2tape.com` |
| DMARC | **PASS** |

Authentication is closed as a hypothesis. No DNS, SPF, DKIM, DMARC or sender change is to be made
in response to placement outcomes.

**Open:** the first Workspace test landed in Junk. Remaining hypotheses, in order of evidential
support:

1. **Sender-domain reputation** on `mail.learn2tape.com` — 11 sent campaigns totalling 6,272
   messages, 10 of them cold outreach to acquired NCB lists; 3.05% bounce rate; 0.213% complaint
   rate; dormant since 2026-07-23. Contrast `mail.taoclinicaltouch.com`: 133,947 sent, 1.68%
   bounce, 0.070% complaints, weekly cadence.
2. **Cross-domain link pattern** — sent from `learn2tape.com`, single link to `taoclinicaltouch.com`,
   no aligned links. Every successful Tao send was self-aligned.
3. **Mailbox-specific filtering** — first contact from this subdomain to that tenant.

**Pending:** Founder-run seed tests to Gmail, Outlook and Yahoo via the Brevo UI. Three providers
distinguish systemic placement failure from single-mailbox filtering. This session has no campaign
test-send capability, so the seeds must be sent manually.

Campaign 42 is **HELD** pending those results. It is not cleared for launch on the evidence
available.

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

**Gate D — Invitation 001 campaign creation.**

Prerequisites now satisfied: copy locked, sender locked (ID 2), audience reconciled (919 unique /
849 mailable, overlap 0), destination live, attribution proven, plan boundary passed.

Remaining before Gate D opens: test-artifact cleanup, and Founder authorization to create the
campaign object. Sending remains a separate authorization after creation.
