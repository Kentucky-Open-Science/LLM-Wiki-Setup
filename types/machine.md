# machine — a machine work runs on

- **Tier**: catalog
- **Prefix**: `machine-`
- **Purpose**: one machine — laptop, workstation, GPU node, shared cluster,
  secure box. The page is its **operating manual**: role, storage,
  connection, guardrails the agent obeys, and every gotcha ever paid for.
  (People and organizations are `entity` pages; machines earn their own type
  because their required sections — Storage, Connection, Guardrails — are a
  different shape entirely.)

## Signals
- `~/.ssh/config` host aliases; more than one machine in the scan or
  conversation; scheduler/cluster traces (`#SBATCH`, job scripts); GPU
  evidence; agent sessions hosted anywhere but the local machine
- conversation: "the cluster", "my GPU box", "deploy to the server"
- Near-automatic with `modules/machines.md`; a single-laptop setup may still
  give the laptop a page, but rarely needs the type on day one

## Required sections
- `## Role` — division of labor vs other machines; where agent sessions run
  and whether they are remotely steerable
- `## Hardware` — CPU/RAM/GPUs/OS, each bullet verified
- `## Storage` — what is writable, what is scarce, what is **not expendable**
- `## Stack` — runtimes, containers, scheduler
- `## Connection` — how to reach it; where credentials live (never values)
- `## Guardrails` — what must never happen here; for shared/sensitive
  machines, the numbered rules from `modules/cluster-guardrails.md`
- `## Submission / run environment` — schedulers only: partitions, account
  string, canonical submission script
- `## Facts` — every verified detail and every gotcha, provenance-tagged

## Ask the user for
- Ownership (personal vs shared) and what is at stake; what is not
  expendable; the exact account/allocation string on clusters; where
  secrets for it live; sensitive-data status and egress rules.

## Naming
- `machine-<name-slug>.md`, e.g. `machine-harbor.md`. Aliases for hostnames
  and IPs so all forms resolve.

## Typical relations
- Runs `project-`/`service-`/`pipeline-` work; sibling machines link each
  other (division of labor); `incident-` and `runbook-` pages anchor here;
  owned/administered by `entity-` people or orgs.
