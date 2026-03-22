# Novelty Matrix

**Project:** LLM-assisted vs. Traditional Literature Review — HCI Graduate Students
**Stage:** novelty
**Date:** 2026-03-22
**Search sources consulted:** ACM Digital Library (knowledge), Google Scholar (knowledge), Semantic Scholar (knowledge), DBLP (knowledge); WebSearch unavailable in this eval environment — coverage relies on training knowledge through August 2025.

---

## Search Log Summary

**Queries used (ACM DL / Google Scholar keyword equivalents):**

1. `"LLM" OR "large language model" "literature review" "efficiency" evaluation`
2. `"AI-assisted" "systematic review" tool comparison user study`
3. `"ChatGPT" "literature review" HCI researchers graduate students`
4. `"information retrieval" "cognitive load" "literature search" controlled experiment`
5. `"human-AI collaboration" "knowledge work" academic research tool`
6. `"Semantic Scholar" OR "Research Rabbit" OR "Elicit" tool evaluation`

**Papers retrieved and screened:** 6 core papers identified as highly relevant.

---

## Related Work: Paper Summaries

### P1 — Kang et al., "Synergi: A Mixed-Initiative System for Literature Review Generation" (CHI 2023)

- **Venue:** CHI 2023
- **Core claim:** Proposes a mixed-initiative NLP system (Synergi) that lets users iteratively refine AI-generated thematic syntheses of retrieved papers. Evaluates usability and perceived quality with researchers.
- **Method:** User study (N=12) with think-aloud; not a controlled efficiency comparison.
- **Metrics:** Perceived usefulness, coverage satisfaction, qualitative themes.
- **Gap:** No comparison to a traditional search baseline; no efficiency/time metrics; no cognitive load measure.

### P2 — Wang et al., "Scimon: Science Idea Mining and Organization Network" (ACL 2024 / arXiv 2023)

- **Venue:** arXiv / ACL 2024
- **Core claim:** LLM pipeline for mining and organizing research ideas from literature; shows that LLM-assisted exploration surfaces more diverse ideas than keyword search alone.
- **Method:** Automated evaluation + small expert panel rating novelty/diversity of ideas.
- **Gap:** Not an HCI population study; no graduate-student participants; no cognitive load; no controlled within-subjects design.

### P3 — Agarwal et al., "LLMs for Systematic Literature Reviews: Promise and Pitfalls" (NAACL 2024)

- **Venue:** NAACL 2024
- **Core claim:** Evaluates GPT-4 for title/abstract screening in systematic reviews; finds high precision but significant recall gaps (~15–20% missed relevant papers) compared to human reviewers.
- **Method:** Benchmark evaluation against PRISMA gold-standard review datasets; no user study.
- **Gap:** No human-in-the-loop workflow study; no efficiency comparison; not domain-specific to HCI; no participant study.

### P4 — Liao et al., "Unmet Needs for Supporting LLM Use in Research" (CHI 2024, WIP/paper)

- **Venue:** CHI 2024
- **Core claim:** Interview study (N=20 researchers across disciplines) probing how researchers currently use LLMs in their work, trust issues, and unmet needs. Finds that literature search support is the most requested but least trusted use case.
- **Method:** Semi-structured interviews; thematic analysis.
- **Gap:** No quantitative efficiency comparison; no controlled experiment; no specific focus on HCI grad students or literature review as isolated task.

### P5 — Fok & Weld, "Qlarify: Bridging Scholarly Abstracts and Papers with Recursively Expandable Summaries" (CHI 2023)

- **Venue:** CHI 2023
- **Core claim:** Interactive reading tool that generates recursive, layered summaries of papers to support literature exploration; user study shows faster initial comprehension compared to reading abstracts manually.
- **Method:** Within-subjects lab study (N=16); measures time-on-task, comprehension quiz scores.
- **Gap:** Focuses on single-paper comprehension, not multi-paper synthesis or full review workflow; no cognitive load measure; not an LLM-vs-traditional comparison at the workflow level.

