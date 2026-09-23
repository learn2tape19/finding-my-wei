# Invitation 001 — Post-Send Monitoring Baseline

**Established:** 2026-09-23T09:46 ET, immediately after Campaign 42 send initiation
**Campaign:** 42 — send trigger 2026-09-23T09:45:54-04:00

---

## Primary KPI

**Confirmed attributed opt-ins** — contacts entering List 64 carrying
`SIGNUP_SOURCE = l2t_invitation`.

**Not opens.** Opens are a weak and, on this account, demonstrably unreliable signal: Issues 007
and 008 reported 48–53% open rates whose `uniqueViews` exceeded `trackable + appleMppOpens` by over
five thousand and exceeded the sum of their own per-list rows by 6–7x. Machine pre-fetch, not
readers.

## Baseline at send — a clean zero

| | |
|---|---|
| List 64 membership | **2** |
| Contacts carrying `SIGNUP_SOURCE` | **0** |
| Members | `drew@taoclinicaltouch.com` (12914), `drew@learn2tape.com` (1) |
| Both predate the attribute | yes — structurally cannot carry it |

**Every contact appearing in List 64 with `SIGNUP_SOURCE = l2t_invitation` from 09:45:54 onward is
an unambiguous Campaign 42 conversion.** No attribution ambiguity exists at this baseline.

## Funnel stages to record

```
unique mailable          849          (known)
  → delivered                          Brevo globalStats.delivered
  → trackable engagement               globalStats.trackableViews / trackableViewsRate
  → CTA visits                         GA4/GTM, signup_source = l2t_invitation
  → signup submissions                 tao_email_signup_submit, same filter
  → DOI confirmations                  tao_email_signup_success, reconciled to Brevo
  → List 64 additions                  membership delta carrying SIGNUP_SOURCE = l2t_invitation
```

## Measurement rules — binding

Per `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6 *Metric interpretation*:

- Request `statistics=globalStats` **explicitly** — the field returns zeroed otherwise.
- **Never sum per-list `campaignStats`.** Rows are attributions of the same send events, not a
  partition; summing overstated Issues 010/011 by ~1.9x.
- Report **`trackableViewsRate`**, never `opensRate`.
- `statsByDomain` is a true partition (one address, one domain) and is the correct tool for
  per-provider placement and complaint analysis.

## Deliverability watch items

Given the accepted Gmail-seed risk, monitor with particular attention:

| Metric | Threshold / note |
|---|---|
| **Complaint rate** | **0.30% is the hard ceiling.** Issue 010 breached it at 0.36% |
| Bounce rate | `mail.learn2tape.com` historical is **3.05%** — elevated |
| `statsByDomain` | compare gmail.com, yahoo.com, aol.com, hotmail.com placement and complaints |
| Unsubscribes | against 849, not against summed list rows |

A complaint rate approaching 0.30% on this send is a stop signal for any further
`mail.learn2tape.com` volume until the domain is warmed.

## No premature interpretation

Early opens and clicks are noise. Delivery and bounce figures settle within hours; engagement
takes days. **This baseline is established now precisely so that later readings are measured
against a recorded zero rather than reconstructed.** No performance conclusion is drawn at
capture time.

## Next readings

1. **Once status flips `in_process` → `sent`** — final sent, delivered, bounce counts; completes
   the send receipt.
2. **~24 hours** — delivery settled, `statsByDomain` placement view, first complaint signal.
3. **~72 hours and ~7 days** — conversion maturity; attributed opt-ins are the figure that matters.
