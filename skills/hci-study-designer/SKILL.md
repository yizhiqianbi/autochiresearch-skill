---
name: hci-study-designer
description: >
  Design the right HCI study for a research topic that has cleared the novelty gate — choosing
  between surveys, prototype evaluations, gameplay studies, and mixed methods, then producing
  consent forms, screeners, task flows, measures, stop criteria, and a complete study spec. Use
  this skill whenever the user needs to turn an HCI idea into a concrete study design, asks "what
  kind of study should I run?", or needs a survey draft, task script, or measurement plan. This
  skill covers both the design decision (what study type?) and the full specification (every
  instrument needed to actually run the study). If a novelty assessment hasn't been done yet,
  run chi-topic-scout first.
---

# HCI Study Designer

Use this skill after the novelty gate is passed and the project is ready to turn into a concrete
study.

## Workflow

1. Restate the research question and the evidence needed to support the claim.
2. Choose the study type based on what the claim requires:
   - attitudes, needs, or self-report only → survey or interview
   - system effectiveness or usability → prototype evaluation
   - process or behavior over time → prototype plus interaction logging
   - playful or experiential interaction → gameplay study plus post-play questionnaire
   - claims requiring both behavioral and attitudinal evidence → mixed methods
3. Specify participants: recruitment channel, inclusion criteria, expected N, and stop criteria.
4. Draft the full instrument set:
   - consent form and data handling note
   - screener
   - attention checks
   - main measures (validated scales where available; justify custom scales)
   - open-ended questions
   - demographics
   - debrief
5. If a prototype is involved, define:
   - tasks and completion markers
   - logged events
   - minimum viable prototype scope (not an aspirational full system)
6. Require a pilot plan before full launch.
7. End with `artifacts/study-spec.md` — a self-contained, analysis-ready specification.

## Rules

- Do not design a study before the novelty gate is complete. If the user hasn't run novelty
  assessment yet, ask them to do that first rather than proceeding.
- Every online study must include consent and data handling notes.
- Every production study must define exclusion rules before full collection begins.
- If the study depends on a custom prototype, specify the minimum viable prototype rather than
  an aspirational full system.
- Choose study type based on the claim, not on what's easiest to build.

## Outputs

Produce these artifacts:

- `artifacts/study-spec.md`
- `studies/survey.md`
- consent draft (in `studies/` or inline in study-spec)
- screener
- task script (when a prototype is involved)
- pilot checklist
- measurement plan with scale citations
