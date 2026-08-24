<!-- generator: becomes wiki/machine-<slug>.md (type definition:
     types/machine.md) — used by setup Wave 5
     and flows/add.md. The Guardrails section and the gotcha-Facts are the
     point; hardware is context. Fill only what is verified (run the
     commands, or tag conv:) — never invent specs. For shared clusters and
     sensitive-data boxes, pull the relevant guardrail text from
     modules/cluster-guardrails.md. -->
---
type: machine
title: {{MACHINE_NAME}}
aliases: [{{ALIASES}}]
tags: [machine, infrastructure, {{KIND}}]   # kind: laptop | workstation | gpu-node | cluster | secure-box
created: {{DATE}}
updated: {{DATE}}
status: stable
sources: ["conv:{{DATE}}", "verified:{{DATE}}"]
related: []
conflicts: []
---
# {{MACHINE_NAME}}

<!-- generator: one paragraph — what this machine is, who owns it (personal
     vs shared), what it's for, and how agent access works (key/password,
     verified date). -->

## Role
- Division of labor vs the other machines: what runs here, what doesn't.
- Where agent sessions run for this machine (locally on it / from another
  machine over SSH), which harness, and whether sessions are remotely
  steerable (Claude Code/Codex: yes; free-claude-code: no — use tmux/screen
  + SSH).

## Hardware
- CPU / RAM / GPUs / OS / relevant drivers — each bullet `— verified:DATE`.

## Storage
- Disk layout: what is writable, what is scarce, what is **not expendable**,
  mount paths. Note per-path quirks (quotas, per-node differences,
  slow filesystems).

## Stack
- Runtimes, container tooling, scheduler (if any), pre-pulled images.

## Connection
- How to reach it (`ssh {{ALIAS}}`, or "this is the local machine").
  Non-interactive auth verified with `ssh -o BatchMode=yes {{ALIAS}} hostname`.
- Where its credentials live (keychain / key file / password file) — never
  the values. The wiki is git-tracked: no plaintext secrets, ever.
- Reachability quirks (VPN required, often asleep — "unreachable is normal,
  never an error" for laptops).

## Guardrails
<!-- generator: for personal machines this can be short (what is not
     expendable; read-before-write on the owner's data). For shared clusters
     / secure boxes, include the applicable numbered rules from
     modules/cluster-guardrails.md — account discipline, read-only defaults,
     approval-required actions, data-egress rules. -->
> [!warning] {{WHAT_IS_AT_STAKE}}
1. …

<!-- BEGIN if:cluster -->
## Submission / run environment
- Scheduler, partitions/queues + time limits, the account/allocation to
  charge (and never any other), the canonical submission script's path in
  the repo, container invocation conventions.
<!-- END if:cluster -->

## Facts
- Every concrete verified detail and **every gotcha ever hit here**, as its
  own provenance-tagged bullet. This section is why the page exists: a
  quirk filed once never costs a debugging session again.
