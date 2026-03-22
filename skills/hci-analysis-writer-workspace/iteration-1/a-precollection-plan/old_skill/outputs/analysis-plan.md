# Analysis Plan
<!-- Study: LLM 对大学生就业的影响 -->
<!-- Status: PRE-COLLECTION — written before any data are gathered -->
<!-- Derived from: projects/llm/artifacts/study-spec.md -->
<!-- Date: 2026-03-22 -->

---

## Skill Applicability Note

The `hci-analysis-writer` skill is designed for use after data collection is complete or stop criteria have been reached. This document is produced at the **pre-collection** stage as a registered analysis plan. Its purpose is to lock in decisions about exclusion rules, derived variables, and statistical methods before data are seen, thereby preventing post-hoc analytic flexibility.

All decisions below are pre-registered. Any departure from this plan after data collection begins must be documented with a rationale in the exclusion log and results section.

---

## 1. Study Overview

| Field | Value |
|-------|-------|
| Study type | Survey-first mixed-method |
| Target N (survey) | ≥ 250 valid responses; ≥ 150 who report any career-related LLM use |
| Interview target | 12–20 participants or thematic saturation |
| Population | Undergraduates, master's students, graduates within 12 months of graduation, age ≥ 18, currently engaged in career preparation |
| Geography | China-first convenience sample |

---

## 2. Exclusion Rules

These rules are derived directly from the study spec. They are applied in order; a response failing any rule is excluded and logged.

### 2.1 Eligibility-Based Exclusion (hard rules)

| Rule ID | Criterion | Source |
|---------|-----------|--------|
| EX-01 | Respondent under age 18 | Spec inclusion criteria |
| EX-02 | Not currently enrolled in higher education AND graduated more than 12 months ago | Spec inclusion criteria |
| EX-03 | Not currently engaged in at least one career-preparation task (fails screener) | Spec inclusion criteria |
| EX-04 | Insufficient language proficiency to complete the questionnaire (e.g., flagged by comprehension check or self-report) | Spec inclusion criteria |

### 2.2 Data-Quality Exclusion (hard rules)

| Rule ID | Criterion | Threshold / Operationalization |
|---------|-----------|-------------------------------|
| EX-05 | Failed attention check(s) | ≥ 1 failed attention-check item results in exclusion |
| EX-06 | Completion time below minimum plausible threshold | < 3 minutes total survey time (to be confirmed against pilot median) |
| EX-07 | Bot-like response pattern | Identical response to all Likert items across all scales (straight-lining); or flagged by platform bot-detection |
| EX-08 | Duplicate submission | Same IP address or device fingerprint submitted more than once; retain the first valid submission |
| EX-09 | Excessive missing data on core scales | > 30 % of scale items missing across the main quantitative constructs |

### 2.3 Conditional Notes

- If the pilot reveals that completion time distributions shift, EX-06's threshold will be updated before full launch and documented.
- EX-07 (straight-lining) will be operationalized as zero variance across all Likert responses (numeric standard deviation = 0 across all scale items).
- Respondents who fail EX-01 through EX-04 are excluded before any substantive analysis; those who fail EX-05 through EX-09 are logged separately as post-collection quality exclusions.

---

## 3. Derived Variables

Derived variables are computed from raw item responses after exclusions are applied. All derivation logic must be implemented in a reproducible analysis script (R or Python) and not modified by hand after data are in hand.

### 3.1 Composite Scale Scores

| Variable Name | Source Items | Derivation Rule | Notes |
|---------------|-------------|-----------------|-------|
| `llm_use_freq_composite` | Task-by-task LLM use frequency items (resume, cover letter, interview rehearsal, information seeking, planning, portfolio, offer comparison) | Mean of numeric-coded frequency items (never = 0, once = 1, monthly = 2, weekly = 3, several times per week = 4) | Reflects overall LLM use intensity; E1, E2 |
| `llm_user_binary` | Any single task-frequency item ≥ 1 (i.e., used at least once) | 1 if `llm_use_freq_composite` > 0, else 0 | Defines the user vs. non-user contrast group |
| `perceived_employability_support` | Relevant Likert items on perceived employability support scale | Mean of items; reverse-code negatively worded items before averaging | E2 |
| `interview_confidence` | Likert items on interview confidence | Mean of items; reverse-code as needed | E2 |
| `career_decision_selfefficacy` | Likert items on career decision self-efficacy | Mean of items | E2 |
| `verification_behavior` | Items on source-checking and verification frequency | Mean of items; higher = more verification | E3 |
| `authenticity_concern` | Items on self-presentation and authenticity worry | Mean of items | E3 |
| `deskilling_concern` | Items on perceived overreliance and skill-development tension | Mean of items | E3 |
| `ai_literacy` | Single self-rating item or brief scale | Use raw score if single item; mean if multi-item | Covariate |
| `tool_diversity` | Count of distinct LLM tools reported in tool inventory | Integer count ≥ 0 | E1 |

