# Study Specification

## Idea Anchor
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Research Questions
- `RQ1`: When the same multi-agent backend is exposed through an infinite canvas versus a terminal, how do users differ in planning, monitoring, and intervention strategies?
- `RQ2`: How do the two interface modalities change subjective workload, perceived control, plan recall, and recovery performance across different task types?
- `RQ3`: Which design properties do users want to keep from each modality when coordinating multiple AI agents in real knowledge-work settings?

## Hypotheses / Evidence Needed
- `H1`: The canvas condition will improve plan recall, state awareness, and monitoring confidence on coordination-heavy tasks because it externalizes agent roles, dependencies, and intermediate artifacts.
- `H2`: The terminal condition will support faster low-level corrections and lower interaction overhead on direct intervention tasks because commands and logs are colocated in a linear stream.
- `H3`: The canvas condition will reduce subjective workload for multi-step synthesis and monitoring tasks, while the terminal condition will be preferred for rapid expert interventions.
- `H4`: Participants will ask for hybrid interaction, specifically spatial overview plus direct textual control.
- Needed evidence:
  - condition-level differences in task time, recovery latency, task quality, and plan recall
  - subjective ratings for workload, transparency, controllability, and willingness to reuse
  - qualitative evidence of strategy shifts, self-generated workarounds, and breakdown recovery

## Study Type
Primary design: counterbalanced within-subject mixed-methods lab study with two interface conditions (`canvas`, `terminal`) and three matched task scenarios per participant.

Current local package: a synthetic dry run that validates the task structure, analysis pipeline, and manuscript scaffolding without claiming real human-subject results.

## Participants
- Target `N = 24` to `30` for the real study, with counterbalanced condition order
- Inclusion:
  - age 18+
  - use LLMs at least weekly for work or study
  - comfortable reading multi-step outputs, logs, or structured documents
- Desired experience mix:
  - roughly half with prior terminal experience
  - at least one third with prior visual workflow / whiteboard / node editor experience
- Exclusion:
  - no meaningful prior use of LLM tools
  - inability to complete both conditions
  - failed attention or protocol-compliance checks in the actual study

## Recruitment Plan
- Recruit AI-literate knowledge workers from graduate networks, technical online communities, and screened participant platforms such as Prolific
- Prescreen for:
  - frequency of LLM use
  - familiarity with terminal tools
  - familiarity with visual canvases or node-based tools
- Offer a fixed study payment for a `60` to `75` minute session in the real deployment
- For the current local-first package, do not recruit until the prototype, task rubric, and logging flow pass pilot checks

## Tasks / Flow
Each participant completes two interface conditions with the same underlying agent capabilities and task content. Order is counterbalanced.

Task set:

1. `Delegation / planning`
   - Participant receives a research request and must assign subtasks to three agents: literature scan, synthesis, and brief drafting.
   - Success depends on creating a coherent plan and checking whether subtasks cover the request.
2. `Monitoring / synthesis`
   - Participant reviews ongoing agent work, detects overlap or drift, and steers the system toward a final synthesis artifact.
   - Success depends on state awareness, dependency tracking, and synthesis quality.
3. `Recovery / correction`
   - One agent takes an erroneous action or drifts from scope.
   - Participant must identify the failure source, intervene, and re-route work efficiently.

Session structure for the real study:

- consent and background: `10` minutes
- interface tutorial and warm-up: `8` minutes
- first condition with three tasks: `18` minutes
- short post-condition questionnaire: `4` minutes
- second condition with three tasks: `18` minutes
- comparison questionnaire and interview: `12` to `15` minutes

## Measures
Behavioral:

- task completion time
- rubric-based task quality score
- number of interventions
- time-to-first-useful intervention
- recovery latency on the failure task
- plan recall score after each condition

Subjective:

- perceived workload items adapted from NASA-TLX style mental demand / effort / frustration framing
- transparency and inspectability
- perceived control over agent work
- confidence in monitoring multiple agents
- willingness to reuse in real work

Qualitative:

- think-aloud snippets during tasks
- post-condition open response on what felt easy, risky, or tiring
- final comparison interview about preferred hybrid features

## Prototype Requirements
- Same multi-agent backend behavior in both conditions using scripted agent outputs and branch points
- Terminal mode must support:
  - issuing commands
  - viewing a linear log
  - pausing, resuming, and redirecting agents
  - inspecting intermediate artifacts inline
- Canvas mode must support:
  - movable agent cards
  - visible dependency links
  - state badges
  - branch visualization
  - artifact inspection without losing overview
- Both modes must log the same event schema:
  - timestamp
  - condition
  - task
  - action type
  - target agent
  - intervention label
- The local prototype can remain a high-fidelity mockup for pilot purposes, but it must make the comparison concrete enough for walkthroughs and study materials

## Pilot Checklist
- Verify participants can understand the shared backend concept before the first task
- Confirm task instructions are matched across conditions
- Check whether the recovery task reliably triggers observable intervention behavior
- Make sure logs, scoring rubric, and observer sheet align on the same event names
- Run at least one local dry run for data export and analysis generation before recruitment
- Confirm the manuscript and figures clearly label synthetic outputs as non-empirical

## Stop Criteria
- Stop a real participant session if the participant requests to withdraw
- Stop if logging fails for an entire condition
- Stop if the prototype becomes non-responsive for more than `2` minutes during a task
- Exclude a session from confirmatory analysis if a participant misses an entire condition or fails the attention / protocol check
- Treat the current local package as pilot infrastructure only; do not interpret synthetic output as study evidence

## Ethics / Privacy Notes
- The real study should avoid collecting secrets, proprietary code, or personally identifying work artifacts
- If screen and interaction logs are recorded, participants must be told exactly what is stored and for how long
- Use synthetic tasks rather than participants' live work during early pilots
- Store exported logs under `output/collection/` and keep any identifiable participant mapping outside version control
- The current package contains only synthetic data and prototype mockups, so no real participant data are stored
