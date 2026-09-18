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
| Sender | **Learn2Tape identity.** ID **1** `Learn2Tape <drew@learn2tape.com>` or ID **2** `Drew Freedman \| Learn2Tape <drew@mail.learn2tape.com>` — **Founder to choose** |
| Reply-to | `drew@learn2tape.com` |
| Subject | `I've been working on something beyond technique.` |
| Preheader | `This time, I'm asking you to opt in.` |
| Recipient lists | **11** and **65** only |
| Exclusion lists | none required (overlap verified 0) |
| Unique recipients | **919** |
| Unique mailable | **849** (70 blacklisted on list 11) |
| CTA target | Tao signup with `data-signup-source="l2t_invitation"` — see below |
| `inlineImageActivation` | `false` if any image is used (external WordPress media pattern) |
| utmCampaign | `tao invitation 001` |
| Sender ID 3 (Tao) | **MUST NOT be used** |

Body copy: `INVITATION_001_APPROVED_COPY.md`, verbatim.

## CTA destination — decision required

The live signup component reads `data-signup-source` from its root, so conversion attribution
needs **no code change**. Two options:

1. **Existing placement** — point the CTA at an existing instance (blog footer, homepage). Zero
   work; attribution reports as `blog_footer` / `homepage` rather than as the invitation.
2. **Dedicated landing instance** — one page carrying
   `data-signup-source="l2t_invitation"`. Gives clean conversion measurement for this campaign
   and every future invitation. **Recommended.** This is a WordPress change and requires its own
   authorization; WordPress credentials are absent from the current execution environment.

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

### Baseline expectation

List 11 historically returns **3.2–7.6%** trackable opens under Learn2Tape identity. A plausible
outcome on 849 mailable is a low-hundreds subscriber count at best, and possibly far fewer. That
is the real size of the readership, and it is the intended result.

## Hard boundaries

- Do not rewrite the Founder-approved copy.
- Do not send to the NCB lists (`2,5,6,7,8,10,44-59`).
- Do not add anyone to list 64 directly. Double opt-in is the only path in.
- Do not resume Campaign 41.
- Do not consume Brevo credits before the September 20, 2026 reset.
