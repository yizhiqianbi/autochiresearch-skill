# Research Brief
## Project: Haptic Feedback UI for Mobile Form-Filling Experience

**Phase:** Pre — Brief
**Date:** 2026-03-22
**Idea (raw):** 触觉反馈 UI 对移动端表单填写体验 (Haptic Feedback UI for Mobile Form-Filling Experience)

---

## 1. Research Motivation

Mobile form filling is one of the most friction-laden tasks on touchscreen devices. Users must navigate multiple input fields (text, dropdowns, toggles, date pickers) with no physical landmark feedback—everything is visually mediated. Errors accumulate silently, completion rates on mobile forms lag behind desktop equivalents, and abandonment rates remain high (industry benchmarks: 67–80% abandonment for multi-step mobile forms).

Haptic actuators (primarily linear resonant actuators, LRAs, and eccentric rotating mass motors, ERMs) are now standard hardware on modern smartphones (iOS Taptic Engine since 2015; Android vibration APIs widely available). Despite this, haptic feedback in UI workflows is largely confined to discrete events (keyboard clicks, notification buzzes) rather than integrated into the continuous, structured interaction flow of form completion.

A principled haptic design layer embedded within form UI could:
- Signal field state transitions (empty → focused → validated → error) through distinct vibration patterns
- Reduce visual attention demands during field navigation
- Lower cognitive load by offloading error signalling from the visual channel
- Improve accessibility for users with visual impairments

---

## 2. Research Question

**RQ1 (Primary):** Does a haptic feedback layer integrated into a mobile form UI reduce task completion time and error rate compared to a no-haptic baseline?

**RQ2 (Secondary):** Does the haptic feedback layer influence perceived usability (SUS scores) and subjective satisfaction?

**RQ3 (Exploratory):** Which specific form interaction events (field focus, validation success, validation error, submission) benefit most from haptic augmentation, and do users prefer different haptic pattern intensities across event types?

---

## 3. Background and Related Work

### 3.1 Haptic Feedback in Mobile Interaction (general)

- **Brewster & Brown (2004)** introduced "tactons"—structured tactile messages analogous to earcons—establishing a vocabulary for communicating information through vibrotactile patterns. Their work demonstrated that humans can distinguish at least 3–5 distinct vibration patterns reliably.
- **Poupyrev & Maruyama (2003)** investigated touchscreen haptics augmentation for menu selection, finding 10–15% faster target acquisition with tactile confirmation.
- **Hoggan et al. (CHI 2008)** found that tactile feedback on touchscreen keyboards improved text entry speed by ~20% and error rate by ~10% versus visual-only feedback.
- **Luk et al. (CHI 2006)** demonstrated that vibrotactile feedback improved button-press confirmation on mobile devices, reducing the need for visual fixation.

### 3.2 Mobile Form Usability

- **Wroblewski (2008)** — "Web Form Design" (Rosenfeld Media) provides the canonical UX framework; shorter forms, inline validation, and field grouping reduce abandonment.
- **Linderman & Fried (Basecamp/37signals, 2009)** empirically documented abandonment hotspots in multi-step mobile forms, identifying validation feedback timing as a key variable.
- **Kieffer et al. (MobileHCI 2017)** studied inline vs. deferred validation on mobile forms, finding that real-time inline validation reduced error correction attempts by 22%.
- **Balagtas-Fernandez & Hussmann (MobileHCI 2009)** showed that simplifying form layouts on small screens significantly improved completion rates and user satisfaction.

### 3.3 Haptic Feedback + Error Signalling

- **Immersion Corporation (2016) white paper** — Industry study showing haptic confirmation of UI events (button presses, toggles) reduced user uncertainty and repeat-tap behavior.
- **Schneider et al. (IEEE Transactions on Haptics 2017)** studied multimodal feedback in touchscreen interaction, finding visual-haptic combinations outperformed either modality alone for error detection tasks.
- **Maclean (2008, "Haptic Interaction Design")** — foundational review noting that haptic feedback is most effective for events requiring rapid confirmation with low attentional cost, matching form validation scenarios.

### 3.4 Accessibility and Haptic UI

- **Kane et al. (CHI 2011)** — "Slide Rule" system provided non-visual touchscreen interaction for blind users via vibration and audio, demonstrating that well-designed tactile cues can replace visual channel for state communication.
- **Guerreiro et al. (Assets 2008)** — studied vibrotactile feedback for accessible mobile interaction, confirming that distinct patterns improve form field navigation for low-vision users.

### 3.5 Identified Gaps

1. No controlled study isolates haptic feedback as the independent variable within a realistic multi-field mobile form task (most prior work uses synthetic button/keyboard tasks).
2. No research maps distinct haptic events to the specific form lifecycle states (focus, inline validation success/error, submission success/error).
3. No study measures the interaction between haptic design complexity (number of distinct patterns) and cognitive load on form completion.
4. Prior work rarely measures abandonment rate—only task completion time and error rate—missing a real-world relevant outcome.

---

## 4. Proposed Contribution

This project proposes a **within-subjects controlled experiment** comparing three conditions:
1. **Control (C):** Standard mobile form, no haptic feedback
2. **Basic Haptic (BH):** Single vibration pulse on all feedback events
3. **Differentiated Haptic (DH):** Distinct vibration patterns per event type (focus, success, error, submission)

The study will measure task completion time, error rate, SUS score, NASA-TLX cognitive load, and abandonment rate on a realistic multi-step registration/checkout form prototype.

---

## 5. Target Venue

CHI 2027 (Papers track); secondary: MobileHCI 2026 (Short Papers track if scope is reduced)

---

## 6. Open Questions Before Study Design

1. What haptic pattern vocabulary to use, and how to ensure patterns are distinguishable across device models (LRA vs. ERM)?
2. Should the prototype be implemented as a native iOS/Android app or a web app (PWA) using the Vibration API?
3. Should the form domain be neutral (registration form) or ecologically valid (e-commerce checkout, health intake form)?
4. Will the study be conducted in-lab (controlled) or remote (higher ecological validity, lower control)?
5. What is the appropriate sample size to detect a medium effect size (Cohen's d = 0.5) with 80% power?
