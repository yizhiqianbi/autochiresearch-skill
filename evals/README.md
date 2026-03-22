# Evals

Evaluation artifacts live outside `skills/` so runtime skill bundles stay focused.

## Layout

- `evals/skills/<skill-name>/evals.json`
  - prompt list or eval inputs for that skill
- `evals/skills/<skill-name>/trigger-eval.json`
  - trigger behavior checks
- `evals/skills/<skill-name>/iteration-*`
  - snapshots, benchmark runs, and grading outputs

These paths are rooted under `evals/`, for example:

- `evals/skills/autochiresearch/evals.json`
- `evals/skills/autochiresearch/iteration-1/benchmark.md`

This mirrors the separation used by larger skill-platform repositories: runtime skills in one tree,
evaluation workspaces in another.
