# Paper Judge Workflow

Use this reference when the project reaches the `paper` stage and `paper/main.tex` is no longer a
short shell.

## Goal

Run an independent manuscript-readiness review before the paper stage can be marked complete.

The review should answer one question:

- is this manuscript strong and complete enough, as a tracked AutoCHIResearch artifact, to count as
  a real stand-alone draft rather than an outline?

## Sub-Agent Setup

Spawn a dedicated sub-agent for this review once the manuscript has the required sections and enough
substance to evaluate. Do not ask that sub-agent to rewrite the paper at the same time.

Give the sub-agent only the minimum local context it needs:

- `paper/main.tex`
- `paper/paper-brief.md`
- `paper/references.bib`
- `output/analysis/results_summary.md`
- `analysis/analysis-plan.md`
- `artifacts/novelty-matrix.md` when the contribution claim is unclear

Do not feed the sub-agent your own verdict first. The review is meant to be independent.

## Required Output

The sub-agent must write or overwrite `paper/paper-review.md` using this exact field structure:

```md
# Paper Judge Review

## Scope
- Manuscript: `paper/main.tex`
- Brief: `paper/paper-brief.md`
- Results Summary: `output/analysis/results_summary.md`
- References: `paper/references.bib`

## Decision
Overall Verdict: READY|REVISE|BLOCKED
Ready for completion: YES|NO

## Dimension Ratings
CHI Framing and Contribution: PASS|REVISE
Related Work Coverage: PASS|REVISE
Method and Analysis Alignment: PASS|REVISE
Results Sufficiency: PASS|REVISE
Ethics and Privacy Framing: PASS|REVISE
Citation Hygiene: PASS|REVISE
Writing Cohesion: PASS|REVISE

## Blocking Issues
- concrete blocking issue or `- None`

## Revision Priorities
- concrete revision target

## Evidence Notes
- short evidence-backed note tied to the manuscript
```

## Verdict Rule

- `READY` means the paper is complete enough, coherent enough, and supported enough to count as the
  tracked paper-stage artifact.
- `REVISE` means the manuscript has a plausible paper shape but still has fixable weaknesses.
- `BLOCKED` means the manuscript is not reviewable as a paper yet because key results, sections, or
  evidentiary support are still missing.

Only mark `Ready for completion: YES` when:

- the verdict is `READY`
- every dimension rating is `PASS`
- `Blocking Issues` is effectively empty

## Review Standards

The sub-agent should judge whether the manuscript:

- is clearly framed as an HCI or CHI contribution rather than a generic essay
- uses related work to position the contribution rather than just list papers
- matches the method and results claims to the actual available evidence
- has enough results substance to support the discussion
- states ethics, privacy, and study limitations in a credible way
- cites enough relevant work to look like a real research draft
- reads as a connected manuscript instead of a stitched outline

The review should be firm. If the manuscript is only long, but still hollow, the verdict should not
be `READY`.
