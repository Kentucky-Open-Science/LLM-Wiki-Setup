# Policies — each asked, each with a recommendation

Every opinionated behavior in the generated setup is a **policy**: asked in the
interview, shipped with a stated recommendation, and independently reversible
later via `tune`. Never silently impose one; never ask without recommending.
Record each decision (choice + one-line reason) in `<wiki>/setup/answers.md`.

Present policies in the groupings below. Users who want speed can accept all
recommendations in one go.

## P1 — Attribution on git activity

**Question:** whose name goes on commits, PRs, and issues the agent produces?
**Recommendation: the user's name alone.** The user directs the work and owns
it; mixed attribution also breaks `git log`-based tooling (including policy
P4's authorship detection). Effect when ON: generated instructions forbid
`Co-Authored-By` trailers, "Generated with…" lines, and agent-branded branch
names; for Claude Code, `"includeCoAuthoredBy": false` is set. If the user
prefers AI attribution, honor it — note that P4's solo-repo detection then
needs the agent identity added to its "user identities" list.

## P2 — Data never reaches the remote

**Question:** should generated `.gitignore` blocks and a pre-commit size guard
keep datasets, model weights, checkpoints, and build artifacts out of git?
**Recommendation: ON, with the 50 MB size guard.** Large binaries in git are
nearly irreversible (history rewrites to remove them are painful), and private
data in a repo is one visibility change from a leak. Effect: repos the setup
touches get `templates/gitignore-block.txt` (tailored to the user's file
types — the shipped block is generic; add the user's formats) and
`templates/hooks/pre-commit` (limit adjustable). Datasets move between
machines by explicit `rsync`/`scp` for a task, never git. `.env` and
credentials are never committed; keep `.env.example` current instead.

## P3 — Secrets policy

**Question:** confirm the handling of secrets in the generated system.
**Recommendation: ON, not negotiable in spirit.** The wiki is git-tracked and
possibly remote: it records *where* a secret lives (keychain, local
chmod-600 file), never the value. Instruction files never inline tokens.
Only the mechanics (which keychain, which file) vary by user and OS.

## P4 — Push authorization: solo vs collaborative repos

**Question:** when may the agent commit and push without asking?
**Recommendation: standing authorization for solo repos, ask-every-push for
collaborative ones.** A repo is *collaborative* iff its history contains
commits authored by someone other than the user (check:
`git log --format='%an <%ae>' | sort -u` against the user's identities from
Wave 2) — org placement is irrelevant, and a repo's own instruction file may
override the heuristic explicitly. Always-ask regardless: force-push, history
rewrites, deleting a repo, changing visibility, and any push to a public
repo. Conservative users can choose ask-always; recording that choice still
lets `tune` relax it later.

## P5 — Sync discipline

**Question:** adopt the hub-and-spoke sync rhythm? (See `modules/github-sync.md`.)
**Recommendation: ON — even on a single machine.** Pull `--ff-only` at
session start; commit and push at natural stopping points and session end;
the wiki commits+pushes after every capture. Multi-machine, this is what
makes one brain possible ("unpushed work is invisible to your other
machines"); single-machine, it is versioning and off-site backup of the
memory. If the wiki stays local-only (no remote), the push clauses degrade
gracefully to commit-only — generate them accordingly.

## P6 — Per-repo instruction files

**Question:** should setup write a `CLAUDE.md`/`AGENTS.md` into each of the
user's existing repos (explicit opt-in, chosen repo-by-repo in the seed
plan)? **Recommendation: yes for actively-developed repos, skip dormant
ones.** The per-repo file holds only what the agent needs every time it opens
that repo (entry points, run/verify commands, working rules, a link to the
repo's wiki page) — depth stays in the wiki. Files are committed to those
repos (they belong to them); in collaborative repos this lands on a branch or
is left uncommitted for the user to propose, per P4.

## P7 — Skills / slash commands

**Question:** install the ready-made command set? (`skills/README.md`:
`/wiki-audit`, `/wiki-tune`, `/wiki-add`, `/wiki-ingest`, `/wiki-sync` — thin
pointers to hub flows and the wiki's own workflows.) **Recommendation: ON for
Claude Code and Codex; ON for free-claude-code** (local command files work
there too). Installed copies have the hub and wiki paths substituted; they
are pointers, so hub updates improve them without reinstallation.

## P8 — Wiki rule strictness

Four toggles, all **recommended ON** — they are what makes the memory
trustworthy rather than plausible-sounding clutter:

- **Provenance tags** on every factual bullet (`— conv:DATE`, `— file:PATH|URL`,
  `— verified:DATE`, `— exp:[[experiment-x]]`, `— [[page]]`). *This is the
  load-bearing one; without it the wiki degrades into unsourced assertions.*
- **Draft discipline**: plausible-but-unverified ⇒ `status: draft` +
  `> [!needs-verification]` + ask the user. Never present a draft fact as
  established.
- **Passive capture**: every user message is scanned for wiki-worthy facts,
  filed without asking, reported in one line. (Users who find this noisy can
  switch to ask-before-filing — capture-on-request only.)
- **Consult-first**: before asking the user for project/data/machine info,
  read `index.md` and drill pages; ask only what is genuinely missing.

Softening any of these is legitimate (a solo writer may not want provenance
tags on every line); generate the wiki schema to match what was chosen, and
record the choice so `audit` lints against the *chosen* rules, not the
defaults.

## P9 — Obsidian

**Question:** set up Obsidian as the wiki's viewer? **Recommendation: ON.**
Effect per `modules/obsidian.md`: versioned core settings, graph colors by
type, Dataview suggestion. Declining changes nothing structural — the wiki is
plain markdown + git either way, and `[[wikilinks]]` remain the link style.
