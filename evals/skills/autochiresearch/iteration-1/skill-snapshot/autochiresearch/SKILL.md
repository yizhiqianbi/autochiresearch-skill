---
name: autochiresearch
description: Run the AutoCHIResearch terminal workflow for HCI and CHI-style projects from a raw idea to a local-first research package. Use when the user wants Codex to take one idea through literature retrieval, novelty judgment, survey or prototype design, local preview, manual external distribution prep, CSV re-import, local analysis, and LaTeX paper drafting inside an AutoCHIResearch workspace.
---

# AutoCHIResearch

## Overview

Use this skill when the user gives an HCI idea and expects Codex to run the rest of the research workflow inside an AutoCHIResearch workspace. Default to local-first execution: author locally, preview locally, let humans distribute surveys or prototypes if needed, then import returned data back into the project for analysis and writing.

This skill must not assume one machine-specific absolute path. Resolve the workspace first, then operate inside it.

## Workspace Resolution

1. Run `scripts/resolve_autochi_repo.py`.
2. If it returns a path, use that as the AutoCHIResearch root.
3. If it fails, read `references/workspace-bootstrap.md` and either:
   - initialize or clone an AutoCHIResearch workspace in the current environment, or
   - tell the user exactly what is missing.

Resolution order is:

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
4. Inspect project state:
   - `python3 scripts/autochi.py status <project-path-or-slug>`
5. Complete the current stage artifact and its support files.
6. Run:
   - `python3 scripts/autochi.py sync <project-path-or-slug>`
7. Continue until `CurrentStage: done`, unless the novelty gate says pivot or drop.

## Phase Routing

### Pre

- `brief`
  - Fill `artifacts/research-brief.md`
- `novelty`
  - Prefer `citation-management` and `chi-topic-scout` if they are available
  - Update `artifacts/novelty-matrix.md`, `literature/search-log.md`, and `literature/references.bib`

### Mid

- `study`
  - Prefer `hci-study-designer` if it is available
  - Decide whether the topic needs a survey, interviews, a prototype, or a mixed path
- `deployment`
  - Treat this as packaging and collection prep, not server deployment by default
  - Prefer `study-deployment-ops` and `playwright` for local preview, flow validation, export, and monitor logic
- `analysis`
  - Prefer `hci-analysis-writer` if it is available
  - Define inclusion rules, derived variables, figures, and manuscript-ready outputs before full analysis

### Post

- `paper`
  - Prefer `scientific-writing` and `citation-management` if they are available
  - Update `paper/paper-brief.md`, `paper/main.tex`, and `paper/references.bib`

## Local-First Rules

- Do not require a server unless the user explicitly wants one.
- Prefer a local preview plus manual human distribution over self-hosted launch.
- When distribution happens through an external platform, preserve a canonical schema in the project and import returned CSV files back into the local database.
- Keep raw returned CSV files separate from cleaned analysis outputs.
- Treat the project directory under `projects/` as the source of truth for the run.
- Do not skip the novelty gate.
- Do not move into study design unless the topic is marked keep.
- Do not claim objective causal effects from retrospective self-report data.

## Output Convention

Read `references/output-convention.md` before creating or moving run artifacts. Default generated outputs belong under:

- `output/analysis`
- `output/collection`
- `output/exports`
- `output/playwright`

Do not scatter generated screenshots and figures across unrelated source directories unless the repo already uses a different explicit convention.

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
- Prepare manual distribution template when the project supports it:
  - `python3 analysis/import_flat_csv.py --write-template output/collection/manual_template.csv`
- Import returned flat CSV data:
  - `python3 analysis/import_flat_csv.py --csv path/to/returned.csv --db prototype/data/<db-name>.db`

## Project Outputs

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
- `literature/references.bib`
- `output/README.md`

When the project uses a manual external distribution path, also leave:

- a distribution guide under `studies/`
- a canonical CSV template or import script under `analysis/`
- an output directory with reproducible exports, figures, screenshots, and summaries

## Trigger Examples

Use this skill for requests like:

- "我给你一个 idea，剩下你自己做"
- "基于这个题做一套 CHI 研究流程"
- "本地把问卷、原型、分析、成文全做完"
- "不要上服务器，人工发问卷，数据回来再分析"
- "继续这个 AutoCHIResearch 项目直到可以收数和写作"

If the user is only asking for one subtask such as literature retrieval or data analysis, prefer the narrower skill instead of this one.