### 3.2 Categorical / Grouping Variables

| Variable Name | Derivation Rule |
|---------------|-----------------|
| `llm_use_tier` | Tertile split of `llm_use_freq_composite` among users: low / medium / high use; non-users coded as a separate baseline category |
| `career_stage` | Derived from survey item on current stage: early exploration / active job search / offer stage / graduate-school track |
| `degree_level` | Undergraduate vs. master's (or other postgraduate) from demographics |
| `recent_graduate` | 1 if graduated within last 12 months and not currently enrolled |

### 3.3 Composite Reliability Checks

Before using any composite score in analysis, compute Cronbach's alpha (or McDonald's omega for non-normal items). If alpha < .70 for a multi-item scale, report the value, examine inter-item correlations, and note it as a limitation. Do not drop items post-hoc to inflate alpha without pre-specifying the item selection rule.

---

## 4. Statistical Methods

Methods are chosen to match the survey-first mixed-method design specified in the study spec. All analyses correspond to the evidence targets (E1–E4).

### 4.1 Descriptive Statistics (E1)

- Frequency and percentage tables for each career-preparation task by LLM use frequency tier.
- Mean, SD, median, and IQR for all composite scales, reported separately for LLM users and non-users.
- Bar charts of task-by-task LLM use frequency (% respondents at each frequency level per task).
- Count and percentage of respondents in each `career_stage` and `degree_level` group.

### 4.2 Scale Reliability and Dimensionality (E2, E3)

- Cronbach's alpha (or omega) for each multi-item scale: `perceived_employability_support`, `interview_confidence`, `career_decision_selfefficacy`, `verification_behavior`, `authenticity_concern`, `deskilling_concern`.
- Exploratory factor analysis (EFA) if any scale has items from multiple theoretical constructs, to confirm or revise subscale structure.

### 4.3 Group Comparisons: LLM Users vs. Non-Users (E2, E3)

- Independent-samples Mann-Whitney U test (non-parametric, because Likert composites may not be normally distributed) comparing users vs. non-users on each perceptual scale.
- Report effect size: rank-biserial correlation r.
- Bonferroni correction applied across the number of comparisons in this family.

### 4.4 Correlation and Regression: LLM Use Intensity and Perceptions (E2)

- Spearman rank correlations between `llm_use_freq_composite` and each of: `perceived_employability_support`, `interview_confidence`, `career_decision_selfefficacy`.
- Multiple linear regression (OLS) with `perceived_employability_support` as the primary outcome:
  - Predictors: `llm_use_freq_composite`, `ai_literacy`, `degree_level`, `career_stage`, `tool_diversity`.
  - Check assumptions: residual normality (Shapiro-Wilk), homoscedasticity (Breusch-Pagan), VIF < 5 for multicollinearity.
  - If assumptions are violated, use robust regression (HC3 standard errors) or report results as exploratory.
- Parallel regression models for `interview_confidence` and `career_decision_selfefficacy` as secondary outcomes; treat as exploratory given multiple testing.

### 4.5 Downside Mechanism Analysis (E3)

- Spearman correlations between `llm_use_freq_composite` and `deskilling_concern`, `authenticity_concern`, `verification_behavior`.
- Descriptive summary of scenario-based item responses: % endorsing each acceptable vs. risky scenario, cross-tabulated by `llm_use_tier`.
- Chi-square test of independence for scenario endorsement by `llm_use_tier` (low / medium / high / non-user); report Cramér's V.

### 4.6 Open-Ended Survey Prompts (E4)

