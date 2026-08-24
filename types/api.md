# api — a contract between systems

- **Tier**: catalog
- **Prefix**: `api-`
- **Purpose**: an interface contract — one the user publishes or one they
  depend on heavily enough to document: endpoints/operations actually used,
  auth, limits, and the gotchas already paid for. (Casual dependencies stay
  `reference-` pages; promote to `api-` when usage details accumulate.)

## Signals
- OpenAPI/GraphQL schemas, generated clients, API-key handling code,
  webhook handlers
- conversation: "their rate limit", "the v2 endpoint", "our public API"

## Required sections
- `## Contract` — the operations that matter here, with shapes; link the
  full spec rather than duplicating it
- `## Auth & limits` — auth method (where credentials live — never values),
  rate limits, quotas
- `## Usage here` — which projects/services call it and for what
- `## Gotchas` — every surprise already hit, provenance-tagged

## Ask the user for
- Which operations are load-bearing, current version pinned, sandbox vs
  production details.

## Naming
- `api-<name-slug>.md`, e.g. `api-noaa-tides.md`.

## Typical relations
- Consumed by `service-`/`project-`/`pipeline-`; owned by an `entity-` org;
  full docs live at a `reference-`.
