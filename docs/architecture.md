# Architecture

This repository now follows a clearer monorepo split inspired by repositories such as
`Auto-claude-code-research-in-sleep`, while staying compatible with the existing AutoCHIResearch CLI.

## Top-Level Boundaries

- `skills/`
  - runtime skills only
- `skills/shared-references/`
  - reusable guidance shared across skills
- `scripts/`
  - runnable orchestration entrypoints such as `autochi.py`
- `templates/`
  - scaffold files used to initialize new project runs
- `evals/`
  - evaluation workspaces, snapshots, and benchmark artifacts
- `docs/`
  - architecture notes and operational documentation
- `projects/`
  - legacy in-repo compatibility folder only

## Design Intent

The repository should behave like a skill platform monorepo rather than a single oversized script.

That means:

- skill packages should stay readable and self-contained
- evaluation artifacts should not live under runtime skill folders
- large scaffold text should live in templates instead of Python string literals
- shared workflow rules should be reusable across multiple skills

## Compatibility Rules

- `scripts/autochi.py` remains the project initialization and status entrypoint
- existing skill names remain unchanged
- legacy in-repo projects continue to resolve
- current skill references continue to work even as canonical shared references move into `skills/shared-references/`
