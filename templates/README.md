# Templates

This directory stores reusable scaffold files used by the AutoCHIResearch runtime.

## Current Layout

- `project/`
  - project initialization templates consumed by `scripts/autochi.py`

The goal is to keep large scaffold text out of Python source so repo structure stays closer to a
skill platform monorepo:

- docs in `docs/`
- runtime scripts in `scripts/`
- reusable templates in `templates/`
- evaluations in `evals/`
- runtime skills in `skills/`
