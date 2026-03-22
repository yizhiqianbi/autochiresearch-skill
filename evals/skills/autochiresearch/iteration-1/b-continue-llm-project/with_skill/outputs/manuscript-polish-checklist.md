# Manuscript Polish Checklist
<!-- AutoCHIResearch — post-pipeline, pre-submission readiness -->
<!-- Project: llm / LLM对大学生就业的影响 -->
<!-- Venue: CHI -->
<!-- Date: 2026-03-22 -->

This checklist covers every task remaining between the current complete-pipeline state and a submission-ready manuscript. Work through it top to bottom after real data are collected.

---

## 1. Data Collection Gate

- [ ] Deploy survey instrument through university mailing lists, career-center channels, and WeChat/class groups.
- [ ] Run pilot with 8–12 students; confirm wording clarity, completion time (~10–12 min), and column schema stability.
- [ ] Collect ≥250 valid responses including ≥150 self-identified LLM users.
- [ ] If opting into follow-up interviews, recruit 12–20 participants; store contact info in a file separate from survey data.
- [ ] Import final CSV export: `python3 analysis/import_flat_csv.py --csv <returned.csv> --db prototype/data/<db>.db`

## 2. Analysis Replacement

- [ ] Re-run the exclusion logic from `analysis/analysis-plan.md` against the real dataset; document all exclusions in `output/analysis/exclusion_log.csv`.
- [ ] Recompute all 7 derived variables (`llm_user_binary`, `task_diversity_score`, `use_intensity_score`, `confidence_support_score`, `verification_score`, `authenticity_tension_score`, `career_stage_group`).
- [ ] Re-run descriptive summaries, group comparisons, and regression models; save outputs to `output/analysis/`.
- [ ] Regenerate Figure 1 (task distribution), Figure 2 (benefits vs. risks by task), and Figure 3 (design-opportunity map).
- [ ] Report Cronbach's alpha or omega for multi-item constructs where reliability is acceptable.
- [ ] Conduct reflexive thematic analysis on open-ended responses using the two-pass coding procedure in the analysis plan.

## 3. LaTeX Manuscript — Content Updates

- [ ] **Abstract**: remove the pipeline-validation framing; replace with a concise empirical summary once real results are known.
- [ ] **Method section**: remove the synthetic-dataset paragraph ("Because real data collection had not yet begun…"); replace with the actual data collection timeline, platform used, and final N.
- [ ] **Results section**: replace all synthetic numbers, percentages, and regression coefficients with real values; remove all "synthetic" qualifiers.
- [ ] **Discussion section**: revise to reflect the actual findings; keep the four design implications but ground them in real evidence rather than the placeholder story.
- [ ] **Limitations section**: remove the first synthetic-data limitation once real data replace it; retain the remaining limitations (self-report, convenience sampling, cultural context).
- [ ] **Figures**: replace placeholder PNG files in `output/analysis/` with publication-quality versions (vector-based PDF or high-res PNG ≥300 dpi); insert figures into the LaTeX source using `\includegraphics`.
- [ ] **Tables**: insert Tables 1–4 as `tabular` environments in the LaTeX source; currently they are described in the analysis plan but not yet in `main.tex`.

## 4. References and Citations

- [ ] Verify all 11 entries in `paper/references.bib` against ACM DL, arXiv, and publisher pages; confirm DOIs resolve.
- [ ] Add any new works cited during analysis or revision.
- [ ] Ensure every `\cite{}` key in `main.tex` matches a BibTeX key in `references.bib`.
- [ ] Run BibTeX and resolve any undefined-citation or missing-field warnings.

## 5. ACM Submission Formatting

- [ ] Confirm `\documentclass[sigconf]{acmart}` and author-year reference format match the current CHI submission guidelines.
- [ ] Fill in author names, affiliations, and email addresses (replace anonymous placeholders before camera-ready; keep anonymous for blind review).
- [ ] Add ACM CCS concepts (`\ccsdesc`) and keywords (`\keywords`) block.
- [ ] Add a Conflicts of Interest or acknowledgment section if required by the venue.
- [ ] Page-count check: CHI full papers are typically 10–14 pages excluding references; verify once the results section is filled with real content.
- [ ] Run the full LaTeX build: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`; confirm zero errors and a clean PDF.

## 6. Internal Review

- [ ] Co-author review pass: check claim boundaries (reported practice vs. perceived effect vs. design implication).
- [ ] Verify that no sentence asserts a causal employment outcome from self-report data.
- [ ] Proofread for consistency in LLM tool names, scale labels, and terminology across sections.
- [ ] Check that all figures and tables are cited in the text.

## 7. Submission Package

- [ ] Prepare a supplementary material archive containing the anonymized survey instrument, codebook, and analysis scripts.
- [ ] Confirm the paper does not include identifying information in the main document (anonymous review).
- [ ] Export final PDF and upload to the CHI submission system.

---

## Checklist Status Summary

| Category | Total Items | Completed |
|---|---|---|
| Data Collection | 5 | 0 |
| Analysis Replacement | 7 | 0 |
| Manuscript Content | 7 | 0 |
| References | 4 | 0 |
| ACM Formatting | 6 | 0 |
| Internal Review | 5 | 0 |
| Submission Package | 3 | 0 |
| **Total** | **37** | **0** |

All 37 items depend on real data collection. The pipeline and draft are structurally complete; the remaining work is empirical and editorial.
