# ISSUE 016 — PRODUCTION BRIEF (DRAFT / GATE 0)

**Created:** October 10, 2026
**Campaign:** CAMPAIGN_001_THERAPEUTIC_ALLIANCE
**Proposed publication week:** October 19–23, 2026 (America/New_York)
**Status:** EDITORIAL DISCOVERY — NOT APPROVED FOR PUBLICATION

## Starting point
Issue 015 (Restraint) is scheduled and its final reconciliation closed. Issue 016 must be a new, distinct installment of the therapeutic-alliance arc. No Issue 016 canonical article or approved theme was located in the repository during initial search.

## Gate 0 — editorial direction (Founder decision required)
- Confirm the central clinical question and theme for Issue 016.
- Verify continuity with Issues 013–015 and the broader campaign arc before drafting.
- Select a specific clinical scene or decision point; avoid recycling Issue 015's restraint, dosing, reassessment, and completion arguments.
- Preserve the author's clinical voice, measured claims, and distinction between observation and mechanistic inference.

## Gate 1 — manuscript and campaign copy
- Draft article for Founder review; mark DRAFT until approved.
- Build five-day Monday–Friday arc with daily feed/landscape copy and three story panels per day.
- Founder approves and locks the article, all platform copy, story text, and visual direction before asset generation or scheduling.

## Gate 2 — assets
- Create/approve 25 original assets: five Feed 1080×1350, five Landscape 1200×628, fifteen Stories 1080×1920.
- Upload to WordPress media and independently reconcile public URLs, dimensions, SHA-256, and alt text.

## Gate 3 — WordPress
- Prepare the approved article and scheduled post. Proposed Monday Oct 19 at 7:45 AM America/New_York, subject to Founder approval.
- Verify wp-admin displayed schedule and site timezone; do not infer publication time from an ambiguous REST timestamp.
- Confirm canonical URL, excerpt, featured image, article body, category and metadata.

## Gate 4 — Buffer
- Duplicate-check first; use current Buffer adapter and latest Founder-approved destination precedent.
- Proposed pattern: 25 content items / 45 channel posts across Oct 19–23, 2026, with Feed/Landscape 8:00 AM, Story 1 9:00 AM, Story 2 11:00 AM, Story 3 1:00 PM ET. Founder must approve schedule and destinations before mutation.
- Verify every post by independent ID readback and a separate window query. No captions or hashtags invented during deployment.

## Gate 5 — Brevo
- Inspect any existing Issue 016 campaign by ID and full content before creating or updating; campaign name is not proof of correct body.
- Use approved sender, audience, hero, subject, preheader, CTA, and body. Proposed Monday 10:00 AM ET send, subject to Founder approval.
- Brevo MCP campaign tools can read/create but not update or schedule existing drafts. Use authorized REST API for existing-campaign writes, with credentials held outside GitHub, never printed/logged/committed. Do not create a duplicate to evade a write limitation.
- Independently read back all fields and queued time before marking PASS.

## Gate 6 — reconciliation and closure
- Commit machine-readable Buffer objects, Buffer receipt, Brevo receipt, media manifest, and final reconciliation.
- Founder checks wp-admin publish hour and Brevo From name where API evidence is insufficient.
- Close only on documented PASS, with zero unexplained exceptions.

## Authority boundary
This brief authorizes **planning and drafting only**. It does not authorize WordPress, Buffer, or Brevo production mutations. Stop on conflicts, missing approvals, or changed system state. No credentials in repository files.
