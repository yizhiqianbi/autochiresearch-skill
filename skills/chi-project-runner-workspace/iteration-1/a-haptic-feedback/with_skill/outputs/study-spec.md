# Study Specification
**Project:** Haptic Feedback UI for Mobile Form Filling Experience
**Date:** 2026-03-22
**Phase:** Mid — Study Design
**Status:** Complete

---

## 1. Research Questions (restated)

| ID | Question |
|----|----------|
| RQ1 | Does event-differentiated haptic feedback reduce form completion time compared to a visuals-only baseline? |
| RQ2 | Does haptic feedback reduce the number of field re-entries (error corrections) before successful submission? |
| RQ3 | How do users perceive usability (SUS), frustration (NASA-TLX), and task confidence with and without haptic feedback? |
| RQ4 | Do individual differences (age, haptic sensitivity, smartphone usage frequency) moderate the effect? |

---

## 2. Study Design Overview

| Parameter | Value |
|-----------|-------|
| Design | Within-subjects, 2-condition repeated-measures |
| Conditions | HAPTIC (event-differentiated vibrotactile cues) vs. CONTROL (no haptic feedback) |
| Primary task | Complete a standardised mobile registration/checkout form |
| Setting | Lab session (in-person) or remote (participant's own device, standardised model) |
| Session duration | ~60 minutes |
| Target N | 32 (justification: §6) |

**Condition order** is counterbalanced using a balanced Latin square (A→B, B→A across participants). A 10-minute washout activity (unrelated digital reading task) separates the two form-filling sessions to reduce carry-over.

---

## 3. Participants

### 3.1 Inclusion Criteria

- Age 18–65
- Own and regularly use an Android smartphone (daily use ≥ 6 months)
- Normal or corrected-to-normal vision
- No known vibrotactile hypersensitivity or chronic hand tremor
- No significant prior experience with haptic UI design (not a haptic researcher/engineer)
- Self-reported smartphone proficiency ≥ 3 on a 5-point scale

### 3.2 Exclusion Criteria

- Habitually keep smartphone on silent/vibration-off mode (screened via pre-study questionnaire)
- Hearing impairment (audio alerts used as a baseline control — participants should hear them even if haptic is the focus)
- Participating in a concurrent HCI study at the same lab

### 3.3 Recruitment

- University participant pool and social media postings
- Purposive stratification on age (18–35 / 36–65, 16 per stratum) and gender (balance where possible)
- Compensation: $15 gift card or equivalent course credit

---

## 4. Apparatus

### 4.1 Device

- **Model:** Google Pixel 8 (or 8a) running Android 14
  - Linear Resonant Actuator (LRA); VibrationEffect API available
  - Standardised screen size (6.2"), display brightness locked at 300 nits
- All participants use **the same physical device** (lab provision) to eliminate hardware-level confounds
- Device held in portrait mode in participant's preferred hand; a standardised foam grip accessory normalises grip

### 4.2 Prototype Application

- Platform: Android native (Kotlin + Jetpack Compose)
- Form scenario: "New User Account + Shipping Address" registration form
- Fields (12 total):

| # | Field | Type | Validation rule |
|---|-------|------|-----------------|
| 1 | First name | Text | Non-empty, letters only |
| 2 | Last name | Text | Non-empty, letters only |
| 3 | Email address | Text (email keyboard) | Valid email format |
| 4 | Password | Text (masked) | ≥ 8 chars, ≥ 1 digit |
| 5 | Confirm password | Text (masked) | Must match field 4 |
| 6 | Date of birth | Date picker | Age ≥ 18 |
| 7 | Phone number | Numeric | 10–15 digits, optional country code |
| 8 | Street address | Text | Non-empty |
| 9 | City | Text | Non-empty |
| 10 | State/Province | Dropdown | Selection required |
| 11 | ZIP / Postal code | Numeric | Format: ##### or #####-#### |
| 12 | Submit button | — | All fields valid |

- **Seeded errors:** The task instructions contain deliberate mistakes (e.g., a date of birth that makes age 17, a mismatched password hint) to elicit inline validation events and test the haptic error signal.

### 4.3 Haptic Event Taxonomy

Implemented using Android `VibrationEffect.createWaveform()`:

| Event | Trigger | Waveform description | Duration |
|-------|---------|---------------------|----------|
| FIELD_FOCUS | User taps any input field | Single soft pulse (amplitude 80/255) | 20 ms |
| INLINE_ERROR | Field loses focus with invalid input | Double sharp pulse (amplitude 220/255, gap 50 ms) | 120 ms |
| INLINE_SUCCESS | Field loses focus with valid input | Single smooth rise-fall (amplitude 160/255) | 60 ms |
| FIELD_COMPLETE | Last field in a logical group confirmed valid | Triple light pulse (amplitude 120/255) | 200 ms |
| SUBMIT_SUCCESS | Form successfully submitted | Long smooth crescendo (amplitude 200/255) | 400 ms |
| SUBMIT_FAIL | Submit attempted with remaining errors | Rapid double-buzz (amplitude 255/255) | 200 ms |

In the CONTROL condition, `VibrationEffect` calls are suppressed entirely; all other UI elements (visual inline validation messages, button states) are identical.

### 4.4 Logging

The app logs (with millisecond timestamps):
- Field focus events (field ID, timestamp)
- Field blur events (field ID, validation state, timestamp)
- Field re-entries (field ID, entry count)
- Keystrokes (count only, no content)
- Submit attempts (success/fail, timestamp)
- Task completion timestamp

Logs written to a local SQLite DB; exported as CSV after each session.

---

## 5. Procedure

### 5.1 Pre-Session (≈10 min)

1. Welcome, consent form signing
2. **Pre-study questionnaire:**
   - Demographics (age, gender, handedness)
   - Smartphone usage frequency and proficiency
   - Haptic sensitivity: "How often do you notice your phone's vibration alerts?" (5-point Likert)
   - Habitual vibration settings (always on / situational / always off)
3. Technology familiarisation: participant holds the device and performs two unrelated tasks (open camera, send a test message) to normalise comfort
4. Training trial: complete a 4-field practice form (not used in analysis) in a randomised warm-up condition — ensures task comprehension without condition priming

### 5.2 Session Block 1 — Condition A (≈15 min)

1. Experimenter loads Condition A (counterbalanced: HAPTIC or CONTROL)
2. Task instruction card presented (printed): "Please complete the registration form as accurately and quickly as possible. Fill in all fields with the information on this card." (A standardised fictional profile card provides all required values.)
3. Three form completion trials (with the same form reset between trials):
   - Trial 1: familiarisation (not included in primary analysis)
   - Trial 2 and Trial 3: primary data trials
4. Post-block questionnaires:
   - SUS (10 items)
   - NASA-TLX (6 subscales; abbreviated paper version)
   - Confidence scale (3 custom items: "I felt sure I was filling in the form correctly", "I felt in control of the process", "I would trust this interface with real personal data" — 7-point Likert each)
   - Open-ended: "Describe anything notable about the experience of filling in that form."

### 5.3 Washout Activity (≈10 min)

- Participant reads a neutral 600-word article on a separate tablet (no form interaction) to reduce condition carry-over.

### 5.4 Session Block 2 — Condition B (≈15 min)

- Mirror of Block 1 with the alternate condition.
- Identical fictional profile card (different values to prevent pure memorisation).
- Post-block questionnaires identical.

### 5.5 Post-Session (≈10 min)

1. **Comparative preference questionnaire:**
   - "Which version did you prefer overall?" (binary + reasoning)
   - "Which version felt more trustworthy?" (binary + reasoning)
   - "Were you aware of the vibration feedback?" (open)
   - "Did the vibration cues help, hinder, or make no difference?" (3-point + explain)
2. Semi-structured debrief interview (5 min): qualitative probes on specific haptic events noticed, perceived value, scenarios where they would/would not want haptic cues
3. Debriefing, compensation

---

## 6. Power Analysis

Based on Hoggan et al. (CHI 2008), who reported a Cohen's d ≈ 0.60 for error reduction in a haptic vs. no-haptic touchscreen task. Given:

- α = 0.05 (two-tailed)
- 1 – β = 0.80
- Repeated-measures correlation estimated at r = 0.50 (conservative for within-subjects form task)
- Adjusted effect size f = 0.30 (ANOVA equivalent)

Using G*Power 3.1 for repeated-measures ANOVA (2 conditions, 1 group):

**Required N = 28.** Planned **N = 32** to account for approximately 10–15% dropout and exclusion after screening.

---

## 7. Measures

### 7.1 Primary Dependent Variables

| Variable | Operationalisation | Collection |
|----------|--------------------|------------|
| Task completion time (TCT) | Seconds from first field focus to successful submit | App log |
| Field re-entry count (FRC) | Number of times a field is re-entered after first blur | App log |
| Submission attempt count (SAC) | Number of submit-button presses per trial | App log |

### 7.2 Secondary Dependent Variables

| Variable | Instrument | Scale |
|----------|-----------|-------|
| Perceived usability | SUS | 0–100 |
| Mental demand / frustration | NASA-TLX (frustration + mental demand subscales) | 0–100 each |
| Task confidence | Custom 3-item scale (Cronbach α target ≥ 0.70) | 7-point Likert |
| Haptic preference | Post-session comparative questionnaire | Binary + qualitative |

### 7.3 Moderators (RQ4)

| Variable | Measurement |
|----------|-------------|
| Age | Continuous (years) |
| Smartphone proficiency | 5-point Likert |
| Haptic sensitivity | 5-point Likert (pre-study) |

---

## 8. Analysis Plan

### 8.1 Primary Analysis

- **TCT and FRC:** Paired-samples t-test (or Wilcoxon signed-rank if normality violated; checked via Shapiro-Wilk). Report mean difference, 95% CI, effect size (Cohen's d).
- **SAC:** Same approach.

### 8.2 Secondary Analysis

- **SUS, NASA-TLX, Confidence:** Paired t-tests / Wilcoxon per subscale; apply Bonferroni correction for 5 questionnaire outcomes (α_adj = 0.01).

### 8.3 Moderation Analysis (RQ4)

- Linear mixed model with condition × moderator interaction term; participant as random effect.
- Report interaction β, SE, t, p for each moderator.

### 8.4 Qualitative Analysis

- Debrief interview transcripts: thematic analysis (reflexive thematic analysis, Braun & Clarke 2022).
- Post-block open responses: inductive coding; two coders, Cohen's κ ≥ 0.70 target.

### 8.5 Order Effects

- Include condition order as a covariate in all models; report whether order × condition interaction is significant.

---

## 9. Ethics and Data Management

| Concern | Mitigation |
|---------|-----------|
| Informed consent | Written consent before any data collection; right to withdraw at any time |
| Data pseudonymisation | Participant IDs only; no names in logs or analysis files |
| Haptic discomfort | Participants explicitly told they can opt out of haptic condition at any time; any discomfort prompts immediate session pause |
| Data storage | Encrypted local drive; delete raw logs 5 years post-publication |
| IRB/Ethics | Full application to institutional ethics board required before recruitment |

---

## 10. Timeline

| Milestone | Target |
|-----------|--------|
| Ethics approval | +4 weeks |
| Prototype development complete | +6 weeks |
| Pilot testing (N = 4) | +7 weeks |
| Pilot revisions | +8 weeks |
| Full data collection | +12 weeks |
| Data cleaning and analysis | +14 weeks |
| Draft paper | +18 weeks |

---

## 11. Risks and Mitigations

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| LRA intensity feels too subtle for some participants | Medium | Pilot test and calibrate waveform amplitude; offer a perceptual threshold check at session start |
| Participants detect condition assignment and adjust behaviour | Low | Counterbalancing; pre-task briefing does not label conditions as "haptic" vs. "no haptic" |
| Ceiling effect on simple form tasks | Low | Seeded errors ensure not all trials complete without at least one re-entry event |
| Prototype bugs affect logged timestamps | Medium | Log unit tests; manual verification on 10% of sessions |
| Low recruitment of 36–65 age group | Medium | Dedicated outreach to community organisations; higher incentive tier |

---

## 12. Expected Outputs

1. **Empirical dataset** (anonymised app logs + questionnaire CSVs): shared as OSF supplementary material
2. **CHI paper** (target 10 pages ACM double-column): Introduction, Related Work, Study Design, Results, Discussion, Design Guidelines
3. **Design guidelines document** (3–5 practitioner-facing rules for haptic form UIs)
4. **Open-source prototype** (GitHub, MIT license): the Android app stripped of participant data

---

*Stage: Mid/study — complete. Next stage: Mid/deployment.*
