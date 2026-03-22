# Keep or Pivot Decision
## Project: Haptic Feedback UI for Mobile Form-Filling Experience

**Phase:** Pre — Novelty Gate
**Date:** 2026-03-22

---

## Decision Summary

**DECISION: KEEP**

The novelty matrix analysis confirms sufficient novelty to proceed to study design. The project should advance to the Mid/study phase without pivoting.

---

## Rationale

### Evidence for Keep

1. **Novel measurement (abandonment rate):** No prior work measures haptic feedback's effect on form abandonment rate. This is a practically significant outcome (abandonment is a key business metric for mobile forms) and an academic gap.

2. **Novel intersection:** The combination of (a) a realistic multi-field form task, (b) a differentiated haptic event vocabulary, (c) abandonment as DV, and (d) NASA-TLX cognitive load assessment has zero coverage in existing CHI/MobileHCI literature.

3. **Cross-device fidelity contribution:** Gap score D9 = 3 (almost completely unaddressed). Designing and testing a haptic pattern vocabulary that degrades gracefully across LRA and ERM hardware provides a methodological and design contribution independent of the main experimental results.

4. **Practical relevance:** Mobile form abandonment is a high-impact problem. Results would have clear design implications for mobile developers, accessibility practitioners, and OS-level haptic API designers.

5. **CHI relevance:** The study sits at the intersection of tactile/haptic interaction, mobile HCI, and accessibility — all well-represented CHI tracks. The empirical contribution (controlled experiment + design guidelines) matches CHI's standards for empirical papers.

### Risks Noted

| Risk | Severity | Mitigation |
|------|----------|------------|
| Haptic API fragmentation across Android devices | Medium | Standardize on iOS Taptic Engine + Android 8+ vibration patterns; document device diversity as a study variable |
| Small effect size from haptic feedback | Medium | Power analysis recommends N=32 minimum for d=0.5; recruiting 40 participants provides buffer |
| Participant smartphones required (BYOD vs. standardized device) | Medium | Use standardized test devices (2× iPhone 14, 2× Pixel 7) to control haptic hardware; report device type as covariate |
| Confound: typing speed variation in form tasks | Low | Within-subjects design controls for individual differences; counterbalancing eliminates order effects |
| PWA Vibration API limitations on iOS (Safari) | High | Implement native iOS prototype (Swift/SwiftUI) as primary; PWA as secondary/fallback |

### Alternatives Considered

| Alternative | Verdict | Reason Rejected |
|-------------|---------|-----------------|
| Pivot to audio-only feedback for form validation | Rejected | Haptic is more novel; audio feedback in forms partially studied (Brewster 2004 earcon work) |
| Narrow to accessibility-only population (blind users) | Rejected | Narrows scope unnecessarily; accessibility can be framed as an implication, not the primary sample |
| Pivot to gesture-based form navigation | Rejected | Drifts away from the haptic feedback core idea; loses the original contribution |
| Extend to wearable haptic feedback (smartwatch) | Deferred | Interesting extension but adds hardware complexity; defer to future work |

---

## Decision Conditions

The KEEP decision is conditional on:

1. The study prototype implementing at minimum 3 distinguishable haptic patterns (verified by a preliminary pattern discrimination pilot, N=5, before main study).
2. The haptic pattern vocabulary being specified in the study spec before IRB submission.
3. The study using a within-subjects design with full counterbalancing across the 3 conditions (Control, Basic Haptic, Differentiated Haptic).

---

## Next Step

Proceed to **Mid phase — Study Design** (study-spec.md).
