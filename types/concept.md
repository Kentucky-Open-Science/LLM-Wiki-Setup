# concept — a method, technique, or idea in use

- **Tier**: core (always included)
- **Prefix**: `concept-`
- **Purpose**: a named method/technique/topic the user's work relies on — an
  algorithm, a statistical method, a writing technique, an architectural
  pattern. The page answers: what is it, and how is it used *here*.

## Signals
Core — no evidence needed. (Mint pages as concepts recur in conversation or
sources.)

## Required sections
- `## Definition` — crisp, cited
- `## How it's used here` — links to the projects/experiments/manuscripts
  that apply it, with the local specifics
- `## Sources` — where the definition comes from

## Ask the user for
- The local usage details no source can supply: which variant, which
  hyperparameters/settings, why it was chosen here.

## Naming
- `concept-<term-slug>.md`, e.g. `concept-isolation-forest.md`. Use
  frontmatter `aliases` for abbreviations so `[[IF]]`-style links resolve.

## Typical relations
- Linked from `project-`, `experiment-`, `paper-`, `manuscript-`,
  `decision-` pages; links out to `reference-`/`paper-` sources.
