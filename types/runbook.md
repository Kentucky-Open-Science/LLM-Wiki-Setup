# runbook — a procedure that must go right

- **Tier**: catalog
- **Prefix**: `runbook-`
- **Purpose**: a step-by-step operational procedure — deploy, restore,
  rotate, migrate, release, submit. The page is executable documentation:
  the agent follows it verbatim and proposes edits when reality diverges.

## Signals
- `docs/runbook*`, `RELEASING.md`, `deploy.sh`-style scripts with prose,
  wiki-page checklists
- conversation: "how do we deploy again?", "the release steps"

## Required sections
- `## When to run` — the trigger and preconditions
- `## Steps` — numbered, exact commands with expected output; verification
  step at the end (how you know it worked)
- `## Rollback` — how to undo if a step fails
- `## Facts` — quirks discovered while running it, provenance-tagged

## Ask the user for
- The verification step (most handed-down procedures lack one), and which
  steps require a human decision vs are safe to execute.

## Naming
- `runbook-<slug>.md`, e.g. `runbook-driftwatch-deploy.md`.

## Typical relations
- Operates a `service-`/`pipeline-`/`machine-` target; updated by
  `incident-` lessons.
