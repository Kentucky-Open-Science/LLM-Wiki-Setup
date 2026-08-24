---
type: project
title: Driftwatch
aliases: [driftwatch]
tags: [project, service, data]
created: 2026-02-11
updated: 2026-04-02
status: stable
sources: ["file:~/work/driftwatch/README.md", "conv:2026-02-11", "conv:2026-04-02"]
related: ["[[service-driftwatch-api]]", "[[dataset-buoy-2019-2024]]", "[[machine-harbor]]"]
conflicts: []
---
# Driftwatch

Tide-anomaly alerting for the harbor co-op: ingest buoy readings nightly,
score anomalies, serve alerts to co-op members. — conv:2026-02-11

## Purpose
- Give [[entity-priya-nair|Priya]]'s co-op early warning of anomalous tide/
  temperature readings so moorings get checked before storms do it for them. — conv:2026-02-11

## Structure
- `ingest/` — nightly NOAA pull + parquet append — file:~/work/driftwatch/README.md
- `scoring/` — [[concept-isolation-forest]] scorer, retrained monthly — file:~/work/driftwatch/README.md
- `api/` — FastAPI app, see [[service-driftwatch-api]] — file:~/work/driftwatch/README.md

## Location
- Local: `~/work/driftwatch` (solo repo, private remote). — verified:2026-02-11
- Deployed on [[machine-harbor]] at `/srv/driftwatch`. — verified:2026-04-02

## Stack
- Python 3.12, FastAPI, scikit-learn, SQLite (per [[decision-sqlite-over-postgres]]), parquet via pyarrow. — file:~/work/driftwatch/pyproject.toml

## Relationships
- Consumes [[dataset-buoy-2019-2024]] for training; live feed owned by [[entity-priya-nair]].
- Scoring approach validated by [[experiment-anomaly-baseline-2026-03]].

## Facts
- Weekly digest email goes out Mondays 07:00 UTC via cron on [[machine-harbor]]. — verified:2026-04-02
