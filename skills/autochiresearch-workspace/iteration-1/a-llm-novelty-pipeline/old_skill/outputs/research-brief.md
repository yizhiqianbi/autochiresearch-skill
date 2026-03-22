# Research Brief

**Stage:** brief
**Date:** 2026-03-22
**AutoCHIResearch Project:** llm-vs-traditional-lit-review-hci

---

## 1. Raw Idea

对比 LLM 辅助 vs 传统检索下 HCI 研究生做文献综述的效率差异。

(Compare the efficiency difference between LLM-assisted and traditional retrieval approaches when HCI graduate students conduct literature reviews.)

---

## 2. Problem Statement

Literature reviewing is one of the most time-consuming and cognitively demanding tasks for HCI graduate students. Traditional retrieval pipelines (ACM DL, Google Scholar, forward/backward citation chasing, manual screening) impose high overhead. LLMs (e.g., ChatGPT, Claude, Perplexity, Elicit, Semantic Scholar's AI features) now offer a complementary retrieval modality. However, we lack empirical evidence on how LLM-assisted review compares to traditional methods for HCI graduate researchers specifically, in terms of:

- **Efficiency** (time-on-task, number of relevant papers identified per hour)
- **Coverage** (recall of a gold-standard corpus)
- **Quality of synthesis** (accuracy of attributed claims, coherence of the narrative)
- **Cognitive load** (NASA-TLX, perceived effort)
- **Trust calibration** (confidence in outputs, ability to detect hallucinations)

---

## 3. Research Questions

**RQ1.** How does LLM-assisted literature review compare to traditional database retrieval in terms of time efficiency and paper recall for HCI graduate students?

**RQ2.** What is the effect of LLM assistance on the cognitive load experienced during a structured literature review task?

**RQ3.** How accurately do HCI graduate students calibrate their trust in LLM-generated summaries, and what behavioral and metacognitive strategies do they employ?

**RQ4.** What are the qualitative trade-offs (breadth vs. depth, serendipitous vs. targeted discovery) perceived by participants?

---

## 4. Proposed Study Design (Pre-Novelty Sketch)

**Design:** Within-subjects (2 conditions, counterbalanced) controlled study + semi-structured interview

**Conditions:**
- **Traditional:** ACM DL + Google Scholar + forward/backward citation chaining (no AI tools)
- **LLM-Assisted:** Participant's choice of LLM tool (ChatGPT / Claude / Perplexity / Elicit) + same databases permitted as supplements

**Participants:** 20–24 HCI graduate students (PhD + Master's) with ≥ 1 year of research experience

**Task:** Produce a structured literature summary (10–15 papers, 500-word synthesis) on a given HCI sub-topic (two topics, one per condition, matched in scope and corpus size)

**Measures:**
- Time-on-task (logged)
- Paper recall (against gold-standard set curated by authors)
- Precision (proportion of cited papers actually relevant)
- NASA-TLX (cognitive load)
- Trust questionnaire (adapted from Lee & See 2004)
- Think-aloud / retrospective verbal protocol
- Semi-structured exit interview

**Venue target:** CHI 2027 (full paper) or CSCW 2027

---

## 5. Motivation and Significance

- **Practical:** Helps HCI programs decide how to train students in AI-era literature review
- **Theoretical:** Contributes to the emerging literature on human-AI collaboration in knowledge work, trust calibration in LLM use, and metacognition under AI assistance
- **Methodological:** Provides an empirical benchmark that is currently missing despite rapid LLM adoption in academia

---

## 6. Initial Risk Flags

| Risk | Level | Notes |
|------|-------|-------|
| Prior work on LLM-assisted lit review (general) | Medium-High | Several papers exist; must differentiate HCI-specific framing and within-subjects efficiency measurement |
| Ecological validity of lab task | Medium | Controlled tasks may not reflect real thesis work |
| Rapidly evolving tool landscape | High | LLM capabilities change fast; findings may date quickly |
| Gold-standard corpus construction | Medium | Requires careful pre-study effort |

---

## 7. Next Stage

Proceed to **novelty** stage: systematic search for prior work, populate novelty matrix, issue keep/pivot/drop.
