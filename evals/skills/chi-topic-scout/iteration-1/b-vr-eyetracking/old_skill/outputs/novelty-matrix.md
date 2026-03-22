# Novelty Matrix
**Topic:** Eye-tracking-assisted text input in VR environments
**Date:** 2026-03-22

---

## Reading Guide

- DONE = published, well-replicated, no additional contribution needed
- PARTIAL = attempted in adjacent context or as pilot/future-work mention; room for systematic work
- GAP = not found in corpus; viable novelty space
- N/A = not applicable or not a meaningful research question

---

## Matrix 1 — Platform x Gaze Mechanism

|  | Dwell Selection | Smooth Pursuit / Swipe | Hybrid Gaze + Gesture | Hybrid Gaze + Head Pose | Hybrid Gaze + LM Prediction |
|---|---|---|---|---|---|
| **2D Desktop / Screen** | DONE (Majaranta 2002+, many) | DONE (EyeSwipe CHI 2016) | PARTIAL (some AT work) | N/A | DONE (IUI 2018, ASSETS 2009) |
| **Mobile (2D)** | PARTIAL | DONE (EyeK MobileHCI 2018) | N/A | N/A | PARTIAL |
| **VR / HMD (3D)** | PARTIAL (ETRA 2018) | **GAP** | PARTIAL (MobileHCI 2018) | DONE (CHI 2019) | **GAP** |
| **AR / passthrough HMD** | PARTIAL | **GAP** | **GAP** | PARTIAL | **GAP** |

Key gaps highlighted: VR smooth-pursuit text entry, VR gaze + LM, AR gaze text entry in all forms.

---

## Matrix 2 — Design Goal x Prior Art

| Design Goal | Status | Closest Paper | What Is Missing |
|---|---|---|---|
| Baseline speed/accuracy measurement (VR + gaze) | PARTIAL — only 2 papers | Yu et al. CHI 2019; Rajanna & Hansen ETRA 2018 | Replication with newer HMDs (Quest Pro, Vive XR Elite), larger N, diverse text corpora |
| Reducing Midas touch / unintended activation | PARTIAL | Knierim et al. MobileHCI 2018 (gesture confirmation) | Gaze-only solution without requiring a second modality; pursuit-based approach untested in VR |
| Fatigue reduction as primary design goal | GAP | Mentioned as limitation in ETRA 2018, CHI 2019 | No paper designs around fatigue; no physiological (EMG/EEG) measurement of gaze-typing fatigue in VR |
| Language model / NLP word prediction | PARTIAL — only on 2D | Tonio et al. IUI 2018; Majaranta ASSETS 2009 | VR-adapted LM keyboard (spatial layout + prediction area in 3D; handling short text bursts typical of VR) |
| Adaptive / personalized dwell threshold | GAP | Alluded to in ETRA 2018 ("threshold tuning critical") | No paper implements real-time adaptive dwell based on user fatigue or accuracy feedback |
| Longitudinal / skill acquisition study | GAP | None | No paper tracks learning curve over multiple sessions for VR gaze typing |
| Accessibility use case (motor-impaired in VR) | GAP | Majaranta 2009 (AT, not VR); general accessibility VR papers | No paper tests gaze typing specifically for motor-impaired users in immersive VR |
| Calibration drift robustness | GAP | Noted as limitation in CHI 2019 | No interaction design solution for degraded gaze accuracy mid-session |
| Keyboard layout optimization for gaze in 3D | GAP | QWERTY assumed in all VR gaze papers | No paper explores alternative layouts (Dvorak, ATOMIK, circular) designed for 3D gaze constraints |
| Multimodal fusion (gaze + voice + gesture) | GAP | Each dyad studied independently | No trimodal combination with intelligent fallback studied |

---

## Matrix 3 — Contribution Type x Prior Art

| Contribution Type | Status |
|---|---|
| New interaction technique (VR gaze + LM adaptive keyboard) | GAP — publishable |
| Controlled lab study replicating baseline with modern HW | PARTIAL — weakly covered; replication with Quest Pro / 2023+ HMDs would contribute |
| Computational model (gaze noise + depth in 3D selection) | GAP — no Fitts' law extension to 3D gaze depth found |
| Design guidelines / design space paper | PARTIAL — only CHI 2019 provides limited guidelines |
| Longitudinal field study | GAP |
| Accessibility-centered system | GAP |

---

## Matrix 4 — Specific Sub-topic Combinations Assessed for Exact Prior Art

| Combination | Exact Prior Art Found? | Nearest Paper |
|---|---|---|
| VR gaze dwell keyboard (basic) | YES | ETRA 2018, CHI 2019 |
| VR gaze + head-pose hybrid keyboard | YES | CHI 2019 |
| VR gaze + gesture hybrid keyboard | PARTIAL | MobileHCI 2018 |
| VR gaze + language model keyboard | NO | — |
| VR gaze + adaptive dwell (fatigue-aware) | NO | — |
| VR gaze + pursuit-based selection | NO | — |
| VR gaze typing: longitudinal (3+ sessions) | NO | — |
| VR gaze typing: motor-impaired users | NO | — |
| VR gaze + spatial 3D keyboard layout optimization | NO | — |
| VR gaze + calibration-drift-robust design | NO | — |

---

## Summary: Where the Novelty Is

**Strongest novelty claims (two or more dimensions uncovered simultaneously):**

1. **Adaptive LM-augmented gaze keyboard in VR** — combines language model prediction (done in 2D only) + VR 3D spatial keyboard (done without LM). Both components exist; the VR-specific integration is new. Contribution: system + evaluation.

2. **Fatigue-aware adaptive dwell with physiological sensing** — no paper has designed an adaptive dwell controller that responds to measured fatigue (blink rate, EEG alpha, or scleral redness) in VR. Contribution: novel mechanism + physiological study.

3. **Pursuit-based (swipe) gaze typing in VR** — EyeSwipe exists only on 2D desktop; no paper has extended swipe-style gaze gestures to a 3D floating keyboard in HMD. Contribution: technique transfer + 3D adaptation challenges.

4. **Longitudinal learning curve study** — any of the above systems would become additionally novel with a 5+ session study. No longitudinal gaze typing study exists in VR. Contribution: empirical; could also yield design guidelines.
