---
name: chi-project-runner
description: Backward-compatible alias for the AutoCHIResearch local-first workflow. Use when the user asks for a full CHI or HCI project to be driven from one raw idea through literature retrieval, novelty judgment, survey or prototype design, local preview, manual external distribution prep, CSV re-import, local analysis, and LaTeX drafting inside an AutoCHIResearch workspace.
---

# CHI Project Runner

Use this skill as a compatibility entrypoint for the same workflow now defined by `$autochiresearch`. Keep old prompts working, but follow the newer AutoCHIResearch local-first and portable-workspace rules.

## Workspace Resolution

1. Reuse `../autochiresearch/scripts/resolve_autochi_repo.py`.
2. If no workspace is found, read `../autochiresearch/references/workspace-bootstrap.md`.

## Workflow

1. Resolve the workspace root.
2. Initialize a new project when needed:
   - `python3 scripts/autochi.py init --idea "<raw idea>"`
3. Read the generated project `README.md`, `README.zh-CN.md`, `STATE.json`, and the root `program.md`.
4. Run `python3 scripts/autochi.py status <project-path>` to identify the current phase and stage.
5. Complete the current stage artifact and any support files it requires.
6. Run `python3 scripts/autochi.py sync <project-path>` after each stage update.
7. Continue until the tracked phases are complete or the novelty gate forces a pivot or drop decision.

## Phase Routing

### Pre

- `brief` -> fill `artifacts/research-brief.md`
- `novelty` -> prefer `citation-management` + `chi-topic-scout` if available

### Mid

- `study` -> prefer `hci-study-designer` if available
- `deployment` -> treat this as local packaging, flow validation, manual distribution prep, or optional self-hosting; prefer `study-deployment-ops` + `playwright`
- `analysis` -> prefer `hci-analysis-writer` if available

### Post

- `paper` -> prefer `scientific-writing` + `citation-management` if available

## Rules

- Treat the user as idea provider by default.
- Do not skip the novelty matrix.
- Do not move to study design before the topic is marked keep.
- Decide within `Mid` whether the project actually needs a questionnaire, a user study, a prototype, or a mixed path.
- Default to local-first operation. Do not require a server unless the user explicitly wants one.
- When humans distribute through an external platform, preserve a canonical schema and import returned CSV files back into the local project.
- Keep generated outputs under `output/`; see `../autochiresearch/references/output-convention.md`.
- Treat the generated project directory in `projects/` as the source of truth for the run.

## Outputs

At minimum, leave each project with:

- `artifacts/research-brief.md`
- `artifacts/novelty-matrix.md`
- `artifacts/study-spec.md`
- `deploy/deployment-plan.md`
- `analysis/analysis-plan.md`
- `paper/paper-brief.md`
- `literature/references.bib`
- `paper/main.tex`
- `output/README.md`

When the project uses manual external distribution, also leave:

- a distribution guide under `studies/`
- a canonical CSV template or import script under `analysis/`
- reproducible local analysis outputs under `output/`
