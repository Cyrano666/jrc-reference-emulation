# JRC reference-emulation experiments

Experiment code for **Sequential reference preservation for label-efficient set-valued prediction**. The manuscript, editable LaTeX source and submission documents are supplied separately through the journal submission system.

Reproducible finite-pool label-acquisition experiments: 354 classifier cases on seven wearable datasets and 45 additional HHAR cases. This repository contains experiment code, locked protocols, data provenance, frozen summaries and verification scripts.

Current version: [reproducibility-2026-09-26](https://github.com/Cyrano666/jrc-reference-emulation/releases/tag/reproducibility-2026-09-26). Download `frozen_artifacts.zip` (318.6 MB) using the checksum-verifying installer below.

The older `submission-ready-2026-09-17` data release is retained only to keep existing manuscript citations working; use the current release for new reproductions.

## Quick start

Use Python 3.12:

```text
git clone https://github.com/Cyrano666/jrc-reference-emulation.git
cd jrc-reference-emulation
python -m pip install -r requirements.txt
python get_artifacts.py
python boundary_demo.py --pool-size 240
python reproduce.py --smoke
python confirmation_hhar/reproduce.py --smoke
```

The checksum-verified download supplies frozen predictions and evaluation records. Acquisition replay runs on CPU and does not refit classifiers. Smoke runs compare complete paired acquisition cases against stored results.

## Replay all frozen-prediction cases

```text
python reproduce.py
python confirmation_hhar/reproduce.py
python revision7/prior_audit.py --full
python visualization/rebuild_figures.py
```

Main and HHAR replays create timestamped directories. The prior diagnostic writes its declared outputs; use an isolated copy to preserve distributed summaries. Quantitative plots are regenerated into figures/.

These commands replay acquisition from saved classifier predictions and regenerate quantitative Figures 2–7. They do not retrain the classifiers or generate the conceptual architecture diagram (Figure 1). For raw-data preparation and model refitting, see [Refitting](docs/REPRODUCTION.md#refitting); the original datasets and additional training dependencies are required.

| Path | Role |
|---|---|
| revision6/ | JRC bounds, acquisition loop, evaluation, tests and protocol locks |
| confirmation_hhar/ | Additional HHAR preprocessing, training, replay and verification |
| revision7/ | Four-prior diagnostic and quantitative plotting code |
| revision5/ | Shared classifiers, required training configuration and preparation |
| revision/ | Score utilities and first-four-dataset preprocessing dependencies |
| visualization/ | Plot regeneration entry points |
| audits/ | One-look and window-weighted metric checks |
| docs/ | Reproduction instructions and data provenance |

Scientific directory names preserve imports, recorded data paths and locked-file hashes. The original core implementation and protocols are unchanged. See [reproduction](docs/REPRODUCTION.md), [method](docs/METHOD.md) and [data](docs/DATA.md).
