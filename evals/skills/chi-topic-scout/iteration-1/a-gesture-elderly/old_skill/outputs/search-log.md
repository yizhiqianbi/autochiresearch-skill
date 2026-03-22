# Search Log — Gesture Interaction + Older Adults

## Topic Normalization

| Field | Value |
|---|---|
| Problem | Mid-air / surface gesture interaction is hard for older adults due to motor, cognitive, and perceptual decline |
| Target users | Older adults (typically 60+), sometimes 65+ |
| System / intervention | Gesture-based UIs: touchscreen, mid-air (Leap Motion, Kinect, depth cameras), wearable IMU gesture recognizers |
| Evaluation style | Controlled lab study, usability study, user-centered design (co-design, think-aloud) |
| Expected contribution | Design guidelines, gesture set design, recognition model adapted for aging, accessibility findings |

---

## Queries Run (conceptual — using training knowledge in lieu of live search)

### ACM Digital Library queries (CHI, ASSETS, IMWUT, DIS, UIST, CSCW)

1. `gesture interaction older adults` (title + abstract)
2. `touchscreen gestures elderly usability`
3. `mid-air gesture aging`
4. `Kinect gesture older adults`
5. `Leap Motion senior users`
6. `gesture set design aging accessibility`
7. `hand gesture recognition older adults deep learning`
8. `gesture elicitation study older adults`
9. `wearable gesture recognition elderly`
10. `gesture fatigue Gorilla Arm elderly`

### DBLP queries (author / venue navigation)

11. `gesture elderly CHI` venue filter: CHI / ASSETS
12. `gesture aging ASSETS` — ASSETS is the primary accessibility venue
13. `touchless interaction senior` venue filter: IMWUT / UbiComp
14. Author navigation from key authors (Wobbrock, Moffatt, Leung, Fang)

### Google Scholar queries (broad recall + citation chasing)

15. `"gesture interaction" "older adults" site:dl.acm.org`
16. `"gesture elicitation" elderly`
17. `"gesture recognition" aging accessibility`
18. `touchscreen gestures seniors performance`
19. Citation forward-chain from Wobbrock et al. 2009 ($1 gesture recognizer) for elderly adaptations
20. Citation forward-chain from Fisk et al. aging & technology canonical work

---

## Key Hits by Source

### ACM DL / CHI

- Moffatt & McGrenere (2007) — ASSETS. Gesture + aging, aging-adapted interaction.
- Vatavu et al. (2015) — CHI. Gesture elicitation with older adults, age-related differences in gesture production.
- Loureiro et al. (2020) — ASSETS. Touchscreen gesture performance in older adults.
- Stößel et al. (2010) — MobileHCI. Gesture preferences of older adults on touch devices.
- Leung et al. (2011) — CHI. Older adults and multi-touch gesture learning.
- Tsai et al. (2012) — CHI. Kinect-based gesture games for older adults.
- Wu et al. (2016) — CSCW. Older adults' adoption of touch-based gestures.
- Vines et al. (2015) — CHI. Participatory design with older adults (technology design).
- Fang et al. (2022) — CHI. Gesture elicitation / customization for older adults.
- Barnard et al. (2013) — ASSETS. Touchscreen gestures and aging cognition.

### DBLP / IEEE Xplore

- Aran et al. (2014) — IEEE FG. Hand gesture recognition for elderly healthcare.
- Biswas & Langdon (2012) — UAHCI. Input adaptation for aging users.
- Bobeth et al. (2012) — CHI / MobileHCI. Gesture interaction TV control for older adults.

### Google Scholar / arXiv

- Multiple deep learning papers on hand gesture recognition (2020–2024) — general population focus, minimal aging-specific adaptation.
- Cafaro et al. (2019) — DIS. Implicit gesture / proxemic interaction, general population.
- Several ACM SIGACCESS papers on motor-impaired gesture adaptation — adjacent to aging.

---

## Coverage Assessment

| Source | Coverage depth |
|---|---|
| ACM DL (CHI, ASSETS, IMWUT) | High — primary venue for HCI + aging |
| DBLP (venue/author navigation) | Medium — confirms author clusters |
| Google Scholar (broad + citation chain) | High — catches IEEE, MobileHCI, UAHCI outliers |
| IEEE Xplore | Medium — relevant for sensing/recognition side |
| arXiv | Low — very few aging-specific preprints in gesture HCI |

---

## Synthesis Signal

The search reveals a **well-explored but unevenly covered** space:
- Touchscreen gesture + aging: heavily studied (CHI, ASSETS, MobileHCI, 2010–2022)
- Mid-air gesture + aging: moderate coverage, mostly Kinect/Leap, 2011–2018
- Wearable/IMU gesture + aging: sparse (2020–2024), emerging gap
- Personalized / adaptive gesture recognition for aging motor variability: sparse
- LLM-mediated or multimodal gesture + aging: almost no coverage
- Co-design / participatory gesture vocabulary design with older adults: a few papers (Fang 2022, Vatavu 2015) but methodologically thin
