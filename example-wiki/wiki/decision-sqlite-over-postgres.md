---
type: decision
title: SQLite over Postgres for driftwatch
aliases: [sqlite decision]
tags: [decision]
created: 2026-03-20
updated: 2026-03-20
status: stable
sources: ["conv:2026-03-20", "exp:[[experiment-anomaly-baseline-2026-03]]"]
related: ["[[project-driftwatch]]", "[[service-driftwatch-api]]"]
conflicts: []
---
# SQLite over Postgres for driftwatch

## Decision
- Driftwatch's alert store is SQLite, not Postgres. Decided 2026-03-20. — conv:2026-03-20

## Context
- Third recurrence of the "shouldn't this be Postgres?" debate; write volume
  is one nightly batch + a handful of reads/min. — conv:2026-03-20

## Alternatives
- Postgres: rejected — an extra service to run and back up on
  [[machine-harbor]] for zero current benefit. — conv:2026-03-20
- Parquet-only (no DB): rejected — alert acknowledgment needs row updates. — conv:2026-03-20

## Consequences
- Backup = one file in the nightly tarball; accepted ceiling: revisit if the
  API exceeds ~50 req/min sustained ([[service-driftwatch-api]] metrics). — conv:2026-03-20

## Status
- Decided 2026-03-20; scoring-load context in
  [[experiment-anomaly-baseline-2026-03]].
