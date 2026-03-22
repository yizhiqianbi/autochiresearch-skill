---
name: autochiresearch
description: >
  Orchestrate the full AutoCHIResearch local-first pipeline for any HCI or CHI-style research idea —
  from literature retrieval and novelty judgment through study design, data collection prep, analysis,
  and LaTeX paper drafting inside an AutoCHIResearch workspace. Use this skill whenever the user
  mentions an HCI research idea, a CHI study pipeline, AutoCHIResearch, or $autochiresearch —
  including mid-project continuation, single-phase work, or resuming a stalled project. Don't wait
  for the user to explicitly say "use AutoCHIResearch": if the request is about running, continuing,
  or setting up an HCI research workflow end-to-end, use this skill immediately.
---

# AutoCHIResearch

## Overview

This skill drives the complete HCI research pipeline from a raw idea to a locally authored, locally
analyzed, locally drafted paper. The default mode is local-first: write artifacts locally, preview
studies locally, let humans distribute surveys when needed, then import returned data back in for
analysis and writing. A server is never required unless the user explicitly asks for one.

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
- a nearby `autochiresearch` sibling directory
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
  - Stop here if the decision is pivot or drop — do not fake progress

### Mid

- `study`
  - Prefer `hci-study-designer` if it is available
  - Decide whether the topic needs a survey, interviews, a prototype, or a mixed path
- `deployment`
  - This stage means packaging and collection prep, **not server deployment by default**
  - Prefer `study-deployment-ops` for local preview, flow validation, export templates, and collection monitoring
  - If the user explicitly wants a server, `study-deployment-ops` can also handle that path
- `analysis`
  - Prefer `hci-analysis-writer` if it is available
  - Define inclusion rules, derived variables, figures, and manuscript-ready outputs **before** full collection begins
  - Write `analysis/analysis-plan.md` at this stage

### Post

- `paper`
  - Prefer `scientific-writing` and `citation-management` if they are available
  - Read `references/paper-judge.md` before the final completion pass
  - Update `paper/paper-brief.md`, `paper/main.tex`, `paper/paper-review.md`, and `paper/references.bib`
  - Treat `paper/main.tex` as the real artifact, not as a placeholder shell
  - The manuscript should be a stand-alone ACM `sigconf` draft with, at minimum:
    - Abstract
    - Introduction
    - Related Work
    - Method
    - Results
    - Discussion
    - Limitations
    - Ethics and Privacy
    - Conclusion
  - Once the manuscript is structurally complete, spawn a dedicated sub-agent to judge the paper.
    Give that sub-agent only the project-local manuscript context it needs and have it write a
    fresh `paper/paper-review.md` using the rubric in `references/paper-judge.md`.
  - Do not self-grade the paper and immediately mark the stage complete. The paper stage now
    requires an independent review artifact with a `READY` verdict before `sync` can advance.
  - Do not mark the paper stage complete with a short synopsis. A CHI-ready draft should be
    substantial enough to read as a real paper rather than an outline.
  - As a practical rule of thumb, target at least a few thousand words in `paper/main.tex`; many real
    CHI papers are much longer, often around the length of a 10--15 page ACM `sigconf` manuscript
    excluding references.

## Local-First Rules

- Do not require a server unless the user explicitly wants one.
- Prefer a local preview plus manual human distribution over self-hosted launch.
- When distribution happens through an external platform, preserve a canonical schema in the project
  and import returned CSV files back into the local database.
- Keep raw returned CSV files separate from cleaned analysis outputs.
- Treat the initialized project directory as the source of truth for the run.
- By default, new projects should live outside the skill repository in a separate projects directory.
- Legacy in-repo `projects/` directories are still valid when resuming older runs.
- Do not skip the novelty gate.
- Do not move into study design unless the topic is marked keep.
- Do not claim objective causal effects from retrospective self-report data.

## Output Convention

Read `references/output-convention.md` before creating or moving run artifacts. Default generated
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
- `artifacts/study-spec.md`
- `studies/survey.md`
- `studies/protocol.md`
- `deploy/deployment-plan.md`
- `analysis/analysis-plan.md`
- `paper/paper-brief.md`
- `paper/main.tex`
- `paper/paper-review.md`
- `literature/references.bib`
- `output/README.md`

For the paper stage specifically, `paper/main.tex` should be a stand-alone manuscript draft rather
than a section list with short placeholder paragraphs. If the project only has a paper brief and a
very short LaTeX shell, the paper stage is still incomplete. The stage is also incomplete if there
is no independent `paper/paper-review.md` or if that review does not give a `READY` verdict.

When the project uses manual external distribution, also leave:

- a distribution guide under `studies/`
- a canonical CSV template or import script under `analysis/`
- an output directory with reproducible exports, figures, screenshots, and summaries

## When to Use This Skill vs Sub-Skills

If the user asks for only one subtask — just literature retrieval, just study design, or just data
analysis — prefer the narrower sub-skill (`chi-topic-scout`, `hci-study-designer`, `hci-analysis-writer`).
Use this skill when the request spans multiple phases or when the user wants the whole pipeline driven
autonomously.
