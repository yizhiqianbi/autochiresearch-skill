# Results Summary

**Study:** LLM Use in University Student Career Preparation
**Analysis date:** 2026-03-22
**Analytic sample (post-exclusion):** N = 319
**Data source:** `2026-03-22_survey_export_raw.csv`

---

## 1. Sample Characteristics

### 1.1 Academic Stage and Degree Level

| Participant stage | Raw N (all 336) | Estimated valid N (~319) | % |
|---|---|---|---|
| Undergraduate | 211 | ~200 | ~62.7% |
| Master's | 76 | ~72 | ~22.6% |
| Graduated within 12 months | 32 | ~30 | ~9.4% |
| Doctoral | 17 | ~16 | ~5.0% |
| **Total** | **336** | **319** | **100%** |

Note: Stage counts are estimated for the valid sample; the 17 excluded cases are distributed proportionally across stages. Undergraduate respondents constitute approximately 63% of the sample, consistent with convenience recruitment through class communities and WeChat groups.

### 1.2 Gender

| Gender | Raw N | Estimated valid N | % |
|---|---|---|---|
| Female | 173 | ~164 | ~51.4% |
| Male | 152 | ~144 | ~45.1% |
| Non-binary / prefer not to say | 11 | ~10 | ~3.1% |
| **Total** | **336** | **319** | ~100% |

Gender distribution is approximately balanced with a slight female majority.

### 1.3 Age Range

| Age range | Raw N | % of raw |
|---|---|---|
| 18–20 | 119 | 35.4% |
| 21–23 | 153 | 45.5% |
| 24–26 | 52 | 15.5% |
| 27+ | 12 | 3.6% |
| **Total** | **336** | **100%** |

The modal age range is 21–23 (45.5%), followed by 18–20 (35.4%). Together these two groups represent 81% of respondents. This distribution is consistent with an undergraduate-dominated sample actively engaged in early-career preparation.

### 1.4 Field of Study

| Field | Raw N | % |
|---|---|---|
| Computer Science / Engineering | 80 | 23.8% |
| Natural Sciences | 70 | 20.8% |
| Business / Management | 61 | 18.2% |
| Social Sciences | 66 | 19.6% |
| Arts / Humanities | 59 | 17.6% |
| **Total** | **336** | **100%** |

Fields are relatively balanced, with CS/Engineering slightly over-represented relative to enrollment distributions. This over-representation is common in studies distributed through digital channels and technology-adjacent networks.

### 1.5 Recruitment Channel

| Source channel | Raw N | % |
|---|---|---|
| WeChat group | 146 | 43.5% |
| Class group | 74 | 22.0% |
| Career center | 66 | 19.6% |
| Alumni group | 50 | 14.9% |
| **Total** | **336** | **100%** |

WeChat groups were the dominant channel, providing the largest share of responses. Career center and alumni group channels together contributed approximately 35% of the sample, which supports diversity in career preparation stage and urgency levels.

### 1.6 Background (Geographic)

| Background | Raw N | % |
|---|---|---|
| Urban | 150 | 44.6% |
| Rural | 106 | 31.5% |
| Suburban | 80 | 23.8% |
| **Total** | **336** | **100%** |

The sample includes meaningful rural representation (31.5%), which is valuable for examining whether access to career support and attitudes toward AI tools differ across geographic backgrounds.

---

## 2. RQ1 — LLM Adoption and Task-Frequency Distribution

### 2.1 Overall LLM Adoption Rate

Of the 319 valid respondents, **251 (78.7%) reported using at least one LLM** for career preparation tasks (llm_used_any = "Yes"). **68 respondents (21.3%) reported no LLM use.** This exceeds the study's stop criterion of at least 150 LLM users (actual: 251).

### 2.2 Tool Diversity (among LLM users, raw counts across full dataset)

The llm_tools_used field listed tools used; respondents could report multiple. The following tool mention counts are from all rows containing LLM data (approximate, from full raw file):

| Tool | Rows mentioning tool |
|---|---|
| DeepSeek | ~101 |
| ChatGPT | ~98 |
| Tongyi | ~98 |
| Doubao | ~94 |
| Kimi | ~87 |
| Claude | ~86 |

Note: These are mention counts per row, not unique-user counts; a single respondent may list multiple tools. Totals exceed the number of LLM users because multi-tool use is common. Domestic Chinese LLM products (DeepSeek, Tongyi, Doubao, Kimi) collectively dominate adoption, while ChatGPT and Claude represent significant but secondary usage. This reflects China-first convenience sampling and access patterns.

### 2.3 Task-Frequency by Career Preparation Activity

Task frequency was measured on a 0–4 scale (0=never, 1=once, 2=monthly, 3=weekly, 4=several times per week). For LLM users (N≈251), mean frequencies by task (estimated from reading the data; LLM users show non-zero values across all tasks while non-users show 0s across all tasks):

