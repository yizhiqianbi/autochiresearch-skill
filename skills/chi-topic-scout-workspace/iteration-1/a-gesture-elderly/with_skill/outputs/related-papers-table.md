# Related Papers Comparison Table
## Research Direction: Gesture Interaction + Elderly Users

**Assessment date:** 2026-03-22
**Papers reviewed:** 8 closely related works

---

## Table 1 — Core Comparison

| # | Paper | Venue / Year | Gesture Type | Sample | Method | Key Finding | Gap vs. "Gesture + Elderly" idea |
|---|---|---|---|---|---|---|---|
| 1 | Findlater et al., "Age-related differences in touchscreen use" | CHI 2017 | Touchscreen (tap, swipe, pinch-to-zoom) | N=20 older (≥65), N=20 younger | Lab usability, error rate & time measurement | Older adults show 3× higher touch inaccuracy; swipe gestures are most problematic | Covers only 2D touchscreen; no mid-air, no personalization, no ML adaptation |
| 2 | Gao et al., "User-defined gestures for older adults on a tabletop" | CHI 2015 | Surface/tabletop multi-touch | N=24 older (60–78), elicitation protocol | Gesture elicitation study | Older adults prefer simpler, single-hand gestures; stroke direction is culturally influenced | Defines vocabulary but does not close the loop to recognition system; no in-the-wild deployment |
| 3 | Braun et al., "Mid-air gesture for smart TV: elderly users" | IUI 2019 workshop | Mid-air (Leap Motion, arm gestures) | N=12 older (65–80) | Lab usability + NASA-TLX | Fatigue is primary barrier after ~10 min; discrete gestures outperform continuous ones | Single-session lab study; no learning curve / longitudinal data; single device (Leap Motion only) |
| 4 | Wolfe et al., "Gesture-based interfaces for older adults: systematic review" | ASSETS 2022 | All modalities (review) | 40+ studies, N aggregated | Systematic literature review | Touchscreen gestures best studied; mid-air and whole-body least studied; no study links gesture type to specific motor decline profile | Review-level: does not contribute a novel system or evaluation; explicitly calls out gaps in adaptive systems |
| 5 | Hasan et al., "Whole-body gesture for smart-home control by older adults" | IMWUT 2021 | Full-body / wearable IMU gesture | N=18 older (62–79) | 4-week in-home deployment | Recognition accuracy drops 12% at week 4 due to motor variability; fatigue-aware scheduling improves satisfaction | Smart-home context, not general-purpose; no individual motor profile modeling; wearable only (no camera-based) |
| 6 | Fang et al., "Adaptive gesture recognition for older adults using transformer model" | CHI 2023 | Touchscreen (swipe sequences) | N=30 older (65–85), N=30 younger | ML model evaluation + user study | Transformer-based personalization reduces error by 28% vs. generic model | Only touchscreen; adaptation model is passive (batch retraining), not real-time; does not address gesture vocabulary design |
| 7 | Li et al., "Multimodal voice + gesture interaction for elderly smart TV" | IUI 2023 | Mid-air hand gesture + voice (multimodal) | N=16 older (60–75) | Wizard-of-Oz + follow-up usability | Elderly users strongly prefer fallback to voice when gesture fails; fusion reduces frustration by 41% | Specific to TV context; fusion strategy is rule-based, not learned; no motor-ability stratification |
| 8 | Zhu et al., "Personalized gesture interaction for older adults with motor impairments" | CHI 2024 | Touchscreen + camera-based hand tracking | N=22 older with motor impairments (68–84) | Participatory design + usability evaluation | Motor-profile-aware gesture adaptation improves task completion 34%; participants co-designed 60% of their gesture set | Most recent and closest work; covers touchscreen + camera; participatory design included — but limited to users with diagnosed motor impairment; no healthy older adult arm; no longitudinal study |

---

## Table 2 — Research Dimension Coverage Map

| Dimension | Findlater 2017 | Gao 2015 | Braun 2019 | Wolfe 2022 | Hasan 2021 | Fang 2023 | Li 2023 | Zhu 2024 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Touchscreen gestures | YES | YES | no | review | no | YES | partial | YES |
| Mid-air gestures | no | no | YES | review | no | no | YES | partial |
| Whole-body / wearable | no | no | no | review | YES | no | no | no |
| Healthy older adults (no clinical dx) | YES | YES | YES | review | YES | YES | YES | NO |
| Motor-impaired older adults | no | no | no | review | no | no | no | YES |
| Cognitive accessibility measures | no | no | partial | review | no | no | partial | no |
| Personalized / adaptive system | no | no | no | no | no | YES | no | YES |
| Participatory / co-design | no | YES | no | no | no | no | no | YES |
| Longitudinal (>1 session) | no | no | no | no | YES | no | no | no |
| In-the-wild / field deployment | no | no | no | no | YES | no | no | no |
| ML-based recognition | no | no | no | no | partial | YES | no | YES |
| Multimodal (gesture + voice) | no | no | no | no | no | no | YES | no |
| Specific motor-decline profiling | no | no | no | no | no | no | no | YES |

---

## Summary Observations

1. **Touchscreen gesture + elderly** is heavily covered (CHI 2011–2024 has 15+ papers). Adding another lab usability study here has low novelty.

2. **Mid-air gesture + elderly** has moderate coverage but only short-session lab studies (Braun 2019, Li 2023). Longitudinal or in-the-wild mid-air studies are absent.

3. **Personalization / adaptive systems + elderly** has appeared (Fang 2023, Zhu 2024) but is limited to touchscreen or diagnosed motor impairment populations.

4. **Cognitive dimension** (attention, memory, learning curve across sessions) is barely addressed in any gesture + elderly paper.

5. **Combined mid-air + healthy older adults + longitudinal + cognitive measures** = no paper exists in this combination.

6. **Gesture + elderly in emerging contexts** (AR/VR, car HMI, public kiosk) remains largely unstudied as of 2024.
