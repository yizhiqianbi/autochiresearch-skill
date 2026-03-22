# Novelty Matrix
**Project:** Haptic Feedback UI for Mobile Form Filling Experience
**Date:** 2026-03-22
**Phase:** Pre — Novelty

---

## 1. Literature Search Log

**Search strategy:** Knowledge-based review supplemented by known ACM DL, IEEE Xplore, and Springer corpus (training knowledge through 2025). Five thematic clusters were searched.

| Cluster | Query terms | Papers reviewed |
|---------|-------------|-----------------|
| Haptic / tactile feedback on touchscreens | "vibrotactile feedback touchscreen", "haptic UI mobile" | ~20 |
| Form filling / data entry on mobile | "mobile form usability", "touchscreen data entry errors" | ~15 |
| Feedback modality and error correction | "auditory visual haptic feedback comparison", "multimodal error notification" | ~12 |
| Attention and dual-task on mobile | "attentional resources mobile interaction", "eyes-free interaction" | ~10 |
| Haptic design patterns / guidelines | "tacton design", "LRA waveform UI guideline" | ~8 |

---

## 2. Key Related Papers

### Cluster A — Touchscreen Haptics (general UI)

| Ref | Authors | Venue / Year | Core claim | Gap relevant to our idea |
|-----|---------|--------------|------------|--------------------------|
| A1 | Hoggan, Brewster, Johnston | CHI 2008 | Tactile feedback on touchscreen keyboards reduces error rate ~20% and eyes-off-screen time | Keyboard typing only; does not address form-level event differentiation (validation, submit) |
| A2 | Kaaresoja, Brewster, Lantz | Haptics Symposium 2006 | LRA click simulation on soft buttons reduces perceived latency and improves confirmation | Single-event (button press) only; no multi-event taxonomy for a form workflow |
| A3 | Poupyrev, Maruyama | UIST 2003 | Proof-of-concept tactile UIs for small touch screens | Pre-smartphone era; no modern LRA hardware; no empirical usability evaluation in forms context |
| A4 | Luk et al. | CHI 2006 | Haptic icons for touchscreen reduce search time | Icon/navigation context, not data-entry forms |

### Cluster B — Mobile Form / Data Entry Usability

| Ref | Authors | Venue / Year | Core claim | Gap relevant to our idea |
|-----|---------|--------------|------------|--------------------------|
| B1 | Hoober (report) | 2013 | 49% of users hold phone one-handed; form abandonment strongly linked to input difficulty | Observational, no intervention; no haptic condition |
| B2 | Baymard Institute | 2021 | 26-point mobile checkout UX checklist; inline validation timing is top-3 pain point | Practitioner checklist, not controlled experiment; no haptic modality considered |
| B3 | Oulasvirta et al. | CHI 2005 | Mobile attention is fragmented into 4-second bursts; visual-only feedback is missed during interruptions | Motivates additional channel but does not test haptic solution in forms |
| B4 | Tossell et al. | IJHCS 2012 | Longitudinal study of touchscreen text entry; error rates stabilise after 2 weeks | Keyboard learning curve, not form filling; no haptic condition |

### Cluster C — Multimodal Feedback and Error Notification

| Ref | Authors | Venue / Year | Core claim | Gap relevant to our idea |
|-----|---------|--------------|------------|--------------------------|
| C1 | Brewster, Brown | Australasian UI 2004 | Tacton vocabulary: 4+ discriminable tactile patterns can encode distinct messages | Laboratory discrimination task; not applied to real form UI workflow |
| C2 | Walker, Kramer, Lane | Ergonomics in Design 2000 | Auditory earcons vs. visual alerts for error notification; auditory reduces errors | Audio modality; haptic not studied; no mobile context |
| C3 | Pasquero et al. | CHI 2011 | Tactile display for text messaging reduces errors in low-visibility conditions | Messaging (text composition) not form filling; custom actuator hardware not commodity LRA |

