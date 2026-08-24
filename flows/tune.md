# Flow: tune — refine an existing setup

Run when the user wants their system improved, changed, or re-fitted: a
policy reversed, the schema evolved, new instructions merged, friction
removed. Tune is setup's adaptive re-run — same contract, but it starts
from recorded state and touches only what needs to change.

## 1. Load state

- Read `.wiki-path` → wiki. Missing? Ask for the wiki location, validate
  (`setup/` present), recreate the pointer.
- Read `setup/answers.md`, `setup/decisions.md`, `setup/manifest.json`,
  `setup/hub-version.txt`, and the wiki schema. This is the baseline — do
  not re-ask what it answers.

## 2. Check the two drifts

- **Hub drift**: recorded hub version vs current
  (`git -C <hub> log --oneline <recorded>..HEAD`). Summarize upstream
  changes relevant to this user (new catalog types, template improvements,
  policy additions) as *offers*, never silent applications.
- **Deploy drift**: `tools/deploy.py --wiki <wiki> check`. A hand-edited
  deployed copy is a signal, not an error — the user wanted a behavior their
  sources lack. Offer to fold each hand-edit back into the source (then
  redeploy); folding in, discarding, or leaving it is their call.

## 3. Hear the feedback

Ask what prompted the tune, then probe the known friction points concisely:
capture too chatty or too timid? provenance rules helping or in the way?
schema fitting — types unused, or pages straining their type? machines and
guardrails still accurate? per-repo files pulling their weight? skills
used? Also run a lightweight re-scan (scan.md, findings-only) when the
user's world may have shifted — new repos, new machines, new activities.

## 4. Re-propose (only what changes)

- Map each piece of feedback to the answer/policy it revises.
- **Schema evolution**: propose additions from new evidence (lean, as in
  Wave 4), retirements for zero-page types (`audit` data helps), splits for
  strained ones. Retiring never deletes pages — re-type or annotate them.
- Present a delta plan: files to regenerate, diffs against current
  generated files, repos touched, anything de-installed. Approval gate,
  exactly as setup step 6.

## 5. Apply

Regenerate only affected files (templates + updated answers), back up
replaced deployed copies to `setup/backups/<date>/`, redeploy via
`deploy.py`, update `answers.md`, append the change to `decisions.md`
(what changed, why, date — this log is what makes the next tune fast),
refresh `hub-version.txt`, commit; push if remote.
`log.md`: `## [DATE] tune | <one line>`.

## 6. Verify & wrap

Setup step 8 checks (deploy check, lint, sync_pair, hub clean). Wrap up
with what changed, what was declined, and anything deferred.

## Adopting mid-stream

"I wrote my own rules into a deployed file since setup" is normal tune
input — handle via drift-folding (step 2). "I have a whole new machine /
repo / collaborator" routes to `flows/add.md`; finish the tune first or
run add standalone.
