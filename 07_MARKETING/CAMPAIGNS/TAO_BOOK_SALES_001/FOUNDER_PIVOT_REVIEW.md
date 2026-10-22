# Tao book sales strategic pivot Founder review

Date: October 21, 2026. Campaign TAO_BOOK_SALES_001.
Decision requested: approve the revised editorial direction and the bounded Shop change plan. Production and implementation remain separate gates.

## Recommendation

Lead with the book's governing idea, support it with reader perspectives once rights are established, and send all initial advertisements to the existing Shop. Keep Amazon, signed and personalized editions together as choices.

Use Creative A first. Plan one website-directed campaign, one initial audience and at most two creatives within the $210/14-day ceiling. Prefer A plus B if a suitable endorsement clears; otherwise A plus C's rights-independent version. No spending or account configuration is authorized.

The most useful immediate conversion improvement is hierarchy and placement, not a new landing page or checkout. The existing Shop already contains an Amazon button, real book imagery, clinical explanation, professional quotes and two functioning Stripe destinations.

## What changes and what stays

Creative 03 “A Personal Touch. From the Author” is ON HOLD — POTENTIAL FUTURE SIGNED-EDITION RETARGETING. Its approved copy and submitted feed image remain unchanged. Visual approval was pending in the existing record; this pivot does not retroactively approve the image.

The previous direct-to-Amazon ad route and signature-first acquisition message are superseded. Canonical book positioning, source cover, typography, palette, preservation discipline and human approval gates remain.

No independent dimensional rendering was found in the preserved campaign. The recorded v01 is a flat-cover reproduction with an external shadow; preserve any additional genuine version if later found.

## Reader evidence

[Reader Evidence and Rights Register](READER_EVIDENCE_AND_RIGHTS_REGISTER.md) contains the selected exact excerpts, source locations, authentication limits and usage status.

Strongest candidates:
- Ruth Werner: thoughtful, reflective reading and invitational bodywork. The live Shop wording matches her original July review submission.
- Doug Nelson: value for both new and experienced massage therapists, supported by a public full reflection.
- Eugenia Binder: a practical invitation to reflect on one's approach, suitable for the reader-experience concept.
- Shannon Johnson: private original and follow-up correspondence establish a specific educator's reported classroom use. The private Founder supplement contains the exact excerpt; no broad adoption claim.
- Shari Aldrich: public enthusiasm for sharing the work with students, not evidence of completed curriculum adoption.
- Laura Boozer: a composed testimonial image exists, but its underlying statement and advertising/photo rights remain incomplete.

No endorsement is yet classified as verified and authorized for paid advertising. B and testimonial-led C are HOLD. A and the non-testimonial alternatives can proceed to editorial approval independently.

Ruth's receipt includes an unlabeled checkbox-like value; the current review form includes marketing-use language. Neither establishes exactly what terms were accepted in July or that this paid Meta scope is covered. Shannon's thread contains no public-use grant. Private raw correspondence and unpublished excerpts stay outside the public repository.

## Current Shop findings

Live inspection: https://taoclinicaltouch.com/shop/ .
Current order is signed-edition hero → two signed offers → clinical value → author story → professional quotes → bulk orders → Amazon section → FAQ → signed-edition closing.

The labeled Amazon purchase button exists in the main page body. It is not absent and is not merely a footer link. At a 390×844 viewport in a logged-in browser, its top was approximately 7,788 CSS px below document top, after six large content sections. The admin toolbar and session affect exact offsets; this is a placement snapshot, not a public-device performance benchmark.

Mobile findings:
- Page width was 390 CSS px at a 390 px viewport; no horizontal overflow in that observation.
- First screen emphasizes Signed Edition Shop, signed/personalized pricing and “Choose your edition.”
- Cover begins near the bottom of that first screen.
- Initial offer section contains two direct options; Amazon appears much later.
- Professional quotes are already available but follow a lengthy author section.
- Both fixed Stripe URLs and data-checkout attributes match earlier audited destinations.
- Phone-width display was inspected; completed transactions and native mobile payment completion were not tested.

Current Shop display:
| Choice | Price displayed | Destination |
|---|---:|---|
| Standard paperback | $14.99 | https://www.amazon.com/dp/B0GVTZZS99 |
| Signed | $19.99 + $5 U.S. shipping; applicable tax | https://buy.stripe.com/aFa3cvaDtapr0LO9gCfUQ00 |
| Personalized + signed | $24.99 + $5 U.S. shipping; applicable tax | https://buy.stripe.com/bJeeVd26X413dyA1OafUQ01 |

