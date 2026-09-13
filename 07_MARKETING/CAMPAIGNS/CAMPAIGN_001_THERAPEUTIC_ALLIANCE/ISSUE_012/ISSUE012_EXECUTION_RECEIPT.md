# ISSUE 012 — EXECUTION RECEIPT

> ## ⚠️ SUPERSESSION NOTICE — September 13, 2026 (later same day)
>
> **This receipt remains a valid historical record. Several of its infrastructure
> conclusions have since been disproven and are superseded below.**
>
> The decision to stop was **correct on the evidence available at that checkpoint.**
> Nothing here is being retracted as a judgment error. What changed is the evidence,
> not the standard.
>
> A five-gate infrastructure verification completed later the same day established:
>
> | Original conclusion | Current status |
> |---|---|
> | WordPress **BLOCKED** — no write credential, `/users/me` 401 | **SUPERSEDED.** A WordPress application password was subsequently provisioned. Authenticated REST access is **verified**: `/wp-json/wp/v2/users/me?context=edit` → **HTTP 200**, user ID 1, `administrator`, `upload_files: true`. Permission-aware media preflight confirms `Allow: GET, POST` authenticated vs `GET` anonymous. |
> | Buffer **BLOCKED** — CLI not installed | **SUPERSEDED AND WITHDRAWN.** Buffer executes via **GraphQL**, not the CLI. Authentication, Tao Facebook and Instagram destination resolution, scheduled-queue readback, and single-object readback by ID all succeed. The missing historical CLI is **irrelevant** and was never a real blocker. |
> | Brevo constrained — "no Brevo image-upload tool available, so the Monday Landscape master has no path into that slot" | **SUPERSEDED.** The approved architecture **does not require** a Brevo image upload. Externally hosted WordPress HTTPS media is proven: sent campaign 36 carried a raw WordPress `<img src>` with `inlineImageActivation: false`, 11,341 delivered. |
> | Template 39 is not a reusable shell | **STILL CORRECT.** Re-verified against live HTML. Unchanged and untouched. |
> | Brevo plan boundary 2026-09-20 — watch item | **STILL CORRECT**, now formally recorded as a Founder/manual billing dependency. Not a technical failure. |
>
> **Distinguish carefully:**
> - **Historical execution result:** Issue 012 execution was stopped. Zero mutations. That stands.
> - **Current infrastructure readiness:** the cross-platform path is verified end to end.
>
> **At the time this notice was written, Issue 012 remained NOT DEPLOYED.** That is no longer
> true: see **ISSUE 012 — EXECUTION LOG** at the end of this file. WordPress media (25 objects,
> IDs 1615-1639) and the canonical article (post 1640, `future`) now exist. Buffer and Brevo
> remain at zero objects — **superseded: all three platforms are now populated. Buffer holds 25
> verified scheduled objects and Brevo campaign 41 is queued. See EXECUTION LOG, PART 3 (FINAL)
> for the authoritative 51/51 state.** Nothing is publicly visible.
>
> Current authority: `04_CAPABILITIES/PUBLISHING/TAO_PUBLISHING_EXECUTION_DOCTRINE.md`

**Status:** **EXECUTION BLOCKED — NO PLATFORM MUTATIONS PERFORMED.**
*(Historical status as of the attempt below. See supersession notice above.)*

**Attempt date:** September 13, 2026
**Repository state at attempt:** `b5c695fb889e8026bd749635804ea68dccb3e820` (main)
**Publication week targeted:** September 21–25, 2026 (America/New_York)

Nothing was created, staged, scheduled, published, or modified on WordPress, Buffer,
or Brevo. No approved copy or approved binary was altered. This receipt records
external state and access limitations. It is not production authority.

---

## Gate status carried into execution

| Gate | Status |
|---|---|
| Production completeness (Phase 7A) | **CLOSED / PASS** at `4825c28`, re-confirmed at `b5c695f` |
| Canonical assets | 25/25 · SHA-256 25/25 · dimensions 25/25 |
| Editorial package | article · email copy · schedule — all committed |
| Root duplicate housekeeping | COMPLETE (`b5c695f`) |
| External execution | **BLOCKED — see below** |

---

## Access preflight results

**Historical — read every row with the supersession notice at the top of this file.**
The "current status" column was added September 13, 2026 so no row can be read as current
authority on its own.

