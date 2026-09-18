# Issue 013 — CONTINUITY — Preflight Receipt

**Phase:** 1 — Preflight only. **No live production mutation performed.**
**Date:** September 18, 2026 — revised after Monday repair
**Repository:** `finding-my-wei` — branch `main` — HEAD `b496cdb2a1e4cd71469c439a957e4065805551d0`
**Canonical package:** `07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_013/`

Nothing was published, scheduled, uploaded, sent, renamed, moved, resized, recompressed,
regenerated, or substituted. No approved binary or approved copy was altered.

---

## 1. Asset inventory — 25/25 PRESENT

| Role | Expected | Found |
|---|---:|---:|
| FEED | 5 | 5 |
| LANDSCAPE | 5 | 5 |
| STORY | 15 | 15 |
| **Total** | **25** | **25** |

Monday–Friday completeness: **PASS** — 5 assets per day, every day, sequences `STORY-01..03`
contiguous and unique.

All 25 live directly in the `ISSUE_013/` root per the Founder-locked canonical rule. No
`APPROVED_ASSETS/` subdirectory was required, created, or expected.

## 2. Integrity — 25/25 VERIFIED

- Independently recomputed SHA-256 for all 25 binaries: **25/25 match `MANIFEST.json`**, 0 mismatches.
- Recorded native binary dimensions for all 25: **25/25 match `MANIFEST.json`**, 0 mismatches.
- `ISSUE013_CHECKSUMS.sha256` regenerated against current binaries and verified: **25/25 OK**.
- Git tracking, commit state, and `origin/main` blob parity: **25/25 verified**.

### Monday repair — scope confirmed

Exactly **5 binaries changed** between `e236bb0` and `b496cdb`; **20 are byte-identical** to their
pre-repair blobs (verified by `git hash-object` against the prior commit, 0 differing).

| File | SHA-256 (superseded → current) | Native |
|---|---|---|
| `ISSUE-013_MONDAY_FEED_1080x1350.png` | `077ac177…` → `07f3b2b8…` | 1122x1402 (unchanged) |
| `ISSUE-013_MONDAY_LANDSCAPE_1200x628.png` | `75adf5a9…` → `f62f62c4…` | 1732x908 → 1733x907 |
| `ISSUE-013_MONDAY_STORY-01_1080x1920.png` | `66842018…` → `67340bb4…` | 941x1672 (unchanged) |
| `ISSUE-013_MONDAY_STORY-02_1080x1920.png` | `18c929df…` → `6167be6b…` | 941x1672 → 941x1671 |
| `ISSUE-013_MONDAY_STORY-03_1080x1920.png` | `15481727…` → `392e79f8…` | 941x1672 (unchanged) |

`MANIFEST.json` and `MONDAY_ASSET_MANIFEST.md` were updated to the current binaries. The 20
non-Monday manifest entries were left byte-for-byte as approved.

### Nominal role label vs native binary size — informational only

Filename dimensions are approved production-role labels. Native sizes differ and were recorded,
not corrected. 23 of 25 sit within 0.2% of their nominal aspect ratio. Two do not — both unchanged by the repair,
and no Monday asset is among them:

| File | Nominal | Native | Aspect delta |
|---|---|---|---:|
| `ISSUE-013_TUESDAY_FEED_1080x1350.png` | 1080x1350 (0.8000) | 1092x1440 (0.7583) | −5.21% |
| `ISSUE-013_WEDNESDAY_FEED_1080x1350.png` | 1080x1350 (0.8000) | 1092x1440 (0.7583) | −5.21% |

These two sit just outside Instagram's 4:5 portrait floor and will be cropped or padded by the
platform at render time. **Recorded as a downstream rendering note. This is not authorization to
crop, resize, recompress, regenerate, or substitute an approved master.**

## 3. Editorial locks

| Lock | Result |
|---|---|
| Weekly movement — Experience → Familiarity → Reflection → Integration → Ownership | **PASS** |
| Day themes — CONTINUITY / FAMILIARITY / REFLECTION / INTEGRATION / OWNERSHIP | **PASS** |
| Approved headline renders on the correct asset (all 25, OCR + visual) | **PASS 25/25** |
| Stale Issue 011/012 editorial bleed | **NONE** |

