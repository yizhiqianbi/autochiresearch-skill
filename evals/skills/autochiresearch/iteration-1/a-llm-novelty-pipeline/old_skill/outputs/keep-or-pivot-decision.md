# Novelty Gate Decision: Keep / Pivot / Drop

**Stage:** novelty gate
**Date:** 2026-03-22
**Project:** llm-vs-traditional-lit-review-hci

---

## Decision

# PIVOT

---

## Rationale

### What is novel and defensible

The core comparison (LLM-assisted vs. traditional literature retrieval) is a real and timely research question. The study as originally framed contains genuine gaps relative to prior work:

- No existing user study uses HCI graduate students as participants for a literature review task.
- Prior comparisons (medical domain, P5) measure only title/abstract screening; none measure full synthesis quality.
- Cognitive load (NASA-TLX) and trust calibration have not been measured together in this context.

These differentiators are real and would be recognized by CHI reviewers.

### Why the original framing warrants a pivot rather than a keep

**1. The efficiency framing is likely to yield predictable, low-insight results.**
Multiple studies already show that LLM-assisted retrieval is faster and has lower recall than manual methods. A within-subjects study confirming this in HCI will be seen as a replication in a new domain — publishable in a workshop, but unlikely to reach CHI full paper without a sharper contribution claim.

**2. "Efficiency difference" as the primary construct undersells the interesting questions.**
The more novel and CHI-appropriate contribution lies in the behavioral and metacognitive dimensions: How do HCI students calibrate trust? When do they over-rely? What strategies distinguish effective from ineffective LLM use? These questions are buried as RQ3/RQ4 in the current brief but are the true differentiator.

**3. Rapidly evolving tool landscape is a structural risk.**
A study reporting that "GPT-4 is X% faster than Google Scholar in 2025" will be partially obsolete by the time it is reviewed. Framing around durable human factors (cognitive load, trust, strategy) insulates the contribution from tool-version decay.

**4. "Graduate student efficiency" overlaps with a crowded adjacent space.**
CHI 2024–2025 saw a wave of "students + LLMs" papers. An efficiency-focused framing risks being desk-rejected as incremental. A behavioral/metacognitive framing is more distinctive.

---

## Recommended Pivot

**New framing:** From "efficiency comparison" to "trust calibration and metacognitive strategy in LLM-assisted literature review among HCI researchers"

**Revised primary RQ:**
How do HCI graduate students calibrate trust in LLM-generated literature summaries, and what metacognitive and behavioral strategies predict effective vs. ineffective LLM use in the literature review process?

**What stays the same:**
- Within-subjects design (both conditions still needed as contrast)
- HCI graduate student population
- Think-aloud + interview data collection
- Recall/precision as secondary measures (now supporting data, not primary outcome)

**What changes:**
- Primary measures shift to: trust calibration accuracy (confidence vs. actual hallucination rate), metacognitive monitoring behaviors (coded from think-aloud), strategy taxonomy
- NASA-TLX moves to a supporting measure
- Time efficiency becomes context, not the headline finding
- The paper's contribution is a behavioral model or strategy taxonomy, not a performance benchmark

**Why this pivot is stronger for CHI:**
- Generates a durable theoretical contribution (strategy/trust model) that survives LLM version changes
- Fills a genuine gap not addressed by any identified prior work
- Aligns with CHI's emphasis on human factors and behavior, not benchmarking
- Positions the study as generative (what should we teach students?) rather than evaluative (which tool wins?)

---

## Pivot Confidence: HIGH

The pivot is low-risk because:
- The study infrastructure (design, population, task) requires minimal change
- The data collected under the pivot framing is a superset of what the original framing needed
- The pivot framing has no direct prior work competitor

---

## Next Steps (if pivot is accepted)

1. Revise `research-brief.md` with updated RQs and primary measures
2. Update the study-spec to foreground behavioral coding and trust measurement instruments
3. In the novelty matrix, confirm no prior work directly addresses trust calibration + strategy in LLM-assisted lit review for HCI students
4. Proceed to `study` stage with revised framing

---

## Summary Table

| Gate Question | Answer |
|---------------|--------|
| Is there clear prior work that already answers the RQ? | Partial — efficiency comparison in medical domain exists |
| Is the population/domain novel enough to warrant a domain-replication paper? | Borderline — possible but weak for CHI full paper |
| Does the study contain a more novel embedded question? | Yes — trust calibration and metacognitive strategy |
| Should we drop the idea entirely? | No — the research space is valid and timely |
| **Verdict** | **PIVOT — reframe around trust calibration and behavioral strategy, not efficiency benchmarking** |
