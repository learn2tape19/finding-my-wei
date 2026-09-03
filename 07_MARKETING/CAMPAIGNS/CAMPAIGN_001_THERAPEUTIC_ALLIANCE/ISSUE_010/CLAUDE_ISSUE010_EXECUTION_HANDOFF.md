# CLAUDE — ISSUE 010 EXECUTION HANDOFF

## Founder directive
Issue 010 editorial is authored under Founder approval. Once locked, execute only the approved package. **NO COPYWRITING. NO REDESIGN. NO NEW ASSETS. NO CONTENT INTERPRETATION.**

## Editorial authority — the Issue 010 architecture rule
`ISSUE010_MASTER_COPY.md` is authoritative for each day's editorial argument. `ISSUE010_STORY_COPY_LOCK.md` derives from that same daily argument. Feed, Story, Blog, and Email may adapt presentation for their medium; they may **not** create independent editorial spines.

> **Why this rule exists.** Issue 009 carried two competing spines — the Master Copy concepts and a separately-titled Story spine. Feed artwork was generated from the Story spine, so Wednesday, Thursday, and Friday feeds argued a different point than their own approved captions. All three required replacement artwork mid-execution. Before any Issue 010 artwork is commissioned, confirm each day's feed headline against that day's Master Copy Social line.

## Preflight
1. Confirm canonical repo/worktree and clean execution branch.
2. Confirm all 30 files in `APPROVED_ASSETS/` and validate `ISSUE010_CHECKSUMS.sha256` (native `shasum -a 256 -c` from the packet root).
3. Confirm exact pixel dimensions from `ISSUE010_ASSET_MANIFEST.md`.
4. Use `ISSUE010_STORY_COPY_LOCK.md` as Story-copy authority.
5. Confirm America/New_York timezone and the exact Founder-approved calendar mapping. **The Sept 7 Labor Day question must be resolved before scheduling.**
6. Confirm production Buffer credential and exact Instagram/Facebook channel identities before mutation.
7. Duplicate-check existing scheduled/published objects before creating anything.
8. Verify every media URL anonymously — HTTP 200, correct dimensions, byte-identical SHA-256 — before referencing it in Buffer.
9. If credentials or destination identity fail, STOP and record the limitation. Do not route around it.

## Authorized executable subset (once assets and dates are approved)
- Instagram + Facebook feed posts using the locked daily Social copy and `*_FEED_1080x1350.png`.
- Three Instagram Stories per day using the exact Story 1/2/3 assets and schedule.
- **No Facebook Stories.**

## Holds
- **Blog publication:** HOLD until canonical article body is Founder-approved. Do not write one during execution.
- **Email campaign:** HOLD until body copy, CTA, list IDs/send pattern, and working Brevo execution path are Founder-approved/available. Do not create duplicate campaigns or infer missing configuration.

## Accessibility
Every image object requires objective alt text written from the actual rendered artwork — describing layout and readable text, not marketing language. Issue 009 was the first issue shipped with alt text on every object; that is now the standard, not an improvement.

## Evidence required per mutation
Record platform, object ID, scheduled/published timestamp, asset filename, SHA-256, copy source, and independent verification result.

## Repo closeout
Commit only intended Issue 010 changes/evidence, push, verify remote HEAD equals local HEAD, and report commit SHA plus unresolved platform limitations. Stop for Founder review.

## Known operational conditions
- Buffer has no media upload tool. Assets must be public HTTPS URLs; stage to the taoclinicaltouch.com WordPress media library first.
- Uploading under an existing filename produces a WordPress `-1` collision suffix rather than an overwrite. Reference the resulting URL, and never delete the prior media item without explicit Founder instruction.
- The site WAF rejects the default python-urllib user agent; send a browser/curl UA.
- Large Story PNGs (~2.3 MB) can break the connection mid-upload. Always re-query WordPress and byte-compare before retrying, so a dropped-but-succeeded POST cannot create a duplicate.
