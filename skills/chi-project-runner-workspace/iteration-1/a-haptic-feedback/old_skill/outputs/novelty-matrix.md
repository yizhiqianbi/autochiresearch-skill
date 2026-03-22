# Novelty Matrix
## Project: Haptic Feedback UI for Mobile Form-Filling Experience

**Phase:** Pre — Novelty
**Date:** 2026-03-22

---

## Instructions for Reading This Matrix

Each cell scores the degree to which existing work already covers the dimension.
- **0** = Not addressed at all
- **1** = Peripherally mentioned / implied
- **2** = Studied in a related but different context
- **3** = Directly studied but with key differences
- **4** = Fully addressed — no remaining gap

A **row score ≤ 2** on any critical dimension indicates a genuine novelty gap worth pursuing.

---

## Dimension Definitions

| ID | Dimension | Description |
|----|-----------|-------------|
| D1 | Setting: realistic multi-field mobile form | Study conducted in ecologically valid form-filling context (not synthetic button/menu task) |
| D2 | IV = differentiated haptic patterns | Haptic pattern vocabulary mapped to distinct form events (focus, success, error, submit) |
| D3 | DV = abandonment rate | Measures whether participants quit before completion |
| D4 | DV = task completion time | Time to complete the full form |
| D5 | DV = error rate | Number of validation failures / corrections |
| D6 | DV = perceived usability (SUS) | Standardized usability scale |
| D7 | DV = cognitive load (NASA-TLX) | Objective cognitive load measurement |
| D8 | Accessibility dimension | Low-vision / blind user inclusion |
| D9 | Cross-device haptic fidelity | Addresses LRA vs. ERM variation |
| D10 | Within-subjects design | Controls for individual differences |

---

## Coverage Matrix

| Paper / Work | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Hoggan et al., CHI 2008 (haptic keyboard) | 0 | 1 | 0 | 4 | 4 | 2 | 1 | 0 | 0 | 3 |
| Luk et al., CHI 2006 (button confirmation) | 0 | 0 | 0 | 3 | 2 | 1 | 0 | 0 | 0 | 2 |
| Kieffer et al., MobileHCI 2017 (inline validation) | 4 | 0 | 2 | 3 | 4 | 3 | 2 | 0 | 0 | 3 |
| Brewster & Brown 2004 (tactons) | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| Schneider et al., IEEE ToH 2017 (multimodal) | 1 | 2 | 0 | 3 | 3 | 2 | 2 | 0 | 1 | 2 |
| Kane et al., CHI 2011 (accessibility) | 1 | 2 | 0 | 2 | 1 | 2 | 0 | 4 | 0 | 1 |
| Guerreiro et al., Assets 2008 (a11y) | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 4 | 0 | 1 |
| Poupyrev & Maruyama 2003 (menu) | 0 | 0 | 0 | 4 | 2 | 1 | 0 | 0 | 0 | 2 |
| Maclean 2008 (haptic design review) | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Immersion Corp 2016 (industry study) | 2 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| **Max coverage across all works** | **4** | **4** | **2** | **4** | **4** | **3** | **2** | **4** | **1** | **3** |
| **GAP score (4 − max)** | **0** | **0** | **2** | **0** | **0** | **1** | **2** | **0** | **3** | **1** |

---

## Gap Summary

| Dimension | Gap Score | Verdict |
|-----------|-----------|---------|
| D1 — Realistic mobile form setting | 0 | Covered (Kieffer 2017) |
| D2 — Differentiated haptic patterns | 0 | Covered (Brewster 2004; pattern design) |
| D3 — Abandonment rate as DV | **2** | **NOVEL** — no existing study measures abandonment |
| D4 — Task completion time | 0 | Covered by multiple works |
| D5 — Error rate | 0 | Covered by multiple works |
| D6 — Perceived usability (SUS) | 1 | Partially covered; not in haptic+form studies |
| D7 — Cognitive load (NASA-TLX) | **2** | **NOVEL** — underexplored in haptic form context |
| D8 — Accessibility | 0 | Covered separately; not in form context |
| D9 — Cross-device haptic fidelity | **3** | **NOVEL** — almost entirely unaddressed |
| D10 — Within-subjects design | 1 | Mostly covered |

---

## Novel Intersection (Critical Novelty Claim)

The proposed study is novel at the **intersection** of dimensions even where individual dimensions are covered:

**No existing work simultaneously:**
1. Uses a realistic multi-field mobile form task (D1)
2. Tests a differentiated haptic vocabulary mapped to form event states (D2)
3. Measures abandonment rate as an outcome (D3)
4. Measures cognitive load via NASA-TLX (D7)

This 4-way intersection (D1 × D2 × D3 × D7) has **zero coverage** in existing literature, establishing a clear novelty claim.

**Secondary novel contribution:** Cross-device haptic fidelity (D9) — testing whether the haptic pattern vocabulary degrades gracefully across LRA and ERM hardware — is almost entirely unaddressed in the literature.

---

## Novelty Gate Assessment

| Criterion | Pass/Fail |
|-----------|-----------|
| At least one dimension with gap score ≥ 2 | PASS (D3=2, D7=2, D9=3) |
| Novel intersection not previously studied | PASS (D1×D2×D3×D7) |
| Not a direct replication of a single existing paper | PASS |
| Contribution beyond incremental parameter variation | PASS — new measurement (abandonment), new context (form lifecycle haptics), new methodological contribution (cross-device fidelity) |

**Overall Novelty Gate Result: PASS**

---

## Closest Prior Work (Risk Assessment)

The paper most likely to be cited as "this already exists" is:

> Hoggan, E., Brewster, S. A., & Johnston, J. (2008). Investigating the effectiveness of tactile feedback for mobile touchscreens. In *Proc. CHI 2008* (pp. 1573–1582).

**Key difference from proposed study:** Hoggan et al. use a synthetic keyboard typing task, not a form-filling task; they do not map haptic patterns to form lifecycle events; they do not measure abandonment or cognitive load. The proposed study's contribution is distinguished.

---

## Recommended Framing for Paper

Frame the contribution as:
1. **First study** to isolate differentiated haptic feedback as an IV in a realistic mobile form completion task
2. **First measurement** of haptic feedback's effect on form abandonment rate
3. **Design guidelines** for haptic pattern vocabulary in form UI across device hardware types
