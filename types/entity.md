# entity — a person, organization, or machine

- **Tier**: core (always included)
- **Prefix**: `entity-`
- **Purpose**: anyone or anything with identity and behavior: collaborators,
  labs/teams/orgs, and — critically — **machines**. A machine's entity page is
  its operating manual: connection, quirks, and guardrails the agent obeys
  (see `templates/machine-page.md`).

## Signals
Core — no evidence needed. (Every collaborator in git history, every SSH host,
every org the user names is a candidate page.)

## Required sections
People/orgs: `## Role` · `## Affiliations` · `## Built/Contributed` (links) ·
`## Facts`.
Machines: `## Role` · `## Hardware` · `## Storage` · `## Stack` ·
`## Connection` · `## Guardrails` · `## Facts` — use the machine template;
the Guardrails and gotcha-Facts sections are the point.

## Ask the user for
- People: role, affiliation, what they own/built, contact conventions.
- Machines: ownership (personal vs shared), what must never be touched,
  scheduling/run conventions, where secrets for it live (never the values).

## Naming
- `entity-<name-slug>.md`, e.g. `entity-priya-nair.md`, `entity-harbor.md`.

## Typical relations
- Linked from nearly everything; machines link to the projects that run on
  them and sibling machines (division of labor).
