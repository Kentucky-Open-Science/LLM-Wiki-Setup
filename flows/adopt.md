# Flow: adopt — record an existing setup as the baseline

**Adoption is the common case.** The users most likely to arrive here
already have a working system — instruction files, a wiki, deployed
configs, conventions they trust. Adopt turns that reality into the recorded
baseline (`setup/` state + `.wiki-path`) that makes every later `tune`
cheap. The one rule that makes it safe:

> **Adopt records; it does not change.** Nothing about the working setup is
> edited, moved, renamed, or "corrected" in this flow. Divergences from hub
> defaults are recorded as decisions, not fixed. Changes belong to `tune`,
> after a baseline exists.

## When you land here

- `setup` step 1 or step 2 finds an existing wiki or instruction stack.
- `tune` step 1 finds a wiki with no `setup/` baseline.
- The user says any variant of "I already have a setup — adopt it."

## 1. Locate the pieces

Ask + scan (per `interview/scan.md` rules — read-only, disclosed): the wiki
root; deployed instruction files per harness (global, work-dir, per-repo);
installed commands/prompts; hooks; how deployment works today (copies?
symlinks? an install script?). Symlink-based deployment is valid and stays
— `deploy.py` treats a target that resolves to its source as `ok (linked)`.

## 2. Read everything fully

Every instruction file, the wiki schema, `index.md`, a sample of pages, any
install/sync scripts. **Read before you classify** — a file that trips
mechanical heuristics (no frontmatter, unlinked, odd location) is a file to
read, never a file to dismiss. Ten seconds of reading routinely reverses
the mechanical call.

## 3. Reconstruct `setup/`

Write into the wiki (`setup/`), the only writes in this flow:

- **`answers.md`** — the interview answers *as this setup implies them*,
  each tagged with how it was obtained:
  - `stated:` the user said it in this run
  - `obs:` observed mechanically (a file, a config key, a git log)
  - `doc:` asserted by the setup's own documentation
  - `inf:` inferred — plausible, unconfirmed
  `tune` trusts `stated:`/`obs:`, cites `doc:`, and re-confirms `inf:` when
  it becomes relevant. List the open `inf:` items at the end.
- **`manifest.json`** — from deployment *reality*: each live instruction
  file mapped to its actual source, symlinked targets included as-is.
- **`decisions.md`** — first entry: what was adopted, which conventions
  were kept verbatim, and every divergence from hub defaults *as a decision
  with its apparent rationale* (so no future run relitigates or "fixes" it
  blind).
- **`custom-types/`** — for each page type the wiki uses that the catalog
  lacks: write its definition in `types/_template.md` shape by reading its
  actual pages.
- **`hub-version.txt`**, and `.wiki-path` in the hub clone.

## 4. Verify (record, don't repair)

- `deploy.py --wiki <wiki> check` — expect all `ok`/`ok (linked)`; drift
  here means the manifest is wrong, not the setup.
- `wiki_lint.py <wiki>` — record the finding count and categories in
  `decisions.md` as the **lint baseline** (with the `--log-since` date if
  legacy log entries predate the current format). Do not fix findings now.
- `sync_pair.py --check` on each pair location (lone-file locations pass).
- Hub clean; wiki committed (and pushed, if it has a remote).

## 5. Hand off

Summarize: what was recorded, the open `inf:` items, the lint baseline,
and the divergences filed as decisions. Then offer `tune` — which now has
everything it needs to be cheap.
