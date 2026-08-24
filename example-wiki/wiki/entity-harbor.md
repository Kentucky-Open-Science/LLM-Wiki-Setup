---
type: entity
title: harbor
aliases: [harbor-vps]
tags: [entity, infrastructure, workstation]
created: 2026-02-11
updated: 2026-04-02
status: stable
sources: ["verified:2026-02-11", "verified:2026-04-02", "conv:2026-04-02"]
related: ["[[service-driftwatch-api]]", "[[dataset-buoy-2019-2024]]", "[[project-driftwatch]]"]
conflicts: []
---
# harbor

Rowan's rented VPS — personal, nothing shared — hosting driftwatch and the
buoy data. Agent SSH access is key-based and non-interactive
(`ssh -o BatchMode=yes harbor hostname` verified). — verified:2026-02-11

## Role
- The always-on hand: runs [[service-driftwatch-api]], the nightly ingest,
  and the digest cron. Agent sessions run on the laptop and reach harbor
  over SSH; nothing interactive runs here. — conv:2026-04-02

## Hardware
- 2 vCPU, 4 GB RAM, 80 GB disk; Ubuntu 24.04 LTS. — verified:2026-02-11

## Storage
- `/srv/driftwatch` — app checkout. `/data/buoy/` — canonical
  [[dataset-buoy-2019-2024]] (2.1 GB; **not expendable** — the NOAA backfill
  takes a day to rebuild). `/home/rowan/backups/` — nightly tarballs, 14-day
  rotation. — verified:2026-04-02

## Stack
- Python 3.12 via uv; systemd user services; no containers. — verified:2026-04-02

## Connection
- `ssh harbor` (alias in `~/.ssh/config`); dedicated no-passphrase
  `~/.ssh/id_ed25519_harbor`. Key location recorded here, never the key. — verified:2026-02-11

## Guardrails
> [!warning] Live service + canonical dataset live here.
1. `/data/buoy/` and the SQLite alert store are not expendable — no deletes
   or schema changes without explicit approval.
2. Deploys only via [[runbook-driftwatch-deploy]] and outside the digest
   window.
3. Anything else on the box is read-only inspection by default.

## Facts
- **Gotcha:** systemd *user* services die on logout unless lingering is on —
  `driftwatch.service` vanished after the first deploy until
  `loginctl enable-linger rowan` (cost an hour, 2026-04-02). — verified:2026-04-02
- Timezone is UTC; the digest cron and all logs are UTC. — verified:2026-04-02
