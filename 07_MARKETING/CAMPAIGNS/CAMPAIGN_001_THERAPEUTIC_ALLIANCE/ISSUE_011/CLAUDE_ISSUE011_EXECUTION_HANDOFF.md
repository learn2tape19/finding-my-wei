# CLAUDE — ISSUE 011 EXECUTION HANDOFF

## Founder directive
Issue 011 editorial is Founder-supplied. Execute only the approved package. **NO COPYWRITING. NO REDESIGN. NO NEW ASSETS. NO CONTENT INTERPRETATION.**

## Gate order — do not collapse

**Editorial authority → Visual authority → Execution authority.**

**Status: FOUNDER APPROVED — EDITORIALLY LOCKED**

| Gate | Status |
|---|---|
| Gate 0 — Editorial Architecture | **CLOSED / FOUNDER APPROVED** |
| Gate 1 — Editorial Completeness | **CLOSED / FOUNDER APPROVED** |
| Visual Production | **HOLD — NOT YET AUTHORIZED** |
| External Execution | **HOLD — NOT AUTHORIZED** |

Editorial copy is persisted verbatim and closed before visual production begins. No artwork exists — asset manifest, visual brief, checksum authorities, `APPROVED_ASSETS/`, and `SOURCE_APPROVED/` are deferred to the Visual Production Gate by design. No WordPress, Buffer, or Brevo objects exist.

> **Founder approval is not publication authority.** Approval of copy establishes editorial completeness only. Canonical persistence is not publication authority either. Each gate is separate and requires its own explicit Founder authorization. Lesson carried forward from Issue 010.

## Editorial authority
`ISSUE011_MASTER_COPY.md` is authoritative for each day's editorial argument and for platform caption copy. `ISSUE011_STORY_COPY_LOCK.md` derives from that same daily argument. Feed, Story, Blog, and Email may adapt presentation for their medium; they may **not** create independent editorial spines.

Canonical bodies:
- Weekly article — `ISSUE011_CANONICAL_BLOG_ARTICLE.md`
- Issue-level email — `ISSUE011_EMAIL_COPY.md`

All four are Founder-supplied verbatim. Do not rewrite, improve, summarize, normalize, or creatively extend any of them during execution.

## Visual doctrine

Issue 011 returns to the **established Founder-approved visual system and the canonical natural-water ripple treatment** per `ADOBE_BRAND_MANIFEST.md` — Deep Clinical Navy `#182633`, Antique Gold `#B8860B`, Charcoal `#3A3A3A`, Warm Ivory `#F7F4EE`; Cormorant Garamond editorial serif, Source Sans Pro supporting.

**The Issue 010 gold 道 / TAO character and gold brush-circle / ensō treatments do NOT carry forward.** They were a Founder-accepted visual exception for **Issue 010 only** — non-canonical and non-precedent. Neither may be introduced in Issue 011 unless separately and explicitly Founder-approved **before** visual production. Any proposed symbol, icon, character, decorative mark, motif, or brand device requires Founder approval before visual production.

Before commissioning artwork, confirm each day's feed visual copy against that day's Master Copy caption. Issue 010 shipped with feed artwork built from a different spine than its captions and required three replacement assets mid-execution.

## Preflight (Gate 3)
1. Confirm canonical repo/worktree and clean execution branch.
2. Confirm all 30 files in `APPROVED_ASSETS/` and validate the checksum authority natively (`shasum -a 256 -c` from the packet root).
3. Confirm exact pixel dimensions from the asset manifest.
4. Use `ISSUE011_STORY_COPY_LOCK.md` as Story-copy authority.
5. Confirm America/New_York and the exact Sept 14–18, 2026 calendar mapping; reconcile against the current date before creating any object and report any slot already past.
6. Confirm production Buffer/WordPress/Brevo credentials and exact channel, sender, and list identities before mutation.
7. Duplicate-check existing scheduled/published objects before creating anything.
8. Verify every media URL anonymously — HTTP 200, correct dimensions, byte-identical SHA-256 — before referencing it.
9. If credentials or destination identity fail, STOP and record the limitation. Do not route around it.

## Authorized executable subset (once assets and dates are approved)
- One WordPress weekly article — Monday 7:45 AM ET.
- Instagram + Facebook feed posts using the locked daily captions and the day's feed asset — 8:00 AM ET.
- Three Instagram Stories per day — 9:00 / 11:00 / 1:00 PM ET.
- One Brevo issue-level email — Monday 10:00 AM ET, CTA to the already-live weekly article.
- **No Facebook Stories.**

## Accessibility
Every image object requires objective alt text written from the **actual rendered artwork** — describing layout and readable text, not marketing language, and not the copy lock's hypothetical artwork. This is the standard, not an improvement.

## Evidence required per mutation
Record platform, object ID, scheduled/published timestamp, asset filename, SHA-256, copy source, and independent verification result.

## Repo closeout
Commit only intended Issue 011 changes/evidence, push, verify remote HEAD equals local HEAD, and report the commit SHA plus unresolved platform limitations. Stop for Founder review.

## Known operational conditions (carried forward)
- **Buffer has no media upload tool.** Assets must be public HTTPS URLs; stage to the taoclinicaltouch.com WordPress media library first.
- **WordPress filename collisions** produce a `-1` suffix rather than an overwrite. Reference the resulting URL; never delete a prior media item without explicit Founder instruction.
- **The site WAF** rejects the default python-urllib user agent; send a browser/curl UA.
- **Large Story PNGs (~2.3 MB)** can break the connection mid-upload. Re-query WordPress and byte-compare before retrying so a dropped-but-succeeded POST cannot create a duplicate.
- **The WordPress site timezone is UTC.** Schedule via `date_gmt` so the real-world moment is correct; wp-admin will display the UTC time. Do not change the site timezone.
- **The site emits no Open Graph tags.** Featured images attach correctly but external link previews will not use the designated OG asset. Site-wide condition.
- **Brevo exposes `create_email_campaign` only.** There is no `update_email_campaign` and no `send_email_campaign`. A created campaign cannot be edited or rescheduled through this surface — the creation call must be correct first time; Founder dashboard action is the only correction path.
- **Brevo sender contract:** `sender.email` and `sender.id` cannot both be sent. Pass `id` with an explicit `name`.
