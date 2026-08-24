# entity — a person or organization

- **Tier**: core (always included)
- **Prefix**: `entity-`
- **Purpose**: someone with identity and agency: collaborators, teams,
  labs, companies, institutions. The page answers: who is this, what do
  they own or build, and how does their work touch the user's. (**Machines
  are not entities** — they take the catalog's `machine` type, whose
  required sections are a different shape.)

## Signals
Core — no evidence needed. (Every collaborator in git history and every
org the user names is a candidate page.)

## Required sections
- `## Role` — who they are relative to the user's work
- `## Affiliations` — teams/orgs, with links where paged
- `## Built/Contributed` — what they own or made, linked
- `## Facts` — provenance-tagged bullets (including the one that matters
  for policy: whether they commit to shared repos — that flips those repos
  to collaborative under P4)

## Ask the user for
- Role, affiliation, what they own, contact conventions, and which repos
  and machines they touch.

## Naming
- `entity-<name-slug>.md`, e.g. `entity-priya-nair.md`.

## Typical relations
- Linked from nearly everything; owns `machine-`/`dataset-`/`service-`
  pages; appears in `interview-`-style minted types and `manuscript-`
  acknowledgments.