| Platform | Result (historical) | Evidence (historical) | Current status |
|---|---|---|---|
| WordPress — taoclinicaltouch.com | **BLOCKED — no write credential** | Site HTTP 200; `/wp-json/` HTTP 200; `/wp-json/wp/v2/users/me` **HTTP 401** | **SUPERSEDED — VERIFIED.** App password provisioned; `/users/me?context=edit` → **200**, user ID 1, `administrator`, `upload_files: true` |
| WordPress.com MCP | **BLOCKED — site not accessible** | `taoclinicaltouch.com` absent from the accessible-site list entirely | **STILL TRUE, AND IRRELEVANT.** The site is reached via its own REST API, not the WordPress.com MCP server |
| Buffer | **BLOCKED — CLI not installed** | `buffer` not on PATH; the `buffer` skill invokes `!buffer context` | **SUPERSEDED AND WITHDRAWN.** Never a real blocker. Buffer executes via GraphQL; both Tao destinations connected; queue and single-object readback verified |
| Brevo | **AVAILABLE** | Account `drew@learn2tape.com`, org `69e660956a08aaef49055093` | **STILL TRUE.** Plus: external WordPress-hosted media proven; no Brevo image upload required |

### WordPress detail

The site is live and its REST API is reachable. Authentication is by application
password (`/wp-admin/authorize-application.php`). No application password is available
to this session, and authenticated endpoints return 401.

The WordPress.com MCP server lists only three sites — learn2tape.com and two Boston
Bodyworker entries — all with `mcp_access: unavailable`. `taoclinicaltouch.com` is not
among them, so that server cannot reach the Tao site under any plan change.

### Buffer detail

The Buffer skill shells out to a `buffer` CLI that is not installed on this machine.
No Buffer API token is available to this session.

> **SUPERSEDED — September 13, 2026.** Both statements are wrong. The `buffer` CLI is
> obsolete, not required, and its absence is not a blocker. Buffer executes through the
> first-party **GraphQL API** at `https://api.buffer.com/graphql`, and a working credential
> **was** available locally the whole time. Verified: authentication, Tao Facebook
> (`6a3eb95f5ab6d2f106763fc9`) and Tao Instagram (`6a3eb89f5ab6d2f106763ca0`) both connected
> and unlocked, 25 scheduled objects read back, single-object readback by ID, and 25 of 25
> scheduled objects successfully using WordPress-hosted HTTPS media.
> See `control_plane/adapters/BUFFER_V1_ADAPTER.md`.

### Brevo detail

Brevo API access works. Verified read-only:

- Sender **id 3** — `Drew Freedman | Tao of Clinical Touch` / `drew@mail.taoclinicaltouch.com` — active.
- Issue 011 Campaign **40** — status `queued`, scheduled `2026-09-14T10:00:00-04:00`, unsent, 22-list inclusion set, estimated reach 11,300. Untouched.
- **No Issue 012 campaign exists.** No duplicate risk.

---

## Dependency chain — why Brevo availability does not unblock execution

Established Tao execution architecture (Issues 008–011, recorded in operating conventions):

```
WordPress media library  →  public HTTPS asset URLs
        ↓                            ↓
WordPress article        →      Buffer objects (Buffer has no upload tool;
   (CTA destination)                  images MUST be public HTTPS URLs)
        ↓
Brevo campaign (CTA points at the live article; header image required)
```

Every downstream object depends on WordPress. Consequences:

1. **Buffer** cannot be built — its 25 objects require public image URLs that only the
   WordPress media library produces in this architecture.
2. **Brevo** cannot be built even though the API is reachable — the campaign CTA must
   resolve to the live Issue 012 article, which does not exist, and the header image
   has no public URL.

### Additional Brevo finding — template 39 is not a reusable shell

`Tao — Weekly Issue Master` (template 39) is described as a master but currently holds
**Issue 011 content end to end**: subject, `ISSUE 011 · RESPONSE` eyebrow, the Issue 011
headline and body, and a CTA hard-linked to
`https://taoclinicaltouch.com/blog/2026/09/issue-011-response/`.

Issue 012 therefore requires newly composed campaign HTML built from the locked
`ISSUE012_EMAIL_COPY.md`, not a field swap on template 39. Editing template 39 in place
would also mutate the object Issue 011's queued campaign was built from — not done.

The template's header image is served from Brevo's content library
(`img.mailinblue.com`), not from WordPress. No Brevo image-upload tool is available to
this session, so the Issue 012 Monday Landscape master has no path into that slot here.

---

## Duplicate / collision checks (read-only, all clear)

| Check | Result |
|---|---|
| WordPress slug `issue-012-agency` | **free** — 0 posts returned |
| Brevo Issue 012 campaign | **none exists** |
| Issue 011 queued objects | intact and untouched |

Most recent published Tao posts: `issue-010-possibility` (Sep 7),
`changing-course-is-clinical-reasoning` (Aug 26),
`the-answer-may-change-before-it-is-spoken` (Aug 20). Issue 011 (post 1582) is `future`
status and correctly not publicly visible.

