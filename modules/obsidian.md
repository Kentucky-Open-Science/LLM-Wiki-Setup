# Module: Obsidian — the human's window into the wiki

Enabled by policy P9 (default ON; declining changes nothing structural —
the wiki is plain markdown + git either way, and `[[wikilinks]]` remain the
link style precisely so any future viewer works).

## Why a viewer at all

The agent reads the wiki as files; the *user* benefits from a graph view
(what links to what), backlinks (what cites this page), and frontmatter
tables. Obsidian does all three locally with no server; any wikilink-aware
editor is an acceptable substitute.

## Setup (what the generator does)

1. The user opens the wiki directory as a vault (Obsidian → Open folder as
   vault). Obsidian creates `.obsidian/`.
2. Enable core plugins: graph, backlinks, outgoing links, tags, search,
   properties, bookmarks.
3. Version the core settings — `app.json`, `core-plugins.json`,
   `graph.json`, `appearance.json`, `community-plugins.json` — and gitignore
   the noise: `workspace.json` (per-machine UI state) and
   `.obsidian/plugins/` (binaries; reinstall via Browse on each machine).
4. Configure graph-view color groups by `type:` so the page types read as
   colors (one group per type in the composed schema).
5. Wikilink setting: "shortest path when possible" — `[[Driftwatch]]`
   resolves regardless of folder, matching how the agent writes links.

## Recommended community plugin

**Dataview** — dynamic tables from frontmatter. The two standing queries
worth bookmarking:

```
TABLE status, updated FROM "wiki" WHERE status = "draft" SORT updated DESC
```
(everything awaiting verification), and per-type inventories
(`WHERE type = "<type>"`).

## Multi-machine note

Each clone gets its own vault state; versioned core settings travel through
git, so the vault looks the same everywhere while window layout stays
per-machine.
