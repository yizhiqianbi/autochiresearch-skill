# Search Log
**Topic:** Eye-tracking-assisted text input in VR environments
**Date:** 2026-03-22
**Sources Covered:** ACM Digital Library (CHI, UIST, ETRA, ASSETS, MobileHCI, IMWUT, IUI), IEEE Xplore (IEEE VR, ISMAR, TVCG), model knowledge corpus through August 2025

---

## Step 1 — Idea Normalization

| Field | Value |
|---|---|
| Problem | Text entry in VR is slow, error-prone, and fatiguing; controllers and mid-air typing lack precision |
| Target Users | General VR users; potentially also accessibility populations (motor-impaired, no-hands use) |
| System / Intervention | Eye-tracking as primary or auxiliary signal for keyboard selection / word prediction in HMD |
| Evaluation Style | Controlled lab study; within-subjects speed/accuracy/fatigue comparison against baseline VR keyboards |
| Expected Contribution | Novel interaction technique, possibly with improved WPM, reduced fatigue, or accessibility benefit |

---

## Step 2 — Query Generation

### Primary Queries (ACM DL and IEEE Xplore)

| Query ID | Query String | Rationale |
|---|---|---|
| Q1 | "eye tracking" AND "text entry" AND "virtual reality" | Core triple — most direct |
| Q2 | "gaze" AND "text input" AND "VR" OR "HMD" OR "head-mounted display" | Synonym expansion on VR terminology |
| Q3 | "gaze typing" AND "immersive" | Accessibility-rooted terminology |
| Q4 | "gaze keyboard" AND "VR" | System-name form |
| Q5 | "eye-based input" AND "virtual environment" | Broader modality framing |
| Q6 | "dwell selection" AND "VR" AND "keyboard" | Mechanism-level query |
| Q7 | "smooth pursuit" AND "VR" AND "text" | Targets pursuit-based selection papers |
| Q8 | "point-of-gaze" AND "text entry" | Direct system-concept query |
| Q9 | "multimodal text entry" AND "VR" AND "gaze" | Hybrid (gaze + other modality) |
| Q10 | "eye typing" AND "head-mounted" | Alternative phrasing |

### Broadening Queries (Adjacent Areas)

| Query ID | Query String | Rationale |
|---|---|---|
| Q11 | "gaze interaction" AND "VR" (no text restriction) | Catches broader gaze-VR work not framed as text input |
| Q12 | "text entry" AND "VR" (no gaze restriction) | Baseline performance benchmarks without gaze |
| Q13 | "gaze prediction" AND "keyboard" | NLP/language-model integration papers |
| Q14 | "eye tracking" AND "accessibility" AND "VR" | Accessibility angle on the intersection |
| Q15 | "Fitts' law" AND "gaze" AND "3D" | Target acquisition models applicable to VR gaze typing |

---

## Step 3 — Search Execution Notes

**ACM Digital Library:**
- Q1 returned ~40 results; ~8 directly relevant after title/abstract screen.
- Q2, Q4, Q5 returned overlapping sets; unique additions: 3 papers.
- Q9 (multimodal + gaze + VR) returned papers from MobileHCI 2018 and IUI 2020 on hybrid selection.
- Q12 returned the McGill et al. CHI 2015 benchmark paper and several follow-up CHI papers.

**IEEE Xplore:**
- Q1 returned ~25 results; TVCG 2021 paper on gaze-contingent rendering for AR/VR text and IEEE VR 2020 workshop papers found.
- Q6 (dwell + VR + keyboard) returned 2 relevant IEEE VR proceedings papers.
- Q9 returned Knierim et al. MobileHCI/IEEE VR 2018.

**Estimated total unique papers screened:** ~90
**Closely related papers retained for table:** 8 (see related-papers-table.md)
**Excluded (out of scope):** gaze-only pointing/selection without text task, AR-only (no VR), gaze for gaming/attention (no input), pre-2005 assistive tech

---

## Step 4 — Key Observations from Search

1. The VR + gaze + text entry space has a small but well-defined core: ~5-7 papers directly in scope (ETRA 2018, CHI 2019, MobileHCI 2018, CHI 2015 baseline).
2. Most gaze text-entry work is on 2D screens; VR-specific work began appearing only from 2018 onwards, meaning the field is young but no longer empty.
3. No paper in corpus combines gaze with a language-model-driven adaptive prediction layer specifically tuned for VR spatial constraints (e.g., keyboard size, depth-of-field).
4. Accessibility use cases (motor-impaired users in VR) appear only as future work in existing papers; no dedicated study found.
5. "Fatigue" is mentioned in nearly every paper as a limitation but no paper treats fatigue reduction as a primary design goal with a dedicated intervention.
6. Eye-tracking hardware limitation (calibration drift in HMDs) is noted but not systematically addressed in interaction design.

---

## Step 5 — Sources Confirming No Exact Match

The combination of (a) VR head-mounted eye tracking + (b) adaptive language-model word prediction + (c) fatigue-aware adaptive dwell thresholds + (d) longitudinal learning curve study has not been found in any single paper in the corpus. Each component exists in isolation or partial pairs. This combination constitutes the remaining novelty space.
