# ISSUE 011 — ASSET MANIFEST

**Status:** **FOUNDER APPROVED — VISUAL PRODUCTION SET PERSISTED.** 30/30 assets ingested and hash-verified.

**Visual production set:** **30/30 Founder-approved.**

**Rejected generations:** excluded from this packet. They carry **no production authority** and must not be introduced.

The Thursday and Friday Feed derivatives were corrected under Founder authority after an audit finding; see **Thursday and Friday Feed correction history** below. Both corrected binaries are Founder-authorized by explicit SHA-256 and are execution authority.

**Rejected generations:** excluded from this packet. They carry **no production authority** and must not be introduced.

**Binary source authority:** `ISSUE_011_APPROVED_ASSET_PACKET_FIXED.zip`
SHA-256 `a52253ad4c9f2064710e5cbf537a5bc42c96990a90faa1abfcaea902d61ef45a` — Founder-designated visual production authority for Issue 011.

## Authority distinction

| Directory | Authority |
|---|---|
| **`SOURCE_APPROVED/<DAY>/`** | **PROVENANCE AUTHORITY** — the exact Founder-approved generated originals, preserved byte-identical at their as-generated dimensions. Never normalized, cropped, recompressed, or edited. |
| **`APPROVED_ASSETS/<DAY>/`** | **EXECUTION AUTHORITY** — the authorized dimension-normalized production derivatives. These are the binaries referenced by WordPress, Buffer, and Brevo execution. |

Canonical directories are `APPROVED_ASSETS/` and `SOURCE_APPROVED/`. There is no `ASSETS/` directory in Issue 011.

## Normalization

**Founder-declared normalization:** dimension-only **LANCZOS** resize. **No crop. No redesign. No regeneration. No recompression intent. No creative alteration.** Source dimensions differ from production dimensions on all 30 assets, confirming the source originals are genuine unnormalized generations rather than copies of the derivatives.

### Measured normalization evidence

Aspect ratio was compared source-to-production for all 30 assets. **28 of 30 are pure uniform resamples** (aspect delta ≤ 0.0034 — rounding only): all 15 Story, all 5 Blog/OG, all 5 Email Header, and the MON/TUE/WED Feed derivatives, which resample from 1122×1402 sources at delta 0.000285.

The remaining two — the THU and FRI Feed derivatives — are **Founder-authorized corrections** rather than plain resamples, and are documented below. **No anamorphic-stretch binary remains in execution authority.**

## Thursday and Friday Feed correction history

Retained as provenance record. Neither superseded binary is execution authority; neither is present in the repository.

**Audit finding.** The originally supplied THU and FRI Feed production derivatives were found to be **full-frame anamorphic stretches** of their sources — THU ~25% vertical elongation (1254×1254 square source → 1080×1350), FRI ~5.5% horizontal (1092×1440 → 1080×1350). Pixel testing against candidate derivations confirmed stretch, not crop: no content was lost, geometry was distorted. The Founder accepted the finding and **rejected both as execution binaries**, limiting the defect to production normalization.

**First correction packet — not applied.** A replacement pair matched its stated hashes but was found on inspection to be *different artwork*, not re-normalized derivatives: Thursday changed scene and headline entirely, Friday was re-rendered with altered subhead, and both dropped the locked recurring bottom furniture. Applying it would have replaced approved creative content under cover of a normalization fix, so it was **failed closed and not applied**.

**Final correction packet — applied.** `ISSUE_011_FINAL_THU_FRI_CORRECTIONS.zip`, SHA-256 `34ea8a5a4b2e4f940497ef1b8f0f6e0cee71f2c9804e97335b552082f2606f74`.

| Day | Disposition | Authorized production SHA-256 |
|---|---|---|
| THU | **Editorial/creative correction — Founder-approved.** Resolves the discovered feed-spine divergence; the derivative now renders the canonical Thursday feed visual copy from `ISSUE011_MASTER_COPY.md`. **It therefore intentionally diverges from its `SOURCE_APPROVED/` provenance original, which renders superseded copy.** This divergence is authorized and is not a defect. | `3d19e490…e0e881` |
| FRI | **Proportional 4:5 crop/resize** of the Founder-approved provenance source. Not regenerated; no intentional creative or copy change. Verified against the source by pixel comparison — matches the proportional-crop derivation (mean abs luminance diff 3.3) and not the anamorphic-stretch derivation (28.6). | `fa439546…e0045d` |

Both were verified before application: authorized SHA-256 exact match, exact 1080×1350, valid PNG, and visual confirmation of rendered copy and locked recurring furniture. `SOURCE_APPROVED/` was not altered at any point in this sequence — all 30 source binaries remain byte-identical to the original approved packet.

