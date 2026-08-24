<!-- generator: becomes <repo>/CLAUDE.md + <repo>/AGENTS.md (identical) for
     repos the user opted in (policy P6). Keep it SHORT — only what the
     agent needs every time it opens this repo; depth lives in the wiki page.
     If it grows past a screen, move detail to the wiki and link it. -->
# {{REPO_NAME}}

> Keep CLAUDE.md and AGENTS.md identical.

{{ONE_LINE_PURPOSE}} Wiki page: `[[project-{{REPO_SLUG}}]]` in
{{WIKI_NAME}} ({{WIKI_PATH}}) — consult it for structure, relationships,
and history before asking.

## Environment
<!-- generator: only what's true and needed: how to set up/enter the env,
     the run entry points, where it deploys or mounts remotely (link the
     machine's entity- page), which machine work should run on. -->
- {{ENV_FACTS}}

## Verify
<!-- generator: the repo's real check commands — tests, build, lint, render.
     One line each, exact commands. -->
- {{VERIFY_COMMANDS}}

## Working rules
<!-- generator: repo-specific rules only (the working-guidelines layer
     already covers general behavior — do not repeat it). Examples: which
     dirs are generated/vendored (don't hand-edit), collaborative status
     ("history has other authors — every push needs approval" per P4),
     remote-machine cautions with entity- page links. -->
- {{REPO_RULES}}
