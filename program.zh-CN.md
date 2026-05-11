# AutoCHIResearch Program（中文版）

这个仓库是一套终端优先的 Codex 研究系统，用来把一个原始 HCI idea 推进成完整研究。

## 人类输入

默认情况下，人一开始只需要提供一件事：

- 一个原始 idea

除非被伦理审批、服务器权限、账号凭据、部署条件或其他外部限制阻塞，否则剩下的流程由 agent 接管。

## 三阶段结构

整个工作流被明确分成 `Pre / Mid / Post` 三段。

## Pre 阶段

目标：先理解题目，判断值不值得做。

包含阶段：

1. `brief`
   - 填 `artifacts/research-brief.md`
   - 明确问题、用户、系统概念、贡献、约束和成功标准
2. `novelty`
   - 使用 `citation-management` 和 `chi-topic-scout`
   - 覆盖 ACM DL、DBLP、Google Scholar 等来源
   - 写 `artifacts/novelty-matrix.md`、`literature/search-log.md`、`literature/references.bib`
   - 保留真实的阅读轨迹；到论文阶段时，项目通常应体现出一个 `40+` 篇论文的语料池
   - 如果结论是 `pivot` 或 `drop`，就停止，不要伪造推进

## Mid 阶段

目标：决定要做什么研究或系统，**构建它**，把它部署出去，并准备把行为和数据变成结果。

包含阶段：

1. `study`
   - 使用 `hci-study-designer`
   - 判断这个题目是否需要 questionnaire、user study、prototype、gameplay study 或 mixed method
   - 如果存在多个合理的 prototype / instrument 方向，要先写出精简的 prototype inventory，并在 build 前插入 human checkpoint
   - 写 `artifacts/study-spec.md`，并更新 `studies/`
2. `build`
   - 使用 `hci-study-designer` 和 `playwright`
   - **实际构建** study-spec 中指定的所有制品：原型应用、问卷、调查工具、刺激材料、任务评分表
   - 交付可运行的代码，而不是计划——原型必须能本地运行，问卷必须能端到端完成
   - 如果 study-spec 里标了 prototype checkpoint，就要先让人确认到底构建哪条 prototype 路径，并把这个决定记录进 `artifacts/build-report.md`
   - 写 `artifacts/build-report.md`，记录构建了什么、如何运行、以及冒烟测试清单
   - 不是每个项目都需要原型；study-spec 决定需要什么，这个阶段就构建什么
3. **数据模式选择门控**（build 完成后）
   - agent **必须**在继续之前让用户选择数据模式：
     - `synthetic` — 生成合成/模拟数据，立即验证完整流程
     - `real` — 暂停，等用户使用已构建的制品收集真实参与者数据
   - 通过 `python3 scripts/autochi.py set-data-mode <project> synthetic|real` 设置
   - 在选择之前，工作流在 deployment 阶段阻塞
4. `deployment`
   - 使用 `study-deployment-ops` 和 `playwright`
   - 如果 `synthetic`：在部署计划中同时准备合成数据生成脚本
   - 如果 `real`：设计真实部署计划（路由、监控、分发、导出），等用户收集数据
   - 如果缺少真实服务器凭据，也要留下可部署包和 blocker list
5. `analysis`
   - 使用 `hci-analysis-writer`
   - 如果 `synthetic`：在生成数据上运行分析流程，所有输出明确标注为合成数据
   - 如果 `real`：定义分析计划，等真实数据到位后再执行
   - 写 `analysis/analysis-plan.md`

## Post 阶段

目标：把实验输出整合成论文级别的论证。

包含阶段：

