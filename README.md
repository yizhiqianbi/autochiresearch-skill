# AutoCHIResearch Skill

This repository is now the single canonical entrypoint. Use `/Users/pencil/Documents/PrepareMLLM/autochiresearch-skill` as both:

1. a Codex skill bundle under `skills/`
2. a runnable AutoCHIResearch workspace

You no longer need the sibling `autochiresearch` repository as the primary runtime dependency.

## Included Components

- `skills/autochiresearch/`
  - the main orchestration skill
- `skills/shared-references/`
  - reusable workflow guidance shared across skills
- `skills/chi-project-runner/`
  - backward-compatible alias
- `skills/chi-topic-scout/`
  - related-work and novelty helper
- `skills/hci-study-designer/`
  - study-design helper
- `skills/hci-analysis-writer/`
  - analysis helper
- `skills/study-deployment-ops/`
  - local preview and collection-prep helper
- `skills/paper-compile/`
  - LaTeX PDF build helper
- `scripts/autochi.py`
  - project init, state tracking, and sync
- `templates/`
  - project scaffold templates consumed by `autochi.py`
- `evals/`
  - evaluation workspaces and benchmark artifacts
- `docs/`
  - architecture and layout notes
- `program.md` and `program.zh-CN.md`
  - workflow-level guidance
- `projects/`
  - legacy/example projects kept in-repo for compatibility; new runs should not default here

## Recommended Companion Skills

These are installed in your Codex environment and work well as optional companions to this repo:

- `frontend-skill`
  - stronger support for richer web prototypes
- `spreadsheet`
  - CSV cleaning, table inspection, and structured data QA
- `transcribe`
  - interview or study-audio transcription
- `doc`
  - working with Word-style study documents and exported forms

## Quick Start

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill
python3 scripts/autochi.py init --idea "your HCI idea"
python3 scripts/autochi.py status <project-slug-or-path>
```

By default, `init` now creates projects in a sibling directory outside this repository:
`../autochiresearch-projects/`. Set `AUTOCHI_PROJECTS_DIR` if you want a different global location.
If you already have legacy in-repo projects, run `python3 scripts/autochi.py migrate-legacy-projects`
to move them into the external projects directory.
When a manuscript is review-ready, run `python3 scripts/autochi.py build-paper <project>` to try to
compile `paper/main.tex` into `output/exports/paper.pdf`.

If you want Codex to drive the full workflow:

```text
Use $autochiresearch to turn this idea into a local-first HCI study project.
```

## Principles

- local-first by default
- the human provides one idea and the agent continues the workflow
- studies can be designed, previewed, analyzed, and drafted locally
- manual external survey distribution is allowed; returned CSV files can be re-imported
- generated artifacts should live under each project's `output/`
- new projects should live outside the skill repository by default to avoid polluting the skill bundle
- the paper stage requires an independent sub-agent review artifact at `paper/paper-review.md`
- runtime skills, templates, docs, and evals should stay in separate top-level directories

## Dependency Boundary

This repository now contains the core AutoCHIResearch workspace files and the project-local support skills needed by `$autochiresearch`. General-purpose skills such as `citation-management`, `scientific-writing`, and `playwright` are still useful when available, but they are treated as optional accelerators rather than as a separate local-repository dependency.
