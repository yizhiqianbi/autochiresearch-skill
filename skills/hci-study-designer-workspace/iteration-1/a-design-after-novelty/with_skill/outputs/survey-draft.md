# Survey Draft
**Study:** LLM Tools and Literature Review Efficiency in HCI Students
**Version:** 1.0 — for pilot review
**Date:** 2026-03-22

This document contains all survey instruments in order of administration:
1. Screener
2. Post-task measures (administered after each of the two experimental sessions)
3. Post-study questionnaire (administered after Session 2 only)
4. Demographics
5. Debrief

All instruments are designed for online delivery (Qualtrics or equivalent). Branching logic is noted inline.

---

## Part 1 — Screener

*Administered online before scheduling. Estimated time: 3–5 min.*

**Introduction text (shown at top of screener):**

> We are recruiting HCI graduate students for a 2-session online study about literature review tools. Each session takes about 50 minutes. Compensation is $20 USD per session ($40 total). Please answer the following questions honestly — there are no right or wrong answers. Responses determine whether you are eligible to participate.

---

**S1.** What is your current enrollment status?
- [ ] Master's student (HCI, interaction design, or related field)
- [ ] PhD student (HCI, interaction design, or related field)
- [ ] Master's student in a different field
- [ ] PhD student in a different field
- [ ] Not currently enrolled as a graduate student
- [ ] Other: ___________

*Routing: If "Not currently enrolled" or "Other" without HCI relevance → disqualify with thank-you message.*

---

**S2.** Which of the following best describes your program?
- [ ] Human-Computer Interaction
- [ ] Interaction Design
- [ ] Computer Science with HCI focus
- [ ] Information Science / Library Science
- [ ] Cognitive Science
- [ ] Design (UX, product, or similar)
- [ ] Other: ___________

*Note: "Other" responses are reviewed manually before scheduling.*

---

**S3.** Have you completed at least one literature review (for a class paper, thesis proposal, or research project)?
- [ ] Yes
- [ ] No

*Routing: If "No" → disqualify.*

---

**S4.** How often do you use Google Scholar?
- [ ] Daily or almost daily
- [ ] A few times a week
- [ ] A few times a month
- [ ] Less than once a month
- [ ] Never

*Routing: If "Never" or "Less than once a month" → flag for manual review (may lack baseline comparison skills).*

---

**S5.** In the past 6 months, have you used any LLM-based tools for research tasks? (Select all that apply)
- [ ] ChatGPT / GPT-4
- [ ] Elicit
- [ ] Semantic Scholar AI features
- [ ] Perplexity AI
- [ ] Consensus
- [ ] Other AI research tool: ___________
- [ ] I have not used any LLM-based tools for research

*Note: No disqualification based on this item — used for covariate analysis and counterbalancing.*

---

**S6.** How would you rate your overall experience with LLM tools for research tasks?
*(1 = No experience at all, 7 = Very extensive experience)*

[ 1 ] — [ 2 ] — [ 3 ] — [ 4 ] — [ 5 ] — [ 6 ] — [ 7 ]

---

**S7.** Have you published or written a paper specifically on any of the following topics? (Select all that apply)
- [ ] Gesture-based interaction in automotive or in-vehicle UIs
- [ ] Haptic or tactile feedback in mobile health applications
- [ ] None of the above

*Routing: If either of the first two boxes checked → disqualify (topic familiarity exclusion).*

---

**S8.** Do you currently work in a role where you use LLM tools for literature search or synthesis every workday?
- [ ] Yes
- [ ] No

*Routing: If "Yes" → disqualify (daily expert use creates skill gap from novice participants).*

---

**S9.** Are you able to complete two online sessions (each ~50 min) within the next 2 weeks, with at least 48 hours between the two sessions?
- [ ] Yes
- [ ] No

*Routing: If "No" → disqualify.*

---

**S10.** Do you have access to a laptop or desktop computer with a stable internet connection and a working webcam?
- [ ] Yes
- [ ] No

