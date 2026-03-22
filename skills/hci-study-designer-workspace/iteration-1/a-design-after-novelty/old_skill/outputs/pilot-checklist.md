# Pilot Checklist

**Study:** LLM Tools and HCI Students' Literature Review Efficiency
**Pilot Target:** 3 participants before full data collection
**Pilot Sign-Off Required By:** PI + at least one co-researcher
**Version:** v0.1

---

## Pre-Pilot Setup Checks

### Materials and Infrastructure

- [ ] Consent form reviewed by IRB and approved (or confirmed exempt)
- [ ] Consent form printed (in-person) or digital signature tool configured (remote)
- [ ] Screener questions loaded and tested in survey platform
- [ ] NASA-TLX instrument loaded and tested (mid-session trigger confirmed)
- [ ] Post-study survey loaded and tested end-to-end; all branching logic verified
- [ ] Attention check items verified to appear in correct positions
- [ ] Debrief script printed / available to facilitator
- [ ] Session timer configured (30-minute task timer clearly visible to facilitator; not shown to participant unless requested)
- [ ] Screen + audio recording software tested and confirmed working (OBS, Zoom, or equivalent)
- [ ] Backup recording method identified (secondary device) in case primary fails
- [ ] LLM tool access confirmed: account created or API key ready; rate limits checked for back-to-back sessions
- [ ] Backup LLM tool identified in case primary is unavailable
- [ ] Unaided condition interface confirmed: Google Scholar + relevant institutional database accessible
- [ ] Gold-standard paper sets completed for both matched topics (minimum 10 papers each, pre-coded as relevant)
- [ ] Relevance coding rubric written and reviewed by both coders
- [ ] Inter-rater reliability calibration round scheduled (at least 10 papers coded independently before pilot)

### Participant Assignment

- [ ] Counterbalancing schedule prepared (AB / BA order assigned to pilot participants)
- [ ] Participant IDs created for pilot slots (P001, P002, P003)
- [ ] Compensation arranged (gift cards purchased or course credit form ready)

---

## During-Pilot Facilitator Checks (Per Session)

### Session Start
- [ ] Participant confirmed eligible via screener before session begins
- [ ] Consent form signed and copy provided to participant
- [ ] Participant briefed: "You'll do two 30-minute tasks. Please think aloud as much as you can, but don't worry about keeping up a running commentary — just narrate when something stands out."
- [ ] Recording started and confirmed active (check indicator light / file size)
- [ ] Participant ID logged in session log

### Training Phase
- [ ] Condition A (LLM) participants: 10-minute tool tutorial delivered; participant asked to confirm they understand the basic query interface
- [ ] Condition B (unaided) participants: 10-minute orientation to database search confirmed
- [ ] Questions from participant answered; any deviations from standard script noted

### Task 1
- [ ] Task 1 topic assigned according to counterbalancing schedule
- [ ] Timer started; start time logged
- [ ] Facilitator observed and noted: time to first citation, number of queries/prompts, visible tool-switching behavior
- [ ] Participant submission received at task end (list of papers + synthesis)
- [ ] End time logged
- [ ] NASA-TLX administered immediately after Task 1

### Task 2
- [ ] Same checks as Task 1 for counterbalanced condition

### Post-Study
- [ ] Post-study survey administered and completed
- [ ] Debrief script read aloud; participant questions noted
- [ ] Participant distress exit check: "On a scale of 1–10, how are you feeling right now?" — log response; if >7, follow distress protocol
- [ ] Compensation provided and receipt obtained (or course credit form signed)
- [ ] Recording stopped and file saved with participant ID filename
- [ ] Session log completed and filed

---

## Post-Pilot Debrief Questions (Facilitator Team Review)

After all 3 pilot sessions, answer the following:

**Timing**
- [ ] Did Task 1 (30 min) allow participants to find ≥3 relevant papers?
  - If <50% found ≥3 papers: adjust task time to 40 min or simplify topic
- [ ] Was the total session within 90–100 minutes?
  - If consistently over 100 min: identify which section to trim

**Task Clarity**
- [ ] Did all participants understand the task goal without needing clarification beyond the standard script?
  - If >1 participant needed extra clarification: revise task instructions
- [ ] Were any topics perceived as too narrow or too broad by participants?
  - Note: ___________________________________________

**Tool Access**
- [ ] Was the LLM tool accessible and stable throughout all 3 pilot sessions?
  - If any outage or rate-limit error: confirm backup tool works; add monitoring step to full-study protocol
- [ ] Did the LLM tool produce any hallucinated (non-existent) paper citations?
  - Count per session: Session 1: ___ Session 2: ___ Session 3: ___
  - If >3 hallucinations per session average: add explicit verification reminder to task instructions

**Survey**
- [ ] Were any survey items flagged as confusing or ambiguous by pilot participants?
  - Items to revise: ___________________________________________
- [ ] Were all required fields completed (no missing data due to survey logic errors)?
- [ ] Did the attention check items perform as expected?
  - AC1 correct responses: ___ / 3
  - AC2 correct responses: ___ / 3

**Coding Reliability**
- [ ] Was inter-rater κ ≥ 0.70 on pilot paper relevance coding?
  - Achieved κ: ___________________________________________
  - If κ < 0.60: schedule rubric revision session before full study

**Ethics and Distress**
- [ ] Did any pilot participant report distress >7/10 on the exit check?
  - If yes: review task framing and consider reducing time pressure cues

---

## Pilot Sign-Off

All items above reviewed. Protocol is cleared for full data collection with the following amendments:

| Amendment | Description |
|-----------|-------------|
| (list any) | |

**PI Signature:** ___________________________________  **Date:** ___________

**Co-Researcher Signature:** ___________________________________  **Date:** ___________

---

## Stop Criteria Reference (from study-spec.md)

The following conditions trigger a halt to data collection at any point:

1. Inter-rater agreement on relevance coding falls below κ = 0.60 after calibration — revise rubric first.
2. Task completion rate <50% in pilot — extend task time to 40 min or simplify topic.
3. Any participant reports distress >7/10 on the exit check — debrief immediately; log incident; do not continue that session.
4. LLM tool inaccessible or rate-limited during sessions — pause; switch to verified backup tool; re-run affected sessions.
5. After first 12 participants, effect size estimate is clearly below d = 0.20 — consult PI on whether to continue or redesign.
6. Any data breach or PII exposure — halt all collection; notify IRB within 48 hours.