Shop displays checked now; Amazon availability/price and Stripe totals were inspected earlier in this same campaign discovery, not newly re-transacted. Reverify all immediately before release. No guaranteed delivery, discount, rating-count or scarcity claim proposed.

### Smallest complete Shop change map

All changes below are proposals. No live edits.

| Current state | Proposed bounded change | Purpose | Tracking and checkout impact |
|---|---|---|---|
| Hero says Signed Edition Shop and emphasizes author-direct edition | Kicker “The book”; retain exact title/subtitle and cover. Replace author-direct sentence with “A clinical perspective on alliance, presence, communication, and permission.” | Match the book-led advertisement | Copy/layout only; no new destination |
| Hero action jumps to signed-only offers | Keep “Choose your edition” linking to the existing choose-your-copy anchor; add a plain “Standard paperback on Amazon” link using the existing data-cta=amazon contract | Make the standard edition discoverable immediately | Same Amazon URL/event; click once must emit once |
| Purchase cards precede value and evidence | Move the existing clinical-value block and a concise existing professional-quote block before the unified purchase section | Book → Value → Reader Evidence → Purchase Choice | Move existing components; preserve root selectors and event contracts |
| Two-card purchase section; Amazon is a later separate section | Add/move an Amazon card into the same choice section, ordered Amazon, Signed, Personalized + Signed. Mobile stacks all three under one heading | Real choice without sending shoppers down another long page | Existing Stripe hrefs, data-checkout values and personalization stay intact; no cart |
| Personalized offer carries Recommended badge and raised/featured styling | Remove recommendation/ranking treatment; use comparable card hierarchy | Keep premium options visible without making them the book's central proposition | Presentation only; no price/default/payment change |
| Long author narrative appears before testimonials | Move it below purchase choices; retain existing content initially | Reduce pre-purchase reading burden while preserving author context | Existing links retained; no new tracking system |
| Late Amazon section duplicates the new unified choice | Consolidate it into the purchase choice; closing CTA links back to all editions rather than signed-only buttons | Avoid competing/duplicated offer architecture | Count DOM nodes, prevent duplicate listeners and preserve event names |
| Current public quotes and source-name typo on perspective page | Keep current Shop quotations unchanged in this bounded plan; separately reconcile any corrected attribution before reuse. Do not propagate “Doug Neloson” | Preserve meaning and provenance | No new testimonial publication authorized |

Proposed purchase section heading: “Choose your copy.”
Cards:
- Standard Paperback — “Buy on Amazon”; $14.99; “Amazon sets shipping and tax at checkout.”
- Signed Paperback — “Order a Signed Copy”; $19.99 + $5 U.S. shipping; tax calculated at checkout.
- Personalized + Signed — “Personalize My Copy”; $24.99 + $5 U.S. shipping; tax calculated at checkout. Preserve the existing inscription disclaimer.
Do not call Amazon shipping free or apply the direct-shop $5 shipping charge to Amazon.

On approval, preserve page 1277's actual current source and scoped CSS before changes, implement on an isolated preview, inspect phone/desktop, compare exact outgoing links/event behavior, then request separate deployment approval with rollback ready. No production page backup or edit was made in this read-only pass.

## Three editorial and composition briefs

Every brief below is proposed, not locked or production-approved. Destination for all:
https://taoclinicaltouch.com/shop/
Append campaign UTMs per creative/platform. Each ad presents one invitation to choose a copy; price comparisons belong on the Shop.

Shared format: first 1080×1350 feed master only. Cormorant Garamond and Source Sans Pro; navy #182633, ivory #F7F4EE, charcoal #3A3A3A, gold #B8860B. Use the recovered authentic front artwork with its existing fidelity evidence. No author portrait, fake handwriting, fabricated stars, issue masthead, invented ripple or simulated testimonials. Keep standalone ripple omitted until approved source resolved; printed cover ripple remains intact.

### Creative A The Book

Purpose: communicate the intellectual distinction to practicing clinicians, educators and students.
On-image headline, exact approved positioning:
“This book is not intended to replace technique.
It is intended to govern it.”
Supporting line: “Alliance. Presence. Communication. Permission.”
CTA: “Explore the Book”

