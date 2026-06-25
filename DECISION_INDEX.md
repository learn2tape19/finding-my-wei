# Decision Index

Major decisions made across all projects, with rationale and context.

---

## Foundational Decisions

### Finding My Wei Architecture
**Decision**: GitHub as permanent source of truth for all intellectual assets  
**Date**: June 2026  
**Rationale**: Version control, longevity, collaboration, ownership, discoverability  
**Status**: Implemented  

**Related decisions**:
- Claude owns architecture, ChatGPT owns strategy (complementary, not competitive)
- Markdown as default format (portable, future-proof)
- 22-directory structure (scalable without redesign)
- Constitutional + Core Principles (durable vs. evolving)

---

## The Tao of Clinical Touch

### Pricing Strategy
**Decision**: Hold $14.99 for 30 days, then increase to $17.99 → $19.99 → $22.95  
**Date**: April 2026  
**Rationale**: Establish initial traction, secure reviews, then increase  
**Status**: In execution (hold through May 20, then evaluate)  

**Rationale**: Avoid aggressive pricing; let word-of-mouth build before premium increase.

### Distribution Approach
**Decision**: Hand-selected seeding (11 books to key influencers) vs. broad marketing  
**Date**: April 2026  
**Rationale**: Authority positioning, peer validation, organic amplification  
**Status**: Distribution complete; follow-up underway  

**Why not cold outreach?**: Influencers respond better to direct relationships and genuine belief in the work.

### CE Course Format
**Decision**: 4-hour live course (first phase) before full 12+ hour program  
**Date**: Q1 2026  
**Rationale**: Test market demand, establish credibility, build community  
**Status**: Phase 1 spec in development  

**Future expansion**: 4 hours → 12+ hours, potentially multi-module structure.

### Amazon Hold Strategy
**Decision**: Don't aggressively drive Amazon traffic yet; wait for 3-5 strong reviews  
**Date**: April 2026  
**Rationale**: Social proof (reviews) more valuable than traffic volume initially  
**Status**: Waiting for review acquisition  

**Next phase**: Coordinated Amazon push once review base established.

---

## Learn2Tape

### Course Platform Technology
**Decision**: WordPress + LearnDash + WooCommerce (not proprietary LMS)  
**Date**: 2024  
**Rationale**: Ownership, customization, cost-effective, media asset integration  
**Status**: Live  

**Trade-off**: Less polish than proprietary platforms, but full control and lower cost.

### K-Cuts Pricing
**Decision**: $299 one-time purchase vs. subscription or higher price  
**Date**: 2024  
**Rationale**: Accessible to therapists, profitable margin, no recurring billing friction  
**Status**: Live  

**Market validation**: Successful sales over 16 CEUs.

### Media Asset Strategy
**Decision**: Use real clinical photos/videos (not stock photography)  
**Date**: Strategic  
**Rationale**: Authenticity, differentiation, authentic marketing  
**Status**: Implemented  

**Advantage**: Competitors use generic images; we use real clinical settings.

### Landing Page Completion Priority
**Decision**: Testimonials and curriculum section (high-value, moderate effort) before design polishing  
**Date**: May 2026  
**Rationale**: Social proof and transparency > visual perfection  
**Status**: In progress  

---

## Sidekick Air / StitchCore

### Patent Strategy
**Decision**: Provisional patent filed (not full utility patent yet)  
**Date**: Q1 2026  
**Rationale**: Establishes priority date, lower cost, time to finalize design  
**Status**: Complete; provisional filed  

**Next decision**: File full utility patent when manufacturer partnership confirmed.

### Manufacturing Approach
**Decision**: Partner with manufacturers (PacMar + Drop Stitch Tech) vs. in-house or licensing  
**Date**: Q2 2026  
**Rationale**: Capital efficiency, expertise leverage, risk sharing  
**Status**: Partner selection underway  

**Handoff pattern**: CDP (performance specs) shared first; manufacturers propose solutions.

### Market Entry
**Decision**: B2B partnerships + direct-to-therapists initially (not VC/scaling)  
**Date**: Q2 2026  
**Rationale**: Sustainable, owner-friendly, quality over growth at all costs  
**Status**: In planning  

---

## Email & Marketing

### NCB Campaign Brand
**Decision**: Send as Learn2Tape, not Tao (list knows Drew through CE relationship)  
**Date**: April 2026  
**Rationale**: Leverage existing trust, avoid cold positioning  
**Status**: Executed (campaigns drafted)  

**Why not Tao?**: Tao is new; L2T relationship is 15+ years. Use what's trusted.

### Warm-up Strategy
**Decision**: 6-day MA warm-up (850 contacts in batches) before full campaign  
**Date**: April 2026  
**Rationale**: Establish sender reputation, catch bounces, refine list  
**Status**: Started April 28, 2026  

**Batches**: 100/100/100/150/250/150 (escalating volume with reputation-building).

---

## Infrastructure & Platforms

### Email Migration
**Decision**: Exchange → Google Workspace (March 2026)  
**Date**: February 2026  
**Rationale**: Better integration, lower cost, modern tooling  
**Status**: Complete  

### Domain Transfer Strategy
**Decision**: Migrate learn2tape.com, bostonbodyworker.com from GoDaddy to SiteGround DNS  
**Date**: April 2026  
**Rationale**: Consolidate hosting and DNS, simplify management  
**Status**: Initiated (5-7 day window)  

### DMARC Configuration
**Decision**: p=quarantine (not p=none or p=reject) with Brevo-only reporting  
**Date**: April 2026  
**Rationale**: Strong authentication without breaking legitimate mail; reduce noise  
**Status**: Configured  

---

## Analytics & Measurement

### GA4 Implementation
**Decision**: Implement full ecommerce funnel tracking (page_view → purchase with items payload)  
**Date**: May 2026  
**Rationale**: Understand customer journey, optimize conversion, measure marketing ROI  
**Status**: Complete  

**Next phase**: Create GA4 tags for Tao-specific events (amazon_click, sample_chapter_click).

---

## Standards & Processes

### Commit Message Discipline
**Decision**: Structured format `[Category] Subject — explanation` (not free-form)  
**Date**: June 2026  
**Rationale**: Searchable history, consistent standards, better git archaeology  
**Status**: Enforced in Finding My Wei repo  

**Categories**: [Tao], [Learn2Tape], [Finding My Wei], [Sidekick Air], [Research], [Admin]

### File Naming
**Decision**: kebab-case for files, PascalCase for directories with numbers  
**Date**: June 2026  
**Rationale**: Consistency, searchability, readability  
**Status**: Standard across Finding My Wei  

---

## What We Explicitly Decided NOT To Do

- **Not to use proprietary note-taking apps** (Notion, Evernote) as source of truth — they're temporary
- **Not to build proprietary learning management system** — LearnDash is good enough
- **Not to aggressively pursue venture funding** — Sustainable, owner-friendly approach preferred
- **Not to fragment across multiple social platforms** — Buffer + strategic platforms only
- **Not to rename files after publication** — Names are permanent
- **Not to optimize for algorithm wins** — Evergreen content over viral content

---

**Last Updated**: 2026-06-25  
**Curator**: Drew Freedman

---

**How to use this index**:
- When making new decisions, log them here with rationale
- Review quarterly to assess if decisions still hold
- Reference when onboarding new collaborators
