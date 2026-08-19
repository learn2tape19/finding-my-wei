# CLAUDE ENGINEERING WORK ORDER 001

**Work Order:** PCP-ENG-001  
**Capability:** Publishing Control Plane  
**Assigned role:** Repository Steward / Engineer  
**Authority:** Founder-approved institutional architecture already committed to `main`  
**Status:** READY FOR EXECUTION

## Mission

Implement the platform-independent spine of the Finding My Wei Publishing Control Plane.

Do not connect to or publish on live social networks, websites or email systems in this work order.

This work order establishes the deterministic approval and deployment machinery that every future adapter must obey.

## Governing Sources

Read and treat as authoritative before engineering:

- `04_CAPABILITIES/PUBLISHING/REMOTE_PUBLISHING_AGENT_ARCHITECTURE.md`
- `04_CAPABILITIES/PUBLISHING/CLAUDE_STEWARD_DEPLOYMENT_PROTOCOL.md`
- `04_CAPABILITIES/PUBLISHING/PUBLISHING_CONTROL_PLANE_SPEC.md`
- `04_CAPABILITIES/PUBLISHING/RUNNERS/RUNNER_STEWARDSHIP_STANDARD.md`
- `04_CAPABILITIES/PUBLISHING/SCHEMAS/publication.manifest.schema.json`
- `04_CAPABILITIES/PUBLISHING/SCHEMAS/founder.approval.schema.json`
- `04_CAPABILITIES/PUBLISHING/SCHEMAS/deployment.receipt.schema.json`
- `04_CAPABILITIES/PUBLISHING/DESTINATIONS/DESTINATION_REGISTRY.template.yaml`
- `04_CAPABILITIES/PUBLISHING/RUNNERS/runner-registry.template.yaml`
- `04_CAPABILITIES/PUBLISHING/ENGINEERING/IMPLEMENTATION_ROADMAP.md`

If implementation conflicts with these documents, stop and report the conflict. Do not silently reinterpret architecture.

## Deliverables

Create a clean implementation under:

`04_CAPABILITIES/PUBLISHING/control_plane/`

Required modules/functions:

1. manifest validation
2. deterministic package hashing
3. Founder approval validation
4. destination registry resolution
5. deployment receipt generation
6. orchestration interface with adapters stubbed, not live
7. structured error classes matching institutional failure states
8. tests

Create fixtures under:

`04_CAPABILITIES/PUBLISHING/tests/fixtures/`

At minimum include:

- valid unapproved publication;
- valid Founder-approved publication;
- hash mismatch;
- changed asset after approval;
- unknown destination;
- disabled destination;
- malformed manifest;
- malformed approval;
- sample successful receipt;
- sample transient failure receipt.

## Security Requirements

- No real credentials.
- No tokens.
- No secrets.
- No live platform calls.
- No environment assumptions tied to Drew's local Mac.
- Never log secret values.
- Fail closed when approval cannot be proven.
- Do not add broad repository permissions.
- Minimize dependencies.

## Dependency Rule

Before adding a dependency, determine whether Python standard library or an already-present trusted dependency is sufficient.

For any new dependency, document:

- why it is required;
- source/upstream;
- pinned version;
- maintenance status;
- security considerations;
- why building the small capability internally would be worse.

Do not add convenience dependencies merely to save a few lines of code.

## Hashing Requirement

Define and document canonical package-hash semantics so that:

- the same package produces the same SHA-256 identity locally and remotely;
- operational receipts/logs are excluded;
- Founder approval files are excluded from the package they approve;
- changing any approved public payload or asset changes the hash;
- ordering/serialization cannot create accidental hash drift.

Add tests proving these properties.

## Approval Requirement

The approval gate must reject deployment unless:

- approval state is exactly `FOUNDER_APPROVED_FOR_LAUNCH`;
- publication IDs match;
- package hashes match exactly;
- requested destination is in Founder-approved destinations;
- destination exists and is enabled.

No fallback approval interpretation.

## Orchestrator Requirement

Implement an adapter protocol/interface but only a `dry_run`/test adapter in PCP-ENG-001.

The dry-run adapter must prove that:

- exact payload reaches the adapter;
- adapter cannot mutate canonical source;
- a structured receipt returns;
- duplicate invocation can be detected using publication/package/destination identity.

## Testing

Tests must cover happy path and failure path.

Required tests include:

- deterministic hashing;
- hash changes after payload mutation;
- approval mismatch fails;
- unapproved package fails;
- undeclared destination fails;
- disabled destination fails;
- valid approved dry run succeeds;
- receipt conforms to schema;
- duplicate protection works;
- errors map to institutional states.

## Documentation

Create:

`04_CAPABILITIES/PUBLISHING/control_plane/README.md`

It must explain:

- architecture;
- local test execution;
- package hashing semantics;
- approval gate;
- adapter contract;
- receipt model;
- security boundary;
- how future WordPress/Brevo/Meta/LinkedIn adapters plug in.

## Git Discipline

- Work from current `main`.
- Use a dedicated engineering branch.
- Do not overwrite canonical Issue 006 production content.
- Keep commits coherent and reviewable.
- Run tests before requesting merge.
- Provide a completion report containing branch, commit SHA(s), files created/changed, tests run/results, dependencies added, known limitations, and exact next work order recommendation.

## Definition of Done

PCP-ENG-001 is complete when the repository can prove, entirely offline and without platform credentials, that an immutable publication package can be hashed, matched to one Founder approval, routed only to approved/enabled destinations through a dry-run adapter, protected from duplicate execution, and recorded through schema-valid deployment receipts.

Do not proceed to WordPress or any external platform adapter until this work order is accepted.
