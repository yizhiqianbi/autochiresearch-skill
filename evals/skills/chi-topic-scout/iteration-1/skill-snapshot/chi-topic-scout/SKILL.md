---
name: chi-topic-scout
description: Turn an HCI or CHI idea into search queries, a related-work map, a novelty matrix, and a keep-or-pivot recommendation. Always use citation-management for metadata and BibTeX, and cover ACM DL, DBLP, Google Scholar, IEEE Xplore, and arXiv as appropriate.
---

# CHI Topic Scout

Use this skill when a user has an HCI research idea and needs to know whether the topic has already been done, what the closest papers are, and where the remaining novelty is.

## Workflow

1. Normalize the idea into five fields: problem, target users, system/intervention, evaluation style, and expected contribution.
2. Generate HCI-specific queries, including synonyms for users, task, setting, and interaction modality.
3. Search broadly first, then narrow to the most similar combinations of problem + system + method.
4. Use `citation-management` to validate metadata and build BibTeX.
5. Record each close paper in a comparison table with method, sample, prototype shape, and findings.
6. Produce a novelty matrix that answers:
   - has this exact combination been done
   - what has been partially done
   - what gap remains
7. End with a clear recommendation: keep, pivot, or drop.

## Source Coverage

For CHI-style projects, do not stop at Google Scholar. Cover these sources as needed:

- ACM Digital Library for CHI, CSCW, UIST, UbiComp, DIS, IUI, IMWUT
- DBLP for author and venue navigation
- Google Scholar for broad recall and citation chasing
- IEEE Xplore when the topic overlaps HRI, sensing, or engineering systems
- arXiv for recent preprints

## Outputs

Produce these artifacts whenever possible:

- updated `research brief`
- `literature` notes or table
- `references.bib`
- `novelty matrix`
- keep-or-pivot decision with one paragraph of rationale
