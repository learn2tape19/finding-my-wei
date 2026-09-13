# Buffer V1 Adapter — GraphQL

**Status:** CURRENT AUTHORITY — verified against live production September 13, 2026
**Supersedes:** Buffer CLI execution doctrine (`buffer context` / `buffer` binary on PATH)
**Parent doctrine:** `04_CAPABILITIES/PUBLISHING/TAO_PUBLISHING_EXECUTION_DOCTRINE.md`

---

## Supersession notice

Earlier operational notes and execution handoffs treated the official **Buffer CLI** as the
required execution mechanism, and recorded its absence from `PATH` as a hard Buffer blocker.

**That doctrine is obsolete.**

Buffer executes through its first-party **GraphQL API**. The CLI is not required, not installed,
and not an execution blocker. The credential the CLI originally wrote to local config remains
valid and is read directly.

Historical records of CLI-based blockage are preserved as evidence of what was believed at that
checkpoint. They are **not** current execution authority.

---

## Verified capability

Confirmed live, read-only, September 13, 2026:

| Check | Result |
|---|---|
| Locally stored credential exists | **YES** |
| Authentication succeeds | **YES** — account and organization resolve |
| Tao Facebook destination resolves and is connected | **YES** |
| Tao Instagram destination resolves and is connected | **YES** |
| Scheduled queue readback succeeds | **YES** — 25 objects returned |
| Individual object readback by ID succeeds | **YES** — `post(input:{id})` |
| WordPress-hosted HTTPS media works in scheduled objects | **YES** — 25 of 25 |

---

## Connection

| Property | Value |
|---|---|
| Endpoint | `https://api.buffer.com/graphql` |
| Method | `POST`, `Content-Type: application/json` |
| Auth header | `Authorization: Bearer <apiKey>` |
| Credential source | locally stored Buffer config (`apiKey` field) |
| Organization | `6a3d317b545b077504a4771b` — Drew Freedman |

The `apiKey` is a secret. Never print it, log it, commit it, embed it in a receipt, or pass it in
a process argument list. Confirm presence by name and length only.

## Destination registry

| Destination | Channel ID | Service |
|---|---|---|
| **Tao Facebook** | `6a3eb95f5ab6d2f106763fc9` | facebook — "The Tao of Clinical Touch" |
| **Tao Instagram** | `6a3eb89f5ab6d2f106763ca0` | instagram — "taoclinicaltouch" |

Also connected to this organization but **NOT Tao destinations** — never publish Tao content to
them:

- LinkedIn `bostonbodyworker` (`6aa07201cd8b9c702c305cf3`)
- Instagram `drewdog19` (`6a3eba3f5ab6d2f106764339`)

**Resolve and assert destination IDs explicitly.** Never select a channel by list position,
service type alone, or name substring.

---

## Required execution sequence

1. **Authenticate** — `account { organizations }` returns the expected account and org.
2. **Resolve destinations** — `channels(input:{organizationId})`, matched by ID.
3. **Verify availability** — target must be `isDisconnected: false` **and** `isLocked: false`.
   A locked or disconnected destination is a STOP condition.
4. **Duplicate-check the target scheduling window** — query scheduled posts for the window and
   confirm no approved object already exists.
5. **Create only approved publication objects** — copy and media from the approved issue package.
6. **Capture the returned object ID.**
7. **Independently retrieve the object by ID** — `post(input:{id})`.
8. **Reconcile** each object against the approved publishing schedule:
   - destination
   - scheduled timestamp
   - copy
   - attached public WordPress media URL

**A mutation response is not proof of scheduled state.** Only the independent readback in step 7
closes the object. Any reconciliation failure in step 8 is a STOP condition.

---

## Media requirement

Buffer has **no upload capability**. Every image must be a **public HTTPS URL**.

Tao uses WordPress media under `https://taoclinicaltouch.com/wp-content/uploads/`. A URL is
eligible for attachment only after it passes the checksum rule:

```
canonical repository SHA-256  ==  anonymously retrieved SHA-256
```

Attaching an unverified URL is a doctrine violation.

---

## Schema notes

Field names drift. **Validate against the live schema rather than from memory** — a
`GRAPHQL_VALIDATION_FAILED` error names the correct field, so read it and correct rather than
guessing again.

Verified working shapes:

```graphql
{ account { id organizations { id name } } }

{ channels(input:{organizationId:"<org>"}) {
    id service name isDisconnected isLocked } }

{ posts(first:40, input:{organizationId:"<org>",
        filter:{status:[scheduled]}}) {
    edges { node { id status dueAt channelId
      assets { __typename ... on ImageAsset { source } } } } } }

{ post(input:{id:"<postId>"}) {
    id status dueAt channelId text
    assets { __typename ... on ImageAsset { source } } } }
```

Gotchas confirmed in production:

- On `ImageAsset`, **`source` is a scalar `String!`** — selecting subfields on it fails.
- The image asset type is **`ImageAsset`**, not `PostImageAsset`.
- `Channel` has no `serviceUsername` field; use `name` (and `serviceData` where richer detail is
  needed).
- `post` takes `input: {id: "..."}`, not a bare `id` argument.
- Enum values are **unquoted**; object keys are unquoted; `metadata` uses the `GqlEnum` wrapper.
- The publishing token can create and delete posts; some list operations are scoped differently
  from read operations — verify capability rather than assuming symmetry.
- `deletePost` returns `DeletePostPayload` (`DeletePostSuccess | VoidMutationError`).

---

## STOP conditions specific to this adapter

- Authentication failure
- Destination ID not found, or resolved to a non-Tao channel
- Destination `isDisconnected: true` or `isLocked: true`
- Duplicate scheduled object already present in the target window
- Readback copy, timestamp, destination, or media URL mismatch
- Media URL not anonymously retrievable, or failing checksum reconciliation

---

## Revision history

- **v1.0 — September 13, 2026** — Established from live verification. Supersedes CLI doctrine.
