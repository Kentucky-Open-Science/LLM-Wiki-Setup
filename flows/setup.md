# Flow: setup — first-run interview and generation

The master flow. You (the agent) run it when the user says "set me up" (or
anything equivalent) in the hub clone. Bound throughout by the hub contract:
**never modify the hub repo; all state goes to the user's wiki and approved
deploy targets.** Nothing is created before the plan is approved (step 6).

## 1. Preflight

- Identify: your harness (Claude Code / Codex / free-claude-code), the OS,
  the hub path. Verify `git` and Python 3 (`python3` or `py`) exist; note
  `gh` presence and auth (needed only if a GitHub remote is wanted).
- If `.wiki-path` exists and points at a valid wiki: a setup already exists
  — summarize it from `<wiki>/setup/` and offer **tune** instead. Continue
  with setup only if the user explicitly wants a second, separate system.
- If the scan (step 2) finds an existing wiki or instruction stack with no
  recorded baseline: route to **`flows/adopt.md`** — record what exists
  first, then tune it. Step 4 below is for the narrower case of generating
  fresh files that must absorb existing ones.

## 2. Scan (read-only, disclosed)

Run `interview/scan.md` exactly: disclose → scan → findings table →
corrections. Existing instruction files and wikis found here are **adoption
inputs**, not obstacles.

## 3. Interview

Run the waves in `interview/topics.md`, with `interview/policies.md` for
Wave 6. Skip what the scan answered; confirm inferences instead of
re-asking; keep every recommendation to one line of rationale.

## 4. Adopt (when an existing setup was found)

For each existing instruction file (global/work-dir/repo level) and any
existing wiki:

- Read it fully. Classify each rule: keep verbatim / keep reworded into the
  generated structure / conflicts with an interview answer (ask) / obsolete
  (confirm).
- The user's own rules survive by default — the generated files must not
  lose a behavior they relied on. Show a before/after diff per file at
  step 6; **nothing is overwritten without the user seeing the diff.**
- An existing wiki is adopted in place when its shape is compatible (pages +
  index; schema mapped onto the composed types, pages progressively
  re-typed by later audits) — prefer adopting over migrating. Only migrate
  page-by-page if the user asks.
- Existing harness settings (`settings.json`, `config.toml`) are edited
  minimally: only keys the interview decided (e.g. attribution), never a
  rewrite. Back up any file you will replace to `<wiki>/setup/backups/<date>/`
  before deploying over it.

## 5. Compose & generate (in a staging dir, not yet deployed)

Build everything in `<wiki-parent>/<wiki-name>/` (creating the wiki
directory is fine now — it was approved in Wave 3; if not yet approved,
stage under the OS temp dir and move later):

1. **Wiki skeleton**: `wiki/`, `index.md` (header + empty type groups),
   `log.md` (first entry: `## [DATE] create | <name> initialized by setup`),
   `.gitignore` (OS noise; `.obsidian/workspace.json` and
   `.obsidian/plugins/` if P9).
2. **Wiki schema**: generate `CLAUDE.md` + identical `AGENTS.md` from
   `templates/wiki-schema.md` — placeholders substituted, if-blocks
   resolved, `{{TYPE_TABLE}}`/`{{TYPE_SECTIONS}}` assembled from the
   composed schema. Minted type definitions → `setup/custom-types/*.md`.
3. **Instruction sources** in `config/`: `global.md` from
   `templates/global-instructions.md`; `working-guidelines.md` from its
   template (unless Codex-only — then fold into global). Copy the tailored
   `gitignore-block.txt` and the substituted `hooks/pre-commit` into
   `config/` too — the wiki, not the hub, is the user's source of truth.
4. **Per-repo files** (P6, per the seed plan): generate each repo's
   `CLAUDE.md` + `AGENTS.md` from `templates/repo-instructions.md` — but
   hold them in staging until deploy.
5. **State** in `setup/`: `answers.md` — every interview answer + policy
   choice with its one-line reason, each tagged with how it was obtained
   (`stated:` the user said it · `obs:` observed mechanically · `doc:` read
   from existing docs · `inf:` inferred, to re-confirm); `decisions.md`
   (append-only; first entry documents this setup); `manifest.json` (see
   below); `hub-version.txt` (hub commit hash + date).
6. **Skills** (P7): prepare command files from `skills/` with
   `{{HUB_PATH}}`/`{{WIKI_PATH}}` substituted.

`manifest.json` — consumed by `tools/deploy.py`:

```json
{ "files": [
  { "source": "config/global.md",
    "targets": ["~/.claude/CLAUDE.md", "~/.codex/AGENTS.md"] },
  { "source": "config/working-guidelines.md",
    "targets": ["<work-dir>/CLAUDE.md", "<work-dir>/AGENTS.md"] }
] }
```

Only harnesses the user actually uses get targets. Per-repo files are NOT
in the manifest — they are committed in their own repos and tracked by that
repo's git.

## 6. The plan — approval gate

Present one complete plan: every file to be created or modified (with diffs
for anything that exists), every repo to be touched, every hook installed,
every network action (repo creation, pushes). Get explicit approval; apply
requested changes and re-present if material.

## 7. Execute

1. `git init` the wiki; first commit. If a remote was approved:
   `gh repo create <owner>/<name> --private --source . --push` (or the
   user's host equivalent). **Private unless the user explicitly said
   otherwise.**
2. Deploy: `python3 <hub>/tools/deploy.py --wiki <wiki-path> deploy`
   (backups per step 4 first). Install hooks into opted-in repos; append
   gitignore blocks; write per-repo instruction files (commit them in solo
   repos; in collaborative repos leave uncommitted or on a branch, per P4).
3. Install skills (P7): Claude Code / free-claude-code →
   `~/.claude/commands/`; Codex → `~/.codex/prompts/`.
4. Write `.wiki-path` in the hub clone (absolute wiki path, one line).
5. Seed (Wave 7 list): one page per approved item, per its type definition
   — provenance-tagged (`file:` what you read, `conv:` what they said),
   cross-linked, indexed. Machines use `templates/machine-page.md`; verify
   SSH reachability (`ssh -o BatchMode=yes <alias> hostname`) only now,
   with permission. `log.md` entry per seeded batch.
6. Obsidian (P9): walk the user through vault creation
   (`modules/obsidian.md`); commit the core settings.
7. Commit everything in the wiki; push if remote.

## 8. Verify

- `python3 <hub>/tools/deploy.py --wiki <wiki> check` → no drift.
- `python3 <hub>/tools/wiki_lint.py <wiki>` → clean (or explained).
- `python3 <hub>/tools/sync_pair.py --check <wiki>` and each deployed
  CLAUDE/AGENTS pair → identical.
- Hub clean: `git -C <hub> status` shows nothing but the ignored pointer.
- Ask the user to open a **new** agent session in their work dir and
  confirm the instructions load (say what "loaded" looks like per harness).

## 9. Wrap up

Tell the user: what was created and where; what was deployed and backed up;
what to try in week one (mention a fact → watch it get filed; ask a question
→ watch it answered from the wiki with citations); and that `tune`, `audit`,
and `add` run from this hub whenever needed. If anything in the plan was
skipped or deferred, list it explicitly.
