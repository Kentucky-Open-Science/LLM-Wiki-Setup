# paper — a source you digested

- **Tier**: catalog
- **Prefix**: `paper-`
- **Purpose**: a summary of someone else's published work — findings only, no
  opinions — linked to the user's work it informs. (The user's *own* writing
  in progress is `manuscript-`, not `paper-`.)

## Signals
- `references.bib`, citation managers (Zotero/Mendeley), `papers/` folders
  of PDFs, arXiv links in notes
- conversation: "that NeurIPS paper", "the study that found…"

## Required sections
- `## Citation` — full, with the canonical URL (arXiv HTML build preferred
  when it exists; else abstract page/DOI)
- `## TL;DR` — three sentences max
- `## Findings` — bulleted, each with provenance (section/table of the paper)
- `## Relevance` — links: what of the user's work this bears on, and how
- `## File` — canonical URL, or local/vault path for unpublished sources

## Ask the user for
- Why it matters to them (the Relevance section is theirs, not the
  abstract's), and whether it contradicts anything already filed.

## Naming
- `paper-arxiv-<id>.md` when an arXiv id exists; else
  `paper-<firstauthor>-<year>-<keyword>.md`.

## Typical relations
- Feeds `concept-` definitions and `synthesis-` answers; contradictions with
  other pages get `> [!contradiction]` callouts, never silent overwrites.
