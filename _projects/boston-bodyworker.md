# The Boston Bodyworker — Project Track

## Objective
Decide the right endgame for The Boston Bodyworker assets and entity after closure: preserve for strategic value, repurpose, sell, wind down, or some combination.

## Current Status
**Migration complete. Site is live on SiteGround.**
- bostonbodyworker.com resolves to SiteGround (35.212.99.34) ✅
- All content, theme, and pages restored and rendering correctly ✅
- Active plugins: bb-plugin, woo360-modules, wordpress-seo, redirection, sg-cachepress, sg-security
- GoDaddy hosting still active — needs cancellation
- Temp files still on server — needs cleanup

## Current Focus
- [x] Strip all commerce and payment plugins from the site
- [x] Pre-migration deep clean (malware artifacts, junk plugins, bad perms)
- [x] Transfer 2.2 GB backup to SiteGround via server-to-server wget
- [x] Switch DNS nameservers at GoDaddy → SiteGround
- [x] Restore site files and database to SiteGround — site live and rendering
- [x] Post-migration cleanup (temp files, unused plugins)
- [x] Cancel GoDaddy hosting
- [ ] Decide long-term use of the site (authority feeder, sell, or sunset)

## Next Actions
1. **Post-migration cleanup** — via SSH or WP admin:
   - Delete `/home/customer/www/bostonbodyworker.com/public_html/sginfo.php` (probe file)
   - Delete `/tmp/database.sql`, `/tmp/extract_wpress.php`, `/tmp/extract_wpress2.php`, `/tmp/extract_wpress.log`, `/tmp/extract_wpress2.log`
   - Deactivate + delete `siteground-migrator` and `all-in-one-wp-migration` plugins (no longer needed)
   - Consider whether to keep or remove `bb-plugin`, `woo360-modules`, `bb-theme-builder` — removing them will break page layouts; keep for now unless converting to blocks
2. **Cancel GoDaddy hosting** — log into GoDaddy → My Products, cancel the hosting plan for bostonbodyworker.com. Domain registration can stay at GoDaddy (nameservers already pointed to SiteGround).
3. **Audit site value** — traffic, rankings, backlinks, domain authority (Ahrefs/Semrush). Do before deciding keep vs sell vs sunset.
4. **Legal/accounting review** — get guidance before dissolving the LLC.

## Funnel Tasks Needing Attention
- [x] Post-migration cleanup (sginfo.php, temp files, unused migration plugins)
- [x] Cancel GoDaddy hosting
- [x] Email routing fixed — MX records switched to Google in SiteGround DNS (March 28, 2026)
- [x] drew@bostonbodyworker.com alias already configured in Google Workspace → routes to drew@learn2tape.com
- [ ] Update SPF and DKIM records in SiteGround DNS for bostonbodyworker.com (email authentication — prevent spam folder)
- [ ] Audit the website asset: traffic, rankings, backlinks, and lead value
- [ ] Determine whether the site should be kept as a feeder, repurposed, sold, or sunset
- [ ] Get legal/accounting guidance before deciding whether to dissolve the LLC

## Decisions
- The Boston Bodyworker has been closed after 25 years.
- The LLC is still active — dissolution needs legal/accounting review before proceeding.
- **March 27, 2026:** Decided to shelve the site, keep content intact, strip all commerce functionality.
- **March 27, 2026:** Chose All-in-One WP Migration (Option A) over SG Migrator (blocked) or manual SiteGround transfer.
- **March 27, 2026:** DNS nameservers switched from GoDaddy (NS51/NS52.DOMAINCONTROL.COM) to SiteGround (ns1/ns2.siteground.net).
- **March 28, 2026:** Migration complete. Site fully live on SiteGround. DB and wp-content restored via custom .wpress extractor (bypassed AIO WP Migration paid restore wall). Site rendering correctly at bostonbodyworker.com.
- **March 28, 2026:** GoDaddy hosting cancelled. Plan set to expire APR 30, 2026 (no refund — past eligibility window). Domain registration stays at GoDaddy with nameservers pointed to SiteGround.

## Migration Log — March 27, 2026

### Phase 1: GoDaddy site cleanup
**Root cause of SG Migrator failure:** WP_Filesystem API defaults to FTP transport on GoDaddy shared hosting (not Direct), blocking plugin-based migration even though filesystem permissions were correct. Confirmed via source code review (Files_Service.php line 198: `$wp_filesystem->mkdir()`).

**Pre-migration sweep completed (all junk removed from GoDaddy):**
- `.sucuriquarantine/` — malware quarantine artifacts from Feb–Apr 2025 infection
- `mu-plugins/` — GoDaddy Worker, Installatron, Nexcess (wrong host)
- `plugins/` — sg-cachepress, ManageWP Worker, Creative Mail, WP Importer, RevSlider zip
- `uploads/` — old migration temp dir, wc-logs, woocommerce_uploads, gravity_forms, mailpoet, et_temp, etc.
- `advanced-cache.php`, `fatal-error-handler.php` (0777 perms, causing stat failures)
- `object-cache.php.MIG` (stale migration artifact), `siteBackup.sh`, `error_log`, `readme.html`, `license.txt`, old index backup
- Permissions corrected: all files 644, all dirs 755 across wp-content

