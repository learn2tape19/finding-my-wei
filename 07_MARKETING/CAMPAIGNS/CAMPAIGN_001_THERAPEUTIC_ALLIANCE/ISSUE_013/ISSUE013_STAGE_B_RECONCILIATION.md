# Issue 013 — Stage B Reconciliation Evidence

**Stage:** B — WordPress media
**Status:** **CLOSED — 25/25 reconciled**
**Reconciled:** September 23, 2026
**Method:** anonymous public HTTPS retrieval, SHA-256 compared against the canonical repository binary

---

## Result

| | |
|---|---|
| WordPress media objects | 25 |
| Canonical assets | 25 |
| Mapped 1:1 | **25** |
| Ambiguous duplicates | **0** |
| Canonical without media object | none |
| Media object without canonical | none |
| **Checksums matched** | **25/25** |
| Transformations by WordPress | **none** — every byte identical |

Uploads completed 2026-09-23 15:37–15:38 ET via the Founder Manual Bridge. No asset was uploaded,
renamed, resized, recompressed, regenerated or otherwise mutated by Claude.

## Filename mapping rule

WordPress appends a collision suffix when a filename already exists in the target month folder.
Mapping strips **only** a trailing `-N` immediately before the extension:

```
ISSUE-013_MONDAY_FEED_1080x1350-1.png  →  ISSUE-013_MONDAY_FEED_1080x1350.png
```

Five Monday assets carry `-1` (IDs 1714–1718). The other twenty retained canonical filenames.

## Verified map

