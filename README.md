# AutoCHIResearch Skill

`autochiresearch` is a Codex skill for running a local-first HCI research workflow from a raw idea to a reusable research package.

It is designed for the workflow:

`idea -> literature / novelty -> study design -> survey or prototype -> local preview -> manual external distribution -> CSV import -> local analysis -> LaTeX drafting`

## What This Repo Contains

- `skills/autochiresearch/`
  - the main skill
- `skills/chi-project-runner/`
  - a backward-compatible alias that points to the same workflow semantics

## Main Design Choice

This skill is deliberately local-first. It does not assume that Codex must self-host or automatically launch a live server. The default path is:

1. build the study locally
2. preview locally
3. let a human distribute the questionnaire or prototype if needed
4. import returned CSV data back into the local project
5. analyze locally and continue writing locally

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/autochiresearch "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/chi-project-runner "${CODEX_HOME:-$HOME/.codex}/skills/"
```

If you only want the main skill:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/autochiresearch "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Invoke

Typical prompts:

```text
Use $autochiresearch to turn this idea into a local-first HCI study project.
```

Chinese usage:

```text
用 $autochiresearch 跑这个题，从 idea 一直到本地分析和成文。
```

Older prompts remain compatible through the alias:

```text
Use $chi-project-runner to continue this AutoCHIResearch project.
```

## Expected Repository Context

The skill assumes an AutoCHIResearch-style repository with:

- `scripts/autochi.py`
- `program.md` or `program.zh-CN.md`
- `projects/<slug>/STATE.json`
- project artifacts under `artifacts/`, `studies/`, `analysis/`, `paper/`

## Notes

- The skill is strongest when paired with narrower support skills such as citation management, study design, analysis, and scientific writing.
- For purely narrow tasks such as only literature search or only statistics, use the narrower skill directly instead of invoking the full workflow.
