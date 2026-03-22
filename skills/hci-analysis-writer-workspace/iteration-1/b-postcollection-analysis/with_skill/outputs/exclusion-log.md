# Exclusion Log

**Study:** LLM Use in University Student Career Preparation
**Data file:** `2026-03-22_survey_export_raw.csv`
**Total raw responses:** 336
**Total excluded:** 12
**Final analytic N:** 324
**Analysis date:** 2026-03-22

---

## Exclusion Criteria (Pre-registered in study spec)

The study spec specifies two types of quality controls built into the survey instrument:

1. **Attention checks** — Two items with unambiguous correct answers were embedded in the perception scale block:
   - `attention_check_1`: Expected response = "Agree"
   - `attention_check_2`: Expected response = "Boiling water"
   - Rule: Exclude any respondent who fails **both** checks.

2. **Completion time** — Responses with `completion_seconds < 120` are flagged as likely speeders. The survey was designed for a 10–12 minute completion window; responses below 2 minutes indicate insufficient engagement regardless of answer content. Threshold set at 120 seconds (below one-fifth of the lower bound of the target window).

**Note:** All 336 raw rows passed `consent = Yes` and `eligible_status = Yes`. No ineligible respondents reached the main questionnaire.

---

## Excluded Respondents

### Category A: Failed Both Attention Checks (N = 7)

| response_id | submitted_at | attention_check_1 | attention_check_2 | completion_s | note |
|---|---|---|---|---|---|
| resp_0047 | 2026-03-22T16:07:00 | Disagree | Interview rehearsal | 561 | Both checks failed |
| resp_0094 | 2026-03-22T23:11:00 | Disagree | Interview rehearsal | 655 | Both checks failed |
| resp_0141 | 2026-03-23T06:13:00 | Disagree | Interview rehearsal | 623 | Both checks failed |
| resp_0188 | 2026-03-23T13:14:00 | Disagree | Interview rehearsal | 499 | Both checks failed |
| resp_0235 | 2026-03-23T20:20:00 | Disagree | Interview rehearsal | 468 | Both checks failed |
| resp_0282 | 2026-03-24T03:22:00 | Disagree | Interview rehearsal | 782 | Both checks failed |
| resp_0329 | 2026-03-24T10:24:00 | Disagree | Interview rehearsal | 495 | Both checks failed |

All seven respondents gave the same wrong answers ("Disagree" and "Interview rehearsal"), suggesting they read neither item carefully. Completion times ranged from 468 to 782 seconds, indicating sufficient time was available, ruling out accidental skipping.

### Category B: Completion Time Below Threshold — < 120 Seconds (N = 5)

| response_id | submitted_at | completion_s | llm_used_any | note |
|---|---|---|---|---|
| resp_0031 | 2026-03-22T13:42:00 | 102 | Yes | Below 120s threshold |
| resp_0062 | 2026-03-22T18:18:00 | 107 | Yes | Below 120s threshold |
| resp_0155 | 2026-03-23T08:18:00 | 84 | No | Below 120s threshold |
| resp_0217 | 2026-03-23T17:36:00 | 93 | No | Below 120s threshold |
| resp_0310 | 2026-03-24T07:33:00 | 86 | Yes | Below 120s threshold |

None of these respondents also failed attention checks. However, completing a 48-variable survey (including 12 open-ended characters) in under 2 minutes is physically implausible for thoughtful responses. Excluded on speeder grounds.

### Overlap Between Categories

No respondent appears in both Category A and Category B.

---

## Retained Borderline Cases

Several respondents completed in 120–180 seconds. These were **retained** because they passed both attention checks and their open-ended responses contained substantive, unique text:

| response_id | completion_s | attention_checks | decision |
|---|---|---|---|
| resp_0093 | 128 | Both passed | Retained |
| resp_0124 | 130 | Both passed | Retained |
| resp_0186 | 123 | Both passed | Retained |
| resp_0248 | 147 | Both passed | Retained |
| resp_0279 | 170 | Both passed | Retained |
| resp_0314 | 180 | Both passed | Retained |

---

## Final Analytic Sample

| Category | N |
|---|---|
| Raw responses | 336 |
| Excluded — attention check failure | 7 |
| Excluded — completion time < 120s | 5 |
| **Final valid N** | **324** |

Stop criterion from study spec: ≥ 250 valid responses including ≥ 150 LLM users. **Both criteria are met.**
