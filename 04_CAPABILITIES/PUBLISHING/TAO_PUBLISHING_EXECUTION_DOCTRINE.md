# Tao Publishing Execution Doctrine

**Status:** CURRENT AUTHORITY
**Effective:** September 13, 2026
**Scope:** Tao of Clinical Touch weekly publication execution across WordPress, Buffer, and Brevo
**Supersedes:** Buffer CLI execution doctrine; Phase 7A `BLOGOG` + `EMAILHEADER` core-role language
**Control plane:** This doctrine operates *inside* the Finding My Wei Publishing Control Plane
(`04_CAPABILITIES/PUBLISHING/control_plane/`). It is not a parallel Tao-specific publishing system.

---

## Why this document exists

The execution path below was verified end to end against live production infrastructure on
September 13, 2026 across five verification gates. Before that verification, each issue's
execution rediscovered the same facts — and in at least one case (Issue 012) stopped on a
blocker that did not exist.

This document converts that verified path into inherited institutional capability so future
issues execute it rather than re-derive it.

**This is a documentation standard. It authorizes nothing by itself.** Deployment authority
still comes from Founder approval and the production completeness gate.

---

## 1. The verified architecture

```
GitHub canonical package
        ↓  (authenticated WordPress REST API, HTTP Basic over HTTPS)
WordPress media library
        ↓  (anonymous public HTTPS + SHA-256 checksum reconciliation)
Public HTTPS media URL
        ├─────────────→  Buffer GraphQL scheduled objects
        └─────────────→  Brevo campaign HTML (external <img src>)
        ↓
Independent platform readback
```

Every link is proven in production, not inferred:

| Link | Evidence |
|---|---|
| GitHub → WordPress | 22 `ISSUE011` media items, all `author: 1`, uploaded via REST 2026-09-08 in a 30-second window |
| WordPress → public HTTPS | Canonical repo SHA-256 == anonymously retrieved SHA-256, byte-identical, no re-encode |
| Public HTTPS → Buffer | 25 of 25 scheduled Tao objects reference `taoclinicaltouch.com/wp-content/` media |
| Public HTTPS → Brevo | Campaign 36 (sent) carried a raw WordPress `<img src>` with `inlineImageActivation: false`; 11,341 delivered |
| Metric interpretation | Per-list `campaignStats` rows are **not** disjoint; they must never be summed. See §6 *Metric interpretation*. |
| Independent readback | Buffer `post(input:{id})` single-object query reconciles destination, time, and media |

---

## 2. WordPress REST doctrine

| Property | Value |
|---|---|
| Destination | `taoclinicaltouch.com` |
| Execution interface | WordPress REST API — `/wp-json/wp/v2/` |
| Authentication | WordPress Application Password + HTTP Basic authentication, HTTPS only |
| Publishing identity | Drew Freedman — WordPress user ID **1**, role `administrator` |
| Credential names | `TAO_WP_USERNAME`, `TAO_WP_APP_PASSWORD` |

`TAO_WP_USERNAME` is the full email-form login, not a short slug.

### Required capabilities

The publishing identity must present, at minimum:

- `upload_files`
- `edit_posts`
- `publish_posts`
- `edit_published_posts`

### Authenticated preflight — required before any mutation

```
GET /wp-json/wp/v2/users/me?context=edit
```

Must return **HTTP 200** and the expected user ID, role, and capability set.
`context=edit` is required: it returns the private capability block, which proves a real
authenticated session rather than an anonymous read. A 401 here is a STOP condition.

### Permission-aware media preflight

WordPress computes the `Allow` header by running each endpoint's `permission_callback` for the
current request. The header therefore reflects *this credential's* authorization, not merely
what the route declares.

| Request | Expected `Allow` |
|---|---|
| `OPTIONS /wp-json/wp/v2/media` — anonymous | `GET` |
| `OPTIONS /wp-json/wp/v2/media` — authenticated | `GET, POST` |

`POST` appearing only under authentication is **acceptable pre-mutation evidence that the
authenticated identity passes the media-create permission callback.**

