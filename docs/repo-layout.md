# Repository Layout

## Runtime

- `scripts/autochi.py`
  - project init, sync, and state-machine logic
- `skills/autochiresearch/`
  - primary orchestration skill
- `skills/chi-project-runner/`
  - compatibility alias
- `skills/chi-topic-scout/`
  - novelty and literature helper
- `skills/hci-study-designer/`
  - study design helper
- `skills/hci-analysis-writer/`
  - analysis helper
- `skills/study-deployment-ops/`
  - deployment and collection helper

## Shared Guidance

- `skills/shared-references/output-convention.md`
- `skills/shared-references/paper-judge.md`

## Scaffolds

- `templates/project/`
  - initialization templates loaded by `scripts/autochi.py`

## Evaluation

- `evals/skills/<skill-name>/`
  - skill-local eval prompts, snapshots, and benchmark runs

## Human Docs

- `README.md`
- `README.zh-CN.md`
- `program.md`
- `program.zh-CN.md`
- `docs/`
