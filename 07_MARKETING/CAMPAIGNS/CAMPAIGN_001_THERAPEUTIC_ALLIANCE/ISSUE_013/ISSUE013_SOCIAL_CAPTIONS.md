# Issue 013 — Social Captions and Buffer Object Plan

**Status:** ASSEMBLED FROM FOUNDER-APPROVED SOURCE — awaiting Founder confirmation
**Source:** `ISSUE013_FOUNDER_APPROVED_PRODUCTION_GATE.md`
**Convention inherited from:** Issues 011 and 012

---

## Caption convention — inherited, not invented

Per the Issue 012 Founder direction (Reading B) and the Issue 011 precedent:

> The day headline and supporting line are **approved visual copy baked into the Feed asset**.
> The canonical Buffer Feed caption is therefore **body + hashtags only.**

Verified for Issue 013 by direct visual inspection of the approved masters: each Feed image carries
the headline and the supporting line. The **closing thought / body** is *not* in the image, so it
becomes the caption. No duplication, no invention, nothing rewritten.

**Hashtag block — identical on all five days, inherited verbatim from Issue 011:**

```
#TheTaoOfClinicalTouch #ClinicalTouch #MassageTherapy #ClinicalReasoning #TherapeuticAlliance
```

**Story frames carry no caption** — Instagram only, image alone. Issues 011 and 012 precedent.

---

## Monday — September 28

**Feed caption** (Facebook + Instagram):

> The session creates an opening. Life determines what happens next. Our role is to set the conditions for that possibility.
>
> #TheTaoOfClinicalTouch #ClinicalTouch #MassageTherapy #ClinicalReasoning #TherapeuticAlliance

*Omitted as baked into the asset:* headline `THE SESSION IS NOT THE FINISH LINE`; support `A change observed is real. But a change observed is not yet a change integrated.`

## Tuesday — September 29

**Feed caption:**

> Change can be available before it feels familiar. The nervous system needs time to make it home.
>
> #TheTaoOfClinicalTouch #ClinicalTouch #MassageTherapy #ClinicalReasoning #TherapeuticAlliance

*Omitted as baked in:* headline `NEW DOESN'T HAVE TO MEAN NORMAL YET`; support `Possibility may happen in a moment. / Familiarity takes time.`

## Wednesday — September 30

**Feed caption:**

> You don't have to have it all figured out to move forward. Clarity often comes in the space between the doing.
>
> #TheTaoOfClinicalTouch #ClinicalTouch #MassageTherapy #ClinicalReasoning #TherapeuticAlliance

*Omitted as baked in:* headline `PAUSE CREATES PERSPECTIVE.`; support `A moment of reflection turns experience into understanding.`

## Thursday — October 1

**Feed caption:**

> The work becomes meaningful when they can use it without us.
>
> #TheTaoOfClinicalTouch #ClinicalTouch #MassageTherapy #ClinicalReasoning #TherapeuticAlliance

*Omitted as baked in:* headline `CHANGE HAS TO FIND A LIFE OUTSIDE THE ROOM.`; support `What happens in treatment matters. / What becomes usable afterward matters more.`

## Friday — October 2

**Feed caption:**

> The possibility may begin with us. The life it enters belongs to them.
>
> #TheTaoOfClinicalTouch #ClinicalTouch #MassageTherapy #ClinicalReasoning #TherapeuticAlliance

*Omitted as baked in:* headline `THE CHANGE WAS NEVER OURS TO KEEP.`; support `Our work can help make something possible. / What they do with that possibility belongs to them.`

---

## Buffer object plan — 25 objects

**Destinations** (resolved and verified, both connected and unlocked):

| Channel | ID |
|---|---|
| Tao Facebook | `6a3eb95f5ab6d2f106763fc9` |
| Tao Instagram | `6a3eb89f5ab6d2f106763ca0` |

