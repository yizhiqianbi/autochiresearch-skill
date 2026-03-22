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
   - 如果结论是 `pivot` 或 `drop`，就停止，不要伪造推进

## Mid 阶段

目标：决定要做什么研究或系统，把它部署出去，并准备把行为和数据变成结果。

包含阶段：

1. `study`
   - 使用 `hci-study-designer`
   - 判断这个题目是否需要 questionnaire、user study、prototype、gameplay study 或 mixed method
   - 写 `artifacts/study-spec.md`，并更新 `studies/`
2. `deployment`
   - 使用 `study-deployment-ops` 和 `playwright`
   - 处理部署、路由、监控、分发和导出
   - 如果缺少真实服务器凭据，也要留下可部署包和 blocker list
3. `analysis`
   - 使用 `hci-analysis-writer`
   - 预先定义 exclusion logic、derived variables、定量分析、定性分析和计划输出
   - 写 `analysis/analysis-plan.md`

`Mid` 阶段也是 agent 判断“是否真的需要做 prototype”的位置。不是所有 CHI 项目都必须做原型。

## Post 阶段

目标：把实验输出整合成论文级别的论证。

包含阶段：

1. `paper`
  - 使用 `scientific-writing` 和 `citation-management`
  - 写 `paper/paper-brief.md`
  - 将结果综合成论文叙事
  - 在准备好后更新 `paper/main.tex` 和 `paper/references.bib`
  - `paper/main.tex` 应该是可以独立阅读的 ACM `sigconf` 论文草稿，而不是每节只有一小段的短壳
  - 主稿完成后，必须再拉起一个独立的论文评审 sub-agent，产出 `paper/paper-review.md`
  - 只有当评审结论是 `READY` 时，`paper` 阶段才允许被视为完成

## 强制规则

- 除非被阻塞，否则不要在阶段之间等待人类确认。
- 不允许跳过 novelty gate。
- 在没有 clear keep decision 之前，不允许直接设计实验。
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
如果 `paper/main.tex` 已经有篇幅，但 `paper/paper-review.md` 仍然要求修改，则项目仍然停留在
`paper` 阶段，不算 `done`。
