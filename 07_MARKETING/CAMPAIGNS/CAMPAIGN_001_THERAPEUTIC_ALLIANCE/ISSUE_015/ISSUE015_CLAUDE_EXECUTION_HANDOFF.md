# Issue 015 — Claude Production Execution Handoff

**Issue:** 015 — RESTRAINT / The Clinical Practice of Restraint  
**Founder authorization:** APPROVED for Buffer execution, October 6, 2026  
**Execution mode:** **PRODUCTION ONLY / NO CREATIVE DISCRETION**  
**Publication week:** October 12–16, 2026  
**Canonical article:** https://taoclinicaltouch.com/blog/2026/10/the-clinical-practice-of-restraint/  
**WordPress post ID:** 1877  
**WordPress state verified by authenticated read:** `future`, scheduled October 12, 2026; article body matches Founder-approved canonical manuscript; featured media ID 1870.

## Claude directive

Execute Issue 015 through the established Tao production control plane. Do not rewrite, regenerate, crop, substitute, rename, or creatively reinterpret copy or assets. Use the Issue 014 deployment as the immediate production precedent and the current Buffer V1 GraphQL adapter as technical authority.

**Sequence:** preflight → Buffer duplicate check → Buffer creation → independent Buffer readback/reconciliation → write machine-readable Buffer receipt → Brevo preflight/build → independent Brevo readback → final reconciliation receipt.

Do not claim completion from mutation responses. Each production object must be independently read back.

## Canonical sources

1. `ISSUE015_CANONICAL_ARTICLE_DRAFT.md` — article source of truth.
2. `ISSUE015_FIVE_DAY_COPY_AND_VISUAL_DIRECTION.md` — Founder-approved campaign copy and roles.
3. WordPress media URLs below — live production media.
4. `04_CAPABILITIES/PUBLISHING/control_plane/adapters/BUFFER_V1_ADAPTER.md` — Buffer technical authority.
5. `ISSUE014_BUFFER_DEPLOYMENT_RECEIPT.md` and `ISSUE014_BUFFER_OBJECTS.json` — immediate prior production architecture and scheduling precedent.

## Buffer architecture to reproduce

Target: **25 content items / 45 channel deliveries**, matching Issue 014 unless a newer Founder-approved distribution directive exists.

- 5 Feed items → Instagram — The Tao of Clinical Touch + Instagram — drewdog19 = 10 deliveries.
- 5 Landscape items → Facebook — The Tao of Clinical Touch = 5 deliveries.
- 15 Story items → both Instagram accounts = 30 deliveries.
- Facebook Stories = 0.
- Feed + Landscape: 8:00 AM ET.
- Story 1: 9:00 AM ET.
- Story 2: 11:00 AM ET.
- Story 3: 1:00 PM ET.
- Story 3 carries the native Story link to the canonical article.
- Facebook Landscape captions carry the canonical article URL.
- Instagram Feed captions use “link in bio”; do not put the raw URL in Instagram body copy.
- Story objects carry no caption.

**IMPORTANT GOVERNANCE CHECK:** the older Buffer adapter contains a warning against Tao publishing to `drewdog19`, while the later Issue 014 Founder-approved production receipt explicitly deployed all 20 Instagram roles to both `taoclinicaltouch` and `drewdog19`. Treat Issue 014 as the immediate production precedent for Issue 015. If repository governance has a still-newer explicit Founder directive that supersedes Issue 014, STOP before mutation and report the conflict. Do not silently choose.

## Buffer channel IDs from current production registry

- Tao Facebook: `6a3eb95f5ab6d2f106763fc9`
- Tao Instagram: `6a3eb89f5ab6d2f106763ca0`
- Instagram drewdog19: `6a3eba3f5ab6d2f106764339`

Resolve all three live before scheduling. Required state: `isDisconnected:false`, `isLocked:false`.

## Schedule

Issue 015 falls during EDT (UTC−4).

