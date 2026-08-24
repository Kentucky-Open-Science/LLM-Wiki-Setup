# model — a trained artifact or model family

- **Tier**: catalog
- **Prefix**: `model-`
- **Purpose**: a model/architecture/family the user trains or relies on:
  config, training recipe, checkpoints, and which experiments established
  what about it.

## Signals
- checkpoints/weights in `.gitignore`s (`*.pt`, `*.ckpt`, `*.safetensors`,
  `*.gguf`), `checkpoints/`/`ckpts/` dirs, training configs, HF cache
- conversation: "the base model", "our fine-tune", "checkpoint from the
  March run"

## Required sections
- `## Architecture` — backbone, objective, variants
- `## Training` — data (links), config, key hyperparameters
- `## Results` — links to the `experiment-` pages that establish each number
  (numbers live in experiments; this section is the map to them)
- `## Checkpoints` — paths per machine, which is canonical
- `## Relationships` — lineage (fine-tuned from, distilled to), consumers

## Ask the user for
- Checkpoint paths, which config file is authoritative, which experiment
  produced which claimed number.

## Naming
- `model-<name-slug>.md`, e.g. `model-driftwatch-anomaly-v2.md`.

## Typical relations
- Trained on `dataset-`, evidenced by `experiment-`, used by `project-`/
  `service-`, runs on `machine-` hosts.
