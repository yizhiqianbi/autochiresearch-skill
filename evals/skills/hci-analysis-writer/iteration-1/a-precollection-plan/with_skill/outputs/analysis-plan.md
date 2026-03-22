# Analysis Plan
<!-- STATUS: pre-registration draft — do not modify exclusion rules after full results are visible without documenting reason -->
<!-- Study: LLM 对大学生就业的影响 -->
<!-- Date written: 2026-03-22 -->
<!-- Data collection status: NOT YET STARTED -->

---

## 1. Overview

This document is the pre-registration analysis plan for the Phase 1 survey-first mixed-method study examining how university students use LLMs in career preparation, and how that use shapes their confidence, perceived employability, and sense of tension around overreliance and authenticity. The plan covers exclusion rules, derived variables, primary statistical methods, and planned outputs. Per skill rules, these exclusion rules must not be altered after the full dataset is visible without an explicit documented rationale appended to this file.

---

## 2. Study Design Summary (from study-spec.md)

| Property | Value |
|---|---|
| Study type | Survey-first mixed methods (online questionnaire + optional follow-up interviews) |
| Primary population | Undergraduates, master's students, recent graduates (≤12 months post-graduation) actively in career preparation |
| Geography | China-first convenience sample |
| Target N (survey) | ≥ 250 valid responses, including ≥ 150 with some career-related LLM use |
| Target N (interviews) | 12–20 or thematic saturation |
| Response scale | 5-point Likert + task-frequency (never / once / monthly / weekly / several times per week) |

Research questions driving the analysis:

- **RQ1**: Distribution and frequency of LLM use across career-preparation tasks.
- **RQ2**: Perceived effects on confidence, perceived employability, learning, and self-presentation.
- **RQ3**: Tensions around efficiency, overreliance, authenticity, credibility, and long-term skill development.
- **RQ4**: Design implications for responsible student-facing LLM career tools.

---

## 3. Inclusion and Exclusion Rules

These rules are locked at the time of pre-registration. Any post-hoc deviation must be documented in Section 3.4.

### 3.1 Inclusion Criteria

A response is retained if ALL of the following hold:

1. **Age**: Respondent self-reports age ≥ 18.
2. **Enrollment status**: Currently enrolled in a higher-education program OR graduated within the last 12 months.
3. **Career-preparation engagement**: Respondent confirms active engagement in at least one career-preparation task (resume, interview prep, job search, career exploration, offer comparison, or related activity) — answered on the screener, Step 2 of the survey flow.
4. **Language proficiency**: Completion of the questionnaire in the target language (Chinese or English as localized), as evidenced by non-null, coherent open-ended text on at least one prompt.
5. **Completion**: Respondent reaches the end of the survey (final page submitted). Partial completions that terminate before the main scale block (Step 6) are excluded.

### 3.2 Exclusion Criteria

A response is excluded if ANY of the following hold:

| Rule ID | Criterion | Threshold / Rationale |
|---|---|---|
| EX-01 | Failed screener | Self-reports age < 18, or reports no current enrollment and graduation > 12 months ago, or confirms no career-preparation activity |
| EX-02 | Attention check failure | Fails ≥ 2 embedded attention-check items (e.g., "Please select 'Agree' for this item") — indicates inattentive responding |
| EX-03 | Speeders | Completion time < 4 minutes (approximately one-third of the 10–12 minute pilot target) — indicates random or auto-clicking |
| EX-04 | Straight-lining | Standard deviation of all Likert responses across the main scale block = 0 (all items rated identically throughout the entire block) |
| EX-05 | Bot / duplicate indicator | IP-based duplicate submissions (flag the later submission) OR identical open-ended text across two or more submissions |
| EX-06 | Missing core outcome | Missing responses on > 50% of items within any single primary scale (perceived employability support, interview confidence, or career decision self-efficacy) — renders that construct unmeasurable for that respondent |

### 3.3 Pilot-Exclusion Responses

Responses collected during the 8–12 person pilot phase are excluded from the main analysis dataset. A separate pilot-summary note will document clarity issues identified during pilot review.

