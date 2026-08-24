# reference — a pointer to an external resource

- **Tier**: core (always included)
- **Prefix**: `reference-`
- **Purpose**: an external resource the user returns to: documentation, a
  dashboard, a spec/standard/protocol, a ticket tracker, an API's docs. The
  page answers: where is it, what is it authoritative for, and what has it
  established.

## Signals
Core — no evidence needed.

## Required sections
- `## What it is` — one paragraph, with the canonical URL/location
- `## Authoritative for` — what questions this source settles
- `## Key facts` — the specific things already looked up, provenance-tagged
  (so the next lookup is a wiki read, not a web fetch)

## Ask the user for
- Access details when non-public (where credentials live — never values),
  and which version/edition is the one in use.

## Naming
- `reference-<resource-slug>.md`, e.g. `reference-stripe-api-docs.md`.

## Typical relations
- Linked from whatever consults it; distinct from `paper-` (a summarized
  source) — a reference is *pointed at*, a paper is *digested*.