| # | Canonical asset | WP ID | Public URL | SHA-256 | Result |
|---:|---|---:|---|---|---|
| 1 | `ISSUE-013_FRIDAY_FEED_1080x1350.png` | 1711 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_FRIDAY_FEED_1080x1350.png` | `4b68062ffc91e187…` | MATCH |
| 2 | `ISSUE-013_FRIDAY_LANDSCAPE_1200x628.png` | 1701 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_FRIDAY_LANDSCAPE_1200x628.png` | `1d9910c6a6b954f4…` | MATCH |
| 3 | `ISSUE-013_FRIDAY_STORY-01_1080x1920.png` | 1694 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_FRIDAY_STORY-01_1080x1920.png` | `135148a00a510977…` | MATCH |
| 4 | `ISSUE-013_FRIDAY_STORY-02_1080x1920.png` | 1691 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_FRIDAY_STORY-02_1080x1920.png` | `f9b1a4bdf1fb842c…` | MATCH |
| 5 | `ISSUE-013_FRIDAY_STORY-03_1080x1920.png` | 1713 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_FRIDAY_STORY-03_1080x1920.png` | `c347920d59197ad5…` | MATCH |
| 6 | `ISSUE-013_MONDAY_FEED_1080x1350.png` | 1716 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_MONDAY_FEED_1080x1350-1.png` | `07f3b2b850c4c8c6…` | MATCH |
| 7 | `ISSUE-013_MONDAY_LANDSCAPE_1200x628.png` | 1715 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_MONDAY_LANDSCAPE_1200x628-1.png` | `f62f62c42c801631…` | MATCH |
| 8 | `ISSUE-013_MONDAY_STORY-01_1080x1920.png` | 1714 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_MONDAY_STORY-01_1080x1920-1.png` | `67340bb4d291786b…` | MATCH |
| 9 | `ISSUE-013_MONDAY_STORY-02_1080x1920.png` | 1718 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_MONDAY_STORY-02_1080x1920-1.png` | `6167be6b79064520…` | MATCH |
| 10 | `ISSUE-013_MONDAY_STORY-03_1080x1920.png` | 1717 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_MONDAY_STORY-03_1080x1920-1.png` | `392e79f88fe33b1f…` | MATCH |
| 11 | `ISSUE-013_THURSDAY_FEED_1080x1350.png` | 1697 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_THURSDAY_FEED_1080x1350.png` | `045a4df5e235fe39…` | MATCH |
| 12 | `ISSUE-013_THURSDAY_LANDSCAPE_1200x628.png` | 1703 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_THURSDAY_LANDSCAPE_1200x628.png` | `cbb8a260542e75e6…` | MATCH |
| 13 | `ISSUE-013_THURSDAY_STORY-01_1080x1920.png` | 1692 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_THURSDAY_STORY-01_1080x1920.png` | `eccc2d0b0d64f46e…` | MATCH |
| 14 | `ISSUE-013_THURSDAY_STORY-02_1080x1920.png` | 1696 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_THURSDAY_STORY-02_1080x1920.png` | `d930834eb16b7f67…` | MATCH |
| 15 | `ISSUE-013_THURSDAY_STORY-03_1080x1920.png` | 1708 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_THURSDAY_STORY-03_1080x1920.png` | `91c251987c3277f2…` | MATCH |
| 16 | `ISSUE-013_TUESDAY_FEED_1080x1350.png` | 1698 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_TUESDAY_FEED_1080x1350.png` | `a6ee4eb2c0aca231…` | MATCH |
| 17 | `ISSUE-013_TUESDAY_LANDSCAPE_1200x628.png` | 1702 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_TUESDAY_LANDSCAPE_1200x628.png` | `137a489592fe0c19…` | MATCH |
| 18 | `ISSUE-013_TUESDAY_STORY-01_1080x1920.png` | 1689 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_TUESDAY_STORY-01_1080x1920.png` | `e6872bbfe29f6701…` | MATCH |
| 19 | `ISSUE-013_TUESDAY_STORY-02_1080x1920.png` | 1693 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_TUESDAY_STORY-02_1080x1920.png` | `c243389778c0c35f…` | MATCH |
| 20 | `ISSUE-013_TUESDAY_STORY-03_1080x1920.png` | 1709 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_TUESDAY_STORY-03_1080x1920.png` | `48c90cb139ef6d4d…` | MATCH |
| 21 | `ISSUE-013_WEDNESDAY_FEED_1080x1350.png` | 1704 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_WEDNESDAY_FEED_1080x1350.png` | `e250ef3cef6eab08…` | MATCH |
| 22 | `ISSUE-013_WEDNESDAY_LANDSCAPE_1200x628.png` | 1710 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_WEDNESDAY_LANDSCAPE_1200x628.png` | `d9e3222ba57a9d59…` | MATCH |
| 23 | `ISSUE-013_WEDNESDAY_STORY-01_1080x1920.png` | 1705 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_WEDNESDAY_STORY-01_1080x1920.png` | `876df337591c29eb…` | MATCH |
| 24 | `ISSUE-013_WEDNESDAY_STORY-02_1080x1920.png` | 1706 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_WEDNESDAY_STORY-02_1080x1920.png` | `129cb07cecb592fd…` | MATCH |
| 25 | `ISSUE-013_WEDNESDAY_STORY-03_1080x1920.png` | 1699 | `https://taoclinicaltouch.com/wp-content/uploads/2026/09/ISSUE-013_WEDNESDAY_STORY-03_1080x1920.png` | `3e00a9604ae07267…` | MATCH |
## Orphaned files on disk — recorded, not actioned

Three un-suffixed Monday files return HTTP 200 on disk but are **not registered media library
objects**:

```
ISSUE-013_MONDAY_LANDSCAPE_1200x628.png   1,959,673 bytes
ISSUE-013_MONDAY_STORY-01_1080x1920.png   2,061,851 bytes
ISSUE-013_MONDAY_STORY-03_1080x1920.png   2,059,849 bytes
```

Leftovers from an earlier partial upload — files written to disk without attachment records, which
is why WordPress appended `-1` on the successful upload. The media library returns exactly five
Monday items, all `-1`, so **no mapping ambiguity exists**.

**All downstream objects use the registered media URLs above, never the orphans.** Cleanup is
explicitly out of scope for this production cycle per Founder direction.

## Known measurement caveat

The WordPress REST `after=` date filter returned inconsistent results during discovery:
`after=2026-09-20T00:00:00` returned 0 items while `after=2026-09-22T00:00:00` returned 25, on
overlapping windows. **That filter is not trusted for reconciliation.** Every result recorded here
was established by direct object retrieval and per-object checksum, not by date filtering.

## Stage B closure

Per `TAO_PUBLISHING_EXECUTION_DOCTRINE.md` §4, a URL is authorized for downstream Buffer or Brevo
use only when `canonical SHA-256 == publicly retrieved SHA-256`. **All 25 satisfy that condition.**
Stage B is closed and the 25 URLs are authorized for downstream use.
