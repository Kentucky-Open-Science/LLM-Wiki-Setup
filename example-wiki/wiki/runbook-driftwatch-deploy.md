---
type: runbook
title: Driftwatch deploy
aliases: [driftwatch deploy]
tags: [runbook, ops]
created: 2026-04-02
updated: 2026-04-02
status: stable
sources: ["verified:2026-04-02"]
related: ["[[service-driftwatch-api]]", "[[machine-harbor]]"]
conflicts: []
---
# Driftwatch deploy

## When to run
- A tagged release exists on the private remote and tests passed locally. — verified:2026-04-02

## Steps
1. `ssh harbor` ([[machine-harbor]]).
2. `cd /srv/driftwatch && git fetch --tags && git checkout <tag>`
3. `.venv/bin/pip install -e . --quiet`
4. `systemctl --user restart driftwatch.service`
5. **Verify:** `curl -fsS http://localhost:8100/health` returns
   `{"ok": true}` with the new `version` field. — verified:2026-04-02

## Rollback
- `git checkout <previous-tag>` then repeat steps 3–5. — verified:2026-04-02

## Facts
- Restart drops in-flight requests; the co-op digest cron is 07:00 UTC —
  deploy outside 06:45–07:15 UTC. — verified:2026-04-02