*Routing: If "No" → disqualify.*

---

**[End of Screener]**

*Qualifying participants see:* "Thank you! You appear to qualify for our study. A member of the research team will contact you within 3 business days to schedule your sessions."

*Disqualified participants see:* "Thank you for your interest. Unfortunately, you do not meet the eligibility criteria for this study at this time. We appreciate your time."

---

## Part 2 — Post-Task Measures

*Administered immediately after completing the literature review task in each session. Estimated time: 8–10 min. Appears identically in Session 1 and Session 2.*

**Introduction text:**

> Thank you for completing the literature review task. Please answer the following questions about your experience during the task you just completed. Try to respond based on this task only, not previous sessions.

---

### Section 2A — NASA-TLX (Cognitive Load)

*NASA Task Load Index (Hart & Staveland, 1988). Standard 20-point bipolar scale per subscale. Presented as 6 individual slider items.*

**Instructions:** For each dimension below, rate how much it applied to your experience during the literature review task you just completed. Use the full scale.

| Subscale | Low anchor (left) | High anchor (right) |
|---|---|---|
| **Mental Demand** | Very Low | Very High |
| **Physical Demand** | Very Low | Very High |
| **Temporal Demand** | Very Low | Very High |
| **Performance** | Perfect | Failure |
| **Effort** | Very Low | Very High |
| **Frustration** | Very Low | Very High |

*Each slider: 0–100 in increments of 5. Standard NASA-TLX scoring applied post-hoc (unweighted or weighted — decision before pre-registration).*

---

### Section 2B — Perceived Coverage

*3 custom 7-point Likert items. Validated against expert quality rating in pilot.*

**Instructions:** Please indicate how much you agree with each statement about the literature review you just completed.

**PC1.** I found enough relevant papers to write a well-supported synthesis.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

**PC2.** I am confident that I did not miss major relevant work on this topic.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

**PC3.** The papers I found represent the key themes in this area.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

---

### Section 2C — Trust in LLM Output

*Shown only in LLM condition. 4 items adapted from Komiak & Benbasat (2006) cognitive trust scale, re-worded for LLM context.*

**Instructions:** Please rate the following statements about the LLM tool you used during this task.

**TR1.** The LLM tool provided accurate summaries of the papers it suggested.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

**TR2.** I trusted the LLM tool to point me toward genuinely relevant literature.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

**TR3.** I verified the LLM tool's suggestions by reading the actual papers.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

**TR4.** Overall, I would rely on this type of tool for a real literature review.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

---

### Section 2D — Attention Check 1

*Embedded after trust items (or after PC items in conventional condition). Designed to catch non-attentive responding.*

**AC1.** For quality control purposes, please select "Somewhat Agree" (5) for this item.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

*Flag: Responses not equal to 5 → mark as potential inattentive; apply exclusion rule if both attention checks failed.*

---

### Section 2E — Task Experience (Open)

**TE1.** Briefly describe any challenges or frustrations you encountered during the task. *(text box, no minimum)*

**TE2.** Did you develop any strategies or workarounds while completing the task? If yes, describe them. *(text box, no minimum)*

---

**[End of Post-Task Measures]**

---

## Part 3 — Post-Study Questionnaire

*Administered after Session 2 only. Estimated time: 8–10 min.*

**Introduction text:**

> You have now completed both sessions. This final questionnaire asks about your overall experience across both sessions. Please answer based on both sessions combined unless a question specifies otherwise.

---

### Section 3A — Tool Preference

**TP1.** Overall, which approach did you prefer for completing the literature review task?
- [ ] Searching with an LLM-based tool
- [ ] Searching with conventional tools (Google Scholar only)
- [ ] No preference

**TP2.** Please explain your preference in a few sentences. *(text box)*

**TP3.** How likely are you to use an LLM-based tool for your next real literature review?
*(1 = Very Unlikely … 7 = Very Likely)*

---

### Section 3B — Comparative Efficiency Perception

