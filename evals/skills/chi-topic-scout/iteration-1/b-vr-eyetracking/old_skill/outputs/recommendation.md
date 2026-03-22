# Recommendation
**Topic:** Eye-tracking-assisted text input in VR environments
**Date:** 2026-03-22

---

## Decision: PIVOT (keep core direction, sharpen contribution axis)

---

## Rationale

The intersection of VR eye tracking and text input is a real, active, and under-saturated area, but the most generic framing — "build a gaze keyboard in VR and compare it to a controller keyboard" — is no longer novel. Two papers (Rajanna & Hansen, ETRA 2018; Yu et al., CHI 2019) have established that baseline, and a third (Knierim et al., MobileHCI 2018) has explored the gaze + gesture hybrid. Publishing a plain replication with newer hardware is possible at a workshop but unlikely to reach CHI or UIST as a full paper without a distinct contribution axis. The recommendation is therefore not to drop the topic — the VR gaze typing space has genuine white space — but to pivot the framing toward one of the clearly uncovered combinations identified in the novelty matrix. The three most viable pivots, ranked by difficulty-to-novelty ratio, are: (1) an LM-augmented adaptive gaze keyboard in VR, where the language model narrows the candidate set in real time and the system adjusts keyboard layout or key saliency in 3D space based on bigram predictions — this is the highest-impact pivot and aligns with current NLP-for-interaction trends; (2) a fatigue-aware adaptive dwell controller that uses gaze signal quality or blink rate as a real-time fatigue proxy to modulate the dwell threshold, addressing the most consistently cited limitation across all prior work without requiring additional hardware; (3) extending smooth-pursuit swipe-typing (EyeSwipe) to a 3D floating VR keyboard, which tests whether the technique's dwell-free advantage survives the depth and noise constraints of HMD-based eye tracking. Any of these three pivots produces a paper with a clear differentiation sentence: "Unlike prior VR gaze keyboards that use fixed thresholds and no language support, our system / prior systems did X but not Y in VR context." A longitudinal component (3–5 sessions) added to any of these pivots would further distinguish the contribution, since the learning curve for VR gaze typing remains entirely unstudied.

---

## Pivot Options Summary

| Option | Pivot Direction | Novelty Score | Feasibility | Recommended Target Venue |
|---|---|---|---|---|
| A | LM-adaptive gaze keyboard in VR (adaptive spatial key highlighting driven by n-gram / neural LM) | Very High | Medium (requires LM integration + VR dev) | CHI / UIST |
| B | Fatigue-aware adaptive dwell threshold (blink rate / EEG as fatigue proxy → auto-adjust dwell) | High | Medium-High (gaze data available; physiological sensor needed) | CHI / IMWUT |
| C | Smooth-pursuit swipe typing in VR 3D (port EyeSwipe to floating HMD keyboard) | High | Medium (3D path recognition is non-trivial) | CHI / ETRA |
| D | Longitudinal study of any existing VR gaze keyboard (skill acquisition, fatigue over time) | Medium | High (no new system needed) | CHI Notes / ETRA |
| E | Accessibility-centered VR gaze keyboard for motor-impaired users | High | Low-Medium (requires specialized recruitment) | ASSETS |

---

## Recommended Next Steps

1. Select one pivot option (A or B recommended for CHI).
2. Implement a minimal prototype: for Option A, a Unity-based floating QWERTY with a pre-trained bigram/trigram LM (or a fine-tuned small transformer) providing next-character probability-weighted key enlargement; for Option B, a dwell controller that reads real-time blink frequency from the eye tracker API and adjusts threshold in 0.5-second windows.
3. Run a pilot study (N = 5) to establish WPM baselines and verify the adaptive mechanism works before scaling to full study.
4. Pre-register the main study design.
5. Target CHI 2026 (deadline ~September 2025) or CHI 2027.

---

## Papers to Cite as Baselines (Confirmed from Corpus)

- Rajanna & Hansen (ETRA 2018) — VR gaze dwell baseline
- Yu et al. (CHI 2019) — VR PoG + head hybrid, ~20 WPM benchmark
- McGill et al. (CHI 2015) — overall VR text entry benchmark
- Tonio et al. (IUI 2018) — LM + gaze keyboard (2D) — motivation for Option A
- Knierim et al. (MobileHCI 2018) — hybrid gaze+gesture in VR
