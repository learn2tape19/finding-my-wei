# Execution Lesson — Brevo Campaign Scheduling Capability

**Recorded:** August 20, 2026
**Issue:** 007
**Context:** Attempted to schedule existing Brevo Campaign 35 via API after Founder-approved draft creation

---

## Finding

Brevo OAuth/MCP (via Claude.ai integration) supports authenticated campaign **creation** and **retrieval**, but the currently exposed execution surface does not support **mutation of an existing campaign's schedule**.

The MCP tool surface includes:

- `create_email_campaign` — supports `scheduledAt` at creation time
- `get_email_campaign` — read-only retrieval
- `get_email_campaigns` — read-only listing

No `update_email_campaign` or `send_email_campaign` endpoint is exposed through the MCP integration.

## Failed alternative: Brevo v3 REST API via curl

The environment variable `$BREVO_API_KEY` contained a JWT/session token (prefix `eyJhc...`), not a Brevo v3 REST API key (prefix `xkeysib-`). Direct curl calls to `PUT /v3/emailCampaigns/{id}` returned `401 unauthorized` with both `api-key:` and `Authorization: Bearer` headers.

## Constraints

- Do not substitute a session/JWT token for a Brevo v3 API key.
- Do not create a duplicate campaign as a scheduling workaround.
- Do not attempt to re-create the campaign with `scheduledAt` — this would produce a second campaign with different content state.

## Approved fallback

Founder manual scheduling via the Brevo dashboard is the approved fallback until one of the following is available:

1. A verified Brevo v3 API key (prefix `xkeysib-`) is provisioned for the execution environment.
2. The Brevo MCP integration exposes an `update_email_campaign` tool.

## Recommendation

If a Brevo v3 API key is generated (Brevo dashboard → Settings → API Keys), it should be provisioned alongside the existing JWT. The v3 key enables `PUT /v3/emailCampaigns/{id}` for schedule, content, and recipient updates on existing campaigns. This would close the scheduling gap without requiring MCP tool surface changes.
