# Flow: audit — health check of wiki and config

Run on request ("audit my wiki", "lint", "health check") — never on a
schedule, never from a hook. Audit **reports and proposes; it fixes only
with approval.**

## 1. Mechanical pass

- `python3 <hub>/tools/wiki_lint.py <wiki-path>` — frontmatter validity,
  unresolved wikilinks, orphans, index coverage, provenance gaps (honor
  the strictness recorded in `setup/answers.md`: audit lints against the
  *chosen* rules, not the defaults), stale drafts, log format.
- `python3 <hub>/tools/deploy.py --wiki <wiki> check` — source↔deployed
  drift.
- `python3 <hub>/tools/sync_pair.py --check <wiki>` plus each deployed
  CLAUDE/AGENTS location — pair identity.

## 2. Semantic pass (yours — the script can't see these)

- Open contradictions: `conflicts:` entries unresolved; contradiction
  callouts that newer evidence could settle.
- Superseded claims still cited as current elsewhere.
- Syntheses older than their sources (compare `updated:` dates of a
  synthesis vs the pages it cites).
- Missing cross-references: pages that plainly should link but don't.
- Schema strain: types with zero pages (retire? — a tune offer), pages
  sprouting the same ad-hoc section repeatedly (split? — a mint offer),
  many unresolved `[[links]]` clustering around a missing concept (create
  it).
- Machine pages: `updated:` far in the past on infrastructure known to
  change; guardrails that no longer match how the user talks about the
  machine.
- Stale drafts: `status: draft` pages that have waited long enough to
  re-ask the user about.

**A lint signature is grounds to look, never grounds to delete.** Before
proposing removal, re-typing, or archival of any page — including one that
trips several checks at once (no frontmatter + orphan + unindexed is also
the signature of a substantive file that predates the schema) — open it
and read it. The proposal must cite what the page actually contains.

## 3. Report

One table: `Finding | Where | Severity | Proposed fix`. Group: mechanical /
semantic / drift. Note what a web search or one question to the user would
resolve. No fix is applied yet.

## 4. Fix (approved items only)

Apply approved fixes; a re-ask of the user resolves what needs them.
Update `index.md`, append `## [DATE] lint | <summary>` to `log.md`, commit;
push if remote. Deferred findings are listed in the wrap-up so the next
audit starts warm.
