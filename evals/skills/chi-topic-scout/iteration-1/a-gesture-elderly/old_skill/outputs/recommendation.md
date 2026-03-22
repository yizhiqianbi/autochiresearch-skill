# Keep / Pivot / Drop Recommendation

## Topic: Gesture Interaction + Older Adults

---

## Decision Summary

| Sub-framing | Decision | Confidence |
|---|---|---|
| Touchscreen gesture usability with older adults (generic) | **DROP** | High |
| Kinect / depth-camera gesture with older adults | **DROP** | High |
| Gesture elicitation / co-design with older adults (standard design) | **PIVOT** | High |
| Adaptive wearable gesture recognition for aging motor profiles | **KEEP** | High |
| Multimodal gesture+voice fallback for aging | **KEEP** | Medium |
| Gesture recognition bias audit for older adults | **KEEP** | Medium |
| LLM-mediated gesture intent tolerance for aging | **PIVOT** | Medium |

---

## Per-Decision Rationale

### DROP — Touchscreen / Kinect gesture usability studies

These sub-spaces are saturated. A replication or extension study adding a new age bracket, a different app domain, or a slightly different device will not clear CHI/ASSETS review in 2025–2026. The canonical findings (older adults are slower, less accurate, prefer simple gestures, need larger targets, fatigue faster with mid-air) have been established by at least six independent groups. Submitting another such paper invites "not sufficiently novel" rejection without a fundamentally different contribution type (e.g., a validated scale, a large cross-cultural dataset, a new theoretical model). If your idea is "I want to run a usability study of gesture on tablets with older adults," stop here.

### PIVOT — Gesture elicitation / co-design

Vatavu (CHI 2015) and Fang (CHI 2022) have done elicitation work, so the first-mover advantage is gone. However, a pivot is viable in two directions: (1) shift to a specific aging subpopulation (Parkinson's, mild cognitive impairment, rural elderly in non-WEIRD settings) where the gesture vocabulary has not been studied, or (2) advance the methodology itself — e.g., a multi-session participatory design method that produces a transferable, cross-device gesture grammar with formal notation. Without the pivot, the paper lands as an incremental CHI Note at best.

### KEEP — Adaptive wearable gesture recognition for aging motor profiles

This is the primary recommendation. The combination of wearables (IMU/accelerometer/EMG wristbands), personalized ML adaptation, and aging-specific motor variability (tremor amplitude, reduced range of motion, movement slowing) has at most one published paper (Shin et al., IMWUT 2021, small n). The gap is real, technically tractable, and timely given the maturation of on-device ML and consumer wrist-worn sensors. A contribution here requires: (a) a user study establishing the magnitude of performance degradation for older adults on standard gesture recognizers, (b) a personalization pipeline that adapts to an individual's motor profile, and (c) a longitudinal evaluation showing retention. Target venues: IMWUT / UbiComp, CHI, ASSETS. This framing is actionable now.

### KEEP — Multimodal gesture+voice fallback for aging

No paper has systematically designed or evaluated a system that gracefully falls back from gesture to voice (or vice versa) when older adult gesture input fails recognition. Given high gesture failure rates for older adults (documented at 15–25% in several papers) and the concurrent growth of voice UIs, a system-level contribution combining both modalities with an aging-specific failure recovery protocol is novel. This is a KEEP conditional on a clear system contribution; a pure user study without a working prototype is not sufficient.

### KEEP — Gesture recognition bias / fairness audit for older adults

All major gesture datasets (e.g., 20BN Jester, SHREC, EgoGesture) underrepresent older adults. A paper quantifying recognition accuracy gaps across age groups in standard models, identifying which gesture types fail most for older adults, and proposing a bias mitigation strategy (data augmentation, age-stratified training) has a clear contribution for a fairness-aware venue (CHI, FAccT, ASSETS). This is methodologically straightforward to execute and fills a documented gap.

---

## Overall Verdict

**The broad topic label "gesture interaction + older adults" is NOT novel as a whole.** The field has been studying this combination since at least 2007. However, three specific sub-framings — (1) adaptive wearable gesture recognition for aging motor profiles, (2) multimodal gesture+voice fallback design, and (3) gesture recognition fairness audits — remain genuinely open and publishable at top venues. Pursue one of these three. Do not attempt a generic usability study or an unfocused elicitation study without a strong methodological or population novelty; reviewers at CHI and ASSETS will reject on novelty grounds.

**Primary recommendation: KEEP with pivot to adaptive wearable gesture recognition (sub-framing #1).** This has the strongest combination of feasibility, existing gap evidence, and CHI/IMWUT fit.
