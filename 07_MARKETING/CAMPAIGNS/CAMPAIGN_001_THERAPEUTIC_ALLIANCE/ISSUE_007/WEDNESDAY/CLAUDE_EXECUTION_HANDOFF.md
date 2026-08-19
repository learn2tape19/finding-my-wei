# Issue 007 — Wednesday Claude Execution Handoff

**Publication:** The Tao of Clinical Touch  
**Issue:** 007 — Permission Over Time  
**Day:** Wednesday  
**Purpose:** Controlled handoff from editorial production to Foundry/Claude execution  
**Current status:** READY FOR FOUNDER CONTENT REVIEW; EXTERNAL EXECUTION LOCKED UNTIL FINAL VISUAL ASSETS ARE FOUNDER-APPROVED

---

## 1. Governing read order

Before taking any execution action, read in this order:

1. `../FOUNDER_APPROVAL_GATE_0.md`
2. `../../TAO_EDITORIAL_ARC_REGISTER.md`
3. `WEDNESDAY_CANONICAL_SOURCE.md`
4. `WEDNESDAY_COPY_PACKAGE.md`
5. `WEDNESDAY_VISUAL_PRODUCTION_BRIEF.md`
6. Current Finding My Wei publishing/editorial governance
7. FREEDMAN-FOUNDRY execution packet, content state machine, preflight, receipt, and current Buffer capability records

If any later file conflicts with Founder-approved source material, STOP and report the conflict. Do not silently repair doctrine or rewrite approved copy.

---

## 2. Editorial continuity lock

Issue 007 progression is:

- Monday: **PERMISSION IS NOT A QUESTION**
- Tuesday: **THE BODY CAN CHANGE ITS ANSWER.**
- Wednesday: **THE ANSWER MAY CHANGE BEFORE IT IS SPOKEN.**

Wednesday must preserve this distinction:

> A nonverbal shift is information that may justify making room for an updated answer. It is not proof of discomfort, withdrawal, refusal, fear, or any other internal state.

Do not rewrite Wednesday into generic consent education, body-language decoding, or a list of red flags.

---

## 3. Canonical content

The canonical Wednesday article is:

`WEDNESDAY_CANONICAL_SOURCE.md`

All platform copy must remain derivative of that source.

Do not generate a parallel article.

---

## 4. Approved destination package

### Tao Facebook

Use the exact Facebook copy from `WEDNESDAY_COPY_PACKAGE.md`.

Canonical Buffer channel ID:

`6a3eb95f5ab6d2f106763fc9`

### Tao Instagram

Use the exact Instagram copy from `WEDNESDAY_COPY_PACKAGE.md`.

Canonical Buffer channel ID:

`6a3eb89f5ab6d2f106763ca0`

### Explicitly unauthorized destination

Personal Instagram `drewdog19` is outside Tao automation authority and must not be selected.

---

## 5. Required visual assets

Claude must confirm these final Founder-approved files exist before creating an execution packet:

- `ISSUE007_WED_FEED_1080x1350.jpg`
- `ISSUE007_WED_STORY_FRAME01_1080x1920.jpg`
- `ISSUE007_WED_STORY_FRAME02_1080x1920.jpg`
- `ISSUE007_WED_STORY_FRAME03_1080x1920.jpg`
- `ISSUE007_WED_BLOGOG_1200x628.jpg`
- `ISSUE007_WED_EMAILHEADER_1200x627.jpg`

Do not substitute mockups, contact sheets, crops, temporary renders, or differently named assets.

If any required asset is missing or not Founder-approved: `BLOCKED`.

---

## 6. Pre-execution QA

Before constructing any external execution packet, verify:

### Editorial
- headline is exact;
- platform copy is exact;
- no unsupported neuroscience claims were added;
- no nonverbal cue is treated as proof of internal meaning;
- Wednesday advances rather than repeats Monday/Tuesday;
- no invented testimonial, quote, URL, publication status, or clinical claim.

### Visual
- native dimensions match filename;
- correct Tao Issue 007 visual identity;
- one ripple only;
- no ripple drip;
- professional draping;
- credible external face cradle geometry;
- no malformed hands/anatomy;
- visual does not depict distress as a shorthand for permission change.

### Execution
- `BUFFER_API_KEY` resolves through the current Foundry credential boundary;
- canonical Buffer account and organization independently verify;
- destination channel independently verifies;
- personal Instagram remains excluded;
- idempotency key is unused;
- authority remains BUILD_DRAFT only.

---

## 7. Execution packet identities

Use separate idempotency keys by destination and asset type. Recommended canonical keys:

### Facebook feed draft
`TAO-ISSUE007-WED-FB-FEED-001`

### Instagram feed draft
`TAO-ISSUE007-WED-IG-FEED-001`

Stories are NOT automatically authorized merely because the feed is authorized. If current Foundry/Buffer execution architecture has not separately verified Instagram Story draft behavior, mark Story external execution `NOT_RUN` and preserve the Story assets for manual or future authorized execution.

Blog/WordPress and Brevo email similarly require their own current capability + authority verification. Do not infer authorization from Buffer feed capability.

---

## 8. Current external authority ceiling

For Buffer:

**BUILD_DRAFT only.**

Allowed only after all Founder approval/preflight conditions are satisfied.

Not authorized:
- publish;
- publish now;
- queue;
- schedule;
- delete;
- cancel;
- Instagram personal-account mutation;
- silent retry after ambiguous write.

Content approval is not publication authority.

---

## 9. Buffer execution sequence

For each separately authorized Tao destination:

1. Resolve idempotency ledger.
2. Independently verify Buffer account.
3. Independently verify canonical organization.
4. Independently verify exact Tao channel.
5. Confirm asset and copy match Founder-approved package.
6. Execute exactly one `createPost` mutation with `saveToDraft: true`.
7. Do not retry an ambiguous write.
8. Independently fetch the created post.
9. Verify created/fetched IDs match.
10. Verify state is exactly DRAFT.
11. Verify destination and copy/media correspond to the execution packet.
12. Only after independent verification, persist execution receipt.
13. STOP for Founder review.

If timeout/ambiguous mutation occurs, return `AMBIGUOUS_WRITE`, escalate, and do not issue a second mutation.

---

## 10. Founder review return

Return one concise execution report containing:

- repository branch + commit SHA used as source;
- asset filenames and hashes used;
- exact platform destination(s);
- exact idempotency key(s);
- preflight result;
- mutation count;
- created Buffer post ID(s);
- independently fetched post ID(s);
- verified DRAFT state;
- receipt path/record;
- anything `NOT_RUN` and why;
- confirmation no publish/queue/schedule/delete action occurred.

STOP after verified drafts. Do not advance authority.

---

## 11. Execution release condition

Claude does not yet have external mutation authority merely from the existence of this handoff.

External BUILD_DRAFT execution becomes authorized only when Founder explicitly states that the final Wednesday content and rendered visual assets are approved for the Foundry draft test.
