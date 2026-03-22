# 无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Original Idea
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Core Principle

The human provides one raw idea. Codex is expected to take over the remaining research workflow unless blocked by ethics, credentials, or deployment access.

## Workflow Model

### Pre

- research brief
- literature retrieval
- novelty gate

### Mid

- if needed, user study and questionnaire design
- if needed, prototype design and implementation
- questionnaire / prototype deployment and distribution
- experiment execution and data collection
- analysis planning and findings preparation

### Post

- writing
- result synthesis and conclusion building

## How Codex Should Use This Project

1. Read the root `program.md`.
2. Run `python3 scripts/autochi.py status canvas-vs-terminal-multi-agent` from the repo root.
3. Work on the current stage artifact and any support files it requires.
4. Run `python3 scripts/autochi.py sync canvas-vs-terminal-multi-agent` after each completed stage.
5. Continue until the project reaches `CurrentStage: done`.

## Key Paths

- `STATE.json`: project workflow state
- `artifacts/`: main markdown outputs
- `literature/`: search log and references
- `studies/`: study materials
- `prototype/`: prototype notes or code
- `deploy/`: deployment notes
- `analysis/`: analysis plan and scripts
- `paper/`: LaTeX manuscript files
- `output/`: run outputs, exported tables, screenshots, figures, and intermediate analysis artifacts
