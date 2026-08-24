# Hub operating contract

This repository — **LLM-Wiki-Setup** — is the user's **hub**: the tooling an AI
agent runs to set up, tune, audit, and extend that user's agentic development
system. Any agent operating in this directory is bound by this contract.

> Keep CLAUDE.md and AGENTS.md identical. They are the same contract for
> different harnesses (Claude Code / free-claude-code read CLAUDE.md; Codex
> reads AGENTS.md).

## The two absolute rules

1. **Never modify this repository.** No tracked file here is ever edited,
   created, or deleted by a setup, tune, audit, or add run. The only local
   write permitted is the untracked, gitignored pointer file `.wiki-path`.
   `git status` in the hub must be clean before and after every flow. The hub
   changes only via `git pull` from upstream.
2. **All user state lives in the user's wiki repo.** Interview answers, the
   decision log, generated instruction sources, the deploy manifest, minted
   page types — everything lands in `<wiki>/setup/` and `<wiki>/config/`, or
   in the deploy targets the user explicitly approves (their home-dir agent
   configs, their work directory, their repos). Nothing user-specific is ever
   written anywhere else.

## Orientation

| Path | What it is |
|---|---|
| `.wiki-path` | Untracked one-line file: absolute path to the user's wiki repo. Present ⇒ a setup already exists — read `<wiki>/setup/` before doing anything. Absent ⇒ first run (or the pointer was lost; ask, then recreate it). |
| `flows/` | The four canonical procedures: `setup.md`, `tune.md`, `audit.md`, `add.md`. Flows are the source of truth; skills and slash commands are thin pointers to them. |
| `interview/` | How to scan (read-only, disclosed) and what to ask: `scan.md`, `topics.md`, `policies.md`. |
| `types/` | The page-type catalog + the meta-schema (`_template.md`) for minting new types. Each type file carries its own detection signals. |
| `templates/` | Sources for every generated file: global instructions, working guidelines, per-repo instructions, the wiki schema, the machine page, the gitignore block, the pre-commit size guard. |
| `modules/` | Optional capability layers: `machines.md`, `cluster-guardrails.md`, `github-sync.md`, `obsidian.md`. |
| `skills/` | Ready-made slash commands / prompts for Claude Code and Codex, installed only if the user opts in. |
| `tools/` | Cross-platform Python 3 (stdlib only): `deploy.py`, `wiki_lint.py`, `sync_pair.py`. Run manually or by a flow — never wired to hooks, CI, or schedules. |
| `example-wiki/` | A small synthetic wiki (fictional user) showing what good looks like. Read-only reference; never copied into a user's wiki. |

## Running a flow

- "Set me up" / first contact → `flows/setup.md`.
- "Tune / improve / change my setup" → `flows/tune.md`.
- "Audit / check my wiki" → `flows/audit.md`.
- "Add a machine / repo / collaborator" → `flows/add.md`.
- Ambiguous request + `.wiki-path` exists → ask which flow; default to `tune`.

## Conduct

- **Scan ethics:** the pre-interview scan is read-only, disclosed before it
  happens, and never opens secrets (`.env`, private keys, tokens, credential
  stores). Nothing collected leaves the machine. See `interview/scan.md`.
- **Propose before creating.** Every flow ends its planning phase with a
  concrete plan (files to be created, repos to be touched, network actions)
  that the user approves before anything is written.
- **The user's wiki is private by default.** Creating it as a private GitHub
  repo is recommended and confirmed, never assumed.
- **Cross-platform always.** Windows, macOS, and Linux are all first-class.
  Never emit a procedure that only works on one of them without naming the
  equivalents for the others.
- **Harness honesty.** Claude Code and Codex support remote steering of
  sessions; free-claude-code does not. Skills/commands, config locations, and
  instruction-file loading differ per harness — say what actually holds for
  the user's harness rather than assuming Claude Code.
