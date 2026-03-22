# Data Export and Import — LLM Study, Phase 1
<!-- Study: LLM对大学生就业的影响 -->
<!-- Generated: 2026-03-22 -->

## Overview

Responses accumulate on the external survey platform. The researcher periodically exports a CSV and saves it locally. All downstream analysis reads from those local CSV snapshots. This document describes:

1. How to export data from the survey platform.
2. The canonical column schema the export must match.
3. How to rename or recode columns when the platform uses different labels.
4. How to run the analysis pipeline on an imported CSV.
5. File naming and versioning rules.

## Step 1 — Export from the Survey Platform

### Wenjuanxing (问卷星)

1. Log into the platform and open the survey dashboard.
2. Navigate to "数据" (Data) tab for the active survey.
3. Click "下载数据" or "导出数据" and select CSV format.
4. If given encoding options, select UTF-8.
5. If given row options, export "所有回答" (all responses).

### Qualtrics

1. Open the survey in Qualtrics and click "Data & Analysis".
2. Click "Export & Import" > "Export Data".
3. Select CSV format. Deselect "Use choice text" if you want numeric codes; otherwise the recoding step below is required.
4. Download the .csv file.

## Step 2 — Save the Raw Export

Save the file immediately to the collection folder with a dated name. Never overwrite an existing raw export.

```
projects/llm/output/collection/YYYY-MM-DD_survey_export_raw.csv
```

Example for an export taken on 2026-04-10:

```
projects/llm/output/collection/2026-04-10_survey_export_raw.csv
```

Keep all dated snapshots. They serve as the audit trail and allow recovery if a later export contains platform-side issues.

## Step 3 — Compare Column Headers Against the Canonical Schema

Open the exported CSV and compare its header row against the canonical schema in:

```
projects/llm/analysis/csv-schema.md
```

The canonical columns are (in order):

```
response_id, submitted_at, completion_seconds, source_channel, consent,
eligible_status, participant_stage, career_path_primary,
career_preparation_urgency, llm_used_any, llm_tools_used,
task_resume_freq, task_cover_letter_freq, task_interview_freq,
task_info_search_freq, task_skill_gap_freq, task_portfolio_freq,
task_offer_compare_freq, task_networking_freq,
p_confidence_support, p_employability_support, p_skill_gap_awareness,
p_polish_advantage, p_deskilling_risk, p_verification_behavior,
p_low_vs_high_stakes_trust, p_authenticity_tension,
p_interview_preparedness, p_uncertainty_reduction, p_fast_acceptance_risk,
p_guidance_need,
scenario_a_acceptability, scenario_b_acceptability,
scenario_c_acceptability, scenario_d_acceptability,
attention_check_1, attention_check_2,
open_benefit, open_risk, open_desired_features,
age_range, gender, field_of_study, degree_level,
first_gen_optional, economic_status_optional, background_optional,
interview_opt_in
```

A blank template with only the header row lives at:

```
projects/llm/output/collection/manual_template.csv
```

## Step 4 — Recode or Rename Columns if Needed

Survey platforms often export with their own column names or text labels instead of numbers. Fix these before running the analysis script.

### Renaming Columns

Open the CSV in any spreadsheet tool or text editor and rename the header cells to match the canonical names above. Alternatively, add a renaming map at the top of the analysis script.

### Recoding Likert Text Labels to Integers

The analysis script expects Likert items (P1–P12, scenario items) as integers 1–5. If the platform exported text labels, recode them:

| Platform label | Integer value |
|---|---|
| Strongly disagree / 非常不同意 | 1 |
| Disagree / 不同意 | 2 |
| Neutral / 一般 | 3 |
| Agree / 同意 | 4 |
| Strongly agree / 非常同意 | 5 |

For task-frequency columns, recode:

| Platform label | Integer value |
|---|---|
| Never / 从未 | 0 |
| Once / 一次 | 1 |
| Monthly / 每月 | 2 |
| Weekly / 每周 | 3 |
| Several times per week / 每周多次 | 4 |

### Recoding Consent and Eligibility

`consent` must be `Yes` or `No`.
`eligible_status` must be `Yes` or `No` (set to `No` for participants who failed the screener).
`llm_used_any` must be `Yes` or `No`.
`attention_check_1` must be `Agree` or the actual response text.
`attention_check_2` must be the text of the selected option (correct answer: `Boiling water`).

## Step 5 — Run the Analysis Pipeline

Once the CSV header and values are in canonical form, run:

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill

python3 projects/llm/analysis/analyze_fake_data.py \
  --input  projects/llm/output/collection/YYYY-MM-DD_survey_export_raw.csv \
  --out    projects/llm/output/analysis/
```

The script applies exclusion rules and writes all analysis outputs to `projects/llm/output/analysis/`.

Exclusion rules applied by the script:

| Rule | Column checked | Exclusion label |
|---|---|---|
| No consent | `consent != "Yes"` | `no_consent` |
| Ineligible | `eligible_status != "Yes"` | `ineligible` |
| Failed both attention checks | `attention_check_1 != "Agree"` AND `attention_check_2 != "Boiling water"` | `failed_both_attention_checks` |
| Too fast | `completion_seconds < 180` | `too_fast` |

Excluded rows are written to `projects/llm/output/analysis/exclusion_log.csv` with the response ID and reason.

## Step 6 — Handling Returned CSVs from Collaborators

If a collaborator or RA collected responses separately and returns a CSV file:

1. Confirm the file uses the canonical schema (Step 3 above).
2. Rename it with the date received: `YYYY-MM-DD_survey_export_raw_[source].csv`.
3. Save it under `projects/llm/output/collection/`.
4. Check for duplicate `response_id` values against existing exports before merging.

To merge two CSV files manually:

```bash
# Combine two exports into one, keeping only the header from the first file
head -1 projects/llm/output/collection/2026-04-10_survey_export_raw.csv > projects/llm/output/collection/merged_raw.csv
tail -n +2 projects/llm/output/collection/2026-04-10_survey_export_raw.csv >> projects/llm/output/collection/merged_raw.csv
tail -n +2 projects/llm/output/collection/2026-04-15_survey_export_raw_collaborator.csv >> projects/llm/output/collection/merged_raw.csv
```

Then run the analysis on the merged file:

```bash
python3 projects/llm/analysis/analyze_fake_data.py \
  --input  projects/llm/output/collection/merged_raw.csv \
  --out    projects/llm/output/analysis/
```

## File Versioning Rules

| Rule | Reason |
|---|---|
| Never overwrite a raw export | Raw files are the audit trail; all cleaning is done in the script |
| Use dated filenames for every export | Enables reconstruction of when each response arrived |
| Keep cleaned outputs in `output/analysis/`, not `output/collection/` | Separates raw source-of-truth from derived outputs |
| Do not commit response data to git if the repository is public | Survey responses may contain free-text that is not fully anonymous |

## Interview Contact Data — Separate Handling

Interview opt-in contacts are stored in a completely separate file. Never import them into or merge them with the main response CSV.

Recommended separate file path (outside the main project if the repo is shared):

```
[secure local folder]/llm-study-interview-contacts/YYYY-MM-DD_interview_interest.csv
```

Columns for that file: `contact_id`, `submitted_at`, `preferred_contact_method`, `contact_detail`, `respondent_code_optional`.

If linkage between a survey response and an interview is ever needed, use a voluntary respondent code the participant enters on both forms — never link by name or contact detail.
