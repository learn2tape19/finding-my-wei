# ISSUE 010 — ASSET MANIFEST

**Status:** FOUNDER-APPROVED PRODUCTION SET PERSISTED — 30/30 assets ingested and hash-verified.

**Binary source authority:** `ISSUE_010_APPROVED_ASSET_PACKET_FIXED` (Founder-designated). The earlier `..._FINAL` packet is **superseded and has no authority**. `_FIXED` is the intentionally corrected packet produced after production-dimension verification found the original generated images were not at canonical dimensions.

**Founder approval:** explicitly supplied by the Issue 010 persistence handoff for all 30 production assets. Approval is **not** inferred from file presence.

## Provenance distinction

- **`SOURCE_APPROVED/<DAY>/`** — the exact Founder-approved generated originals, preserved **byte-identical**. Never normalized, cropped, recompressed, or edited.
- **`APPROVED_ASSETS/<DAY>/`** — the authorized production derivatives, created from those originals by **dimension normalization only** (LANCZOS resize, no crop, no creative edits).

Canonical directories are `APPROVED_ASSETS/` and `SOURCE_APPROVED/`. There is no `ASSETS/` directory in Issue 010.

## Production specifications

| Surface | Dimensions | Count |
|---|---:|---:|
| Feed (Instagram + Facebook) | 1080×1350 | 5 |
| Story (3 per day) | 1080×1920 | 15 |
| Email header | 1200×627 | 5 |
| Blog / Facebook / OG header | 1200×628 | 5 |
| **Total** | | **30** |

Six production assets per weekday, Monday–Friday.

## Production assets — `APPROVED_ASSETS/`

