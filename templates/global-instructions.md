<!-- generator: this becomes <wiki>/config/global.md, deployed to
     ~/.claude/CLAUDE.md (Claude Code / free-claude-code) and
     ~/.codex/AGENTS.md (Codex). It loads in EVERY session on this machine,
     so keep it policy-only and short: machine facts belong in the wiki,
     project facts in per-repo files. Resolve if-blocks from interview
     policies; for Codex-only users, fold working-guidelines.md content in
     here (Codex loads no work-dir layer). -->
# Global agent policy — {{USER_NAME}}

Applies to every agent session on every machine. Machine facts live in the
wiki (`entity-` pages); project facts live in each repo's instruction file.

## The wiki — your memory

{{USER_NAME}}'s knowledge wiki, **{{WIKI_NAME}}**, lives at `{{WIKI_PATH}}`
(schema: its own CLAUDE.md/AGENTS.md). In every session:

<!-- BEGIN if:P5-remote -->
1. **Pull it, then consult it first.** Before asking {{USER_NAME}} about
   their projects, data, machines, results, or people:
   `git -C {{WIKI_PATH}} pull --ff-only`, read `index.md`, drill the pages.
   Ask only what is genuinely missing.
<!-- END if:P5-remote -->
<!-- BEGIN if:P5-local-only -->
1. **Consult it first.** Before asking {{USER_NAME}} about their projects,
   data, machines, results, or people: read `index.md`, drill the pages. Ask
   only what is genuinely missing.
<!-- END if:P5-local-only -->
2. **Capture facts {{USER_NAME}} states** (per the wiki schema's standing
   behaviors): file, cross-link, index, log — then report in one line.
3. **Ask-then-file** missing details rather than guessing.
4. **No speculation in the wiki** — uncertain facts are `draft` +
   `needs-verification`.
<!-- BEGIN if:P5-remote -->
5. **Every capture ends with commit and push.** An unpushed capture doesn't
   exist for the other machines.
<!-- END if:P5-remote -->

<!-- BEGIN if:module-machines -->
## Devices

| Device | Role | Reach |
|---|---|---|
{{DEVICE_TABLE}}
<!-- generator: one row per machine from the interview; keep each cell short
     and put depth in the machine's entity- page — link it. Note which
     machines host agent sessions and which are reached over SSH; mark
     laptops that are "often asleep — unreachable is normal, never an
     error" where that applies. -->

Full connection details, guardrails, and per-device gotchas: the `entity-`
pages. Consult the wiki before asking {{USER_NAME}}.
<!-- END if:module-machines -->

<!-- BEGIN if:P1-sole-attribution -->
## Attribution — absolute rule

All git/GitHub activity is authored by **{{USER_NAME}} <{{GIT_EMAIL}}>**
alone. Never add `Co-Authored-By`, "Generated with…", or any AI attribution
to commits, PRs, issues, or comments; never create agent-branded branch
names.
<!-- END if:P1-sole-attribution -->

<!-- BEGIN if:P5-remote -->
## Sync — GitHub is the hub

Code and the wiki move between machines through git only (full model: the
hub's `modules/github-sync.md`).

- **Session start** in a repo: `git pull --ff-only`.
- **Natural stopping points and session end**: commit and push. Work is not
  done until pushed.
- **Standing authorization** (act without asking): commit+push to
  {{USER_NAME}}-solo private repos under `{{WORK_DIR}}`; commit+push the
  wiki.
- **Always ask first**: force-push, history rewrites, deleting a repo or
  changing its visibility, any push to a public repo.
- **Collaborative repos** — history contains commits by anyone besides
  {{USER_NAME}} ({{USER_IDENTITIES}}) — local commits are fine, but **every
  push requires approval**. A repo's own instruction file may declare its
  status explicitly, which overrides the heuristic.

### End of session (non-negotiable)
1. Commit and push every repo you worked in. 2. If you touched the wiki:
commit, push. 3. Say in your wrap-up what you pushed.
<!-- END if:P5-remote -->

<!-- BEGIN if:P2-data-guard -->
## Data & secrets — nothing sensitive reaches the remote

- Data, datasets, model weights, checkpoints, and build artifacts are never
  committed. Managed repos carry the standard `.gitignore` block and the
  pre-commit size guard ({{SIZE_LIMIT_MB}} MB) — install both when
  normalizing a new repo (sources: `{{WIKI_PATH}}/config/`).
- Datasets move between machines only by explicit transfer for a task
  (rsync/scp/robocopy), never git.
- `.env` and credentials are never committed; keep `.env.example` current.
  The wiki records *where* secrets live, never values.
<!-- END if:P2-data-guard -->

## Uncertainty — two modes

- **Interactive** ({{USER_NAME}} is responding): surface assumptions; ask
  before ambiguous or design-level choices.
- **Unattended** (remote/overnight): proceed on the most conservative
  reasonable assumption, record every assumption prominently in output and
  commit messages, and block only when all paths are destructive,
  irreversible, or would make the run worthless.

## Hub

Setup, tuning, audits, and adding machines/repos/people run from the hub
clone at `{{HUB_PATH}}` — never modify the hub repo itself.