### 3.4 Post-Hoc Deviation Log

*(This section is empty at pre-registration. Any changes to Rules 3.1–3.2 made after the full dataset is visible must be appended here, with date, rule ID changed, reason, and the name of the person making the change.)*

---

## 4. Derived Variables

All derived variables are computed from raw item responses via script; no hand-editing of derived scores is permitted.

### 4.1 LLM Use Frequency Score (LLMF)

**Purpose**: Quantify overall reliance on LLMs across career tasks (addresses RQ1, E1).

**Computation**:
1. For each of the seven task domains listed in the survey (resume drafting, cover letter writing, interview rehearsal, information seeking / job search, career planning, portfolio work, offer comparison), recode the frequency item to an ordinal integer:
   - Never = 0, Once = 1, Monthly = 2, Weekly = 3, Several times per week = 4
2. Sum all seven recoded items → `LLMF_sum` (range 0–28).
3. Compute mean across available items → `LLMF_mean` (used when one item is missing; if two or more are missing, treat LLMF as missing for that respondent).

**User classification**:
- `LLM_user` = 1 if `LLMF_sum` ≥ 1 (any use reported); 0 if `LLMF_sum` = 0.
- `LLM_intensity` = three-level categorical: Low (LLMF_sum 1–7), Moderate (8–15), High (16–28). Non-users are kept as a fourth level ("None") for descriptive comparison.

### 4.2 Tool Diversity Index (TDI)

**Purpose**: Capture breadth of LLM tool adoption (addresses RQ1, E1).

**Computation**: Count of distinct LLM systems (e.g., ChatGPT, Claude, Kimi, Wenxin Yiyan, etc.) the respondent reports having used for any career task. Missing / "none" = 0. Report as a raw integer; treat as a continuous predictor in regressions.

### 4.3 Perceived Employability Support Scale (PES)

**Purpose**: Composite measure of how much LLM use is perceived to help with employability (addresses RQ2, E2).

**Computation**: Mean of all items constituting the perceived-employability-support scale block. Report Cronbach's α for internal consistency; if α < 0.70, investigate item-level correlations and flag items for possible removal before locking the scale (document any removal in Section 4 deviation log). Range on the mean score: 1–5 (higher = more positive perception).

### 4.4 Interview Confidence Scale (ICS)

**Purpose**: Self-rated confidence in interview situations (addresses RQ2, E2).

**Computation**: Same procedure as PES — mean of interview-confidence block items, report α. Range 1–5.

### 4.5 Career Decision Self-Efficacy Score (CDSE)

**Purpose**: Perceived ability to make sound career decisions (addresses RQ2, E2).

**Computation**: Mean of career-decision-self-efficacy items, report α. Range 1–5.

### 4.6 Verification Behavior Index (VBI)

**Purpose**: Capture how often respondents fact-check or verify LLM outputs during career tasks (addresses RQ3, E3).

**Computation**: Mean of verification-behavior and source-checking items. Range 1–5 (higher = more frequent verification). Treat as continuous in regression.

### 4.7 Authenticity Concern Score (ACS)

**Purpose**: Extent to which respondents worry that LLM-generated content misrepresents their authentic self (addresses RQ3, E3).

**Computation**: Mean of authenticity / self-presentation concern items. Range 1–5 (higher = greater concern).

### 4.8 Perceived Deskilling Score (PDS)

**Purpose**: Perception that LLM use is reducing independent skill development (addresses RQ3, E3).

**Computation**: Mean of deskilling / overreliance-risk items. Range 1–5 (higher = greater perceived deskilling).

### 4.9 AI Literacy Self-Rating (AILSR)

**Purpose**: Control variable capturing self-assessed AI knowledge and skill (used as a covariate).

**Computation**: Mean of AI-literacy items or single-item rating, as specified in the final instrument. Range 1–5.

### 4.10 Career Stage Indicator (CSI)

**Purpose**: Contextual grouping variable for subgroup comparisons.

