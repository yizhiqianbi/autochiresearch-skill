# Local Run Instructions — LLM Career Study
<!-- project: projects/llm -->
<!-- study: Phase 1 Survey — Local Preview and Analysis Environment -->

## Purpose

This document explains how to preview the survey locally before uploading it to the hosting platform, how to verify the question flow offline, and how to run the local analysis pipeline once data is collected. No server needs to be running during actual data collection.

---

## Part 1: Local Survey Preview (Before Platform Upload)

Because the canonical survey lives in `projects/llm/studies/survey.md`, you can render and review it locally in a browser before constructing the live form.

### Option A: Render Markdown in VS Code (fastest)

1. Open VS Code.
2. Open `projects/llm/studies/survey.md`.
3. Press `Cmd+Shift+V` (macOS) or `Ctrl+Shift+V` (Windows/Linux) to open the Markdown preview panel.
4. Read through every section in order: Consent → Screener → C → U → P → Scenarios → Attention Checks → O → D → Interview Opt-In → Debrief.
5. Annotate any wording concerns in a separate note before uploading to the platform.

### Option B: Convert to HTML and open in a browser

Requires `pandoc` (install via `brew install pandoc` on macOS).

```bash
pandoc projects/llm/studies/survey.md \
  -o /tmp/survey_preview.html \
  --standalone \
  --metadata title="Survey Preview — LLM Career Study"
open /tmp/survey_preview.html   # macOS
# or: xdg-open /tmp/survey_preview.html  (Linux)
# or: start /tmp/survey_preview.html     (Windows)
```

This produces a self-contained HTML file you can scroll through and share with co-investigators for sign-off. The file is temporary; it is not the live form.

### Option C: Quick terminal read

```bash
cat projects/llm/studies/survey.md | less
```

Useful for a fast line-by-line check without installing anything.

---

## Part 2: Verifying the CSV Template Locally

Before uploading the survey to the platform, confirm the local header template matches the canonical schema.

```bash
head -1 projects/llm/output/collection/manual_template.csv
```

Compare the output to `projects/llm/analysis/csv-schema.md`. Every field listed in the schema should appear as a column header in the template. If a column is missing, add it to the template and update the csv-schema document before platform construction begins.

---

## Part 3: Local Pilot Review Workflow

After running the pilot (8–12 students), the researcher receives a small CSV from the platform.

1. Save it as `projects/llm/output/collection/YYYY-MM-DD_pilot_export_raw.csv`.
2. Open the file in a spreadsheet application or run:

```python
import pandas as pd
df = pd.read_csv("projects/llm/output/collection/YYYY-MM-DD_pilot_export_raw.csv")
print(df.shape)
print(df.columns.tolist())
print(df["completion_seconds"].describe())
```

3. Check:
   - Column headers match `manual_template.csv`.
   - `completion_seconds` median is 600–720 seconds (10–12 minutes).
   - Attention-check columns (`attention_check_1`, `attention_check_2`) are present.
   - Interview opt-in data does NOT appear in this file.

4. Delete pilot rows from the platform before opening full collection.

---

## Part 4: Local Analysis Pipeline

Once data collection is closed and raw CSVs are saved, run the analysis locally. Python 3.10+ is assumed.

### 4.1 Set up the environment

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill/projects/llm

# Create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate.bat       # Windows

# Install dependencies (add to requirements.txt if not present)
pip install pandas numpy scipy statsmodels matplotlib seaborn
```

### 4.2 Run the analysis scripts

```bash
# Generate fake data for pipeline testing (before real data arrives)
python analysis/generate_fake_data.py

# Run the analysis pipeline on real or fake data
python analysis/analyze_fake_data.py
```

Output files are written to `output/analysis/`. Do not overwrite the raw export; always read from the `_raw.csv` file and write cleaned derivatives to `output/analysis/`.

### 4.3 Directory layout during analysis

```
projects/llm/
  output/
    collection/
      YYYY-MM-DD_survey_export_raw.csv       <- untouched platform export
      YYYY-MM-DD_interview_interest_raw.csv  <- separate opt-in contacts
    analysis/
      cleaned_survey.csv                     <- after exclusion logic
      exclusion_log.csv                      <- who was dropped and why
      sample_characteristics.csv
      task_usage_summary.csv
      scales_summary.csv
      group_comparison_summary.csv
      regression_summary.csv
      qualitative_theme_summary.csv
      results_summary.md
      figure_task_distribution.png
      figure_theme_prevalence.png
```

### 4.4 Exclusion logic (apply before any analysis)

Exclude a response row if any of the following are true:

- `consent` is not "Yes"
- `eligible_status` is "Ineligible" (screener S2 = "None of the above")
- `attention_check_1` is not "Agree"
- `attention_check_2` is not "Boiling water"
- `completion_seconds` < 180 (under 3 minutes — likely rushing or bot)

Log every excluded row with the reason to `output/analysis/exclusion_log.csv`.

---

## Part 5: Quick Health Check During Collection

While collection is ongoing, run this short script daily to check the response count and quality:

```python
import pandas as pd, datetime

path = "output/collection/YYYY-MM-DD_survey_export_raw.csv"  # update date
df = pd.read_csv(path)

valid = df[
    (df["consent"] == "Yes") &
    (df["eligible_status"] != "Ineligible") &
    (df["attention_check_1"] == "Agree") &
    (df["attention_check_2"] == "Boiling water") &
    (df["completion_seconds"] >= 180)
]

print(f"Total rows: {len(df)}")
print(f"Valid rows: {len(valid)}")
print(f"Completion rate: {len(valid)/len(df)*100:.1f}%")
print(f"LLM users: {(valid['llm_used_any'] == 'Yes').sum()}")
print(f"Median time (s): {valid['completion_seconds'].median():.0f}")
print(f"AC1 fail rate: {(df['attention_check_1'] != 'Agree').mean()*100:.1f}%")
print(f"AC2 fail rate: {(df['attention_check_2'] != 'Boiling water').mean()*100:.1f}%")
```

Pause collection if:
- Completion rate drops below 50% for 3+ consecutive days.
- AC1 or AC2 fail rate exceeds 20% on any day.
- Median completion time drops below 4 minutes.

---

## Part 6: No-Server Verification Checklist

Because there is no local server, the "smoke test" is manual. Run through this checklist before sending the first recruitment message.

- [ ] Survey platform link opens in an incognito window with HTTPS.
- [ ] Consent gate blocks progression if "No" is selected.
- [ ] Screener skip logic routes ineligible respondents to an exit screen.
- [ ] All Likert matrices render and accept one response per row.
- [ ] Attention check AC1 accepts only "Agree" and flags other responses on export.
- [ ] Attention check AC2 offers the four options with "Boiling water" as distractor.
- [ ] Open-ended boxes accept multi-line text.
- [ ] Interview opt-in page or form does not pre-fill any survey data.
- [ ] Debrief screen shows after final submission.
- [ ] Export from platform contains correct column headers matching `manual_template.csv`.
- [ ] Pilot rows deleted from platform before launch.