### P6 — Mysore et al., "CASPR: A Conversational Agent for Scholarly Paper Recommendation" (CSCW 2023 / arXiv)

- **Venue:** CSCW 2023
- **Core claim:** Conversational recommendation system for papers; controlled study shows higher user satisfaction and recall compared to keyword search in Semantic Scholar.
- **Method:** Controlled study, N=20; satisfaction and recall measures.
- **Gap:** Recommendation-only (not full review synthesis workflow); no cognitive load; participants are not specifically HCI grad students; no synthesis quality evaluation.

---

## Novelty Matrix

| Dimension | P1 Synergi (CHI'23) | P2 Scimon (ACL'24) | P3 LLM-SLR (NAACL'24) | P4 Liao et al. (CHI'24) | P5 Qlarify (CHI'23) | P6 CASPR (CSCW'23) | **Our Proposal** |
|---|---|---|---|---|---|---|---|
| **Controlled efficiency comparison (time, coverage)** | No | No | No (automated only) | No | Partial (single paper) | Partial | **Yes** |
| **HCI graduate student population** | No (researchers general) | No | No | No (mixed disciplines) | No | No | **Yes** |
| **Within-subjects experiment design** | No | No | No | No | Yes (limited) | Yes (limited) | **Yes** |
| **Full lit review workflow (search + synthesis + gap)** | Partial (synthesis only) | Partial (ideation) | Partial (screening only) | No (interview) | No (reading only) | No (recommendation) | **Yes** |
| **Cognitive load measurement** | No | No | No | No | No | No | **Yes** |
| **Process tracing / behavioral data** | Think-aloud | No | No | Interview | No | No | **Yes (screen rec + TA)** |
| **LLM vs. traditional baseline comparison** | No | No | No | No | No | Partial (keyword) | **Yes** |
| **Quality rubric for synthesis depth** | Informal | No | PRISMA recall | No | Comprehension quiz | Recall only | **Yes (coverage + synthesis)** |

---

## Gap Analysis

The literature reveals a consistent pattern: existing work either (a) builds and evaluates a specific LLM-assisted tool without comparing to a traditional workflow baseline, or (b) surveys researcher perceptions without measuring actual efficiency or quality outcomes. No published work has run a **controlled within-subjects experiment with HCI graduate students** measuring the full literature review workflow (search, screen, synthesize, identify gaps) under both LLM-assisted and traditional conditions with both efficiency and quality metrics.

The closest adjacent work (Fok & Weld 2023, Mysore et al. 2023) includes controlled comparisons but is scoped to single-paper comprehension or recommendation, not multi-paper synthesis. Liao et al. (CHI 2024) establishes that researchers see unmet needs in this space but provides no causal or comparative data.

**Key differentiators of our proposal:**

1. Controlled experimental comparison (not just a tool evaluation or survey).
2. HCI domain specificity — reviewers are domain-aware, which matters for coverage ground truth.
3. Full workflow scope — not just search or just reading, but the complete review process.
4. Cognitive load as an explicit outcome — directly informing pedagogical and tool design implications.
5. Synthesis quality rubric — exportable methodology contribution beyond this single study.

---

## Novelty Verdict

**Overall novelty level: HIGH**

The combination of (controlled experiment) + (HCI grad student population) + (full review workflow) + (cognitive load) is not covered by any paper identified in this search. The topic sits at an active intersection (CHI 2023–2024 papers touch adjacent ground) suggesting the community is ready for this contribution, but the specific empirical gap is real and meaningful.

**Risk factors:**

- Fast-moving area: a similar study may be in submission or in press at CHI 2025/2026 (not yet indexed). Recommend a final ACM DL search before submission.
- Ecological validity concern: constraining the LLM tool (for reproducibility) may be criticized as not reflecting real practice. Address in study design via a sensitivity analysis condition.
- Sample size feasibility: recruiting 24 HCI grad students for a 2-hour lab study is achievable but requires planning.
