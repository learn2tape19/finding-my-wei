# Project Atlas — Task 007

## Repair GA4 Instrumentation

**Status:** Blocked  
**Priority:** Medium  
**Created:** June 27, 2026  
**Related Phase:** Phase 6 (Production Rollout)

---

## Overview

Google Site Kit measurement ID configuration is preventing completion of attribution validation. This issue affects analytics instrumentation only and does **not** affect referral infrastructure.

All 41 referral redirects are deployed and functional. UTM parameters are capturing correctly at the infrastructure level. Analytics attribution validation is the only outstanding requirement.

---

## Root Cause

- Site Kit is configured with measurement ID **G-BXN19CF60Q** (wrong property)
- Correct measurement ID should be **G-FW3PRHTX2P** (Tao Clinical Touch GA4 property)
- GA4 property mismatch prevents data collection on the correct analytics property
- Site Kit React UI is unresponsive to automation, blocking rapid configuration changes

---

## Objective

Restore complete attribution by validating:

✅ GA4 measurement configuration (measurement ID: G-FW3PRHTX2P)  
✅ Google Tag Manager events firing correctly  
✅ Custom dimensions capturing relationship data  
✅ Amazon click events tracking  
✅ Dashboard attribution showing correct source attribution  

---

## Scope

- Do **not** modify WordPress database directly
- Do **not** modify wp_options without documented repair procedure
- Do **not** use temporary workarounds that increase technical debt
- Avoid Site Kit UI automation (React component interactions are fragile)

## Recommended Approach

1. **Option 1 (Preferred):** Update Site Kit configuration via the WordPress admin UI manually (requires one-time manual interaction)
2. **Option 2:** Use WP-CLI to directly update the googlesitekit option with correct measurement ID
3. **Option 3:** Use documented SQL update with proper backup/rollback procedure

---

## Why This Matters

Attribution validation is required for future analytics-driven optimization of the referral campaign. However, it does **not** block:

- Publishing marketing assets
- Advisor outreach
- Content production
- Referral sharing
- Campaign execution

**This task should be completed independently of marketing execution.**

---

## Success Criteria

- [ ] GA4 receives data from taoclinicaltouch.com
- [ ] Real-time report shows active sessions with correct utm_source values
- [ ] GTM events firing correctly (page_view, book_page_view, amazon_click)
- [ ] Dashboard attribution showing correct source attribution
- [ ] All 5 pilot redirects validated end-to-end
- [ ] Documentation updated with validation results

---

## Notes

- Phase 1 referral infrastructure deployment is **COMPLETE** and operational
- This task is **blocked** by Site Kit configuration, not by referral infrastructure
- Marketing execution should proceed in parallel
- GA4 repair can be completed without affecting any other systems
