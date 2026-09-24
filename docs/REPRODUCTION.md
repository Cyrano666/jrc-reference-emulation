# Reproduction guide

Install requirements.txt with Python 3.12. Run `python get_artifacts.py`, or install a downloaded archive with `python get_artifacts.py --archive PATH_TO_ZIP`. The installer verifies every record before writing and stops on conflicting existing numerical files.

| Command | Purpose |
|---|---|
| `python boundary_demo.py --pool-size 240` | Construct boundaries and independently recompute crossing probability |
| `python reproduce.py --smoke` | Replay one complete main case and compare frozen rows |
| `python reproduce.py` | Replay all 354 cases and compare the overview |
| `python confirmation_hhar/reproduce.py --smoke` | Compare one HHAR case, including campaign rows |
| `python confirmation_hhar/reproduce.py` | Replay all 45 HHAR cases |
| `python revision7/prior_audit.py --full` | Recompute all four original confidence-sequence priors |
| `python visualization/rebuild_figures.py` | Regenerate quantitative Figures 2-7 |
| `python audits/baseline_definition.py` | Recompute one-look ranks and window-weighted enlargement |

Use `python revision6/reproduce.py --resume --output PATH` to resume a main replay. Replays condition on frozen models and partitions and are not new confirmation experiments.

## Implementation checks

Run revision6/test_horizon.py for exhaustive small-population recursion checks, revision6/test_sequential.py for interval/stopping checks, and revision6/check_oracle.py for unqueried-label invariance. These scripts write check reports: use an isolated checkout. Original hashes are recorded in revision6/protocol_lock.json and confirmation_hhar/protocol_lock.json.

## Refitting

Install revision6/requirements.txt and obtain original signals from the providers in DATA.md. The declared InceptionTime-style fitting needs CUDA; saved-probability replay does not. Use a separate copy because training scripts cache cases.

- revision/prepare_v2.py and train_v2.py: first-four-dataset preparation and original fits.
- revision5/download_confirmation.py, prepare_confirmation.py and train_models.py: PAMAP2/REALDISP preparation and shared model fits.
- revision6/download_uschad.py, prepare_uschad.py and train_confirmation.py: USC-HAD preparation and fitting.
- confirmation_hhar/prepare.py and train.py: the additional cohort.

Raw signal archives and preprocessing caches are not required for acquisition replay and are not bundled. Model refitting requires the original inputs; hardware-dependent timings may differ.

## Numerical source map

| Result | Source |
|---|---|
| Acquisition savings and set utility | revision6/summaries/overview.csv |
| Failures | revision6/summaries/failure_rates.csv |
| Window-weighted enlargement | revision6/summaries/campaign_cells.csv |
| Paired participant intervals | revision6/summaries/paired_intervals.csv |
| Classifier outcomes | revision6/summaries/model_summary.csv and prediction metadata |
| Prior diagnostic | revision7/prior_full_summary.csv |
| Timings | revision6/runtime.csv |
| Declared trace | revision6/results/predictions/uschad_0_0_MR.npz |
| Trial-label sensitivity | revision6/schema_sensitivity/ |
| HHAR | confirmation_hhar/summaries/ |
