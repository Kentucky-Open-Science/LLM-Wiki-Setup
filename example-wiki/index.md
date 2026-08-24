# Rowan's Wiki — Index

Content catalog, grouped by type. One line per page. **Read this first when
querying.** (13 pages; history in `log.md`.)

## Projects
- [[project-driftwatch]] — tide-anomaly alerting for the harbor co-op; sensor ingest + API + weekly digest · 3 sources
- [[project-fieldnotes]] — the Fieldnotes book effort: research, interviews, drafts, submission · 2 sources

## Manuscripts
- [[manuscript-fieldnotes-book]] — book draft v3; ch. 1–4 drafted, ch. 5 outlined; target [[venue-orchard-press]] · 2 sources

## Venues
- [[venue-orchard-press]] — target publisher for Fieldnotes; proposal rules; deadline unconfirmed (draft) · 1 source

## Interviews
- [[interview-mara-okafor]] — harbor-master interview 2026-03-02; consent signed; 2 quotes pending approval · 1 source

## Services
- [[service-driftwatch-api]] — FastAPI on [[entity-harbor]]; nightly ingest + /alerts endpoint · 2 sources

## Runbooks
- [[runbook-driftwatch-deploy]] — deploy via git pull + systemd restart on [[entity-harbor]]; verified rollback · 1 source

## Datasets
- [[dataset-buoy-2019-2024]] — NOAA buoy readings 2019–2024, 2.1 GB parquet on [[entity-harbor]] · 2 sources

## Experiments
- [[experiment-anomaly-baseline-2026-03]] — isolation forest beats z-score baseline (P@50 0.62 vs 0.41) on 2023 holdout · 1 source

## Decisions
- [[decision-sqlite-over-postgres]] — SQLite for driftwatch; revisit at 50 req/min; settled 2026-03-20 · 2 sources

## Concepts
- [[concept-isolation-forest]] — anomaly detection method used in driftwatch scoring · 2 sources

## Entities
- [[entity-harbor]] — Rowan's VPS (2 vCPU/4 GB, Ubuntu 24.04); runs driftwatch; guardrails: live DB not expendable · 4 sources
- [[entity-priya-nair]] — collaborator; harbor co-op data lead; owns the sensor feed · 2 sources

## Syntheses
(none yet)
