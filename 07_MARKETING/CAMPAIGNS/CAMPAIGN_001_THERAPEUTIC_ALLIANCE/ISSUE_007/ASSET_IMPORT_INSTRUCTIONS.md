# Issue 007 — Approved Asset Import Instructions

**Status:** FOUNDER APPROVED HANDOFF SUPPORT  
**Source bundle:** `ISSUE007_WED_FRI_APPROVED_ASSETS.zip`

The ChatGPT production environment generated the 18 Founder-approved Wednesday–Friday native visual files. The GitHub connector used for institutional documentation does not expose a binary-file upload action, so the exact approved binary bundle is transferred separately as one ZIP and must be imported into this repository by Claude before any external execution.

This is a mechanical transfer only. It does **not** authorize visual regeneration, redesign, recomposition, or copy changes.

## Required destination

After receiving the ZIP, extract its contents into:

`07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_007/APPROVED_ASSETS/`

Preserve the three day folders and exact filenames.

Expected structure:

```text
APPROVED_ASSETS/
  WEDNESDAY/
    ISSUE007_WED_FEED_1080x1350.jpg
    ISSUE007_WED_STORY_FRAME01_1080x1920.jpg
    ISSUE007_WED_STORY_FRAME02_1080x1920.jpg
    ISSUE007_WED_STORY_FRAME03_1080x1920.jpg
    ISSUE007_WED_BLOGOG_1200x628.jpg
    ISSUE007_WED_EMAILHEADER_1200x627.jpg
    ASSET_MANIFEST.json
  THURSDAY/
    ISSUE007_THU_FEED_1080x1350.jpg
    ISSUE007_THU_STORY_FRAME01_1080x1920.jpg
    ISSUE007_THU_STORY_FRAME02_1080x1920.jpg
    ISSUE007_THU_STORY_FRAME03_1080x1920.jpg
    ISSUE007_THU_BLOGOG_1200x628.jpg
    ISSUE007_THU_EMAILHEADER_1200x627.jpg
    ASSET_MANIFEST.json
  FRIDAY/
    ISSUE007_FRI_FEED_1080x1350.jpg
    ISSUE007_FRI_STORY_FRAME01_1080x1920.jpg
    ISSUE007_FRI_STORY_FRAME02_1080x1920.jpg
    ISSUE007_FRI_STORY_FRAME03_1080x1920.jpg
    ISSUE007_FRI_BLOGOG_1200x628.jpg
    ISSUE007_FRI_EMAILHEADER_1200x627.jpg
    ASSET_MANIFEST.json
  MASTER_ASSET_MANIFEST.json
```

## Mandatory verification

Before committing or using any asset:

1. verify exact dimensions;
2. compute SHA-256 for each file;
3. compare against the corresponding day `APPROVED_ASSET_MANIFEST.md` in GitHub;
4. verify all 18 files are present;
5. verify no extra production asset has been substituted;
6. commit the imported binaries on the Issue 007 execution branch;
7. report the import commit SHA before any Buffer mutation.

Any missing asset or checksum mismatch = **BLOCKED**.

## Visual authority

Founder-approved visual rules remain locked:

- use the approved files as-is;
- no generative rebuild;
- no crop-from-contact-sheet substitution;
- no added drip motif;
- do not replace the ripple;
- do not invent or remove copy;
- do not add slogans or secondary branding;
- do not alter dimensions.

## Execution dependency

No Wednesday–Friday Buffer mutation may occur until the approved binary asset import is complete and checksum verified.