Copy was read, verified, and left untouched. No headline was rewritten, paraphrased, or proposed.

## 4. Brand lock — **PASS (25/25)**

**Superseded finding.** The original preflight at HEAD `e236bb0` recorded a brand-lock FAIL on all
five Monday masters: masthead `THE TAO OF PHYSICAL THERAPY`, footer URL
`THETAOPHYSICALTHERAPY.COM`, tagline absent.

The Founder replaced those five binaries at commit `b496cdb`. Re-verified at that HEAD:

| Element | Result |
|---|---|
| `THE TAO OF CLINICAL TOUCH` | 25/25 |
| `A PUBLICATION EXPLORING THE NEUROSCIENCE OF PERMISSION.` | 25/25 |
| `PRACTICE A HIGHER STANDARD` | 25/25 |
| `TAOCLINICALTOUCH.COM` | 25/25 |
| `ISSUE 013` / `CONTINUITY` | 25/25 |
| Any occurrence of "PHYSICAL THERAPY" anywhere in the set | **0** |

All five replaced Monday masters were additionally confirmed by direct visual inspection, not OCR
alone. Approved Monday editorial copy and photography are unchanged; only brand chrome differs
from the superseded binaries.

Four OCR-only flags across the set (`THURSDAY_STORY-01`, `THURSDAY_STORY-03`, `MONDAY_FEED`,
`MONDAY_STORY-01`) were each disproven by visual inspection. They are recognition artifacts —
dropped leading characters, a split domain string, and headline lines interleaved with in-scene
wall-poster text inside the photograph. No editorial or brand defect underlies any of them.

## 5. Production Completeness Gate — **CLOSED**

Run: `07_MARKETING/STANDARDS/verify_production_completeness.py ISSUE_013`

| Stage | Result |
|---|---|
| On arrival | GATE OPEN — 5 failures (`MANIFEST_PRESENT`: no per-day asset manifests) |
| After per-day manifests created | GATE OPEN — 25 failures (`FILE_PRESENT`, all 25) |
| After authorized `locate_asset()` root-path patch | **GATE CLOSED — 0 failures** |

`locate_asset()` previously searched only `APPROVED_ASSETS/<DAY>/` and `APPROVED_ASSETS/`, so it
could not see the Founder-locked canonical root layout. **Founder authorized** the addition of one
candidate path — `issue_dir / filename` — and it is now applied in the repository.

Regression check across every prior issue package, before and after the patch:

| Package | Pre-patch | Post-patch |
|---|---:|---:|
| ISSUE_009 | 5 failures | 5 failures (unchanged — pre-existing day-manifest naming, unrelated) |
| ISSUE_010 | 5 failures | 5 failures (unchanged — as above) |
| ISSUE_011 | 5 failures | 5 failures (unchanged — as above) |
| ISSUE_012 | 0 failures | 0 failures (unchanged) |
| ISSUE_013 | 25 failures | **0 failures** |

The patch is strictly additive: it appends a fallback candidate that is only reached when neither
`APPROVED_ASSETS/` location exists. No prior issue's result changed.

The checker never reads native PNG dimensions, so the nominal-vs-native differences in §2 do not
and cannot trip it.

## 6. Platform readiness

| Platform | State | Detail |
|---|---|---|
| WordPress | **BLOCKED** | `TAO_WP_USERNAME` / `TAO_WP_APP_PASSWORD` absent from session environment. REST API reachable; anonymous `OPTIONS /wp/v2/media` returns `Allow: GET` as expected. Authenticated preflight (`/users/me?context=edit`) not performable. |
| Buffer | **READY** | GraphQL authenticated. Account `6a3d317b545b077504a47719`, org `6a3d317b545b077504a4771b`. Tao Facebook `6a3eb95f5ab6d2f106763fc9` and Tao Instagram `6a3eb89f5ab6d2f106763ca0` both `isDisconnected: false`, `isLocked: false`. Window duplicate-check deferred to execution gate. |
| Brevo | **BLOCKED — by Founder decision and by dependency** | API reachable. Sender ID 3 active. No Issue 013 campaign exists. Plan period ends **2026-09-20** with **5,755** send credits against ~11,300 recipients. Founder has prohibited credit consumption before the Sept 20 reset, and campaign creation is blocked pending recipient reconciliation (§7). |