---

## Watch item — not a blocker

The Brevo plan period on record runs **2026-08-20 → 2026-09-20** (17,065 send credits).
The Issue 012 email is scheduled for **2026-09-21**, one day after that period ends.
This is expected to be a routine renewal boundary rather than a fault, but confirm the
plan renews and credits are available before the campaign is queued.

---

## What is required to unblock

1. **A WordPress application password for taoclinicaltouch.com** with author/editor
   rights — the single blocking dependency for the entire chain.
2. **A Buffer API token, or the `buffer` CLI installed and authenticated.**
3. Confirmation of the Brevo plan renewal past 2026-09-20.

> **SUPERSEDED — September 13, 2026.** Current state of this list:
>
> 1. **RESOLVED.** Application password provisioned; authenticated REST access verified
>    (user ID 1, `administrator`, `upload_files: true`).
> 2. **WITHDRAWN — never a real requirement.** Buffer works via GraphQL with the existing
>    local credential. No CLI, no new token.
> 3. **OPEN — Founder/manual billing check.** Confirm Brevo Starter renewal and send credits
>    beyond 2026-09-20 17:31 UTC before Issue 012 email scheduling. Billing dependency, not a
>    technical failure.
>
> Remaining bounded residual: a live WordPress multipart upload has not yet been executed under
> the new credential. Authorization is proven; execution resolves at the first real upload.

Per `CLAUDE_ISSUE011_EXECUTION_HANDOFF.md` item 9 — *"If credentials or destination
identity fail, STOP and record the limitation. Do not route around it."* — execution
stopped here. No workaround, alternate host, substitute asset, or partial deployment
was attempted.

---

## Receipt summary

| Field | Value |
|---|---|
| WordPress article | **NOT CREATED** |
| WordPress media staged | **0 / 25** |
| Buffer objects | **0 / 25** |
| Brevo campaign | **NOT CREATED** |
| Platform mutations performed | **0** |
| Approved copy or assets altered | **NONE** |
| Issue 011 objects disturbed | **NONE** |
| Repository SHA at attempt | `b5c695fb889e8026bd749635804ea68dccb3e820` |

**EXECUTION HELD — CREDENTIALS REQUIRED.**

---

# ISSUE 012 — EXECUTION LOG (September 13, 2026)

**Status:** **SUPERSEDED — see EXECUTION LOG, PART 2 at the end of this file.**
*(Historical: this stage ended held at Buffer. The hold was resolved by Founder direction and
Stage D subsequently executed in full. Stage E remains outstanding.)*

Supersedes the historical "no platform mutations performed" state above for this date.
WordPress objects now exist. **Do not re-upload or re-create them.**

## Stage A — Repository: PASS
- Repository HEAD at execution: `bf4150246e00feba02535bcd6a482f2a51993609`, parity with `origin/main`, tree CLEAN
- Production completeness gate: **CLOSED**, 0 failures
- Canonical checksums: **25/25 OK** against `ISSUE012_CHECKSUMS.sha256`

## Stage B — WordPress media: PASS (25/25)

All 25 Founder-approved masters uploaded via authenticated REST multipart POST as user ID 1.
**This closed the documented multipart-upload residual.** First upload returned HTTP 201.

Every asset was then retrieved **anonymously** over HTTPS and reconciled against its canonical
repository SHA-256.

**Result: 25/25 anonymous HTTP 200 + SHA-256 byte-identical. 0 mismatches.**
No regeneration, resize, recompression, or rename occurred. Filenames preserved exactly.

