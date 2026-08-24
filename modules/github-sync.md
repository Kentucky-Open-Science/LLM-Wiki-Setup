# Module: git sync — the remote is the hub

Enabled by policy P5. On one machine this is versioning plus off-site backup
of the memory; on many machines it is what makes one brain possible. GitHub
is assumed below; any git host works identically.

## The model

Code and the wiki move between machines **through git only** — never by
copying working trees around. Every machine holds clones; the remote is the
single source of truth; laptops and workstations converge on it.

- **Session start** in any repo (wiki included): `git pull --ff-only`.
  `--ff-only` makes divergence loud instead of silently merging.
- **Natural stopping points and session end**: commit and push. **Unpushed
  work is invisible to every other machine — work is not done until
  pushed.** Session wrap-ups state what was pushed.
- The wiki additionally commits+pushes **after every capture/ingest/lint**
  — a capture that isn't pushed doesn't exist for the other machines.

## Authorization (policy P4)

- **Solo repos** (every commit authored by the user): standing authorization
  — the agent commits and pushes without asking, any branch.
- **Collaborative repos** (history contains other authors — check
  `git log --format='%an <%ae>' | sort -u` against the user's identities):
  local commits are fine; **every push requires approval, every time.**
  A repo's own instruction file may declare its status explicitly and
  override the heuristic.
- **Always ask, regardless**: force-push, history rewrites, deleting a repo,
  changing visibility, any push to a public repo.

## What never reaches the remote (policy P2)

Bulk data, model weights, checkpoints, build artifacts, `.env`, credentials.
Enforced three ways: the managed `.gitignore` block
(`templates/gitignore-block.txt`, tailored to the user's formats), the
pre-commit size guard (`templates/hooks/pre-commit`), and instruction-file
policy. Datasets move between machines only by explicit rsync/scp/robocopy
for a specific task. Secrets: the wiki records *where* they live, never
values; keep `.env.example` current.

## Normalizing a repo

Bringing a repo under management = confirm remote + default branch; append
the gitignore block; install the size-guard hook; determine solo vs
collaborative and record it; optionally add per-repo instruction files (P6).
`flows/add.md` § repo runs this; setup's seed step offers it for existing
repos.

## Conflict posture

`--ff-only` pulls fail rather than merge. On failure: stop, show the user
the divergence, and resolve deliberately (usually: the other machine forgot
to push, or two sessions edited the same repo — rebase the smaller side).
Never resolve wiki conflicts by discarding either side's captures: merge
both, then re-run the capture log entries.