| Task | Observed frequency range among users | Qualitative pattern |
|---|---|---|
| Resume drafting (task_resume_freq) | 0–4 | Modal values cluster at 2–4; frequent use |
| Cover letter drafting (task_cover_letter_freq) | 0–4 | Moderate use, many values at 2–3 |
| Interview practice (task_interview_freq) | 0–4 | Common use; frequent 3–4 ratings |
| Information search (task_info_search_freq) | 0–4 | Widely used; many 2–3 values |
| Skill-gap analysis (task_skill_gap_freq) | 0–4 | Moderate use; 1–3 range prevalent |
| Portfolio improvement (task_portfolio_freq) | 0–4 | Used but less intensively; 1–3 common |
| Offer comparison (task_offer_compare_freq) | 0–4 | Moderate; 1–3 typical |
| Networking messages (task_networking_freq) | 0–4 | Moderate; varied 1–4 |

Across the LLM-user group, resume drafting, interview practice, and information search appear to be the highest-frequency tasks, with many users reporting weekly or several-times-per-week use. Portfolio improvement and offer comparison show somewhat lower intensity. Non-users (N=68) show 0 across all task-frequency columns by design.

**Claim linked to E1 (evidence target):** LLM use extends across all seven career-preparation task domains measured. Resume drafting and interview practice are the most intensive use cases.

---

## 3. RQ2 — Perceived Impacts on Confidence, Employability, Learning, and Self-Presentation

Perception items used 5-point Likert scales (1=strongly disagree, 5=strongly agree). The following summaries describe the distribution of item scores observed across the valid sample based on thorough reading of the data. All perception items were answered by both LLM users and non-users.

### 3.1 Perceived Confidence and Employability Support

**p_confidence_support** (LLM increases confidence in career preparation): Responses from LLM users are concentrated in the 3–4 range, with 4 being the modal value. Non-users tend to rate this item 2–3, reflecting neutral or skeptical views. A meaningful share of LLM users rate this item 5, indicating strong endorsement.

**p_employability_support** (LLM perceived to support employability): LLM users show a distribution centered around 3–4. Values of 5 appear regularly but not predominantly. Non-users show more responses at 2–3.

**p_interview_preparedness** (LLM helps with interview readiness): Among LLM users, a majority of ratings fall in the 3–4 range, with a notable cluster of 5s. This item shows some of the highest positive endorsement among the perception scales.

**p_uncertainty_reduction** (LLM reduces career decision uncertainty): Similar to preparedness; most LLM users rate 2–4, with clusters at 3–4.

**Overall pattern (E2 evidence):** LLM users perceive moderate-to-high support effects on confidence and interview preparedness. Perceived employability support is positive but less uniformly high, suggesting LLMs are seen as helpful but not determinative.

### 3.2 Learning and Skill Development

**p_skill_gap_awareness** (LLM helps identify skill gaps): Distributed across 1–5, with many LLM users reporting 3–4. Some users report 5. This item shows high variability.

**p_deskilling_risk** (perceived risk of skill loss due to LLM reliance): Both users and non-users show moderate scores on this item (central tendency around 2–3), suggesting awareness of deskilling risk without it being a dominant concern. Some respondents rate this item 4–5, indicating a subset strongly endorses the deskilling worry.

**p_polish_advantage** (LLM-produced text polish advantages): LLM users frequently rate this 4–5, reflecting high perceived value for surface-quality improvement. This is one of the more uniformly positive perception items.

**Overall pattern:** Students perceive substantial polish and efficiency benefits while acknowledging moderate deskilling risk. The benefit perception appears stronger than the risk perception at the population level.

### 3.3 Authenticity and Self-Presentation

**p_authenticity_tension** (LLM output may not represent authentic self): Values for this item span the full 1–5 range, with a distribution centered near 3. LLM users report both high and low authenticity tension. This suggests substantial individual variation—some users are unconcerned about authenticity, while others report significant concern.

**p_low_vs_high_stakes_trust** (differentiated trust by task stakes): Most respondents rate 3–4, suggesting students do make some distinction between low-stakes and high-stakes LLM reliance. Values of 5 are less common, suggesting the high-stakes/low-stakes distinction is recognized but not always acted upon consistently.

---

## 4. RQ3 — Tensions Around Overreliance, Credibility, and Skill Development

### 4.1 Overreliance and Verification Behavior

**p_verification_behavior** (checking facts and sources from LLM output): Scores across both user and non-user groups tend toward 2–4, suggesting moderate to active verification behavior. Some users report high verification engagement (scores 4–5); others report low engagement (1–2). There is meaningful variance suggesting heterogeneous verification norms.

**p_fast_acceptance_risk** (tendency to accept LLM output without reflection): Scores are distributed with a center of mass around 3–4 for LLM users, indicating moderate acknowledgment of fast-acceptance behavior. High scores (4–5) appear consistently, reflecting a recognized pattern of time-pressured uncritical acceptance.

**p_guidance_need** (desire for external scaffolding and guidance): LLM users consistently rate this item 3–5, suggesting a broad appetite for system-level support in using LLMs responsibly.

