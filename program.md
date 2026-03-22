# AutoCHIResearch Program

This repository is a terminal-first Codex system for taking a raw HCI idea and pushing it through the full research pipeline.

## Human Input

The human should provide exactly one thing at the start:

- a raw idea

Everything after that is the agent's job unless blocked by ethics review, credentials, deployment access, or other external constraints.

## Phase Model

The workflow is intentionally grouped into three phases.

## Pre

Goal: understand the topic and decide whether it is worth doing.

Stages:

1. `brief`
   - fill `artifacts/research-brief.md`
   - clarify the problem, users, system concept, contribution, constraints, and success criteria
2. `novelty`
   - use `citation-management` and `chi-topic-scout`
   - search across ACM DL, DBLP, Google Scholar, and other relevant sources
   - write `artifacts/novelty-matrix.md`, `literature/search-log.md`, and `literature/references.bib`
   - if the decision is `pivot` or `drop`, stop rather than faking progress

## Mid

Goal: decide what should be built or studied, get it out, and prepare to turn activity into findings.

Stages:

1. `study`
   - use `hci-study-designer`
   - decide whether the idea needs a questionnaire, user study, prototype, gameplay study, or mixed method
   - write `artifacts/study-spec.md` and update `studies/`
2. `deployment`
   - use `study-deployment-ops` and `playwright`
   - prepare deployment, routing, monitoring, distribution, and export logic
   - if real credentials are missing, leave a deployable package plus an explicit blocker list
3. `analysis`
   - use `hci-analysis-writer`
   - define exclusion logic, derived variables, quantitative analysis, qualitative analysis, and planned outputs
   - write `analysis/analysis-plan.md`

The `Mid` phase is also where the agent decides whether a prototype is actually necessary. Not every CHI project needs one.

## Post

Goal: turn experimental outputs into a paper-level argument.

Stages:

1. `paper`
  - use `scientific-writing` and `citation-management`
  - write `paper/paper-brief.md`
  - synthesize the results into a manuscript narrative
  - update `paper/main.tex` and `paper/references.bib` when drafting is ready
  - `paper/main.tex` should be a stand-alone ACM `sigconf` manuscript draft, not a short shell
    with a paragraph per section
  - draft in full paragraphs; treat section length seriously rather than aiming for a minimal shell
  - once the manuscript is draftable, spawn an independent paper-judge sub-agent and require it to
    produce `paper/paper-review.md`
  - after the review is `READY`, compile the manuscript with `python3 scripts/autochi.py build-paper <project>`
  - the `paper` stage should only count as complete when that review returns a `READY` verdict
    and a PDF build succeeds

## Mandatory Rules

- Do not wait for the human between phases unless blocked.
- Do not skip the novelty gate.
- Do not design a study before there is a clear keep decision.
- Do not claim a deployment is complete without routing, storage, monitoring, and export plans.
- Do not change exclusion logic after data collection begins without documenting why.
- Treat the human as idea provider by default, not as the person who needs to hand-hold the workflow.

## Initialization

When a new idea arrives:

1. Run:
   - `python3 scripts/autochi.py init --idea "<raw idea>"`
2. Read:
   - the generated project `README.md`
   - the generated project `README.zh-CN.md`
   - the generated project `STATE.json`
   - the root `program.md`
3. Run:
   - `python3 scripts/autochi.py status <project-path>`

The generated project directory becomes the source of truth for that run. By default, new projects
live outside this repository in a sibling `autochiresearch-projects/` directory, or in whatever
path `AUTOCHI_PROJECTS_DIR` points to. Legacy in-repo `projects/` directories can still be resumed.

## Success Condition

A run is successful when the project has:

- a completed `Pre` phase
- a completed `Mid` phase
- a completed `Post` phase
- a project state of `CurrentStage: done`

At that point the project is ready for deeper implementation, live collection, or paper polishing.
If the manuscript still has a non-ready `paper/paper-review.md`, the project remains in the
`paper` stage rather than reaching `done`.
