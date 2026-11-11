# PCP-CERT-001 — SiteGround Staging Recovery and Security Gate

**Recorded:** 2026-11-11
**Status:** BLOCKED_ENVIRONMENT — NO PRODUCTION PUBLICATION AUTHORIZED
**Scope:** The Tao of Clinical Touch WordPress staging certification
**Incident:** SiteGround WordPress > Staging failed with "Failed to clone database" when attempting staging copy `pcp-cert-001`.

## Governing facts

- This is a **staging-clone failure**, not evidence that the accepted WordPress adapter failed.
- The previous SiteGround interface displayed the installation as `http://taoclinicaltouch.com/`; this display alone does not establish whether the public site uses HTTPS. Verify the actual WordPress Site Address/Home URL and SSL configuration before adapter certification.
- The current official SiteGround staging guide states: database must be **under 5 GB**, fewer than **500 tables**, account must have **more than 51% free disk** and **more than 20% free inodes**, at most 10 staging environments and 15 operations daily; Multisite is unsupported. Source: https://www.siteground.com/tutorials/staging/create-staging
- WordPress issued security release **7.1.4 on 2026-10-28**. Source: https://wordpress.org/news/2026/10/wordpress-7-1-4/
- The installed WordPress version on production and staging has **NOT BEEN VERIFIED**. Do not claim patched or vulnerable without inspection.

## Recovery procedure (non-destructive)

1. Confirm a current restorable production backup in SiteGround before any update or staging changes.
2. Inspect the production WordPress version in Dashboard > Updates or Site Tools (authenticated). If below a release with the applicable October 28 fixes, plan the host-supported security update with backup and maintenance safeguards. **No production update is authorized by this runbook alone.**
3. Check SiteGround disk and inode usage, MySQL database size/table count, number of staging sites, daily staging operations and Multisite status.
4. Examine whether a partial `pcp-cert-001` staging entry/subdomain/database was left behind; do not delete without validating ownership and backup state.
5. If published limits are satisfied, request that **SiteGround Support inspect internal staging database clone logs** for the exact failure: MySQL permission, table corruption, timeout/resource limit, staging service issue, or other specific cause.
6. Ask SiteGround to fix the staging **clone path**, not restore/overwrite/modify the production database without explicit Founder authorization.
7. Once staging exists, verify HTTPS, URL/site identity, staging access protection and non-indexability; disable real outbound email/payment/transaction side effects and check the cloned environment for live third-party keys.
8. Confirm the staging installation contains October 28 security fixes before enabling any certification credentials.
9. Set up dedicated staging-only publishing credentials using secure secrets storage, with exact staging identity and least privileges.
10. Re-enter the existing PCP-CERT-001 work order; retain the full certification stop/approval gates. No production destination may be enabled.

## Support request (copy-ready)

SiteGround Support: In Site Tools > WordPress > Staging, creating `pcp-cert-001` for `taoclinicaltouch.com` failed with **"Failed to clone database."** Please inspect the server-side staging/database cloning logs and identify the specific failure. Please confirm whether database size/table count, disk/inode limits, MySQL permissions, corrupted tables, timeouts, or staging service errors are responsible. Please do not modify, restore, overwrite, or deploy to the production database without my separate approval. Advise the safest corrective action and whether any partial staging resources were left behind.

## Evidence required to clear the gate

- production WordPress core version (or security-backport verification);
- verified working production HTTPS (no credentials);
- backup verification;
- database size/table count and quota checks;
- SiteGround support finding and remediation;
- non-public staging URL and verified access restrictions;
- staging WordPress core version and security patch verification;
- staging-only certification account and external secret-reference identifiers;
- staging taxonomy and timezone details;
- explicit certification readiness decision.

**Current decision:** Keep `tao.wordpress.production` disabled. Do not run PCP-CERT-001 against the public Tao site. Do not claim the SiteGround clone failure was fixed until a new safe staging clone succeeds and evidence is recorded.
