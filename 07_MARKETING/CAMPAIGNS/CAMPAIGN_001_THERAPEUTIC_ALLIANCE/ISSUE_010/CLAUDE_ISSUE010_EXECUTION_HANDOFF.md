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

## Blog and Email status
- **Blog body:** Founder-approved and persisted verbatim at `ISSUE010_CANONICAL_BLOG_ARTICLE.md`. **No longer HOLD.** Do not rewrite it during execution.
- **Blog publication:** **NOT AUTHORIZED.** Separate Founder gate. WordPress out of scope.
- **Email body:** Founder-approved and persisted verbatim at `ISSUE010_EMAIL_COPY.md`. **No longer HOLD.** Do not rewrite it during execution.
- **Email campaign creation/scheduling:** **NOT AUTHORIZED.** Separate Founder gate. Brevo out of scope; list IDs and send pattern still not established.

Editorial completeness is not publication authority. Do not collapse these gates.

## ISSUE 010 — VISUAL EXCEPTION / NON-PRECEDENT

The Issue 010 visual set contains two decorative elements introduced during visual generation: a gold **道 / TAO character treatment** and a gold **brush-circle / ensō-style treatment**. **These are NOT established canonical Tao visual branding.**

Founder accepted them for **ISSUE 010 — POSSIBILITY ONLY**. Do not remove them from Issue 010, and do not regenerate or modify any Issue 010 image because of their presence.

Acceptance does **not** establish either treatment as canonical branding, does **not** authorize reuse in Issue 011, does **not** modify established Tao visual doctrine, and does **not** supersede previously approved visual authority.

**Beginning with Issue 011**, neither treatment may be introduced unless separately and explicitly Founder-approved *before* visual production. Any proposed symbol, icon, character, decorative mark, motif, or brand device requires Founder approval before visual production. Where a recurring Tao visual identifier is required, return to the established Founder-approved visual system and the canonical natural-water ripple treatment, unless a later Founder directive explicitly supersedes it.

**Classification:** FOUNDER-ACCEPTED VISUAL EXCEPTION · NON-CANONICAL · NON-PRECEDENT · ISSUE 010 ONLY. Full record in `ISSUE010_ASSET_MANIFEST.md`.

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
