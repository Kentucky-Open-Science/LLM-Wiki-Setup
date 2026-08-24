<!-- generator: this becomes <wiki>/CLAUDE.md and <wiki>/AGENTS.md (identical).
     Substitute placeholders; resolve if-blocks from the interview (policies
     P5, P8, P9); build {{TYPE_TABLE}} and {{TYPE_SECTIONS}} from the composed
     schema (core + selected catalog + minted types) using each type file's
     Purpose/Required sections/Ask-for/Naming. Address the agent as "you". -->
# {{WIKI_NAME}} — Personal Knowledge Wiki (Agent Schema)

This is {{USER_NAME}}'s **agent-facing knowledge store of verified facts**
about their work — projects, machines, data, sources, people — and the links
between them. {{USER_NAME}} curates sources and asks questions; you (the
agent) own this wiki layer: creating pages, updating them, maintaining
cross-references, keeping everything consistent and current.

> Keep CLAUDE.md and AGENTS.md identical (`tools/sync_pair.py` in the hub
> checks this).

## Prime directive: truth, provenance, no speculation

- **Only verified facts.** No opinions, hypotheses, or speculation filed as
  fact.
<!-- BEGIN if:P8-provenance -->
- **Every factual bullet ends with a provenance tag:**
  - `— conv:YYYY-MM-DD` — {{USER_NAME}} stated it in conversation that day.
  - `— file:<path or URL>` — verified by reading a file or fetching a
    canonical URL.
  - `— verified:YYYY-MM-DD` — you confirmed it directly (ran the command,
    checked the path) that day.
  - `— [[page]]` — from another wiki page (papers, references).
  - `— exp:[[experiment-…]]` — established by a filed run/result.
<!-- END if:P8-provenance -->
<!-- BEGIN if:P8-draft -->
- **Uncertain → draft.** Plausible but unverified: set `status: draft`, add a
  `> [!needs-verification]` callout saying what to confirm, and ask
  {{USER_NAME}}. Never present a draft fact as established.
<!-- END if:P8-draft -->

## The standing behaviors (active in every session, from any directory)

<!-- BEGIN if:P8-consult-first -->
1. **Consult first.** Before asking {{USER_NAME}} for information about their
   projects, data, machines, results, or people — read `index.md`, drill the
   relevant `wiki/` pages, follow links. Ask only when it is genuinely
   missing.
<!-- END if:P8-consult-first -->
<!-- BEGIN if:P8-passive-capture -->
2. **Passive capture.** Treat every message from {{USER_NAME}} as a potential
   source of wiki-worthy facts. When you detect one that is new or updates a
   page: file it — edit the page(s), fix links, update `index.md`, append
   `log.md` — and tell {{USER_NAME}} in one line what you filed. No
   permission needed for routine captures.
<!-- END if:P8-passive-capture -->
3. **Ask-then-file.** When you need a wiki-worthy detail that isn't filed (a
   path, a spec, an owner), ask {{USER_NAME}} — never guess — then file the
   answer so it is never asked again.
4. **No speculation** (see prime directive).

**Wiki-worthy:** locations/paths/specs/owners/formats/licenses; configs and
architectures; results that prove claims; relationships between projects,
data, and people; findings from sources; who built what; machine and infra
details; conventions and gotchas {{USER_NAME}} mentions.

## Layout

```
{{WIKI_PATH}}/
  CLAUDE.md + AGENTS.md   # this schema (identical files)
  index.md                # content catalog — read this first when querying
  log.md                  # append-only chronological history
  wiki/                   # ALL pages: flat, type-prefixed kebab-case slugs
  config/                 # generated instruction sources (deployed by copy)
  setup/                  # interview answers, decision log, deploy
                          # manifest, minted type definitions, hub version
<!-- BEGIN if:P9-obsidian -->
  .obsidian/              # Obsidian viewer config (core settings versioned)
<!-- END if:P9-obsidian -->
```

`setup/` and `config/` belong to the hub flows (see "Tooling"); your day-to-day
surface is `wiki/`, `index.md`, `log.md`.

## Page types

{{TYPE_TABLE}}
<!-- generator: table with columns Type | Prefix | What it's for — one row per
     type in the composed schema. -->

### Frontmatter (all pages)

