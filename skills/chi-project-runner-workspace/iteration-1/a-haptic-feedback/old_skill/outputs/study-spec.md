# Study Specification
## Project: Haptic Feedback UI for Mobile Form-Filling Experience

**Phase:** Mid — Study
**Date:** 2026-03-22
**Novelty Gate:** PASSED (see keep-or-pivot-decision.md)

---

## 1. Study Overview

This document specifies the full controlled experiment to investigate how differentiated haptic feedback in a mobile form UI affects task completion time, error rate, abandonment rate, perceived usability, and cognitive load.

### 1.1 Study Type

- **Design:** Controlled within-subjects experiment
- **Modality:** In-lab (controlled environment)
- **Platform:** Native iOS prototype app (Swift/SwiftUI) running on standardized test devices
- **Deliverable:** Empirical paper + haptic design guidelines

---

## 2. Research Questions and Hypotheses

### RQ1 (Primary)
Does a haptic feedback layer integrated into a mobile form UI reduce task completion time and error rate compared to a no-haptic baseline?

- **H1a:** Task completion time will be significantly lower in the Differentiated Haptic condition than in the Control condition.
- **H1b:** Error rate will be significantly lower in the Differentiated Haptic condition than in the Control condition.
- **H1c:** Basic Haptic will show intermediate results between Control and Differentiated Haptic on both DVs.

### RQ2 (Secondary)
Does the haptic feedback layer influence perceived usability and subjective satisfaction?

- **H2a:** SUS scores will be significantly higher in both haptic conditions (BH, DH) than in Control.
- **H2b:** NASA-TLX scores will be significantly lower in the DH condition than Control.

### RQ3 (Exploratory)
Which specific form events benefit most from haptic augmentation?

- No directed hypothesis; explored via post-study semi-structured interview and event-level log analysis.

---

## 3. Study Design

### 3.1 Independent Variable

**Haptic Feedback Condition** (3 levels, within-subjects):

| Condition | Code | Description |
|-----------|------|-------------|
| Control | C | Standard form UI, no haptic feedback |
| Basic Haptic | BH | Single 50ms vibration pulse on all haptic events |
| Differentiated Haptic | DH | Distinct vibration patterns per event type (see §3.3) |

### 3.2 Dependent Variables

| DV | Measurement Method | Primary/Secondary |
|----|-------------------|-------------------|
| Task completion time | Logged automatically (ms, from form first field focus to submission success) | Primary |
| Error rate | Count of validation-failed field submissions per session | Primary |
| Abandonment rate | Boolean: did participant close/restart the form before completion? | Primary |
| Perceived usability | System Usability Scale (SUS, 10 items, Brooke 1996) | Secondary |
| Cognitive load | NASA Task Load Index (NASA-TLX, 6 subscales, Hart & Staveland 1988) | Secondary |
| Preference | Post-condition ranking (1=most preferred, 3=least preferred) | Secondary |
| Think-aloud qualitative notes | Video + audio transcription | Exploratory |

### 3.3 Haptic Pattern Vocabulary (Differentiated Haptic condition)

All patterns implemented via iOS `UIImpactFeedbackGenerator` and `UINotificationFeedbackGenerator` APIs.

| Form Event | Pattern Name | Pattern Description | iOS API Call |
|------------|-------------|---------------------|--------------|
| Field focus (tap to activate) | Focus Tap | Single light tap, 20ms | `UIImpactFeedbackGenerator(.light)` |
| Inline validation — success | Success Pulse | Two soft pulses, 30ms each, 50ms gap | `UINotificationFeedbackGenerator(.success)` |
| Inline validation — error | Error Buzz | Three sharp pulses, 40ms each, 30ms gap | `UINotificationFeedbackGenerator(.error)` |
| Form submission — success | Completion Thud | Single heavy long pulse, 80ms | `UIImpactFeedbackGenerator(.heavy)` |
| Form submission — error | Warning Rumble | Two medium pulses + one sharp, 40ms-40ms-60ms | `UINotificationFeedbackGenerator(.warning)` |