| Day | Asset | Canonical filename | Required px | Actual px | SHA-256 | Founder | Repository path |
|---|---|---|---:|---:|---|---|---|
| MON | FEED | `ISSUE010_MON_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `71f1f3a40cb5c0bd0daa45a5d946eac7e197cd5818d6cc5e43ee953bfca47535` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | STORY 1 | `ISSUE010_MON_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `b0f15cae0c9f68992ce27465eb3609859b8020ae5f8ed4a157c4e6ed787f98df` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | STORY 2 | `ISSUE010_MON_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `45f9f93c2b792ca6a9292cc3390eb84b3cfdb4713ffbffbb91ba3f399465ec7f` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | STORY 3 | `ISSUE010_MON_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `252d1da07a20f047a129ab9e37d11350745f8d74b45ec22be65ad00ef99b6f70` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | BLOG/OG | `ISSUE010_MON_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `84697e45a78003a8e73bbe2ec68438d6c0e3e783ea305e0861cedea1d9c7b73d` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | EMAIL HEADER | `ISSUE010_MON_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `d8bb38325a24780cb09df5268cf746e0f489eb6bbdd57a92a548e0c1f8126aa4` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| TUE | FEED | `ISSUE010_TUE_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `8ff350d572e770f9e5d89362c4449bc416c4bec8be1ab37973d3ec8fe651677e` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | STORY 1 | `ISSUE010_TUE_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `3dfbe550bd06e5ec8c078b44ba3738c9424772bb922cf3af2163456879c41a24` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | STORY 2 | `ISSUE010_TUE_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `19a5d163d11ce72ca2243aa78d5ba0ab6c1426758778ed2a70cfa2b4933b775f` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | STORY 3 | `ISSUE010_TUE_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `a5eb259f1db68655014f33562a5ab70f33beb73a0260c0f6702df95f5e6002a8` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | BLOG/OG | `ISSUE010_TUE_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `7e990fb45e63645d5c612156dd5e667be3df2ed21de459073d96d0c8d0a53b88` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | EMAIL HEADER | `ISSUE010_TUE_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `7859c66a4bf0867845e9cb16a08eaa41596b5741b7881218f26fd52bfefa41bc` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| WED | FEED | `ISSUE010_WED_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `cb1fb0f6c401c77ba80eb5049493a527dd4167dc6fecbfc513905ce46770276b` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | STORY 1 | `ISSUE010_WED_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `64616b71fec010f0fb1f2f70e34bfc0f7839d4808d2fcab2c9d0c560d85bb697` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | STORY 2 | `ISSUE010_WED_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `87140a944171773f39f3d0f10d7fda2cb24f765cd673d7ceeee577ca6309dfb7` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | STORY 3 | `ISSUE010_WED_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `eb5e56971bcea7226f477bc889aacac21f5995195ab8037d0070ceac2956dc61` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | BLOG/OG | `ISSUE010_WED_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `d36d9d121ddd2e1006ee80476679099b2ca32cfbcaf2556fdf70cf2db5db6eee` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | EMAIL HEADER | `ISSUE010_WED_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `9be4f5d31bc74310ba08a9ae5f16e6d8f2da0ccb196bccf5971fbf51dec608a1` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| THU | FEED | `ISSUE010_THU_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `5a1e3a9dc99428215f48a504239b741658dbc53ec7f6f6377ce66afb8a897e13` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | STORY 1 | `ISSUE010_THU_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `5cc5c771addf48c892b780aa8b6bae2b422f18ebf30b01d15eab88578f642e28` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | STORY 2 | `ISSUE010_THU_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `a7507d22f49fa4f88e1dc47135fe3114d7b194261f66fa2b2ebb311c1339b08e` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | STORY 3 | `ISSUE010_THU_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `006e3d0dd4eb5b4a606f01abc1f75b642030763b13a0f9ea39a1bfbb1120343b` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | BLOG/OG | `ISSUE010_THU_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `bf41774b351ca0d58529006ccfea2eaf1f7a1092e8adcbf05917077c1f06f2ee` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | EMAIL HEADER | `ISSUE010_THU_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `e2e816bad0bdd7027918b9a913ef3236e85897223b8244fd85fc7bab1d6aefb7` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| FRI | FEED | `ISSUE010_FRI_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `6683bb8c414c5336b55335bb67d76d6637fcd04bfd4ed4b6c484b691ef1d3358` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | STORY 1 | `ISSUE010_FRI_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `8536935125e909e62314c3475f26c796be7e31662c5fedd817925ab43adeae45` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | STORY 2 | `ISSUE010_FRI_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `ff506818dc79b42a31ce6104de375954beeac5d7b270a3b00f2fe7b1dde097d7` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | STORY 3 | `ISSUE010_FRI_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `569aa4539d6b5d40559e53f4f0514499bafa9c3aff4fd8b93a05a1a4b055f679` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | BLOG/OG | `ISSUE010_FRI_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `0e61907caf183c5ec0d29db9db5f93bc772498d9ca74e27c09b696ac60736df7` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | EMAIL HEADER | `ISSUE010_FRI_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `f9d91f5e7b02d2cdfd9f96610964cdfd002dab4b509a536d53aaf649448d3196` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |

## Source originals — `SOURCE_APPROVED/`

Preserved unchanged. Source dimensions are the as-generated dimensions and intentionally differ from production dimensions.

