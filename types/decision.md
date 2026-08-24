# decision — a choice with reasons, recorded

- **Tier**: catalog
- **Prefix**: `decision-`
- **Purpose**: one significant, settled choice — technical (ADR-style),
  methodological, or editorial — with its alternatives and rationale, so it
  is not relitigated from memory. Reversals get a *new* decision page linking
  the old one, never an edit that erases history.

## Signals
- `docs/adr/`/`docs/decisions/` dirs, RFC-like documents
- conversation: "we decided to…", "why did we pick…", the same debate
  recurring twice

## Required sections
- `## Decision` — one sentence, unambiguous
- `## Context` — the situation that forced a choice
- `## Alternatives` — what else was considered and why rejected
- `## Consequences` — what this commits to; costs accepted
- `## Status` — decided (date) | superseded by `[[decision-x]]`

## Ask the user for
- The real rationale (the written-down reason is often not the operative
  one), and who made the call if not the user.

## Naming
- `decision-<slug>.md`, e.g. `decision-sqlite-over-postgres.md`.

## Typical relations
- Anchored to a `project-`/`service-`/`manuscript-`; evidenced by
  `experiment-` when a run settled it; superseded-by chains within the type.