**Bounded residual — state it, do not hide it.** This proves *authorization*, not *execution*.
Environmental failure modes remain possible (uploads-directory permissions, a security plugin
filtering application-password writes, a WAF rejecting multipart bodies). They are not
architectural, and they resolve unambiguously at the first real upload. Record the residual in
the receipt; do not manufacture a disposable test object to chase it without authorization.

### Known platform behaviours

- Media upload requires a **multipart form body** (`-F`), not a binary payload with a
  `Content-Disposition` header.
- Elementor pages store rendered content in the `_elementor_data` postmeta, **not**
  `post_content`. REST updates to `post_content` do not change rendered output.
- Elementor HTML belongs in the `html.default` widget, not `text-editor` — `text-editor`
  applies `wp_kses_post`, which strips CSS properties.

---

## 3. Credential-handling doctrine

Secrets must **never** be:

- committed to the repository
- written into destination registries or repository configuration
- printed to a terminal, log, or transcript
- embedded in execution receipts
- passed in a process argument list where `ps` can read them

**Required handling:**

- Read credentials from the environment or an explicit secret manager reference.
- When a tool needs the secret on a command line, pass it through a `600`-mode config file
  (for example `curl --config`) and delete that file when the operation completes.
- Confirm credential *presence* by reporting name, presence, and length only.
- Redact secrets from every exception, log line, and error message.

An application password inherits the full capability set of its user. Regenerating the password
does not change authorization; re-run the preflight in §2 to confirm the new credential.

---

## 4. Media integrity and checksum doctrine

**Canonical visual authority remains GitHub.** WordPress is a transport and hosting surface,
never the source of truth.

### The production rule

```
Approved repository binary
    → WordPress upload
    → anonymous public HTTPS retrieval (no auth header, no Referer)
    → SHA-256 comparison against the canonical repository hash
```

**A successful WordPress upload response alone does not close the asset gate.**

A URL is authorized for Buffer or Brevo use only when:

```
canonical SHA-256  ==  publicly retrieved SHA-256
```

A mismatch is a STOP condition. It means the platform transformed the approved master —
recompression, resize, format conversion, or substitution — and the downstream objects must not
be built on it.

### Non-regeneration rule (preserved)

No downstream platform may regenerate, resize, recompress, reinterpret, or substitute an
approved production master unless explicitly authorized by the Founder. Preserve approved files
byte-for-byte. Claim checksum verification only when it was actually performed.

---

## 5. Buffer execution doctrine

### Current authority: GraphQL

**Buffer executes through the first-party GraphQL API at `https://api.buffer.com/graphql`**
using `Authorization: Bearer <apiKey>`.

The historical `buffer` CLI is **obsolete and is not an execution blocker.** Its absence from
`PATH` must never again be recorded as a Buffer blockage. The credential the CLI originally
wrote remains valid and is read directly.

| Property | Value |
|---|---|
| Endpoint | `https://api.buffer.com/graphql` |
| Auth | `Authorization: Bearer <apiKey>` |
| Credential | locally stored Buffer config (`apiKey`) — never printed |
| Organization | `6a3d317b545b077504a4771b` — Drew Freedman |
| Tao Facebook | `6a3eb95f5ab6d2f106763fc9` — "The Tao of Clinical Touch" |
| Tao Instagram | `6a3eb89f5ab6d2f106763ca0` — "taoclinicaltouch" |

Also connected but **not Tao**: LinkedIn `bostonbodyworker`, Instagram `drewdog19`. Destination
IDs must be resolved and asserted, never assumed by position in a list.

### Required execution sequence

1. **Authenticate** — `account { organizations }` returns the expected account and org.
2. **Resolve destinations** — query `channels(input:{organizationId})`; match Tao Facebook and
   Tao Instagram by ID.
3. **Verify availability** — each target must be `isDisconnected: false` **and**
   `isLocked: false`.
4. **Duplicate-check the target scheduling window** before creating anything.
5. **Create only approved publication objects.**
6. **Capture the returned object ID.**
7. **Independently retrieve each object by ID** — `post(input:{id})`.
8. **Reconcile** destination · scheduled timestamp · copy · attached public WordPress media URL.

**A mutation response is not proof of scheduled state.** Only an independent readback is.

### Schema notes

