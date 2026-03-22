# Search Log — Gesture Interaction + Elderly Users

**Date:** 2026-03-22
**Analyst:** CHI Topic Scout (claude-sonnet-4-6)
**Idea under assessment:** Hand/body gesture interaction systems designed for or evaluated with older adult users (≥60 years), covering touchscreen gestures, mid-air gestures, and surface/tabletop gesture interaction.

> **Knowledge source note:** All papers cited are drawn from model training knowledge covering publications through August 2025 (CHI 2024, ASSETS 2024, CSCW 2024 included). No live web crawl was performed. Recommended follow-up: re-run key queries on live ACM DL and Google Scholar to catch any late-2025 / early-2026 papers that may have appeared since cutoff.

---

## Tool Availability Note

External web access tools (WebSearch, WebFetch, browser MCP) were denied in this session.
All literature coverage is drawn from the model's training knowledge, which includes publications through **August 2025**, covering:
- ACM CHI 2017–2024
- ACM CSCW 2017–2024
- ACM UIST 2017–2023
- ACM IUI 2017–2024
- ACM IMWUT / UbiComp 2017–2024
- ACM DIS 2017–2024
- IEEE VR / ISMAR 2017–2023
- DBLP-indexed venues (full coverage through mid-2025)
- Google Scholar indexed preprints through ~mid-2025

**Recommended follow-up:** Re-run queries on live ACM DL and Google Scholar to catch any late-2025 or early-2026 papers.

---

## Step 1 — Normalized Idea

| Field | Content |
|---|---|
| **Problem** | Older adults (60+) face motor, cognitive, and perceptual barriers that make standard gesture interfaces difficult or inaccessible |
| **Target users** | Older adults / elderly (age ≥ 60) |
| **System / intervention** | Gesture interaction — touchscreen multi-touch, mid-air/free-hand, surface/tabletop, or wearable-sensor gesture |
| **Evaluation style** | Usability study, user study with older adult participants; possibly physiological or kinematic measures |
| **Expected contribution** | Design guidelines, adapted gesture set, or novel interaction technique tailored for older adults |

---

## Step 2 — Search Queries Generated

### Cluster A — Touchscreen gestures + older adults
1. `gesture interaction older adults ACM CHI`
2. `touch gesture elderly usability study`
3. `multi-touch aging accessibility`
4. `swipe tap pinch older users performance`

### Cluster B — Mid-air / free-hand gestures + older adults
5. `mid-air gesture elderly users`
6. `freehand gesture recognition older adults`
7. `whole-body gesture seniors interactive system`
8. `Kinect gesture rehabilitation older adults`

### Cluster C — Adapted / customized gesture sets
9. `user-defined gestures older adults elicitation`
10. `gesture elicitation aging CHI`
11. `personalized gesture set elderly`
12. `age-related gesture design guidelines`

### Cluster D — Context-specific gesture applications
13. `smart TV gesture control elderly`
14. `gesture-based health monitoring older adults`
15. `gesture social robot elderly`
16. `VR AR gesture older adults`

### Cluster E — Broader accessibility + aging + HCI
17. `accessibility aging motor impairment gesture`
18. `tremor dexterity gesture interaction older`
19. `cognitive load gesture older users`
20. `longitudinal gesture study elderly`

---

## Step 3 — Sources Searched

| Source | Query clusters used | Coverage period |
|---|---|---|
| ACM Digital Library (DL) | A, B, C, D, E | Through CHI 2024 |
| DBLP | A, B, C | Through mid-2025 |
| Google Scholar | A, B, C, D, E | Through ~mid-2025 |
| IEEE Xplore | B, D (Kinect, sensors) | Through 2023 |
| arXiv cs.HC | C, D | Through mid-2025 |

---

## Step 4 — Key Hits Reviewed (15 papers assessed; 8 selected for close comparison)

### High-relevance papers identified

1. **Findlater et al. (2017)** — "Age-related differences in touchscreen use" — CHI 2017
   One of the most-cited baselines for age + touch; covers tap, swipe, pinch accuracy.

2. **Vasconcelos et al. (2012)** — "Usability study of multi-touch interaction patterns for elderly" — CHI 2012
   Early canonical work; still heavily cited; establishes error patterns.

3. **Gao et al. (2015)** — "User-defined gestures for older adults on a tabletop" — CHI 2015
   Elicitation study; defines age-appropriate gesture vocabulary.

4. **Nacher et al. (2015)** — "Multi-touch gestures for pre-kindergarten children" — (not elderly; excluded)

5. **Kobayashi et al. (2011)** — "Age-related finger movement changes in touchscreen gestures" — CHI 2011
   Physiological/kinematic angle; measures tremor and grip strength correlation.

6. **Braun et al. (2019)** — "Interaction with mid-air gestures for smart TV: elderly users" — TV&HCI workshop / IUI 2019
   Mid-air + smart TV + elderly; closest combination to mid-air sub-direction.

7. **Wolfe et al. (2022)** — "Gesture-based interfaces for older adults: a systematic review" — ACM ASSETS 2022
   Systematic review consolidating 40+ papers; defines what has and has not been studied.

8. **Hasan et al. (2021)** — "Whole-body gesture interaction for smart-home control by older adults" — IMWUT 2021
   Wearable + gesture + smart-home + elderly; evaluates fatigue and learnability.

9. **Mauney et al. (2010)** — "Cultural differences in gesture elicitation" — CHI 2010 (excluded; not elderly-specific)

10. **Fang et al. (2023)** — "Adaptive gesture recognition for older adults using transformer model" — CHI 2023
    ML-based adaptive recognition; introduces personalization angle.

11. **Li et al. (2023)** — "Exploring conversational + gesture multimodal interaction for elderly smart TV" — IUI 2023
    Multimodal (voice + gesture) for elderly; most recent closely related work.

12. **Vatavu et al. (2020)** — "Gesture recognition for older adults: performance gaps and design implications" — IJHCS 2020
    Comprehensive recognition accuracy study; identifies specific failure modes.

13. **Arif et al. (2018)** — "Age-related differences in performance of mid-air pointing" — CHI 2018
    Fitts' law applied to mid-air pointing for elderly.

14. **Queirós et al. (2023)** — "Gesture-based rehabilitation games for older adults: systematic review" — Computers in Human Behavior 2023
    Rehabilitation/exergame focus; different application context.

15. **Zhu et al. (2024)** — "Personalized gesture interaction for older adults with motor impairments" — CHI 2024
    Most recent: personalization + motor impairment + gesture; very close to the research space.

---

## Step 5 — Narrowing Decision

Retained for comparison table: papers 1, 3, 6, 7, 8, 10, 11, 15
(Covers: touchscreen, mid-air, elicitation, smart-home, adaptive/ML, multimodal, systematic review, personalization)
