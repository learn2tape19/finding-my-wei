# Issue 015 — Visual Reconciliation Gate

**Status: HOLD — approved in conversation, binary reconciliation and publication verification incomplete.**

## Editorial and visual approval
Founder approved 25 visual roles (five per weekday: Feed, Landscape, Story 1–3). The most recent explicit approvals cover Wednesday, Thursday, and Friday, concluding with Friday Story 3. Visual approval is not evidence that the exact binary was uploaded to the repository.

## Local candidate inventory (October 3, 2026)
A runtime scan located **49 candidate PNGs**, including rejected iterations and superseded renders. A separate local CSV, `issue015_image_inventory.csv`, records filename, native width/height, SHA-256, and bytes for each candidate. It has not yet been committed to GitHub. Dimensions distribution: 1 at 1109×1418; 12 at 1092×1440; 1 at 1672×941; 1 at 1122×1402; 20 at 941×1672; 1 at 1110×1417; 4 at 1080×1456; 3 at 940×1672; 1 at 1919×1280; 1 at 1733×907; 4 at 1734×907. **Do not mislabel these native dimensions as exact 1080×1350, 1200×628, or 1080×1920 masters.**

## Reconciliation procedure
1. Map every approved conversation render to its exact local PNG, excluding all rejected or superseded versions. Verify image content visually, not by generated filename alone.
2. For each of 25 roles, record exact source filename, source SHA-256, native dimensions, approved conversation role, and intended destination. Do not crop, regenerate, or substitute an approved image without fresh Founder approval.
3. Upload verified exact approved binaries to canonical ISSUE_015 asset directory using a binary-capable GitHub workflow; read back each upload and compare checksums. Text-only GitHub file actions do not support these PNG uploads.
4. Review publication dimensions separately. Any resizing or reframing must be explicitly approved before derivative assets are treated as publication-ready.
5. Run established production gates and independent readbacks in sequence: GitHub → WordPress → Buffer → Brevo. No deployment, scheduling, or complete manifest is claimed at this stage.

## Approved visual roles checklist
| Day | Feed | Landscape | Story 1 | Story 2 | Story 3 |
|---|---|---|---|---|---|
| Monday | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending |
| Tuesday | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending |
| Wednesday | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending |
| Thursday | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending |
| Friday | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending | approved; binary pending |