**Pilot discrimination test:** Before the main study, a 5-participant pilot will verify that all 5 patterns are distinguishable at ≥80% accuracy using a 5-alternative forced-choice task. Patterns will be revised if discrimination falls below threshold.

### 3.4 Counterbalancing

Latin square counterbalancing across the 3 conditions. With N=36 participants, 12 participants will complete each order permutation (6 possible orders × 6 participants each).

**Order matrix:**

| Group | Session 1 | Session 2 | Session 3 |
|-------|-----------|-----------|-----------|
| G1 | C | BH | DH |
| G2 | C | DH | BH |
| G3 | BH | C | DH |
| G4 | BH | DH | C |
| G5 | DH | C | BH |
| G6 | DH | BH | C |

Each group N=6. Total N=36.

---

## 4. Participants

### 4.1 Sample Size and Power Analysis

- **Effect size target:** Cohen's d = 0.5 (medium effect; conservative given prior haptic keyboard work showed d=0.6–0.8)
- **Power:** 1 − β = 0.80
- **Alpha:** α = 0.05 (two-tailed)
- **Design correction:** Within-subjects with 3 conditions; using repeated-measures ANOVA formula
- **Required N:** 27 (per G*Power 3.1 calculation for repeated-measures ANOVA, f=0.25, 3 groups)
- **Target recruitment:** N=36 (includes ~25% attrition buffer and enables full Latin square)

### 4.2 Inclusion Criteria

- Age 18–65
- Own and daily-use a smartphone (iOS or Android; standardized devices provided for the study)
- Experience filling out online forms on a smartphone (self-reported, ≥2× per month)
- Normal or corrected-to-normal vision
- No motor impairments affecting touch-based smartphone use
- Fluent in the study language (Mandarin Chinese or English; study materials provided in both)

### 4.3 Exclusion Criteria

- Hearing impairment (not a study requirement, but noted for think-aloud protocol)
- Prior participation in haptic feedback studies in the past 6 months (avoids demand characteristics)
- Participants who work in UX/HCI research (to reduce experimenter bias)

### 4.4 Recruitment

- University participant pool (SONA system or equivalent)
- Compensation: CNY 80 / USD 12 per session (approximately 60–75 minutes total)
- Recruitment target: 40 participants to ensure 36 completions

---

## 5. Apparatus

### 5.1 Test Devices

| Device | OS | Haptic Engine | Role |
|--------|-----|---------------|------|
| iPhone 14 (×2) | iOS 17 | Taptic Engine (LRA) | Primary test device |
| Google Pixel 7 (×1) | Android 13 | LRA + amplitude API | Secondary (cross-device check) |

All devices mounted on a standard smartphone holder at 30° angle on a table. Participants may hold the device naturally if preferred.

### 5.2 Prototype Application

**Platform:** Native iOS (Swift 5.9 / SwiftUI 5)

**Form Task:** A realistic 3-page mobile registration/profile-setup form with the following fields:

*Page 1 — Personal Info (6 fields):*
1. First name (text, required)
2. Last name (text, required)
3. Email address (text, required; validated: format check)
4. Date of birth (date picker, required; validated: age ≥ 18)
5. Phone number (text, required; validated: format check)
6. Gender (segmented control, optional)

*Page 2 — Account Setup (5 fields):*
7. Username (text, required; validated: 4–20 alphanumeric chars, no spaces)
8. Password (secure text, required; validated: ≥8 chars, 1 uppercase, 1 number)
9. Confirm password (secure text, required; validated: matches password)
10. Country (picker, required)
11. Agree to terms (toggle, required)

*Page 3 — Preferences (3 fields):*
12. Notification preference (segmented: Always / Sometimes / Never)
13. Theme preference (segmented: Light / Dark / System)
14. Bio (text area, optional, max 200 chars)

**Total:** 14 fields across 3 pages, 2 navigation steps, 1 submission step.

**Validation rules are identical across all 3 conditions.** The only difference between conditions is the presence and type of haptic feedback.

### 5.3 Logging System

The app logs the following events to a local JSON file per session:

