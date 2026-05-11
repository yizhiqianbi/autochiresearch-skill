---
name: autochiresearch
description: >
  Drive the full AutoCHIResearch local-first HCI/CHI pipeline inside an AutoCHIResearch workspace:
  start from a raw idea or continue an existing project or current stage through brief, novelty,
  study, build, deployment, analysis, and paper drafting. Trigger when the user asks to start,
  continue, resume, or fully drive an HCI/CHI research workflow, says AutoCHIResearch or
  $autochiresearch, references STATE.json/current stage/workspace, or asks to take an HCI idea
  从 idea 到投稿.
---

# AutoCHIResearch

## Overview

This skill drives the complete HCI research pipeline from a raw idea to a locally authored, locally
analyzed, locally drafted paper. The default mode is local-first: write artifacts locally, preview
studies locally, let humans distribute surveys when needed, then import returned data back in for
analysis and writing. A server is never required unless the user explicitly asks for one.

Do not wait for the user to explicitly say "use AutoCHIResearch" — if the request involves running,
continuing, or setting up an HCI research workflow end-to-end, use this skill immediately.

This skill must not assume one machine-specific absolute path. Resolve the workspace first, then
operate inside it.

## Workspace Resolution

1. Run `scripts/resolve_autochi_repo.py`.
2. If it returns a path, use that as the AutoCHIResearch root.
3. If it fails, read `references/workspace-bootstrap.md` and either:
   - initialize or clone an AutoCHIResearch workspace in the current environment, or
   - tell the user exactly what is missing and stop until it is resolved.

Resolution order:

- `AUTOCHI_REPO` environment variable
- current working directory or one of its parents if they contain `scripts/autochi.py` and `program.md`
- a nearby `autochiresearch` or `autochiresearch-skill` sibling directory
- legacy default path only as a last fallback

## Workflow

1. Resolve the workspace root.
2. Read:
   - `program.md` or `program.zh-CN.md`
   - root `README.md` or `README.zh-CN.md`
   - the target project's `README.md`, `README.zh-CN.md`, and `STATE.json` when a project already exists
3. If the user gives only a raw idea, initialize a project:
   - `python3 scripts/autochi.py init --idea "<raw idea>"`
   - New projects should default outside the skill repository. Use the CLI default or set `AUTOCHI_PROJECTS_DIR`.
4. Inspect project state:
   - `python3 scripts/autochi.py status <project-path-or-slug>`
5. Complete the current stage artifact and its support files.
6. Run:
   - `python3 scripts/autochi.py sync <project-path-or-slug>`
7. Continue through all phases until `CurrentStage: done`, unless the novelty gate says pivot or drop.
8. If `CurrentStage: done` when you arrive, do not invent a fake new stage. Treat the continuation task as audit, polishing, packaging, deployment follow-through, data-collection follow-through, or manuscript-readiness review, depending on the user's request.

Treat the user as idea provider by default. Do not stop between phases to ask permission unless
genuinely blocked by ethics review, missing credentials, or an explicit novelty gate decision.

## Phase Routing

### Pre

- `brief`
  - Fill `artifacts/research-brief.md`
- `novelty`
  - Prefer `citation-management` and `chi-topic-scout` if they are available
  - Update `artifacts/novelty-matrix.md`, `literature/search-log.md`, and `literature/references.bib`
  - Maintain a real reading log; the paper stage should usually reflect a 40+ paper corpus
  - Stop here if the decision is pivot or drop — do not fake progress

### Mid

- `study`
  - Prefer `hci-study-designer` if it is available
  - Decide whether the topic needs a survey, interviews, a prototype, or a mixed path
  - If multiple prototype or instrument directions are plausible, create a prototype inventory and insert a human checkpoint before build
- `build`
  - **Actually build** the prototype, questionnaire, or instrument specified in study-spec
  - Deliver working artifacts: runnable prototype apps, completable questionnaires, task rubrics, stimulus sets
  - Record which prototype path the human approved, or explicitly note when a checkpoint was waived
  - Write `artifacts/build-report.md` documenting what was built, how to run it, and smoke-test results
- **Data-mode gate** (after `build` completes)
  - Ask the user to choose: `synthetic` (generate fake data now) or `real` (wait for real participant data)
  - Set via `python3 scripts/autochi.py set-data-mode <project> synthetic|real`
  - The workflow blocks at `deployment` until a mode is chosen
- `deployment`
  - This stage means packaging and collection prep, **not server deployment by default**
  - Prefer `study-deployment-ops` for local preview, flow validation, export templates, and collection monitoring
  - In `synthetic` mode: also prepare data generation scripts
  - In `real` mode: design the deployment plan and wait for the user to collect data
  - If the user explicitly wants a server, `study-deployment-ops` can also handle that path
- `analysis`
  - Prefer `hci-analysis-writer` if it is available
  - In `synthetic` mode: run the analysis pipeline on generated data, label all outputs as synthetic
  - In `real` mode: define the analysis plan, wait for real data before executing
  - Write `analysis/analysis-plan.md` at this stage

### Post

