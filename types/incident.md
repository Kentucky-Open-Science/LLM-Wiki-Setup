# incident — something broke; what was learned

- **Tier**: catalog
- **Prefix**: `incident-`
- **Purpose**: one outage/failure/near-miss and its postmortem: what
  happened, why, what fixed it, what changed to prevent recurrence. The
  cheapest page in the wiki — each one is a debugging session that never
  repeats.

## Signals
- postmortem docs, `#incident` channels referenced in notes, alerting
  configs
- conversation: "when it went down", "the outage", "that data-loss scare"

## Required sections
- `## Timeline` — detection → diagnosis → resolution, timestamped
- `## Impact` — who/what was affected, for how long
- `## Root cause` — the actual mechanism, not the trigger
- `## Fix` — immediate remediation and durable prevention (link `decision-`
  or `runbook-` changes it produced)
- `## Lessons` — provenance-tagged bullets

## Ask the user for
- The root cause as finally understood (early theories are usually wrong),
  and what monitoring/guardrail changed afterward.

## Naming
- `incident-<yyyy-mm>-<slug>.md`, e.g. `incident-2026-01-disk-full.md`.

## Typical relations
- Belongs to a `service-`/`pipeline-`/`entity-` machine; produces
  `decision-`/`runbook-` updates; cited by machine-page guardrails.
