---
type: service
title: Driftwatch API
aliases: [driftwatch api]
tags: [service, api]
created: 2026-04-02
updated: 2026-04-02
status: stable
sources: ["verified:2026-04-02", "conv:2026-04-02"]
related: ["[[project-driftwatch]]", "[[machine-harbor]]", "[[runbook-driftwatch-deploy]]"]
conflicts: []
---
# Driftwatch API

## What it does
- FastAPI app serving `/alerts` (recent anomalies) and `/health` to co-op
  members; nightly ingest task appends to the parquet store and rescores. — verified:2026-04-02

## Runs on
- [[machine-harbor]], `/srv/driftwatch`, systemd **user** service
  `driftwatch.service` (see the lingering gotcha on the machine page). — verified:2026-04-02

## Deploy
- [[runbook-driftwatch-deploy]] — git pull + restart; rollback = checkout previous tag.

## Dependencies
- SQLite alert store (per [[decision-sqlite-over-postgres]]); NOAA endpoint
  for ingest; no other services. — verified:2026-04-02

## Health
- `curl -fsS http://harbor:8100/health` → `{"ok": true}`; ingest freshness
  visible as `last_ingest` in the same payload. — verified:2026-04-02
- Known failure mode: NOAA endpoint stalls → ingest task times out at 120 s
  and retries at 06:30 UTC. — conv:2026-04-02

## Facts
- Port 8100, LAN + tailnet only — nothing public. — verified:2026-04-02
