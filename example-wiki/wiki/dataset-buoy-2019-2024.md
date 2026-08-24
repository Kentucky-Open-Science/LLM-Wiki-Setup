---
type: dataset
title: Buoy readings 2019–2024
aliases: [buoy dataset, buoy-2019-2024]
tags: [dataset]
created: 2026-02-11
updated: 2026-03-14
status: stable
sources: ["file:https://www.ndbc.noaa.gov/", "verified:2026-03-14"]
related: ["[[project-driftwatch]]", "[[experiment-anomaly-baseline-2026-03]]"]
conflicts: []
---
# Buoy readings 2019–2024

## Specs
- Hourly readings, 3 stations, 2019-01-01 → 2024-12-31; water temp, tide
  height, wind; 2.1 GB parquet, 1 file per station-year. — verified:2026-03-14

## Location & Access
- [[machine-harbor]]: `/data/buoy/` (canonical). — verified:2026-03-14
- Public NOAA NDBC source; no license constraints. — file:https://www.ndbc.noaa.gov/
- Not in any git repo (data policy); refreshed by the ingest task.

## Preprocessing
- Raw NDBC text → parquet via `ingest/backfill.py` in
  [[project-driftwatch]]; gaps forward-filled max 3 h, longer gaps left NaN. — verified:2026-03-14

## Used by
- [[experiment-anomaly-baseline-2026-03]] (train 2019–2022, holdout 2023).
- Nightly scoring in [[service-driftwatch-api]].

## Facts
- Station 3 has a 6-week gap (sensor failure, 2021-09 → 2021-10). — verified:2026-03-14