**Computation**: Categorical, derived from the career-context block (Step 3):
- Undergraduate job-seeker, Master's job-seeker, Recent graduate (≤12 months), Internship-seeker, Graduate-school applicant.

---

## 5. Primary Statistical Methods

Analysis follows the evidence targets defined in the study spec. All quantitative analyses will be conducted in a reproducible script (e.g., Python with pandas / scipy / statsmodels, or R). No results will be computed manually.

### 5.1 Descriptive Statistics (addresses E1, RQ1)

- Frequency and percentage for `LLM_user` and `LLM_intensity` groups.
- Mean ± SD (or median + IQR for skewed distributions) of `LLMF_sum` for the overall sample and by task domain.
- Bar chart of mean task-specific LLM frequency across the seven career-task domains, sorted by frequency.
- Frequency table for `TDI` (number of tools used); report modal tool(s).
- Cross-tabulation of `LLM_intensity` by `CSI` (career stage).

### 5.2 Internal Reliability (scale validation, prerequisite for 5.3–5.5)

Report Cronbach's α for each composite scale (PES, ICS, CDSE, VBI, ACS, PDS, AILSR) before running inferential tests. If α < 0.70 for any scale, review item-level inter-item correlations and document any item removal in the deviation log before proceeding.

### 5.3 Group Comparisons: LLM Users vs. Non-Users (addresses E2, RQ2)

Primary comparisons between `LLM_user` = 1 vs. 0 on all scale outcomes (PES, ICS, CDSE, VBI, ACS, PDS):

- **Test**: Independent-samples t-test if normality assumptions hold (Shapiro-Wilk p > .05 and n ≥ 30 per group); otherwise Mann-Whitney U.
- **Effect size**: Cohen's d (t-test) or rank-biserial r (Mann-Whitney).
- **Multiple comparisons**: Apply Bonferroni correction across the six primary outcome tests (adjusted α = .05 / 6 ≈ .0083).
- **Reporting**: Table with group means, SDs, test statistic, p-value (corrected), and effect size.

### 5.4 LLM Intensity and Outcome Associations (addresses E2, RQ2)

Examine whether higher LLM use intensity is linearly associated with the three core perception outcomes (PES, ICS, CDSE):

- **Primary test**: Ordinary least squares regression for each outcome, with `LLMF_mean` as the continuous predictor and `AILSR`, `CSI` (dummy-coded), and demographics (gender, degree level) as covariates.
- Report unstandardized B, standardized β, and 95% confidence intervals.
- Check and report model assumptions: residual normality (Q-Q plot), homoscedasticity (Breusch-Pagan), and variance inflation factor (VIF < 5) for collinearity.
- Prespecified exploratory test: add `TDI` as an additional predictor to evaluate whether tool breadth explains unique variance beyond use frequency.

### 5.5 Tension Mechanism Analysis (addresses E3, RQ3)

Examine relationships among tension-related variables (VBI, ACS, PDS) and LLM use intensity:

- Spearman correlations among `LLMF_mean`, `VBI`, `ACS`, and `PDS` — reported as a correlation matrix with 95% CIs (bootstrapped, 1000 iterations).
- One-way ANOVA (or Kruskal-Wallis if non-normal) comparing `ACS` and `PDS` across `LLM_intensity` levels (None, Low, Moderate, High); post-hoc pairwise with Bonferroni correction if omnibus is significant.

### 5.6 Scenario-Based Item Analysis (addresses E3, RQ3)

For the scenario-based "acceptable vs. risky use" items:

- Report percentage of respondents marking each scenario as acceptable, borderline, or risky.
- Chi-square test of independence for each scenario × `LLM_intensity` group to check whether higher users differ in their tolerance for risky LLM use scenarios.

### 5.7 Qualitative Analysis of Open-Ended Prompts (addresses E4, RQ3, RQ4)

Open-ended items (benefits, harms, unmet support needs) will be analyzed using thematic analysis following Braun and Clarke (2006):

