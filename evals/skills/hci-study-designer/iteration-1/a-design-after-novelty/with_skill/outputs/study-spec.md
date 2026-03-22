# Study Specification
**Topic:** Effect of LLM-based tools on literature review efficiency among HCI students
**Novelty gate status:** PASSED — proceed to full study design
**Spec version:** 1.0
**Date:** 2026-03-22

---

## 1. Research Question

**Primary RQ:**
Does using an LLM-based literature review tool (e.g., a ChatGPT-style interface, Elicit, or Semantic Scholar AI) reduce the time and cognitive effort required for HCI graduate students to complete a literature review task, compared to completing the same task with conventional tools (Google Scholar + manual reading)?

**Secondary RQs:**
- RQ2: Does LLM tool use affect the perceived quality and coverage of the resulting literature review (as judged by the student and by expert raters)?
- RQ3: What interaction patterns and workarounds do students develop when using LLM tools for literature search and synthesis?
- RQ4: How does self-reported trust in LLM-generated summaries change over the course of the task?

---

## 2. Study Type Choice and Rationale

**Chosen design:** Within-subjects controlled experiment with interaction logging + post-task questionnaire (mixed methods)

### Rationale

The primary claim is about **system effectiveness** (efficiency — time, cognitive load) and **behavioral process** (interaction patterns, workarounds). This requires:

| Evidence needed | Method |
|---|---|
| Time-on-task, task completion | Controlled experiment with timed tasks |
| Cognitive load | NASA-TLX scale (post-task self-report) |
| Perceived quality and coverage | Expert blind rating of outputs + self-report |
| Interaction patterns | Screen recording + think-aloud (subset) |
| Trust dynamics | In-task probes + post-task scale |
| Attitudes and experience | Post-study questionnaire |

A pure survey would miss behavioral measures. A prototype evaluation of a single custom tool would limit generalizability. A **controlled experiment comparing LLM-assisted vs. conventional search** on a standardized task anchors the efficiency claim in observable behavior, while the questionnaire captures the attitudinal and experiential dimensions. Mixed methods is appropriate per the skill workflow rule: "claims requiring both behavioral and attitudinal evidence → mixed methods."

**Counter-argument considered:** A diary study over a full semester would capture authentic review behavior, but the confounds (topic difficulty, prior knowledge, motivation) are too severe for an initial efficacy claim. A controlled task is the right choice for iteration 1.

---

## 3. Study Design Details

### 3.1 Design

- **Design:** 2 (condition) × within-subjects, counterbalanced order
- **Conditions:**
  - **LLM condition:** participant uses a designated LLM tool (Elicit or a standard ChatGPT-4o interface — to be fixed before IRB submission) alongside a browser
  - **Conventional condition:** participant uses Google Scholar + browser only; LLM tools blocked via study browser profile
- **Task:** A standardized literature review sprint — find and synthesize 8–10 relevant papers on a given HCI sub-topic within 30 minutes, producing a short (≤ 300 words) written synthesis
- **Two topic sets** (matched for difficulty by pilot) are assigned in counterbalanced order to avoid topic learning effects
- **Primary outcome:** Time to produce an accepted synthesis (capped at 30 min); secondary outcomes as listed below

### 3.2 Task Materials

- **Topic Set A:** "Gesture-based interaction in automotive UIs"
- **Topic Set B:** "Haptic feedback in mobile health applications"
- Topics chosen to be within HCI but sufficiently niche that participants are unlikely to have prior knowledge; verified by pilot screening question
- Each topic accompanied by a one-sentence framing prompt given identically in both conditions

### 3.3 Procedure

1. Consent and screener (online, 5 min)
2. Onboarding call / video (10 min): explain task, tools available per condition, timer display
3. **Session 1 — Condition A** (50 min total)
   - Warm-up: free exploration of assigned tool, no task (5 min)
   - Timed literature review task on Topic Set X (30 min)
   - Post-task measures: NASA-TLX, perceived coverage, trust scale, open text (10 min)
   - Brief break + optional rest (5 min)
4. **Session 2 — Condition B** (≥ 48 hours later to reduce fatigue; same session structure, Topic Set Y)
5. Post-study questionnaire (10 min): overall preference, experience, demographics
6. Debrief and compensation

Sessions are conducted remotely via Zoom with screen share enabled. Screen recordings are kept for interaction log analysis. Think-aloud is encouraged but not required.

---

## 4. Participants

### 4.1 Target Population

