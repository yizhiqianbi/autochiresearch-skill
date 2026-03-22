# Research Brief

## Original Idea
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Working Title
Space to Steer, Text to Command: Comparing Infinite-Canvas and Terminal Interfaces for Coordinating Multiple AI Agents

## Research Problem
As multi-agent AI systems become practical for research, coding, and long-running knowledge work, interface design has become a first-order problem rather than a thin wrapper around model calls. Current tool ecosystems are splitting into two dominant interaction styles. One style uses terminal-like linear command streams that privilege low-friction invocation, explicit logs, and direct intervention. The other style uses spatial or canvas-like workspaces that externalize plans, branches, agent roles, and intermediate artifacts in a shared visual field. Prior work has introduced tools in each family, but the field still lacks a head-to-head comparison of how these interface representations change actual human supervision strategies when the underlying multi-agent capability is held constant.

The central problem of this project is therefore not "which interface is prettier" but how representation affects human coordination. When people supervise several agents at once, they must form and revise a mental model of who is doing what, what state each subtask is in, where failures originated, and when to intervene. We do not yet have clear evidence about whether an infinite canvas helps by offloading cognition into space, or whether a terminal helps by preserving action transparency and low interaction cost. This gap matters for HCI because agentic workflows are increasingly long-running, high-context, and error-prone.

## Target Users / Population
- Knowledge workers who already use LLMs for complex tasks such as literature synthesis, planning, coding, and document production
- AI-native researchers, developers, analysts, and technical product workers who may supervise more than one agent or thread at a time
- Secondary population for future work: novice agent users who benefit differently from spatial scaffolding versus terminal directness

## Interaction or System Concept
We will build a matched-interface research prototype with the same multi-agent backend exposed through two interfaces:

- `Terminal mode`: a linear, command-first interface that shows agent logs, status changes, interventions, and message history in a textual stream
- `Canvas mode`: a spatial, infinite-canvas interface that represents agent roles, subtasks, dependencies, outputs, and intervention points as movable cards connected in a shared workspace

Both modes will support the same core actions: assign subtasks, inspect intermediate outputs, pause or resume agents, redirect work, and recover from errors. The design comparison is therefore about representational and interaction differences, not different models or task coverage.

## Expected Contribution
This project targets four contributions:

1. An HCI framing of multi-agent supervision as a representational coordination problem rather than only a prompting or orchestration problem.
2. A comparative prototype that isolates two increasingly common interface paradigms for agentic work: spatial infinite-canvas coordination and terminal-style command coordination.
3. A mixed-method evaluation plan that measures task success, recovery behavior, strategy shifts, and subjective workload under matched multi-agent tasks.
4. Design implications for future agent interfaces, including which properties of terminal systems should be preserved in spatial tools, and which properties of spatial tools should be imported into command-driven systems.

## Candidate Methods
- Literature review focused on agent-debugging interfaces, visual prompt/programming tools, spatial sensemaking systems, and terminal-oriented human-agent interaction
- Matched prototype implementing terminal and canvas conditions over the same scripted multi-agent backend
- Within-subject task study with counterbalanced order, using multi-step knowledge-work tasks that require planning, monitoring, and recovery
- Measures: task completion, intervention count, correction latency, plan recall, NASA-TLX style workload items, perceived control, transparency, and post-task interviews
- Local-first dry run with synthetic data to validate analysis scripts and manuscript structure before any real data collection

## Target Venue
CHI

## Constraints
- The current repository can produce a credible local-first research package, prototype, and long paper draft, but cannot claim real participant data unless such data are actually collected.
- The comparative prototype should not depend on proprietary hosted infrastructure for core interaction.
- The manuscript must stay explicit about evidence boundaries: local mockups and synthetic results are for pipeline validation, not final empirical claims.
- The user explicitly requested a manuscript of at least `5000` words, so the paper stage must exceed the default project threshold.

## Success Criteria
- The novelty gate concludes `KEEP` because no prior work directly compares infinite-canvas and terminal supervision for matched multi-agent workflows.
- The project leaves a runnable local prototype, a concrete study protocol, and reproducible synthetic analysis outputs.
- The paper draft reaches `5000+` visible words, cites adjacent CHI / CSCW / VIS / arXiv work accurately, and compiles to PDF locally.
- The manuscript produces actionable design implications instead of a generic opinion piece about "visual vs textual" interfaces.