| WP Media ID | Canonical filename | Asset integrity |
|---|---|---|
| 1615 | `ISSUE-012_MONDAY_LANDSCAPE_1200x628.png` | VERIFIED |
| 1616 | `ISSUE-012_FRIDAY_FEED_1080x1350.png` | VERIFIED |
| 1617 | `ISSUE-012_FRIDAY_LANDSCAPE_1200x628.png` | VERIFIED |
| 1618 | `ISSUE-012_FRIDAY_STORY-01_1080x1920.png` | VERIFIED |
| 1619 | `ISSUE-012_FRIDAY_STORY-02_1080x1920.png` | VERIFIED |
| 1620 | `ISSUE-012_FRIDAY_STORY-03_1080x1920.png` | VERIFIED |
| 1621 | `ISSUE-012_MONDAY_FEED_1080x1350.png` | VERIFIED |
| 1622 | `ISSUE-012_MONDAY_STORY-01_1080x1920.png` | VERIFIED |
| 1623 | `ISSUE-012_MONDAY_STORY-02_1080x1920.png` | VERIFIED |
| 1624 | `ISSUE-012_MONDAY_STORY-03_1080x1920.png` | VERIFIED |
| 1625 | `ISSUE-012_THURSDAY_FEED_1080x1350.png` | VERIFIED |
| 1626 | `ISSUE-012_THURSDAY_LANDSCAPE_1200x628.png` | VERIFIED |
| 1627 | `ISSUE-012_THURSDAY_STORY-01_1080x1920.png` | VERIFIED |
| 1628 | `ISSUE-012_THURSDAY_STORY-02_1080x1920.png` | VERIFIED |
| 1629 | `ISSUE-012_THURSDAY_STORY-03_1080x1920.png` | VERIFIED |
| 1630 | `ISSUE-012_TUESDAY_FEED_1080x1350.png` | VERIFIED |
| 1631 | `ISSUE-012_TUESDAY_LANDSCAPE_1200x628.png` | VERIFIED |
| 1632 | `ISSUE-012_TUESDAY_STORY-01_1080x1920.png` | VERIFIED |
| 1633 | `ISSUE-012_TUESDAY_STORY-02_1080x1920.png` | VERIFIED |
| 1634 | `ISSUE-012_TUESDAY_STORY-03_1080x1920.png` | VERIFIED |
| 1635 | `ISSUE-012_WEDNESDAY_FEED_1080x1350.png` | VERIFIED |
| 1636 | `ISSUE-012_WEDNESDAY_LANDSCAPE_1200x628.png` | VERIFIED |
| 1637 | `ISSUE-012_WEDNESDAY_STORY-01_1080x1920.png` | VERIFIED |
| 1638 | `ISSUE-012_WEDNESDAY_STORY-02_1080x1920.png` | VERIFIED |
| 1639 | `ISSUE-012_WEDNESDAY_STORY-03_1080x1920.png` | VERIFIED |

URL pattern: `https://taoclinicaltouch.com/wp-content/uploads/2026/09/<filename>`

One transient TLS fault (`SSL_read ... bad record mac`, HTTP 000) interrupted the batch.
Server state was inspected before any retry and confirmed the failed object had **not** landed;
no duplicate was created. Retry succeeded.

## Stage C — WordPress article: PASS

| Field | Value |
|---|---|
| Post ID | **1640** |
| Title | The Clinical Practice of Agency |
| Slug | `issue-012-agency` |
| Status | `future` |
| Scheduled | `2026-09-21T11:45:00Z` = **Mon Sep 21, 2026 7:45 AM ET** |
| Featured media | **1615** — Monday LANDSCAPE 1200x628 |
| Category | 25 — Therapeutic Alliance |
| Author | 1 — Drew Freedman |
| Expected permalink | `https://taoclinicaltouch.com/blog/2026/09/issue-012-agency/` |

Independent authenticated readback: **all 9 field checks PASS.** Body content stored verbatim —
745 words, 5 `<h3>` section headings, byte-identical to the converted canonical article.
Anonymous fetch of the permalink returns 404, correct for a `future` post.

Duplicate check before creation: 0 posts with slug `issue-012-agency`.

**Excerpt:** omitted. No Founder-approved excerpt or meta description exists in the Issue 012
package. Per the handoff EXECUTION HOLD RULE, no editorial copy was invented. The site runs no
SEO plugin, consistent with the Issue 007 accepted exception.

## Stage D — Buffer: **HELD — NOT EXECUTED**

**0 Buffer objects created.** See the open question below.

## Stage E — Brevo: **NOT REACHED**

**0 Brevo objects created or modified.** Template 39 untouched. Issue 011 Campaign 40 untouched.

## Open question blocking Stage D

`ISSUE-012_AGENCY_VISUAL_HANDOFF.md` presents one block per day headed
`### Feed copy — LOCKED`, containing: day headline, body, bolded supporting line, hashtags.

Issue 011 — the immediately preceding completed issue, and the reference the handoff's
EXECUTION HOLD RULE directs us to — used an explicit **two-part** structure:
`### Feed visual copy` (headline + supporting line, baked into the image) and
`### Canonical feed caption` (the text actually posted to Buffer). Its published captions
**excluded** the headline and supporting line.

Issue 012 does not make that separation. The approved Issue 012 feed images already carry both
the headline and the supporting line as rendered typography.

Therefore the Buffer caption text cannot be established with confidence:

- **Reading A** — post the LOCKED block verbatim, headline and supporting line included.
  Honors "do not alter approved copy" literally; duplicates text already in the image and
  departs from the Issue 011 caption convention.
- **Reading B** — post body + hashtags only, matching Issue 011.
  Matches convention; requires deleting lines from a block marked LOCKED.

