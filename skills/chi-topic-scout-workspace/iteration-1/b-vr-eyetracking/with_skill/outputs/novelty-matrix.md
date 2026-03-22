# Novelty Matrix
**Topic:** Eye-tracking-assisted text input in VR environments
**Date:** 2026-03-22

---

## Dimension Definitions

The target idea is decomposed into five orthogonal dimensions. For each row the matrix asks: *has this dimension been covered, and at what level of completeness?*

| Dimension | What "done" looks like | Status | Evidence |
|-----------|------------------------|--------|----------|
| **D1: Gaze as primary text selection in non-VR 2D** | Gaze dwell / swipe on flat virtual keyboard | FULLY DONE | EyeSwipe (CHI 2016), GazeType (ETRA 2018 — non-VR arm), GazeKeyboard (ASSETS 2009), EyeK (MobileHCI 2018) |
| **D2: VR text entry performance benchmarking** | Speed, accuracy, fatigue comparisons across modalities in HMD | FULLY DONE | McGill et al. CHI 2015 (no gaze); multiple controller/speech studies 2015-2022 |
| **D3: Gaze-only text entry in VR (dwell or PoG)** | Pure gaze input on floating VR keyboard inside HMD | SUBSTANTIALLY DONE | GazeType ETRA 2018; PoG VR CHI 2019 (Yu et al.) — both demonstrate feasibility, ~14-20 WPM range |
| **D4: Gaze + secondary modality hybrid for VR text** | Gaze selection confirmed by gesture, blink, or head pose | PARTIALLY DONE | Knierim et al. MobileHCI/IEEE VR 2018 (gaze+gesture); Yu et al. CHI 2019 (gaze+head) — but no voice, no foot pedal, no controller-grip confirmation |
| **D5: Adaptive / ML-augmented gaze text in VR** | Language model, user model, or neural decoder integrated with gaze to boost speed/accuracy | LARGELY OPEN | Majaranta et al. ASSETS 2009 used word prediction on desktop; no paper found that integrates a modern LLM/neural language model with gaze VR text entry |
| **D6: Accessibility-targeted gaze VR text entry** | Designed for users with motor impairments; tested with that population in VR | OPEN | GazeKeyboard (ASSETS 2009) covered accessibility on desktop; no VR + accessibility + gaze text entry paper found |
| **D7: Gaze text entry in social/multi-user VR** | Gaze typing while presence, avatar, or co-presence is a variable | OPEN | No paper found combining social VR context with gaze text input |
| **D8: Gaze text entry combined with foveated rendering optimization** | Simultaneous use of gaze for rendering and input without conflicts | OPEN | GazeGAN (SIGGRAPH Asia 2020) covers rendering side; no paper combines both goals jointly |
| **D9: Gaze text entry on non-QWERTY or optimized VR layouts** | Layout redesigned for 3D space + gaze physics (e.g., circular, spherical, Dvorak-derived) | OPEN | All VR gaze papers use flat QWERTY layouts; no optimized-for-gaze-in-3D layout paper found |
| **D10: Longitudinal / learning-curve study of gaze VR text** | Multi-session study showing expert performance trajectory | OPEN | All existing VR gaze text studies are single-session (1-2 hours); no longitudinal data |

---

## Has the Exact Combination Been Done?

**Target combination:** eye-tracking + VR + text entry (gaze-assisted, not gaze-only)

| Sub-combination | Done? | Closest paper | Gap |
|-----------------|-------|---------------|-----|
| Gaze-only dwell VR keyboard | YES | GazeType 2018, PoG CHI 2019 | Replication only; no contribution |
| Gaze + head pose VR keyboard | YES | Yu et al. CHI 2019 | If this is the exact design, it is done |
| Gaze + hand gesture VR keyboard | YES (partial) | Knierim 2018 | Done but small N=14, no language model |
| Gaze + voice confirmation VR text | NO | — | Open |
| Gaze + adaptive word prediction in VR | NO | — | Open; strong novelty |
| Gaze + optimized non-QWERTY layout in VR | NO | — | Open; layout design contribution |
| Gaze + accessibility focus in VR | NO | — | Open; ASSETS-ready contribution |
| Gaze + foveated rendering co-optimization | NO | — | Open; systems contribution |
| Longitudinal expert gaze typing in VR | NO | — | Open; learning science contribution |

---

## What Has Been Partially Done?

1. **Gaze + secondary input in VR** — Three papers address this but with small samples, simple confirmation modalities, and no intelligent disambiguation.
2. **Language-model-assisted gaze typing** — Done on desktop (ASSETS 2009 word lists); not brought into 3D VR with a modern neural language model.
3. **Layout optimization for gaze** — Done in 2D (e.g., OPTIGAZE-style works); not translated into 3D VR spatial constraints.
4. **Longitudinal gaze typing** — One or two desktop AT studies show expert curves; nothing in VR.

---

## What Gap Remains (Novelty Space Map)

```
HIGH NOVELTY
  |
  |  [D10] Longitudinal / expert learning curve in VR gaze text
  |  [D5]  Adaptive LLM-assisted gaze text in VR   <-- STRONGEST NOVELTY
  |  [D9]  3D-optimized non-QWERTY layout for gaze VR
  |  [D6]  Accessibility (motor-impaired) + gaze + VR
  |  [D8]  Gaze input + foveated rendering co-design
  |  [D7]  Social / multi-user VR + gaze text
  |
  |  [D4]  Gaze + novel confirmation modality (voice, grip) in VR  <-- MODERATE NOVELTY
  |
  |  [D3]  Gaze-only text entry in VR  (done; marginal contribution only)
  |  [D2]  VR text entry benchmarking  (done)
  |  [D1]  2D gaze text entry         (done)
  |
LOW NOVELTY
```

---

## Summary Assessment

| Verdict | Dimension |
|---------|-----------|
| DONE — avoid replication | Pure gaze dwell / PoG VR keyboard (D1, D2, D3) |
| PARTIALLY DONE — must differentiate | Gaze + secondary modality hybrid (D4) |
| OPEN — strong novelty | Adaptive LLM + gaze VR text (D5); Accessibility VR gaze text (D6); Social VR gaze text (D7); Foveated rendering + input co-design (D8); 3D-optimized layout (D9); Longitudinal study (D10) |
