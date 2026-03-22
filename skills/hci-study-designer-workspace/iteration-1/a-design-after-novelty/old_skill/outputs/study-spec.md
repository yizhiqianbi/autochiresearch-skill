# Study Spec: LLM Tools and HCI Students' Literature Review Efficiency

## 1. Research Question

**Primary RQ:** Do LLM-assisted literature review tools improve the efficiency and output quality of literature reviews conducted by HCI students, compared to unaided database search?

**Secondary RQs:**
- RQ2: How do students' perceived workload and confidence differ between LLM-assisted and unaided conditions?
- RQ3: What strategies do students adopt when integrating LLM tools into their review workflow?

---

## 2. Study Type

**Controlled within-subjects experiment** with a post-task survey and a brief think-aloud protocol.

Rationale: The study requires both objective performance measures (time-on-task, citation coverage, relevance precision) and self-reported measures (workload, satisfaction). A within-subjects design controls for individual variation in academic background. Because participants perform a bounded literature review task — not an extended longitudinal workflow — a single-session lab-style study is sufficient.

No custom prototype is required; the intervention is an existing LLM-assisted tool (e.g., Elicit, Consensus, or a representative ChatGPT + Scholar workflow). The comparison condition is standard unaided search (Google Scholar + institutional database).

---

## 3. Participants

| Parameter | Value |
|-----------|-------|
| Target N (full study) | 24 participants |
| Target N (pilot) | 3 participants |
| Population | Graduate or advanced undergraduate students enrolled in an HCI or related course who have conducted at least one literature review |
| Recruitment channel | Course mailing lists, HCI lab Slack/Discord, posted flyers in CS/design departments |
| Compensation | $15 gift card or equivalent course credit |

### Inclusion criteria
- Currently enrolled in a degree program that includes HCI, interaction design, or a closely related field
- Has completed at least one literature review (self-reported)
- Comfortable reading English-language academic papers
- Has not used the specific LLM tool(s) selected as the intervention for more than 5 hours total

### Exclusion criteria
- Extensive prior use of the assigned LLM tool (>5 hours self-reported)
- Enrolled in a course where the assigned topic is the exact focus of a current assignment (conflict-of-interest risk)
- Unable to complete a 90-minute in-person or synchronous remote session

---

## 4. Design

| Factor | Levels |
|--------|--------|
| Tool condition (within-subjects) | (A) LLM-assisted tool; (B) Unaided search |
| Order | Counterbalanced (Latin square, half AB / half BA) |
| Topic | Two matched HCI sub-topics (one per condition), matched for prior literature volume and difficulty |

**Session structure (90 min total):**

| Phase | Duration | Description |
|-------|----------|-------------|
| Consent + screener | 5 min | Confirm eligibility; obtain written consent |
| Training | 10 min | Brief tutorial on the assigned LLM tool (condition A only; condition B receives equivalent orientation to search databases) |
| Task 1 | 30 min | Literature review task, Topic 1, assigned condition |
| Short break + NASA-TLX | 5 min | Workload questionnaire for Task 1 |
| Task 2 | 30 min | Literature review task, Topic 2, counterbalanced condition |
| Post-study questionnaire | 8 min | Full survey (see survey-draft.md) |
| Debrief + think-aloud debrief | 7 min | Semi-structured debrief questions |

---

## 5. Tasks

### Task definition
Participants are asked to identify the **5 most relevant papers** for a specified HCI research question within 30 minutes. They must produce:
1. A list of paper titles and citation keys
2. A 2–3 sentence synthesis summary

### Matched topic pairs (examples — replace with final versions after pilot)
- Pair 1: (A) Accessibility in conversational agents; (B) Gesture interaction for older adults
- Pair 2: (A) Attention and notification design; (B) Affective computing in educational tools

### Completion markers
- Participant has submitted a list of ≥1 paper with at least one synthesis sentence, OR
- 30-minute timer expires

### Logged / observed events (facilitator records)
- Time to first citation identified
- Total number of citations retrieved
- Number of relevant citations (scored post-hoc by researcher using a pre-defined relevance rubric)
- Number of search queries or prompts issued
- Tool switches (switching away from assigned tool)