Both readings change public-facing copy on 10 feed objects across Facebook and Instagram.
Per the handoff rule — *"If the value still cannot be established with confidence, HOLD that
step and report exactly what is missing. Do not alter approved copy or assets to solve an
execution problem"* — Stage D was held pending Founder direction.

## Resolved dependency

Brevo renewal confirmed by Founder in the billing interface: Starter, monthly, 40,000 emails/month,
next credit renewal **September 20, 2026 1:31 PM ET**. The Gates 3-5 billing dependency is
**CLOSED**. It is no longer a blocker.

## Confirmations

| | |
|---|---|
| Approved assets regenerated/resized/recompressed/renamed | **NO** — 25/25 byte-identical |
| Approved editorial copy rewritten | **NO** |
| Issue 011 objects modified | **NO** |
| Brevo Template 39 modified | **NO** |
| Buffer objects created | **NO** |
| Brevo objects created | **NO** |
| Issue 012 publicly visible | **NO** — article is `future`, nothing published |

---

# ISSUE 012 — EXECUTION LOG, PART 2 (September 13, 2026)

**Status:** **SUPERSEDED — see EXECUTION LOG, PART 3 (FINAL) at the end of this file.**
*(Historical: Stage E was blocked by a permission gate at this point. Founder subsequently
authorized the campaign; Stage E executed and verified as Brevo campaign 41.)*

Supersedes the "HELD AT BUFFER STAGE" status above. The Buffer hold was resolved by Founder
direction (Reading B) and Stage D executed in full.

## Founder direction applied — Feed caption interpretation (Reading B)

For Issue 012 Feed posts, the day headline and the supporting line are **approved visual copy
baked into the Feed asset** (visually confirmed present in the rendered 1080x1350 masters).
The canonical Buffer Feed caption is therefore **body + hashtags only**.

This is an execution interpretation of already-approved copy. **The body and hashtags were not
rewritten, paraphrased, reordered, or altered.** Only two elements were removed per day — the
headline and the supporting line — and markdown emphasis markers were stripped, following the
Issue 011 convention. Applied identically to all five days on both Tao Facebook and Tao Instagram.

| Day | Removed headline | Removed supporting line |
|---|---|---|
| Monday | THE CHANGE IS NOT YOURS | You can create the conditions. / The body still has to choose. |
| Tuesday | BETTER ON THE TABLE IS NOT THE FINISH LINE | Change observed is not always change owned. |
| Wednesday | LET THEM TRY | At some point, your hands have to leave. |
| Thursday | KNOW WHEN TO STEP BACK | Guidance creates possibility. / Space allows ownership. |
| Friday | THEY HAVE TO OWN THE CHANGE | Agency is what remains when the practitioner steps away. |

## Stage D — Buffer: PASS (25/25)

Preflight: authenticated (account `6a3d317b545b077504a47719`, org `6a3d317b545b077504a4771b`);
Tao Facebook `6a3eb95f5ab6d2f106763fc9` and Tao Instagram `6a3eb89f5ab6d2f106763ca0` both
**connected and unlocked**; duplicate check across the Sep 21-25 window returned **0 existing
objects** before any creation.

Structure follows the Issue 011 precedent exactly: Feed posts to **both** channels carrying the
caption; Story frames to **Instagram only** with no caption.
Facebook metadata `type: post`; Instagram Feed `type: post, shouldShareToFeed: true`;
Instagram Story `type: story, shouldShareToFeed: false`. `schedulingType: automatic`.

**Every object was independently retrieved by ID after creation** via `post(input:{id})` and
reconciled on seven fields: id, status, dueAt, channelId, caption text, attached media URL, and
platform metadata.

**Result: 25/25 independent readback PASS. 0 failures.**
All 25 timestamps reconcile against the canonical publishing schedule (EDT, UTC-4):
Feed 12:00Z = 8:00 AM ET, Story 1 13:00Z = 9:00 AM ET, Story 2 15:00Z = 11:00 AM ET,
Story 3 17:00Z = 1:00 PM ET.