| Date | Feed + Landscape | Story 1 | Story 2 | Story 3 |
|---|---|---|---|---|
| Mon Oct 12 | 8:00 AM ET / 12:00Z | 9:00 / 13:00Z | 11:00 / 15:00Z | 1:00 PM / 17:00Z |
| Tue Oct 13 | 8:00 AM ET / 12:00Z | 9:00 / 13:00Z | 11:00 / 15:00Z | 1:00 PM / 17:00Z |
| Wed Oct 14 | 8:00 AM ET / 12:00Z | 9:00 / 13:00Z | 11:00 / 15:00Z | 1:00 PM / 17:00Z |
| Thu Oct 15 | 8:00 AM ET / 12:00Z | 9:00 / 13:00Z | 11:00 / 15:00Z | 1:00 PM / 17:00Z |
| Fri Oct 16 | 8:00 AM ET / 12:00Z | 9:00 / 13:00Z | 11:00 / 15:00Z | 1:00 PM / 17:00Z |

## Live WordPress media

Base: `https://taoclinicaltouch.com/wp-content/uploads/2026/10/`

| MON | 2026-10-12 | `ISSUE015_MON_FEED.png` | `ISSUE015_MON_LANDSCAPE.png` | `ISSUE015_MON_STORY_1.png` | `ISSUE015_MON_STORY_2.png` | `ISSUE015_MON_STORY_3.png` |
| TUE | 2026-10-13 | `ISSUE015_TUE_FEED.png` | `ISSUE015_TUE_LANDSCAPE.png` | `ISSUE015_TUE_STORY_1.png` | `ISSUE015_TUE_STORY_2.png` | `ISSUE015_TUE_STORY_3.png` |
| WED | 2026-10-14 | `ISSUE015_WED_FEED.png` | `ISSUE015_WED_LANDSCAPE.png` | `ISSUE015_WED_STORY_1.png` | `ISSUE015_WED_STORY_2.png` | `ISSUE015_WED_STORY_3.png` |
| THU | 2026-10-15 | `ISSUE015_THU_FEED.png` | `ISSUE015_THU_LANDSCAPE.png` | `ISSUE015_THU_STORY_1.png` | `ISSUE015_THU_STORY_2.png` | `ISSUE015_THU_STORY_3.png` |
| FRI | 2026-10-16 | `ISSUE015_FRI_FEED.png` | `ISSUE015_FRI_LANDSCAPE.png` | `ISSUE015_FRI_STORY_1.png` | `ISSUE015_FRI_STORY_2.png` | `ISSUE015_FRI_STORY_3.png` |

All 25 were present in authenticated WordPress media readback on October 6. Before Buffer mutation, anonymously retrieve every full-size URL, verify dimensions (Feed 1080×1350; Landscape 1200×628; Story 1080×1920), compute SHA-256, and record bytes/checksum. Do not use WordPress-generated resized derivatives.

## Approved campaign language

### MON — THE INTERVENTION NEEDS A REASON
Feed/Landscape approved text only:

THE INTERVENTION NEEDS A REASON

A technique is an option. The patient's goal gives it a purpose.

Before the next move, know what you are asking it to accomplish.

### TUE — THE DOSE IS A CLINICAL DECISION
Feed/Landscape approved text only:

THE DOSE IS A CLINICAL DECISION

Pressure is one variable. Pace, duration, and complexity matter too.

Match the input to the person—not the person to the technique.

### WED — REASSESS BEFORE YOU ADD MORE
Feed/Landscape approved text only:

REASSESS BEFORE YOU ADD MORE

A change is information, not an instruction.

Return to the goal before deciding what comes next.

### THU — CHANGE THE PLAN, NOT THE PATIENT
Feed/Landscape approved text only:

CHANGE THE PLAN, NOT THE PATIENT

A plan should respond to the person—not demand that the person justify it.

Adapting is a clinical decision, not a retreat.

### FRI — KNOW WHEN THE WORK IS COMPLETE
Feed/Landscape approved text only:

KNOW WHEN THE WORK IS COMPLETE

More intervention is not automatically more care.

Knowing when to put our hands down is part of knowing how to use them.

