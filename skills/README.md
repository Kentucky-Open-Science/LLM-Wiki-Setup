# Skills — ready-made commands (opt-in, policy P7)

Five thin commands, each a pointer to a canonical procedure — the hub flows
or the wiki's own workflows — so hub updates improve them without
reinstallation. Installed by setup (or by hand) with the two placeholders
substituted; nothing here runs automatically.

| Command | Points at | Use |
|---|---|---|
| `/wiki-audit`  | `flows/audit.md` | health check, on demand |
| `/wiki-tune`   | `flows/tune.md` | refine the setup |
| `/wiki-add`    | `flows/add.md` | new machine / repo / collaborator |
| `/wiki-ingest` | wiki schema § ingest | file a paper/codebase/document |
| `/wiki-sync`   | wiki schema § tooling + `deploy.py` | pull/commit/push wiki; redeploy configs |

## Install

Substitute `{{HUB_PATH}}` and `{{WIKI_PATH}}` (absolute paths), then copy:

- **Claude Code / free-claude-code**: `claude-code/*.md` →
  `~/.claude/commands/` (invoke as `/wiki-audit` etc.; the argument hint
  works as `$ARGUMENTS`).
- **Codex**: `codex/*.md` → `~/.codex/prompts/` (invoked as custom
  prompts by name).

Both harnesses read the files at invocation time — reinstall only when the
placeholders must change (wiki moved, hub re-cloned).