| Day | Role | Channel | ET | dueAt (UTC) | Buffer object ID | Readback |
|---|---|---|---|---|---|---|
| Monday | FEED | FB | 8:00 AM ET | `2026-09-21T12:00:00.000Z` | `6aa6a7c332ba2073e81c925a` | PASS |
| Monday | FEED | IG | 8:00 AM ET | `2026-09-21T12:00:00.000Z` | `6aa6a7ee66679b076f2a3919` | PASS |
| Monday | STORY-01 | IG | 9:00 AM ET | `2026-09-21T13:00:00.000Z` | `6aa6a7efeba7bc567797c442` | PASS |
| Monday | STORY-02 | IG | 11:00 AM ET | `2026-09-21T15:00:00.000Z` | `6aa6a7ef4cc07ffa4d369096` | PASS |
| Monday | STORY-03 | IG | 1:00 PM ET | `2026-09-21T17:00:00.000Z` | `6aa6a7f066679b076f2a3957` | PASS |
| Tuesday | FEED | FB | 8:00 AM ET | `2026-09-22T12:00:00.000Z` | `6aa6a7f132ba2073e81c9728` | PASS |
| Tuesday | FEED | IG | 8:00 AM ET | `2026-09-22T12:00:00.000Z` | `6aa6a7f1f7b1958d5ce89f1d` | PASS |
| Tuesday | STORY-01 | IG | 9:00 AM ET | `2026-09-22T13:00:00.000Z` | `6aa6a7f232ba2073e81c975a` | PASS |
| Tuesday | STORY-02 | IG | 11:00 AM ET | `2026-09-22T15:00:00.000Z` | `6aa6a7f2f7b1958d5ce89f51` | PASS |
| Tuesday | STORY-03 | IG | 1:00 PM ET | `2026-09-22T17:00:00.000Z` | `6aa6a7f34cc07ffa4d3690e0` | PASS |
| Wednesday | FEED | FB | 8:00 AM ET | `2026-09-23T12:00:00.000Z` | `6aa6a7f34cc07ffa4d36911a` | PASS |
| Wednesday | FEED | IG | 8:00 AM ET | `2026-09-23T12:00:00.000Z` | `6aa6a7f466679b076f2a39a6` | PASS |
| Wednesday | STORY-01 | IG | 9:00 AM ET | `2026-09-23T13:00:00.000Z` | `6aa6a7f432ba2073e81c97a3` | PASS |
| Wednesday | STORY-02 | IG | 11:00 AM ET | `2026-09-23T15:00:00.000Z` | `6aa6a7f532ba2073e81c97ce` | PASS |
| Wednesday | STORY-03 | IG | 1:00 PM ET | `2026-09-23T17:00:00.000Z` | `6aa6a7f6bcabda92e1b01072` | PASS |
| Thursday | FEED | FB | 8:00 AM ET | `2026-09-24T12:00:00.000Z` | `6aa6a7f64cc07ffa4d369140` | PASS |
| Thursday | FEED | IG | 8:00 AM ET | `2026-09-24T12:00:00.000Z` | `6aa6a7f732ba2073e81c97f3` | PASS |
| Thursday | STORY-01 | IG | 9:00 AM ET | `2026-09-24T13:00:00.000Z` | `6aa6a7f7bcabda92e1b010ab` | PASS |
| Thursday | STORY-02 | IG | 11:00 AM ET | `2026-09-24T15:00:00.000Z` | `6aa6a7f84cc07ffa4d3691c7` | PASS |
| Thursday | STORY-03 | IG | 1:00 PM ET | `2026-09-24T17:00:00.000Z` | `6aa6a7f84cc07ffa4d3691ec` | PASS |
| Friday | FEED | FB | 8:00 AM ET | `2026-09-25T12:00:00.000Z` | `6aa6a7f966679b076f2a39f5` | PASS |
| Friday | FEED | IG | 8:00 AM ET | `2026-09-25T12:00:00.000Z` | `6aa6a7faeba7bc567797c5d0` | PASS |
| Friday | STORY-01 | IG | 9:00 AM ET | `2026-09-25T13:00:00.000Z` | `6aa6a7fabcabda92e1b010d3` | PASS |
| Friday | STORY-02 | IG | 11:00 AM ET | `2026-09-25T15:00:00.000Z` | `6aa6a7fb66679b076f2a3a20` | PASS |
| Friday | STORY-03 | IG | 1:00 PM ET | `2026-09-25T17:00:00.000Z` | `6aa6a7fbbcabda92e1b0110c` | PASS |

Every attached image is a checksum-verified WordPress-hosted HTTPS URL from Stage B.

## Stage E — Brevo: **BLOCKED — PERMISSION GATE**

**0 Brevo objects created or modified.** Template 39 untouched. Issue 011 Campaign 40 untouched.

The campaign was fully composed and pre-verified, but the create call was **denied by the
session's permission classifier**. This is an environmental authorization gate on a
mutation that would queue mail to approximately 11,300 recipients. It is **not** a doctrine STOP
condition, not an API failure, and not a canonical-source discrepancy. No workaround was
attempted and no alternate transport was used.

Prepared and verified, ready to submit unchanged:

