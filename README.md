# LLM-Wiki-Setup

**Give your coding agent a memory and a map.**

This is a setup kit that an AI agent (Claude Code, Codex, or free-claude-code)
runs against your machine to build you a personal agentic work system:

- A **private knowledge wiki** — a git repo of verified, provenance-tagged facts
  about your projects, machines, data, sources, and collaborators. Your agent
  consults it before asking you anything, files new facts passively as you work,
  and never presents a guess as a fact. It is the shared memory between
  sessions, between machines, and between you and the agent.
- A **layered instruction stack** — global policy → working guidelines →
  (optionally) per-repo instructions → the wiki's own schema — generated for
  *your* tools, *your* machines, and *your* kind of work, and kept identical
  across the harnesses you use.
- A **sync discipline** — GitHub as the hub — that lets any number of machines
  (a laptop, a GPU box, a shared cluster) share one brain, with guardrails for
  the machines that need them.

It is built by **interview, not template-filling**: the agent first scans your
machine (read-only, disclosed up front), infers what it can, and asks only what
it can't. And it is **not domain-locked**: the wiki's page-type schema is
composed per user from a catalog of types with a mechanism for minting new
ones — it fits deep-learning research, product engineering, data work, ops,
and long-form writing equally, including all of them at once.

## The problems this solves

| Without | With |
|---|---|
| Every session starts from scratch; you re-explain your projects, paths, and what you already tried | The agent reads the wiki's `index.md` first and answers from filed, cited facts |
| Agent "memory" is confabulated or stale | Only verified facts enter the wiki; every fact carries a provenance tag; uncertainty is marked `draft` and asked about, never guessed |
| Each machine (and each harness) has its own drifting configuration | One generated instruction stack, versioned in your wiki repo, deployed by copy to every harness and machine, with drift detection |
| Remote machines are re-explained every time, and shared clusters are one confident mistake away from disaster | Each machine is a wiki page that doubles as its operating manual — connection, quirks, and explicit guardrails the agent obeys |

## Quickstart

1. **Clone this repo** anywhere you like. The clone becomes your **hub** — the
   place you return to whenever you want to set up, tune, or audit your system.
   The hub itself is never modified: everything generated lands in *your* wiki
   repo and the config locations you approve, so `git pull` here is always clean.
2. **Open your agent inside the clone:**
   - Claude Code or free-claude-code: run `claude`
   - Codex: run `codex`
3. **Say: "Set me up."**

The agent discloses what it will scan, interviews you in short adaptive waves,
proposes a plan, and only then creates anything. Expect 15–40 minutes depending
on how much of your existing world you want ingested on day one.

**Already have CLAUDE.md files, an AGENTS.md, or a wiki?** Setup adopts and
merges: it reads what you have, maps it onto the schema, and shows you a diff —
your existing rules survive; nothing is overwritten silently. Re-run any time:

- *"Tune my setup"* — refine anything, from one policy to the whole schema
- *"Audit my wiki"* — health check: orphans, missing provenance, config drift
- *"Add a machine / repo / collaborator"* — targeted extension flows

## What you end up with

```
your-wiki/  (private git repo — the memory)     your machine(s)
├── CLAUDE.md + AGENTS.md   wiki schema          ~/.claude/CLAUDE.md      ┐ deployed
├── index.md                catalog: read first  ~/.codex/AGENTS.md       │ copies of
├── log.md                  append-only history  <work-dir>/CLAUDE.md     │ config/
├── wiki/*.md               typed, linked,       <work-dir>/AGENTS.md     ┘ sources
│                           provenance-tagged    <repo>/CLAUDE.md  (optional, per repo)
│                           pages                <repo>/.git/hooks/pre-commit  (size guard)
├── config/                 instruction sources   ~/.claude/commands/*  (optional skills)
└── setup/                  your answers, the    ~/.codex/prompts/*    (optional skills)
                            decision log, the
                            deploy manifest
```

Single machine works fully on day one. Multi-machine (SSH, remote dispatch,
shared-cluster guardrails, secure boxes) is an optional module the interview
offers when it sees the evidence.

## Supported agents

| Harness | Reads | Remote steering | Skills / commands |
|---|---|---|---|
| **Claude Code** | `CLAUDE.md` (global, work-dir, repo) | Yes (Claude app / remote control) | Yes — installed on opt-in |
| **Codex** | `AGENTS.md` (global `~/.codex/`, repo root) | Yes (cloud tasks / IDE) | Yes — custom prompts, installed on opt-in |
| **free-claude-code** | `CLAUDE.md` (same conventions as Claude Code) | **No** — plan on tmux/screen + SSH instead | Local slash commands work |
| Anything else | `AGENTS.md` is vendor-neutral; most harnesses read it | varies | varies |

Windows, macOS, and Linux are all supported; shipped tooling is Python 3,
standard library only.

## What it will and won't do

- The scan is **read-only and disclosed before it happens**. Secrets, private
  keys, `.env` files, and credential stores are never opened.
- **Nothing leaves your machine.** The only network actions are git/GitHub
  operations you explicitly approve (e.g. creating your private wiki repo).
- Your wiki repo is created **private** — recommended, and confirmed with you.
- **This repo is never modified by your setup.** All state lives in your wiki.
- Nothing runs automatically: no hooks you didn't approve, no CI, no
  schedulers. Lint and audit run when you invoke them.

---

## Agent directive

**If you are an AI agent reading this, you have been asked to set up (or tune,
audit, or extend) this user's agentic work system. Proceed as follows:**

1. Read `CLAUDE.md` / `AGENTS.md` in this directory — the operating contract.
   Two rules bind every flow: **never modify this repository**, and **all
   user-specific state goes to the user's wiki repo or the deploy targets they
   approve** — nowhere else.
2. Check for `.wiki-path` here. Present ⇒ a setup exists: read
   `<wiki>/setup/` first. Absent ⇒ first run.
3. Route the request:
   - first-time setup, "set me up" → **`flows/setup.md`**
   - an existing setup with no recorded baseline → **`flows/adopt.md`**
   - refine an existing setup → **`flows/tune.md`**
   - health check → **`flows/audit.md`**
   - new machine, repo, or collaborator → **`flows/add.md`**
4. Follow the flow exactly. Flows are canonical; skills and slash commands are
   thin pointers to them. Do not improvise a different procedure.