- Session start/end timestamps
- Each field focus event (timestamp, field ID)
- Each field blur event (timestamp, field ID, validation result: pass/fail)
- Each page navigation event (timestamp, from page, to page)
- Each validation error shown (timestamp, field ID, error type)
- Form completion event (timestamp, success/abandoned)
- Total errors per field per session

Logs are exported as JSON after each session and imported to the analysis pipeline.

### 5.4 Questionnaires

Administered on a separate iPad to avoid confounding the test device:
- **SUS (10 items):** Administered after each condition
- **NASA-TLX (6 subscales):** Administered after each condition
- **Condition preference ranking:** Administered after all 3 conditions
- **Post-study semi-structured interview:** 10–15 minutes, audio recorded

---

## 6. Procedure

### 6.1 Session Timeline

| Step | Activity | Duration |
|------|----------|----------|
| 1 | Arrival, informed consent, demographics questionnaire | 10 min |
| 2 | Experimenter introduction + device orientation (no mention of haptic conditions to avoid demand characteristics) | 5 min |
| 3 | Practice trial (a short 4-field practice form, same device, no condition labelling) | 5 min |
| 4 | Condition 1: complete registration form + SUS + NASA-TLX | 15 min |
| 5 | 2-minute break, distractor task (word puzzle) | 2 min |
| 6 | Condition 2: complete registration form + SUS + NASA-TLX | 15 min |
| 7 | 2-minute break, distractor task | 2 min |
| 8 | Condition 3: complete registration form + SUS + NASA-TLX | 15 min |
| 9 | Condition preference ranking + post-study semi-structured interview | 10 min |
| 10 | Debrief (reveal conditions, answer questions) + payment | 5 min |
| **Total** | | **~85 min** |

### 6.2 Experimenter Script (abbreviated)

*Introduction (read verbatim):*
"Welcome. In this study, we're exploring how different versions of a mobile form app affect your experience. You'll complete the same form three times, each time using a slightly different version of the app. Please try to complete the form as naturally as you would on your own phone. Think aloud if you're comfortable doing so — just say what you're thinking as you fill out the form."

*No mention of haptic feedback* until debrief.

### 6.3 Think-Aloud Protocol

Concurrent think-aloud (Ericsson & Simon, 1993). Participants verbalize their thoughts while completing the form. The experimenter only prompts with: "What are you thinking?" if the participant goes silent for more than 20 seconds.

Sessions are video-recorded (front-facing camera on a separate device captures screen interactions + hand movements; audio capture for think-aloud).

### 6.4 Debrief

After all 3 conditions and the interview, the experimenter reveals:
1. The three conditions were Control (no haptic), Basic Haptic (one vibration), and Differentiated Haptic (distinct patterns)
2. The specific haptic patterns used
3. The overall study goals

Participants are given time to ask questions before receiving compensation.

---

## 7. Data Analysis Plan

### 7.1 Primary Statistical Analysis

**Test:** One-way repeated-measures ANOVA for task completion time and error rate (3 conditions × 1 factor within subjects)

- **Assumption checks:** Mauchly's test for sphericity; Greenhouse-Geisser correction if violated
- **Post-hoc tests:** Bonferroni-corrected pairwise comparisons (C vs. BH, C vs. DH, BH vs. DH)
- **Significance threshold:** α = 0.05
- **Effect size:** η² (partial eta squared)

**For abandonment rate:** Cochran's Q test (non-parametric test for related proportions, 3 conditions)

### 7.2 Secondary Statistical Analysis

**SUS scores:** Repeated-measures ANOVA (same procedure as primary DVs)
**NASA-TLX:** Repeated-measures ANOVA on overall TLX score; exploratory repeated-measures MANOVA on 6 subscales

### 7.3 Qualitative Analysis

