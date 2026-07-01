# Learn2Tape Website Rebuild — Project Track

## Objective
Rebuild Learn2Tape site to improve certification course sales conversion.

## Current Focus (This Week)
- [ ] Complete site migration cleanly without breaking funnel-critical assets
- [ ] Lock post-migration CRM/email platform direction (ActiveCampaign)
- [ ] Protect database hygiene during import and rebuild lifecycle marketing foundation

## Funnel Checklist
- [ ] Landing page clarity
- [ ] Offer positioning
- [ ] Social proof/testimonials
- [ ] Checkout friction audit
- [ ] Email follow-up sequence

## Next Actions
1. Finish migration and validate conversion-critical pages, forms, checkout, tracking, and redirects.
2. Set up ActiveCampaign architecture: lists/tags/fields/segments for leads, students, alumni, and future live-class prospects.
3. Build first automations: new lead nurture, buyer onboarding, reengagement, and upsell / ascension path.

## Blockers
- ~~Google Ads purchase conversion is broken~~ — **RESOLVED March 28, 2026**
  - `purchase` is a GA4 key event ✓
  - "Learn2Tape P (web) purchase" is the sole Primary conversion action in Google Ads ✓
  - All garbage Primary conversions removed/demoted ✓
  - Awaiting first ad-attributed purchase to confirm data flow end-to-end

## Google Ads Conversion Tracking — RESOLVED (2026-03-28)
**What was broken:**
- PMax showing 106 "conversions" — all Add to Cart (Primary), not purchases
- Purchase conversion action used Website tag source — pixel never installed on order-received page
- GA4 WAS correctly firing `purchase` — the disconnect was Google Ads ↔ GA4 linkage

**What was fixed:**
- `purchase` confirmed as GA4 key event
- "Learn2Tape P (web) purchase" confirmed sole Primary (GA4 source, property 438258964)
- Removed: "shop" (page view miscategorized as purchase)
- Demoted to Secondary: About Us, demo, read, YouTube subscriptions, YouTube follow-on views, Lead form - Submit
- Identified Pixel Manager (SweetCode) as Google Ads tracking plugin
  - Conversion label "Course Sold" is orphaned (matches no Google Ads conversion action)
  - Pixel Manager reaches order-received 100% of the time — plugin is functional
  - Tag placement warning (footer vs head) is a performance issue, not a tracking failure

**Secondary issue still open:** Search campaign (53 clicks, 0 add-to-carts) pointing to correct URL (/kinesiology-taping-certification/) — low conversion rate on page itself. Investigate separately.

**Spam:** 67/102 form submissions from India (bots). reCAPTCHA added to public demo forms March 28.



## Funnel Tasks Needing Attention
- [ ] Finish site migration and verify redirects, forms, checkout, tracking, and mobile sanity.
- [ ] Finalize ActiveCampaign as the post-migration automation platform.
- [ ] Import cleaned subscriber / student / lead lists with disciplined field mapping and tag rules.
- [ ] Define audience architecture: leads, students, alumni, exclusives, and later live-class prospects.
- [ ] Build first automation set: lead nurture, buyer onboarding, reengagement, and upsell path.
- [ ] Define the content machine: blog, social, email, and Google Ads handoff.
- [ ] Clarify the ascension path from ecourses to future live classes.

## Decisions
- Learn2Tape should compete as a specialized authority brand in taping education, not as a broad CE-course dumping ground.
- Preferred post-migration email/automation platform: ActiveCampaign.
- Marketing stack model: social = attention, website/landing pages = conversion, ActiveCampaign = follow-up/monetization, Google Ads = intent capture once migration/tracking/funnel are stable.
- Database hygiene is strategic: preserve one source of truth, strict tag discipline, and clean audience separation.

## Notes
- Learn2Tape contact exports were reorganized and normalized into segmented import files for subscribers, students, and leads.
- Drewdog cleaned the source database heavily; the cleaned DB is now about one-third the previous size after removing duplicate ad-account junk, mixed tags, and other bad data.
- Post-migration objective: grow sales of the 3 ecourses to new customers, reengage past/present users with exclusive offers, then build live-class pages and lead generation.

## Weekly Review Snapshot
- Wins:
- Stuck points:
- Carryover:
- Next week top outcome:
