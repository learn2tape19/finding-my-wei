# Learn2Tape — October 8, 2026: Commercial and Measurement Decision Record

**Status:** Founder decisions recorded; implementation and test details below are reported from Claude's session and should not be mistaken for an independent live-site audit. **Scope:** learn2tape.com K-Cuts certification; Tao only where links cross over. **Objective:** restore qualified $299 certification enrollments with reliable conversion measurement. Google Ads remains **paused** pending readiness.

## Durable founder decisions
- **Product 2249 ($299) is the sole actively promoted K-Cuts Certification offer**: eCourse component 1873, digital eBook 1830, LearnDash course 1589. No printed-book bonus or physical-book bundle advertising; approximately eight printed books remained and restocking depends on renewed sales.
- Product **8327**, the $299 physical-book bundle (regular $348.99), was reported set **out of stock**, reversibly. Four certification CTAs moved to 2249, fifth already pointed there; physical-book bonus widget removed and misleading book graphic replaced. Preserve 8327 configuration and order history.
- Nine legacy direct add-to-cart links for **2880** were reported migrated to **2249**; preserve 2880 for historical orders.
- **49069**, a competing $249 demo special with course access but no eBook, was approved for reversible out-of-stock withdrawal, replacing the Bunion Demo CTA with 2249 and removing it as a purchasable related-product alternative. **Execution not independently confirmed in this record.**
- **1830** is a $0 digital eBook component. Hiding it from the catalog does not prevent standalone permalink or direct add-to-cart acquisition. An isolated, deactivatable snippet may block **standalone** acquisition **only after** confirming legitimate 2249 bundle component addition still works. Cart-only test 2249 at $299 with both components; no real test orders. Do not change product prices, types, or bundle configuration. **Execution not independently confirmed.**
- **1834** (book and tape, $144.99) remains unchanged; it is not a competing certification package.

## Purchase measurement architecture — do not casually change
- **GTM v29 published**; v28 is rollback via GTM Versions > Publish.
- **Pixel Manager** is the sole GA4 purchase owner (also GA4 add_to_cart and begin_checkout). GTM GA4 purchase tag paused to prevent duplication.
- GTM Google Ads K-Cuts purchase tag fires on custom `l2t_purchase_first_view` from **Code Snippet #8** on eligible legitimate first-view thank-you pages: valid order key, nonstaff, Processing/Completed, under three days, and no prior `_l2t_gtm_purchase_pushed` meta. The timestamp is persisted on the order to suppress replays across sessions.
- Qualifying paid parent IDs: **2249, 2880, 8327**; not $0 component 1873 or 49069. Uses actual WooCommerce order value, currency and transaction ID, with `l2t_is_kcuts`.
- Ads conversion ID **AW-16520820549**, label **Z-m_CNncx6gcEMXu3sU9**, action **7601253977**.
- Controlled test **order 49622**, 2249 at $0 with 100%-off coupon: one Google Ads conversion request (HTTP 200, transaction 49622, value 0 USD), one GA4 purchase via Pixel Manager, course 1589 enrollment successful, no duplicate after reload. Test coupon disabled/drafted, test enrollment removed, order retained. This establishes event dispatch, **not attributed ad conversions**.
- Historical GA4 purchases/revenue were contaminated by old hardcoded $299 values and revisited thank-you pages. **Use actual WooCommerce orders as historical sales source of truth.**
- **Google for WooCommerce Enhanced Conversions setting stays OFF.** Do not connect Ads via this plugin just to turn it on. Enhanced Conversions does not inherently create duplicate purchase events, but any future implementation should be assessed in the existing GTM tag with consent/privacy requirements and no second conversion owner.
- WooCommerce Order Attribution is enabled to capture source information where available. Attribution fields should be interpreted cautiously; no automatic inference of organic traffic.