HCI graduate students (Master's or PhD) currently enrolled in an HCI, CSCW, or interaction design program.

### 4.2 Inclusion Criteria

- Currently enrolled in an HCI-adjacent graduate program (self-report, verified by email domain or program name)
- Has completed at least one literature review as part of coursework or research
- Comfortable reading academic papers in English
- Has used Google Scholar at least once in the past 6 months
- Has access to a laptop/desktop with stable internet and a camera (for screen share)

### 4.3 Exclusion Criteria

- Has published a paper specifically on gesture-based automotive UIs **or** haptic feedback in mobile health (would compromise topic novelty)
- Currently employed in a role where LLM literature review tools are used daily (would create large skill gap vs. novice participants)
- Unable to complete two sessions within a 2-week window

### 4.4 Recruitment

- **Primary channel:** HCI course mailing lists and Slack workspaces at participating universities (PI's institution plus 1–2 partner sites)
- **Secondary channel:** Call for participants posted to CHI-ANNOUNCE and relevant HCI subreddits
- **Screener:** Online form (see survey-draft.md)
- **Compensation:** $20 USD Amazon gift card per session ($40 total) or equivalent local currency

### 4.5 Expected N

- **Target N:** 24 participants (12 per counterbalancing order)
- **Power basis:** Time-on-task effect sizes in comparable tool comparison studies range from d = 0.5–0.8. For d = 0.6, α = 0.05, power = 0.80, within-subjects design, N ≈ 20 is sufficient. We target 24 to account for ~15–20% attrition.
- **Minimum viable N for analysis:** 16 participants with complete data in both conditions

---

## 5. Stop Criteria

Stop criteria define when to pause or halt data collection before the target N is reached.

| Trigger | Action |
|---|---|
| **Technical failure rate > 25%** — more than 25% of completed sessions have corrupted screen recordings or missing task output | Pause collection; fix logging pipeline; review affected sessions manually |
| **Attrition rate > 30%** between Session 1 and Session 2 | Pause collection; investigate dropout cause via brief email survey; adjust session gap or compensation if needed |
| **Adverse event** — any participant reports significant distress, privacy concern about recording, or data breach suspicion | Halt immediately; notify IRB; do not collect further data until reviewed |
| **Systematic carryover effect detected** in pilot — performance in Session 2 is uniformly better regardless of condition (suggesting topic learning rather than tool effect) | Redesign task before main collection; do not launch production run |
| **Ceiling effect detected** in pilot — > 80% of participants in conventional condition also complete the task in < 20 min | Increase task difficulty or duration before main collection |
| **N = 24 complete pairs reached** | Normal stop: proceed to analysis |
| **N = 36 attempted** with < 16 complete pairs | Hard stop: declare data insufficient; report as pilot study; publish lessons learned |

---

## 6. Primary Measures

| Measure | Type | Instrument | Timing |
|---|---|---|---|
| Time-on-task | Behavioral | Timer log (task start/submit timestamps) | Per session |
| Number of sources consulted | Behavioral | Screen recording coding | Per session |
| Synthesis quality | Expert rating (blind, 2 raters) | 5-point rubric (coverage, accuracy, coherence) | Post-collection |
| Cognitive load | Self-report | NASA-TLX (6 subscales) | Post-task |
| Perceived coverage | Self-report | 3 custom 7-point items | Post-task |
| Trust in LLM output | Self-report | 4-item adapted Komiak & Benbasat (2006) trust scale | Post-task (LLM condition only) |
| Tool preference | Self-report | Forced-choice + free text | Post-study |
| Prior LLM experience | Self-report | 3-item screener + 1 frequency item | Screener |

---

## 7. Analysis Plan

- **Primary analysis:** Paired t-test (or Wilcoxon signed-rank if normality violated) on time-on-task: LLM vs. conventional condition
- **Secondary:** Mixed ANOVA for NASA-TLX subscales (condition × order); inter-rater reliability (Cohen's κ) for quality ratings; thematic analysis of think-aloud and open text
- **Minimum reporting:** Effect size (Cohen's d) and 95% CI for all comparisons; N per condition, attrition reasons, exclusions
- **Pre-registration:** OSF pre-registration before Session 1 data collection begins

---

## 8. Ethical Considerations

- IRB approval required before recruitment
- Screen recordings contain potentially identifiable behavior; stored encrypted, deleted after coding
- Participants may withdraw at any time without penalty; partial compensation for single session
- Deception: none — full task purpose disclosed
- See consent.md for full data handling statement