**CE1.** Compared to conventional search, using the LLM tool felt:
*(1 = Much slower … 4 = About the same … 7 = Much faster)*

**CE2.** Compared to conventional search, using the LLM tool required:
*(1 = Much more mental effort … 4 = About the same … 7 = Much less mental effort)*

**CE3.** Compared to conventional search, the literature I found with the LLM tool felt:
*(1 = Much lower quality … 4 = About the same … 7 = Much higher quality)*

---

### Section 3C — Attention Check 2

**AC2.** This item checks that you are reading carefully. Please select "Disagree" (2) for this item.
*(1 = Strongly Disagree … 7 = Strongly Agree)*

*Flag: Responses not equal to 2 → mark as potential inattentive.*

---

### Section 3D — Open Reflection

**OR1.** Is there anything about the LLM tool that you feel we did not capture in the survey? *(text box)*

**OR2.** Do you have any suggestions for how LLM tools could better support literature reviews? *(text box)*

---

## Part 4 — Demographics

*Collected at end of post-study questionnaire. Used for sample description and covariate analysis.*

**D1.** What is your age?
*(open number field; if under 18, flag for IRB review — should be excluded at screener)*

**D2.** What is your gender?
- [ ] Woman
- [ ] Man
- [ ] Non-binary / gender non-conforming
- [ ] Prefer to self-describe: ___________
- [ ] Prefer not to say

**D3.** What year of your program are you currently in?
- [ ] Year 1
- [ ] Year 2
- [ ] Year 3
- [ ] Year 4+
- [ ] Other: ___________

**D4.** What is your primary research area within HCI? *(short text)*

**D5.** What is your first language?
*(text box — used to note English proficiency variance)*

**D6.** How many literature reviews have you completed in total (approximate)?
- [ ] 1–2
- [ ] 3–5
- [ ] 6–10
- [ ] More than 10

---

## Part 5 — Debrief

*Shown on final screen after demographics are submitted.*

---

**Debrief Text:**

> **Thank you for participating in our study.**
>
> **What this study is about:**
> This study investigated whether LLM-based tools (such as Elicit or ChatGPT) affect the efficiency, cognitive load, and perceived quality of literature reviews conducted by HCI graduate students. We compared LLM-assisted search to conventional search (Google Scholar) on controlled literature review tasks.
>
> **Why we did not fully disclose this upfront:**
> We told you we were studying "literature review tools" but did not specify our hypothesis in advance. This is standard practice in behavioral experiments to prevent participants from consciously performing differently based on what they believe is being measured. The task instructions and tools you used were genuine — there was no deception about the core task.
>
> **What happens to your data:**
> Your screen recordings, survey responses, and task outputs will be stored in encrypted form on institutional servers. All data will be de-identified before analysis. Screen recordings will be reviewed only by trained research team members and will be deleted after coding is complete. Your data will not be linked to your name in any publication.
>
> **Your rights:**
> You may withdraw your data from analysis at any time up to 4 weeks after your second session by contacting us at [STUDY EMAIL]. Withdrawal will not affect your compensation.
>
> **If you have questions:**
> Please contact the principal investigator at [PI EMAIL] or the IRB at [IRB CONTACT].
>
> **Compensation:**
> Your $20 USD gift card for this session will be emailed to you within 3 business days.
>
> Thank you for contributing to HCI research.

---

*[End of all survey instruments]*

---

## Instrument Notes for Pilot Review

- NASA-TLX anchors follow the standard printed form (Hart, 2006); do not modify wording
- Trust items (TR1–TR4) should be piloted for internal consistency (target α > 0.70); replace if below threshold
- Perceived Coverage items (PC1–PC3) are custom — pilot should confirm face validity with 3 HCI faculty before production run
- Attention check pass threshold: participant must pass at least 1 of 2 checks; failure on both → exclude from primary analysis, retain in sensitivity analysis
- All open-text fields: minimum character count set to 0 (do not force length — quality over length)
- Survey platform should prevent back-navigation after post-task submission to avoid inflation of response quality
