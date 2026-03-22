---
name: chi-project-runner
description: >
  Backward-compatible alias for the AutoCHIResearch local-first workflow. Use when the user
  invokes "chi-project-runner" by name, or when starting a full HCI project pipeline with older
  prompts. Follows the same local-first, idea-to-paper pipeline as $autochiresearch — literature
  retrieval, novelty judgment, study design, deployment prep, analysis, and LaTeX drafting inside
  an AutoCHIResearch workspace. If in doubt between chi-project-runner and autochiresearch, use
  autochiresearch — this skill exists only to keep older prompts working.
---

# CHI Project Runner

This skill is a compatibility entrypoint for the same workflow now defined by `$autochiresearch`.
It exists so that older prompts and bookmarks that reference `chi-project-runner` continue to work
without changes.

**Follow all rules and logic from `$autochiresearch` exactly.** The only difference is the name.

## Workspace Resolution

Reuse `../autochiresearch/scripts/resolve_autochi_repo.py`.
If no workspace is found, read `../autochiresearch/references/workspace-bootstrap.md`.

## Workflow

Identical to `$autochiresearch`:

1. Resolve the workspace root.
2. Initialize a new project when needed:
   - `python3 scripts/autochi.py init --idea "<raw idea>"`
3. Read the generated project `README.md`, `README.zh-CN.md`, `STATE.json`, and the root `program.md`.
4. Run `python3 scripts/autochi.py status <project-path>` to identify the current phase and stage.
5. Complete the current stage artifact and any support files it requires.
6. Run `python3 scripts/autochi.py sync <project-path>` after each stage update.
7. Continue until all phases are complete or the novelty gate forces a pivot or drop decision.

## Phase Routing

### Pre
- `brief` → fill `artifacts/research-brief.md`
- `novelty` → prefer `citation-management` + `chi-topic-scout` if available

### Mid
- `study` → prefer `hci-study-designer` if available
- `deployment` → local packaging and collection prep by default; prefer `study-deployment-ops` + `playwright`; server only if user explicitly requests it
- `analysis` → prefer `hci-analysis-writer` if available

### Post
- `paper` → prefer `scientific-writing` + `citation-management` if available

## Rules

- Treat the user as idea provider by default. Do not stop between phases unless blocked.
- Do not skip the novelty gate.
- Do not move to study design before the topic is marked keep.
- Default to local-first. Do not require a server unless the user explicitly wants one.
- Keep generated outputs under `output/`; see `../autochiresearch/references/output-convention.md`.
- Treat the generated project directory in `projects/` as the source of truth for the run.

## Minimum Outputs

Same as `$autochiresearch`:

- `artifacts/research-brief.md`
- `artifacts/novelty-matrix.md`
- `artifacts/study-spec.md`
- `deploy/deployment-plan.md`
- `analysis/analysis-plan.md`
- `paper/paper-brief.md`
- `literature/references.bib`
- `paper/main.tex`
- `output/README.md`