| Field | Value |
|---|---|
| Name | Tao Issue 012 - Agency |
| Sender | ID **3** - Drew Freedman \| Tao of Clinical Touch <drew@mail.taoclinicaltouch.com> |
| Reply-to | drew@learn2tape.com |
| Subject | When does the change become theirs? |
| Preheader | Better movement is one thing. Owning it is another. |
| Scheduled | **2026-09-21T10:00:00-04:00** = Mon Sep 21, 10:00 AM ET |
| Recipients | 22 lists - `[2,5,6,7,8,10,44-59]`, matching Campaigns 36 and 40 |
| CTA target | `https://taoclinicaltouch.com/blog/2026/09/issue-012-agency/` (post 1640) |
| Image | `.../2026/09/ISSUE-012_MONDAY_LANDSCAPE_1200x628.png` (media 1615, checksum-verified) |
| inlineImageActivation | `false` - external WordPress media, per proven Campaign 36 pattern |
| utmCampaign | tao issue 012 |

Pre-submission content verification: all 20 approved email paragraphs present **verbatim**,
subject and preheader exact, CTA label exact, sign-off present. Brevo duplicate check: **no
Issue 012 campaign exists**; the only draft in the account is an unrelated Learn2Tape item.

Template 39 was **not** used, referenced, modified, or read into the campaign.

## Stage F — Reconciliation

| Layer | Objects | Verified | Reconciles to schedule |
|---|---|---|---|
| WordPress media | 25 | 25/25 SHA-256 byte-identical | n/a |
| WordPress article | 1 | 9/9 field checks | Mon 7:45 AM ET |
| Buffer | 25 | 25/25 independent readback | 25/25 |
| Brevo | 0 | - | **BLOCKED** |

**50 of 51 canonical publication objects are queued and verified.** The outstanding object is the
Monday 10:00 AM ET email.

## Stage G — Receipt

This record. No credentials, tokens, or PII recorded.

## Confirmations

| | |
|---|---|
| Approved assets regenerated/resized/recompressed/renamed | **NO** - 25/25 byte-identical |
| Approved editorial copy rewritten or paraphrased | **NO** |
| Issue 011 objects modified | **NO** |
| Brevo Template 39 modified | **NO** |
| Brevo objects created or modified | **NO** |
| Anything published publicly yet | **NO** - article `future`, Buffer scheduled, nothing live |

---

# ISSUE 012 — EXECUTION LOG, PART 3 — FINAL (September 13, 2026)

**Status:** **EXECUTION COMPLETE. 51/51 CANONICAL PUBLICATION OBJECTS QUEUED AND VERIFIED.**

Supersedes the "Stage E BLOCKED" status above. Founder authorized the single Issue 012 Brevo
campaign creation; Stage E executed and verified.

## Stage E — Brevo: PASS

| Field | Value | Verified |
|---|---|---|
| Campaign ID | **41** | PASS |
| Name | Tao Issue 012 — Agency | PASS |
| Status | `queued` | PASS |
| Scheduled | `2026-09-21T10:00:00.000-04:00` = **Mon Sep 21, 10:00 AM ET** | PASS — matches canonical schedule |
| Sender | ID **3** — drew@mail.taoclinicaltouch.com | PASS |
| Reply-to | drew@learn2tape.com | PASS |
| Subject | When does the change become theirs? | PASS — exact |
| Preheader | Better movement is one thing. Owning it is another. | PASS — exact |
| Recipients | 22 lists `[2,5,6,7,8,10,44-59]` | PASS — identical to Campaigns 36 and 40 |
| Estimated reach | 11,295 | — |
| CTA target | `https://taoclinicaltouch.com/blog/2026/09/issue-012-agency/` | PASS — resolves to post 1640 |
| Image | `.../2026/09/ISSUE-012_MONDAY_LANDSCAPE_1200x628.png` (media 1615) | PASS — anonymous 200, SHA-256 match |
| inlineImageActivation | `false` | PASS — external WordPress media |
| utmCampaign | tao issue 012 | PASS |
| Body | all 20 approved paragraphs, verbatim | PASS |

Independent readback confirmed the stored `htmlContent` is byte-identical to what was submitted.

### Sender-name field note — verified benign, not a mismatch

Campaign 41 stores `sender.name` as the Brevo token `[DEFAULT_FROM_NAME]` rather than the
literal string, which differs from Campaigns 36, 38, and 40. This was investigated before being
accepted rather than assumed harmless.

**Campaign 35 (Issue 007) stored the same `[DEFAULT_FROM_NAME]` token with sender ID 3 and sent
successfully to 11,352 recipients.** The token resolves to the sender record's configured name at
send time. Sender identity is unchanged and correct. No corrective mutation was made, and none is
required.

### Creation note