### Thursday provenance note

For Thursday alone, `SOURCE_APPROVED/THURSDAY/ISSUE011_THU_FEED_1080x1350.png` (`9111652f…dd2545`) is **provenance only** and does not correspond to the rendered content of the execution binary. It is preserved unchanged as the historical approved original. For all other 29 assets, production and source render the same content.

## Production specifications

| Surface | Dimensions | Count |
|---|---:|---:|
| Feed (Instagram + Facebook) | 1080×1350 | 5 |
| Story (3 per day) | 1080×1920 | 15 |
| Blog / Facebook / OG header | 1200×628 | 5 |
| Email header | 1200×627 | 5 |
| **Total** | | **30** |

Six production assets per weekday, Monday–Friday.

## Issue 011 visual arc

| Day | Arc |
|---|---|
| Monday | change / information |
| Tuesday | restraint |
| Wednesday | proportion |
| Thursday | attention |
| Friday | integration / return to listening |

## Locked recurring furniture

```
THE TAO OF CLINICAL TOUCH
ISSUE 011 / RESPONSE
LISTEN. RESPOND. LISTEN AGAIN.
```

This furniture is fixed across the issue. Do not alter, re-letter, or reposition it.

## Visual doctrine

Issue 011 uses the established Founder-approved visual system and the canonical **natural-water ripple** treatment per `ADOBE_BRAND_MANIFEST.md`.

The Issue 010 gold 道 / TAO character and gold brush-circle / ensō treatments were a Founder-accepted exception for **Issue 010 only** — non-canonical and non-precedent. They do **not** carry forward into Issue 011.

## Production assets — `APPROVED_ASSETS/` (EXECUTION AUTHORITY)

