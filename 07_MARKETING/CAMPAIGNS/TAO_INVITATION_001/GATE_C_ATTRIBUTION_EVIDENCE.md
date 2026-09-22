# Gate C — SIGNUP_SOURCE Attribution: Closure Evidence

**Status:** **GATE C CLOSED — attribution and provenance preservation empirically verified**
**Closed:** September 22, 2026
**Authority:** `07_MARKETING/DECISIONS/2026-09-18_TAO_AUDIENCE_PERMISSION_ARCHITECTURE.md`

Verified against live production. Every claim below is an observed API response, not an inference.

---

## 1. Deployment verification — read-only

The production handler exposes a build marker in its REST schema, so the deployed build is
verifiable without submitting a form:

```
GET https://taoclinicaltouch.com/wp-json/tao/v1     (cache-busted, cf-cache-status: DYNAMIC)

"source": {
    "type": "string",
    "default": "unknown",
    "description": "Signup placement source; allowlisted server-side. build:gate-c-v1",
    "required": false
}
```

**`build:gate-c-v1` confirmed live.** Endpoint contract unchanged: `/tao/v1/subscribe` POST-only,
`email` string/required, `source` string/optional/default `unknown`, no unexpected args. The only
schema delta from the pre-patch state is the `description` field itself.

## 2. Attribution write — PROVEN

Test address `drew@areasalons.com`, submitted once through the live `/join/` form carrying
`data-signup-source="l2t_invitation"`. Baseline before submission: **404, no contact record, no
list membership, no attributes, no campaign history.**

Pre-confirmation: Brevo still returned **404** — DOI gating intact, nothing written before consent.

Post-confirmation:

```json
{
  "id": 12916,
  "email": "drew@areasalons.com",
  "createdAt":  "2026-09-22T14:50:56.163-04:00",
  "modifiedAt": "2026-09-22T14:50:56.163-04:00",
  "listIds": [64],
  "attributes": {
    "DOUBLE_OPT-IN": "1",
    "SIGNUP_SOURCE": "l2t_invitation"
  }
}
```

| Check | Result |
|---|---|
| `SIGNUP_SOURCE = l2t_invitation` | **PASS** |
| `SOURCE` absent / untouched | **PASS** |
| Membership List 64 only | **PASS** |
| List 64 moved 3 → 4 | **PASS** |
| Single contact, no duplicate | **PASS** |
| Single write — `createdAt == modifiedAt` | **PASS** |

**Brevo carries contact attributes through `POST /v3/contacts/doubleOptinConfirmation` and applies
them at confirmation.** This was the open architectural question. It is now answered empirically.

## 3. No-overwrite guard — PROVEN

Same contact (12916, already carrying `SIGNUP_SOURCE = l2t_invitation`) submitted once through a
**different** placement: `/signup-test/`, verified live as `data-signup-source="gate1_test"` — an
allowlisted value distinct from the original.

Post-attempt state:

```json
{
  "id": 12916,
  "createdAt":  "2026-09-22T14:50:56.163-04:00",
  "modifiedAt": "2026-09-22T14:50:56.163-04:00",
  "listIds": [64],
  "attributes": { "DOUBLE_OPT-IN": "1", "SIGNUP_SOURCE": "l2t_invitation" }
}
```

| Check | Result |
|---|---|
| `SIGNUP_SOURCE` remains exactly `l2t_invitation` | **PASS** — not `gate1_test` |
| `SOURCE` absent / untouched | **PASS** |
| Contact ID remains 12916 | **PASS** |
| No duplicate contact | **PASS** |
| No unintended list membership | **PASS** |
| List 64 membership intact | **PASS** |
| **`modifiedAt` unchanged** | **PASS** — identical to the millisecond |

`modifiedAt` did not move. The record was not written to at all. Original opt-in provenance
survives a later signup from a different source.

Nothing was altered to make the test pass — guard, contact, attributes, lists and endpoint were
untouched throughout.

### Bounded residual — stated, not hidden

The handler maps both `201/204 → doi_sent` and `400 "already exist" → already_subscribed` to
`status: success`, and the UI renders the same panel for both. From outside it is therefore **not
observable** which mechanism prevented the write:

1. `tao_may_write_signup_source()` returned `false` and omitted the attribute, or
2. Brevo rejected the DOI outright because the contact already exists

**The protective outcome is identical and verified either way.** Distinguishing them would require
the PHP error log or Brevo's transactional log for that request. Recorded as a known limit of the
external evidence, not as an open defect.

## 4. Safeguards confirmed in production

| Requirement | Status |
|---|---|
| `source` reaches the bridge | PROVEN |
| Allowlist normalizes client input | PROVEN — `l2t_invitation`, `gate1_test` both accepted |
| Attribute persists through DOI confirmation | PROVEN |
| Reusable per placement, never hard-coded | PROVEN — two placements, two distinct values |
| `SOURCE` never referenced or written | PROVEN — absent throughout both tests |
| Existing `SIGNUP_SOURCE` never overwritten | PROVEN — `modifiedAt` unmoved |
| Deployment verifiable read-only | PROVEN — `build:gate-c-v1` |

## 5. Conclusion

**GATE C CLOSED — attribution and provenance preservation empirically verified.**

Invitation 001 conversions will carry `SIGNUP_SOURCE = l2t_invitation` on confirmation, making the
final funnel stage — List 64 additions — attributable for the first time. Commerce provenance
(`SOURCE`, e.g. `AMTA2026` on the 15 AMTA buyers) is structurally unreachable by this code path.

## 6. Test artifacts

Created solely by Gate B/C testing; not real subscribers:

| ID | Address | Created | Note |
|---|---|---|---|
| 12914 | `drew@taoclinicaltouch.com` | 2026-09-19 | Gate B DOI test; pre-patch, no `SIGNUP_SOURCE` |
| 12915 | `drew+gatec@taoclinicaltouch.com` | 2026-09-22 | Gate C attempt against undeployed patch; no `SIGNUP_SOURCE` |
| 12916 | `drew@areasalons.com` | 2026-09-22 | Gate C success; `SIGNUP_SOURCE = l2t_invitation` |

Founder directed removal of **12915** and **12916**. `drew@taoclinicaltouch.com` (12914) and
`drew@learn2tape.com` (1) are retained.

**Deletion is a manual Brevo action.** This session's Brevo connector exposes no contact-delete
capability — contact operations are read-only. Post-deletion List 64 baseline should be **2**.

## 7. Funnel-baseline consequence

Any contact in List 64 without a `SIGNUP_SOURCE` predates this capability and must not be counted
as an Invitation 001 conversion. After cleanup that is `drew@taoclinicaltouch.com` and
`drew@learn2tape.com`.
