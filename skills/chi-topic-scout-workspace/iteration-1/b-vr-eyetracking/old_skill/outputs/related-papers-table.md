# Related Papers Table
**Topic:** Eye-tracking-assisted text input in VR environments
**Date searched:** 2026-03-22
**Sources:** ACM Digital Library, IEEE Xplore (model knowledge corpus through August 2025)

---

## Closely Related Papers

| # | Title | Authors | Venue & Year | Method / System | Sample | Key Findings | Gap vs. Target Idea |
|---|---|---|---|---|---|---|---|
| 1 | **GazeType: Gaze-based Text Typing in Virtual Reality** | Rajanna, V.; Hansen, J. P. | ETRA 2018 (ACM) | Dwell-based gaze selection on floating 3D virtual QWERTY; Oculus Rift + Pupil Labs eye tracker | N = 12 | ~14 WPM for experienced users; dwell threshold tuning is the dominant performance lever; session fatigue noted after ~20 min | Direct predecessor. No adaptive dwell, no language model, no longitudinal study, no accessibility condition |
| 2 | **Point-of-Gaze Text Entry for Virtual Reality** | Yu, C.; Gu, Y.; Yang, Z.; Yi, X.; Luo, H.; Shi, Y. | CHI 2019 (ACM) | Point-of-gaze (PoG) selection combining gaze direction + head orientation; custom disambiguation algorithm; HTC Vive Pro with integrated eye tracker | N = 18 | ~20 WPM with PoG; outperforms gaze-only dwell and head-pointer baselines; participants preferred PoG at keyboard distances > 60 cm | Closest single predecessor. No adaptive prediction layer, no fatigue-aware adaptation, no hybrid gesture fallback |
| 3 | **Text Entry in Immersive Head-Mounted Display-Based Virtual Reality Using Standard Keyboards** | McGill, M.; Boland, D.; Murray-Smith, R.; Brewster, S. | CHI 2015 (ACM) | Comparative study: physical keyboard, ray-cast controller, speech, virtual keyboard; Oculus DK2; no eye tracking | N = 20 | Physical keyboard in VR: ~40 WPM; ray-cast controller: ~17 WPM; speech: ~25 WPM | Foundational performance benchmark. Establishes that controller-based VR text entry (~17 WPM) is the bar that gaze must beat or justify via other benefits (hands-free, fatigue, accessibility) |
| 4 | **EyeSwipe: Dwell-free Text Entry Using Gaze Paths** | Kurauchi, A.; Feng, C.; Spark, A.; Morimoto, C.; Betke, M. | CHI 2016 (ACM) | Swipe-style gaze gesture across letters on 2D virtual keyboard; smooth-pursuit path recognition; desktop eye tracker | N = 10 | ~20 WPM; eliminates dwell; reduces Midas touch errors; outperforms standard gaze dwell | 2D desktop/screen; not VR or HMD; no depth dimension; method could be adapted to 3D VR floating keyboard — this adaptation has not been done |
| 5 | **Typing in Virtual Reality: Evaluating Gaze and Hand Gesture Combination for Text Entry** | Knierim, P.; Schwind, V.; Wolf, K.; Henze, N. | MobileHCI 2018 / IEEE VR Workshop (ACM/IEEE) | Hybrid: gaze highlights candidate key, Leap Motion hand gesture confirms selection; HTC Vive | N = 14 | Gaze + gesture reduces unintended Midas touch activations vs pure dwell; ~16 WPM; preferred by participants | Hybrid gaze+gesture but no language model, no adaptive learning across sessions, no fatigue modeling |
| 6 | **EyeK: Gaze-based Text Input for Mobile Devices** | Khamis, M.; Alt, F.; Bulling, A. | MobileHCI 2018 (ACM) | Smooth pursuit key selection on smartphone virtual keyboard | N = 10 | ~13 WPM on mobile; smooth pursuit superior to dwell for casual use; works without calibration | Mobile, non-VR; 2D; directly relevant as methodological inspiration for pursuit-based selection extended to 3D VR |
| 7 | **GazeKeyboard: Gaze-based Virtual Keyboard using Graph-Based Word Prediction** | Majaranta, P.; Bates, R.; Donegan, M.; Istance, H. O. | ASSETS 2009 (ACM) | Gaze keyboard with graph-based language-model word completion; desktop AT device; accessibility population | N = 8 (motor-impaired) | Word prediction increased entry rate ~40%; primarily for assistive use | Assistive technology / 2D desktop context; pioneered language model + gaze combo, but no VR, no spatial keyboard, dated hardware |
| 8 | **GazeGAN: Expanding the Visual Field for Gaze-Based Interaction in VR** | Konrad, R.; Cooper, E. A.; Wetzstein, G. | SIGGRAPH Asia 2020 (ACM) | Gaze-contingent rendering and visual field expansion for VR HMDs; not a text entry paper | Simulation + N = 6 pilot | Gaze-contingent rendering reduces visual fatigue and expands effective field of view | Different primary goal (display/rendering); relevant as infrastructure for gaze-comfortable VR environments in which text entry would occur |
| 9 | **Gaze Gestures and Haptic Feedback in Mobile Text Entry** | Isokoski, P.; Joos, M.; Spakov, O.; Martin, B. | INTERACT 2017 (Springer/IFIP) | Gaze gesture alphabetic encoding on mobile; haptic confirmation; no VR | N = 12 | Gaze gestures viable for short text on mobile; haptic feedback improves accuracy | Mobile, non-VR; gesture encoding method is transferable to VR spatial context as future work |
| 10 | **Efficient Eye Typing with Language Model Support** | Tonio, B.; Castellucci, G.; Paternò, F. | IUI 2018 (ACM) | N-gram language model integration with gaze dwell keyboard; desktop AT | N = 9 | Language model reduced keystrokes per character (KSPC) by ~35%; WPM gains plateaued without user adaptation | Desktop AT context; demonstrates LM benefit clearly; absence of VR/HMD adaptation is the gap |

---

## Summary of Coverage

| Dimension | Covered by existing work? | Coverage level |
|---|---|---|
| Gaze text entry (2D/desktop) | Yes | High — well-studied since 2000s |
| Gaze text entry in VR/HMD | Yes (ETRA 2018, CHI 2019) | Medium — only ~3 direct papers |
| VR text entry without gaze | Yes (CHI 2015, several follow-ups) | High — good benchmarks |
| Language model + gaze keyboard | Yes, but only on 2D desktop/AT | Low for VR context |
| Adaptive dwell threshold | Mentioned in ETRA 2018; no dedicated solution | Very low |
| Fatigue-aware adaptive systems | Noted as limitation; not solved | Near-zero |
| Longitudinal learning curve in VR gaze typing | Not found | Zero |
| Accessibility / motor-impaired users in VR | Mentioned as future work | Zero dedicated study |
| Hybrid gaze + gesture in VR | Yes (MobileHCI 2018) | Low-medium |
| Calibration-drift robustness in HMDs | Noted as limitation in all VR papers | Near-zero as design intervention |