Meta primary:
The Tao of Clinical Touch: The Neuroscience of Permission examines the conditions surrounding hands-on care: therapeutic alliance, practitioner presence, communication, safety, and permission.

A clinical philosophy for reflecting on how existing skills are applied.

Explore the book and choose your copy: standard paperback on Amazon, signed, or personally inscribed.

Meta headline: The Tao of Clinical Touch
Description: Explore the book. Choose your copy.
Native CTA candidate: Learn More, subject to available account settings.
Composition: authentic book prominent at center/right; complete positioning statement upper-left with generous space. Supporting themes and CTA in quiet lower band. Book is the dominant visual object; do not shrink it to make room for an essay.
Evidence: Founder-approved positioning and authenticated cover; supporting prose is proposed editorial language.
Status: READY FOR FOUNDER EDITORIAL REVIEW.
Organic adaptation: use the same primary text; Facebook gets a tracked Shop URL, Instagram a verified bio or native Story link. No organic publication authorized.

### Creative B Professional Perspectives

Purpose: establish professional credibility.
Exact proposed on-image excerpt: “a thoughtful and inspiring re-imagining of the power of gentle, invitational, listening bodywork.”
Source: https://taoclinicaltouch.com/shop/ ; original submission cross-check in the rights register.
Attribution: “Ruth Werner · Author, A Massage Therapist’s Guide to Pathology” after current identification and paid-use approval.
Supporting line: “The Tao of Clinical Touch”
CTA: “Explore the Book”

Meta primary:
Ruth Werner describes The Tao of Clinical Touch as a thoughtful invitation to reflect on therapeutic touch.

Explore its clinical philosophy, read professional perspectives, and choose the copy that suits you through the Tao Shop.

Meta headline: A professional perspective on the Tao
Description: Read more and choose your edition.
Native CTA candidate: Learn More.
Composition: readable quotation at upper-left, attribution immediately adjacent, authentic book large in lower/right field. No headshot, stars or implied organizational endorsement. Do not combine homepage/Shop/foreword passages.
Evidence: verified review submission and matching Shop passage; paid scope unconfirmed.
Status: HOLD FOR PAID RIGHTS AND FOUNDER EDITORIAL APPROVAL.
Organic adaptation: same text only after organic-use scope and exact adaptation are approved.

Rights-independent alternative B0:
On-image headline: “THE CONDITIONS SURROUNDING TOUCH.”
Supporting: “Alliance. Presence. Communication. Permission.”
CTA: “Explore the Book”
Meta primary: “The Tao of Clinical Touch explores the clinical relationship, the treatment environment, and the judgment surrounding skilled touch. Read about the book and choose your edition through the Tao Shop.”
Meta headline: The Tao of Clinical Touch
Description: A clinical philosophy for hands-on care.
Composition: book-led navy/ivory typography, no quotation marks, reviewer names, stars or implied independent endorsement.
This is book description, not substitute social proof.

### Creative C Reader Experience

Purpose: connect to professional reflection without inventing treatment outcomes.
Exact proposed on-image excerpt: “We could all use a reminder to take a moment to reflect on our approach and this book does exactly that.”
Source: https://taoclinicaltouch.com/share-your-perspective/ .
Attribution: “Eugenia Binder · Reader” pending identity/usage confirmation; no unverified credentials.
Supporting line: “The Tao of Clinical Touch”
CTA: “Find Your Copy”

Meta primary:
The Tao of Clinical Touch offers a framework for considering the clinical encounter: how we communicate, establish trust, and approach hands-on care.

Read a reader's perspective, explore the book, and choose your copy through the Tao Shop.

Meta headline: A reader’s perspective on the Tao
Description: Explore the book and purchasing options.
Native CTA candidate: Learn More.
Composition: authentic book central; one intact continuous reader sentence, with clear attribution, on ivory. No stock portrait standing in for the reader, no “results” badge or classroom-adoption claim.
Evidence: public named reflection; paid rights unconfirmed. Shannon's independently authenticated private classroom account is a separate possible educator variant, not blended into Eugenia's quotation.
Status: HOLD FOR PAID RIGHTS AND FOUNDER EDITORIAL APPROVAL.
Organic adaptation: same offer and themes, with platform-specific Shop link only after use scope is approved.

