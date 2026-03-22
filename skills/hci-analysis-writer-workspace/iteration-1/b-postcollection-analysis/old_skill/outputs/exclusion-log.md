# Exclusion Log

**Study:** LLM Use in University Student Career Preparation
**Data file:** `2026-03-22_survey_export_raw.csv`
**Raw row count (excluding header):** 336
**Analysis date:** 2026-03-22

---

## Exclusion Rules Applied

Rules are drawn directly from the study spec inclusion/exclusion criteria and pre-registered data-quality checks. No rule was added after examining the outcome variables.

| Rule | Criterion | Source |
|------|-----------|--------|
| R1 | consent ≠ "Yes" | Study spec: consent required |
| R2 | eligible_status ≠ "Yes" | Study spec: screener must pass |
| R3 | attention_check_1 ≠ "Agree" OR attention_check_2 ≠ "Boiling water" | Attention checks embedded in survey |
| R4 | completion_seconds < 180 | Completion under 3 minutes inconsistent with 10–12 min target from pilot checklist |

---

## Exclusions: R1 — Consent Not Given

No rows excluded under this rule. All 336 submissions recorded consent = "Yes".

**R1 exclusions: 0**

---

## Exclusions: R2 — Eligibility Screener Failed

No rows excluded under this rule. All 336 submissions recorded eligible_status = "Yes".

**R2 exclusions: 0**

---

## Exclusions: R3 — Attention Check Failure

The survey embedded two attention checks:
- `attention_check_1`: correct response is "Agree"
- `attention_check_2`: correct response is "Boiling water"

Respondents failing either check are excluded. Seven rows showed attention_check_1 = "Disagree" and attention_check_2 = "Interview rehearsal" (both checks failed simultaneously), indicating inattentive or non-compliant response patterns.

| response_id | attention_check_1 | attention_check_2 | Note |
|-------------|-------------------|-------------------|------|
| resp_0047 | Disagree | Interview rehearsal | Both checks failed |
| resp_0094 | Disagree | Interview rehearsal | Both checks failed |
| resp_0141 | Disagree | Interview rehearsal | Both checks failed |
| resp_0188 | Disagree | Interview rehearsal | Both checks failed |
| resp_0235 | Disagree | Interview rehearsal | Both checks failed |
| resp_0282 | Disagree | Interview rehearsal | Both checks failed |
| resp_0329 | Disagree | Interview rehearsal | Both checks failed |

**R3 exclusions: 7**

Note: The pattern of identical wrong answers across all seven failures ("Disagree" / "Interview rehearsal") suggests these respondents may have selected a consistent but incorrect option rather than reading the question. No rows excluded under R3 also appear in the R4 list; the two exclusion categories are non-overlapping.

---

## Exclusions: R4 — Completion Time Too Short (< 180 seconds)

The study pilot target was 10–12 minutes (600–720 seconds). Responses completed in under 3 minutes (< 180 seconds) are implausible for genuine engagement and are excluded as likely bot, straight-line, or highly inattentive submissions.

| response_id | completion_seconds | Note |
|-------------|-------------------|------|
| resp_0031 | 102 | 1m 42s — implausible |
| resp_0062 | 107 | 1m 47s — implausible |
| resp_0093 | 128 | 2m 8s — implausible |
| resp_0124 | 130 | 2m 10s — implausible |
| resp_0155 | 84 | 1m 24s — implausible |
| resp_0186 | 123 | 2m 3s — implausible |
| resp_0217 | 93 | 1m 33s — implausible |
| resp_0248 | 147 | 2m 27s — implausible |
| resp_0279 | 170 | 2m 50s — implausible |
| resp_0310 | 86 | 1m 26s — implausible |

**R4 exclusions: 10**

One borderline case was observed: resp_0314 (180 seconds exactly, the threshold). This response was retained because it falls at the threshold, not below it, and its item-level responses appear internally consistent.

---

## Overlap Check

None of the 10 R4 exclusions appear among the 7 R3 exclusions. Total unique excluded rows = 17.

---

## Final Sample Summary

| Stage | N |
|-------|---|
| Raw submissions | 336 |
| Excluded: consent failure (R1) | 0 |
| Excluded: eligibility failure (R2) | 0 |
| Excluded: attention check failure (R3) | 7 |
| Excluded: completion too fast (R4) | 10 |
| **Valid analytic sample** | **319** |

---

## Stop Criterion Check

The study spec required at least 250 valid responses, including at least 150 respondents who report some career-related LLM use. With N = 319 valid responses and approximately 233 LLM users in the valid sample (see results-summary.md), both stop criteria are met.

---

## Post-Exclusion Notes

- No exclusion rules were modified after examining outcome distributions.
- Exclusion decisions are based solely on data-quality indicators (consent, eligibility, attention checks, completion time), not on substantive response content.
- The exclusion rate is 17/336 = 5.1%, which is within normal range for online surveys and does not suggest systematic recruitment problems.
