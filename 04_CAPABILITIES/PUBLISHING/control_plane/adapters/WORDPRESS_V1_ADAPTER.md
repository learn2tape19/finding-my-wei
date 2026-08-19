# WordPress V1 Adapter for Publishing Control Plane

**Status:** Candidate (unit tested, ready for staging validation)  
**Implementation:** `04_CAPABILITIES/PUBLISHING/control_plane/adapters/wordpress_v1.py`  
**Tests:** 33 comprehensive unit tests with mocked HTTP responses

## Overview

The WordPress V1 adapter transports exact Founder-approved WordPress publication payloads through the official WordPress REST API (v2). It implements:

- HTTPS-only connectivity
- WordPress Application Password authentication
- Complete preflight validation before any writes
- Exact payload preservation (no editorial modifications)
- Media upload with asset hash verification
- Deterministic category/tag resolution
- Post create/update/schedule/publish with exact state preservation
- Idempotency (no duplicate posts on retry)
- Verification through authenticated readback
- Institutional error mapping
- Secret redaction in all logs and exceptions

## Authentication Model

### WordPress Application Password (Recommended)

Application Passwords are application-specific credentials that avoid storing personal WordPress passwords.

**Required Configuration:**
- `base_url`: WordPress site URL (HTTPS only, e.g., `https://example.com`)
- `username`: WordPress user account (publisher identity)
- `app_password`: Application Password (generated in WordPress user settings)

**How to Create:**
1. Log into WordPress as publisher user
2. Navigate to user profile → "Application Passwords"
3. Create a new password for "Publishing Control Plane"
4. Store in GitHub Actions secrets or secure secret manager (NEVER in repository)

### Credentials in GitHub Actions

Store as repository secrets:
```
WORDPRESS_BASE_URL=https://your-site.com
WORDPRESS_USERNAME=publisher_user
WORDPRESS_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx
```

## Destination Registry Configuration

Example registry entry:

```yaml
destinations:
  - destination_id: tao.wordpress.production
    domain: tao_of_clinical_touch
    platform: wordpress
    enabled: true
    adapter: wordpress_v1
    account_ref: "tao_site"
    auth:
      method: "application_password"
      secret_refs:
        - "WORDPRESS_TAO_BASE_URL"
        - "WORDPRESS_TAO_USERNAME"
        - "WORDPRESS_TAO_APP_PASSWORD"
    permissions:
      - media_upload
      - post_create
      - post_schedule
      - post_publish
    verification: wordpress_post_readback
```

## Supported Payload Fields

Required:
- `title`: Post title (string, not modified)
- `content`: Post body/HTML (string, not modified)
- `status`: One of `draft`, `future`, `publish`

Optional:
- `excerpt`: Post excerpt (string, preserved exactly)
- `slug`: URL slug (preserved exactly, used for idempotency detection)
- `featured_media_id`: WordPress media ID for featured image
- `categories`: List of category names (exact match resolution)
- `tags`: List of tag names (exact match resolution)
- `author`: WordPress user ID or login (if author change desired)
- `comment_status`: `open` or `closed`
- `ping_status`: `open` or `closed`
- `publish_at`: ISO datetime for scheduled posts (when status=`future`)

### Media Assets

Media must be declared in publication manifest with:
```json
{
  "id": "featured_image",
  "path": "assets/image.png",
  "sha256": "...",
  "media_type": "image/png",
  "alt_text": "Image description"
}
```

The adapter:
1. Verifies asset hash before upload
2. Uploads exact file with preserved filename
3. Sets alt text exactly as declared
4. Returns WordPress media ID for featured image assignment

## Preflight Validation

Before any write operation, preflight checks that the configured destination is suitable:

1. **HTTPS Verification**: Base URL must use HTTPS (never HTTP)
2. **REST API Reachability**: `/wp-json/wp/v2/` endpoint responds
3. **Authentication Success**: Application Password credentials work
4. **Identity Verification**: Authenticated username matches configuration
5. **Endpoint Availability**:
   - `/posts` endpoint reachable
   - `/media` endpoint reachable (if media declared)
   - `/categories` endpoint reachable (if categories declared)
   - `/tags` endpoint reachable (if tags declared)
6. **Permissions Verification**: User has required capabilities

Preflight performs **no public publication**. If any check fails, no content write occurs.

## Taxonomy Resolution Strategy

Categories and tags are resolved deterministically to prevent ambiguity and accidental creation of unintended taxonomy items.

### Category Resolution

1. Search for category by exact name
2. If found: use that category ID
3. If not found: raise error with `FAILED_REQUIRES_FOUNDER`
4. If ambiguous matches (multiple categories with same name): fail closed

Categories are **NOT created automatically** by the adapter. Approved content must target categories that already exist on the site.

### Tag Resolution

Same strategy as categories:
1. Search for tag by exact name
2. Fail closed if not found or ambiguous
3. No automatic tag creation

## Post Create/Update Behavior

### First Deployment (Create)

1. Search for existing post by slug
2. If not found: create new post with declared status
3. If found: update existing post (idempotency)

### Idempotency

To prevent duplicate posts on retry:
- Adapter searches for existing post by `slug` field
- If found, updates existing post instead of creating new
- Uses publication ID + destination ID to detect re-runs
- Deployment receipt identifies whether post was created or updated

**Important:** Use stable, globally unique slugs. If slug is not provided, the adapter may create a new post on retry.

## Scheduling Behavior

For scheduled posts (`status: "future"`):

1. Exact scheduled datetime from payload preserved
2. Site timezone NOT transformed (WordPress stores in UTC)
3. Readback verifies stored schedule matches approved time
4. No automatic rescheduling outside approved manifest window

