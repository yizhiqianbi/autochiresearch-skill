# Paper Brief

## Original Idea
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Target Venue
CHI

## Working Title
Space to Steer, Text to Command: Comparing Infinite-Canvas and Terminal Interfaces for Multi-Agent Supervision

## Abstract Focus
The paper argues that interface representation is now a central HCI problem in multi-agent systems. It contributes a matched-interface comparison framework, a local-first prototype, a mixed-methods study design, and a synthetic dry run that validates the analysis and writing pipeline. The abstract must be explicit that the dry-run numbers are descriptive and non-empirical.

## Introduction Claim
The central claim is that terminal and infinite-canvas interfaces do not simply differ in visual style; they redistribute what users must remember, where they notice breakdowns, and how they intervene. Current literature introduces tools in both families, but lacks a controlled comparison of representational modality under a shared backend.

## Related Work Angle
The related-work section should bridge four threads: spatial sensemaking and external cognition, visual prompt / workflow tools, emerging multi-agent oversight interfaces, and terminal-oriented design arguments. The point is not to review each tool in isolation, but to show that the field has all the pieces for the comparison while still missing the comparison itself.

## Method Story
The method centers on a matched prototype with the same scripted multi-agent backend exposed through `canvas` and `terminal` conditions. Three tasks cover delegation, monitoring, and recovery. A within-subject study is planned, while the current repository includes only a synthetic dry run used to validate logging, analysis outputs, and manuscript flow.

## Results Spine
The results section should present descriptive dry-run patterns only. Canvas should appear stronger for monitoring, plan recall, and lower workload in coordination-heavy tasks, while terminal should appear stronger for rapid repair and direct corrective action. The section must repeatedly state that the numbers are synthetic and only validate the intended evaluative logic.

## Discussion Arc
The discussion should argue for hybrid agent interfaces rather than choosing a single winner. Spatial overview and branch visibility should be combined with terminal-grade precision, commandability, and low-friction repair. The broader implication is that agent-interface research should compare representational choices while holding backend capability constant.

## Limitations
The package does not contain real participant data, so the manuscript cannot claim confirmatory evidence. The prototype is a high-fidelity mockup rather than a production agent runtime. The synthetic dry run encodes hypothesized tradeoffs and therefore validates the pipeline, not the truth of the claims.
