# Invitation 001 — Brevo Campaign Object QA

**Campaign ID:** **42**
**Status:** **DRAFT — not scheduled, not sent**
**Created:** 2026-09-22T15:28:26-04:00
**QA result:** **PASS**

Read-only verification of the live Brevo object. Every value below was read back from the API
after creation, not assumed from the create call.

---

## Configuration

| Field | Value | Result |
|---|---|---|
| Campaign ID | 42 | — |
| Name | `Tao Invitation 001 — Join The Tao of Clinical Touch` | PASS |
| Status | **`draft`** | PASS |
| `scheduledAt` | **empty** — not scheduled | PASS |
| `sent` | **0** | PASS |
| Sender | ID **2**, `drew@mail.learn2tape.com` — Learn2Tape identity | PASS |
| Sender ID 3 (Tao) used | **NO** | PASS |
| Reply-to | `drew@learn2tape.com` | PASS |
| Subject | `An invitation to stay in the conversation` | PASS — verbatim |
| Preheader | `The Tao of Clinical Touch is becoming an ongoing publication. You're invited to join it.` | PASS — verbatim |
| Recipient lists | **`[11, 65]`** | PASS |
| Exclusion lists / segments | none | PASS |
| **NCB lists `[2,5,6,7,8,10,44-59]`** | **absent** | PASS |
| `remaining` (Brevo's own recipient count) | **849** | PASS — matches the reconciled mailable figure exactly |
| `inlineImageActivation` | `false` | PASS |
| `mirrorActive` | `true` | PASS |
| `abTesting` | `false` | PASS |
| `sendAtBestTime` | `false` | PASS |
| utmCampaign | `tao invitation 001` | PASS |

**Independent confirmation of the audience:** Brevo computed `remaining: 849` from lists 11 + 65
on its own. That matches the reconciliation recorded on September 18 — 919 unique memberships,
70 blacklisted, **849 mailable** — derived independently. Two methods, same number.

## Body copy — 13/13 verbatim

Stored `htmlContent` read back from the object is byte-identical to what was submitted. All
Founder-approved lines present verbatim, in order:

1. I've been working on something beyond technique.
2. For years, Learn2Tape has been about giving clinicians practical tools they can bring into the treatment room.
3. Over time, another question kept getting louder:
4. What happens before technique ever gets a chance to work?
5. That question became The Tao of Clinical Touch—first the book, and now an ongoing publication exploring permission, safety, and the clinical relationship.
6. You may have seen a few of these essays from me already. That was me getting ahead of myself.
7. I don't want to assume that because you know my work through Learn2Tape, you want another publication in your inbox.
8. So this time, I'm asking.
9. If this is a conversation that belongs in your practice, I'd like to invite you into it.
10. JOIN THE TAO OF CLINICAL TOUCH *(CTA)*
11. New essays and clinical reflections. No noise. Unsubscribe anytime. *(under CTA)*
12. No automatic migration.
13. Just an invitation.

No paraphrase, no reordering, no additions to the approved text. The `<em>` treatment on the
publication name is preserved.

## CTA and compliance

| Check | Result |
|---|---|
| CTA destination | `https://taoclinicaltouch.com/join/` | 
| CTA occurrences | exactly **1** | PASS |
| CTA carries `l2t_invitation` attribution | PASS — via the destination page's `data-signup-source` |
| Unsubscribe token | `{{ unsubscribe }}` present and linked | PASS |
| Brevo footer | `EXISTS` | PASS |
| Mirror / view-in-browser | enabled | PASS |
| Tracking | Brevo default open/click tracking; `utmCampaign` set | PASS |
| Images | none — no external media dependency, no checksum gate | PASS |
| Recipient-identifying data in markup | none | PASS |

## Sender-name field note

`sender.name` reads `[DEFAULT_FROM_NAME]` on the stored object. This is Brevo's placeholder for a
name resolved from the sender ID at send time; Campaign 41 showed the same and it was verified
benign during Issue 012. Sender **ID 2** and address `drew@mail.learn2tape.com` are stored
correctly, which is what determines the from-identity.

## Not done

Not scheduled. Not sent. No test send. `scheduledAt` is empty and `status` is `draft`.
Scheduling and sending each require separate Founder authorization.
