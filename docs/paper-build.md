# Paper Build

AutoCHIResearch now treats PDF buildability as part of manuscript readiness.

## Command

```bash
python3 scripts/autochi.py build-paper <project-slug-or-path>
```

## Output Paths

- `output/exports/paper.pdf`
- `output/exports/paper-build.log`
- `output/exports/paper-build-status.md`

## Compiler Resolution

The build command checks for local TeX tooling in this order:

1. `latexmk`
2. `tectonic`
3. `pdflatex` together with `bibtex`

If none are available, the command writes a blocked build status instead of silently succeeding.

## Completion Rule

The `paper` stage should only be treated as complete when:

- `paper/main.tex` is a stand-alone long draft
- `paper/paper-review.md` has a `READY` verdict
- `output/exports/paper.pdf` exists from a successful build
