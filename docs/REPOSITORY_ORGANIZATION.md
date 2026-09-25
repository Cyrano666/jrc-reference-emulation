# Repository organization

This public repository is the code, data and reproducibility archive for the manuscript "Sequential reference preservation for label-efficient set-valued prediction," submitted to the International Journal of Approximate Reasoning. Use the **ijar-submission-cleanup** release for the current reproducibility archive (Online Resource 1). The repository intentionally contains no manuscript PDF, title page or LaTeX source; those files are handled through the journal submission system.

The source directories `revision/`, `revision5/`, `revision6/` and `revision7/` contain shared code, model implementations, the locked acquisition procedure and diagnostics; deleting them would break imports or remove evidence. `confirmation_hhar/` holds the separately specified additional cohort study. Larger numerical files are distributed through the release as `frozen_artifacts.zip`; `get_artifacts.py` downloads and verifies them against `artifacts.json`.

Older tags and releases are retained as an audit trail and remain available in git history; they are not the current archive.
