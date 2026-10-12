# Issue 016 evidence and verification

**Record date:** October 12, 2026. These are retained snapshots of the production session, not later delivery evidence.

| Criterion | Result | Method and retained evidence |
|---|---|---|
| Approved image originals | PASS | 25 copied originals, SHA-256 compared against prior approved manifest; repository paths in ISSUE016_APPROVED_ASSET_MANIFEST.json |
| Canvas/export dimensions and rendered copy | PASS as recorded in production QA | Per-day QA and dimension records; later archival copy is byte-identical |
| WordPress media equality | PASS | Prior anonymous HTTP 200 retrieval, decoded dimensions, canonical/public SHA-256 equality in asset manifest |
| Article content | PASS | Exact approved blob retained at canonical BLOG path; metadata-only WordPress receipt avoids second editable manuscript |
| WordPress scheduled state | PASS | API readback post 1924, future, October 19 07:45 ET/11:45 UTC; schedule receipt |
| Buffer expected destinations/counts | PASS | BUFFER_SCHEDULE_READBACK.json: 5 Facebook + 20 Tao IG + 20 Drew IG in week window |
| Story asset/date/time mapping | PASS | All 30 assignments reconciled against visually verified BUFFER_STORY_ASSET_MAPPING.json |
| Individual Buffer IDs/native Story links | NOT VERIFIABLE from retained evidence | Browser execution did not retrieve individual object IDs/native link fields; no claim of adapter by-ID certification |
| Brevo state/sender/audience/design | PASS | Browser campaign 46 scheduled Oct 19 10 AM ET; list 64, seven current recipients; email payload/design retained |
| Social Open Graph image | Known limitation | Existing shared site emitter uses book cover, despite approved article header/schema image; no shared SEO change claimed |
| Scientific/editorial reviewer identities | NOT VERIFIABLE from this session | Locked Founder-approved article used; do not invent independent reviewer attestations |
| Public article and actual campaign delivery | NOT YET DUE | Scheduled October 19–23; requires post-publication verification before PUBLISHED/ARCHIVED |

Approval authority is Drew's explicit approvals and direction in the production conversation, recorded in the closeout and institutional decision. Machine retrieval, Founder direction, inferred expectations and future outcomes remain distinct.

Repository files are evidence snapshots and derivatives; only the linked BLOG article is the editable article authority. Metadata is centrally represented by WORDPRESS_METADATA_RECEIPT.json; email and social records are adaptations/receipts, not new article authorities. Local filesystem paths inside retained historical raw records are provenance and are superseded for asset retrieval by the repository-path manifest.
