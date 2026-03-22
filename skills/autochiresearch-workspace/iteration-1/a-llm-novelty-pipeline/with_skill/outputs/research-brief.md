# Research Brief

**Project slug:** llm-vs-traditional-litreview-hci
**Stage:** brief
**Date:** 2026-03-22

---

## 1. Research Idea (Raw)

对比 LLM 辅助 vs 传统检索下 HCI 研究生做文献综述的效率差异。

*English translation:* Comparing the efficiency of LLM-assisted versus traditional search-based literature review among HCI graduate students.

---

## 2. Refined Research Question

**Primary RQ:**
How does using an LLM-assisted literature review workflow (e.g., ChatGPT / Perplexity / Claude for search, summarization, and gap identification) compare to a traditional keyword-search-and-skim workflow (ACM DL / Google Scholar / Semantic Scholar) in terms of task efficiency, coverage quality, and cognitive load for HCI graduate students conducting literature reviews?

**Sub-questions:**

- RQ1 (Efficiency): Does LLM assistance reduce the time required to produce a scoped literature review with comparable coverage?
- RQ2 (Quality): Does LLM assistance lead to different recall/precision of relevant papers, more synthesis depth, or more gaps identified?
- RQ3 (Cognitive experience): How do participants perceive cognitive load, confidence, and trust in findings under each condition?
- RQ4 (Behavior): What search and synthesis strategies do participants adopt under each condition (process tracing)?

---

## 3. Motivation

Large language models are rapidly being adopted as research assistants in academic settings, yet empirical evidence comparing their effectiveness against established information-retrieval workflows is sparse — especially for domain-specific, nuanced tasks like HCI literature reviews. HCI graduate students represent a tractable, ecologically valid population: they regularly conduct literature reviews and can articulate both instrumental and epistemic criteria for quality. Understanding where LLMs help, where they introduce risk (hallucination, coverage gaps, over-reliance), and what the cognitive trade-offs are has direct implications for graduate pedagogy, tool design, and research integrity.

---

## 4. Proposed Contribution

1. **Empirical:** A controlled within-subjects study (N ≈ 24 HCI graduate students) providing the first fine-grained comparative measurement of LLM-assisted vs. traditional literature review workflows on efficiency, coverage, and cognitive load metrics.
2. **Methodological:** A reusable evaluation rubric for assessing literature review quality (coverage recall, synthesis depth, gap identification accuracy) that can be applied to future tool comparisons.
3. **Design implications:** Actionable guidelines for integrating LLM tools into HCI graduate research practice and research-tool design.

---

## 5. Methodology Sketch

- **Design:** 2 × 1 within-subjects counterbalanced experiment (condition A: LLM-assisted; condition B: traditional keyword search).
- **Participants:** ~24 HCI PhD/Master's students at a research university, recruited via departmental mailing lists.
- **Task:** Conduct a 60-minute scoped literature review on a pre-selected HCI subtopic (topics matched for difficulty and unfamiliarity across conditions).
- **Measures:**
  - Task completion time, number of papers retrieved/skimmed/cited
  - Expert-graded coverage score (recall of a gold-standard paper set)
  - Synthesis depth score (rubric-graded synthesis paragraph)
  - NASA-TLX cognitive load; trust and confidence self-report
  - Think-aloud / screen recording for process analysis
- **Analysis:** Paired t-tests / Wilcoxon signed-rank for efficiency metrics; mixed-effects models for subjective measures; thematic analysis for process data.

---

## 6. Scope Boundaries

- Focus on HCI literature reviews specifically (domain expertise and corpus familiarity matter).
- LLM tool is constrained to a fixed interface (e.g., ChatGPT-4o with web search, or Claude with Projects) to ensure reproducibility; not a free-choice tool evaluation.
- No deployment or server required; data collected via screen recording + post-task surveys administered locally.

---

## 7. Keywords (for novelty search)

`LLM literature review`, `AI-assisted systematic review`, `information retrieval HCI`, `research tool evaluation`, `cognitive load literature search`, `CHI graduate student research`, `human-AI collaboration knowledge work`
