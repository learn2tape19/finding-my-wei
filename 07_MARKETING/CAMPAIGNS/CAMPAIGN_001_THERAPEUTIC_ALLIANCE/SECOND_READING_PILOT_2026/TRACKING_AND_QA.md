# Tracking, QA and approval record

**No configuration changes, test submissions, test emails or platform drafts were executed.** Proposed instrumentation and release checks below are pending.

## Attribution contract

Campaign slug: `tao_second_reading_2026_pilot`. `utm_source` = facebook, instagram or brevo. `utm_medium` = organic_social or email. `utm_content` = `sr01_orig001_mon_primary`, `sr01_orig001_wed_practice`, `sr01_orig001_fri_join`, `sr01_orig001_mon_story` or `sr01_orig001_mon_bio`, with correct pilot/original pair for every week. Instagram sources add the account suffix in content (`_tao`, `_drew`) so both accounts can be distinguished. Use URL-encoded generated links in `tracked_links.csv`; never put email addresses, patient details or recipient identifiers in UTMs.

External links go to the preserved original page or existing `/join/`. Do not tag internal navigation with new UTMs; retain original campaign context through existing attribution where supported. Verify that Brevo rewriting and redirects retain query parameters before release. If an Instagram bio can expose only one active destination, approve a weekly original-article link Monday–Thursday and join link Friday–Sunday, and log changes; existing unrelated bio promotions require Drew's review before replacement. No profile changes have been made. Stories use a separate tracked link only if the native field exists and is verified. Otherwise record “bio route; Story click attribution unavailable.”

## What to count

| Metric | Source of truth | Definition / denominator |
|---|---|---|
| Eligible audience | Brevo list 64 at release | Subscribed, permissioned, unsuppressed contacts; record exact count before send |
| Delivered | Brevo campaign report | Successful deliveries, not selected list size |
| Reported clicks | Brevo/Buffer | Keep raw counts and provider definition; never label human readers without validation |
| Unique article clickers | Brevo link-level report, bot-filtered if supported | Unique contacts clicking the original-article CTA / delivered; exclude unsubscribe and preference links; if filtering unavailable mark raw/unknown |
| Substantive responders | Manual operator log | Unique people with an issue-related reply, comment or direct message; exclude own/test replies and automated responses; dedupe only where identity is legitimately known |
| New confirmed subscribers | Brevo list membership and opt-in evidence | New confirmed Tao contacts in pilot window, excluding pre-existing, test, imported or suppressed contacts; source known / unknown separately |
| Article users and engagement | GA4 path + session campaign | Original path with pilot campaign, consented observable traffic; cannot represent all actual readers |
| Saves/shares | Platform/Buffer | Per placement, separately; not unique humans across platforms |
| Sales | Verified order/payment record plus available attribution | Report matched attributable orders separately from total orders; no inferred Amazon orders |

No fingerprinting, cross-platform identity matching or uploading reader identities into GA4. Manual reply log stores an internal nonpublic reference, channel, date, SR ID and theme; put only aggregates in the repository. Ask before quoting a person's reply publicly. AI may draft responses after authorization; this plan authorizes no outbound replies.

## Measurement readiness

Use existing GA4 page_view/user_engagement/scroll reports where verified. Proposed additional events, only after explicit implementation approval: `tao_subscription_confirmed` from a real confirmed subscription state (not a confirmation-page load), `tao_book_outbound_click` and a bounded article engagement event if needed. Do not call a click a lead or a purchase. Audit existing tags/consent before adding events; one owner per event to prevent duplication. No GTM/GA4 production edits are needed to draft or run a basic UTM-and-manual-reply pilot.

Before release, verify property timezone and align all comparison windows; it was not confirmed in this audit. Capture GA4 internal/developer traffic policy and consent effects without assuming filters are active. Keep operator QA traffic in its own record and flag contaminated windows; do not retroactively erase valid observations. Native dashboard rates remain labeled as platform rates.

## Collection windows and evaluation

Take baseline snapshot **Oct 25**, before the pilot; refresh since this audit is Oct 14. Record eligible list size, channel followers, existing queue collisions and prior 28-day issue-only outcomes if accessible. Capture each pilot item at **+24 hours** (operational check) and **+7 days** (weekly comparison), plus final review **Nov 23**. No automation has been created.

Use four equal seven-day exposure windows from each Monday 00:00 through Sunday 23:59 local time for calendar reporting; separately retain exact send-relative +7-day captures. DST ends between week 1 and week 2, so use timezone-aware dates. Compare like channels and formats. Do not compare seven-person pilot rates against 11,000-person legacy sends as a causal experiment. With this sample, no A/B significance claim is warranted.

**Proposed learning thresholds, for Drew's review; not evidence-based forecasts:**