### Phase 2: SiteGround prep
- Fresh WordPress 6.9.4 installed at bostonbodyworker.com/ root on SiteGround
- SSH access established: `ssh -i ~/.ssh/siteground_bb -p 18765 u2851-apfiurxo4lfg@35.212.99.34`
  - SSH key: `~/.ssh/siteground_bb` (ed25519, imported to SiteGround as "macbook-bb")
- AIO WP Migration 7.103 installed + activated via WP-CLI
- siteurl/home corrected to `https://bostonbodyworker.com` in wp_options

### Phase 3: File transfer
- 2.2 GB `.wpress` backup created on GoDaddy via AIO WP Migration UI
- Transferred server-to-server via SSH wget at ~100 MB/s:
  ```
  nohup wget -q -P /home/customer/www/bostonbodyworker.com/public_html/wp-content/ai1wm-backups/ \
  'https://www.bostonbodyworker.com/wp-content/ai1wm-backups/www-bostonbodyworker-com-20260327-163454-xat2vfax1bre.wpress' \
  > /tmp/wget_bb.log 2>&1 &
  ```
- Backup confirmed complete at 2.2G on SiteGround

### Phase 4: DNS
- GoDaddy nameservers changed from NS51/NS52.DOMAINCONTROL.COM → ns1/ns2.siteground.net
- SiteGround server IP: `35.212.99.34`
- Status: propagating as of March 27, 2026

### Phase 5: Restore (PENDING)
- Once DNS resolves to 35.212.99.34:
  - Log into `https://bostonbodyworker.com/wp-admin/` (user: `drewfreedman`)
  - All-in-One WP Migration → Backups → Restore `www-bostonbodyworker-com-20260327-163454-xat2vfax1bre.wpress`

## Site Cleanup Log — March 27, 2026
**Removed (deactivated + deleted):**
- WooCommerce (core)
- WooPayments, WooCommerce Stripe Gateway, WooCommerce PayPal Payments, WooCommerce Square
- Payment Gateway PayPal Pro WooCommerce
- Gravity Forms + Gravity Forms Stripe Add-On
- ShipStation for WooCommerce, USPS Simple Shipping, WooCommerce USPS Shipping
- WooCommerce Tax, WooCommerce.com Update Manager, WP Menu Cart
- Google for WooCommerce, Coupon Shortcodes for WooCommerce
- UpdraftPlus Pro (SiteGround has native backups)
- Remaining WooCommerce.com-managed plugins deleted via cPanel

**Kept (remove after migration confirmed):**
- Woo360 Builder + Themer + Modules — powering page layouts
- GoDaddy Pro Sites Worker
- All content, SEO (Yoast), redirects, analytics plugins — preserved

**Also resolved:**
- Removed learn2tape.com from ManageWP/GoDaddy Pro monitoring → stopped nightly backup failure emails

## Notes
- Drewdog had to file personal bankruptcy after the closure; handle this lane with care.
- The site has age and authority — potential SEO equity worth assessing before any decision.
- Core question (deferred): should the site feed other properties, be sold, or be shut down cleanly?
- WP-CLI `wp ai1wm restore/import` requires paid Unlimited Extension — restore must be done via browser UI.

## Migration Technical Notes — March 28, 2026
The AIO WP Migration free tier blocks restore from Backups AND WP-CLI restore (both require paid Unlimited Extension). Bypassed by:
1. Writing a custom PHP extractor that parses the .wpress binary format (4377-byte headers: a255 filename + a14 size + a12 mtime + a4096 path) directly on the SiteGround server
2. Extracted 18,497 wp-content files (1,764 MB) and database.sql (363 MB) to correct locations via SSH
3. Ran `wp db import` — imported as SERVMASK_PREFIX_ tables (AIO's placeholder prefix used in the backup SQL)
4. Ran shell loop to rename all SERVMASK_PREFIX_ tables to the site's actual rsj_ prefix
5. Activated woo360-theme-child theme and key plugins (bb-plugin, woo360-modules, wordpress-seo, redirection, sg-cachepress, sg-security)
6. Site rendered correctly on first load

Active plugins kept (site depends on them for rendering): bb-plugin, woo360-modules, bb-theme-builder, redirection, wordpress-seo, sg-cachepress, sg-security

## Weekly Review Snapshot
- Wins: Migration fully complete. Site live on SiteGround with all content, pages, images, and theme intact. Zero data loss. Bypassed two separate paywalls (SG Migrator + AIO restore) without spending a dollar.
- Stuck points: None on migration. Decision phase begins.
- Carryover: Site value audit, LLC legal review, GoDaddy hosting cancellation
- Next session top outcome: Cancel GoDaddy hosting + begin site value audit