---

## 6. Measures

### Primary outcomes

| Measure | Operationalization | Collection |
|---------|-------------------|------------|
| Task efficiency | Time (seconds) to submit ≥3 relevant citations | Timer log |
| Citation relevance precision | Proportion of submitted papers rated relevant by two coders (κ target ≥ 0.70) | Post-hoc coding |
| Citation coverage | Number of relevant papers found / total relevant papers in pre-compiled gold set (top 10 per topic) | Post-hoc scoring |

### Secondary outcomes

| Measure | Scale | Collection |
|---------|-------|------------|
| Perceived workload | NASA-TLX (6 subscales, 0–100 each) | Mid-session (after each task) |
| Satisfaction with results | 5-point Likert (1 = not at all satisfied, 5 = very satisfied) | Post-task, post-study survey |
| Perceived tool usefulness | 5 items adapted from TAM (Davis, 1989) | Post-study survey |
| Perceived ease of use | 5 items adapted from TAM | Post-study survey |
| Trust in LLM output | 3 items (custom; see survey-draft.md) | Post-study survey |
| Strategy use (qualitative) | Open-ended: describe your search approach | Post-study survey + debrief |

### Covariates
- Prior literature review experience (number of reviews completed)
- Self-reported LLM familiarity (general, not tool-specific)
- Academic level (MS, PhD, advanced UG)

---

## 7. Analysis Plan

| Question | Method |
|----------|--------|
| RQ1 — efficiency and quality difference | Paired t-test or Wilcoxon signed-rank (depending on normality) on time, precision, coverage |
| RQ2 — workload and confidence | Paired comparison on NASA-TLX subscales (Bonferroni-corrected for 6 comparisons) |
| RQ3 — strategies | Thematic analysis of open-ended responses and debrief notes |
| Order effects | Mixed ANOVA with order as between-subjects factor |
| Effect size | Cohen's d for parametric tests; r for non-parametric |

**Power analysis:** With N=24 and a within-subjects design, assuming ρ=0.50 correlation between conditions, the study achieves 80% power to detect d=0.55 at α=0.05 (two-tailed). This is conservative for expected efficiency differences reported in analogous tool comparison studies.

---

## 8. Stop Criteria

| Criterion | Action |
|-----------|--------|
| Inter-rater agreement on relevance coding falls below κ=0.60 after calibration round | Revise rubric and re-code before continuing data collection |
| Pilot reveals task completion rate <50% within 30 min | Extend task time to 40 min or simplify topic |
| Any participant reports significant distress or frustration (>7/10 on exit check) | Debrief immediately; do not continue; log incident |
| Discovered that the LLM tool is inaccessible or rate-limited during sessions | Pause data collection; switch to a verified backup tool; re-run affected sessions |
| After first 12 participants, effect size estimate falls below d=0.20 with CI clearly excluding target effect | Report null trend; consult advisor on whether to continue or redesign |
| Any data breach or PII exposure involving study records | Halt collection; notify IRB within 48 hours |

---

## 9. Data Handling

- All session recordings (screen + audio for think-aloud) stored in encrypted folder on institutional server
- Participants assigned anonymous ID codes; name-to-ID mapping stored separately
- Recordings deleted after transcription and coding are verified
- Data retained for 3 years per institutional policy
- No data shared with third parties

---

## 10. IRB and Ethics Notes

- IRB application required before recruitment begins
- Consent form (see consent.md) must be signed before any task or data collection
- Deception is not used; participants are informed of both conditions
- The LLM tool's terms of service must be confirmed to allow use in research contexts
- Pilot checklist (see pilot-checklist.md) must be completed and signed off before full data collection

---

## 11. Timeline (from IRB approval)

| Week | Milestone |
|------|-----------|
| 1–2 | Finalize materials, build gold-standard paper sets for both topics |
| 3 | Pilot (3 participants); revise protocol |
| 4–7 | Full data collection (24 participants, ~3–4 per week) |
| 8–9 | Coding and reliability checks |
| 10–11 | Analysis |
| 12 | Write-up |
