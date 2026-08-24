# Templates — sources for every generated file

Conventions, used consistently across these files:

- `{{PLACEHOLDER}}` — substitute a concrete value from the interview.
- `<!-- BEGIN if:<condition> --> … <!-- END if:<condition> -->` — include the
  block only when the condition holds (a policy from `interview/policies.md`,
  a module, or an interview fact); strip the marker comments from output.
- `<!-- generator: … -->` — an instruction to you, the generating agent.
  Follow it, then remove it. **No `{{…}}`, no marker comments, and no
  generator notes may survive into a generated file.**

Generated sources live in `<wiki>/config/` (global, working guidelines) and
at the wiki root (the wiki schema); per-repo files are written into their own
repos. Deployment is by copy via `tools/deploy.py` and the manifest — see
`flows/setup.md`.

| Template | Generates | Deploys to |
|---|---|---|
| `wiki-schema.md` | `<wiki>/CLAUDE.md` + `AGENTS.md` | in place (the wiki root) |
| `global-instructions.md` | `config/global.md` | `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md` |
| `working-guidelines.md` | `config/working-guidelines.md` | `<work-dir>/CLAUDE.md` + `AGENTS.md` (Claude Code / free-claude-code load the work-dir layer; Codex does not — fold the content into the global file for Codex-only users) |
| `repo-instructions.md` | `<repo>/CLAUDE.md` + `AGENTS.md` | committed in that repo (policy P6) |
| `machine-page.md` | `wiki/machine-<slug>.md` | in place |
| `gitignore-block.txt` | appended to repo `.gitignore`s | per repo (policy P2) |
| `hooks/pre-commit` | `.git/hooks/pre-commit` | per repo (policy P2) |
