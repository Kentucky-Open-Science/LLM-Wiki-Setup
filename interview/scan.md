# The pre-interview scan

Read-only reconnaissance so the interview asks only what cannot be inferred.
Run it at the start of `setup` (and a lighter re-scan in `tune`).

## Rules

1. **Disclose first.** Before reading anything, tell the user exactly what you
   will look at (the list below, trimmed to their OS) and that the scan is
   read-only and local. Wait for a go-ahead.
2. **Read-only.** No file writes, no state changes, no network calls. Reaching
   out to remote machines (even `ssh host hostname`) is NOT part of the scan —
   connectivity is verified later, with permission, in the machines wave.
3. **Never open secrets.** Do not read: private keys (`~/.ssh/id_*` contents),
   `.env` / `.env.*` files, credential stores, keychains, token files,
   `auth.json`-style files inside harness config dirs. For `~/.ssh/config`,
   read host aliases and hostnames only — never key material.
4. **Sample, don't trawl.** Read directory listings broadly but file contents
   narrowly: READMEs, manifests, and instruction files only. Do not read
   project source code during the scan.
5. **Summarize back.** End by showing the user a compact findings table and
   asking them to correct it. Corrections are wiki-worthy facts — keep them
   for the seed step.

## What to look at

**Identity & platform**
- OS and version; shell; `python3 --version` / `py --version`; `git --version`;
  `gh --version` and `gh auth status` (presence only, no tokens printed).
- `git config user.name` / `user.email` (global), plus distinct author
  identities in recent repo history (`git log --format='%an <%ae>'` sampled).

**Where work lives**
- Home-directory top level: names and modification times only.
- Candidate work directories: `~/Developer`, `~/Projects`, `~/code`, `~/src`,
  `~/work`, `~/repos`, plus anything the home listing suggests. For each git
  repo inside: name, remotes, default branch, last-commit date, whether authors
  besides the user appear, README first lines, language mix by extension.
- Candidate writing locations: `~/Documents` top level, Obsidian vaults
  (directories containing `.obsidian/`), LaTeX trees (`*.tex`, `main.tex`,
  Overleaf syncs), Scrivener/Typora/Zotero footprints, `drafts/`,
  `manuscript/`, `notes/` directories.

**Existing agent setup (adopt-and-merge input)**
- `~/.claude/`: `CLAUDE.md`, `settings.json` (read; it may contain no secrets,
  but do not echo anything token-like), `commands/`, `skills/` listings.
- `~/.codex/`: `AGENTS.md`, `config.toml` (same caution), `prompts/` listing.
- free-claude-code config presence (its install dir / proxy config), noting
  only that it exists and where.
- Work-dir and repo-level `CLAUDE.md` / `AGENTS.md` files — read fully; these
  are the adoption inputs.
- Existing wikis: directories that look like a knowledge vault (an `index.md` +
  many interlinked `.md` files, or `.obsidian/`), especially git repos.

**Machines & infra evidence**
- `~/.ssh/config`: Host aliases, hostnames, users (never keys). Note
  ControlMaster/keepalive settings.
- SLURM/cluster traces: `*.sbatch`, `slurm-*.out`, `#SBATCH` lines in scripts.
- Container traces: Dockerfiles, `docker-compose.yml`, `singularity`/
  `apptainer` files. GPU evidence: `nvidia-smi` on PATH (run it only if
  present; it is read-only).
- Windows specifics: whether OpenSSH client is present, whether WSL exists
  (`wsl -l` if on Windows).

**Activity signals for the schema** (see `types/` — each type file lists its
own signals; collect the evidence, match it later)
- Experiment tracking (`wandb/`, `mlruns/`, `runs/`, `checkpoints/`),
  notebooks, `data/` directories, model files in `.gitignore`s.
- Service/product traces (deploy configs, `k8s/`, `Procfile`, CI workflows).
- Pipeline/orchestration traces (`dags/`, `dbt_project.yml`, Airflow/Prefect).
- Writing traces (LaTeX, `references.bib`, citation managers, long-form
  markdown, publisher correspondence folders — names only).
- Ops traces (Ansible/Terraform, runbook-like docs, monitoring configs).

## Findings summary format

Present one table: `Area | What I found | Confidence | My inference`. Follow
with: "Corrections? Anything important I could not see?" Log the corrected
summary — it seeds both the interview defaults and the wiki's first pages.