| Day | Asset | Canonical filename | Source px | SHA-256 | Repository path |
|---|---|---|---:|---|---|
| MON | FEED | `ISSUE010_MON_FEED_1080x1350.png` | 1122×1402 | `dd47bcf9ce1f77b62d25cf3b7db8f183f38147ed4c72748b9825abb9cdc92646` | `SOURCE_APPROVED/MONDAY/` |
| MON | STORY 1 | `ISSUE010_MON_STORY_01_1080x1920.png` | 941×1672 | `8b29e7bff0f6342110ee210542a3220d7cffe811b84063e5ccd12df81fae4089` | `SOURCE_APPROVED/MONDAY/` |
| MON | STORY 2 | `ISSUE010_MON_STORY_02_1080x1920.png` | 941×1672 | `73d72cd70746a8d703d28687c400abb089a6e5d74f76e63adf9784eb6dfe7aef` | `SOURCE_APPROVED/MONDAY/` |
| MON | STORY 3 | `ISSUE010_MON_STORY_03_1080x1920.png` | 941×1672 | `9fe539ec23e81364369b70bf5ffb8284b11df6f86f12e8bdf1fba3354407bbf9` | `SOURCE_APPROVED/MONDAY/` |
| MON | BLOG/OG | `ISSUE010_MON_BLOG_OG_1200x628.png` | 1736×906 | `146c137c84d5c2d8855c935450e5b17672c4d15cb395d38a81a8b3decef0d108` | `SOURCE_APPROVED/MONDAY/` |
| MON | EMAIL HEADER | `ISSUE010_MON_EMAIL_HEADER_1200x627.png` | 1736×906 | `c8a6b90474008fcf2f25da2fbcc44aeae7bd045c97c1ba5968d05943d2a7e69b` | `SOURCE_APPROVED/MONDAY/` |
| TUE | FEED | `ISSUE010_TUE_FEED_1080x1350.png` | 1122×1402 | `38595179c94d8caa7b2da2f6c8ffdc258fe7ff03c6d56e82089b4a33bb723158` | `SOURCE_APPROVED/TUESDAY/` |
| TUE | STORY 1 | `ISSUE010_TUE_STORY_01_1080x1920.png` | 941×1672 | `4c0047ec131144f67277be13553c68c6612ff8395433c50ff0c4b081268689c4` | `SOURCE_APPROVED/TUESDAY/` |
| TUE | STORY 2 | `ISSUE010_TUE_STORY_02_1080x1920.png` | 941×1672 | `21928cd8e05f24e9ad9dfda68437ba809e9515ebe1b89faf7a45975b9fdd69b0` | `SOURCE_APPROVED/TUESDAY/` |
| TUE | STORY 3 | `ISSUE010_TUE_STORY_03_1080x1920.png` | 941×1672 | `d7ee3075335b6a0bfa2869995b5d8497737a4d6a7a6609fdc6122b1fcff05d71` | `SOURCE_APPROVED/TUESDAY/` |
| TUE | BLOG/OG | `ISSUE010_TUE_BLOG_OG_1200x628.png` | 1733×907 | `ee89e607b9a1c958e4b16765dcd0567dbd32541e6b484cc816cea52048789e0f` | `SOURCE_APPROVED/TUESDAY/` |
| TUE | EMAIL HEADER | `ISSUE010_TUE_EMAIL_HEADER_1200x627.png` | 1735×907 | `35ab88e1b794ad2439d51f73e350ec5a8561ce6fdb2cd3083c2890cc61dc244a` | `SOURCE_APPROVED/TUESDAY/` |
| WED | FEED | `ISSUE010_WED_FEED_1080x1350.png` | 1122×1402 | `78d71c7e3e3b963ae6936debae01fbdac17b36692b65b9b40c659795fa3b00c4` | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | STORY 1 | `ISSUE010_WED_STORY_01_1080x1920.png` | 941×1672 | `166851212cdb8383a7f7757858724a7cdc7032523286744394df31bf6520eb6a` | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | STORY 2 | `ISSUE010_WED_STORY_02_1080x1920.png` | 941×1672 | `d7a5ad7dc87838fa4a12c6d729e973d46290fdd84576a36e31d76f52d3bc83ce` | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | STORY 3 | `ISSUE010_WED_STORY_03_1080x1920.png` | 941×1672 | `61a4de3417dd4b8508327c998d616a8b9a1ac77327334d977ac4e4615a4ec852` | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | BLOG/OG | `ISSUE010_WED_BLOG_OG_1200x628.png` | 1734×907 | `3d7388e35710fec90fa86c362495f416a464823bf41a0321cb1197630b5a14c7` | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | EMAIL HEADER | `ISSUE010_WED_EMAIL_HEADER_1200x627.png` | 1734×907 | `df62ac8b825ee380d6037e165b39536d6500bf0af21fcbbc2f18050bcf0c9a95` | `SOURCE_APPROVED/WEDNESDAY/` |
| THU | FEED | `ISSUE010_THU_FEED_1080x1350.png` | 1122×1402 | `2c5607264758dfd198e585b82f36fbd2468179af772726bfe46c3fb2987bf56e` | `SOURCE_APPROVED/THURSDAY/` |
| THU | STORY 1 | `ISSUE010_THU_STORY_01_1080x1920.png` | 941×1672 | `9c5bb701fad915deeef2313018d810ae861cafb7378948bafc922c53defa10e1` | `SOURCE_APPROVED/THURSDAY/` |
| THU | STORY 2 | `ISSUE010_THU_STORY_02_1080x1920.png` | 941×1672 | `7c5a66e3563f598c5da39f666ba24a0bc09497f1b9443f84e06a6a5f43e67fe0` | `SOURCE_APPROVED/THURSDAY/` |
| THU | STORY 3 | `ISSUE010_THU_STORY_03_1080x1920.png` | 941×1672 | `82d7b326523426a9e77fd3670620deaf4b6e07dda5fd7e3819ecc7085c46e0be` | `SOURCE_APPROVED/THURSDAY/` |
| THU | BLOG/OG | `ISSUE010_THU_BLOG_OG_1200x628.png` | 1733×907 | `3b5df2f9384b7ab4c308d41e6ac0420cb70c94bc62d4e92b6e802338ae6eacb9` | `SOURCE_APPROVED/THURSDAY/` |
| THU | EMAIL HEADER | `ISSUE010_THU_EMAIL_HEADER_1200x627.png` | 1734×907 | `babfccaaa211c346fad68cf1f8b145871cc76d15ee54a777a7b9b9dbf6799b94` | `SOURCE_APPROVED/THURSDAY/` |
| FRI | FEED | `ISSUE010_FRI_FEED_1080x1350.png` | 1122×1402 | `a3b771b09ca5381c9b319b020a8ba7d3d4e2b6d5126ae1b3f52382319f26b0a1` | `SOURCE_APPROVED/FRIDAY/` |
| FRI | STORY 1 | `ISSUE010_FRI_STORY_01_1080x1920.png` | 941×1672 | `56e9cbc8f19f70b7248e24e45ec404373b9a5c37b80a0e7fa5c54581dc1c3a5c` | `SOURCE_APPROVED/FRIDAY/` |
| FRI | STORY 2 | `ISSUE010_FRI_STORY_02_1080x1920.png` | 941×1672 | `62e5bd5c4ef756947a3f6302ac27d0ba283ea272af946da85a231ab94272a99c` | `SOURCE_APPROVED/FRIDAY/` |
| FRI | STORY 3 | `ISSUE010_FRI_STORY_03_1080x1920.png` | 941×1672 | `0a708d135b8a84a5c53595578cbfb9764d8c98f7e7987ada791defde476b231b` | `SOURCE_APPROVED/FRIDAY/` |
| FRI | BLOG/OG | `ISSUE010_FRI_BLOG_OG_1200x628.png` | 1733×907 | `69c70b0f047ca77908d867412515347cda6051d10531c98885bf52d950c4a4d8` | `SOURCE_APPROVED/FRIDAY/` |
| FRI | EMAIL HEADER | `ISSUE010_FRI_EMAIL_HEADER_1200x627.png` | 1734×907 | `443127d8842db7c102f100ce2966100bac2772fff7749db7c885822f74e1cd77` | `SOURCE_APPROVED/FRIDAY/` |
## ISSUE 010 — RENDERED VISUAL COPY AUTHORITY

