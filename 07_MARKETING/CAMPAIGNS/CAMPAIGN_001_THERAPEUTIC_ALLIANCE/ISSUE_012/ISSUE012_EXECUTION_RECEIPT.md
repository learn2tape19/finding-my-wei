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
> **Issue 012 itself remains NOT DEPLOYED.** No WordPress article, no media, no Buffer objects,
> no Brevo campaign. This notice records infrastructure readiness only — it is not deployment
> authority and does not begin execution.
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
