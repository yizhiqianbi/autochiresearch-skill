# Data Collection Workflow
<!-- project: projects/llm -->

This document covers everything from opening the survey for collection through returning
participant-filled CSV data into the local analysis pipeline. No server is required at any
point — you share the link yourself and pull the export back manually.

---

## 1. Before Opening Collection

### 1a. Confirm the survey is ready

- The canonical question wording lives in `projects/llm/studies/survey.md`.
- The column schema every export must match is documented in
  `projects/llm/analysis/csv-schema.md`.
- The header-only CSV template is at `projects/llm/output/collection/manual_template.csv`.
  Use this file to verify that a platform export has the right column names before
  importing.

### 1b. Smoke-test the live survey link

1. Open the survey link in a clean browser session (private window).
2. Walk through the full flow: consent gate → screener → main instrument →
   attention checks → open-ended questions → demographics → optional interview opt-in.
3. Submit one eligible-participant response and one ineligible-participant response
   (answer "No" on consent or screener).
4. Export the test responses and compare the column headers against
   `output/collection/manual_template.csv`. They must match exactly.
5. Delete both smoke-test rows from the platform before real collection starts.

---

## 2. Sharing the Link

You distribute the link yourself via whatever channels you use (WeChat groups, class groups,
career-center lists, etc.). There is nothing to configure in this repository for that step.

Use one stable link for the entire wave. Do not revise core scale items after launch.

---

## 3. During Collection — Monitoring

Review the platform dashboard periodically (suggested: once per day when active):

| Signal | Action trigger |
|---|---|
| Completion rate drops below 60 % | Check for broken page or redirect |
| Median completion time < 4 min | Check for bot or auto-fill traffic |
| Attention-check pass rate < 85 % | Consider closing early and inspecting open-ends |
| Response volume stalls | Push a reminder to distribution channels |

Target: 250+ valid responses (after exclusions). Pause collection if low-quality responses
exceed 15 % of new submissions on any single day.

---

## 4. Exporting Data from the Platform

At the end of collection (or at regular snapshot intervals):

1. Log in to the survey platform.
2. Export all responses as **CSV, UTF-8 encoding**.
3. Name the file using the convention:

   ```
   YYYY-MM-DD_survey_export_raw.csv
   ```

   Example: `2026-05-10_survey_export_raw.csv`

4. Save the file here, without modification:

   ```
   projects/llm/output/collection/YYYY-MM-DD_survey_export_raw.csv
   ```

5. If you collected interview opt-in data on a separate form, export that separately:

   ```
   projects/llm/output/collection/YYYY-MM-DD_interview_interest_raw.csv
   ```

   Keep interview contact data in that file only. Never merge it with the main response
   export.

**Rule:** Never edit the raw file after saving it. It is the permanent record of what
participants submitted. All cleaning happens downstream, on a copy.

---

## 5. Column-Mapping the Raw Export

Platform exports often use verbose question text as column headers instead of the short
canonical names. Before running analysis, rename the columns to match the canonical schema.

### The canonical column order

```
response_id, submitted_at, completion_seconds, source_channel, consent, eligible_status,
participant_stage, career_path_primary, career_preparation_urgency, llm_used_any,
llm_tools_used, task_resume_freq, task_cover_letter_freq, task_interview_freq,
task_info_search_freq, task_skill_gap_freq, task_portfolio_freq, task_offer_compare_freq,
task_networking_freq, p_confidence_support, p_employability_support, p_skill_gap_awareness,
p_polish_advantage, p_deskilling_risk, p_verification_behavior, p_low_vs_high_stakes_trust,
p_authenticity_tension, p_interview_preparedness, p_uncertainty_reduction,
p_fast_acceptance_risk, p_guidance_need, scenario_a_acceptability, scenario_b_acceptability,
scenario_c_acceptability, scenario_d_acceptability, attention_check_1, attention_check_2,
open_benefit, open_risk, open_desired_features, age_range, gender, field_of_study,
degree_level, first_gen_optional, economic_status_optional, background_optional,
interview_opt_in
```

The header-only reference file is `projects/llm/output/collection/manual_template.csv`.

### How to remap

**Option A — Python one-liner (recommended)**

Open a terminal in the workspace root and run:

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill/projects/llm
python3 - <<'EOF'
import csv, pathlib

RAW    = pathlib.Path("output/collection/2026-05-10_survey_export_raw.csv")
MAPPED = pathlib.Path("output/collection/2026-05-10_survey_export_mapped.csv")

# Edit this dict: left side = platform header, right side = canonical name
REMAP = {
    "Response ID":           "response_id",
    "Start Date":            "submitted_at",
    # ... add every column that needs renaming
}

with RAW.open(newline="", encoding="utf-8") as fin, \
     MAPPED.open("w", newline="", encoding="utf-8") as fout:
    reader = csv.DictReader(fin)
    renamed = [REMAP.get(h, h) for h in reader.fieldnames]
    writer  = csv.DictWriter(fout, fieldnames=renamed)
    writer.writeheader()
    for row in reader:
        writer.writerow({REMAP.get(k, k): v for k, v in row.items()})

print("Saved to", MAPPED)
EOF
```

**Option B — spreadsheet**

1. Open the raw export in Excel or Numbers.
2. Replace each header cell with the corresponding canonical name from the schema above.
3. Save as CSV (UTF-8) to `output/collection/YYYY-MM-DD_survey_export_mapped.csv`.

After remapping, verify the header row matches `manual_template.csv` exactly before
proceeding.

---

## 6. Importing the CSV into the Analysis Pipeline

Once the column names are correct, run the analysis pipeline on the mapped file.

### Step 1 — Clean and validate

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill/projects/llm

python3 analysis/analyze_fake_data.py \
  --input  output/collection/2026-05-10_survey_export_mapped.csv \
  --out    output/analysis/
```

