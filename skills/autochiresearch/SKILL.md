---
name: autochiresearch
description: Run the AutoCHIResearch terminal workflow for HCI and CHI-style projects from a raw idea to a local-first research package. Use when the user wants Codex to take one idea through literature retrieval, novelty judgment, survey or prototype design, local preview, manual external distribution prep, CSV re-import, local analysis, and LaTeX paper drafting inside the AutoCHIResearch repository.
---

# AutoCHIResearch

## Overview

Use this skill when the user gives an HCI idea and expects Codex to run the rest of the research workflow inside the AutoCHIResearch repository. Default to local-first execution: author locally, preview locally, let humans distribute surveys or prototypes if needed, then import returned data back into the project for analysis and writing.

## Workflow

1. Locate the repository root. Default path is `/Users/pencil/Documents/PrepareMLLM/autochiresearch`.
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
  - Use `citation-management` and `chi-topic-scout`
  - Update `artifacts/novelty-matrix.md`, `literature/search-log.md`, and `literature/references.bib`

### Mid

- `study`
  - Use `hci-study-designer`
  - Decide whether the topic needs a survey, interviews, a prototype, or a mixed path
- `deployment`
  - Treat this as packaging and collection prep, not server deployment by default
  - Use `study-deployment-ops` and `playwright` for local preview, flow validation, export, and monitor logic
- `analysis`
  - Use `hci-analysis-writer`
  - Define inclusion rules, derived variables, figures, and manuscript-ready outputs before full analysis

### Post

- `paper`
  - Use `scientific-writing` and `citation-management`
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
  - `python3 analysis/analyze.py --db prototype/data/<db-name>.db --out analysis/output`
- Prepare manual distribution template when the project supports it:
  - `python3 analysis/import_flat_csv.py --write-template analysis/output/manual_template.csv`
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

When the project uses a manual external distribution path, also leave:

- a distribution guide under `studies/`
- a canonical CSV template or import script under `analysis/`
- an analysis output directory with reproducible exports, figures, and summaries

## Trigger Examples

Use this skill for requests like:

- "我给你一个 idea，剩下你自己做"
- "基于这个题做一套 CHI 研究流程"
- "本地把问卷、原型、分析、成文全做完"
- "不要上服务器，人工发问卷，数据回来再分析"
- "继续这个 AutoCHIResearch 项目直到可以收数和写作"

If the user is only asking for one subtask such as literature retrieval or data analysis, prefer the narrower skill instead of this one.
