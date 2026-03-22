# Novelty Gate Decision

**Project:** LLM-assisted vs. Traditional Literature Review — HCI Graduate Students
**Stage:** novelty → gate
**Date:** 2026-03-22

---

## Decision

**KEEP**

---

## Rationale

### Why KEEP (not pivot or drop)

**1. Genuine empirical gap confirmed.**
The novelty matrix search (6 papers, ACM DL / Google Scholar / Semantic Scholar knowledge base) found no existing work that combines all four dimensions: controlled experiment, HCI-domain-specific participant population, full literature review workflow, and cognitive load measurement. The gap is specific and well-bounded — not a vague "nobody has studied this."

**2. CHI community readiness signals.**
CHI 2023–2024 contains multiple adjacent papers (Synergi, Qlarify, Liao et al.) indicating the program committee actively values this intersection of AI tools, academic knowledge work, and empirical evaluation. The topic is neither too early (infrastructure for LLM-assisted research tools now exists) nor too late (the controlled comparison has not been published).

**3. Tractable scope.**
The proposed within-subjects design (N ≈ 24, two 60-minute sessions) is achievable within a single academic semester with standard IRB protocols. No novel prototype is required — existing commercial LLM tools (ChatGPT-4o, Claude) serve as the intervention. This limits engineering risk.

**4. Multiple contribution types.**
Even if the efficiency result is null or mixed, the study contributes: (a) a validated quality rubric for literature review assessment, (b) behavioral process data on how grad students use LLMs for research, and (c) replication infrastructure. The paper has a viable floor.

**5. Clear practical and pedagogical stakes.**
The question matters to HCI programs, library researchers, and tool designers right now. CHI reviewers reliably favor papers with clear, immediate relevance to academic practice.

---

### Conditions on KEEP

The following risks must be addressed in study design before proceeding:

| Risk | Mitigation |
|---|---|
| A near-identical paper may be in submission at CHI 2026 | Run a live ACM DL search immediately before submitting; adjust scope if a direct competitor appears |
| Constraining the LLM tool may limit ecological validity | Include a brief free-choice LLM session as a secondary condition or probe; discuss limitation explicitly |
| "Efficiency" is multidimensional — cherry-picking metrics risks null results | Pre-register primary outcomes before data collection begins |
| Sample (HCI grad students at one university) may lack diversity | Recruit across at least 2 institutions if possible; report institution as a covariate |

---

### Why NOT pivot

A pivot would be warranted if: the gap were partially covered (it is not) or the methodology sketch were infeasible (it is feasible). The study does not require a novel prototype, specialized apparatus, or unusual population access. No pivot is needed.

### Why NOT drop

A drop would be warranted if: (a) the topic were entirely saturated, (b) the research question were untestable, or (c) the contribution were marginal. None of these apply. The literature is active but the specific empirical question is open.

---

## Next Step

Proceed to **study** stage: design the within-subjects experiment protocol, define the counterbalancing scheme, write the task materials (two matched HCI subtopics), and draft the IRB application.

Per AutoCHIResearch rules: do not advance to study design without this KEEP decision being recorded — it is now recorded.
