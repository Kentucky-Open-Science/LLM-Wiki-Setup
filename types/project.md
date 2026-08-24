# project — a body of work with a goal

- **Tier**: core (always included)
- **Prefix**: `project-`
- **Purpose**: one endeavor — a codebase, a book, a research effort, a
  migration. The page answers: what is this, where does it live, how do its
  pieces relate, and how does it connect to everything else.

## Signals
Core — no evidence needed. (Each repo, each manuscript-in-progress, each named
effort the user describes is a candidate page.)

## Required sections
- `## Purpose` — what it is and why it exists, in the user's terms
- `## Structure` — key directories/files/parts with one-line roles
- `## Location` — local path(s); remote/cluster mounts; the repo remote
- `## Stack` — languages, frameworks, key tools (or genre/format for writing)
- `## Relationships` — links to related projects, datasets, machines, people
- `## Facts` — provenance-tagged bullets

## Ask the user for
- Anything not readable from the tree: cluster mount paths, entry points,
  which other projects it feeds or consumes, its status (active/paused/done).

## Naming
- `project-<repo-or-effort-slug>.md`, e.g. `project-driftwatch.md`.

## Typical relations
- Links out to `entity-` (people, machines), `dataset-`, `service-`,
  `manuscript-`, `concept-`; linked from `experiment-` and `decision-` pages.