| Day | Asset | Canonical filename | Required px | Actual px | Production SHA-256 | Founder | Repository path |
|---|---|---|---:|---:|---|---|---|
| MON | FEED | `ISSUE011_MON_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `c53f8927784659d35de0eaabab553ff9eae29b485e406df92f3a40737eb7f3ef` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | STORY 1 | `ISSUE011_MON_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `8559ada82ae4dc1fca76017a3d6c20165ad74f6a426c2da2d995731153077993` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | STORY 2 | `ISSUE011_MON_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `8c508d71a52c8c38a7b41a1ce6571123a7e6ccfce24215a015ed9e87b491799b` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | STORY 3 | `ISSUE011_MON_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `40267496c0a440d9d73402e9f05a4a0a93a29f8a7e328a34d5ca652164d1de25` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | BLOG/OG | `ISSUE011_MON_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `df8bf70e29e667895abdeb33243f11267ff07ba6e193acfa5bcdc953f6333301` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| MON | EMAIL HEADER | `ISSUE011_MON_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `11772cb2370ac58bd4a9ca90540db79f08fb9dd763a0b6c37fb6a4312f4f8949` | APPROVED | `APPROVED_ASSETS/MONDAY/` |
| TUE | FEED | `ISSUE011_TUE_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `15db0595bfbd605e9c84631d66d1fa9a2463c172e8a19986c8da3c3af9ae2ac8` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | STORY 1 | `ISSUE011_TUE_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `96286a6b57dbd0e1ed2ccfda6b5ee3ab94f5fef32986f8fe903d2cb2aa8b58d4` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | STORY 2 | `ISSUE011_TUE_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `e2442639dde8698510e97bc05d978f9188ea647c10661c822113e62c38879b37` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | STORY 3 | `ISSUE011_TUE_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `0a5c212bcb1f5ab5660d92e2ea9d074c9b9d2e2776cf8b4c3f7e549367252a6e` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | BLOG/OG | `ISSUE011_TUE_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `bb6103e74aeb0860ba304623cce1a18633188ebca270db0007d5d383a5f53833` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| TUE | EMAIL HEADER | `ISSUE011_TUE_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `6ade08442795ad1ea2e9219775691f2aec4af28bf0d93dafe964e824929c23dc` | APPROVED | `APPROVED_ASSETS/TUESDAY/` |
| WED | FEED | `ISSUE011_WED_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `62d7c75b963af5ae2f4caaab6c2b78b3a9ab9979ba79d9ca5678b6149a893fc5` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | STORY 1 | `ISSUE011_WED_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `47cb8a11daf892cd0c66d614da3732ad62cd103efc02faef30adfcd92337abf1` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | STORY 2 | `ISSUE011_WED_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `93dde271060d09d274f45feba6a1752ce714373ce541c2b5b01b85e1013e21f1` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | STORY 3 | `ISSUE011_WED_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `68eecba30d805a28214a6f2ce26cd04596155a81ddb18e7b2c50cef68ab3b5e8` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | BLOG/OG | `ISSUE011_WED_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `31646c5c70a1fc46b353a68bfb9d1647313041dcc5dd633dca6dad05e549310b` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| WED | EMAIL HEADER | `ISSUE011_WED_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `e99292b9cda84065470971be19b93e222ad6b7389a247d7d874e59dacbe484a3` | APPROVED | `APPROVED_ASSETS/WEDNESDAY/` |
| THU | FEED | `ISSUE011_THU_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `3d19e490de2d8f44cfee7be64787f6d0cca688322729a2bcff53b51c1fe0e881` | APPROVED — editorial/creative correction · **intentionally diverges from provenance source** | `APPROVED_ASSETS/THURSDAY/` |
| THU | STORY 1 | `ISSUE011_THU_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `bcbfba7f4fbec73847ffbbfcd8a4a966bf83464b1d5a677738d3f93132060def` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | STORY 2 | `ISSUE011_THU_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `a0c84d90bc2fcc2c5eecd89d6e9f1867f1bdd3825b6e2c72f47ad4174fd41e4a` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | STORY 3 | `ISSUE011_THU_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `76c6b1787503c013163e4271b2d2ff5f9ac0401cede8e17e6d10ad8ffe158a69` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | BLOG/OG | `ISSUE011_THU_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `8568655a7639a18d2a3bdb23be57b5c9bf4e2525c2f627ac16fc82acf5532cde` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| THU | EMAIL HEADER | `ISSUE011_THU_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `d146ca2749c76bd9c11f37f8790f1784daf47a62f95e8d4f2f28c0c8456a381e` | APPROVED | `APPROVED_ASSETS/THURSDAY/` |
| FRI | FEED | `ISSUE011_FRI_FEED_1080x1350.png` | 1080×1350 | 1080×1350 | `fa439546797ecb88fc83fe76b24dffeb0f193aa86daeb9f6944b59c5c3e0045d` | APPROVED — proportional 4:5 crop/resize of provenance source | `APPROVED_ASSETS/FRIDAY/` |
| FRI | STORY 1 | `ISSUE011_FRI_STORY_01_1080x1920.png` | 1080×1920 | 1080×1920 | `b4399f9c6df3956839359d60f8cf85311336b675ae9ddbc2440f416ad4707b4f` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | STORY 2 | `ISSUE011_FRI_STORY_02_1080x1920.png` | 1080×1920 | 1080×1920 | `648c3d209fea0ba72e1e0ac50cbd4ef0f575c1e21468ba2cb2e7f0d230387a49` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | STORY 3 | `ISSUE011_FRI_STORY_03_1080x1920.png` | 1080×1920 | 1080×1920 | `efa973121983107dc9635861b4a9918a110c4fab995798eabc00536f3cae6925` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | BLOG/OG | `ISSUE011_FRI_BLOG_OG_1200x628.png` | 1200×628 | 1200×628 | `fb91d51ca8cea392f533ce59fba00a17751540eaf6773f56f316dcdeabced087` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
| FRI | EMAIL HEADER | `ISSUE011_FRI_EMAIL_HEADER_1200x627.png` | 1200×627 | 1200×627 | `1d52bfeff9aabb4360da331b76002accd1249817b452f44a47716b3b4f851c8c` | APPROVED | `APPROVED_ASSETS/FRIDAY/` |
## Source originals — `SOURCE_APPROVED/` (PROVENANCE AUTHORITY)

Preserved unchanged at as-generated dimensions. Filenames are identical to the production derivatives; the directory determines which authority applies.

