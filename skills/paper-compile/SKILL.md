---
name: paper-compile
description: >
  Compile a local LaTeX manuscript into PDF, surface TeX toolchain blockers, and leave reproducible
  build outputs under output/exports/. Use when a paper draft already exists and the user wants a
  PDF, a build log, or a clear diagnosis of why compilation failed. Prefer the AutoCHIResearch
  build entrypoint `python3 scripts/autochi.py build-paper <project>` when working inside this repo.
---

# Paper Compile

Use this skill when the manuscript already exists and the main task is to build or debug the PDF.

## Default Path

1. Confirm the project has `paper/main.tex`.
2. Run:
   - `python3 scripts/autochi.py build-paper <project-slug-or-path>`
3. Inspect:
   - `output/exports/paper.pdf`
   - `output/exports/paper-build.log`
   - `output/exports/paper-build-status.md`

## Toolchain Order

The build command prefers:

1. `latexmk`
2. `tectonic`
3. `pdflatex` together with `bibtex`

If none are available, do not pretend the paper compiled. Report the blocker clearly.

## Rules

- Do not mark the manuscript buildable without a real `paper.pdf`.
- Keep generated outputs under `output/exports/`.
- When compilation fails, summarize the real TeX blocker from the build log instead of giving vague advice.
