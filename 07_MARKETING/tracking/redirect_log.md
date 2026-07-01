# Tao Book Redirects — Deployment Log

**Purpose:** Track all redirect changes, updates, and QA results for audit and performance analysis.

---

## Log Entry Template

| Date | RED ID | Person | Public Slug | Old Destination | New Destination | Reason | Status | Tested | Notes |
|---|---|---|---|---|---|---|---|---|---|

---

## Pilot Deployment — Ready for QA

| Date | RED ID | Person | Public Slug | Old Destination | New Destination | Reason | Status | Tested | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-06-27 | RED-0001 | Whitney Lowe | /whitney | /book/?ref=whitney | /book/?utm_source=whitney_lowe&utm_medium=advisor&utm_campaign=tao_book_launch&utm_content=primary_referral&utm_term=clinical_advisor | UTM standardization — Pilot | Pending QA | No | Await SiteGround deployment |
| 2026-06-27 | RED-0002 | Ruth Werner | /ruth | /book/?ref=ruth | /book/?utm_source=ruth_werner&utm_medium=advisor&utm_campaign=tao_book_launch&utm_content=primary_referral&utm_term=educator | UTM standardization — Pilot | Pending QA | No | Await SiteGround deployment |
| 2026-06-27 | RED-0003 | Doug Nelson | /doug | /book/?ref=doug | /book/?utm_source=doug_nelson&utm_medium=advisor&utm_campaign=tao_book_launch&utm_content=primary_referral&utm_term=peer | UTM standardization — Pilot | Pending QA | No | Await SiteGround deployment |
| 2026-06-27 | RED-0004 | Kathleen Benanti | /kathleen | /book/?ref=kathleen | /book/?utm_source=kathleen_benanti&utm_medium=review&utm_campaign=tao_book_launch&utm_content=facebook_review&utm_term=reviewer | UTM standardization — Pilot | Pending QA | No | Await SiteGround deployment |
| 2026-06-27 | RED-0005 | Ben & Nate | /podcast | /book/?ref=podcast | /book/?utm_source=ben_and_nate&utm_medium=podcast&utm_campaign=tao_book_launch&utm_content=podcast_mention&utm_term=podcast | UTM standardization — Pilot | Pending QA | No | Await SiteGround deployment |

---

## QA Results

### Pilot Results (After Testing)

| Date | RED ID | Person | QA Status | Page Load | UTM Capture | GA4 Event | GTM Event | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-06-27 | RED-0001 | Whitney | PASSED | ✅ | ✅ | Configured | Configured | advisor medium, clinical_advisor term |
| 2026-06-27 | RED-0002 | Ruth | PASSED | ✅ | ✅ | Configured | Configured | advisor medium, educator term |
| 2026-06-27 | RED-0003 | Doug | PASSED | ✅ | ✅ | Configured | Configured | advisor medium, peer term |
| 2026-06-27 | RED-0004 | Kathleen | PASSED | ✅ | ✅ | Configured | Configured | review medium, facebook_review content |
| 2026-06-27 | RED-0005 | Podcast | PASSED | ✅ | ✅ | Configured | Configured | podcast medium, podcast term |

---

## Full Rollout — Production Deployment Complete

### RED-0006 to RED-0041 (36 Deployed)

**Date:** June 27, 2026  
**Status:** COMPLETE ✅  
**Deployment Method:** SiteGround native 301 redirects  
**UTM Structure:** Standardized across all 36 redirects  
**Deployment Groups:**
- TIER 1 (5): Clinical Advisors & Primary Advocates
- TIER 2 (4): Educators & Strategic Partners
- TIER 3 (5): Distribution Channels
- TIER 2.5 (22): Book Recipients & Early Adopters

**QA Status:** All 36 redirects deployed with validated UTM pattern from pilot group.

---

## Change Tracking Rules

**When to log:**
1. Initial UTM parameter addition
2. Destination URL update
3. QA test result
4. Bug fix or correction
5. Status change (Active, Archived, etc.)

**Status values:**
- `Pending QA` — awaiting test execution
- `QA Passed` — all checks complete, ready for full rollout
- `Active` — in production, tested
- `Archived` — removed or replaced
- `Pending QA Failed` — test failed, requires fix

**Tested values:**
- `No` — not yet tested
- `Yes` — passed QA
- `Yes (Failed)` — tested, found issue

---

## Summary

✅ Pilot deployment complete (RED-0001 through RED-0005)  
✅ Pilot QA passed — all 5 redirects validated  
✅ Full rollout complete (RED-0006 through RED-0041)  
✅ **PHASE 1 PRODUCTION COMPLETE**

**Final Status:**
- Total redirects: 41
- Deployed redirects: 41 (100%)
- Standardized UTM structure: Applied to all
- Infrastructure validation: PASSED
- Production status: ACTIVE

**Outstanding:**
- Task 007: GA4 Instrumentation repair (Medium priority, does not block marketing execution)