1. Familiarization: read all responses.
2. Initial coding: generate descriptive codes inductively, without prior category constraints.
3. Theme development: cluster codes into candidate themes; check for E3-relevant patterns (answer-copying, reduced reflection, shallow skill rehearsal, trust in inaccurate advice) and E4-relevant patterns (scaffolding needs, verification support, confidence calibration).
4. Theme review: test themes against the full dataset.
5. Theme definition: write clear definitions and representative quotes for each theme.
6. Reporting: themes with supporting exemplary quotes (anonymized) and frequency counts of code occurrence.

Inter-rater reliability: a second coder will independently code a 20% random subsample; Cohen's κ or Krippendorff's α will be reported and must exceed .70 before themes are finalized.

### 5.8 Interview Analysis (addresses E4, RQ4, if interviews collected)

Interviews will be transcribed verbatim and analyzed alongside open-ended survey data using the same thematic framework (5.7). Themes from surveys will be tested against interview accounts for confirmatory or disconfirmatory evidence. Member-checking will be used where feasible.

---

## 6. Subgroup and Sensitivity Analyses (Exploratory)

These analyses are exploratory and will be clearly labeled as such in the manuscript:

- Compare LLM use patterns by degree level (undergraduate vs. master's vs. recent graduate).
- Compare PES and ICS by career pathway (job vs. internship vs. graduate school).
- Sensitivity check: re-run primary regressions (5.4) after excluding respondents who failed exactly one attention check (rather than the two-failure threshold in EX-02) to verify robustness of main findings.
- Sensitivity check: re-run with list-wise deletion vs. pairwise deletion for missing items to assess impact on sample size and estimates.

---

## 7. Planned Outputs

| Output | Type | Analysis section |
|---|---|---|
| Table 1: Sample demographics | Markdown / CSV | 5.1 |
| Table 2: LLM use frequency by career task (mean ± SD) | Markdown / CSV | 5.1 |
| Figure 1: Bar chart of task-specific LLM frequency | PNG (script-generated) | 5.1 |
| Table 3: Scale reliability (Cronbach's α, N items, mean, SD) | Markdown / CSV | 5.2 |
| Table 4: Group comparison — users vs. non-users on all outcome scales | Markdown / CSV | 5.3 |
| Table 5: Regression results — LLMF_mean predicting PES, ICS, CDSE | Markdown / CSV | 5.4 |
| Table 6: Correlation matrix — LLMF_mean, VBI, ACS, PDS | Markdown / CSV | 5.5 |
| Figure 2: Boxplots of ACS and PDS by LLM intensity group | PNG (script-generated) | 5.5 |
| Table 7: Scenario-item acceptability rates by LLM intensity | Markdown / CSV | 5.6 |
| Thematic summary: open-ended qualitative themes | Markdown prose | 5.7 |
| Inter-rater reliability report | Inline in manuscript | 5.7 |
| Design implication notes (RQ4) | Markdown section | 5.7–5.8 |
| results_summary.md (post-collection, Phase 2) | Markdown | All |
| exclusion_log.csv (post-collection, Phase 2) | CSV | Section 3 |

---

## 8. Ethics and Reporting Constraints

- All reported findings are limited to self-reported perceptions, confidence, and behaviors — no causal claims about objective employment outcomes will be made.
- Quotes from open-ended items will be anonymized and paraphrased to prevent identification.
- Aggregated statistics only; no individual-level data will be reported.
- Findings will explicitly acknowledge the convenience sample and self-report limitations in any manuscript.

---

## 9. Stop Criteria Reference (from study-spec.md)

- **Survey**: ≥ 250 valid responses, with ≥ 150 reporting any career-related LLM use.
- **Interviews**: 12–20 interviews or thematic saturation.
- Pause trigger: bot-traffic spikes, failure rate > 20%, or core-construct changes in the instrument after launch.

---

## 10. Deviation Log

*(Empty at pre-registration. Append entries here if any deviation from Sections 3–5 is made after data collection begins or after full results are visible. Each entry must include: date, section changed, original rule, new rule, and justification.)*
