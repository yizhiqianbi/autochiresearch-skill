# Research Brief
**Project:** Haptic Feedback UI for Mobile Form Filling Experience
**Date:** 2026-03-22
**Phase:** Pre — Brief

---

## 1. Core Idea

Design and evaluate a haptic feedback layer integrated into mobile form UIs to improve the form-filling experience on touchscreen devices. The system delivers contextually differentiated vibrotactile cues at key interaction moments — field focus, input validation (inline error / success), field completion, and form submission — with the goal of reducing errors, lowering completion time, and improving perceived usability and confidence.

---

## 2. Motivation and Problem Space

Mobile form filling is one of the most friction-laden tasks on touchscreen devices. Users must (a) navigate small tap targets, (b) decipher inline validation messages while the soft keyboard obscures content, (c) detect when they have skipped required fields, and (d) confirm that submission succeeded — all with limited screen real estate and no physical keyboard feedback. Error rates and abandonment rates for mobile forms consistently exceed those of desktop equivalents (Oulasvirta et al., 2013; Hoober, 2013; Baymard Institute, 2021).

Haptic feedback — primarily short-burst vibrotactile patterns delivered by a linear resonant actuator (LRA) or eccentric rotating mass (ERM) motor — is already present in most mid-to-high-end smartphones and is routinely used for keyboard key clicks, notifications, and navigation confirmation in iOS (UIFeedbackGenerator) and Android (VibrationEffect API). However, its systematic application to form UIs remains largely unexplored: most apps either suppress all haptics or reuse a single generic buzz.

Filling this gap has practical value. When users cannot see validation state clearly (e.g., one-handed use, bright outdoor light, attention divided), a distinct tactile signal could serve as an additional sensory channel that reduces reliance on visual feedback alone.

---

## 3. Research Questions

**RQ1.** Does incorporating event-differentiated haptic feedback in a mobile form UI reduce form completion time compared to a visuals-only baseline?

**RQ2.** Does haptic feedback reduce the number of user-initiated error corrections (field re-entries) before successful submission?

**RQ3.** How do users perceive usability (SUS), frustration, and confidence with haptic vs. non-haptic form UIs?

**RQ4.** Do individual differences (haptic sensitivity, prior smartphone experience, age) moderate the effect of haptic feedback on task performance and perception?

---

## 4. Proposed Contribution

1. **Empirical evidence:** A controlled within-subjects experiment quantifying the effect of form-specific haptic feedback on efficiency (time, error count) and perceived quality (SUS, NASA-TLX frustration subscale, custom confidence scale).
2. **Design taxonomy:** A minimal set of haptic event types for form UIs (focus, inline error, inline success, field completion, form submit success, form submit failure) with recommended LRA waveform parameters drawn from existing haptic design guidelines.
3. **Design guidelines:** Practitioner-facing recommendations for when and how to apply haptic cues in mobile forms, including accessibility considerations and opt-in/opt-out patterns.

---

## 5. Relevant Prior Work (to be expanded in novelty stage)

| # | Paper | Venue | Year | Key finding |
|---|-------|-------|------|-------------|
| 1 | Hoggan et al., "Investigating the Effectiveness of Tactile Feedback for Mobile Touchscreens" | CHI | 2008 | Tactile feedback reduces eyes-off-screen time and error rate on touchscreen keyboards |
| 2 | Brewster & Brown, "Tactons: Structured tactile messages for non-visual information display" | Australasian UI | 2004 | Tacton vocabulary enables discrimination of ≥4 distinct tactile events |
| 3 | Oulasvirta et al., "Interaction in 4-second bursts: The fragmented nature of attentional resources in mobile HCI" | CHI | 2005 | Attention fragmentation on mobile devices amplifies value of non-visual feedback |
| 4 | Poupyrev & Maruyama, "Tactile Interfaces for Small Touch Screens" | UIST | 2003 | Early demo of touchscreen haptics for UI confirmation |
| 5 | Kaul et al., "HapticHead: A Spherical Vibrotactile Grid Around the Head for 3D Guidance" | CHI | 2017 | Differentiable vibrotactile patterns for spatial navigation guidance |
| 6 | Kaaresoja et al., "Snap, Crackle, Pop: Tactile Feedback for Mobile Touch Screens" | Haptics Symposium | 2006 | LRA feedback for touchscreen button-press reduces perceived latency |
| 7 | Lee & Starner, "Don't Bother Me: An Analysis of Ignored Notifications on Smartphones" | MobileHCI | 2010 | Notification fatigue is relevant when designing frequent haptic cues |

---

## 6. Scope and Constraints

- **Platform:** Native Android (Kotlin) or iOS (Swift) prototype, or cross-platform Flutter — targeting one platform for the study to ensure haptic fidelity.
- **Form type:** A standardized multi-field registration / checkout form (10–14 fields of mixed type: text, numeric, date, select) used in both conditions.
- **Populations:** Adult smartphone users (18–65), recruited via university participant pool or online panel.
- **Exclusions:** Participants with hand tremors, vibrotactile hypersensitivity, or who routinely mute device vibration.
- **Ethical considerations:** IRB/ethics review required; data pseudonymised; participants can disable haptics at any time.

---

## 7. Anticipated Impact

If significant effects are found, findings would directly inform mobile UI toolkits (UIKit, Jetpack Compose) and accessibility guidelines (WCAG 2.2 tactile supplement discussions). Negative or null results would also be informative, potentially reframing haptic cues as a user-controlled preference rather than a universal usability improvement.

---

*Stage: Pre/brief — complete. Next stage: Pre/novelty.*