Field names drift; validate against the live schema rather than from memory.
Verified working shapes: `account { organizations }`;
`channels(input:{organizationId}) { id service name isDisconnected isLocked }`;
`posts(first, input:{organizationId, filter:{status:[scheduled]}})`;
`post(input:{id})`. On `ImageAsset`, `source` is a **scalar String**, not an object.
Enum values are unquoted; `metadata` uses the `GqlEnum` wrapper.

### Media requirement

Buffer has no upload tool. Images **must** be public HTTPS URLs. Tao uses WordPress media under
`/wp-content/uploads/`, checksum-verified per §4 before attachment.

---

## 6. Brevo architecture doctrine

### Template 39 is not presently a neutral master

Template 39, currently named **"Tao — Weekly Issue Master"**, is **not** a reusable master. It
contains Issue 011-specific content end to end: subject line, `ISSUE 011 · RESPONSE` eyebrow,
the Issue 011 body, and a CTA hard-linked to that issue's article.

Editing it in place would also mutate the object Issue 011's queued campaign was built from.
**Do not treat template 39 as a shell. Do not modify or delete it.**

### Current reusable doctrine

- Stable Tao branding and layout **may** form a neutral master.
- Issue-specific editorial content belongs in the **issue campaign object**, composed from the
  approved issue copy — not in the master.
- The issue-specific CTA **must** resolve to that issue's canonical WordPress article URL, which
  must exist before the campaign is composed.
- Compatible email imagery **may reference the Founder-approved WordPress-hosted 1200×628
  Landscape master directly** by public HTTPS URL.
- **A separate Brevo image-library upload is not required** when external HTTPS media is used.

### Precedent

Campaign 36 (Issue 008, status `sent`) carried a raw WordPress `<img src>` with
`inlineImageActivation: false`. Brevo stored and delivered the external URL without proxying or
inlining it: **11,341 delivered**. No Brevo image-upload capability is required by this
architecture.

The delivery figure is the load-bearing evidence here. Campaign 36's reported **53.28% open rate
is not evidence of engagement** and must not be cited as a performance benchmark — see §6
*Metric interpretation*.

### Sender and recipients

| Property | Value |
|---|---|
| Sender | ID **3** — "Drew Freedman \| Tao of Clinical Touch" <drew@mail.taoclinicaltouch.com> |
| Reply-to | drew@learn2tape.com |

Sender and recipient lists must be asserted against the approved issue plan before scheduling.

**Recipient configuration is an open Founder decision, not settled doctrine.**

#### Recipient configuration — verified state, September 18, 2026

| | |
|---|---|
| List **64** — actual Brevo name | **"Tao subscriber list"** |
| List 64 — state | created 2026-08-23, **1 subscriber**, **no campaign history** |
| Configuration used by every Tao issue send to date | **22 lists** `[2,5,6,7,8,10,44-59]` — campaigns 35, 36, 38, 40, 41 (Issues 007, 008, 010, 011, 012); byte-identical in all five |
| What those 22 lists are | **NCB licensed-massage-therapist acquisition lists** — cold-outreach and warm-up batches, not publication opt-ins |

**That configuration is historical production behavior, not established intent.** Two
Founder-approved records point the other way, and nothing on record supersedes either:

- `07_MARKETING/STANDARDS/TAO_PUBLICATION_SIGNUP_INFRASTRUCTURE.md` — the publication requires a
  dedicated double-opt-in subscriber list, and states: *"Do not mix publication subscribers into
  unrelated marketing/customer lists unless Founder explicitly approves."*
- `DECISION_INDEX.md` → Email & Marketing → *NCB Campaign Brand* (April 2026) — *"Send as
  Learn2Tape, not Tao (list knows Drew through CE relationship)"*; *"Tao is new; L2T relationship
  is 15+ years. Use what's trusted."*

A further anomaly: list **9** (`NCB_MA_Batch_Day5`, 250 contacts) belongs to the documented
six-day MA warm-up series but is absent from all five sends. The 22-list set is therefore not a
designed audience boundary.

**Until the Founder resolves this, treat neither configuration as canonical.** Asserting a
recipient set for a new issue is a STOP condition pending that decision.

List 64 is **not retired.** It remains the intended destination for publication opt-ins under the
signup infrastructure standard; it is simply not yet a viable send target.