| Day | Asset | Canonical filename | Source px | Source SHA-256 | Founder | Repository path |
|---|---|---|---:|---|---|---|
| MON | FEED | `ISSUE011_MON_FEED_1080x1350.png` | 1122×1402 | `6e7c0dff23ee9c36a3cf395faeb1cd929c4d39973f28f8a24355bfd157f7d8c0` | APPROVED | `SOURCE_APPROVED/MONDAY/` |
| MON | STORY 1 | `ISSUE011_MON_STORY_01_1080x1920.png` | 941×1672 | `3b86bf27f338eae441d32c554c71d836b550619b507f4682c7fd2c439fe1c72c` | APPROVED | `SOURCE_APPROVED/MONDAY/` |
| MON | STORY 2 | `ISSUE011_MON_STORY_02_1080x1920.png` | 941×1672 | `1d03f57e381f4977f9a9571060293206d85b67780ea82c147b0c732a7970e5da` | APPROVED | `SOURCE_APPROVED/MONDAY/` |
| MON | STORY 3 | `ISSUE011_MON_STORY_03_1080x1920.png` | 941×1672 | `78508b9bc7ef0e308d19cd517dc96a33b7349a917f90c681f4aba71c17e88ee8` | APPROVED | `SOURCE_APPROVED/MONDAY/` |
| MON | BLOG/OG | `ISSUE011_MON_BLOG_OG_1200x628.png` | 1733×907 | `0bbf325978d62a710857377cfb27a3aae18f5f8d30450567f36a3b5b366f5533` | APPROVED | `SOURCE_APPROVED/MONDAY/` |
| MON | EMAIL HEADER | `ISSUE011_MON_EMAIL_HEADER_1200x627.png` | 1734×907 | `130b065dc3c6bea42ef096160185db8eb8b1b5c04bd56177fd3fab76d6a5f87d` | APPROVED | `SOURCE_APPROVED/MONDAY/` |
| TUE | FEED | `ISSUE011_TUE_FEED_1080x1350.png` | 1122×1402 | `f56287c14caf8a5e74de7c1866042072ee3416aea773c669aeaf964c8f78219d` | APPROVED | `SOURCE_APPROVED/TUESDAY/` |
| TUE | STORY 1 | `ISSUE011_TUE_STORY_01_1080x1920.png` | 941×1672 | `6b2b30b27bab4bc61cf539d68f8e4328a175fbe6545212f4a6cd6044da9af670` | APPROVED | `SOURCE_APPROVED/TUESDAY/` |
| TUE | STORY 2 | `ISSUE011_TUE_STORY_02_1080x1920.png` | 941×1672 | `ca6eb4914dba2c51894e6c8f7bef64fe93ba9420886927decdd06a1abbae27b1` | APPROVED | `SOURCE_APPROVED/TUESDAY/` |
| TUE | STORY 3 | `ISSUE011_TUE_STORY_03_1080x1920.png` | 941×1672 | `3dac724d3929987a83d4690bd2d1ee0936095bd463482e7594add6ef75bb11a7` | APPROVED | `SOURCE_APPROVED/TUESDAY/` |
| TUE | BLOG/OG | `ISSUE011_TUE_BLOG_OG_1200x628.png` | 1732×908 | `d6f38764cda1be017b4eb2af20bc1ebcede06ad45263572a0d84fd17551a475c` | APPROVED | `SOURCE_APPROVED/TUESDAY/` |
| TUE | EMAIL HEADER | `ISSUE011_TUE_EMAIL_HEADER_1200x627.png` | 1734×907 | `672ff66ddfa68e243a17d6d78b8027f506840cad29f9f5db0a5a410e9f300c7c` | APPROVED | `SOURCE_APPROVED/TUESDAY/` |
| WED | FEED | `ISSUE011_WED_FEED_1080x1350.png` | 1122×1402 | `3d95c84ac6a385e42340f07c8c7e49d24cdb9ca494dd4f8bef52fdd2e44f26e3` | APPROVED | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | STORY 1 | `ISSUE011_WED_STORY_01_1080x1920.png` | 941×1672 | `1e517b34338c85e992c96a7f713bd634e1ac764fc3b37404799407473ad8fbe7` | APPROVED | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | STORY 2 | `ISSUE011_WED_STORY_02_1080x1920.png` | 941×1672 | `0bd2160cdd62c39496178835b45789f754de09f9447de8ff67ecd343923a6dd2` | APPROVED | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | STORY 3 | `ISSUE011_WED_STORY_03_1080x1920.png` | 941×1672 | `29e4385d25acbe205daea51554e1304d72a3ade5d762b1d3d711bd7fc42094b6` | APPROVED | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | BLOG/OG | `ISSUE011_WED_BLOG_OG_1200x628.png` | 1734×907 | `34f2915b990e3e51ab6271087ccd52568e525419c67ce9da2d385566f5ba7492` | APPROVED | `SOURCE_APPROVED/WEDNESDAY/` |
| WED | EMAIL HEADER | `ISSUE011_WED_EMAIL_HEADER_1200x627.png` | 1734×907 | `e1dfc02c2d3994013e06da2a90f7842ee694e60e7ae0b3f5f1a81ba78f60f3bb` | APPROVED | `SOURCE_APPROVED/WEDNESDAY/` |
| THU | FEED | `ISSUE011_THU_FEED_1080x1350.png` | 1254×1254 | `9111652fe369586f5ee6c376a5720531d162aca1bb9c8d78732b5fb1fcdd2545` | APPROVED | `SOURCE_APPROVED/THURSDAY/` |
| THU | STORY 1 | `ISSUE011_THU_STORY_01_1080x1920.png` | 941×1672 | `3f056268aca03d061ce2625c7e9a21da2598e169bc71d8ffbb8ffd16d5ff22b7` | APPROVED | `SOURCE_APPROVED/THURSDAY/` |
| THU | STORY 2 | `ISSUE011_THU_STORY_02_1080x1920.png` | 941×1672 | `1e58a7dc9350251d28e372d8d374ac065991790eca609fe807a94846bd6d2819` | APPROVED | `SOURCE_APPROVED/THURSDAY/` |
| THU | STORY 3 | `ISSUE011_THU_STORY_03_1080x1920.png` | 941×1672 | `da2172dfaace2d54f1bd6f1ec1e3fc1d63e31b687d080aced6498e033d23a7ed` | APPROVED | `SOURCE_APPROVED/THURSDAY/` |
| THU | BLOG/OG | `ISSUE011_THU_BLOG_OG_1200x628.png` | 1734×907 | `0b24fc10e77a3b609a514ea67aae6f1dccc7d2321a41af47a9dd3456a1d946c8` | APPROVED | `SOURCE_APPROVED/THURSDAY/` |
| THU | EMAIL HEADER | `ISSUE011_THU_EMAIL_HEADER_1200x627.png` | 1734×907 | `68f9eae960c5832cd906c9e62539eff21ec07e2c725f00ce819691c1c7499ee5` | APPROVED | `SOURCE_APPROVED/THURSDAY/` |
| FRI | FEED | `ISSUE011_FRI_FEED_1080x1350.png` | 1092×1440 | `b2393de2d5eb750510d0b9a379700a4b62588bf4cb992185e8c6bfdfe10d761c` | APPROVED | `SOURCE_APPROVED/FRIDAY/` |
| FRI | STORY 1 | `ISSUE011_FRI_STORY_01_1080x1920.png` | 941×1672 | `b0598f8840e9af4666609e0b979cc737cc2054214e3db77105b85ff899c7712a` | APPROVED | `SOURCE_APPROVED/FRIDAY/` |
| FRI | STORY 2 | `ISSUE011_FRI_STORY_02_1080x1920.png` | 941×1672 | `e448d0db446a220c3be645d2a1fa02c511ee1c0d8f78bc62cf2e102fa56e57ec` | APPROVED | `SOURCE_APPROVED/FRIDAY/` |
| FRI | STORY 3 | `ISSUE011_FRI_STORY_03_1080x1920.png` | 941×1672 | `e582b80e0bff4669a099965a46f2a28bf9634e1f3dffe88c071fcdbdfb6c3929` | APPROVED | `SOURCE_APPROVED/FRIDAY/` |
| FRI | BLOG/OG | `ISSUE011_FRI_BLOG_OG_1200x628.png` | 1734×907 | `0d3af68709b1f3f9e3af9e0703b40f8e3154a4618e77d663fad75973db251e04` | APPROVED | `SOURCE_APPROVED/FRIDAY/` |
| FRI | EMAIL HEADER | `ISSUE011_FRI_EMAIL_HEADER_1200x627.png` | 1734×907 | `3f80030da97d57b885fd63e4b27e9d355297e2d6b2672a9143839bbdc0513ec9` | APPROVED | `SOURCE_APPROVED/FRIDAY/` |
## Checksum authority

- `ISSUE011_CHECKSUMS.sha256` — 30 production derivatives, path-labelled `APPROVED_ASSETS/<DAY>/`
- `ISSUE011_SOURCE_CHECKSUMS.sha256` — 30 source originals, path-labelled `SOURCE_APPROVED/<DAY>/`

Both validate natively with `shasum -a 256 -c` run from the Issue 011 packet root. Hashes were computed from the repository binaries and independently confirmed identical to the packet's supplied `SHA256SUMS.txt` and `SOURCE_SHA256SUMS.txt`.

## Rules

- Every feed asset carries the day's canonical Feed visual copy from `ISSUE011_MASTER_COPY.md`. Feed artwork is not built from Story copy.
- Story artwork renders `ISSUE011_STORY_COPY_LOCK.md` text under the IDEA / TENSION / APPLICATION architecture.
- Do not crop, redraw, regenerate, substitute, recolor, rename, or reinterpret an approved asset.
- Story 1/2/3 are discrete publishing objects for each weekday.
- Every image published to a platform requires objective accessibility alt text written from the actual rendered artwork.
- **Canonical persistence is not publication authority.** External execution remains a separate Founder gate.