Founder resolution. The 30 approved, checksum-locked production binaries are **authoritative for the text rendered inside the artwork**. They must not be regenerated, edited, replaced, or altered.

`ISSUE010_STORY_COPY_LOCK.md` and the Master Copy feed copy remain canonical **editorial and platform-copy** authorities, but they must **not** be read as requiring the artwork to reproduce every canonical line verbatim.

| Layer | Authority |
|---|---|
| Text rendered *inside* an asset | The approved binary |
| Caption / platform copy accompanying a post | Canonical editorial copy |

Story artwork publishes **as approved**. Do not overlay, reconcile, or supply "missing" Copy Lock language during execution. **Monday's issue-cover treatment is Founder-accepted** as the opening visual treatment for POSSIBILITY and is not a defect.

This resolves the apparent contradiction without rewriting historical editorial copy. The Issue 010 道 / ensō visual exception above is unchanged and remains non-canonical and non-precedent.

## ISSUE 010 — WEEKLY ARTICLE / EMAIL VISUAL AUTHORITY

Founder designation:

- **`ISSUE010_MON_BLOG_OG_1200x628.png` — canonical weekly article / featured / OG visual.**
- **`ISSUE010_MON_EMAIL_HEADER_1200x627.png` — canonical issue-level email header.**

Tuesday–Friday BLOG/OG and EMAIL HEADER assets remain preserved in the canonical production set but are **not execution authority** for the single weekly article or the single issue-level email.

