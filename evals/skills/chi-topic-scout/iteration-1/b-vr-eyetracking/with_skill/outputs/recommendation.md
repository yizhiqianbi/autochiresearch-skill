# Recommendation: Keep / Pivot / Drop
**Topic:** Eye-tracking-assisted text input in VR environments
**Date:** 2026-03-22

---

## Decision: PIVOT

---

## Rationale

The broadest framing of this idea — "use eye tracking to help with text input in VR" — is no longer novel at the level required for a CHI full paper. GazeType (ETRA 2018) and Yu et al. CHI 2019 both implement and evaluate gaze-based VR text entry with real eye trackers inside HMDs, reaching ~14-20 WPM and publishing results at high-quality venues. A straight replication or incremental parameter sweep (different dwell threshold, slightly different keyboard layout, another HMD model) would be desk-rejected as insufficient novelty at CHI or UIST. This makes a naive "keep" untenable.

However, the broader research space around gaze + VR + text is alive with open sub-problems, several of which have strong novelty and would support compelling CHI-level contributions. The recommendation is therefore a targeted pivot rather than a drop: retain the VR + eye-tracking frame but commit to one of the following differentiated angles.

---

## Recommended Pivot Directions (ranked by novelty + feasibility)

### Pivot 1 (STRONGEST — recommended): Adaptive LLM-Augmented Gaze Text Entry in VR
**What it is:** Integrate a neural language model (e.g., a small transformer-based next-word predictor or character-level model) directly into the VR gaze keyboard loop to reduce the number of gaze fixations required per word. The system predicts completions from partial gaze paths and allows the user to confirm with a single dwell or blink.

**Why novel:** No paper combines modern neural language modeling with gaze text entry in VR. Desktop gaze systems used n-gram word lists (Majaranta 2009); no VR system has used a learned model. The interaction design challenge (when to show suggestions without cluttering the VR field of view, how to confirm with gaze alone) is genuinely unsolved.

**Contribution type:** Technique + empirical user study.
**Target venue:** CHI 2027 or UIST 2027.
**Risk:** Moderate. Eye tracking SDK access required (Tobii, Meta Quest Pro, PICO 4 Enterprise). Main challenge is low-latency integration with VR rendering loop.

---

### Pivot 2 (HIGH novelty): 3D-Optimized Keyboard Layout for Gaze in VR
**What it is:** Design a non-QWERTY keyboard layout optimized for the biomechanics of eye movement in 3D space (saccade amplitude distributions, vergence fatigue, depth-plane placement). Evaluate against flat QWERTY with a controlled user study.

**Why novel:** All existing VR gaze text papers use a QWERTY layout ported from 2D with minimal spatial adaptation. Layout optimization for 2D gaze keyboards has been done (e.g., OPTIGAZE), but nobody has applied this to 3D VR constraints where saccade direction costs differ from 2D.

**Contribution type:** Design + empirical comparison study.
**Target venue:** CHI 2027.
**Risk:** Medium-high. Layout optimization requires an optimization pass before user study; needs >20-session study to show learning curve.

---

### Pivot 3 (HIGH novelty + ASSETS path): Accessibility-First Gaze VR Text Entry
**What it is:** Design and evaluate gaze text entry in VR specifically for users with motor impairments (e.g., ALS, spinal cord injury). VR offers a hands-free immersive environment that could benefit this population uniquely, but no study has recruited motor-impaired users in a VR gaze text context.

**Why novel:** Desktop gaze AT has a 15-year history; VR is an entirely new environment for this population. Research questions about fatigue, comfort, dwell calibration, and social VR participation are open.

**Contribution type:** User study + design guidelines.
**Target venue:** ASSETS 2026 or CHI 2027.
**Risk:** Low-medium technically; higher for IRB and participant recruitment.

---

### Pivot 4 (MODERATE novelty): Gaze + Voice Multimodal Confirmation for VR Text
**What it is:** Use gaze to position the cursor on a virtual keyboard, voice (speech phoneme detection, not full ASR) to confirm selection. Addresses Midas touch without requiring hands.

**Why novel:** Knierim 2018 did gaze + hand gesture; Yu 2019 did gaze + head; nobody has done gaze + voice-confirmation (distinct from pure speech-to-text). Adds a hands-free advantage relevant to scenarios where controllers are absent.

**Contribution type:** Technique + controlled comparison study.
**Target venue:** CHI 2027 or MobileHCI 2026.
**Risk:** Lower technical risk; main challenge is latency of phoneme detection.

---

## What to Drop

A project framed purely as "we built a gaze VR keyboard and measured WPM" should be dropped for CHI submission — the basic feasibility result already exists in the literature. A replication study might be suitable for a short CHI paper or workshop if combined with a new HMD/platform, but would not be competitive as a full paper.

---

## Decision Summary

| | Framing | Decision |
|-|---------|----------|
| Generic gaze VR keyboard (dwell/PoG) | Already done (CHI 2019) | DROP |
| Gaze + head hybrid | Already done (CHI 2019) | DROP |
| Gaze + gesture hybrid | Mostly done (2018, small N) | PIVOT required to add LM or larger study |
| LLM-augmented gaze VR text | Open | KEEP (as Pivot 1) |
| 3D-optimized layout for gaze VR | Open | KEEP (as Pivot 2) |
| Accessibility gaze VR text | Open | KEEP (as Pivot 3) |

**Bottom line:** Pivot to Pivot 1 (LLM-augmented gaze VR text entry) for highest CHI novelty and timeliness. If no GPU/inference infrastructure is available, Pivot 3 (accessibility) is the second-best option with a clearer path to ASSETS and CHI.