Example:
```json
{
  "status": "future",
  "publish_at": "2026-08-15T14:30:00Z",
  "categories": ["News"],
  "slug": "scheduled-post"
}
```

## Error Mapping

WordPress errors map to institutional states:

| Condition | Status | Retry? |
|-----------|--------|--------|
| 401/403 (auth failure) | `BLOCKED_AUTH` | No |
| 429 (rate limited) | `FAILED_TRANSIENT` | Yes |
| 5xx (server error) | `FAILED_TRANSIENT` | Yes |
| Ambiguous category/tag | `FAILED_REQUIRES_FOUNDER` | No |
| Post/site mismatch | `FAILED_REQUIRES_FOUNDER` | No |
| Existing post update conflict | `FAILED_REQUIRES_FOUNDER` | No |
| Unknown HTTP error | `FAILED_REQUIRES_FOUNDER` | No |

## Verification

After publication/scheduling, the adapter verifies remote state:

1. Fetch post by ID via authenticated readback
2. Verify:
   - Post exists at remote ID
   - Title matches approved payload
   - Content matches (with documented WordPress rendering normalization)
   - Slug matches
   - Status is correct
   - Featured media ID assigned correctly
   - Categories/tags correct
   - Scheduled time correct (for future posts)
3. Return verification receipt

Verification uses authenticated requests to ensure accuracy. Public-facing URLs may have caching delays.

## Exact-State Preservation

The adapter MUST NOT:

- Rewrite titles (capitalization, punctuation preserved)
- Rewrite body copy
- Generate missing excerpts
- Alter or choose slugs
- Choose or modify categories
- Choose or modify tags
- Change alt text
- Add hashtags
- Modify CTAs
- Transform content encoding
- Silently adapt content to WordPress constraints

If WordPress rejects exact approved content, the adapter returns `BLOCKED_PLATFORM` error for manual Founder review.

## Content Normalization in Verification

WordPress may make harmless changes to HTML:

**Acceptable normalization** (verified, not treated as mismatch):
- `<p>Text</p>` vs `<p>Text\n</p>` (trailing whitespace)
- Attribute ordering: `class="x" id="y"` vs `id="y" class="x"`
- Void element rendering: `<br>` vs `<br />`
- Entity normalization: `&nbsp;` vs numeric entity
- Insignificant whitespace in HTML tags

**Unacceptable changes** (treated as verification failure):
- Text content modified
- HTML structure changed (tag removal/addition)
- Links altered
- Images removed or replaced
- Semantic meaning changed

## Secret Handling

**NEVER:**
- Print Authorization header (contains Base64-encoded credentials)
- Log Application Password in plaintext
- Include credentials in error messages
- Store credentials in repository
- Commit `.env` files

**Secrets are redacted from:**
- Exception messages
- HTTP error responses
- Deployment receipts
- All logging output

## Running Tests

### Unit Tests (Mocked, No Credentials Required)

```bash
cd 04_CAPABILITIES/PUBLISHING
pip install -r control_plane/requirements.txt
pytest tests/test_wordpress_v1_adapter.py -v
```

Expected: 33 tests pass with 0 failures

### Original PCP-ENG-001 Tests

```bash
pytest tests/test_control_plane.py -v
```

Adapter implementation does not modify existing tests. Original control plane tests remain green.

## Integration Harness (Staging Only)

Optional integration test against a **staging/non-production** WordPress site.

**Environment variables required:**
```
PCP_WORDPRESS_STAGING_URL=https://staging.example.com
PCP_WORDPRESS_STAGING_USERNAME=staging_user
PCP_WORDPRESS_STAGING_APP_PASSWORD=xxxx xxxx xxxx xxxx
PCP_WORDPRESS_STAGING_ENABLED=true
```

**What it does:**
1. Verifies preflight against staging site
2. Creates a clearly marked test draft post
3. Uploads test fixture media asset
4. Verifies post via readback
5. Optionally cleans up test post
6. Redacts credentials from output

**Important:** Must explicitly enable with environment variable. Will NOT run automatically during test suite. Refuses to run if destination is marked production.

To run:
```bash
pytest tests/test_wordpress_v1_adapter_integration.py -v
```

## Known Limitations

1. **No Multi-Site Support**: Each destination in registry points to single WordPress site. WP Multisite not tested.
2. **No Custom Post Types**: Adapter only supports standard `post` post type. Custom CPTs not implemented.
3. **No Plugin Metadata**: Registered REST metadata only when explicitly declared and supported.
4. **No OAuth**: Only Application Password auth. OAuth flow not implemented (future work order).
5. **No Media Library Search**: Media assumed identified by hash or ID. No filename-based search.
6. **No Taxonomy Creation**: Categories/tags must pre-exist. No automatic creation.
7. **WordPress Versions**: Tested against WordPress 6.0+. Earlier versions not verified.

## Rollback / Manual Publishing Fallback

If adapter fails unexpectedly:

1. Retrieve deployment receipt to get remote post ID
2. Manually edit post in WordPress admin if needed
3. Publish manually if status is still draft
4. File issue with receipt details for adapter investigation

Adapter failures do not prevent manual publishing.

## Site Capabilities Required

WordPress site must have:

- REST API enabled (default in WordPress 4.7+)
- Publishing user has `edit_posts` and `publish_posts` capabilities
- Media uploads enabled
- Permalinks configured (for slug uniqueness)

If using categories/tags:
- Respective taxonomies enabled
- Required categories/tags pre-created in WordPress

## Future Work

Potential enhancements after acceptance:

1. OAuth2 authentication model
2. Custom post type support
3. Automatic media reuse by hash
4. Plugin-specific REST metadata
5. WordPress Multisite support
6. Batch post creation
7. Post template application
8. Custom field population

These require dedicated work orders and architectural decisions.