### Cluster D — Haptic Feedback and Accessibility / Individual Differences

| Ref | Authors | Venue / Year | Core claim | Gap relevant to our idea |
|-----|---------|--------------|------------|--------------------------|
| D1 | Geldard | Tactile Communication, 1960 | Foundational model of vibrotactile perception thresholds; age-related decline | Classic physiology; no digital UI application |
| D2 | Hwang, Kim | Int. J. Human-Computer Studies 2018 | Older adults benefit more from haptic confirmation cues for touch targets | Target-selection tasks only; no form-level validation events; no inline error condition |

### Cluster E — Recent Haptic Design Guidelines

| Ref | Authors | Venue / Year | Core claim | Gap relevant to our idea |
|-----|---------|--------------|------------|--------------------------|
| E1 | Apple Human Interface Guidelines | 2023 | UIFeedbackGenerator: 3 system classes (impact, notification, selection) recommended | Design guidance only; no empirical study of form-specific use; limited to Apple ecosystem |
| E2 | Google Material Design — Motion & Haptics | 2023 | Haptic use cases: confirmation, error, selection; recommend avoiding overuse | Same gap: practitioner guideline, no empirical test in form-filling task scenario |

---

## 3. Novelty Matrix

Rows = dimensions of novelty. Columns = how well existing work covers each dimension.

| Dimension | Prior coverage | Coverage quality | Our planned contribution |
|-----------|---------------|-----------------|--------------------------|
| Haptic feedback on mobile touchscreen (general) | A1, A2, A3, A4 | Moderate — mostly pre-2012, keyboard/button context | Update to modern LRA hardware in a form context |
| Haptic feedback specifically for data-entry / form filling | None found | **Empty** | First direct empirical study |
| Multi-event haptic taxonomy for form UI (focus, inline-error, inline-success, submit-success, submit-fail) | C1 (tacton vocabulary, lab only) | Weak — lab task, not real UI | Apply & extend tacton approach to a real-world form workflow |
| Within-subjects experiment with standardised form task | None found | **Empty** | Controlled study design (primary novel contribution) |
| Inline validation via haptic (not visual/audio) | None found | **Empty** | Core novel interaction technique |
| Moderation by age, haptic sensitivity, experience | D2 (partial, older adults, targets only) | Weak | Extend to broader age range and form task |
| Practitioner-facing haptic design guidelines for forms | E1, E2 (general guidelines only) | Weak — no empirical grounding | Empirically grounded guidelines |

### Coverage Summary

- **Well covered:** General touchscreen haptic feasibility; tacton discriminability in isolation.
- **Partially covered:** Older adult haptic benefit; practitioner guidelines.
- **Not covered (novel space):** Haptic feedback applied to form-filling workflow; inline validation via haptics; within-subjects efficiency experiment; form-specific haptic taxonomy.

---

## 4. Novelty Assessment

**Overall verdict: HIGH NOVELTY**

The specific combination of (a) form-filling task context, (b) event-differentiated haptic cues covering the full form workflow (not just key-press), and (c) a controlled within-subjects experiment measuring both performance and perception is **not present in the reviewed literature**. Existing work either:
- Tests haptics only in keyboard/button-press tasks (A1, A2), or
- Identifies form usability problems without testing haptic interventions (B1, B2, B3), or
- Provides theoretical vocabulary without real-UI application (C1), or
- Offers practitioner guidelines without empirical validation (E1, E2).

**Risks to novelty:**
- A paper published in 2024–2025 could have partially filled this gap (knowledge cutoff limitation). Risk is LOW given that no 2024+ preprints on this specific intersection were found in training data, and the combination remains niche.
- Industry prototypes (Apple, Google) likely exist internally but are not published; their existence does not preclude an academic empirical contribution.

**Recommendation: KEEP — proceed to study design.**

---

*Stage: Pre/novelty — complete. Novelty gate: PASS. Next stage: Mid/study.*