### Metric interpretation — verified September 18, 2026

**Per-list `campaignStats` rows are attributions of the same send events, not a partition.** A
contact on N of a campaign's lists is counted in N rows. Brevo deduplicates recipients at send;
the per-list breakdown does not. **Summing per-list fields across overlapping lists is invalid.**

Use `globalStats`, which is deduplicated and matches the Brevo UI. It is returned only when
`statistics=globalStats` is requested explicitly; otherwise it comes back zeroed. `statsByDomain`
is also a true partition (one address, one domain).

Verified: contacts on two campaign lists show exactly one `messagesSent` and one `delivered` event
per campaign. **No duplicate delivery has ever occurred.** Summed per-list totals overstated
Issues 010/011 by ~1.9x.

#### Open rates are not comparable across the Tao issue series

| Issue | Reported open rate | Trackable rate | uniqueViews − (trackable + AppleMPP) |
|---|---:|---:|---:|
| 007 | 48.42% | 0.43% | **+5,209 unexplained** |
| 008 | 53.28% | 0.74% | **+5,597 unexplained** |
| 010 | 0.14% | 0.14% | 0 |
| 011 | 3.23% | 0.66% | −2 |

For Issues 010 and 011, `uniqueViews` equals `trackable + appleMppOpens` exactly. For 007 and 008
it exceeds that sum by over five thousand, and exceeds the sum of the campaign's own per-list rows
by 6–7x — impossible for a deduplicated count. Those opens are machine pre-fetch and scanner
traffic against a cold acquired list, not human reads.

**`trackableViewsRate` is the reliable engagement signal**: 0.43% / 0.74% / 0.14% / 0.66% across
the series. Click rates corroborate it at 0.26–0.37%.

Do not set expectations, compare issues, or evaluate audiences on `opensRate`.

### Controlled-mutation boundary

Creating a neutral reusable master is a **controlled Brevo mutation** requiring its own
authorization. It is not authorized by this doctrine.

---

## 7. Canonical execution and verification order

Execute in this order. Each stage must verify before the next begins.

### A. Repository
Verify `HEAD` parity with `origin/main`, clean working tree, production completeness gate CLOSED,
manifests present, and all declared checksums verified.

### B. WordPress media
Upload canonical assets → retrieve each public URL **anonymously** → SHA-256 verify against the
canonical repository hash (§4). No URL proceeds downstream until its checksum matches.

### C. WordPress article
Create the future-dated canonical article → retrieve the authenticated object → verify slug,
content, status, scheduled timestamp, and featured/landscape media as applicable.

### D. Buffer
Duplicate-check the scheduling window → create approved scheduled objects → **independently read
each object back by ID** → reconcile destination, time, copy, and media URL.

### E. Brevo
Only after the canonical WordPress article URL exists. Compose the issue-specific campaign from
approved copy and structure → verify sender, recipient lists, subject, preheader, CTA target,
image URL, and scheduled timestamp.

### F. Reconciliation
Compare every external object against the canonical issue publishing schedule — every object,
every timestamp, every destination.

### G. Receipt
Persist object IDs, URLs, timestamps, verification results, and any bounded residuals.
**No credentials. No PII.**

---

## 8. STOP conditions

Execution halts immediately on any of the following. The condition is recorded; the limitation is
not routed around.

1. Authentication failure on any platform
2. Destination identity mismatch
3. Checksum mismatch between canonical and publicly retrieved asset
4. Unexpected WordPress transformation of an approved master
5. Duplicate scheduled object detected
6. Copy mismatch against approved editorial content
7. Schedule or timezone mismatch against the approved publishing schedule
8. Media URL not retrievable anonymously over HTTPS
9. Buffer destination disconnected or locked
10. Brevo sender or recipient-list mismatch
11. Unresolved subscription or send-credit eligibility
12. Any requirement to modify Founder-approved copy or imagery

**No workaround may silently bypass a STOP condition.** No alternate host, substitute asset,
partial deployment, or "close enough" reconciliation. Stop, record, escalate to the Founder.

---

## 9. Known execution dependencies

### Brevo subscription eligibility — manual Founder check

