# Deployment Plan — LLM Career Study (Local / No-Server)
<!-- project: projects/llm -->
<!-- study: Phase 1 Survey -->

## Overview

This study (LLM对大学生就业的影响) is a pure-survey phase-1 study with no prototype component. No custom server is required. The entire data-collection pipeline runs through an external survey platform chosen by the researcher, with all raw data exported and stored locally under `projects/llm/output/`.

The researcher distributes survey links manually through WeChat groups, mailing lists, and career-center channels. Participants never interact with a locally hosted service.

---

## Runtime Stack

| Layer | Choice |
|---|---|
| Survey authoring | `projects/llm/studies/survey.md` (source of truth) |
| Survey hosting | External platform: Wenjuanxing (问卷星) recommended for China-first sample; Qualtrics is an alternative |
| Interview opt-in | Separate form on the same platform or a standalone Tencent Doc / Google Form |
| Local storage | `projects/llm/output/collection/` for raw CSVs |
| Analysis | Local Python scripts in `projects/llm/analysis/` |
| Version control | This workspace directory; no platform credentials or PII in git |

No HTTPS configuration, reverse proxy, or server process is needed for phase 1.

---

## Study Routes and Session Flow

```
Recruitment message
  └─> Survey public link (HTTPS provided by platform)
        └─> Consent gate
              └─> Eligibility screener
                    ├─> Ineligible: soft-exit screen
                    └─> Eligible: main instrument (sections C, U, P, Scenarios, ACs, O, D)
                          └─> Interview opt-in page (separate form)
                                └─> Debrief
```

Session ID is assigned automatically by the survey platform (the `response_id` column in the export). No cross-system session linking is required because there is no prototype.

---

## Pre-Launch Checklist

### Survey construction
- [ ] Copy every question from `studies/survey.md` verbatim into the platform.
- [ ] Verify section order: Consent → Screener → C → U → P → Scenarios → Attention Checks → O → D → Interview Opt-in → Debrief.
- [ ] Apply skip logic: route ineligible responses (S1 = "Other" with no active career prep, S2 = "None of the above") to a soft-exit screen.
- [ ] Set all Likert items to forced-response; mark optional demographic items (D5, D6, D7) as not required.
- [ ] Set attention-check AC1 to require "Agree"; set AC2 correct answer to "Boiling water".
- [ ] Place the interview opt-in on a separate page or a separate form so that contact data is never merged with the main response export.

### Link and access
- [ ] Generate one stable public link for the main survey.
- [ ] Confirm the link opens with HTTPS in a clean browser session.
- [ ] Confirm the platform's privacy policy satisfies your institutional requirements.
- [ ] Record the stable link in the researcher notes (not in any public document).

### Export setup
- [ ] Configure the platform export to produce a CSV with column headers matching `analysis/csv-schema.md`.
- [ ] Download `output/collection/manual_template.csv` and compare headers before collecting real data.
- [ ] Create the naming convention: `YYYY-MM-DD_survey_export_raw.csv` for main data; `YYYY-MM-DD_interview_interest_raw.csv` for opt-in contacts.

### Pilot
- [ ] Run a pilot with 8–12 students per the spec.
- [ ] Measure completion time (target 10–12 minutes).
- [ ] Revise wording-only issues; do not change constructs after pilot.
- [ ] Delete pilot rows from the live dataset before opening full collection.

---

## Smoke Test Procedure

Perform before opening collection to non-pilot participants.

1. Open the public survey link in a private / incognito window.
2. Proceed as an **eligible LLM user**: complete all sections, answer attention checks correctly, select "Yes" for interview opt-in.
3. Submit and confirm a response row appears in the platform response list.
4. Export and verify the row contains all expected columns from `analysis/csv-schema.md`.
5. Repeat as an **ineligible user** (S2 = "None of the above") and confirm the skip logic routes to the exit screen.
6. Open the interview opt-in form and submit a test entry. Confirm it does not appear in the main survey export.
7. Delete all smoke-test rows from both exports before launch.

---

## Collection Monitor Rules

Review at the end of each active collection day:

| Metric | Action threshold |
|---|---|
| Total valid responses | Track toward 250+ target |
| Daily completion rate | Pause if < 50 % over three consecutive days |
| Median completion time | Flag if median drops below 4 minutes |
| Attention-check pass rate (AC1 + AC2) | Pause if failure rate exceeds 20 % on a given day |
| Duplicate open-text patterns | Manually review and flag |
| Balance across degree levels | Note skew; adjust recruitment channels |

Pause collection if suspicious low-duration responses (< 3 minutes) exceed 15 % of new daily submissions.

---

## Sample Targets

- Survey: 250+ valid responses, including 150+ respondents reporting any career-related LLM use.
- Interviews: 12–20 follow-up conversations, or thematic saturation.

---

## Stop Criteria

- Hard stop: 250+ valid responses meeting eligibility and attention-check criteria.
- Pause triggers: bot-like traffic spike, failure rate > 20 %, any revision that would change core scale items after launch.
- Interview stop: 12–20 completed interviews or thematic saturation.

---

## Privacy and Data Storage

- Do not log IP addresses, browser fingerprints, or device information.
- The `response_id` column is the only persistent identifier in the main export.
- Interview contact details must be stored in a separate file (`output/collection/YYYY-MM-DD_interview_interest_raw.csv`) and never joined to the main response table.
- If any incentive is used, collect contact details in a third file; never merge with survey data.
- All local files are kept under `projects/llm/output/` which should not be committed to a public repository.

---

## Environment Variables

No server-side environment variables are needed for phase 1.

If the researcher's analysis scripts later require API keys (e.g., for LLM-assisted qualitative coding), store them in a `.env` file at the workspace root and add `.env` to `.gitignore`. Do not hard-code credentials in any script.

---

## Artifacts Cross-Reference

| Document | Path |
|---|---|
| Survey questions | `projects/llm/studies/survey.md` |
| CSV schema | `projects/llm/analysis/csv-schema.md` |
| CSV header template | `projects/llm/output/collection/manual_template.csv` |
| Distribution guide | `studies/distribution-guide.md` (this output set) |
| Local run instructions | `local-run-instructions.md` (this output set) |
| Data export/import guide | `data-export-import.md` (this output set) |
