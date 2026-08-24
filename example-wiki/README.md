# Example wiki — a synthetic reference

**Everything here is fictional.** "Rowan Ellis" is an invented user who spans
three activities at once — writing a book, running a tiny data service, and
doing light ML experiments — chosen to show a *composed* schema rather than a
domain preset. Read it to calibrate what good pages look like; never copy it
into a real wiki.

What to notice:

- **Composition**: core types (`project`, `entity`, `concept`, `synthesis`) +
  catalog picks (`dataset`, `experiment`, `manuscript`, `venue`, `service`,
  `runbook`, `decision`) + one **minted** type (`interview-` — created with
  `types/_template.md` because interview pages need sections no catalog type
  has: consent status, quote-approval state).
- **Provenance tags** ending factual bullets: `— conv:DATE`, `— file:…`,
  `— verified:DATE`, `— exp:[[…]]`.
- **A machine page with guardrails** (`entity-harbor`) — the operating-manual
  pattern, including a gotcha filed the day it cost an hour.
- **Draft discipline**: `venue-orchard-press` is `status: draft` with a
  `> [!needs-verification]` callout — uncertainty marked, not guessed away.
- **A decision page** that ended a recurring debate, citing the experiment
  that settled it.
- `index.md` as the catalog and `log.md` as append-only history.

Smoke test: `python3 ../tools/wiki_lint.py .` — exactly one expected
finding: the `stale-draft` warning on [[venue-orchard-press]], which has
waited past 30 days. That is the mechanism working — an audit would now
re-ask Rowan about the deadline and resolve the draft.
