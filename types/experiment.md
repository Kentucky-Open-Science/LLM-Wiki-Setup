# experiment — a run that proves a claim

- **Tier**: catalog
- **Prefix**: `experiment-`
- **Purpose**: one experimental run/result that establishes something —
  metrics, config, where it ran, what it shows. This is how "what did we get
  on X?" becomes a wiki read instead of a memory. Applies beyond ML: an A/B
  test, a benchmark, a load test.

## Signals
- `wandb/`, `mlruns/`, `runs/`, `outputs/` dirs; tracking-tool configs;
  sbatch/job scripts; results notebooks/CSVs
- conversation: "the run hit 0.83", "the ablation showed…", "we benchmarked"

## Required sections
- `## Claim` — the one thing this run proves (write it first)
- `## Setup` — model/system, dataset, config, exact command, where it ran,
  job id
- `## Results` — the table; exact numbers, no rounding-by-memory
- `## Interpretation` — factual only; speculation stays out or goes to a
  `draft` note
- `## Source` — logs/artifacts location; tracking-tool URL

## Ask the user for
- The run command and config file, exact metrics, cluster/job id — never
  reconstruct these from memory.

## Naming
- `experiment-<slug>.md`, e.g. `experiment-anomaly-baseline-2026-03.md`.

## Typical relations
- Evidences `model-`/`concept-`/`decision-` claims (cite as
  `exp:[[experiment-x]]`); consumes `dataset-`; ran on `entity-` machine.
