# Commerce, measurement and contribution audit
Date: October 21, 2026. Read-only inspection; no transactions or production configuration changes.

## Offer evidence
| Channel | Current observation | Scope |
|---|---|---|
| Amazon | https://www.amazon.com/dp/B0GVTZZS99 ; exact title/subtitle, Drew Freedman author, Whitney Lowe foreword; paperback $14.99; In Stock; shipper/seller Amazon.com | Live browser readback |
| Amazon rating | 4.8/5 and 15 global ratings; top link says 15 Reviews | Do not describe 15 as 15 written reviews without reconciling written-review count |
| Amazon fulfillment | Location-dependent Prime/non-Prime delivery and $35 qualifying free-shipping presentation visible | No campaign delivery date/Prime guarantee |
| Signed | Shop $19.99 + $5; Stripe checkout total before address/tax $24.99 | Live Shop and hosted checkout |
| Personalized + Signed | Shop $24.99 + $5; Stripe detail subtotal $24.99, shipping $5, total $29.99 before address-based tax | Live Shop and hosted checkout details |
| Fulfillment | Shop says initial U.S. shipping; both checkouts show United States fixed | Verified current display |
| Handling | Shop FAQ: typically 3–5 business days to leave author; explicitly not carrier delivery estimate | Current policy display, not new campaign promise |
| Inscription | Required “Who should Drew make this out to?”; optional “Anything you’d like Drew to know?” | Personalized checkout displayed fields; no submission |

Shop: https://taoclinicaltouch.com/shop/
Signed checkout: https://buy.stripe.com/aFa3cvaDtapr0LO9gCfUQ00
Personalized checkout: https://buy.stripe.com/bJeeVd26X413dyA1OafUQ01
Bulk inquiry: https://taoclinicaltouch.com/bulk-orders/ (linked from Shop; form not submitted).

Actual path is Shop → Stripe hosted checkout. No cart step observed on this path. WooCommerce inventory, analytics and checkout are not the verified mechanism for these two links. Do not create add_to_cart as a fictitious funnel stage. Begin_checkout means checkout-link click in current source, not a successful payment or confirmed checkout render.

Payment choices displayed include card, Cash App, Klarna and bank; personalized checkout also displayed Amazon Pay; signed mobile express region showed Apple Pay, Link, Klarna and Amazon Pay. Availability depends on device/session and was not exercised. Coupon field/behavior not verified; no discount promised.

## QA coverage and limits
PASS: Shop page loads; two offer CTAs reach matching hosted checkout; personalization input exists; shipping restriction displayed; personalized subtotal/shipping match advertised offer; tracked Shop query renders and persists; phone-width Shop FAQ readable.
PARTIAL: Shop phone inspection at 390×844 covered FAQ region, not full-page checkout usability. Amazon phone-width screenshot retained a wide desktop-like layout in this browser; native mobile experience not certified.
NOT VERIFIED: Successful payments, tax outcome, failed-payment recovery, duplicate-order prevention, confirmations/emails, fulfillment data readback, refunds, coupon behavior, complete mobile path, Stripe webhook status, WooCommerce relationship.
No Pay/Buy, card details, address, email or synthetic order entered.

## Tracking actually found
Live rendered HTML retrieved through WPVibe:
- GTM-PP2CC4D6 and G-BEBQ6ENK69 present. Retired G-FW3PRHTX2P not found in inspected HTML. This is code presence/absence, not GA4 receipt proof.
- Current source emits view_item_list, select_item, begin_checkout, amazon_click, bulk_inquiry_click, faq_open.
- Shop script pushes events to dataLayer and clears prior items to avoid two-item contamination.
- UTM source/medium/campaign/content/term captured in sessionStorage. Despite “First touch wins” comment, incoming UTMs replace stored attribution; semantics are session-local latest tagged entry, not durable first-touch proof.
- Consent defaults include denied analytics/ad storage/ad user data/ad personalization. WPConsent scripts and preferences UI present. Runtime behavior before/after consent and withdrawal was not verified.
- A separate installed attribution script can append a consent-bound client_reference_id to allowed Stripe links and calls same-origin reference/revoke routes. Backend acceptance, retention/deletion and consent behavior not independently exercised.
- Script contains both enabled=true and stale staging/GA4 purchases OFF text. Resolve with server-side configuration and read-only event receipts.
- No fbq/fbevents marker found in returned HTML. GTM-injected Pixel and server-side CAPI could exist; neither absence nor functioning is established.