The Brevo account API exposes the **current plan period only**. It carries no `autoRenew`,
`renewalDate`, `nextBillingDate`, or `cancelAtPeriodEnd` field, and therefore **cannot**
distinguish automatic renewal from lapse.

Plan period on record: **2026-08-20 → 2026-09-20 17:31 UTC** (13:31 ET), Starter / paid / active.

**Issue 012 dependency:** Founder or manual check required — confirm Brevo Starter renewal and
send-credit eligibility beyond **September 20, 2026** before Issue 012 email scheduling.
Issue 012's email is scheduled 2026-09-21 10:00 ET, approximately 20 hours after the period
boundary.

This is a **billing dependency, not a technical infrastructure failure.** Do not classify it as
one. Do not change the subscription programmatically.

---

## Change control

When a Founder decision changes a rule here:

1. Preserve the historical evidence.
2. Add the new rule with its effective date.
3. State what it supersedes.
4. Update affected standards, adapters, and deterministic tooling **before** using them as a
   release gate.
5. Do not silently rewrite completed campaign history.

---

## Revision history

- **v1.2 — September 18, 2026** — **§6 metric-interpretation correction, and audience decision
  recorded (change control).** *Prior state:* §1 and §6 cited Campaign 36 as "11,341 delivered,
  53.24% open rate"; the adapter repeated it. Nothing warned against summing per-list
  `campaignStats`. *Evidence:* per-contact readback proved contacts on two campaign lists receive
  exactly one send and one delivery — no duplicate delivery has ever occurred — so per-list rows
  are attributions, not a partition, and summing them overstated Issues 010/011 by ~1.9x.
  Campaign 36's reported open rate is genuine Brevo output but is not engagement: its
  `uniqueViews` exceed `trackable + appleMppOpens` by 5,597 and exceed the sum of its own per-list
  rows by 7x. *Corrected state:* the open-rate citation is removed from both files, the delivery
  evidence is preserved, and a **Metric interpretation** subsection records the partition rule,
  the `statistics=globalStats` requirement, and `trackableViewsRate` as the reliable signal.
  *Audience decision:* recipient configuration, open since v1.1, is resolved for the Tao
  publication — see `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`.
  The NCB acquisition base is placed outside the Tao publication architecture pending results of a
  Learn2Tape-branded invitation to lists 11 and 65. List 64 becomes the publication destination by
  explicit opt-in only.

- **v1.1 — September 18, 2026** — **§6 recipient-configuration correction (change control).**
  *Prior state:* §6 listed `Publication list | ID 64 — "Tao — Publication Subscribers"` as the
  recipient configuration. *Evidence:* read-only Brevo verification established list 64's actual
  name is **"Tao subscriber list"**, created 2026-08-23, with **1 subscriber** and **no campaign
  history**; campaigns 35/36/38/40/41 (Issues 007/008/010/011/012) each used an identical
  **22-list** set `[2,5,6,7,8,10,44-59]`, all of which are **NCB licensed-MT acquisition lists**;
  list 9 belongs to the documented warm-up series yet appears in none of the sends. *Reason:* the
  prior entry was factually wrong on both the list name and its role, and the 22-list set could
  not be promoted in its place because two standing Founder-approved records —
  `TAO_PUBLICATION_SIGNUP_INFRASTRUCTURE.md` ("do not mix publication subscribers into unrelated
  marketing/customer lists") and `DECISION_INDEX.md` *NCB Campaign Brand*, April 2026 ("send as
  Learn2Tape, not Tao") — point the other way, and nothing on record supersedes either.
  *Corrected state:* the false publication-list row is removed; the verified state of both
  candidate configurations is recorded; recipient configuration is marked an **open Founder
  decision** and a STOP condition pending resolution. List 64 is **not retired**. Authority was
  deliberately **not** inferred from repetition. Same correction applied to
  `control_plane/adapters/BREVO_V1_ADAPTER.md`. No other doctrine altered.

- **v1.0 — September 13, 2026** — Established from Gates 1–4 live infrastructure verification.
  Supersedes Buffer CLI execution doctrine. Records WordPress REST authentication, the
  checksum-reconciliation asset rule, Buffer GraphQL execution and readback, Brevo external-media
  architecture, canonical execution order, and STOP conditions.