- Continue to the next four originals if the four-week pilot produces at least **3 unique substantive responders** or **5 new confirmed Tao subscribers**, with no unresolved audience, delivery or approval problem. At least one signal should come from someone outside production/testing. If identity cannot be deduplicated, report the lower verified count and channel counts separately.
- If observed reach remains very small (for example fewer than 20 attributable article sessions across the pilot), classify the result as **distribution inconclusive**, not editorial failure; improve the consented discovery route before producing twelve more weeks.
- If delivery and reach occur but there are no substantive responses and no confirmed new subscribers, revise the hook/question/placement and rerun a bounded test rather than repeat the entire series unchanged.
- Pause the next unreleased send for any confirmed audience-permission error, broken unsubscribe/CTA, sender-authentication failure or unresolved provider block/complaint. Report the specific failure and fix before further release. A single unsubscribe in a seven-person cohort is a reason for human review, not a reliable population rate.
- Record production time; proposed cap is **6 operator hours/week** for this lean pilot after setup. Exceeding it triggers a scope review rather than silent expansion. This is a planning budget, not measured historical effort.

Book orders remain a secondary observation. There is no spend, paid campaign or ROAS target in this pilot.

## Approval ledger — bounded SR01 direction approval recorded

| Gate | Required evidence | Approver / status |
|---|---|---|
| 0: Direction | Exact original mapping, new purpose, cadence exception, format choice, audience boundary | SR01 anchor/emphasis and presented cadence APPROVED by Drew Oct 14; see SR01_APPROVAL_RECORD.md. Final format/audience details remain pending. SR02–SR04 direction pending |
| 1: Scientific | Review old/new distinction; flag historical overstated physiology; confirm new copy does not diagnose or replace consent | Named scientific reviewer — PENDING |
| 2: Editorial | Distinct reviewer; voice, continuity, source fidelity, no invented personal history | Named editorial reviewer — PENDING |
| 3: Founder copy | Exact reflection, subject, preheader, caption, Story and CTA versions | Drew — PENDING |
| 4: Rendered assets | Actual pixels, proofreading, legibility, clipping, image/context review and exact manifest hashes | Operator QA + Drew visual approval — PENDING |
| 5: Platform drafts | Account/site/list identity, sender/reply-to, recipient count, original links, duplicate/object reconciliation | Operator — NOT CREATED |
| 6: Release | Explicit schedule/send authority naming versions, channels, dates/times and audience | Drew — NOT AUTHORIZED |
| 7: Delivery | IDs, status, public URL, sent/delivery receipts; limits stated | Operator — FUTURE |
| 8: Reflection | Seven-day data and Nov 23 decision, lesson/prevention record | Operator + Drew — FUTURE |

No gate is PASS because a checklist exists. Do not fabricate reviewer independence, Founder approval or checks not performed.

## Operator QA checklist

- [ ] Match SR01→001, SR02→002, SR03→003, SR04→004 throughout copy, images, links, dates and filenames.
- [ ] Preserve original WP IDs, bodies, dates, titles, slugs, canonicals and approved asset bytes. Hash snapshots before and after any future permitted operations; no overwrite is part of this plan.
- [ ] Anonymous original-page GET returns expected page, correct title and canonical; follow redirects and record destination. External web reader failed to access pilot originals during this audit, so this remains pending despite authenticated WP publish state.
- [ ] Verify public join page and existing opt-in destination; no synthetic/live submission without separate authorization.
- [ ] Word-by-word proof full email/mobile preview, social truncation and Story order, old-versus-new labels, correct original issue number and original title.
- [ ] Validate all 36 proposed asset masters, exact dimensions independently, no stretching/clipping; original featured-image metadata is not final pilot QA.
- [ ] Reconcile 48 Buffer objects, 4 email campaigns, 0 new WP posts against calendar after approved draft creation; no unintended duplicates. Do not run old five-day completeness check unchanged for this reduced pilot.
- [ ] Confirm list 64 membership, suppressions and consent; no cross-brand expansion. Verify sender/reply-to and functional unsubscribe.
- [ ] Verify Monday 8/9/10 AM plus Wed/Fri 8 AM, America/New_York; Oct 26 EDT (UTC−04), Nov dates EST (UTC−05).
- [ ] Verify native Story link fields, not merely link text. Independently approve bio changes if necessary.
- [ ] Save exact-version preview/screenshots before release; final release evidence separate from draft evidence.
- [ ] After authorized scheduling, read back destination, copy, asset, time, timezone, status and object ID where available. Label queue-only verification accurately.
- [ ] After execution, verify actual public posts and sent email report. Scheduled does not mean delivered; page views do not mean confirmed subscribers or sales.
- [ ] Preserve approved source, originals, hashes, receipts, outcome limits and lesson in canonical repo; push/remote-verify only the authorized final package and report actual state.

## Verification performed in this task

PASS: original source discovery and current WP metadata/content/media reads; repo HEAD identified; four Monday dates and timezone conversions generated; tracked links generated without PII; original-to-pilot mapping; local file integrity inventory. No source/approved original was modified.

NOT PERFORMED: independent scientific/editorial review; Founder approval; new visual rendering/pixel QA; anonymous live-page/canonical proof; platform draft previews; audience eligibility audit; test send; form submission; production event validation; final schedule/readback; publication; delivery or sales reconciliation.
