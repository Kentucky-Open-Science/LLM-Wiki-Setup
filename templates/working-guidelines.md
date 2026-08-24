<!-- generator: this becomes <wiki>/config/working-guidelines.md, deployed to
     {{WORK_DIR}}/CLAUDE.md and {{WORK_DIR}}/AGENTS.md. Claude Code and
     free-claude-code auto-load it for any subdirectory of {{WORK_DIR}};
     Codex does not load this layer — for Codex-only users fold it into the
     global file. Resolve activity if-blocks from Wave 2: keep only the
     blocks matching what the user actually does, and adapt the verification
     examples to their stack. -->
# Working guidelines — everything under {{WORK_DIR}}

Behavioral guidelines shared across all projects here. Per-project
instruction files add to these; they don't replace them. **Tradeoff: these
bias toward caution over speed — for trivial tasks, use judgment.**

## 1. Think before acting

**Don't assume. Don't hide confusion. Surface tradeoffs.**

- State assumptions explicitly. Uncertain? Ask (interactive) or proceed
  conservatively and record it (unattended — see the global policy).
- Multiple interpretations → present them; don't pick silently.
- A simpler approach exists → say so. Push back when warranted.
- Something is unclear → stop, name what's confusing, ask.

## 2. Simplicity first

**The minimum work that solves the problem. Nothing speculative.**

- Nothing beyond what was asked; no abstractions for single-use code; no
  unrequested flexibility/configurability.
- If the result is 200 lines and could be 50, redo it. Ask: "would a senior
  colleague call this overcomplicated?"

## 3. Surgical changes

**Touch only what you must. Clean up only your own mess.**

- Don't "improve" adjacent code or text, comments, or formatting; don't
  refactor what isn't broken; match existing style even if you'd differ.
- Notice unrelated dead weight → mention it, don't delete it.
- Your changes orphaned something (imports, variables, references,
  citations) → remove those; leave pre-existing issues alone.
- The test: every changed line traces directly to the request.

## 4. Goal-driven execution

**Define success criteria. Loop until verified.**

Turn tasks into verifiable goals before starting, and state a short
plan (`step → verify` per line) for multi-step work:

<!-- BEGIN if:activity-coding -->
- "Add validation" → "write tests for invalid inputs; make them pass"
- "Fix the bug" → "write a test that reproduces it; make it pass"
- "Refactor X" → "tests pass before and after"
<!-- END if:activity-coding -->
<!-- BEGIN if:activity-writing -->
- "Draft the section" → "outline approved → draft → every claim carries a
  citation that resolves → read-aloud pass"
- "Revise per feedback" → "each comment addressed or explicitly declined,
  tracked to zero"
- Verification for writing: the document builds/renders, references resolve,
  terminology matches the manuscript page's Decisions section.
<!-- END if:activity-writing -->
<!-- BEGIN if:activity-data -->
- "Build the pipeline step" → "run on a sample; row counts and nulls checked
  against expectations; idempotence verified before any backfill"
- Verification for data work: checks are stated *before* running, and
  numbers are read from output, never recalled.
<!-- END if:activity-data -->

Strong criteria let you loop independently; weak ones ("make it work")
guarantee round-trips.

## 5. Sync discipline

<!-- BEGIN if:P5-remote -->
**The remote is the hub. Unpushed work is invisible to every other machine.**
Session start in a repo: `git pull --ff-only`. Stopping points and session
end: commit and push (authorization rules: global policy).
<!-- END if:P5-remote -->
<!-- BEGIN if:P2-data-guard -->
Data, datasets, weights, artifacts, `.env`: never committed. New repos get
the standard `.gitignore` block and the size guard.
<!-- END if:P2-data-guard -->
<!-- BEGIN if:P1-sole-attribution -->
No AI attribution anywhere — commits, PRs, branch names.
<!-- END if:P1-sole-attribution -->
