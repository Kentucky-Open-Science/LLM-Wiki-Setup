# service — something that runs and is depended on

- **Tier**: catalog
- **Prefix**: `service-`
- **Purpose**: a deployed, running thing — an API, a web app, a bot, a daemon.
  The page answers: where does it run, how is it deployed, what does it depend
  on, how do I know it's healthy.

## Signals
- deploy configs (`Dockerfile` + compose, `k8s/`, `Procfile`, `fly.toml`,
  `vercel.json`), CI deploy workflows, reverse-proxy configs, systemd units
- conversation: "prod", "the API is down", "deployed on…"

## Required sections
- `## What it does` — one paragraph, with the public endpoint(s)
- `## Runs on` — host (`machine-` link), runtime, how it starts and restarts
- `## Deploy` — how a change ships (link the `runbook-` if one exists)
- `## Dependencies` — datastores, third-party APIs, other services (links)
- `## Health` — how to check it (URLs, commands, dashboards); known failure
  modes
- `## Facts` — provenance-tagged bullets

## Ask the user for
- The host and deploy method (never guess), where env/secrets live (never
  values), what counts as "down".

## Naming
- `service-<name-slug>.md`, e.g. `service-driftwatch-api.md`.

## Typical relations
- Built by a `project-`; runs on `machine-`; operated via `runbook-`;
  failures become `incident-` pages.