**Think-aloud and interview data:** Thematic analysis (Braun & Clarke 2006) conducted by two researchers. Inter-rater reliability (Cohen's κ) computed on 20% of transcripts. Target κ ≥ 0.7.

**Event-log analysis (exploratory):** Identify which specific fields generate the most validation errors per condition; correlate with event-level haptic log timestamps to understand temporal dynamics of error recovery.

### 7.4 Software

- **Statistical analysis:** R 4.3+ (packages: `ez`, `emmeans`, `ggplot2`)
- **Qualitative coding:** NVivo or MAXQDA
- **Log processing:** Python 3.11+ (pandas, json)
- **Power analysis:** G*Power 3.1

---

## 8. Ethical Considerations

### 8.1 IRB Requirements

- Full IRB review required (involves human participants, video recording)
- Informed consent covers: video recording, data storage, right to withdraw, compensation

### 8.2 Data Privacy

- All participant data assigned a numeric ID; names removed from analysis files
- Video recordings stored on encrypted local drive; deleted after transcription and qualitative coding
- No sensitive personal data from the registration form is transmitted — the form is a UI prototype with no backend

### 8.3 Participant Welfare

- 2-minute breaks built into session to prevent fatigue
- Participants informed they may stop at any time without penalty
- No deception beyond withholding condition labels until debrief; full debrief provided

---

## 9. Limitations and Threats to Validity

| Threat | Type | Mitigation |
|--------|------|------------|
| Order effects (learning, fatigue) | Internal validity | Within-subjects + full Latin square counterbalancing |
| Device hardware variation | Internal validity | Standardized test devices; device type logged as covariate |
| Demand characteristics (participants guess the study is about haptics) | Internal validity | Verbal introduction avoids mentioning haptics; full debrief after all conditions |
| Sample limited to university students | External validity | Broad age range targeted; demographic diversity in recruitment |
| In-lab setting not representative of real-world mobile use | Ecological validity | Acknowledged in limitations; future work should include field study |
| Single form type (registration form) | Generalizability | Acknowledged; future work: checkout forms, health intake forms |

---

## 10. Deliverables from This Study

| Deliverable | Format | Location |
|-------------|--------|----------|
| iOS prototype app (Swift/SwiftUI) | Xcode project | `studies/prototype/` |
| Session logging module | Swift + Python | `studies/prototype/logger/` |
| Questionnaire instruments (SUS, NASA-TLX) | PDF + paper | `studies/instruments/` |
| Experimenter script | Markdown | `studies/protocol/experimenter-script.md` |
| Consent form | PDF | `studies/protocol/consent-form.pdf` |
| Raw log files (JSON) | Per session | `studies/data/raw/` |
| Processed analysis dataset (CSV) | Aggregated | `analysis/data/study1_processed.csv` |
| R analysis scripts | .R files | `analysis/scripts/` |
| Qualitative codebook | Markdown | `analysis/codebook.md` |
| Study results summary | Markdown | `output/results-summary.md` |

---

## 11. Timeline

| Milestone | Target Date |
|-----------|-------------|
| Prototype development complete | 2026-05-15 |
| Pattern discrimination pilot (N=5) | 2026-05-22 |
| IRB submission | 2026-05-25 |
| IRB approval (estimated) | 2026-06-15 |
| Participant recruitment opens | 2026-06-16 |
| Data collection complete (N=36) | 2026-07-31 |
| Data analysis complete | 2026-08-31 |
| Paper first draft | 2026-10-15 |
| CHI 2027 submission deadline (estimated) | 2026-09-12 |

*Note: CHI 2027 deadline may fall before full analysis. If so, target MobileHCI 2026 short paper with N=20 interim results as first submission.*

---

## 12. Study Spec Sign-off Checklist

- [x] Research questions and hypotheses specified
- [x] IV with all levels defined and operationalized
- [x] All DVs with measurement methods specified
- [x] Haptic pattern vocabulary defined (with pilot discrimination gate)
- [x] Sample size with power analysis documented
- [x] Inclusion/exclusion criteria specified
- [x] Full procedure documented (session timeline + experimenter script)
- [x] Counterbalancing scheme specified
- [x] Data analysis plan (statistical tests + qualitative) documented
- [x] Ethical considerations addressed
- [x] Threats to validity documented
- [x] Device and apparatus specified (local-first, no server required)
- [x] Deliverables and file locations specified
- [x] Timeline specified
