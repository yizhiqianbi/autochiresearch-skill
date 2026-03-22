# Local Run Instructions — LLM Study, Phase 1
<!-- Study: LLM对大学生就业的影响 -->
<!-- Generated: 2026-03-22 -->

## What "Local Run" Means for This Study

Phase 1 has no custom prototype app. The survey instrument is hosted on an external platform (Wenjuanxing or Qualtrics). "Local run" in this context means:

1. Running the local analysis pipeline to validate the CSV schema and analysis outputs before collection opens.
2. Running a smoke test against the live survey link to confirm the participant flow works.
3. Generating or regenerating analysis outputs from a collected or synthetic CSV at any time.

No local web server, HTTPS configuration, or Docker setup is required.

## Prerequisites

- Python 3.9 or later
- The following Python packages (install once):

```bash
pip install matplotlib numpy scipy
```

All scripts live under `projects/llm/`. Run commands from the workspace root:

```
/Users/pencil/Documents/PrepareMLLM/autochiresearch-skill/
```

## Step 1 — Validate the CSV Schema Against the Synthetic Export

Before opening real collection, run the analysis pipeline on the synthetic export to confirm the schema and scripts work end-to-end.

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill

python3 projects/llm/analysis/analyze_fake_data.py \
  --input  projects/llm/output/collection/2026-03-22_survey_export_raw.csv \
  --out    projects/llm/output/analysis/
```

Expected output (printed to terminal):

```
Input rows: <N>
Cleaned rows: <N minus exclusions>
Excluded rows: <exclusion count>
Analysis outputs written to projects/llm/output/analysis/
```

Expected files created under `projects/llm/output/analysis/`:

- `cleaned_survey.csv`
- `exclusion_log.csv`
- `sample_characteristics.csv`
- `task_usage_summary.csv`
- `scales_summary.csv`
- `group_comparison_summary.csv`
- `qualitative_theme_summary.csv`
- `regression_summary.csv`
- `results_summary.md`
- `figure_task_distribution.png`
- `figure_theme_prevalence.png`

If any file is missing or the script exits with an error, fix the column mismatch before proceeding to real collection.

## Step 2 — Smoke Test the Live Survey Link

Do this manually before sending the link to any participants.

1. Open the survey link in a fresh browser window (private/incognito mode).
2. Walk through the full flow:
   - Consent gate: confirm the "No" path terminates the survey.
   - Eligibility screener S2: confirm the "None of the above" path terminates early.
   - Screener S3 (LLM use): both Yes and No paths should reach the main instrument.
   - Matrix question U2: confirm all 8 rows render correctly with 5 frequency options.
   - Attention check AC1: confirm "Agree" is a selectable option and the item label matches the survey draft.
   - Attention check AC2: confirm "Boiling water" is one of the four options.
   - Open-ended fields O1–O3: confirm text input accepts multi-sentence responses.
   - Submit one complete response as an eligible participant.
3. Export a test CSV from the platform and compare column headers against `projects/llm/analysis/csv-schema.md`.
4. Confirm the interview opt-in is on a separate form, not in the main export.
5. Delete all smoke-test rows from the live dataset before opening collection to real participants.

## Step 3 — Generate a Fresh Synthetic Dataset (Optional, for Re-Testing)

If the schema has changed or you want to re-run the analysis on a fresh synthetic batch:

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill

python3 projects/llm/analysis/generate_fake_data.py
```

This writes a new synthetic CSV to `projects/llm/output/collection/`. Check the script's default output path and rename the file with today's date before committing.

## Step 4 — Re-Run Analysis on Real Data After Export

After each export during active collection, run:

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill

python3 projects/llm/analysis/analyze_fake_data.py \
  --input  projects/llm/output/collection/YYYY-MM-DD_survey_export_raw.csv \
  --out    projects/llm/output/analysis/
```

Replace `YYYY-MM-DD` with the actual export date. The script overwrites the analysis outputs each time. Raw exports are never overwritten.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `KeyError: 'some_column'` | Platform export column name differs from the canonical schema | Add a column rename mapping at the top of the script, or rename the column in the CSV before running |
| `ValueError: could not convert string to float` | A Likert column contains text labels instead of integers (e.g., "Agree" instead of "4") | Recode the column in the CSV: replace text labels with numeric values matching the 1–5 scale |
| `IndexError` on `cleaned[0]` | All rows were excluded (e.g., pilot data was not removed) | Check the raw export for consent and eligibility columns; confirm smoke-test rows were deleted |
| matplotlib fails silently | `MPLBACKEND` not set to `Agg` on headless machines | The script sets `MPLBACKEND=Agg` automatically; if running in an unusual environment, set it manually: `export MPLBACKEND=Agg` |
| Script runs but figures are blank | No valid cleaned rows | Resolve exclusions first; figures require at least one cleaned row |