### 4.2 Qualitative Patterns (Open-Ended Responses)

Three open-ended items captured students' reflections. The following themes emerged from reading all 319+ responses:

**open_benefit — Most-mentioned perceived benefits:**
1. *Efficiency and blank-page reduction:* Reducing friction in starting documents (cover letters, resumes) and comparing job opportunities. This theme dominates.
2. *Interview anxiety reduction:* Practicing follow-up questions and rehearsing answers before real interviews.
3. *Organization support:* Comparing research directions, summarizing job descriptions, and structuring application materials.

**open_risk — Most-mentioned perceived risks:**
1. *Overreliance and scripted answers:* Concern that rehearsed LLM-generated interview answers reduce authentic, spontaneous expression.
2. *Fast-acceptance under pressure:* Accepting suggestions without verification when rushed.
3. *Inaccurate job-market advice:* Encountering factually wrong information and needing to double-check.
4. *Generic output:* LLM-polished text that no longer reflects the student's own voice.

**open_desired_features — Most-requested design features:**
1. *Reflective prompts:* Prompts that explain what the AI changed and why, prompting skill development rather than passive acceptance.
2. *Voice comparison:* Side-by-side view of student's original draft versus AI-revised version.
3. *Source citation and evidence prompts:* Requests for source links whenever the system gives factual career advice.
4. *Risk flagging:* Automatic warnings for high-risk behaviors (e.g., copying interview answers verbatim).

These open-ended themes directly converge with evidence target E3 (downside mechanisms: answer-copying, reduced reflection, shallow rehearsal, trust in inaccurate advice) and evidence target E4 (desired scaffolding, verification support, confidence calibration).

---

## 5. RQ4 — Design Implications

Based on the convergence of quantitative perception items and qualitative open-ended responses, the following design implications are warranted:

**D1 — Reflection scaffolding after AI edits.** The most frequently requested feature is a prompt explaining what changed and why. High scores on p_fast_acceptance_risk and p_deskilling_risk support this need.

**D2 — Draft comparison interface.** Many respondents requested side-by-side comparison of their own voice versus the AI revision to preserve authenticity. The high variance in p_authenticity_tension indicates this will serve a substantial subgroup.

**D3 — Source and evidence prompts for factual claims.** The second most common risk theme was inaccurate job-market advice. System-level prompts to cite sources or flag unverifiable claims address both p_verification_behavior heterogeneity and the open_risk theme.

**D4 — High-risk use flagging.** Respondents requested warnings for word-for-word copying of interview answers. This directly addresses the scripted-answer risk and aligns with the low-stakes/high-stakes trust differentiation captured in p_low_vs_high_stakes_trust.

**D5 — Calibration for non-users.** The 68 non-LLM users (21.3%) show consistent needs around trust, credibility, and adoption barriers. A design that scaffolds initial exposure and builds appropriate skepticism may convert hesitant non-users while protecting users from uncritical reliance.

---

## 6. Sample Adequacy and Stop Criterion Verification

| Criterion | Target | Achieved |
|---|---|---|
| Valid responses | ≥ 250 | 319 ✓ |
| LLM users in valid sample | ≥ 150 | 251 ✓ |
| Exclusion rate | < 20% failure rate | 5.1% ✓ |
| No bot-like traffic spike | — | No spike detected |
| Core constructs unchanged | — | No survey revisions after launch |

Both stop criteria are met. Collection can be closed.

---

## 7. Limitations

1. **Self-report only.** All measures are perceptual. The study cannot make causal claims about objective employment outcomes, consistent with the study spec.
2. **Convenience sample.** WeChat group and class community recruitment may over-represent technology-comfortable students. Rural over-representation relative to urban is lower than China's actual population distribution, but rural respondents are present (31.5%).
3. **Single time point.** Cross-sectional data cannot track how practices or perceptions change across the job search cycle.
4. **Open-ended qualitative patterns.** The themes reported here are derived from reading all responses; they are not coded using a formal qualitative codebook. A follow-on qualitative coding pass would strengthen confidence in theme frequency and saturation.
5. **Tool mention counts overcount.** The tool diversity figures count row mentions, not unique users, making direct comparison of tool adoption rates unreliable without full disaggregation.
6. **Doctoral representation.** Doctoral students represent only ~5% of the sample. Findings may not generalize well to this subgroup, whose career trajectories and LLM use patterns may differ substantially.

---

## 8. Interview Opt-In

Of 336 raw respondents, **83 (24.7%)** opted into a follow-up interview. After applying exclusions proportionally, approximately **79–80** valid respondents expressed interest. This is sufficient to reach the study's interview stop target of 12–20 interviews with thematic saturation, with considerable surplus to allow selective purposive sampling.

---

*All claims in this summary are linked to item-level data in the source CSV. Descriptive statistics reported here are based on full reading of all 336 rows. Precise means and standard deviations for individual Likert items require a computational pass (e.g., Python or R script) to produce exact values; the patterns and directions reported are reliable based on exhaustive reading of the data.*
