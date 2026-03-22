# Novelty Matrix

## Original Idea
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Search Queries
- `"multi-agent interface" CHI debugging steering agents`
- `"infinite canvas" sensemaking CHI workspace`
- `"terminal" "human-AI agent collaboration"`
- `"visual toolkit" prompt engineering CHI`
- `"computational notebooks" layout study CHI`
- `"co-planning and co-execution with AI agents"`
- `"human-in-the-loop agentic systems" interface`

## Source Coverage
- ACM CHI / CHI EA papers on visual prompt engineering, debugging, and interface evaluation
- arXiv papers on emerging agentic-system interfaces and terminal-oriented design arguments
- ACL Anthology entry for AutoGen Studio
- TVCG / VIS work on LLM evaluation interfaces
- Prior HCI theory on space-to-think and spatial offloading for sensemaking

## Related Work Table
| Paper | Venue/Year | Problem | Method | Population | System/Prototype | Main Finding | Gap vs Us |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Andrews et al., *Space to Think* | CHI 2010 | How larger spatial workspaces support sensemaking | Observational study on large displays | Analysts | Large high-resolution sensemaking workspace | Spatial layout supports external memory, relationship tracing, and analytic thinking | Not about AI agents, terminals, or matched interface comparison |
| Wu et al., *PromptChainer* | CHI EA 2022 | How users chain multiple LLM prompts for complex tasks | Pilot studies + case studies | 4 users | Visual node-based chaining interface | Visual chaining improves transparency and controllability for multi-step prompting | Early prompt-chain tool, not multi-agent supervision and no comparison to terminal |
| Mishra et al., *PromptAid* | arXiv 2025 | How non-experts iterate on prompts with less cognitive overhead | Iterative prototyping + quantitative and qualitative assessment | LLM users | Coordinated visual analytics views for prompt testing | Visual analytics can lower overhead during prompt iteration | Focused on single-prompt refinement, not multi-agent coordination or terminal comparison |
| Arawjo et al., *ChainForge* | CHI 2024 | Support prompt engineering and hypothesis testing across models | In-lab + interview studies | Academics and online users | Graphical toolkit for prompt and model comparison | Identifies exploration, limited evaluation, and iterative refinement modes | Evaluates visual toolkit use, but not agent supervision or linear command interfaces |
| Kim et al., *EvalLM* | CHI 2024 | Help prompt designers evaluate outputs on user-defined criteria | Interviews + comparative study | Prompt designers | Interactive evaluation interface | Participants inspected more outputs and needed fewer revisions | Evaluation-focused rather than task-time coordination of multiple agents |
| Kahng et al., *LLM Comparator* | TVCG / CHI EA 2024-2025 | Interpret side-by-side LLM evaluations at scale | Industry-centered iterative design + observational study | Researchers and engineers | Visual analytics for side-by-side model comparisons | Visual aggregation aids interpretability of many comparisons | Comparison is between model outputs, not between interaction modalities for agent oversight |
| Dibia et al., *AutoGen Studio* | EMNLP Demo 2024 | Make building and debugging multi-agent systems easier | Design principles + open-source system demo | Developers | Drag-and-drop multi-agent workflow builder | No-code interfaces can lower setup and debugging barriers | Describes a graphical builder, but not empirical comparison with terminal workflows |
| Epperson et al., *Interactive Debugging and Steering of Multi-Agent AI Systems* | CHI 2025 | Support debugging of long, complex agent conversations | Interviews + two-part user study (N=14) | Agent developers | AGDebugger with message browser, resets, overview visualization | Long multi-agent traces need overview and reset mechanisms | Strongly relevant to debugging, but not a matched terminal-vs-canvas study |
| Lin et al., *InterLink* | CHI 2025 | Improve understanding of linear computational notebooks | Formative study + user study (N=12) | Notebook readers | Two-column linked notebook layout | Alternative layouts improved accuracy by 13.6% for complex analyses | Shows linear layouts have comprehension limits, but not in agent coordination |
| Mozannar et al., *Magentic-UI* | arXiv 2025 | Human-in-the-loop interfaces for agentic systems | Benchmarking + simulated user testing + qualitative study | Mixed users | Extensible interface with co-planning, multi-tasking, action guards | Human oversight should be embedded into agentic interfaces | Not a modality comparison and not specifically spatial-canvas vs terminal |
| Feng et al., *Cocoa* | CHI 2026 | Flexible human-agent collaboration in long-running tasks | Formative study + lab study (n=16) + field deployment (n=7) | Researchers | Notebook-inspired co-planning / co-execution interface | Shared plans improve steerability without losing ease of use | Notebook-inspired but not infinite canvas, and no direct terminal contrast |
| De Masi, *Terminal Is All You Need* | arXiv / CUCHI workshop 2026 | Why terminal tools dominate agent practice | Design analysis grounded in HCI theory | N/A | Conceptual analysis of terminal-based tools | Terminal tools benefit from representational compatibility, transparency, and low entry cost | Offers a strong terminal-side argument, but no empirical comparison with spatial interfaces |

## Decision
- Topic status: Narrow and keep
- Main novelty axis: A matched comparison of representational modalities for multi-agent supervision, with the same backend exposed through a terminal and an infinite canvas
- Keep / Pivot / Drop: KEEP
- Why: Existing literature provides strong ingredients but no direct answer. Visual tools show benefits for prompt/program comprehension and spatial externalization; terminal-oriented work argues for transparency and low-friction control; recent multi-agent interface papers emphasize overview, steering, and co-planning. What is still missing is a controlled HCI comparison of how spatial and textual representations change human coordination strategies, workload, and recovery behavior when supervising the same multi-agent system on the same tasks.