The script applies the following exclusion rules automatically:

| Rule | Column checked | Exclusion value |
|---|---|---|
| No consent | `consent` | anything other than `Yes` |
| Ineligible | `eligible_status` | anything other than `Yes` |
| Failed both attention checks | `attention_check_1` + `attention_check_2` | both wrong simultaneously |
| Completed too fast | `completion_seconds` | < 180 seconds |

Rows that pass all checks are written to `output/analysis/cleaned_survey.csv`.
Rows that fail at least one check are logged to `output/analysis/exclusion_log.csv`
with the specific reasons.

### Step 2 — Review exclusion log

```bash
# Quick count of excluded rows and reasons
python3 -c "
import csv, collections, pathlib
rows = list(csv.DictReader(pathlib.Path('output/analysis/exclusion_log.csv').open()))
print('Excluded:', len(rows))
for r in rows[:10]:
    print(r)
"
```

If the exclusion rate exceeds 20 %, inspect patterns in the log before proceeding.

### Step 3 — Analysis outputs

After the script finishes, `output/analysis/` will contain:

| File | Contents |
|---|---|
| `cleaned_survey.csv` | Valid responses with derived computed fields added |
| `exclusion_log.csv` | Excluded response IDs and reasons |
| `sample_characteristics.csv` | Demographic breakdown (counts and percentages) |
| `task_usage_summary.csv` | Per-task frequency means and weekly-or-more percentages |
| `scales_summary.csv` | Scale means, SDs, and Cronbach's alpha |
| `group_comparison_summary.csv` | Non-user / light-user / heavy-user comparison |
| `qualitative_theme_summary.csv` | Keyword-coded theme prevalence in open-ends |
| `regression_summary.csv` | OLS results for employability and confidence models |
| `results_summary.md` | Narrative summary of all findings |
| `figure_task_distribution.png` | Bar chart of task-frequency distribution |
| `figure_theme_prevalence.png` | Horizontal bar chart of qualitative theme prevalence |

---

## 7. Storage Layout — Raw vs. Cleaned

```
projects/llm/
  output/
    collection/          ← raw exports only; never edited after saving
      manual_template.csv
      YYYY-MM-DD_survey_export_raw.csv
      YYYY-MM-DD_survey_export_mapped.csv   (optional intermediate after column remap)
      YYYY-MM-DD_interview_interest_raw.csv (interview opt-in, separate file)

    analysis/            ← all cleaned and derived outputs
      cleaned_survey.csv
      exclusion_log.csv
      sample_characteristics.csv
      task_usage_summary.csv
      scales_summary.csv
      group_comparison_summary.csv
      qualitative_theme_summary.csv
      regression_summary.csv
      results_summary.md
      figure_task_distribution.png
      figure_theme_prevalence.png
```

**Separation rule:** Files in `output/collection/` are permanent, unmodified records of
what came off the platform. Files in `output/analysis/` are derived outputs that can be
regenerated at any time by re-running the analysis scripts on the same raw input.

---

## 8. Multiple Collection Waves or Snapshot Exports

If you take interim CSV snapshots during collection (e.g., to monitor progress):

1. Export and save each snapshot with its date in the filename:
   `output/collection/2026-04-15_survey_export_raw.csv`

2. For interim analysis, pass the snapshot as `--input` to the analysis script. Use a
   matching `--out` subdirectory to avoid overwriting the final outputs:

   ```bash
   python3 analysis/analyze_fake_data.py \
     --input  output/collection/2026-04-15_survey_export_raw.csv \
     --out    output/analysis/interim_2026-04-15/
   ```

3. At the end of collection, the final analysis should always run on the complete,
   final-wave raw export.

---

## 9. End-to-End Checklist

- [ ] Smoke test passed and test rows deleted from platform
- [ ] Collection open with stable link
- [ ] Final export downloaded as UTF-8 CSV and saved to `output/collection/` unmodified
- [ ] Interview opt-in export saved to a separate file
- [ ] Column headers remapped to canonical schema
- [ ] `analyze_fake_data.py` run on the mapped file
- [ ] Exclusion log reviewed; exclusion rate checked
- [ ] `output/analysis/` outputs verified (cleaned row count, scale means, figures generated)
- [ ] `results_summary.md` reviewed before writing any manuscript section

---

## 10. If a Participant Sends Their Responses Manually

In the rare case where a participant fills out the `manual_template.csv` header file and
sends it back by email or message:

1. Copy their row into a new file:
   `output/collection/YYYY-MM-DD_manual_entries.csv`

2. Make sure the header row matches `manual_template.csv` exactly.

3. For analysis, concatenate the manual file with the main export before running the
   analysis script:

   ```bash
   python3 - <<'EOF'
   import csv, pathlib

   files = [
       "output/collection/2026-05-10_survey_export_mapped.csv",
       "output/collection/2026-05-10_manual_entries.csv",
   ]
   out = pathlib.Path("output/collection/2026-05-10_combined.csv")

   all_rows = []
   fieldnames = None
   for f in files:
       with open(f, newline="", encoding="utf-8") as fh:
           reader = csv.DictReader(fh)
           if fieldnames is None:
               fieldnames = reader.fieldnames
           all_rows.extend(reader)

   with out.open("w", newline="", encoding="utf-8") as fh:
       writer = csv.DictWriter(fh, fieldnames=fieldnames)
       writer.writeheader()
       writer.writerows(all_rows)

   print(f"Combined {len(all_rows)} rows into {out}")
   EOF
   ```

4. Run `analyze_fake_data.py` on the combined file as in Step 6.
