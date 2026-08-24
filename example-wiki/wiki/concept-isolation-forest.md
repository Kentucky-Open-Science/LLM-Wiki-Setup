---
type: concept
title: Isolation forest
aliases: [isolation forests, iforest]
tags: [concept, ml]
created: 2026-02-11
updated: 2026-03-14
status: stable
sources: ["file:https://doi.org/10.1109/ICDM.2008.17", "exp:[[experiment-anomaly-baseline-2026-03]]"]
related: ["[[project-driftwatch]]"]
conflicts: []
---
# Isolation forest

## Definition
- Anomaly detection by random recursive partitioning: anomalies are isolated
  in fewer splits, so short average path length ⇒ high anomaly score. — file:https://doi.org/10.1109/ICDM.2008.17

## How it's used here
- [[project-driftwatch]] scoring: 200 trees, contamination 0.02, features =
  hourly deltas + 24 h rolling stats; retrained monthly. — exp:[[experiment-anomaly-baseline-2026-03]]
- Chosen over the z-score baseline on holdout evidence. — exp:[[experiment-anomaly-baseline-2026-03]]

## Sources
- Liu, Ting, Zhou (2008), ICDM. — file:https://doi.org/10.1109/ICDM.2008.17
