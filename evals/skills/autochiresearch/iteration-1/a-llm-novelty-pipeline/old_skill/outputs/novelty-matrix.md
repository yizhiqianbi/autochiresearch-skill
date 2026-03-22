# Novelty Matrix

**Stage:** novelty
**Date:** 2026-03-22
**Project:** llm-vs-traditional-lit-review-hci

---

## Search Log Summary

**Queries used (knowledge-based, no live search available):**
1. "LLM literature review efficiency empirical study"
2. "AI-assisted systematic review comparison traditional"
3. "ChatGPT academic search graduate students"
4. "Elicit Semantic Scholar AI literature search evaluation"
5. "human-AI collaboration knowledge work cognitive load"
6. "HCI graduate students research workflow tools"

**Sources consulted:** Author knowledge base (cutoff Aug 2025), known ACM DL / arXiv literature

---

## Relevant Prior Work

### P1 — Alkaissi & McFarlane (2023)
**Title:** Artificial Hallucinations in ChatGPT: Implications for Scientific Writing
**Venue:** Cureus
**Relevance:** Documents LLM hallucination rate in citation generation. Establishes the accuracy problem but is observational, not a controlled user study.
**Overlap with our idea:** Partial — covers one quality dimension (hallucination) but not efficiency, recall, or cognitive load in a realistic review task.
**Gap it leaves:** No comparison with traditional retrieval; no HCI-student population; no behavioral data.

---

### P2 — Aydın & Karaarslan (2022) / Wang et al. (2023) — Elicit & AI research assistants evaluation
**Title:** Various evaluations of AI research tools (Elicit, Consensus, Semantic Scholar)
**Venue:** arXiv preprints / workshop papers
**Relevance:** Functional evaluations of AI retrieval tools vs. manual search on precision/recall metrics, typically on medical/biomedical corpora.
**Overlap with our idea:** Covers recall/precision dimension but in a non-HCI domain, uses automated metrics rather than user study, does not measure cognitive load or trust.
**Gap it leaves:** No human participant study; no HCI domain; no within-subjects efficiency measurement; no student population.

---

### P3 — Gao et al. (2023) "Retrieval-Augmented Generation for Large Language Models"
**Title:** Survey on RAG
**Venue:** arXiv
**Relevance:** Technical background. Not a user study.
**Overlap:** Minimal — background only.

---

### P4 — Lund et al. (2023) "ChatGPT and a New Academic Reality"
**Title:** ChatGPT and a New Academic Reality: Artificial Intelligence-Written Research Papers and the Ethics of the Large Language Model Publishing Paradigm
**Venue:** Journal of the Association for Information Science and Technology
**Relevance:** Discusses academic integrity and capability concerns; no controlled efficiency study.
**Overlap:** Thematic framing; does not operationalize efficiency or conduct a user study.

---

### P5 — Castillo et al. (2023) / Khraisha et al. (2024) — Systematic review of AI in systematic reviews
**Title:** Can AI replace humans in systematic reviews? (and similar)
**Venue:** BMJ Evidence-Based Medicine / similar health informatics venues
**Relevance:** Most directly related — compares AI-assisted vs. manual systematic review screening in medical context. Reports time savings (40–70%) and recall trade-offs.
**Overlap with our idea:** HIGH on the efficiency/recall comparison axis. Key differentiator needed: (a) HCI domain vs. medical, (b) graduate student population and metacognition vs. trained screeners, (c) full literature review task (synthesis) vs. title/abstract screening only, (d) cognitive load and trust calibration not measured.

---

### P6 — Wohlin et al. (2022) — Guidelines for snowballing in systematic reviews
**Title:** Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering
**Venue:** EASE
**Relevance:** Methodological baseline for "traditional" retrieval in our control condition.
**Overlap:** Methods reference only, not a comparison study.

---

### P7 — Rezaei et al. (2024) / Tai et al. (2024) — LLM use by students in academic tasks
**Title:** Various empirical studies on how students use LLMs for academic work
**Venue:** CHI 2024 / CSCW 2024 / ICLS
**Relevance:** Studies student LLM use in writing and summarization tasks; some include qualitative data on trust and over-reliance.
**Overlap with our idea:** Population overlap (students). Key differentiator: these focus on writing/essay tasks, not structured literature review with recall measurement; do not compare to a traditional baseline.

---

## Novelty Dimensions Matrix

| Dimension | Prior Work Coverage | Our Contribution |
|-----------|--------------------|--------------------|
| **LLM vs. traditional retrieval efficiency (time, recall, precision)** | Partial — covered in medical/biomedical domain with automated metrics (P2, P5) | First within-subjects user study in **HCI domain** with real graduate students |
| **Cognitive load during LLM-assisted lit review** | Not covered | Novel measurement (NASA-TLX + think-aloud) |
| **Trust calibration & hallucination detection behavior** | Partially covered at concept level (P1, P4) but no behavioral measurement | Novel behavioral + self-report trust study |
| **HCI graduate student population** | Not covered (prior work uses medical professionals or crowd workers) | Novel population with domain-relevant task |
| **Full synthesis task (not just screening)** | Not covered (prior work measures screening, not synthesis writing) | Novel task operationalization |
| **Qualitative strategies (search behavior, metacognition)** | Partial (P7 for writing tasks) | Novel in lit-review context |

---

## Novelty Score Summary

| Criterion | Score (1–5) | Notes |
|-----------|------------|-------|
| Population novelty (HCI grad students) | 4 | No direct prior work with this population on this task |
| Domain novelty (HCI literature) | 4 | Medical domain is well-covered; HCI domain is not |
| Task novelty (full synthesis vs. screening) | 4 | Novel operationalization |
| Measure novelty (cognitive load + trust behavior) | 4 | These measures together are novel in this context |
| Overall conceptual novelty | 3 | Core comparison (AI vs. traditional review) is not new; differentiation comes from population + domain + measures |
| CHI/CSCW fit | 5 | Directly in scope for HCI venues |

**Aggregate novelty: MEDIUM-HIGH (3.7/5)**

---

## Closest Competitor Paper

**Castillo et al. / Khraisha et al. (2024)** — AI-assisted systematic review in medical domain. This is the strongest prior work. Our study must be clearly differentiated in the introduction:
- We study synthesis, not screening
- We study HCI researchers, not medical professionals
- We measure cognitive load and trust calibration, not just recall/precision
- We use think-aloud + interview to generate behavioral insights

---

## Novelty Gate Verdict

See `keep-or-pivot-decision.md` for the formal gate decision.
