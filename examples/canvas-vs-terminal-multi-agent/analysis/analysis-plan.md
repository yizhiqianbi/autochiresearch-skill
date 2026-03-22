# Analysis Plan

## Idea Anchor
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Inclusion / Exclusion Rules
- Include only participants who:
  - consented
  - completed both interface conditions
  - passed the protocol / attention check
  - have usable logs for all three tasks
- Exclude participants who:
  - withdraw
  - lose a full condition because of prototype failure
  - fail the attention check
- In the synthetic dry run, two participants are intentionally excluded to validate the pipeline

## Derived Variables
- `task_success_pct`: rubric-based quality score from `0` to `100`
- `completion_seconds`: task duration
- `intervention_count`: number of user steering actions
- `recovery_latency_seconds`: delay from visible failure cue to corrective action
- `workload_score`: mean of mental demand and effort items
- `transparency_score`: mean of inspectability / monitoring items
- `control_score`: perceived control item
- `plan_recall_score`: post-condition reconstruction score
- `reuse_score`: willingness to reuse the interface in real work

## Statistical Analysis
- Primary confirmatory analysis for a real study:
  - within-subject comparison between `canvas` and `terminal`
  - Wilcoxon signed-rank or paired t-tests depending on distribution
  - task-specific exploratory comparisons for `delegation`, `monitoring`, and `recovery`
- Planned reporting:
  - condition means and standard deviations
  - effect directions and confidence intervals where appropriate
  - no claim that an interface is globally superior without task-context qualification
- For the synthetic dry run:
  - compute descriptive summaries only
  - generate figures and tables to validate the reporting pipeline

## Qualitative Analysis
- Use post-condition open responses and interview notes
- First-pass coding categories:
  - spatial overview and memory offloading
  - low-friction intervention
  - hidden state or uncertainty
  - navigation overhead
  - hybrid feature requests
- Conduct a lightweight thematic synthesis for the synthetic dry run and a fuller reflexive thematic analysis when real data exist

## Figures and Tables
- Table 1: participant characteristics
- Table 2: condition summary across key metrics
- Table 3: task-by-condition summary
- Figure 1: workload by condition
- Figure 2: plan recall by condition
- Figure 3: task success by condition and task type
- Figure 4: qualitative theme counts by condition

## Reporting Notes
- Clearly label all current outputs as synthetic dry-run artifacts
- Use the dry run to check wording, file paths, figure generation, and manuscript integration
- Do not convert synthetic patterns into confirmatory claims
