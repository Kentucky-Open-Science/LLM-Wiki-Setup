# pipeline — data moving on a schedule

- **Tier**: catalog
- **Prefix**: `pipeline-`
- **Purpose**: a recurring data flow — ETL/ELT job, dbt project, training
  data refresh, scraper, report generator. The page answers: what moves from
  where to where, when, transformed how, and what happens when it fails.

## Signals
- `dags/` (Airflow), Prefect/Dagster projects, `dbt_project.yml`, cron
  entries, scheduled CI workflows that move data
- conversation: "the nightly job", "the refresh", "upstream broke"

## Required sections
- `## Flow` — sources → transforms → sinks, with links (`dataset-`,
  `api-`, `service-`)
- `## Schedule & trigger` — when it runs and what starts it
- `## Failure` — how failures surface, what to check first, rerun/backfill
  procedure (or link its `runbook-`)
- `## Facts` — provenance-tagged bullets (volumes, durations, quirks)

## Ask the user for
- The orchestrator and where its UI/logs live, backfill safety (idempotent
  or not — never assume), data-contract owners upstream.

## Naming
- `pipeline-<slug>.md`, e.g. `pipeline-buoy-nightly-ingest.md`.

## Typical relations
- Reads `api-`/`dataset-`/`service-`; writes `dataset-`; runs on `entity-`;
  breakage becomes `incident-`.