The first create attempt returned HTTP 400 `missing_parameter` — the Brevo write API expects
`recipients.listIds` while the read API returns `recipients.lists`. No campaign was created by
that error. The corrected call used the **same 22 list IDs**; no recipient configuration was
changed.

## Stage F — Final cross-platform reconciliation: 51/51

| Layer | Objects | Verification | Reconciles to canonical schedule |
|---|---|---|---|
| WordPress media | 25 | 25/25 anonymous SHA-256 byte-identical | n/a |
| WordPress article | 1 | 9/9 authenticated field checks | Mon 7:45 AM ET |
| Buffer | 25 | 25/25 independent readback by ID | 25/25 |
| Brevo | 1 | 14/14 field checks + body verbatim | Mon 10:00 AM ET |
| **Total** | **51** | **51/51 VERIFIED** | **51/51** |

### Publication week — Sep 21–25, 2026 (America/New_York, EDT)

| Time (ET) | Object | Platform ID | Status |
|---|---|---|---|
| Mon 7:45 AM | Canonical article — The Clinical Practice of Agency | WP post 1640 | `future` |
| Mon 8:00 AM | Feed — THE CHANGE IS NOT YOURS | Buffer FB + IG | scheduled |
| Mon 9:00 / 11:00 AM / 1:00 PM | Story 1 / 2 / 3 | Buffer IG ×3 | scheduled |
| Mon 10:00 AM | Weekly email | Brevo campaign 41 | `queued` |
| Tue 8:00 AM | Feed — BETTER ON THE TABLE IS NOT THE FINISH LINE | Buffer FB + IG | scheduled |
| Tue 9:00 / 11:00 AM / 1:00 PM | Story 1 / 2 / 3 | Buffer IG ×3 | scheduled |
| Wed 8:00 AM | Feed — LET THEM TRY | Buffer FB + IG | scheduled |
| Wed 9:00 / 11:00 AM / 1:00 PM | Story 1 / 2 / 3 | Buffer IG ×3 | scheduled |
| Thu 8:00 AM | Feed — KNOW WHEN TO STEP BACK | Buffer FB + IG | scheduled |
| Thu 9:00 / 11:00 AM / 1:00 PM | Story 1 / 2 / 3 | Buffer IG ×3 | scheduled |
| Fri 8:00 AM | Feed — THEY HAVE TO OWN THE CHANGE | Buffer FB + IG | scheduled |
| Fri 9:00 / 11:00 AM / 1:00 PM | Story 1 / 2 / 3 | Buffer IG ×3 | scheduled |

No deviation from `ISSUE012_PUBLISHING_SCHEDULE.md` in any object, date, time, destination, or
timezone offset.

## Isolation verification — adjacent objects untouched

| Object | Baseline | Current | Result |
|---|---|---|---|
| Brevo Campaign 40 (Issue 011) | `modifiedAt` 2026-09-08T19:21:00-04:00 | identical, still `queued` for Sep 14 | **UNTOUCHED** |
| Brevo Template 39 | `modifiedAt` 2026-09-09T16:21:13Z | identical; still holds the Issue 011 CTA | **UNTOUCHED** |
| Buffer Issue 011 objects | 25 scheduled Sep 14–18 | unchanged | **UNTOUCHED** |
| Issue 012 approved assets | 25 canonical SHA-256 | unchanged in repo and byte-identical on WordPress | **UNTOUCHED** |
| Issue 012 locked editorial copy | committed | unchanged | **UNTOUCHED** |

## Stage G — Receipt

This record. Object IDs, URLs, timestamps, and verification results persisted.
**No credentials, tokens, or PII recorded.**

## Dependencies — all closed

| Dependency | Status |
|---|---|
| WordPress multipart-upload residual | **CLOSED** — first upload HTTP 201; 25/25 succeeded |
| Brevo renewal past 2026-09-20 | **CLOSED** — Founder confirmed: Starter, monthly, 40,000/month, renews Sep 20 1:31 PM ET |
| Feed caption interpretation | **CLOSED** — Founder approved Reading B; applied to all 10 Feed objects |

## Final confirmations

| | |
|---|---|
| Approved assets regenerated/resized/recompressed/renamed | **NO** — 25/25 byte-identical |
| Approved editorial copy rewritten or paraphrased | **NO** |
| Issue 011 objects modified | **NO** |
| Brevo Template 39 modified | **NO** |
| Brevo Campaign 40 modified | **NO** |
| Additional campaigns created | **NO** — exactly one (41) |
| Buffer objects modified after creation | **NO** |
| Anything published publicly yet | **NO** — all objects future-dated/queued for Sep 21–25 |

**ISSUE 012 QUEUED AND VERIFIED — 51/51.**
