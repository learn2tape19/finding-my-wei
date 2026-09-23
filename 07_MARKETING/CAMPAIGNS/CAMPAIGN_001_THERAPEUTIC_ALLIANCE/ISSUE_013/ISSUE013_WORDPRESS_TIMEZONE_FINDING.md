# Issue 013 — WordPress Site Timezone Finding

**Status:** **PRODUCTION-CRITICAL for Issue 013 — not merely housekeeping**
**Found:** September 23, 2026, during Stage C article verification

---

## The finding

The WordPress site timezone is **UTC**, not America/New_York:

```
GET /wp-json/           timezone_string: ""     gmt_offset: "0"
```

Confirmed independently: on every published issue, `date` equals `date_gmt` exactly.

| Post | `date` (site-local) | `date_gmt` | Identical |
|---|---|---|---|
| `issue-012-agency` | 2026-09-21T11:45:00 | 2026-09-21T11:45:00 | yes |
| `issue-011-response` | 2026-09-14T11:45:00 | 2026-09-14T11:45:00 | yes |
| `issue-010-possibility` | 2026-09-07T11:45:00 | 2026-09-07T11:45:00 | yes |

## What this means

Issues 010, 011 and 012 all published at **11:45 site-local = 11:45 UTC = 7:45 AM ET**. The
established convention is therefore that **UTC time is entered into the WordPress editor**, not
Eastern time.

`ISSUE013_FOUNDER_MANUAL_BRIDGE.md` Part 2 specified *"Publish date/time: Monday, September 28,
2026 — 7:45 AM ET"* without accounting for the site running on UTC. **That instruction was
incomplete and is the origin of this risk.**

If `7:45 AM` was entered in the editor, the Issue 013 article is scheduled for
**07:45 UTC = 3:45 AM ET** — four hours earlier than the locked schedule, and before every Buffer
object.

## Correct value

| | |
|---|---|
| Locked publication time | **Monday, September 28, 2026, 7:45 AM ET** |
| Value to enter in the WordPress editor | **11:45** on September 28, 2026 |
| Matches | Issues 010, 011, 012 — all `11:45` |

## Why it could not be verified automatically

Scheduled (`future`) posts are not exposed to anonymous REST, and `status=future` requires
authentication — which is unavailable pending the parked Application Password issue. The permalink
correctly returns 404 while scheduled. **Founder confirmation of the editor value is the only
available verification.**

## Housekeeping item — after Issue 013 closes

Correct the WordPress site timezone to **America/New_York** (Settings → General → Timezone).

**Do not change it during this production run.** Altering the site timezone while a post is
scheduled would shift that post's effective publication time. Sequence it after Issue 013 is
closed, and re-verify the scheduled times of anything then outstanding.

Once corrected, future issues should enter **Eastern** time in the editor, and the manual bridge
instruction must be updated to match — otherwise the same error recurs inverted.
