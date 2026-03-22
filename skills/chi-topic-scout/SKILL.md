---
name: chi-topic-scout
description: >
  Search the HCI literature for a given research idea and produce a novelty assessment — querying
  ACM DL, DBLP, Google Scholar, IEEE Xplore, and arXiv — then deliver a related-work map, a
  novelty matrix, and a concrete keep, pivot, or drop recommendation. Use this skill whenever
  the user needs to know if an HCI idea is novel, wants a literature review or related-work map,
  or needs to pass the novelty gate before designing a study. If someone mentions CHI, CSCW, UIST,
  HRI, UbiComp, or asks "has this been done?" or "what's the closest work?" in a user-interaction
  or HCI domain, use this skill. Don't wait for the user to say "do a novelty check" — if they
  have an HCI idea and haven't assessed novelty yet, use this skill.
---

# CHI Topic Scout

Use this skill when a user has an HCI research idea and needs to know whether the topic has already
been done, what the closest papers are, and where the remaining novelty is.

## Workflow

1. Normalize the idea into five fields: problem, target users, system/intervention, evaluation
   style, and expected contribution.
2. Generate HCI-specific search queries, including synonyms for users, task, setting, and
   interaction modality.
3. Search broadly first, then narrow to the most similar combinations of problem + system + method.
4. Use `citation-management` to validate metadata and build BibTeX.
5. Record each close paper in a comparison table with: method, sample size, prototype shape,
   findings, and how it differs from the current idea.
6. Produce a novelty matrix that answers:
   - has this exact combination been done?
   - what has been partially done?
   - what gap remains?
7. End with a clear, decisive recommendation: **keep**, **pivot**, or **drop** — with one paragraph
   of rationale. Do not hedge if the evidence is clear.

## Source Coverage

For CHI-style projects, do not stop at Google Scholar. Cover these sources as needed:

- ACM Digital Library for CHI, CSCW, UIST, UbiComp, DIS, IUI, IMWUT
- DBLP for author and venue navigation
- Google Scholar for broad recall and citation chasing
- IEEE Xplore when the topic overlaps HRI, sensing, or engineering systems
- arXiv for recent preprints

## Outputs

Produce these artifacts:

- updated `artifacts/research-brief.md` (if one exists in the project)
- `literature/search-log.md` — queries run, sources checked, hits reviewed
- `literature/references.bib`
- `artifacts/novelty-matrix.md`
- keep/pivot/drop decision with one paragraph of rationale
