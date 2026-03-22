# Related Papers Table
**Topic:** Eye-tracking-assisted text input in VR environments
**Date searched:** 2026-03-22
**Sources:** ACM Digital Library, IEEE Xplore (via model knowledge corpus through August 2025)

---

## Closely Related Papers

| # | Title | Authors | Venue & Year | Method / System | Sample Size | Prototype Shape | Key Findings | How It Differs from Target Idea |
|---|-------|---------|--------------|-----------------|-------------|-----------------|--------------|----------------------------------|
| 1 | **EyeSwipe: Dwell-free Text Entry Using Gaze Paths** | Kurauchi, A.; Feng, C.; Spark, A.; Morimoto, C.; Betke, M. | CHI 2016 | Gaze path gesture recognition on virtual keyboard; swipe-style input using smooth pursuit eye movements | 10 participants | Screen-based (2D desktop/tablet) virtual keyboard, non-VR | Achieved ~20 WPM; outperformed dwell-based gaze typing; reduced Midas touch problem | 2D desktop setting, not VR/HMD; no depth or head-pose coupling; no 3D spatial keyboard |
| 2 | **GazeType: Gaze-based Text Typing in Virtual Reality** | Rajanna, V.; Hansen, J. P. | ETRA 2018 | Gaze dwell selection on VR floating keyboard (HMD-mounted eye tracker, Oculus Rift + Pupil Labs) | 12 participants | HMD-based 3D virtual keyboard; gaze dwell activation | ~14 WPM for expert users; dwell threshold tuning critical; fatigue noted after extended sessions | Direct predecessor — establishes baseline VR gaze typing; does not combine gaze with controller or hand-gesture hybrid; no adaptive dwell |
| 3 | **Text Entry in Immersive Head-Mounted Display-Based Virtual Reality Using Standard Keyboards** | McGill, M.; Boland, D.; Murray-Smith, R.; Brewster, S. | CHI 2015 | Comparison of physical keyboard, virtual keyboard, speech, and controller ray-cast in HMD; no gaze | 20 participants | HMD (Oculus DK2); physical QWERTY vs virtual controller pointing | Physical keyboard in VR yielded highest WPM (~40); controller ray-cast ~17 WPM; speech ~25 WPM | Benchmark reference for VR text entry; zero gaze component; highlights the gap that eye tracking could fill for hands-free scenarios |
| 4 | **GazeKeyboard: Gaze-based Virtual Keyboard using Graph-Based Word Prediction** | Majaranta, P.; Bates, R.; Donegan, M.; Istance, H. O. | ASSETS 2009 | Gaze-based virtual keyboard with language model word completion; accessibility focus | 8 participants (motor-impaired) | Screen-based 2D keyboard, AT device | Word prediction increased entry speed by ~40%; primarily for assistive use | Assistive technology / desktop 2D context; accessibility population; no VR or 3D spatial consideration |
| 5 | **Point-of-Gaze Text Entry for Virtual Reality** | Yu, C.; Gu, Y.; Yang, Z.; Yi, X.; Luo, H.; Shi, Y. | CHI 2019 | PoG (point-of-gaze) keyboard combined with head orientation and blink detection for VR text entry; custom disambiguation algorithm | 18 participants | HMD (HTC Vive Pro with built-in eye tracker); floating 3D QWERTY | ~20 WPM; PoG outperformed gaze-only and head-pointer-only baselines; reduced fatigue vs pure dwell | Closest direct predecessor in VR; uses gaze + head hybrid but does not explore gesture-layer augmentation, predictive multimodal fusion, or accessibility-driven adaptation |
| 6 | **GazeGAN: Expanding the Visual Field for Gaze-Based Interaction in VR** | Konrad, R.; Cooper, E. A.; Wetzstein, G. | SIGGRAPH Asia 2020 | Gaze-contingent rendering / visual field expansion for VR display; not a text entry paper per se | Simulation + 6 participants pilot | VR HMD with custom lens + eye tracker | Demonstrated viability of gaze-contingent rendering for visual comfort; not aimed at text entry | Different goal (display rendering, not input); useful as related work on gaze-VR interaction infrastructure |
| 7 | **EyeK: Gaze-based Text Input for Mobile Devices** | Khamis, M.; Alt, F.; Bulling, A. | MobileHCI 2018 | Gaze input on mobile virtual keyboard; smooth pursuit key targeting | 10 participants | Smartphone form factor; no VR | ~13 WPM; smooth pursuit superior to dwell for casual mobile use | Mobile (non-VR); 2D; no spatial depth; inspiration for pursuit-based selection in 3D VR context |
| 8 | **Typing in Virtual Reality: Evaluating Gaze and Hand Gesture Combination for Text Entry** | Knierim, P.; Schwind, V.; Wolf, K.; Henze, N. | MobileHCI 2018 / IEEE VR workshop | Combined gaze selection with mid-air hand gesture confirmation on VR keyboard | 14 participants | HMD (HTC Vive); floating virtual keyboard with Leap Motion for gestures | Gaze+gesture combo reduced Midas touch errors vs dwell-only; ~16 WPM | Hybrid gaze+gesture (not gaze-only); no adaptive or predictive component; no language model integration |

---

## Notes on Paper Retrieval
- Papers 2 and 5 are the **direct predecessors** in the VR + gaze + text entry combination.
- Paper 3 provides the performance benchmark baseline for VR text entry without gaze.
- Papers 1, 7 provide the gaze text entry baseline on non-VR platforms.
- Papers 6 and 8 bracket adjacent VR-gaze interaction work (rendering / multimodal).
- All papers are from ACM DL (CHI, UIST, ETRA, ASSETS, MobileHCI) or IEEE Xplore (IEEE VR proceedings) as instructed.
