# Keep-or-Pivot Decision
**Project:** Haptic Feedback UI for Mobile Form Filling Experience
**Date:** 2026-03-22
**Phase:** Pre — Novelty Gate

---

## Decision

**KEEP** — proceed to Mid/study stage.

---

## Rationale

### Evidence for keeping

1. **Empty novelty cell on the core claim.** No published controlled experiment studies haptic feedback in a form-filling workflow. The combination of (a) event-differentiated haptic cues, (b) a realistic multi-field form task, and (c) within-subjects performance + perception measurement is new.

2. **Strong motivating literature.** Prior work on touchscreen keyboard haptics (Hoggan et al., CHI 2008) shows consistent error-rate and attention benefits, providing a plausible mechanism for transfer to form tasks. The effect size reported (≈20% error reduction) is large enough to power a feasible study.

3. **Clear practical relevance.** Mobile form abandonment and inline-validation miss-rates are well-documented industry pain points (Baymard 2021; Hoober 2013). A positive result would have immediate design implications for UIKit and Jetpack Compose.

4. **Tractable scope.** The study requires a single-platform prototype app and a within-subjects lab/remote protocol. No exotic hardware: commodity Android LRA is sufficient.

5. **Fits CHI contribution types.** The planned output satisfies at least two CHI contribution types: (i) empirical finding and (ii) design guidelines — both well-represented at CHI venues.

### Risks reviewed and mitigated

| Risk | Severity | Mitigation |
|------|----------|-----------|
| A 2024–2025 paper fills the gap | Low | Closest papers remain in keyboard/button space; conduct updated ACM DL search before submission |
| LRA hardware variation across devices confounds results | Medium | Standardise on a single device model per condition; report device specs; run sensitivity analysis |
| Haptic annoyance / fatigue over repeated trials | Medium | Include a haptic annoyance sub-scale in questionnaire; limit form repetitions to 3 per condition with rest breaks |
| Small effect size requiring large N | Low–Medium | Power analysis based on Hoggan 2008 (d ≈ 0.6) yields N ≈ 28 at 80% power; planned N = 32 provides buffer |
| Participants habitually mute vibration | Low | Screen during recruitment; report percentage in methods |

### Pivot options considered and rejected

| Option | Why rejected |
|--------|-------------|
| Pivot to audio cues instead of haptic | Audio is already studied (Walker & Kramer 2000); haptic remains the gap |
| Pivot to haptic feedback for navigation (not forms) | Covered by Luk et al. 2006 and others; lower novelty |
| Narrow to accessibility only (visual impairment) | Reduces generalisability; better as follow-on study |
| Drop and select a different idea | Not warranted given high novelty score |

---

## Next Steps

Proceed immediately to **Mid/study** stage:
- Design within-subjects controlled experiment
- Define prototype conditions (haptic vs. no-haptic)
- Define task scenario, dependent variables, and questionnaire battery
- Conduct a priori power analysis
- Write study-spec.md

---

*Gate decision: KEEP. Confidence: HIGH.*