Rights-independent alternative C0, recommended second creative if no rights clear:
On-image headline: “A FRAMEWORK FOR PROFESSIONAL REFLECTION.”
Supporting line: “Alliance, communication, and permission in hands-on care.”
CTA: “Find Your Copy”
Meta primary: “For your clinical library, a professional discussion, or a conversation with students. The Tao of Clinical Touch explores alliance, presence, communication, and permission. Learn about the book and choose a standard, signed, or personalized copy through the Tao Shop.”
Meta headline: Reflect on the clinical encounter
Description: The Tao of Clinical Touch.
Composition: authentic book, restrained editorial space, no reader attribution, no claim of proven adoption or outcomes.

## Measurement and spending

Live HTML still contains GTM-PP2CC4D6 and G-BEBQ6ENK69. Source-level events remain view_item_list, select_item, begin_checkout, amazon_click, bulk_inquiry_click and faq_open. No fbq/fbevents marker was found in inspected HTML; that does not exclude GTM-injected Pixel or server-side CAPI.

WPConsent defaults and the separate consent-linked Stripe-reference script remain visible. Its enabled configuration coexists with staging/purchases-off wording. Backend delivery, consent withdrawal, Pixel/CAPI eligibility/deduplication and Stripe reporting are unverified. No purchase-optimization recommendation is made until these account-level checks pass.

Required funnel:
Meta click → Shop visit → edition choice → Amazon outbound OR signed/personalized Stripe checkout click → verified paid order where measurable.
There is no observed cart stage. Do not relabel checkout clicks or Amazon exits as purchases.

| Stage | Evidence required |
|---|---|
| Ad delivery | Meta account/campaign/ad export: spend, impressions, reach, clicks; available controls verified before configuration |
| Shop entry | Tagged visits and consent-eligible receipt; creative IDs/UTMs preserved |
| Edition choice | Existing amazon_click or begin_checkout with checkout_type signed/personalized and placement; no inscription/user text |
| Direct purchase | Successful Stripe payment/order identity, amount, refund status, actual fee; reconcile revenue and deduplicate |
| Amazon purchase | Authorized Amazon Attribution report/link where available; outbound event alone is insufficient |
| Economics | Net royalty or direct contribution less actual variable fulfillment and media costs |

UTMs: utm_source=instagram or facebook, utm_medium=paid_social, utm_campaign=tao_book_sales_001, utm_content=creative_a_book_v01 (or b/c identifier).
Preserve eligible source data through Stripe's existing consent-bound reference mechanism only after verified. For Shop→Amazon, verify current authorized Amazon Attribution account/link strategy; adding UTMs to a Shop URL does not make Amazon orders attributable. Do not silently replace the working Amazon URL with an unverified tag.

A single Shop destination still contains two purchase systems. Meta direct-purchase optimization, if eventually eligible, would optimize observable direct sales rather than all Amazon sales. Report the two channel outcomes separately and do not assume either is a complete campaign total.
No L2T/NCB list upload, no health/patient data, no contact or inscription text in analytics.
$210 is the maximum proposed 14-day media total, not authorization. Two ads in one audience avoid fragmentation but do not guarantee equal delivery or a statistically valid A/B test. Use an actual experiment only if available and appropriate. Account timing/billing/spend limits require inspection; no automatic scaling.
Review proposals remain day 3 for delivery/measurement, day 7 for funnel loss and contribution, day 14 for retain/revise/pause. No automation scheduled. Profitability and sustainable CAC remain unverified until actual royalty/copy/postage/fees/labor are supplied.

## Decisions and sequence

1. Approve/revise exact Creative A copy/composition as the first master.
2. Select B/C subject to rights, or approve C0 as the second book-led direction. Rights clearance remains separate from Founder editorial approval.
3. Approve/revise the bounded Shop change map as a plan. Preview and deployment approval follow separately.
4. Resolve existing paid-use permissions through original records; no outreach has been authorized or sent.
5. Validate Meta/GA4/Stripe/Amazon account evidence and unit costs before launch-readiness assessment.

Gate A: strategic pivot recorded.
Gate B: evidence located/classified; paid rights HOLD.
Gate C: live Shop audit/change map ready for review.
Gate D: revised editorial approval PENDING; STOP before image production.
Gate E: first new feed image NOT STARTED.
Gates F/G: website/tracking implementation and launch HOLD.

No new creative, site edit, payment, campaign configuration, publication, scheduling or spending occurred. Prior Creative 03 originals and hashes remain intact.

