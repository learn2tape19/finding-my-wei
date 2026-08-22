# Publishing Dependency Sequence

**Program:** The Tao of Clinical Touch — Therapeutic Alliance Campaign  
**Effective:** Issue 009 onward  
**Authority:** Founder decision, August 22, 2026  
**Status:** CANONICAL PRODUCTION ARCHITECTURE

## Purpose

The public editorial calendar remains Monday through Friday, but production must no longer be built strictly in publication order.

Issue 008 execution exposed an upstream dependency: Wednesday's canonical WordPress article establishes the permalink required by downstream email and post-publication social calls to action. Therefore the production sequence must resolve the canonical article destination before downstream promotional copy is finalized or scheduled.

## Editorial / Publication Sequence

The audience-facing sequence remains unchanged:

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday

This sequence governs the narrative arc and publication experience. It does **not** govern production dependency order.

## Canonical Production Dependency Sequence

For Issue 009 onward:

1. **Lock the weekly thesis and Monday-Friday editorial arc.**
   - Establish the complete narrative progression before platform derivatives are finalized.

2. **Build the Wednesday canonical WordPress article first.**
   - Finalize canonical title, slug, article body, metadata, CTA, and approved Blog/OG visual.
   - Create/schedule the WordPress object early enough to establish its canonical permalink before downstream promotional assets are finalized.
   - The article does not need to be publicly live for its canonical destination to be established.

3. **Establish the canonical destination layer.**
   - Record one authoritative `ARTICLE_URL` / canonical permalink for the issue.
   - Downstream platforms consume this destination; they do not invent or reconstruct URLs independently.

4. **Build the Wednesday email from the canonical article destination.**
   - Email CTA must use the established canonical permalink.
   - Email remains scheduled after the WordPress article publication time.

5. **Finalize social copy and CTA behavior.**
   - Monday and Tuesday may operate as lead-in content before the article publishes.
   - Wednesday-Friday social copy is finalized only after the canonical article destination exists.
   - Facebook may use the direct canonical article URL where appropriate.
   - Instagram Feed should use the approved Instagram CTA strategy rather than inserting a non-clickable URL merely for consistency.
   - Instagram Story link behavior must be based on verified platform/API capability; do not assume a link-sticker capability that has not been proven.

6. **Produce and Founder-approve social visuals.**
   - Visual production follows the locked editorial/copy architecture and established destination layer.

7. **Build the execution handoff and schedule.**
   - Claude executes from repository authority only.
   - WordPress permalink, email CTA, and Wednesday-Friday social destination behavior must reconcile to the canonical destination layer before scheduling.

## Canonical Destination Rule

The WordPress canonical permalink is an upstream execution dependency for all downstream content intended to drive readers to the weekly article.

There must be one canonical destination record for the issue. Platform derivatives reference that record rather than independently constructing URLs.

No platform-specific URL may be inferred, invented, or reconstructed when the canonical WordPress destination can be established directly.

## Required Issue Packet Addition

Each weekly issue packet should include a canonical destination record containing, at minimum:

- `ARTICLE_URL`
- WordPress post ID when created
- canonical slug
- scheduled publication timestamp
- downstream CTA consumers (Brevo, Facebook, Instagram Feed strategy, Instagram Story strategy)
- verification state

The exact filename may be standardized by the production system, but the destination record is required before downstream execution is released.

## Issue 008 Lesson

Issue 008 successfully established its WordPress permalink during scheduled article creation and used that destination for the Brevo CTA. The execution exposed that the same dependency should be resolved **before** Wednesday-Friday social copy is finalized so post-publication social content can intentionally drive readers to the canonical article.

This is an architectural correction, not a change to the Monday-Friday editorial narrative.

## Production Gate

Beginning with Issue 009, a weekly issue is **not execution-ready** until:

- weekly thesis/arc is locked;
- Wednesday canonical article is complete;
- WordPress canonical destination is established and recorded;
- Wednesday email CTA resolves to that destination;
- Wednesday-Friday social CTA behavior is explicitly defined against that destination;
- all downstream copy/assets are Founder-approved.

**Founder principle:** editorial order serves the reader; production order serves the dependency chain.
