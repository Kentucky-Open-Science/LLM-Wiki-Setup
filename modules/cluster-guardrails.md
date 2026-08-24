# Module: shared-cluster & sensitive-data guardrails

Enable when any machine is **shared** (other people's data and jobs; charged
allocations) or holds **sensitive data** (PHI/PII, clinical, proprietary).
This module exists because a shared cluster is where a confident agent does
the most damage. The guardrails land in two places: the machine's `machine-`
page (the agent re-reads them every time it touches the machine) and the
global policy's device table (one-line reminders).

## The core stance: read-before-write, always

On shared infra the default is **read-only inspection** (`ls`, `cat`,
`stat`, `squeue`, `df`). Writes, deletes, and job submissions require the
user's explicit approval until the machine page records standing
authorizations. Baseline rules for any shared machine's Guardrails section:

1. Shared data pools are immutable — treat them as read-only.
2. No writes, deletes, or job submissions without explicit approval;
   default to inspection commands.
3. Charge only the user's own account/allocation — never another group's.
   Record the exact account string on the machine page.
4. Never touch other users' files, jobs, or environments.
5. Login nodes are not for compute — submit through the scheduler.
6. Verify before assuming: `ls`/`stat` paths before referencing them; check
   job states before acting on them.

## Sensitive data (PHI/PII) — additional rules

7. Sensitive data never leaves the box: no copying images, records, or raw
   text off; no pasting record contents into anything that leaves the
   machine. De-identified extracts and aggregate numbers only, and only per
   the machine page's stated egress policy.
8. The box is not a live mount of local projects — deploy code *to* it
   explicitly (scp/rsync); bring back only what rule 7 allows.

## The gotcha catalog — capture yours the moment they cost you

The Facts section of a cluster page is its operating manual. Classes of
gotcha worth capturing immediately (each cost someone a real debugging
session once):

- **Login-shell PATH**: when the scheduler is loaded by an environment
  module, plain non-interactive `ssh cluster 'sbatch …'` fails
  ("command not found") — run scheduler commands via a login shell:
  `ssh cluster 'bash -lc "sbatch …"'`.
- **Container mount paths**: with a mount like `/project:/app/project`,
  paths read *inside* the container use `/app/project/...` while host-side
  wrapper commands use `/project/...`; mixing them fails only at runtime.
  Also record who owns container-written files (root-owned files a plain
  `rm` can't delete; fix by running rm inside a root container).
- **Per-node storage is not uniform**: scratch disks differ per node in
  size and persistence; the big NVMe may be root-only. Record per-node
  numbers so jobs request nodes that fit.
- **Shared-filesystem contention**: a reader/prefetcher co-located with a
  many-worker job on the same node can starve that node's NFS client —
  separate them or pre-stage to local scratch.
- **Launch-channel hangs**: `nohup … &` over an SSH channel can hang on
  channel close even though the process started — don't wait on the launch
  call; poll progress in a fresh connection.

## Scheduler submission (SLURM archetype)

Keep **one canonical submission script in the repo** and point the machine
page at it — the agent reads the template instead of being re-taught the
scheduler. Skeleton:

```bash
#!/bin/bash
#SBATCH --job-name=<name>
#SBATCH --account=<your-account>     # NEVER another group's allocation
#SBATCH --partition=<partition>
#SBATCH --time=12:00:00
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --output=<project-logs>/%x-%j.out
set -euo pipefail
# container clusters: the image reference IS the pull on compute nodes
srun --container-image=<image> --container-mounts=/project:/app/project \
     bash -lc 'cd /app/project/<repo> && <command>'
# host-side sentinel: host paths here, container paths above
touch <project>/runs/${SLURM_JOB_ID}.DONE
```

## Secure box over password auth (no key allowed)

POSIX pattern — the password lives in a local `chmod 600` file and never
enters the model context or the remote:

```bash
sshpass -f ~/secrets/<box>.pw ssh -o PreferredAuthentications=password \
  -o PubkeyAuthentication=no <user>@<host> '<command>'
```

Windows has no sshpass: run this pattern inside WSL, or press for a key
exception. Record on the machine page *where* the password file lives —
never the value; the wiki is git-tracked.

## Interview questions this module adds (Wave 5)

- Which machines are shared, and what is at stake there (whose data, whose
  money, whose jobs)?
- The exact account/allocation string; partitions and their limits.
- Any sensitive data? What is the stated egress policy?
- Which standing authorizations, if any, does the user grant on day one
  (e.g. "submitting to partition X under account Y is fine without
  asking")? Everything else defaults to ask-first.
