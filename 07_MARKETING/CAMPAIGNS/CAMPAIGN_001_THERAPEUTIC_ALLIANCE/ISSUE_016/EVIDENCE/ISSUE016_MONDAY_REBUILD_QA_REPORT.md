# ISSUE No. 016 — Monday Rebuild QA

**Date:** October 12, 2026  
**Status:** FOUNDER APPROVED — October 12, 2026  
**Theme:** Explain the decision  
**Headline:** EXPLAIN THE DECISION  
**Scope:** Recreate the unavailable Monday originals using approved campaign copy. These are NEW replacement renders; the previous originals' approval does not transfer.

## Source and branding authority

[Canonical approved campaign](https://github.com/learn2tape19/finding-my-wei/blob/main/07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_016/ISSUE016_FIVE_DAY_COPY_AND_VISUAL_DIRECTION.md)

Campaign blob recorded in accepted handoff: `b6db1cf92c4c3353d15b3cc7eb2e701dcbff1227`. Monday copy was taken from its verbatim transcription in the accepted handoff. Current branding corrections govern: ISSUE No. 016, dominant TRUST, day identifier and exact daily message; charcoal/teal/cream and editorial serif publication branding.

Available founder-approved Tuesday files were used as style references only. Unavailable Monday originals were not inspected or reused.

## Completed dimension gates

| Final PNG | Canvas before production | Final image-decoder check | Independent PNG IHDR + full decode |
|---|---:|---:|---:|
| ISSUE016_MON_FEED_BUILD1_1080x1380_REBUILD_v01_DRAFT.png | 1080×1380 PASS | 1080×1380 PASS | 1080×1380 PASS |
| ISSUE016_MON_LANDSCAPE_BUILD2_1200x628_REBUILD_v01_DRAFT.png | 1200×628 PASS | 1200×628 PASS | 1200×628 PASS |
| ISSUE016_MON_STORY01_1080x1920_REBUILD_v01_DRAFT.png | 1080×1920 PASS | 1080×1920 PASS | 1080×1920 PASS |
| ISSUE016_MON_STORY02_1080x1920_REBUILD_v01_DRAFT.png | 1080×1920 PASS | 1080×1920 PASS | 1080×1920 PASS |
| ISSUE016_MON_STORY03_1080x1920_REBUILD_v01_DRAFT.png | 1080×1920 PASS | 1080×1920 PASS | 1080×1920 PASS |

All dimensions are width × height in pixels. Five target canvases were created, saved, reopened, and verified before production. Exact exported PNGs were checked using macOS image decoding, then independently through their PNG headers and full Pillow decoding.

## Rendered-copy proof

Every rendered word was visually proofread in the final-size PNGs after export.

Shared branding correct in all five:
- `ISSUE No. 016`
- `THE CLINICAL PRACTICE OF`
- `TRUST`
- `Monday`
- `The Tao of Clinical Touch`
- `A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.`

| Asset | Exact approved headline/message | Result |
|---|---|---|
| Feed | EXPLAIN THE DECISION | PASS |
| Landscape | EXPLAIN THE DECISION | PASS |
| Story 1 | EXPLAIN THE DECISION | PASS |
| Story 2 | A clinical explanation should give the patient something they can respond to. | PASS |
| Story 3 | Trust begins with reasoning the patient can question. | PASS |

Capitalization, punctuation, final periods, and all words retained. Line breaks do not change copy. Stories 2–3 carry only their own panel message, not another daily headline. No additional CTA, hashtag, byline, URL, or background text added.

## Exact approved Feed / Landscape caption

Use unchanged outside both images:

A patient can agree to care without understanding every decision made during it.

Explain what you are trying to accomplish. Leave room for the person receiving care to question the plan.

## Visual inspection

All five PASS:
- TRUST remains largest and dominant; Monday and exact daily message follow.
- Charcoal, teal, cream and editorial serif publication treatment visually match the approved series references.
- Fully clothed clinician and patient converse at equal eye level in a bright contemporary clinical room before hands-on care.
- Clinician explains with natural open-palm gestures; patient visibly engaged, with question participation on Story 3.
- Calm expressions, natural posture, comfortable conversational distance.
- Hands, fingers, arms, faces, and seated bodies inspected; no obvious extra limbs, fused hands, deformities, or critical clipping found.
- No hands-on care, shoulder exercise demonstration, forced positioning, implied diagnosis, outcome claims, anatomy imagery, skeletons, charts, or diagrams.
- Final copy readable, complete, and uncut.

Branding matching is visual against approved Tuesday assets; exact historical font files/color tokens and original Monday artwork were not supplied.

## Independent composition and exact-size export

Built-in image-generation tool used in five separate asset calls with separate format/panel prompts. Tuesday references supplied branding only. No finished Feed was converted into Landscape or Stories, and no Story was converted into another Story.

The generator did not retain native requested dimensions despite verified canvas references. Each independently generated same-format composition was proportionally fitted into its own exact canvas:

| Asset | Fitted content | Exact final canvas |
|---|---:|---:|
| Feed | 1080×1378 | 1080×1380; 1px cream top/bottom |
| Landscape | 1200×628 | 1200×628 |
| Story 1 | 1079×1920 | 1080×1920; 1px cream width padding |
| Story 2 | 1080×1920 | 1080×1920; editorial margins preserved |
| Story 3 | 1013×1800 | 1080×1920; centered cream outer margins |

No separate-axis stretching, distortion, content cropping, or cross-format repurposing occurred. Every final file was reopened at original resolution and proofread after export. Integrity hashes are recorded in `dimension-verification.json`.

## Approval and upload gate

All five Monday REBUILD v01 assets remain **DRAFT — AWAITING FOUNDER APPROVAL**. No replacement has been uploaded. Previous approval of missing Monday originals does not approve these new files.

The standing user request authorizes Issue 016 media-library uploads. Once Drew explicitly approves these exact replacements, Monday's five may be uploaded to complete the 25-asset media set. Tuesday–Friday's 20 approved PNGs have already been uploaded and independently verified. No article/page or scheduling changes authorized or performed.

## Prompt record — built-in image-generation tool

### feed
```text
Use case: ads-marketing. Issue No. 016 Monday editorial clinical campaign. This is a NEW REBUILD of unavailable previous Monday originals; no old image approval transfers to it. Image 1 is the verified target-size blank canvas. Image 2 is founder-approved Tuesday artwork for charcoal/teal/cream palette, elegant high-contrast serif typography, divider rules and publication branding ONLY. Do NOT reuse its shoulder movement or photograph. Compose a fresh original Monday scene independently.
Exact shared text, case and punctuation:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Monday
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Hierarchy: small issue identifier and small lead-in, huge dominant TRUST alone on its own line, teal Monday underneath, then exact panel headline/message subordinate to TRUST. Footer masthead serif and uppercase tagline with final period. No extra copy, story numbers, CTA, hashtags, author, URL, or scene lettering. Daily headline EXPLAIN THE DECISION MUST be ALL UPPERCASE, not Title Case.
MONDAY VISUAL: treatment-room conversation BEFORE any hands-on care. Fully clothed female clinician in teal and fully clothed female patient in cream sit at equal eye level in a bright contemporary clinical room. Clinician offers a clear explanation with one small relaxed palm-up conversational gesture near her own waist. Patient visibly ENGAGED, thoughtfully listening with natural eye contact and perhaps a quiet question; patient hands resting on her own lap. Calm measured expressions, no exaggerated grin, patient is not passive or compliant. This is explanation before treatment, NOT a shoulder exercise, NOT a pause in active treatment, NOT confrontation, NOT end-of-consultation departure. Treatment table may be in background, but no contact, no manipulation or diagnosis implied. Comfortable conversational distance, open natural posture. Plausible faces, hands, fingers, forearms and seated bodies.
No diagrams, anatomy images, skeletons, charts, anatomical posters, x-rays, model bones, forced positioning, hands-on treatment, recovery claim or implied cure. Every word sharply readable, exact spelling/capitalization/punctuation and full unclipped text.
Feed Build 1: EXACT1080x1380. Centered cream editorial header top, new vertical photograph middle, masthead footer bottom. Exact daily headline "EXPLAIN THE DECISION", ALL UPPERCASE, below Monday and dominant TRUST. Photo: clinician left and patient right seated in chairs, clinician's small palm-up explanation gesture, engaged patient with hands on lap and thoughtful eye contact. Minimum45px text margin; complete hands inside frame.
```

### landscape
```text
Use case: ads-marketing. Issue No. 016 Monday editorial clinical campaign. This is a NEW REBUILD of unavailable previous Monday originals; no old image approval transfers to it. Image 1 is the verified target-size blank canvas. Image 2 is founder-approved Tuesday artwork for charcoal/teal/cream palette, elegant high-contrast serif typography, divider rules and publication branding ONLY. Do NOT reuse its shoulder movement or photograph. Compose a fresh original Monday scene independently.
Exact shared text, case and punctuation:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Monday
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Hierarchy: small issue identifier and small lead-in, huge dominant TRUST alone on its own line, teal Monday underneath, then exact panel headline/message subordinate to TRUST. Footer masthead serif and uppercase tagline with final period. No extra copy, story numbers, CTA, hashtags, author, URL, or scene lettering. Daily headline EXPLAIN THE DECISION MUST be ALL UPPERCASE, not Title Case.
MONDAY VISUAL: treatment-room conversation BEFORE any hands-on care. Fully clothed female clinician in teal and fully clothed female patient in cream sit at equal eye level in a bright contemporary clinical room. Clinician offers a clear explanation with one small relaxed palm-up conversational gesture near her own waist. Patient visibly ENGAGED, thoughtfully listening with natural eye contact and perhaps a quiet question; patient hands resting on her own lap. Calm measured expressions, no exaggerated grin, patient is not passive or compliant. This is explanation before treatment, NOT a shoulder exercise, NOT a pause in active treatment, NOT confrontation, NOT end-of-consultation departure. Treatment table may be in background, but no contact, no manipulation or diagnosis implied. Comfortable conversational distance, open natural posture. Plausible faces, hands, fingers, forearms and seated bodies.
No diagrams, anatomy images, skeletons, charts, anatomical posters, x-rays, model bones, forced positioning, hands-on treatment, recovery claim or implied cure. Every word sharply readable, exact spelling/capitalization/punctuation and full unclipped text.
Landscape Build 2: EXACT1200x628. Independent wide composition: left cream text roughly48% and right fresh consultation photo52%. Exact headline "EXPLAIN THE DECISION" ALL UPPERCASE, below teal Monday and enormous TRUST. Masthead/tagline lower left. New horizontal explanation-before-care scene: seated clinician on left in photo uses a small open-palm gesture, engaged patient on right listens, equal eye level, all visible hands complete. Do not reuse Feed composition or shoulder photo.
```

### story1
```text
Use case: ads-marketing. Issue No. 016 Monday editorial clinical campaign. This is a NEW REBUILD of unavailable previous Monday originals; no old image approval transfers to it. Image 1 is the verified target-size blank canvas. Image 2 is founder-approved Tuesday artwork for charcoal/teal/cream palette, elegant high-contrast serif typography, divider rules and publication branding ONLY. Do NOT reuse its shoulder movement or photograph. Compose a fresh original Monday scene independently.
Exact shared text, case and punctuation:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Monday
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Hierarchy: small issue identifier and small lead-in, huge dominant TRUST alone on its own line, teal Monday underneath, then exact panel headline/message subordinate to TRUST. Footer masthead serif and uppercase tagline with final period. No extra copy, story numbers, CTA, hashtags, author, URL, or scene lettering. Daily headline EXPLAIN THE DECISION MUST be ALL UPPERCASE, not Title Case.
MONDAY VISUAL: treatment-room conversation BEFORE any hands-on care. Fully clothed female clinician in teal and fully clothed female patient in cream sit at equal eye level in a bright contemporary clinical room. Clinician offers a clear explanation with one small relaxed palm-up conversational gesture near her own waist. Patient visibly ENGAGED, thoughtfully listening with natural eye contact and perhaps a quiet question; patient hands resting on her own lap. Calm measured expressions, no exaggerated grin, patient is not passive or compliant. This is explanation before treatment, NOT a shoulder exercise, NOT a pause in active treatment, NOT confrontation, NOT end-of-consultation departure. Treatment table may be in background, but no contact, no manipulation or diagnosis implied. Comfortable conversational distance, open natural posture. Plausible faces, hands, fingers, forearms and seated bodies.
No diagrams, anatomy images, skeletons, charts, anatomical posters, x-rays, model bones, forced positioning, hands-on treatment, recovery claim or implied cure. Every word sharply readable, exact spelling/capitalization/punctuation and full unclipped text.
Story 1: EXACT1080x1920. Centered editorial card with cream outer margins like approved Story. All text inside x80..1000,y250..1660. Sole exact panel message "EXPLAIN THE DECISION" ALL UPPERCASE, no extra daily headline. New independent medium seated explanation-before-care photo, clinician left palm-up at waist and patient right thoughtfully engaged; no physical contact. TRUST dominant, Monday teal.
```

### story2
```text
Use case: ads-marketing. Issue No. 016 Monday editorial clinical campaign. This is a NEW REBUILD of unavailable previous Monday originals; no old image approval transfers to it. Image 1 is the verified target-size blank canvas. Image 2 is founder-approved Tuesday artwork for charcoal/teal/cream palette, elegant high-contrast serif typography, divider rules and publication branding ONLY. Do NOT reuse its shoulder movement or photograph. Compose a fresh original Monday scene independently.
Exact shared text, case and punctuation:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Monday
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Hierarchy: small issue identifier and small lead-in, huge dominant TRUST alone on its own line, teal Monday underneath, then exact panel headline/message subordinate to TRUST. Footer masthead serif and uppercase tagline with final period. No extra copy, story numbers, CTA, hashtags, author, URL, or scene lettering. Daily headline EXPLAIN THE DECISION MUST be ALL UPPERCASE, not Title Case.
MONDAY VISUAL: treatment-room conversation BEFORE any hands-on care. Fully clothed female clinician in teal and fully clothed female patient in cream sit at equal eye level in a bright contemporary clinical room. Clinician offers a clear explanation with one small relaxed palm-up conversational gesture near her own waist. Patient visibly ENGAGED, thoughtfully listening with natural eye contact and perhaps a quiet question; patient hands resting on her own lap. Calm measured expressions, no exaggerated grin, patient is not passive or compliant. This is explanation before treatment, NOT a shoulder exercise, NOT a pause in active treatment, NOT confrontation, NOT end-of-consultation departure. Treatment table may be in background, but no contact, no manipulation or diagnosis implied. Comfortable conversational distance, open natural posture. Plausible faces, hands, fingers, forearms and seated bodies.
No diagrams, anatomy images, skeletons, charts, anatomical posters, x-rays, model bones, forced positioning, hands-on treatment, recovery claim or implied cure. Every word sharply readable, exact spelling/capitalization/punctuation and full unclipped text.
Story 2: EXACT1080x1920. Cream editorial card, generous margins x80..1000,y250..1660. Sole exact panel message "A clinical explanation should give the patient something they can respond to." Sentence case, final period. No additional daily headline. Independent closer consultation view showing clinician clearly explaining with small relaxed hand gesture, patient actively considering what is said and engaged at equal eye level, hands resting. Full message wraps into balanced lines below huge TRUST and teal Monday, reduce photo height if needed, do not shorten.
```

### story3
```text
Use case: ads-marketing. Issue No. 016 Monday editorial clinical campaign. This is a NEW REBUILD of unavailable previous Monday originals; no old image approval transfers to it. Image 1 is the verified target-size blank canvas. Image 2 is founder-approved Tuesday artwork for charcoal/teal/cream palette, elegant high-contrast serif typography, divider rules and publication branding ONLY. Do NOT reuse its shoulder movement or photograph. Compose a fresh original Monday scene independently.
Exact shared text, case and punctuation:
ISSUE No. 016
THE CLINICAL PRACTICE OF
TRUST
Monday
The Tao of Clinical Touch
A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.
Hierarchy: small issue identifier and small lead-in, huge dominant TRUST alone on its own line, teal Monday underneath, then exact panel headline/message subordinate to TRUST. Footer masthead serif and uppercase tagline with final period. No extra copy, story numbers, CTA, hashtags, author, URL, or scene lettering. Daily headline EXPLAIN THE DECISION MUST be ALL UPPERCASE, not Title Case.
MONDAY VISUAL: treatment-room conversation BEFORE any hands-on care. Fully clothed female clinician in teal and fully clothed female patient in cream sit at equal eye level in a bright contemporary clinical room. Clinician offers a clear explanation with one small relaxed palm-up conversational gesture near her own waist. Patient visibly ENGAGED, thoughtfully listening with natural eye contact and perhaps a quiet question; patient hands resting on her own lap. Calm measured expressions, no exaggerated grin, patient is not passive or compliant. This is explanation before treatment, NOT a shoulder exercise, NOT a pause in active treatment, NOT confrontation, NOT end-of-consultation departure. Treatment table may be in background, but no contact, no manipulation or diagnosis implied. Comfortable conversational distance, open natural posture. Plausible faces, hands, fingers, forearms and seated bodies.
No diagrams, anatomy images, skeletons, charts, anatomical posters, x-rays, model bones, forced positioning, hands-on treatment, recovery claim or implied cure. Every word sharply readable, exact spelling/capitalization/punctuation and full unclipped text.
Story 3: EXACT1080x1920. Centered cream editorial Story card, safe text x80..1000,y250..1660. Sole exact panel message "Trust begins with reasoning the patient can question." Sentence case and final period. No extra daily headline. Fresh independent wider seated conversation before care, clinician left attentive as patient right asks a quiet thoughtful question with a tiny natural gesture, equal eye level, neither touching. Patient participation visible, not disagreement or distress. TRUST dominant and Monday teal.
```


## Founder approval — October 12, 2026

Drew approved all five Monday REBUILD v01 exports with “approved”. Approved copies are byte-identical to the reviewed drafts. This supersedes earlier pending-approval statements. The standing WordPress media upload request authorizes their upload. No article publishing or scheduling authorized.