- Inductive thematic analysis following Braun & Clarke (2006):
  1. Familiarization with all responses.
  2. Initial open coding.
  3. Theme clustering and labeling.
  4. Review and refinement by at least two coders.
  5. Inter-rater reliability reported as Cohen's kappa on a random 20 % sample; target κ ≥ .70.
- Themes will be reported with representative quotes (anonymized) and frequency counts.
- Thematic findings will be mapped back to evidence target E4 (where students want scaffolding, verification support, and confidence calibration).

### 4.7 Interview Analysis (E4)

- If interview data are collected (12–20 participants or saturation):
  - Semi-structured transcript analysis using thematic analysis (same procedure as 4.6).
  - Data triangulation: compare interview themes to open-ended survey themes and quantitative patterns.
  - Saturation assessment documented by theme emergence curve.
  - Report participant N and whether saturation was reached.

### 4.8 Significance Conventions

| Parameter | Value |
|-----------|-------|
| Alpha level (two-tailed) | .05 |
| Multiple comparison correction | Bonferroni within each hypothesis family |
| Effect size reporting | Always report alongside p-values |
| Confidence intervals | 95 % CIs reported for regression coefficients and mean differences |

---

## 5. Analysis Execution Rules

These rules operationalize the skill's own constraints for pre-registered analysis:

1. **Lock before data arrival.** This plan must not be revised after the first complete data export is viewed, except for corrections to typographic errors or pilot-driven adjustments documented before full launch.
2. **Exclusion log required.** Every excluded response must appear in a separate exclusion log with the rule ID (EX-01 through EX-09) and a brief reason. The log will be an appendix artifact alongside the cleaned data summary.
3. **Script-driven figures and tables.** No figures or tables may be produced by hand. All outputs must be generated by a versioned analysis script; the script will be archived alongside the data.
4. **Separate results from interpretation.** The results section will state numerical findings only. Interpretation and implications for design (RQ4) belong in the discussion section.
5. **No post-hoc exclusion rule changes.** If a new data-quality concern emerges after collection, it must be labeled as a post-hoc sensitivity analysis, not applied to the primary analysis.
6. **Ethics compliance.** No individual-level data are reported. Quotes from open-ended responses are anonymized. Interview contact data are kept in a separate file and never merged with survey responses.

---

## 6. Planned Outputs (to be produced after data collection)

When data collection is complete, the `hci-analysis-writer` skill should produce the following artifacts:

| Artifact | Description |
|----------|-------------|
| `cleaned-data-summary.md` | Record of raw N, excluded N per rule, final analysis N |
| `exclusion-log.csv` | Row per excluded response with rule ID and reason |
| `reliability-report.md` | Alpha/omega per scale, EFA results if run |
| `descriptive-tables.csv / .tex` | Means, SDs, frequencies per construct and group |
| `regression-results.md` | Regression tables with coefficients, CIs, effect sizes |
| `correlation-matrix.csv` | Spearman r matrix for key quantitative variables |
| `scenario-analysis.md` | Chi-square and Cramér's V for scenario items |
| `thematic-coding-scheme.md` | Codebook with definitions, examples, kappa |
| `figures/` | Bar charts, scatter plots, thematic frequency charts (script-generated) |
| `results-prose.md` | Manuscript-ready results section text |
| `limitations-notes.md` | Notes on self-report bias, convenience sample, single-country scope |

---

## 7. Limitations to Pre-Register

The following limitations are known before data collection and must be disclosed in the final paper:

- **Self-report only.** All outcome measures are perceptual; no behavioral logging or objective employment outcomes are captured. Causal claims about LLM use and actual employment are not supported by this design.
- **Convenience sample.** Recruitment through university networks and WeChat groups will oversample digitally engaged students; findings may not generalize to students with limited LLM access.
- **China-first geography.** Results reflect a specific regulatory and platform context (e.g., domestic LLM tools vs. GPT-family tools) and may not transfer to other national contexts.
- **Cross-sectional design.** No longitudinal data; associations between LLM use intensity and perceptions cannot be interpreted as causal.
- **Social desirability.** Students may under-report reliance on LLMs for self-presentation tasks if they perceive it as academically dishonest.
- **Scale development.** If any scales are adapted or newly constructed rather than validated instruments, internal consistency and construct validity are not guaranteed.
