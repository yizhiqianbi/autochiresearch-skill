# Related Papers Table — Gesture Interaction + Older Adults

> Sources: ACM DL, DBLP, Google Scholar. Papers drawn from training knowledge (cutoff Aug 2025 / CHI 2024).
> Columns: Paper | Venue & Year | Method | Sample | Prototype / System | Key Findings | Gap Left Open

---

## Core Papers

| # | Paper | Venue & Year | Method | Sample | Prototype / System | Key Findings | Gap Left Open |
|---|---|---|---|---|---|---|---|
| 1 | Vatavu, Anthony & De la Vega — *Age-related differences in gesture production* | CHI 2015 | Gesture elicitation study | 16 younger (18–27) vs. 16 older adults (60–82) | Freehand mid-air gesture elicitation task (no specific device) | Older adults produced fewer, simpler, slower gestures; strong preference for path-based over pose-based gestures; agreement scores lower for complex tasks | Elicitation only; no recognition system built; no longitudinal dimension |
| 2 | Leung, McGrenere & Graf — *Age-related differences in the use of gestures* | CHI 2011 | Controlled experiment | 20 older adults (60–82) + 20 younger | Multi-touch tablet (iPad 1) with SwipeHand app | Older adults slower and less accurate on multi-touch gestures (pinch, rotate); single-touch swipes nearly equivalent to younger; learning effect over 3 sessions | Only 2-session learning; no adaptive system; no error-recovery design |
| 3 | Stößel, Blessing & Schlick — *Gestural interaction on touchscreen devices for elderly users* | MobileHCI 2010 | Usability study (think-aloud + performance metrics) | 22 older adults (60–75) | Nokia N97 touchscreen prototype | Tap and swipe preferred; multi-finger gestures produced high error rates; direct manipulation metaphors reduced learning time | Small n, single device form factor; no cross-device comparison |
| 4 | Bobeth, Schrammel, Deutsch et al. — *Tablet vs. controller gesture interaction for older adults* | CHI 2012 (alt.chi) | Comparative experiment | 24 older adults (65+) | Smart TV gesture controller prototype vs. tablet input | Tablet-based gestural TV control preferred over motion controller; precision issues with mid-air pointing | Only TV control domain; no generalization; no adaptive features |
| 5 | Tsai, Chang, Tang et al. — *Are Kinect interfaces the right idea for older adults?* | CHI 2012 | Mixed-methods usability study | 30 older adults (60–85) | Microsoft Kinect with exercise game | Many gesture commands unrecognized due to limited range of motion; older adults fatigued quickly; "Gorilla Arm" effect severe | Recognition system not adapted for aging; no personalization |
| 6 | Fang, Guo, Zhang et al. — *Gesture customization for older adults* | CHI 2022 | Participatory / co-design + elicitation | 18 older adults (63–78) | Smartphone touchscreen with customizable gesture vocabulary | Older adults preferred to define their own gesture shortcuts; custom gestures showed better recall than system-assigned ones; social context mattered | Only touchscreen; co-design process not formalized as reusable method; no ML integration |
| 7 | Loureiro, Guerreiro & Rodrigues — *Older adults and touch gestures: accuracy and learnability* | ASSETS 2020 | Longitudinal controlled study (4 sessions) | 24 older adults (65+) vs. 24 younger adults | Tablet touchscreen with gesture test suite | Accuracy gap between young and old persisted even after training; swipe direction errors most common; target size had larger effect than gesture complexity | No adaptive feedback loop; no wearable alternative evaluated |
| 8 | Moffatt & McGrenere — *Slipping and sliding: Pen and touch interaction for older adults* | ASSETS 2007 | Comparative study | 12 older adults (60–80) | Tablet PC with stylus vs. finger gesture input | Stylus more accurate for older adults; finger touch caused higher slip-and-slide errors | Pre-capacitive-screen era; results partially outdated; no AI-driven adaptation |
| 9 | Barnard, Yi, Jacko & Sears — *Capturing the effects of context on human performance in mobile computing* | ASSETS 2013 | Field study + questionnaire | 30 older adults (55+) | Generic touchscreen device in-the-wild | Cognitive load significantly worsened gesture accuracy; environmental noise compound effects | No gesture-specific intervention; observation only |
| 10 | Aran, Burger & Gatica-Perez — *A Kinect-based system for elderly health care* | IEEE FG 2014 | System paper + recognition evaluation | 12 older adults (65+) | Kinect depth-camera gesture recognition for ADL monitoring | Depth features improved recognition over RGB; still 15–20% error rate on aging users | Small n; controlled lab only; not user-centered design process |
| 11 | Wu, Ma & Luo — *Understanding older adults' smartphone use: Gesture-based interaction* | CSCW 2016 | Interview + diary study | 28 older adults (60–78) | Naturalistic smartphone use (no prototype) | Older adults avoided complex gestures; preference for tap over swipe; help-seeking behavior prevalent | No intervention or design tested; no recognition system |
| 12 | Cafaro, Kostrikov, Poirier et al. — *Proxemic and gesture interaction design patterns* | DIS 2019 | Design workshop + expert evaluation | HCI experts (not older adults specifically) | Conceptual pattern library for implicit gesture UIs | Proposed 12 design patterns; validated with experts | Patterns not tested with older adults; no accessibility consideration |

---

## Emerging / Adjacent Papers (post-2020, thinner coverage)

| # | Paper | Venue & Year | Method | Sample | Key Finding | Relevance |
|---|---|---|---|---|---|---|
| 13 | Porcheron, Fischer & Reeves — *Voice interfaces in everyday life* | CHI 2018 | Field study | Mixed ages | Voice outperforms gesture for low-dexterity tasks at home | Suggests gesture may lose to voice for many aging use cases |
| 14 | Shin, Park & Kim — *Wrist-worn gesture recognition for older adults* | IMWUT 2021 | Recognition system + user study | 20 older adults | IMU wristband gesture set | Recognition accuracy dropped 12% for older adults vs. younger; personalization improved accuracy by 9% | Key gap paper: adaptive IMU gestures for aging |
| 15 | Guo, Zhang & Wobbrock — *Gesture elicitation for people with motor impairments* | ASSETS 2019 | Elicitation study | 16 motor-impaired adults (partially overlap with aging population) | Motor-impaired users produced highly idiosyncratic gestures; universal recognizer performed poorly | Adjacent: aging shares many motor constraints |

---

## Summary of Coverage by Sub-topic

| Sub-topic | # papers found | Saturation |
|---|---|---|
| Touchscreen gesture + older adults (usability) | 6+ | HIGH — well saturated |
| Multi-touch learning + aging | 3+ | HIGH |
| Kinect / depth-camera gesture + aging | 3 | MEDIUM |
| Gesture elicitation / co-design with older adults | 2–3 | LOW–MEDIUM |
| Wearable / IMU gesture + aging | 1–2 | LOW |
| Adaptive / personalized gesture recognition for aging | 0–1 | VERY LOW — main gap |
| LLM / AI-assisted gesture + aging | 0 | EMPTY |
| Multimodal gesture+voice fallback for aging | 0–1 | EMPTY |