```yaml
---
type: <type>
title: <Title>
aliases: []          # alternate names so [[links]] resolve
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: stable       # draft | stable | superseded
sources: []          # provenance: conv:…, file:…, verified:…, [[page]], exp:[[…]]
related: []          # topical neighbors (wiki links)
conflicts: []        # pages this contradicts, if any
---
```

### Required sections and ask-{{USER_NAME}}-for, per type

{{TYPE_SECTIONS}}
<!-- generator: for each composed type: "**<type>:** <required sections
     joined by ·>. *Ask for:* <ask-for checklist, one line>." -->

## Naming & linking

- Slugs are kebab-case and type-prefixed: `project-driftwatch.md`,
  `machine-harbor.md`. Use frontmatter `aliases` so abbreviations resolve.
- Use `[[wikilinks]]` everywhere, not markdown links. Link liberally — a
  `[[name]]` that doesn't resolve yet marks a page worth creating (lint
  catches it). Link an entity/concept on first mention in a page.

## Contradictions & supersession

- A new source contradicts a filed claim: add
  `> [!contradiction] Newer source says X; [[old-page]] says Z.`, list the
  other page under `conflicts:`, append `log.md`. Never silently overwrite.
- A claim is superseded: mark the old block `> [!superseded]`, set
  `status: superseded`, keep the text for history, link the replacement.

## Workflows

### ingest (one source: a paper, a codebase, a document, a conversation)
1. Read the source. 2. Discuss takeaways with {{USER_NAME}} (unless told
"just ingest"). 3. Write/update the appropriate page(s). 4. Update every
page the source touches; fix cross-references both directions. 5. Flag
contradictions. 6. Update `index.md`. 7. Append
`## [YYYY-MM-DD] ingest | <subject>` to `log.md`.

### query
1. Read `index.md` for candidates. 2. Drill pages, follow links.
3. Answer **with inline citations** (`[[page]]` / provenance tags). 4. If the
answer is a reusable analysis, file it as `synthesis-<slug>.md` (ask first if
it's large) and index it.

### capture (always-on)
See standing behaviors. Every capture: edit page(s) → `index.md` →
`## [YYYY-MM-DD] capture | <one line>` in `log.md` → one-line report.

### lint (on demand — never automated)
Run the hub's `tools/wiki_lint.py`, then a semantic pass: open
contradictions; superseded claims still cited; orphans; unresolved links;
missing cross-references; facts without provenance; stale drafts. Fix with
approval; append `## [YYYY-MM-DD] lint | <summary>` to `log.md`. The full
procedure is the hub's `flows/audit.md`.

## index.md

Content catalog grouped by type, one line per page:
`- [[project-driftwatch]] — <hook> · N sources`. Update on every
ingest/capture. Read it first when querying. **Entries are pointers, not
summaries** — one line, ≤ ~165 characters; when an entry wants more, the
detail belongs in the page. (The index loads every session; lint warns on
oversized entries and a bloated total.)

## log.md

Append-only: `## [YYYY-MM-DD] create|ingest|capture|lint|tune | <one line>`.
Parseable with `grep "^## \[" log.md | tail`.
<!-- BEGIN if:P9-obsidian -->

## Obsidian

Graph view colors pages by `type`; wikilinks use shortest-path format;
Dataview (if installed) builds tables from frontmatter. Core settings are
versioned; community plugin binaries are not.
<!-- END if:P9-obsidian -->

## Tooling & sync

<!-- BEGIN if:P5-remote -->
- This wiki is a git repo with a **private remote**, cloned on every machine.
  Pull `--ff-only` before working in it; **every capture/ingest/lint ends
  with commit and push** — an unpushed capture doesn't exist for the other
  machines.
<!-- END if:P5-remote -->
<!-- BEGIN if:P5-local-only -->
- This wiki is a local git repo (no remote yet). **Every capture/ingest/lint
  ends with a commit.** If a remote is added later, the push rule applies:
  see the hub's `modules/github-sync.md`.
<!-- END if:P5-local-only -->
- Setup, tuning, audits, and additions run from the hub clone at
  `{{HUB_PATH}}` — see its README. Generated instruction files deploy from
  `config/` by copy (`tools/deploy.py`); if you edit a source here, redeploy.
- Never a plaintext secret in this wiki: record *where* secrets live, never
  values.
