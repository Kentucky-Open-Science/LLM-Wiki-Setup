# Tools — manual, stdlib-only, cross-platform

Python 3 (no dependencies), same invocation on Windows (`py` or `python`),
macOS, and Linux (`python3`). **Nothing here runs automatically** — no
hooks, no CI, no schedulers; a human or an agent invokes them.

| Tool | Does | Typical caller |
|---|---|---|
| `deploy.py` | copy generated sources from `<wiki>/config/` to their live locations per `setup/manifest.json`; `check` reports drift, `diff` shows it; a target already symlinked to its source is respected (`ok (linked)`), never copied over | setup step 7, `/wiki-sync`, audit |
| `wiki_lint.py` | mechanical wiki checks: frontmatter, unresolved links, orphans, index coverage, provenance (`--provenance facts|all|off`), stale drafts, log format | audit step 1 |
| `sync_pair.py` | keep a CLAUDE.md/AGENTS.md pair identical (`--check`, `--from claude|agents`) | setup/audit verification |

**Deployment modes:** copy mode (the manifest + `deploy.py`) is the
cross-platform path and the default the flows generate. Symlink-based
deployment — pointing the live locations at the sources, as POSIX install
scripts often do — is fully supported: `deploy.py` and `sync_pair.py`
recognize linked targets and report them in sync. It is POSIX-only in
practice (Windows symlinks require Developer Mode or admin), so on Windows
use copy mode.

The one shipped non-Python artifact is `templates/hooks/pre-commit` (POSIX
sh) — a git hook must run under git's own shell, which Git for Windows
bundles, so sh is the only truly dependency-free choice there. It is
installed per-repo only under policy P2, which the user approves.
