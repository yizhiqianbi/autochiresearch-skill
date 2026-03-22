---
name: hci-analysis-writer
description: >
  Write HCI study analysis plans and run post-collection analysis — covering exclusion logic,
  derived variables, statistical tests, qualitative coding, figures, tables, and manuscript-ready
  results prose. Use this skill both BEFORE data collection (to write analysis-plan.md and lock
  in your analysis strategy) and AFTER collection (to clean data, run scripts, and generate
  results). If the user needs to plan how to analyze a study, define what statistics to run, or
  actually execute the analysis on collected data, use this skill. Also use it to write the
  Methods and Results sections of an HCI paper.
---

# HCI Analysis Writer

This skill covers two distinct but connected jobs: **planning** the analysis before data collection
and **executing** the analysis after data comes in. Both produce concrete, reproducible artifacts.

## Phase 1: Pre-Collection Analysis Planning

Use this when the study spec is ready but data collection hasn't started yet.

1. Load the study spec and research question.
2. Define:
   - inclusion and exclusion rules (based on completion, attention checks, demographics)
   - derived variables and how they're computed
   - primary analysis methods matched to the study design:
     - survey → descriptive stats, internal reliability (Cronbach's α), regression or group comparison when justified
     - prototype study → completion rate, time-on-task, usability scales, behavioral log analysis
     - gameplay study → event sequences plus post-play responses
     - mixed methods → quantitative results plus qualitative coding scheme
   - planned outputs (tables, figures, prose sections)
3. Write `analysis/analysis-plan.md` — this becomes the pre-registration record.
4. Commit: do not change exclusion rules after full results are visible without documenting why.

## Phase 2: Post-Collection Analysis

Use this when data collection is complete or stop criteria have been reached.

1. Load the study spec and `analysis/analysis-plan.md`.
2. Clean the raw data following the pre-defined inclusion/exclusion rules.
   - Produce an auditable `output/analysis/exclusion_log.csv`.
3. Build derived variables and summary tables from scripts, not manually.
4. Run the analyses defined in the plan.
5. Generate figures and tables reproducibly — every figure should be regenerable from a script.
6. Write results and methods prose. Use `scientific-writing` for drafting if available.
7. Clean and verify references with `citation-management` before final paper assembly.

## Rules

- Do not change exclusion rules after looking at full results without documenting the reason.
- Separate objective results from interpretation — keep "what we found" and "what it means"
  in distinct sections.
- Every reported claim must link back to a concrete analysis artifact (a table row, a figure, a script).
- Keep figure and table generation reproducible — no hand-edited outputs.

## Outputs

**Pre-collection:**
- `analysis/analysis-plan.md`

**Post-collection:**
- cleaned dataset summary (`output/analysis/cleaned_survey.csv` or equivalent)
- `output/analysis/exclusion_log.csv`
- results tables (CSV or Markdown)
- figures (PNG, generated from scripts)
- `output/analysis/results_summary.md`
- manuscript-ready results prose
- limitations notes