Story copy/headlines are locked in `ISSUE015_FIVE_DAY_COPY_AND_VISUAL_DIRECTION.md`. Use them as source validation for the artwork, but **do not add Story captions**.

For Feed/Landscape captions, use only Founder-approved language from the campaign file. Preserve wording. Platform adaptation is limited to the established Issue 014 link treatment above; no new claims, hashtags, emojis, hooks, or rewritten prose.

## WordPress preflight

Authenticated WordPress readback already established:
- post 1877
- title: *The Clinical Practice of Restraint*
- slug: `the-clinical-practice-of-restraint`
- status: `future`
- featured image: `ISSUE015_MON_LANDSCAPE.png`
- body matches canonical article.

Before Buffer execution, verify the scheduled article time is safely ahead of the 8:00 AM ET social launch. **Do not change WordPress unless a discrepancy requires Founder approval.** The site has historically used UTC and has had a 7:45 ET / 11:45 UTC scheduling trap; verify rather than assume.

## Buffer execution requirements

1. Authenticate to Buffer GraphQL with the locally stored credential. Never print or commit the token.
2. Resolve organization and the exact channel IDs.
3. Assert each destination is connected and unlocked.
4. Query the Oct 12–16 scheduled window for duplicates.
5. Verify all 25 public media URLs and checksums.
6. Create exactly 25 content items using the established multi-channel `createContentItem` architecture where applicable.
7. Capture content-item IDs and every child post ID.
8. Independently read back every created object by ID.
9. Reconcile: status, date/time, channel, copy, media URL, Story type, `shouldShareToFeed`, native Story link.
10. STOP on any mismatch. Do not “fix forward” by creating duplicates.
11. Write:
   - `ISSUE015_BUFFER_OBJECTS.json`
   - `ISSUE015_BUFFER_DEPLOYMENT_RECEIPT.md`
   Include all IDs, checksums, bytes, timestamps, destinations, and reconciliation counts.

Required PASS conditions:
- 25/25 content items present.
- 45/45 channel posts scheduled.
- 5/5 Facebook Landscapes.
- 10/10 Instagram Feeds.
- 30/30 Instagram Stories.
- 10/10 Story 3 channel posts carry the canonical native link.
- 5/5 Facebook captions carry canonical URL.
- 10/10 Instagram Feed captions use “link in bio.”
- 15/15 Story content items have no caption.
- zero Facebook Stories.
- zero duplicate IDs.
- zero duplicate (channel,time,media) combinations.
- zero media mismatches.
- zero copy mismatches.
- zero failed imports/channel warnings.

## Brevo gate — after Buffer PASS only

Do **not** begin Brevo until Buffer has passed independent reconciliation and the Buffer receipt is committed.

Then inspect the Issue 014 Brevo receipt/campaign as the immediate production precedent and the current Brevo doctrine. Build Issue 015 from the Founder-approved canonical article and approved Monday landscape/brand assets. Preserve established sender, list, layout, CTA/link conventions, and Monday send cadence unless a newer Founder-approved directive exists.

Required Brevo behavior:
- campaign remains scheduled/queued, not sent immediately;
- canonical article URL is the CTA destination;
- verify sender/list/subject/preheader/body/link/image state by independent readback;
- do not invent new editorial copy where an approved source exists;
- write an Issue 015 Brevo execution receipt with campaign ID and exact scheduled time;
- STOP on any conflict or missing production authority rather than improvising.

## Final reconciliation

After Buffer and Brevo both PASS, produce one final Issue 015 reconciliation record covering:
- WordPress article state and publication time;
- 25 WordPress media objects;
- 25 Buffer content items / 45 deliveries;
- Brevo campaign ID/status/send time;
- canonical URL consistency;
- all checksums and exceptions;
- explicit PASS/FAIL.

Do not touch Issue 014 or any earlier issue objects.

## Founder authorization boundary

Founder has approved execution of Issue 015 distribution. This is authorization to execute the already-approved production package, **not** authorization to change creative, editorial, destinations, cadence, or technical doctrine. Any substantive discrepancy is a STOP-and-report condition.
