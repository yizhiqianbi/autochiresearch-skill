# Pilot Study Checklist
**Study:** LLM Tools and Literature Review Efficiency in HCI Graduate Students
**Pilot target:** 4 participants (2 per counterbalancing order) — NOT included in main analysis
**Pilot completion deadline:** Before IRB production-run launch
**Version:** 1.0
**Date:** 2026-03-22

---

## Purpose of the Pilot

The pilot run serves four functions:
1. **Technical validation** — confirm recording, logging, and platform pipelines work end-to-end
2. **Task calibration** — verify that task difficulty and timing are appropriate
3. **Instrument validation** — check survey clarity, scale reliability, and attention check placement
4. **Stop criteria calibration** — observe whether any of the pre-defined stop conditions are already triggered

Do not launch production data collection until all checklist items below are marked PASS.

---

## Section 1 — Pre-Pilot Preparation

### 1.1 Materials Ready

- [ ] Screener form published and tested in Qualtrics (or equivalent) — confirm branching logic works for all disqualification paths
- [ ] Consent form reviewed by IRB (or submitted pending review) — confirmed IRB protocol number is present
- [ ] Post-task survey (Session 1 and Session 2 versions) published and tested — confirm NASA-TLX sliders, Likert scales, and open-text boxes render correctly on both desktop and mobile
- [ ] Post-study questionnaire and demographics form published and tested
- [ ] Debrief screen text confirmed — verify it appears only after Session 2 demographics submission
- [ ] Task prompt documents for Topic Set A and Topic Set B finalized (printed as PDF for screen sharing)
- [ ] Counterbalancing assignment table prepared (random, 2 orders × 2 topic assignments)
- [ ] Compensation process tested — verify gift card delivery pipeline works before pilot begins

### 1.2 Technical Infrastructure

- [ ] Screen recording setup confirmed: Zoom cloud recording OR Camtasia local capture — choose one and document which
- [ ] Recording consent reminder slide confirmed in Zoom waiting room or session start screen
- [ ] Timestamp logging confirmed: task start and task submit buttons log UTC timestamps to a Google Sheet or database — test with a dummy session
- [ ] LLM tool access confirmed: participant-facing Elicit or ChatGPT-4o link tested; confirm it does not require participants to create an account (use a study-provisioned shared session link if needed)
- [ ] Conventional condition browser profile prepared: Chrome profile with all LLM-related extensions and bookmarks removed; tested that chatgpt.com, elicit.com, consensus.app, and perplexity.ai are blocked
- [ ] File upload path confirmed: where do participants submit their written synthesis? (Google Form, shared folder link, or Qualtrics text entry) — test submission-to-researcher pipeline
- [ ] Backup plan documented: what happens if Zoom crashes mid-task? (answer before pilot: reschedule with full compensation, or resume from timer pause)

### 1.3 Team Readiness

- [ ] All researchers who will run sessions have completed one dry-run session with each other as mock participant and facilitator
- [ ] Session script finalized and reviewed by at least one team member not involved in drafting
- [ ] IRB-required data access agreements signed by all team members who will view screen recordings
- [ ] Data storage folder structure created on institutional encrypted server; access permissions confirmed

---

## Section 2 — During Each Pilot Session

*Run all 4 pilot sessions before reviewing results. Do not adjust task or instruments mid-pilot unless a session-blocking technical failure occurs.*

### 2.1 Pre-Task (per session)

- [ ] Participant arrived on time and Zoom link is working
- [ ] Consent confirmed verbally ("Did you complete and submit the consent form? Do you have any questions before we begin?")
- [ ] Recording started and confirmed active (participant can see recording indicator)
- [ ] Participant confirmed: personal browser tabs closed; only study browser profile open
- [ ] Task prompt document shared on screen — participant confirms they can read it
- [ ] Warm-up period timer started (5 min) — participant explores the assigned tool freely
- [ ] Any technical issues during warm-up noted: _______________

### 2.2 During Task (per session)

- [ ] Task timer started and visible to participant (shared screen or verbal countdown at 10 min remaining and 5 min remaining)
- [ ] Participant reminded of think-aloud (encouraged, not required): "Feel free to narrate your thinking as you work"
- [ ] Facilitator does not answer content questions during the task (script: "I can't answer that during the task, but note it and I'll explain after")
- [ ] Any technical interruptions noted with timestamp: _______________
- [ ] Task submit event logged (timestamp confirmed in log): _______________
- [ ] If 30-min cap reached and participant has not submitted — note: participant submitted? [ ] Yes / [ ] No (partial completion)

### 2.3 Post-Task (per session)

- [ ] Post-task survey link sent in Zoom chat; participant confirms they can open it
- [ ] Participant completes survey without facilitator visible (facilitator camera off or waiting room)
- [ ] Survey submission confirmed (Qualtrics response ID noted): _______________
- [ ] Brief debrief check-in: "Any confusion about the survey questions? Any technical issues I should know about?"
- [ ] Notes from check-in: _______________

---

## Section 3 — Post-Pilot Analysis (after all 4 sessions)

Complete this section before making any go/no-go decision on main collection.

### 3.1 Task Calibration

- [ ] **Timing check:** Did all 4 participants submit within the 30-min window?
  - If 3 or more ran out of time: task is too long or too hard — revise task scope before main collection
  - If all 4 submitted in under 15 min: task is too easy — increase scope or topic difficulty
  - Target: 15–28 min to submit; ceiling at 30 min acceptable for ≤ 1 participant per condition
