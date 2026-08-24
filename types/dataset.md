# dataset — data with a location and a shape

- **Tier**: catalog
- **Prefix**: `dataset-`
- **Purpose**: one dataset/corpus/data pool. The page answers the questions
  that otherwise get re-asked forever: where exactly is it, what format, how
  big, who owns it, what preprocessing produced it, what may I do with it.

## Signals
- `data/`, `datasets/` directories; data formats in `.gitignore`s (parquet,
  hdf5, zarr, npz, csv archives, imaging formats)
- download/ETL scripts, DVC/`lakeFS` traces, dataloader code
- conversation: "the training set", "the corpus", "the survey responses"

## Required sections
- `## Specs` — modality/kind, format, size, counts (rows/files/subjects),
  resolution/granularity, versions
- `## Location & Access` — absolute path(s) per machine, owner, access
  method, license/usage constraints
- `## Preprocessing` — what produced this from what, and where that code is
- `## Used by` — links to projects/experiments/pipelines consuming it
- `## Facts` — provenance-tagged bullets

## Ask the user for
- Absolute paths (never guess), owner, license, sensitive-data status
  (PII/PHI ⇒ the machine guardrails apply), which version is canonical.

## Naming
- `dataset-<name-slug>.md`, e.g. `dataset-buoy-2019-2024.md`.

## Typical relations
- Consumed by `experiment-`/`pipeline-`/`model-` pages; lives on `entity-`
  machines; produced by `project-` code.
