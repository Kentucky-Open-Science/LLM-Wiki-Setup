# schema — the shape of data that others depend on

- **Tier**: catalog
- **Prefix**: `schema-`
- **Purpose**: a data contract — a database schema, a table, an event/message
  format, a file layout — whose shape other things depend on. The page
  answers: what are the fields *really*, what consumes this, and what is the
  migration story.

## Signals
- migrations dirs, `schema.sql`/`models/` (dbt), protobuf/Avro/JSONSchema
  files, ORM model files
- conversation: "the events table", "don't rename that column"

## Required sections
- `## Shape` — fields/columns with types and *meaning* (the part the DDL
  doesn't say); which are load-bearing
- `## Producers & consumers` — links; who writes it, who breaks if it
  changes
- `## Evolution` — migration mechanism, versioning, compatibility rules
- `## Facts` — provenance-tagged bullets (cardinalities, known dirty data)

## Ask the user for
- Field *semantics* (units, nullability-in-practice, sentinel values), and
  which consumers are not visible in code.

## Naming
- `schema-<slug>.md`, e.g. `schema-readings-table.md`.

## Typical relations
- Realized in a `dataset-`/`service-` datastore; changed via `decision-`;
  moved by `pipeline-`.