## Measurement plan
Before activation, inspect authorized Stripe reporting/webhook configuration and GA4 event receipts without creating a live charge. Reconcile a permitted existing transaction with payment status, amount, shipping, refunds and stable order ID. If using synthetic verification, use isolated test mode with separate test endpoints and disabled notifications under an approved plan; do not switch production into test mode.

Count a purchase only after verified successful payment. Reconcile server-side events idempotently by transaction ID; if browser and server Meta events both exist, use matching event_name/event_id and confirm deduplication. Gate optimization on actual eligible Purchase delivery and Events Manager restrictions, not a tag's presence. Do not silently install CAPI or change consent.

Exclude inscription/free-text/contact/payment information from advertising and analytics payloads. No health-associated customer or patient information. Validate permitted event parameters and URLs before sending.

| Metric | Authoritative source / status |
|---|---|
| Spend, impressions, reach, clicks, CTR, CPC | Meta Ads Manager export after authorized activation; currently unavailable |
| Landing-page views | GA4/network receipt after consent verification; current event delivery unknown |
| Checkout intent | Current begin_checkout event contract; not completed purchase |
| Add to cart | Not applicable to observed direct Stripe path; do not fabricate |
| Paid orders, net revenue, refunds, fees | Stripe/operational ledger; not yet inspected |
| Meta purchases/CPA | Platform attribution only, after validated event eligibility |
| Amazon attributed visits/orders | Amazon Attribution account if enabled; account access unverified |
| Creative contribution | Order-level reconciled revenue minus actual variable costs and spend; not yet available |

Maintain one row per date/channel/campaign/ad/creative/destination with spend, clicks, LPV, checkout clicks, paid orders, refunded orders, net product revenue, shipping collected, variable costs and contribution. Separately label Meta-attributed, GA4-attributed and reconciled orders; do not add overlapping attribution counts.

Amazon official product documentation includes eligible KDP authors, but this does not prove Drew’s account eligibility or enabled access:
https://advertising.amazon.com/solutions/products/amazon-attribution .
Use account-generated links per creative/destination; ordinary UTMs do not create Amazon purchase attribution.

## Proposed link schema
Campaign = tao_book_sales_001.
Paid Shop:
https://taoclinicaltouch.com/shop/?utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign=tao_book_sales_001&utm_content=creative_03_signature&utm_term={{adset.id}}
Record immutable campaign/ad/ad-set IDs in reporting. site_source_name may yield platform abbreviations; document mapping to facebook/instagram. Use explicit platform values if separate ads are configured.
Organic: utm_source=instagram or facebook; utm_medium=organic_social; same campaign; creative token plus format/version in content. Instagram feed requires a verified bio destination; caption URLs are not assumed clickable. Stories require native link verification. No bio changes made.
Example tested: explicit instagram/paid_social/creative_03_signature query loads Shop without breaking rendering. Stripe paid-order attribution and query transfer remain unverified; never claim end-to-end UTM PASS.

## Unit economics — fill with confirmed costs before spend
Sales tax is excluded from revenue. Shipping collected is not profit.
Signed pre-ad contribution = 19.99 + 5 − author copy landed cost − packaging − actual postage − processor fees − fulfillment labor − expected returns/damage cost.
Personalized = 24.99 + 5 − same costs − inscription labor.
Amazon = actual net royalty per unit from KDP statement minus any additional variable costs. Do not substitute 14.99 retail.
For labor, minutes ÷ 60 × chosen hourly opportunity cost. Include inscription plus pick/pack/dispatch time. Processor fees must come from the actual account/method, not generic Stripe pricing.

Sustainable CAC = pre-ad contribution − desired retained contribution.
| Illustrative pre-ad contribution, not verified economics | Break-even CAC | CAC retaining $3/order |
|---:|---:|---:|
| $4 | $4 | $1 |
| $8 | $8 | $5 |
| $12 | $12 | $9 |

For example, at $0.60 CPC and $5 target CAC, click-to-order conversion must be 12%; at $9 target CAC it must be 6.67%. These are sensitivity calculations, not CPC or conversion forecasts. Low book margins make cold paid acquisition a hypothesis to test, not a promised growth engine.

Needed inputs: latest KDP royalty and author-copy landed cost, packaging/postage, Stripe method-specific fees, fulfillment/inscription minutes and hourly value, refund/damage experience. No verified CAC ceiling or ROAS can yet be assigned.

