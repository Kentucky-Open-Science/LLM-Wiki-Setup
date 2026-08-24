---
type: experiment
title: Anomaly baseline (2026-03)
aliases: [anomaly baseline]
tags: [experiment, ml]
created: 2026-03-14
updated: 2026-03-14
status: stable
sources: ["file:~/work/driftwatch/experiments/2026-03-baseline/results.json"]
related: ["[[dataset-buoy-2019-2024]]", "[[concept-isolation-forest]]", "[[decision-sqlite-over-postgres]]"]
conflicts: []
---
# Anomaly baseline (2026-03)

## Claim
- [[concept-isolation-forest]] beats the rolling z-score baseline on 2023
  holdout anomalies, enough to justify the sklearn dependency. — exp:[[experiment-anomaly-baseline-2026-03]]

## Setup
- Train 2019–2022, holdout 2023 from [[dataset-buoy-2019-2024]]; labels =
  Priya's storm-log incident weeks. `python experiments/2026-03-baseline/run.py
  --contamination 0.02`; ran on [[machine-harbor]] (CPU, ~9 min). — file:~/work/driftwatch/experiments/2026-03-baseline/results.json

## Results

| method | P@50 | R@50 |
|---|---|---|
| rolling z-score (24 h) | 0.41 | 0.33 |
| isolation forest | **0.62** | **0.49** |

## Interpretation
- The forest's wins concentrate in multi-variable anomalies (temp+tide);
  single-spike events are caught by both. — file:~/work/driftwatch/experiments/2026-03-baseline/results.json

## Source
- `~/work/driftwatch/experiments/2026-03-baseline/` (config, results.json, plots). — verified:2026-03-14
