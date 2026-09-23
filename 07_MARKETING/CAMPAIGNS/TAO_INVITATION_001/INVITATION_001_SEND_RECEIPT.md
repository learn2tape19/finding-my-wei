# Invitation 001 — Send Receipt

**Campaign ID:** **42**
**Send initiated:** **2026-09-23T09:45:54-04:00**
**Status at receipt capture (09:46 ET):** **`in_process`** — sending in flight
**Authority:** Founder SEND authorization, September 23, 2026

---

## Send configuration as executed

Read back from the live Brevo object after send initiation.

| Field | Value |
|---|---|
| Campaign ID | **42** |
| Name | `Tao Invitation 001 — Join The Tao of Clinical Touch` |
| Status | **`in_process`** |
| Send trigger (`scheduledAt`) | **2026-09-23T09:45:54-04:00** |
| Last modified | 2026-09-23T09:45:33-04:00 |
| Sender | ID **2** — `drew@mail.learn2tape.com` — Drew Freedman \| Learn2Tape |
| Reply-to | `drew@learn2tape.com` |
| Subject | `An invitation to stay in the conversation` |
| Preheader | `The Tao of Clinical Touch is becoming an ongoing publication. You're invited to join it.` |
| Recipient lists | **`[11, 65]`** — no exclusions, no segments |
| NCB lists | **absent** |
| Audience at send | **849 mailable** (919 unique memberships, 70 blacklisted) |
| `remaining` post-initiation | **0** — queue drained into sending |
| CTA | `https://taoclinicaltouch.com/join/` — registered in `linksStats` |
| Body | 13/13 Founder-approved lines, verbatim |
| `inlineImageActivation` | false |
| `mirrorActive` | true |
| utmCampaign | `tao invitation 001` |

## Pre-send verification — PASS

Completed immediately before send:

- Campaign 42 `draft`, unscheduled, `sent: 0`
- Sender, reply-to, subject, preheader, recipients, CTA, body all matching the locked package
- `/join/` HTTP 200, component SHA-256 `e96b13de6cd122541335a83e1a194154a0aee913243abfd2b458102143bb1483` — identical to the locked conversion-path baseline
- `data-signup-source="l2t_invitation"` intact
- Repository at parity, `76f775a`, clean tree

## Authentication — verified PASS

From Campaign 42 test-message headers, September 23, 2026:

| | |
|---|---|
| SPF | **PASS** |
| DKIM | **PASS** — signed by `mail.learn2tape.com` |
| DMARC | **PASS** |

## Known accepted risk

The Gmail/Workspace seed test landed in Junk. **Founder accepted this risk explicitly** and authorized
send, with performance to be evaluated post-launch. The standing hypothesis is sender-domain
reputation on `mail.learn2tape.com` — 6,272 lifetime sends, 10 of 11 campaigns cold outreach to
acquired NCB lists, 3.05% bounce rate, dormant since 2026-07-23 — not authentication, which is
verified passing.

**No remediation by sender migration.** Per doctrine §6 v1.3, deliverability pressure on the
Learn2Tape identity is never grounds for borrowing the Tao domain's reputation.

## Sending-identity compliance

| | |
|---|---|
| Sent from | `mail.learn2tape.com` (sender 2) — **correct** for a Learn2Tape-originated invitation |
| Audience | Learn2Tape relationship, lists 11 + 65 — **correct** |
| Tao sender used | **NO** |
| NCB audience touched | **NO** |
| Campaign 41 | untouched, remains suspended |

## Outstanding at receipt capture

Status is `in_process`; `sent`, `delivered`, and bounce figures are not yet populated. **Final
counts require a follow-up read once status flips to `sent`.** This receipt records send
initiation, not completed delivery.