### Clean duplicate state confirmed
- WordPress slug `issue-013-continuity`: **free** (0 posts)
- WordPress media matching `ISSUE-013`: **0**
- Brevo Issue 013 campaign: **none**

## 7. Founder decisions — September 18, 2026

### Locked

| Decision | Value |
|---|---|
| Visual-production gate | **ACCEPTED AS CLOSED — 25/25 PASS** |
| Publication week | **Monday September 28 – Friday October 2, 2026** |
| Brevo credit consumption | **Prohibited before the September 20, 2026 plan reset** |
| Brevo campaign creation | **Blocked** until Issue 013 recipient configuration is reconciled against the *actual successful* Issue 012 production configuration |
| Email subject line and preheader | **Founder-review items.** Not approved. Any proposal remains a proposal until explicitly approved |
| Completeness-checker root-path patch | **AUTHORIZED AND APPLIED** |

### Still open

1. **WordPress credentials** — `TAO_WP_USERNAME` / `TAO_WP_APP_PASSWORD` absent from the execution
   environment. Stage B cannot begin without them. **This is the binding blocker.**
2. **Canonical slug** — `issue-013-continuity` proposed by pattern from `issue-012-agency`.
   Confirmed free on the live site; not yet Founder-confirmed.
3. ~~**Recipient reconciliation**~~ — **RESOLVED September 18, 2026.** Issue 013's Brevo recipient
   configuration is **list 64 only**, by explicit double opt-in. The NCB acquisition base
   (`2,5,6,7,8,10,44-59`) is placed outside the Tao publication architecture. See
   `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`. Doctrine §6
   corrected at v1.1/v1.2. **List 64's size at send time is the readership**; a small confirmed
   audience is the intended outcome, not a shortfall.
4. **Brevo plan reset** — confirm renewal and send-credit eligibility after September 20, 2026.
   Credit consumption is prohibited before that reset.
5. **Root duplicate housekeeping** — 10 byte-identical `ISSUE-013_*.png` strays at repository root
   from commit `95d38b1` ("Add files via upload"). Not canonical. Left in place; Issue 012 cleaned
   an equivalent condition at `b5c695f`.

### Not yet created — next production gate

`ISSUE013_PUBLISHING_SCHEDULE.md`, the canonical blog article, social captions, and email copy are
**not** part of this preflight commit. They are assembled at the next gate from Founder-approved
source material, against the now-locked publication week.

## 8. Artifacts created by this preflight

All inside the Issue 013 package. No approved source material altered.

- `MONDAY_ASSET_MANIFEST.md`
- `TUESDAY_ASSET_MANIFEST.md`
- `WEDNESDAY_ASSET_MANIFEST.md`
- `THURSDAY_ASSET_MANIFEST.md`
- `FRIDAY_ASSET_MANIFEST.md`
- `ISSUE013_CHECKSUMS.sha256`
- `ISSUE013_PREFLIGHT_RECEIPT.md` (this file)

One authorized change outside the package:

- `07_MARKETING/STANDARDS/verify_production_completeness.py` — `locate_asset()` root-path candidate (§5)

## 9. State at commit

Visual production is **complete and gate-closed**. Copy, arc, branding, and asset integrity pass
**25/25**. The Production Completeness Gate reports **0 failures**.

Execution remains **blocked on WordPress credentials**. Because every downstream object depends on
public checksum-verified WordPress media URLs, neither Buffer nor Brevo can proceed until Stage B
is unblocked — independent of the Brevo credit and recipient constraints locked above.

Nothing was published, uploaded, scheduled, sent, or created on WordPress, Buffer, or Brevo.
No approved binary or approved copy was altered. No credentials, tokens, or PII recorded.
