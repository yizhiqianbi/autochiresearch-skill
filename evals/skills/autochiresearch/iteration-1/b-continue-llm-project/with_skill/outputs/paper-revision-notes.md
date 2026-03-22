# Paper Revision Notes
<!-- AutoCHIResearch — editorial review of paper/main.tex -->
<!-- Project: llm / LLM对大学生就业的影响 -->
<!-- Date: 2026-03-22 -->

These notes document specific editorial issues found in the current `paper/main.tex` draft. Each note includes a location, the problem observed, and a recommended fix. All items are pre-data: they can be addressed now without waiting for real participant data.

---

## A. Abstract — Synthetic-Data Framing Must Be Removed

**Location**: `\begin{abstract}…\end{abstract}`

**Problem**: The abstract currently leads with a pipeline-validation rationale ("To validate the local-first analysis and writing pipeline before live deployment, we generated a synthetic dataset…"). This framing is appropriate for internal project documentation but must not appear in a CHI submission abstract. Reviewers will reject a paper whose abstract describes a synthetic dry run as the empirical contribution.

**Recommended fix**: After real data collection, rewrite the abstract using the standard CHI structure: motivation and gap (2–3 sentences), method summary (1–2 sentences), key findings (2–3 sentences), and contribution claim (1 sentence). The working title ("From Resume Drafting to Interview Rehearsal: Understanding How University Students Use LLMs for Career Preparation") is strong and should be retained.

---

## B. Introduction — Research Question Is Implicit, Not Explicit

**Location**: `\section{Introduction}`, final paragraph

**Problem**: The paragraph ends with a description of the project's aims ("The project therefore asks how university students use LLMs across career-preparation tasks, how they perceive those interactions as shaping confidence and employability…") but does not state the four research questions from `artifacts/study-spec.md` (RQ1–RQ4). CHI reviewers expect either explicit RQs or a clear contribution statement in the Introduction.

**Recommended fix**: After the final paragraph of the Introduction, add a short paragraph that explicitly lists RQ1–RQ4 or collapses them into a two-sentence contribution statement. Example:

> Concretely, this paper addresses four research questions: (RQ1) which career-preparation tasks involve LLMs and how frequently; (RQ2) how LLM use shapes perceived confidence and employability; (RQ3) what tensions students report around authenticity, overreliance, and skill development; and (RQ4) what design implications follow for responsible student-facing career-support systems.

---

## C. Related Work — Two Missing Citation Candidates

**Location**: `\section{Related Work}`

**Problem**: The related work covers metacognition, student perceptions, disability, co-design, and career systems. It does not yet cite literature on AI-mediated self-presentation or resume writing beyond a single mention of Chakrabarty et al. If real findings highlight resume generation and authenticity concerns strongly, the related work section will need additional grounding in writing-assistance and self-presentation literature.

**Recommended fix**: Consider adding 1–2 citations from HCI or education literature on AI-assisted writing, cover letters, and personal statements once the final results direction is confirmed. Do not pad the related work with tangentially relevant papers; only add if the findings specifically require that foundation.

---

## D. Method — Synthetic Dataset Paragraph Flags the Whole Paper

**Location**: `\section{Method}`, final paragraph (begins "Because real data collection had not yet begun…")

**Problem**: This paragraph explicitly labels the current analysis as a synthetic dry run. This is accurate for the current internal state but is the single largest submission blocker. It is correctly positioned for now, but it marks every downstream result and discussion claim as placeholder.

**Recommended fix**: Delete this paragraph entirely once real data are collected and the analysis pipeline has been re-run. Replace the method section's closing paragraph with a brief account of the actual data collection timeline, recruitment channel, final N, and survey platform used.

---

## E. Results — Tables Are Described But Not Inserted

**Location**: `\section{Results}`

**Problem**: The analysis plan specifies four tables (sample characteristics, task-by-task frequencies, scale descriptives and reliability, regression or association models) and three figures. The current LaTeX draft describes findings in prose but does not include any `tabular` or `\includegraphics` environments. The paper as written has no tables or embedded figures.

**Recommended fix**: After regenerating all analysis outputs with real data, insert tables using the standard ACM `table` and `tabular` environments. Insert figures using `\includegraphics{../output/analysis/figure_task_distribution.pdf}` (or equivalent). Add `\label{}` and `\ref{}` cross-references for all figures and tables. Confirm that ACM sigconf class handles table/figure float placement correctly before submission.

---

## F. Discussion — Design Implications Need Inline Evidence Links

**Location**: `\section{Discussion}`, paragraph on four design implications

**Problem**: The four design implications (preserve authorship, support verification, support skill-development reflection, institutional guidance) are well-structured but currently read as free-standing claims. In the final submission, each implication should cite a result finding or quote from the data.

**Recommended fix**: After inserting real results, revise each implication paragraph to reference a specific finding (e.g., "Given that X% of heavy users reported authenticity tension…" or "Interview participants described wanting to see which edits the LLM made so they could decide whether to keep them…"). This grounds the implications in evidence and makes them harder to dismiss as speculative.

---

## G. Ethics Section — Venue-Specific Ethics Statement May Be Required

**Location**: `\section{Ethics and Privacy}`

**Problem**: CHI 2026 and recent ACM venues have required a formal positionality or ethics statement. The current Ethics section covers participant privacy, data minimization, and neutral framing. It does not include a researcher positionality statement or an explicit IRB/ethics board reference.

**Recommended fix**: Before submission, add a one-sentence note about whether the study received institutional ethics review (or confirm that the venue's APA/ACM ethics framework applies). If the venue requires a positionality statement, add a short paragraph describing the researchers' relationship to the subject matter (e.g., whether the authors are students, educators, or practitioners).

---

## H. Minor Wording Issues

| Location | Issue | Fix |
|---|---|---|
| Abstract, sentence 4 | "This manuscript draft frames the project" — "manuscript draft" is informal for a submission | Remove "manuscript draft"; rewrite as empirical framing after real data |
| Introduction, paragraph 1 | "That framing is too coarse for human-computer interaction" — slightly dismissive of prior discourse | Soften to "that framing does not readily translate into interaction-level insights" |
| Results, paragraph 2 | "among LLM users, the most common weekly-or-more activities were resume drafting (59.4%)" — all numbers are synthetic | Replace after real analysis; retain sentence structure |
| Limitations, paragraph 1 | "The strongest limitation is that the current analysis uses synthetic rather than empirical data" — must be removed entirely | Delete once real data are in place |

---

## Summary: Pre-Data Fixes vs. Post-Data Fixes

**Can be done now (pre-data)**:
- Note B: Add explicit RQ list to Introduction
- Note C: Identify candidate new references if findings confirm specific directions
- Note G: Confirm ethics review status and add statement
- Note H: Minor wording fixes in Introduction

**Requires real data**:
- Note A: Rewrite abstract
- Note D: Remove synthetic dataset paragraph from Method
- Note E: Insert tables and figures
- Note F: Ground design implications in actual findings
- Note H (Results and Limitations rows)