1. `paper`
  - 使用 `scientific-writing` 和 `citation-management`
  - 写 `paper/paper-brief.md`
  - 将结果综合成论文叙事
  - 在准备好后更新 `paper/main.tex`、`paper/adversarial-review.md`、`paper/paper-review.md` 和 `paper/references.bib`
  - 在 `paper/figure-plan.md` 里决定是否需要方法图 / pipeline 图
  - 默认使用 Codex 图像生成 / GPT Image 2 生成论文图片资产，把最终 PNG 存到
    `output/exports/figures/`，在 `paper/figure-plan.md` 里把 `Figure Decision` 设为
    `gpt-image-2`，不要默认走 PaperBanana
  - 把 `paper/figure-plan.md` 当成结构化 brief，而不是一句 caption；生图前要补完 visual style、
    must include / avoid、以及 human approval 这些字段
  - 摘要要保持紧凑，不要把引言层面的铺垫和细致相关工作都塞进 abstract
  - 引言要尽快交代 problem、gap 和 contribution，详细文献综合应主要放在 Related Work
  - 对于 workflow、interface、multi-step system 这类论文，图表包通常应包含方法图 / pipeline 图，而不只是一张 teaser 和结果图
  - 如果 GPT Image 2 暂时不可用，也要在 `paper/figure-plan.md` 里写出精确图片 brief，并用本地确定性绘图或 diagram 代码兜底
  - `paper/main.tex` 应该是可以独立阅读的 ACM `sigconf` 论文草稿，而不是每节只有一小段的短壳
  - 论文前部默认应该有一个真正的 `teaserfigure`，并且每张图都要同时写 `\caption{...}` 和
    `\Description{...}`
  - 到论文完成时，`paper/references.bib` 通常应至少有 `40+` 条经过验证的引用，并且这些引用背后应有真实阅读过程
  - 主稿必须用完整段落写作，不是 bullet 拼接；每个核心章节都要有足够篇幅支撑论证
  - `paper/main.tex` 必须至少有 `10000` 个可见英文词，编译后的 PDF 必须在
    `output/exports/rendered-pages/` 下至少渲染出 `10` 页；任一条件不足时，继续扩写主稿并重跑 `build-paper`
  - 主稿达到可审稿状态后，必须运行 adversarial reviewer subagent gate，产出
    `paper/adversarial-review.md`；至少包含四个独立审稿角色：
    methods/validity、systems/interaction contribution、related work/novelty、
    writing/claim-evidence/CHI fit
  - 当用户明确要求 subagent 且环境支持时，把这些角色作为独立 subagent 派发；否则串行扮演同样四个角色，并在 `paper/adversarial-review.md` 里记录 fallback
  - 每个 adversarial reviewer 都要像真实 CHI 审稿人一样先写拒稿风险，再写缺失证据、缺失图表/表格和具体修稿动作；作者必须修稿，并把每个 reviewer response 标为 `addressed` 或 `waived`
  - adversarial revision 完成后，再拉起最终 paper-judge sub-agent，产出 `paper/paper-review.md`
  - 最终评审结论为 `READY` 之后，还要运行 `python3 scripts/autochi.py build-paper <project>` 产出 PDF
  - 每次构建成功后，都要检查 `output/exports/rendered-pages/` 里的渲染页，持续修 teaser、
    figure、table 和正文排版，直到没有明显的裁切、重叠或拥挤问题
  - 只有当 adversarial review 完成、作者修订完成、最终评审结论是 `READY` 且 PDF 构建成功时，`paper` 阶段才允许被视为完成

## 强制规则

- 除非被阻塞，否则不要在阶段之间等待人类确认。
- 不允许跳过 novelty gate。
- 在没有 clear keep decision 之前，不允许直接设计实验。
- 当存在多个合理的 prototype 方向时，不允许静默替人做最终选择，必须插入 human checkpoint。
- 没有路由、存储、监控和导出计划时，不允许声称部署完成。
- 数据开始收集后，不允许随意修改 exclusion logic，除非把原因写清楚。
- 默认把人看作 idea provider，而不是整个流程的手动操作者。

## 初始化方式

当一个新 idea 到来时：

1. 运行：
   - `python3 scripts/autochi.py init --idea "<raw idea>"`
2. 读取：
   - 生成项目目录下的 `README.md`
   - 生成项目目录下的 `README.zh-CN.md`
   - 生成项目目录下的 `STATE.json`
   - 根目录的 `program.md` 或本文件
3. 运行：
   - `python3 scripts/autochi.py status <project-path>`

生成出来的项目目录就是该次研究 run 的事实来源。默认新项目会放在仓库外的同级
`autochiresearch-projects/` 目录，或者 `AUTOCHI_PROJECTS_DIR` 指向的位置；仓库内旧的
`projects/` 目录仍然可以继续恢复和推进。

## 成功条件

一个 run 成功的标志是：

- `Pre` 阶段完成
- `Mid` 阶段完成
- `Post` 阶段完成
- 项目状态显示 `CurrentStage: done`

到这一步，项目就已经进入“可继续实现、可继续上线收数、可继续打磨论文”的状态。
如果 `paper/adversarial-review.md` 缺失或仍有未解决项，或者 `paper/paper-review.md` 仍然要求修改，
项目仍然停留在 `paper` 阶段，不算 `done`。如果 `paper/figure-plan.md` 明确要求生成 figure，
但还没有产出对应图片，项目也会继续停留在 `paper` 阶段。
