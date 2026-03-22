# Deployment Plan — LLM Study, Phase 1
<!-- Study: LLM对大学生就业的影响 -->
<!-- Generated: 2026-03-22 -->

## Collection Approach

This study has no custom server. The distribution model is:

1. The researcher authors and hosts the questionnaire on an external survey platform (Wenjuanxing / 问卷星 recommended for the China-first sample; Qualtrics as a fallback).
2. The researcher manually shares the survey link through WeChat groups, class communities, career-center channels, mailing lists, and alumni networks.
3. Responses accumulate on the platform. The researcher exports a CSV snapshot at regular intervals and saves it under `projects/llm/output/collection/`.
4. All analysis is performed locally from the exported CSV files after collection closes.

No local prototype app is required in phase 1. The only local tooling needed is Python for analysis scripts.

## Data Storage

| Asset | Location | Notes |
|---|---|---|
| Raw response exports | `projects/llm/output/collection/YYYY-MM-DD_survey_export_raw.csv` | One file per export snapshot; never overwrite an existing snapshot |
| Interview opt-in contacts | Separate platform form or a separate sheet NOT merged with response data | Keep identity apart from survey answers |
| Cleaned analysis-ready CSV | `projects/llm/output/analysis/cleaned_survey.csv` | Produced by `analysis/analyze_fake_data.py`; regenerate from the latest raw export |
| Analysis outputs (summaries, figures) | `projects/llm/output/analysis/` | Overwrite-safe because they are derived; always regenerate from the raw export |
| Exclusion log | `projects/llm/output/analysis/exclusion_log.csv` | Documents removed rows and their reasons |

Do not collect or store interview contact information in the same file or folder as survey response data. If incentives are used, maintain a separate incentive-tracking sheet that contains contact details only, with no response-level data.

## Operational Checklist Before Opening Collection

- [ ] Pilot run complete with 8–12 students, completion time confirmed at 10–12 minutes.
- [ ] Wording confirmed for LLM tool names, career-preparation task labels, and attention checks.
- [ ] Export from pilot matches the canonical column schema in `projects/llm/analysis/csv-schema.md`.
- [ ] Smoke-test rows deleted from the live dataset.
- [ ] Stable survey link confirmed. The same link will be used for the entire collection wave; do not create multiple links.
- [ ] Interview opt-in is on a separate form, not embedded in the main response export.
- [ ] HTTPS confirmed on the survey platform's hosted URL (delegated to the platform; no local HTTPS setup needed).

## Collection Monitor Rules

Review at least every two days during active collection:

- Total responses accumulated since last check.
- Completion rate (started vs. submitted). Investigate if below 70%.
- Median completion time. Flag if median drops below 4 minutes (possible rushing).
- Attention-check pass rate. Pause collection if failure rate exceeds 20% of new submissions in a single day.
- Duplicate or near-duplicate open-ended text (possible bot or incentive-farm responses).
- Balance across degree levels (undergraduate, master's, recent graduate) and primary career pathway.

Pause collection if suspicious low-duration responses exceed 15% of new submissions on any given day, or if bot-like traffic spikes.

## Stop Criteria

| Criterion | Target |
|---|---|
| Survey valid responses | 250 or more, including at least 150 who report any career-related LLM use |
| Interview follow-up participants | 12–20, or thematic saturation — whichever comes first |
| Hard pause trigger | Failure rate exceeds 20%; bot-like traffic spike; core construct items changed post-launch |
| Collection deadline | Set a calendar deadline at launch (recommended: no more than 8 weeks of active collection) |

After stop criteria are met, export a final dated snapshot, lock the raw file, and proceed to cleaning.

## Privacy Commitments

- Do not ask participants to upload resumes, offer letters, or identifying documents.
- Do not merge interview contact data with survey response data.
- Report only aggregate findings in any publication.
- Do not include any PII in files committed to the project repository.
