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
   - keep a real reading trail; by the paper stage the project should usually reflect a 40+ paper corpus
   - if the decision is `pivot` or `drop`, stop rather than faking progress

## Mid

Goal: decide what should be built or studied, build it, get it out, and prepare to turn activity into findings.

Stages:

1. `study`
   - use `hci-study-designer`
   - decide whether the idea needs a questionnaire, user study, prototype, gameplay study, or mixed method
   - when multiple prototype or instrument directions are plausible, write a compact prototype inventory and insert a human checkpoint before build
   - write `artifacts/study-spec.md` and update `studies/`
2. `build`
   - use `hci-study-designer` and `playwright`
   - **actually build** every artifact specified in study-spec: prototype apps, questionnaires, survey instruments, stimulus sets, task rubrics
   - deliver working code, not just plans — prototypes must run locally, questionnaires must be completable end-to-end
   - if the study-spec contains a prototype checkpoint, pause long enough for the human to confirm which prototype path should be built and record that decision in `artifacts/build-report.md`
   - write `artifacts/build-report.md` documenting what was built, how to run it, and a smoke-test checklist
   - not every project needs a prototype; the study-spec decides what is required, and this stage builds exactly that
3. **Data-mode gate** (after build completes)
   - the agent **must** ask the user to choose a data mode before proceeding:
     - `synthetic` — generate synthetic/simulated data to validate the full pipeline now
     - `real` — pause and wait for the user to provide real participant data using the built artifacts
   - set the mode with `python3 scripts/autochi.py set-data-mode <project> synthetic|real`
   - the workflow blocks at deployment until a mode is chosen
4. `deployment`
   - use `study-deployment-ops` and `playwright`
   - if `synthetic`: prepare synthetic data generation scripts alongside the deployment plan
   - if `real`: design the real deployment plan (routing, monitoring, distribution, export) and wait for the user to collect data
   - if real credentials are missing, leave a deployable package plus an explicit blocker list
5. `analysis`
   - use `hci-analysis-writer`
   - if `synthetic`: run the analysis pipeline on generated data, clearly labeling all outputs as synthetic
   - if `real`: define the analysis plan and wait for real data before executing
   - write `analysis/analysis-plan.md`

## Post

Goal: turn experimental outputs into a paper-level argument.

Stages:

1. `paper`
  - use `scientific-writing` and `citation-management`
  - write `paper/paper-brief.md`
  - synthesize the results into a manuscript narrative
  - update `paper/main.tex` and `paper/references.bib` when drafting is ready
  - decide whether the paper needs generated teaser and method / pipeline figures in `paper/figure-plan.md`
  - use Codex image generation / GPT Image 2 for paper image assets by default, save final PNGs under
    `output/exports/figures/`, set `Figure Decision` to `gpt-image-2` in `paper/figure-plan.md`,
    and do not default to PaperBanana
  - treat `paper/figure-plan.md` as a structured brief, not a one-line caption dump; fill the visual style,
    inclusion/exclusion constraints, and human approval fields before generation
  - keep the abstract compact; it should summarize the paper in one dense paragraph rather than rehearse the full setup
  - keep the introduction focused on problem, gap, and contribution; do not let it duplicate the detailed synthesis that belongs in Related Work
  - for workflow, interface, and multi-step system papers, the figure package should usually include a designed or generated teaser, a method / pipeline overview figure, and the core results figures
  - if GPT Image 2 generation is unavailable, still prepare a precise figure prompt/brief and use deterministic
    local plotting or diagram code as a fallback; record the fallback in `paper/figure-plan.md`
  - `paper/main.tex` should be a stand-alone ACM `sigconf` manuscript draft, not a short shell
    with a paragraph per section
  - include a real `teaserfigure` in the front matter and pair every figure with both `\caption{...}`
    and `\Description{...}`
  - prefer a designed or generated teaser asset over a raw validation screenshot; screenshots belong in `output/playwright/` unless there is a clear paper-specific reason to use one as the teaser
  - by paper completion, `paper/references.bib` should usually contain at least 40 validated citations tied to an actual reading pass
  - draft in full paragraphs; treat section length seriously rather than aiming for a minimal shell
  - `paper/main.tex` must contain at least 10000 visible words and the compiled PDF must render to at
    least 10 pages under `output/exports/rendered-pages/`; if either threshold is missed, expand the
    manuscript and rerun `build-paper`
  - once the manuscript is draftable, run an adversarial reviewer subagent pass and require
    `paper/adversarial-review.md` before the final review; use four independent roles:
    methods/validity, systems/interaction contribution, related work/novelty, and
    writing/claim-evidence/CHI fit
  - when the user explicitly asks for subagents and the environment provides them, dispatch those
    reviewer roles as separate subagents; otherwise run the same four-role review serially and record
    the fallback in `paper/adversarial-review.md`
  - each adversarial reviewer should argue like a real skeptical CHI reviewer: rejection risks first,
    missing evidence and figures/tables next, then concrete revision actions; the author must revise
    the manuscript and mark each reviewer response as `addressed` or `waived`
  - after adversarial revisions, spawn a final paper-judge sub-agent and require it to produce
    `paper/paper-review.md`
  - after the review is `READY`, compile the manuscript with `python3 scripts/autochi.py build-paper <project>`
  - inspect `output/exports/rendered-pages/` after each successful build and keep fixing clipping,
    overlap, crowded tables, and weak figure composition before calling the paper complete
  - the `paper` stage should only count as complete when adversarial review is complete, author
    revisions are complete, the final review returns a `READY` verdict, and a PDF build succeeds

## Mandatory Rules

- Do not wait for the human between phases unless blocked.
- Do not skip the novelty gate.
- Do not design a study before there is a clear keep decision.
- Do not silently choose between multiple plausible prototype directions without a human checkpoint.
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
If the manuscript still has a missing or unresolved `paper/adversarial-review.md`, or a non-ready
`paper/paper-review.md`, the project remains in the `paper` stage rather than reaching `done`. The
same is true when `paper/figure-plan.md` requests a generated figure but no figure has been produced
yet.