## October 8 live-order follow-up: 49631
- Claude reported a real **$299** order **49631** around **12:31 ET on October 8**. At about 15:40 ET (3.1 hours later), GA4 Free-form Exploration had **no 49631 transaction row**; the standard 7-day Home chart still ended October 7. Reported exploration events rose from 9,044 to 9,048 while revenue stayed $1,495.00.
- **Absence at 3.1 hours is inconclusive**; do not assert that GA4 is broken, that it will definitely appear, or that source is organic.
- **Oct 9 after 13:00 ET:** check for transaction 49631 exactly once at $299 USD and examine its reported source/medium, without revisiting the thank-you page.
- **Oct 10 at/after 12:31 ET:** if still absent at 48 hours, investigate Pixel Manager purchase path and GA4 diagnostics, without replaying purchase events. No scheduled checks had been created at the time of Claude's report.
- Claude reported appending an addendum to `ORDER_49631_TRACKING_VALIDATION.md` in its own workspace. This GitHub record is not a substitute for that underlying investigation file.

## SEO, authority and mobile
- Certification landing page SEO title reported: **Online Kinesiology Taping Certification | Learn 2 Tape**. Meta description emphasizes $299 offer content: 16 CE hours, NCBTMB Approved Provider, 31 clinical applications and eBook. Product 2249 metadata aligned.
- NCBTMB directory reportedly lists **Andrew Freedman**, provider **451603-11**, course **The K-Cuts Taping System: Online Course**, Home Study, **16.00 CE hours**. Directory listing alone does not establish perpetual current approval. The **CEUL171708 / Approval #171708** seal is **APTA Massachusetts course approval**, reportedly through **January 2027**, **not** the NCBTMB provider number. Claude corrected seal alt text; validate claims and expiry before reuse.
- Shared Elementor Product Inside template **15018** heading changed h2→h1; 2249 reportedly has one H1 and same styling. **Spot-check unrelated products** for duplicate H1 and regressions.
- Rank Math product sitemap excluded 11 published-but-redirecting product URLs, reducing 90→79 with reported 200 responses; products and redirects unchanged. `/sitemap.xml` 301s to `/sitemap_index.xml`; redundant GSC submissions are harmless, **leave alone**. Inspect `/checkout/` and `/a3b/` sitemap inclusion given empty-cart 302 behavior; only safe exclusions if appropriate.
- Isolated reversible **Code Snippet #10** reportedly preloads 60 KB WebP hero (formerly 880 KB JPEG) and reserves badge space on landing mobile; on product 2249 preloads main image and removes gallery JS wait. Product main image was **already eager with fetchpriority=high**; do not claim it had been lazy-loaded.
- Single PageSpeed Insights mobile lab runs: landing LCP **7.4→6.0s**, CLS **0.528→0.339**, score **41→28**, TBT **140→800ms**; product 2249 LCP **12.2→6.6s**, score **56→53**, TBT **220→470ms**. These mixed outcomes are **not a proven net performance gain**. No field INP or repeatability established. Investigate mobile header-logo and cart CLS in isolated low-risk changes; use three comparable runs and medians when feasible. **No broad script deferral or font preload without evidence.**
- Google for WooCommerce emits an extra meta description on some pages alongside Rank Math; low severity, deferred. No Course/FAQPage schema expansion authorized.

## Security and secondary site context
- FormCraft patched 3.9.12→3.9.16 from legitimate source; demo forms reportedly tested. Public matrix form #21 `/live-eval/` disabled/blocked by Code Snippet #7. Avoid reopening without new evidence.
- Tao secondary work: `/services/`→`/book/`, placeholder pages drafted/noindexed, blog link corrected. Do not divert Learn2Tape acquisition work into unrelated Tao cleanup.

## Next commercial gate
1. Confirm reversible withdrawal of 49069 and absence of competing certification CTAs; confirm standalone 1830 cannot be obtained without breaking 2249.
2. Confirm 2249 checkout still shows **$299**, eCourse and digital eBook, correct enrollment and no physical-book promise. Do not place unnecessary live test orders.
3. Recheck 49631 at 24h and 48h thresholds; document GA4 presence, actual value, duplication and source/medium only when observable.
4. Close isolated mobile CLS defects, check template side effects and factual accreditation claims.
5. Review **Google Ads campaign structure, qualified search terms, negative keywords, ad-to-landing message match, budget and break-even economics** before deciding on a controlled Ads restart. Keep Ads **paused** until explicit founder authorization.

## Change control
No secrets, customer personal information or credentials in this record. Preserve GTM v29, Pixel Manager, WooCommerce bundles, LearnDash enrollment, pricing and order history. Changes to product visibility should be reversible; code snippets should be individually deactivatable. This is a **decision and evidence log**, not a repository backup of the live WordPress configuration.
