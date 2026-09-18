# Tao Audience — Permission Architecture

**Decision date:** September 18, 2026
**Status:** FOUNDER-APPROVED / LOCKED
**Supersedes:** the open recipient-configuration question recorded in
`TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §6 v1.1
**Related:** `DECISION_INDEX.md` → Email & Marketing → *NCB Campaign Brand* (April 2026),
`07_MARKETING/STANDARDS/TAO_PUBLICATION_SIGNUP_INFRASTRUCTURE.md`

---

## The decision

The Tao of Clinical Touch publication is delivered to **explicitly opted-in subscribers only.**

```
Learn2Tape relationship → invitation → explicit permission → List 64 → Tao publication
```

The campaign's behavior embodies the publication's thesis: **permission is asked, not assumed.**

| | |
|---|---|
| Publication destination | Brevo list **64** — by double-opt-in only |
| First invitation audience | lists **11** (Learn2Tape Users) and **65** (TAO — AMTA National 2026 Buyers) |
| Invitation sender identity | **Learn2Tape**, not Tao — per the April 2026 decision |
| NCB acquisition base (22 lists) | **Outside the Tao publication architecture**, pending results of the first invitation |
| Campaign 41 (Issue 012) | **Remains suspended.** Not resumed. |
| Automatic migration of any audience into list 64 | **Prohibited** |

## Why the NCB base is excluded

Five Tao issues (007, 008, 010, 011) were sent to 22 NCB licensed-massage-therapist acquisition
lists. Deduplicated campaign-level evidence:

| Issue | Delivered | Trackable opens | Clicks | Unsub | Complaints | Complaint % |
|---|---:|---:|---:|---:|---:|---:|
| 007 | 11,352 | 0.43% | 0.33% | 9 | 0 | 0.00% |
| 008 | 11,341 | 0.74% | 0.26% | 8 | 1 | 0.01% |
| 010 | 11,140 | 0.14% | 0.37% | 50 | 40 | **0.36%** |
| 011 | 11,056 | 0.66% | 0.28% | 8 | 0 | 0.00% |

Issue 010 breached the 0.30% industry complaint ceiling. Its complaints concentrated in
Yahoo-operated infrastructure — yahoo.com 0.84%, aol.com 1.15%, gmail.com 0.00% — 35 of 38 in the
domain partition. That is where sender reputation is lost.

By contrast, list 11 under Learn2Tape identity (campaigns 9, 10, 11, 33):

| Campaign | Delivered | Trackable opens | Complaints |
|---|---:|---:|---:|
| 9 | 816 | **7.60%** | 1 |
| 10 | 814 | **6.63%** | 0 |
| 11 | 812 | **6.40%** | 1 |
| 33 | 809 | **3.21%** | 0 |

List 11 outperforms the NCB base by roughly 5–15x on genuine opens, with effectively zero
complaints. The April 2026 decision — *"send as Learn2Tape, not Tao; the list knows Drew through
the CE relationship"* — is confirmed by the data. It also identifies where that relationship
actually lives: list 11, not the acquired NCB records.

## Recipient reconciliation — Invitation 001

Recorded as **unique recipients**, never as a sum of list memberships.

| | Unique | Blacklisted | Mailable |
|---|---:|---:|---:|
| List 11 — Learn2Tape Users | 904 | 70 | 834 |
| List 65 — TAO AMTA National 2026 Buyers | 15 | 0 | 15 |
| Sum of list memberships | 919 | — | — |
| **Verified overlap** | **0** | — | — |
| **Unique recipients** | **919** | **70** | **849** |

Overlap verified by inspecting all 15 list-65 contacts: every one carries `listIds: [65]` only.
None belongs to list 11, and none has ever received a Tao issue. Brevo also deduplicates at send;
this reconciliation does not rely on that alone.

## Infrastructure state — verified, no build required

| Component | State |
|---|---|
| Signup component `#tao-publication-signup` v1.0.0 | **live** |
| Server-side bridge `POST /wp-json/tao/v1/subscribe` | **live**, POST-only, no client-side key |
| Brevo DOI template **37** | active, `tag: "optin"`, `doiTemplate: true` |
| Confirmation page `/subscription-confirmed/` (page 1425) | **live**, HTTP 200 |
| Destination list **64** | exists; 1 confirmed contact carrying `DOUBLE_OPT-IN: "1"` |
| Per-page source tagging | working — `homepage`, `shop`, `blog_footer` |
| Analytics events | all four present |
| Placement | blog, homepage, shop. `/about/` not yet injected. |

The funnel is proven end-to-end. It required no audience it did not have; it required an invitation.

## Consequences for Issue 013 and beyond

1. Issue 013's Brevo recipient configuration is **list 64 only**.
2. List 64's size at the time of any issue send is the real readership. A small confirmed audience
   is the intended outcome, not a shortfall.
3. No issue may be sent to the NCB lists without a new, explicit Founder decision superseding this
   record.
4. Email subject and preheader for any issue remain Founder-review items.

## Open items

- Invitation 001 is **prepared, not created and not sent.** See
  `07_MARKETING/CAMPAIGNS/TAO_INVITATION_001/`.
- Brevo credit consumption remains prohibited before the September 20, 2026 plan reset.
- Whether to inject the signup component into `/about/` and the remaining Phase 3 placements.
- Whether the NCB base is ever invited, and if so staged by domain with Yahoo/AOL last.
