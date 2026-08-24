# The page-type catalog

A wiki's schema is **composed per user, not picked from a menu of domains**.
Nobody *is* "an ML researcher" or "a writer" — people have a mix of
activities, and the mix shifts. The mechanism:

1. **Core five, always included:** `project`, `entity`, `concept`,
   `reference`, `synthesis`. Every wiki gets them; they cover any kind of work.
2. **Catalog types, selected by evidence.** Every other file in this directory
   is one self-contained type definition carrying its own **Signals** section —
   the scan/conversation evidence that suggests it. Selection logic is
   distributed: the scan collects evidence, then you walk the catalog and
   match. Adding a type to the catalog automatically extends detection.
3. **Minted types, when the catalog falls short.** `_template.md` is the
   meta-schema: author a new type in the same shape (a novelist's
   `character-`, a PI's `grant-`, an educator's `course-`). Mint only when
   pages would need **different required sections or a different
   ask-the-user-for checklist** — never for a tag's worth of difference.
   Minted definitions are saved to `<wiki>/setup/custom-types/` and inlined
   into the generated wiki schema like any catalog type.

## Proposing (setup Wave 4 / tune)

Propose **lean**: strongly-evidenced types with one line of evidence each;
weakly-evidenced ones compressed into a single "I also saw hints of X — want
any?" line; then ask what the catalog misses. The user edits the list. The
result — core + selections + mints — is what `templates/wiki-schema.md`
generates from: its type table and required-sections blocks are assembled from
these files.

## The schema is living

`tune` re-proposes the composition when the user's work shifts (started a
thesis → offer `manuscript` + `venue`). `audit` flags types with zero pages
(retire?) and types whose pages keep sprouting ad-hoc sections (split?).
Retiring a type never deletes pages — they are re-typed or left with a note.

## File format

Every definition, core or catalog or minted, has: **Tier · Prefix · Purpose ·
Signals · Required sections · Ask the user for · Naming · Typical relations.**
Required sections are a floor, not a ceiling; "ask the user for" is the
checklist that makes pages complete instead of vague.
