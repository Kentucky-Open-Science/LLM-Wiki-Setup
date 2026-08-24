# Tools — manual, stdlib-only, cross-platform

Python 3 (no dependencies), same invocation on Windows (`py` or `python`),
macOS, and Linux (`python3`). **Nothing here runs automatically** — no
hooks, no CI, no schedulers; a human or an agent invokes them.

| Tool | Does | Typical caller |
|---|---|---|
| `deploy.py` | copy generated sources from `<wiki>/config/` to their live locations per `setup/manifest.json`; `check` reports drift, `diff` shows it | setup step 7, `/wiki-sync`, audit |
| `wiki_lint.py` | mechanical wiki checks: frontmatter, unresolved links, orphans, index coverage, provenance (`--provenance facts|all|off`), stale drafts, log format | audit step 1 |
| `sync_pair.py` | keep a CLAUDE.md/AGENTS.md pair identical (`--check`, `--from claude|agents`) | setup/audit verification |

The one shipped non-Python artifact is `templates/hooks/pre-commit` (POSIX
sh) — a git hook must run under git's own shell, which Git for Windows
bundles, so sh is the only truly dependency-free choice there. It is
installed per-repo only under policy P2, which the user approves.
