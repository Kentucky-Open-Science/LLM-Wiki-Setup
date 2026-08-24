# Interview topics — the adaptive waves

The interview is a conversation, not a questionnaire. Ask in short waves, skip
whatever the scan already answered (confirm inferences instead of re-asking),
and keep each wave to a handful of questions. Batch related questions; where
the harness supports structured multiple-choice prompts, use them; always mark
a recommended option and say why in one line. Record every answer — they land
in `<wiki>/setup/answers.md`.

## Wave 1 — Confirm the scan

Show the findings table (`scan.md` format). Ask only: what's wrong, and what's
missing. If an existing setup or wiki was found, ask whether to **adopt** it
(read + merge + diff — the default) or start clean beside it.

## Wave 2 — Identity & activities

- Name as it should appear in generated files and git attribution (confirm
  the inferred `git config` identity; collect alternate emails/identities).
- The activities that make up their work — *proposed from evidence, then
  edited by the user*: e.g. ML research / product engineering / data
  engineering / ops / long-form writing / teaching / anything else. Multiple
  is normal; this drives the schema wave.
- Who else appears: collaborators, labs/teams, orgs (seeds `entity-` pages;
  determines whether the solo-vs-collaborative push policy matters).

## Wave 3 — The wiki

- **Name** it (default: `wiki`; the name becomes the repo name, the directory
  name, and how the agent refers to it — e.g. "the Atlas" reads better than
  "the knowledge base").
- **Location** on disk (default: `~/<name>`).
- **Private remote**: recommend creating it as a private GitHub repo now
  (`gh repo create`) so it syncs and survives the laptop; confirm, never
  assume. Local-only `git init` is a fine fallback; the remote can come later.
- **Obsidian** as the viewer: default ON (versioned core settings, graph
  colors by type, Dataview suggestion). Easy to decline — the wiki is plain
  markdown either way. See `modules/obsidian.md`.
- **Rule strictness** — each defaults ON, each independently adjustable
  (see `interview/policies.md` for the recommendation script):
  provenance tags on every factual bullet · `draft`/needs-verification
  discipline · passive capture · consult-first.

## Wave 4 — Schema composition

Per `types/README.md`: match the scan's activity evidence against each type
file's Signals section, then propose **lean**:

- Core five always in: `project`, `entity`, `concept`, `reference`,
  `synthesis`.
- Strongly-evidenced catalog types listed with one line of evidence each
  ("4 repos with sbatch scripts and wandb dirs → `experiment`, `dataset`,
  `model`").
- Weakly-evidenced types get one line total: "I also saw hints of X — want
  any of them?"
- Ask what the catalog misses; **mint** new types with `types/_template.md`
  when an activity genuinely needs different sections (not just a tag).

The user edits the list. The composed schema — catalog selections plus minted
types — is what `templates/wiki-schema.md` gets generated from. Say
explicitly: the schema is living; `tune` re-proposes it as work shifts, and
`audit` flags types that never got pages.

## Wave 5 — Machines & where agents run

Skip entirely for a single machine with no SSH evidence — say so in one line.
Otherwise, per `modules/machines.md`:

- Inventory: for each machine — role (laptop / workstation / GPU node /
  shared cluster / secure box), ownership (personal vs shared), reachability.
- **Where do agent sessions run?** (Just the laptop? On the workstation over
  SSH? On several?) For each host that runs agents: which harness, and
  whether sessions must survive disconnects (tmux/screen on POSIX; WSL or
  persistent terminals on Windows).
- **Remote steering:** Claude Code and Codex sessions can be steered from
  their apps; free-claude-code cannot — if they use it remotely, design
  around SSH + tmux and say so plainly.
- Shared clusters trigger `modules/cluster-guardrails.md`: account/allocation
  discipline, read-before-write defaults, PHI/secure-box handling if it
  applies.
- Each machine becomes a `machine-` page (`templates/machine-page.md`,
  type: `types/machine.md`) — the
  guardrails section is the point, not the hardware inventory.

## Wave 6 — Policies

Walk `interview/policies.md`: attribution, data-in-git + size guard, push
authorization (solo vs collaborative), sync discipline, per-repo instruction
files (explicit opt-in), skills/commands (explicit opt-in). Every policy has a
stated recommendation and a one-line rationale; the user can take the
defaults in one breath ("recommended for all") or adjust any.

## Wave 7 — Seed plan

Rank what the scan found (recency, remotes, README quality, cross-references)
and propose a checklist: which repos get `project-` pages now, which machines
get `entity-` pages, which collaborators, which datasets/sources. The user
checks items off. Everything seeded carries provenance (`file:` for what was
read, `conv:` for what they told you). Un-seeded items are not lost — passive
capture files them when they come up.

## Then

Assemble the full plan (files, targets, network actions), get approval, and
proceed — `flows/setup.md` § "Generate".