## ISSUE 010 — SLUG vs PRODUCTION PERMALINK

The canonical editorial slug and the production URL are different things and both are correct:

| | |
|---|---|
| Canonical editorial slug | `issue-010-possibility` |
| Production article URL authority | `https://taoclinicaltouch.com/blog/2026/09/issue-010-possibility/` |

The production site uses a `/blog/YYYY/MM/{slug}/` permalink architecture. Founder accepts it; do not attempt to alter it. The production URL above is the CTA destination for all Issue 010 downstream execution.

## Checksum authority

- `ISSUE010_CHECKSUMS.sha256` — 30 production derivatives, path-labelled `APPROVED_ASSETS/<DAY>/`
- `ISSUE010_SOURCE_CHECKSUMS.sha256` — 30 source originals, path-labelled `SOURCE_APPROVED/<DAY>/`

Both validate natively with `shasum -a 256 -c` run from the Issue 010 packet root, following the Issue 008/009 persistence precedent.

## ISSUE 010 — VISUAL EXCEPTION / NON-PRECEDENT

During final Founder review, two decorative elements were identified throughout the Issue 010 visual set:

1. gold 道 / TAO character treatment
2. gold brush-circle / ensō-style treatment

These elements were introduced during visual generation. **They are NOT established canonical Tao visual branding.**

**Founder decision.** The existing elements are accepted for **ISSUE 010 — POSSIBILITY ONLY**. They must not be removed from Issue 010, and no Issue 010 image may be regenerated or modified because of their presence.

**Non-precedent directive.** Acceptance in Issue 010 does **not**:

- establish the 道 / TAO treatment as canonical branding
- establish the brush-circle / ensō as canonical branding
- authorize reuse in Issue 011
- modify the established Tao visual doctrine
- supersede previously approved visual authority

**Beginning with Issue 011**, neither the 道 / TAO decorative character treatment nor brush-circle / ensō-style imagery may be introduced unless separately and explicitly Founder-approved **before** visual production. Any proposed symbol, icon, character, decorative mark, motif, or brand device requires Founder approval before visual production. Where a recurring Tao visual identifier is required, return to the established Founder-approved visual system and the canonical natural-water ripple treatment, unless a later Founder directive explicitly supersedes it.

**Classification:** FOUNDER-ACCEPTED VISUAL EXCEPTION · NON-CANONICAL · NON-PRECEDENT · ISSUE 010 ONLY.

> A future executor must not infer from Issue 010 that the 道 / TAO or ensō treatments are canonical Tao branding. They are not.

## Rules

- Every feed asset carries the day's canonical Feed headline from `ISSUE010_MASTER_COPY.md`.
- Story artwork renders `ISSUE010_STORY_COPY_LOCK.md` text under the IDEA / TENSION / APPLICATION architecture.
- Do not crop, redraw, regenerate, substitute, recolor, or reinterpret an approved asset.
- Story 1/2/3 are discrete publishing objects for each weekday.
- Every image published to a platform requires objective accessibility alt text written from the actual rendered artwork.
- Canonical persistence is not publication authority. Publication remains a separate Founder gate.