- `paper`
  - Prefer `scientific-writing`, `citation-management`, and `paper-compile` if they are available
  - Read `../shared-references/paper-judge.md` before the final completion pass
  - Update `paper/paper-brief.md`, `paper/figure-plan.md`, `paper/main.tex`, `paper/adversarial-review.md`, `paper/paper-review.md`, and `paper/references.bib`
  - Treat `paper/figure-plan.md` as a structured visual brief with style, must-include, must-avoid, and human approval fields
  - Use Codex image generation / GPT Image 2 for paper image assets by default, save final PNGs under
    `output/exports/figures/`, set `Figure Decision` to `gpt-image-2` in `paper/figure-plan.md`,
    and do not default to PaperBanana
  - Do not mark the paper stage complete with a thin bibliography; target at least 40 validated citations in `paper/references.bib`
  - Do not mark the paper stage complete if `paper/main.tex` has fewer than 10000 visible words or if
    the compiled PDF renders to fewer than 10 pages under `output/exports/rendered-pages/`; expand the
    manuscript and rebuild until it reaches both thresholds
  - Run the built-in adversarial reviewer subagent gate before final paper review. Write the
    critiques, author repairs, and residual risks to `paper/adversarial-review.md`
  - Adversarial reviewer roles:
    - Reviewer A: methods, construct validity, measures, statistics, and claim support
    - Reviewer B: systems contribution, interaction design, prototype concreteness, and differentiation
    - Reviewer C: related work, novelty, citation fit, and contribution positioning
    - Reviewer D: writing clarity, claim-evidence alignment, CHI fit, and overall reviewer readability
  - Only after those reviewer responses are marked addressed or waived should the final paper-judge
    sub-agent produce `paper/paper-review.md`
  - Follow all paper-stage rules in `program.md` — manuscript quality, section requirements, figure
    generation, independent review, PDF build, and visual QA are defined there as the single source
    of truth
  - Key gate: the paper stage requires a complete `paper/adversarial-review.md`, an independent
    `paper/paper-review.md` with a `READY` verdict, **and** a successful PDF build before `sync`
    can advance

## Local-First and Mandatory Rules

Read `program.md` for the full set.  Critical rules repeated here for routing clarity:

- Do not require a server unless the user explicitly wants one.
- Do not skip the novelty gate.
- Do not move into study design unless the topic is marked keep.
- Do not silently choose between multiple plausible prototype directions without a human checkpoint.
- Treat the initialized project directory as the source of truth for the run.
- New projects should live outside the skill repository by default.

## Output Convention

Read `../shared-references/output-convention.md` before creating or moving run artifacts. Default generated
outputs belong under:

- `output/analysis`
- `output/collection`
- `output/exports`
- `output/playwright`

Do not scatter generated screenshots and figures across unrelated source directories unless the repo
already uses a different explicit convention.

## Command Spine

- Initialize a project:
  - `python3 scripts/autochi.py init --idea "<raw idea>"`
- Inspect progress:
  - `python3 scripts/autochi.py status <slug>`
- Recompute phase state:
  - `python3 scripts/autochi.py sync <slug>`
- Set data mode (after build stage):
  - `python3 scripts/autochi.py set-data-mode <slug> synthetic`
  - `python3 scripts/autochi.py set-data-mode <slug> real`
- Compile the paper:
  - `python3 scripts/autochi.py build-paper <slug>`
- Run adversarial paper review:
  - Spawn the four reviewer subagents described in the paper-stage rules when the user requests
    subagents/adversarial review and subagent tooling is available.
  - Merge their critiques and the author response matrix into `paper/adversarial-review.md`.
  - If subagent tooling is unavailable, run the same four-role review serially and record the fallback in that file.
- Generate paper image assets:
  - Use Codex image generation / GPT Image 2 by default for teaser and method/pipeline images.
  - Save final project-bound assets under `output/exports/figures/`.
  - If GPT Image 2 generation is unavailable, prepare the exact image prompt in `paper/figure-plan.md` and use a deterministic local plotting/diagram fallback rather than PaperBanana.
- Run a local study app:
  - `python3 prototype/app.py init-db`
  - `python3 prototype/app.py run --host 127.0.0.1 --port <port>`
- Seed demo data:
  - `python3 prototype/app.py seed-demo`
- Analyze local data:
  - `python3 analysis/analyze.py --db prototype/data/<db-name>.db --out output/analysis`
- Prepare manual distribution template:
  - `python3 analysis/import_flat_csv.py --write-template output/collection/manual_template.csv`
- Import returned flat CSV data:
  - `python3 analysis/import_flat_csv.py --csv path/to/returned.csv --db prototype/data/<db-name>.db`

## Minimum Project Outputs

Leave each project with, at minimum:

- `artifacts/research-brief.md`
- `artifacts/novelty-matrix.md`
- `literature/search-log.md`
- `artifacts/study-spec.md`
- `artifacts/build-report.md`
- `studies/survey.md`
- `studies/protocol.md`
- `deploy/deployment-plan.md`
- `analysis/analysis-plan.md`
- `paper/paper-brief.md`
- `paper/figure-plan.md`
- `paper/main.tex`
- `paper/adversarial-review.md`
- `paper/paper-review.md`
- `literature/references.bib`
- `output/README.md`

Paper-stage completeness is enforced by `autochi.py sync` — see `program.md` for the full
checklist (manuscript word count, minimum 10 rendered pages, required sections, teaser, adversarial
reviewer gate, final review verdict, PDF build, etc.).

When the project uses manual external distribution, also leave:

- a distribution guide under `studies/`
- a canonical CSV template or import script under `analysis/`
- an output directory with reproducible exports, figures, screenshots, and summaries

## When to Use This Skill vs Sub-Skills

If the user asks for only one subtask — just literature retrieval, just study design, or just data
analysis — prefer the narrower sub-skill (`chi-topic-scout`, `hci-study-designer`, `hci-analysis-writer`).
Use this skill when the request spans multiple phases or when the user wants the whole pipeline driven
autonomously.