**Metadata**, per Issues 011/012: Facebook `type: post`; Instagram Feed `type: post, shouldShareToFeed: true`; Instagram Story `type: story, shouldShareToFeed: false`. `schedulingType: automatic`.

| # | Day | Role | Channel | ET | dueAt (UTC) | Caption |
|---:|---|---|---|---|---|---|
| 1 | Mon | FEED | Facebook | 8:00 AM | `2026-09-28T12:00:00.000Z` | Monday |
| 2 | Mon | FEED | Instagram | 8:00 AM | `2026-09-28T12:00:00.000Z` | Monday |
| 3 | Mon | STORY-01 | Instagram | 9:00 AM | `2026-09-28T13:00:00.000Z` | none |
| 4 | Mon | STORY-02 | Instagram | 11:00 AM | `2026-09-28T15:00:00.000Z` | none |
| 5 | Mon | STORY-03 | Instagram | 1:00 PM | `2026-09-28T17:00:00.000Z` | none |
| 6 | Tue | FEED | Facebook | 8:00 AM | `2026-09-29T12:00:00.000Z` | Tuesday |
| 7 | Tue | FEED | Instagram | 8:00 AM | `2026-09-29T12:00:00.000Z` | Tuesday |
| 8 | Tue | STORY-01 | Instagram | 9:00 AM | `2026-09-29T13:00:00.000Z` | none |
| 9 | Tue | STORY-02 | Instagram | 11:00 AM | `2026-09-29T15:00:00.000Z` | none |
| 10 | Tue | STORY-03 | Instagram | 1:00 PM | `2026-09-29T17:00:00.000Z` | none |
| 11 | Wed | FEED | Facebook | 8:00 AM | `2026-09-30T12:00:00.000Z` | Wednesday |
| 12 | Wed | FEED | Instagram | 8:00 AM | `2026-09-30T12:00:00.000Z` | Wednesday |
| 13 | Wed | STORY-01 | Instagram | 9:00 AM | `2026-09-30T13:00:00.000Z` | none |
| 14 | Wed | STORY-02 | Instagram | 11:00 AM | `2026-09-30T15:00:00.000Z` | none |
| 15 | Wed | STORY-03 | Instagram | 1:00 PM | `2026-09-30T17:00:00.000Z` | none |
| 16 | Thu | FEED | Facebook | 8:00 AM | `2026-10-01T12:00:00.000Z` | Thursday |
| 17 | Thu | FEED | Instagram | 8:00 AM | `2026-10-01T12:00:00.000Z` | Thursday |
| 18 | Thu | STORY-01 | Instagram | 9:00 AM | `2026-10-01T13:00:00.000Z` | none |
| 19 | Thu | STORY-02 | Instagram | 11:00 AM | `2026-10-01T15:00:00.000Z` | none |
| 20 | Thu | STORY-03 | Instagram | 1:00 PM | `2026-10-01T17:00:00.000Z` | none |
| 21 | Fri | FEED | Facebook | 8:00 AM | `2026-10-02T12:00:00.000Z` | Friday |
| 22 | Fri | FEED | Instagram | 8:00 AM | `2026-10-02T12:00:00.000Z` | Friday |
| 23 | Fri | STORY-01 | Instagram | 9:00 AM | `2026-10-02T13:00:00.000Z` | none |
| 24 | Fri | STORY-02 | Instagram | 11:00 AM | `2026-10-02T15:00:00.000Z` | none |
| 25 | Fri | STORY-03 | Instagram | 1:00 PM | `2026-10-02T17:00:00.000Z` | none |

## Blocking dependency

**Every one of these 25 objects requires a public, checksum-verified WordPress media URL.** Buffer
has no upload capability; images must be public HTTPS. No Buffer object can be created until the
25 masters are uploaded to WordPress and each URL is checksum-reconciled against the canonical
repository hash.

Everything else — captions, destinations, timestamps, metadata, structure — is complete and
verified. The media URLs are the single unresolved input.
