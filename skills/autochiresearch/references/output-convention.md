# Output Convention

Use `output/` for generated artifacts that come from concrete runs, validation, or analysis rather than source-of-truth study design.

## Standard Layout

- `output/analysis`
  - generated tables
  - summaries
  - charts
  - derived CSV files
- `output/collection`
  - canonical CSV templates
  - imported external CSV snapshots
- `output/exports`
  - explicit database or admin exports
- `output/playwright`
  - screenshots
  - browser validation artifacts

## Rules

- Keep reusable source files under `artifacts/`, `studies/`, `analysis/`, `prototype/`, and `paper/`.
- Keep generated outputs under `output/` unless the repository already defines another explicit convention.
- Keep sensitive raw data or identifiable contact exports out of version control when ethics or privacy rules require it.