- [ ] **Topic difficulty match:** Were Topic Set A and Topic Set B similarly difficult?
  - Check: mean time-on-task per topic set across pilot participants
  - If difference > 5 min: replace the harder topic or adjust task framing
- [ ] **Topic novelty confirmed:** No pilot participant reported prior familiarity with their assigned topic (screener item S7 was not sufficient — confirm verbally)

### 3.2 Instrument Quality

- [ ] **NASA-TLX:** All 6 subscale sliders recorded responses; no missing values across 4 pilot sessions
- [ ] **Perceived Coverage (PC1–PC3):** Pilot inter-item correlation > 0.4 — confirm internal consistency direction makes sense
- [ ] **Trust Scale (TR1–TR4):** Cronbach's α ≥ 0.70 across 4 LLM-condition responses; if below threshold, flag TR3 (reverse-worded) for revision
- [ ] **Attention Check 1 (AC1):** All 4 pilot participants passed; if any failed — review item wording and placement
- [ ] **Attention Check 2 (AC2):** All 4 pilot participants passed; same review if not
- [ ] **Survey completion time:** Post-task survey completed in ≤ 12 min by all 4 participants; if longer, shorten open-text instructions or remove one section
- [ ] **No comprehension issues flagged** in post-session check-in for any survey item; if yes, list items to revise: _______________

### 3.3 Technical Pipeline

- [ ] All 4 screen recordings successfully saved and accessible by research team
- [ ] All 4 timestamp logs contain both task-start and task-submit events
- [ ] All 4 synthesis documents received and stored in correct participant folders
- [ ] LLM tool access worked for all participants in LLM condition (no login friction, no rate-limit errors)
- [ ] Conventional condition browser profile successfully blocked LLM tools (verify by checking browser history in recording)
- [ ] Qualtrics data export confirmed: all survey responses linked to correct participant IDs

### 3.4 Stop Criteria Pre-Check

- [ ] Technical failure rate in pilot: _____ / 4 sessions had significant technical failures
  - If > 1 failure: fix pipeline before main collection; do not proceed
- [ ] Carryover effect check: is Session 2 performance uniformly faster than Session 1 regardless of condition?
  - If yes for 3+ pilot participants: increase session gap (currently 48 h) or change topic sets before main collection
- [ ] Ceiling effect check: did any pilot participant in the conventional condition complete the task in < 15 min?
  - If yes for 2+ participants: task difficulty revision needed

---

## Section 4 — Go / No-Go Decision

Complete this after reviewing all Section 3 items.

| Gate | Status | Notes |
|---|---|---|
| All materials and tech pipelines confirmed working | PASS / FAIL / PARTIAL | |
| Task timing is in acceptable range (15–28 min for most) | PASS / FAIL | |
| Topic Sets A and B are balanced in difficulty | PASS / FAIL | |
| All survey instruments clear and complete | PASS / FAIL | |
| No stop criteria triggered in pilot | PASS / FAIL | |
| IRB production approval confirmed | PASS / FAIL / PENDING | |
| OSF pre-registration submitted | PASS / FAIL / PENDING | |

**Overall decision:**
- [ ] **GO** — all gates PASS; proceed to main data collection
- [ ] **CONDITIONAL GO** — minor items remaining (list below); may begin main collection while resolving
- [ ] **NO GO** — one or more critical gates FAILED; revise and re-pilot before main collection

Conditional GO items outstanding:
1. _______________
2. _______________

Decision made by: _______________ Date: _______________

---

## Section 5 — Pilot Participant Debrief Notes

*For each pilot participant, record any verbal feedback or observations that may improve the main study.*

| Participant | Session 1 tool | Session 2 tool | Key feedback |
|---|---|---|---|
| P01 | | | |
| P02 | | | |
| P03 | | | |
| P04 | | | |

---

## Appendix — Session Script (Facilitator Reference)

**Session opening (read verbatim or close paraphrase):**

> "Hi [NAME], thanks for joining. Before we start, I want to confirm a few things. Did you have a chance to review and submit the consent form? [Confirm yes.] Great. Today's session will take about 50 minutes. You'll complete a literature review task using [TOOL NAME / Google Scholar — depending on condition]. I'll show you a task prompt on screen. You'll have 30 minutes to find relevant papers and write a short synthesis — about 200–300 words. There are no right or wrong papers to find; we're interested in how you work, not in testing your knowledge. I'll start the screen recording now. [Start recording.] You can see the recording indicator at the top of the Zoom window. Please make sure your personal browser tabs are closed and only the study browser profile is open. Any questions before we begin the 5-minute warm-up?"

**At warm-up end:**

> "Great, the 5 minutes are up. Here's the task prompt. [Share PDF / screen.] Your 30-minute timer starts now."

**At 10 minutes remaining:**

> "Just a heads-up — you have 10 minutes remaining."

**At 5 minutes remaining:**

> "Five minutes left."

**At time limit:**

> "Time is up. Please submit whatever you have — even if it feels incomplete. [Send survey link.] Now please complete this short questionnaire. I'll step away while you do — just message me in the chat when you're done."

**After survey:**

> "Thank you. Before we wrap up — were there any questions in the survey that were confusing, or any technical issues I should know about?"

*[Note responses. If Session 2: run debrief text from survey-draft.md Section 5.]*
