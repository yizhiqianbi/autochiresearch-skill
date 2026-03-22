# Keep / Pivot / Drop Recommendation
## Research Direction: Gesture Interaction + Elderly Users

**Assessment date:** 2026-03-22
**Decision:** **PIVOT**

---

## Decision

**PIVOT** — Do not proceed with the generic framing "gesture interaction + elderly users." Pivot to one of the specific sub-directions identified below. A non-specific proposal targeting this area will be rejected at CHI/CSCW on novelty grounds due to 15+ years of accumulated literature.

---

## Rationale

The broad combination of "gesture interaction + elderly users" is one of the most studied topics in accessible HCI. Touchscreen gesture usability with older adults has been exhaustively characterized (Findlater 2017; Kobayashi 2011; Vasconcelos 2012; and 10+ additional CHI/IUI papers). Gesture elicitation for this population is also established (Gao 2015; Vatavu 2020). A 2022 systematic review (Wolfe et al., ASSETS 2022) already synthesizes 40+ papers and explicitly maps the remaining gaps — meaning reviewers at top venues will use that review as a benchmark and will reject any submission that does not clearly address one of those named gaps. The most recent close paper (Zhu et al., CHI 2024) reached the personalization + motor impairment frontier, leaving a specific population gap (healthy older adults with age-typical — non-diagnosed — motor variability) and a modality gap (mid-air, AR/VR). A straight replication or minor variant of any existing combination is not publishable at CHI, CSCW, UIST, or IUI in 2025–2026.

**The idea is not dead — it must be sharpened to one of three viable pivots:**

---

## Recommended Pivots (choose one)

### Pivot A — Longitudinal mid-air gesture study with healthy older adults [RECOMMENDED FIRST CHOICE]

**Framing:** A 4-week within-subjects study of mid-air gesture interaction (MediaPipe / Leap Motion 2) with healthy community-dwelling adults aged 60+, measuring learning curve, gesture drift, fatigue adaptation, and subjective confidence across sessions.

**Why this is novel:** Every published mid-air + elderly study is single-session (Braun 2019: N=12, 1 session; Li 2023: N=16, Wizard-of-Oz). No paper has tracked how mid-air gesture performance evolves over weeks. This directly answers Wolfe et al.'s (2022) explicit call for longitudinal data.

**Why this is feasible:** Standard within-subjects protocol; no clinical population required; off-the-shelf tracking hardware; 3–4 week study; suitable for a PhD chapter or single CHI paper.

**Target venue:** CHI 2026 (Late Breaking Work deadline ~Oct 2025 has passed; aim for CHI 2027 full paper or IUI 2026).

---

### Pivot B — Gesture interaction in AR/VR for older adults [HIGH NOVELTY, HIGHER COST]

**Framing:** A formative + evaluative study of hand-gesture-based navigation and object manipulation in a VR or AR environment (Meta Quest 3 / HoloLens 2) with older adults, addressing depth perception, gesture disambiguation, and fall-risk posture constraints.

**Why this is novel:** As of 2024, virtually no peer-reviewed work examines how older adults perform gesture input specifically within VR/AR, despite rapid deployment of these devices in elderly care and rehabilitation. The IEEE VR and CHI communities have begun noting this gap.

**Why this is harder:** Requires VR lab setup; ethical screening for dizziness/vestibular issues in older adults; higher IRB complexity.

**Target venue:** CHI 2027, IEEE VR 2026, or ASSETS 2026.

---

### Pivot C — MCI-spectrum cognitive profiling linked to gesture learnability [HIGHEST IMPACT, HARDEST]

**Framing:** A cross-sectional study recruiting older adults across the full MCI spectrum (healthy aging → subjective cognitive decline → mild cognitive impairment, using MoCA/MMSE), measuring how cognitive profile predicts gesture error type, learning speed, and long-term retention. Contribute a gesture-design decision tree indexed by cognitive score.

**Why this is novel:** No gesture paper treats cognitive profile as a primary independent variable. Zhu 2024 addresses motor impairment; no work touches cognitive impairment. With 15% of adults over 60 having MCI, and that percentage rising, this is a pressing accessibility gap.

**Why this is harder:** Requires clinical collaboration (memory clinic or geriatric partner); ethics review; recruitment of a clinical population; longer study timeline (6–12 months).

**Target venue:** CHI 2027, ASSETS 2026, or ACM Health.

---

## What NOT to Do

- Do not submit a study that is "gesture usability study with N=20 older adults on a touchscreen" — this is a drop-level idea in 2025–2026.
- Do not frame the contribution as a gesture design guideline document without longitudinal or cognitive data — Gao 2015 and Wolfe 2022 already cover that.
- Do not pursue a systematic review — Wolfe 2022 is recent and comprehensive; a new review would require a fundamentally different angle (e.g., pure ML-recognition focused) to be accepted.

---

## Decision Summary

| Option | Decision | Reason |
|---|:---:|---|
| Generic "gesture + elderly" usability study | **DROP** | Saturated; reviewers will cite Wolfe 2022 and reject |
| Longitudinal mid-air gesture with healthy older adults | **KEEP (after pivot)** | Clear gap, feasible, directly addresses Wolfe 2022's call |
| Gesture in AR/VR for older adults | **KEEP (after pivot)** | Very high novelty, emerging context, higher cost |
| MCI-spectrum cognitive + gesture learnability | **KEEP (after pivot)** | Highest impact, requires clinical partnership |
| Touchscreen gesture + ML personalization (healthy older adults) | **PIVOT** | Low novelty unless combined with real-time adaptation and non-impaired population gap from Zhu 2024 |
