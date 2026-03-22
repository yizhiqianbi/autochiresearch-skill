# 无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## 原始 Idea
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## 核心原则

人只需要提供一个原始 idea。除非被伦理审批、服务器权限、账号凭据或部署条件阻塞，否则剩下的研究流程默认由 Codex 接管并推进。

## 工作流结构

### Pre 阶段

- 研究问题整理
- 文献检索
- novelty 判断

### Mid 阶段

- 如有需要，设计 user study / questionnaire
- 如有需要，设计并实现 prototype
- 将问卷或原型部署出去并分发
- 执行实验并收集数据
- 规划分析并整理结果

### Post 阶段

- 写作
- 将实验结果综合成论文叙事和结论

## Codex 使用方式

1. 先读仓库根目录的 `program.md` 或 `program.zh-CN.md`。
2. 在仓库根目录运行 `python3 scripts/autochi.py status canvas-vs-terminal-multi-agent`。
3. 根据当前阶段完成对应 artifact 和支撑文件。
4. 每完成一个阶段后运行 `python3 scripts/autochi.py sync canvas-vs-terminal-multi-agent`。
5. 持续推进直到项目显示 `CurrentStage: done`。

## 关键路径

- `STATE.json`：项目状态机
- `artifacts/`：核心 markdown 产物
- `literature/`：检索日志与参考文献
- `studies/`：问卷、协议、实验材料
- `prototype/`：原型代码或说明
- `deploy/`：部署与分发
- `analysis/`：分析脚本与结果
- `paper/`：LaTeX 论文
- `output/`：每次运行的导出结果、截图、图表和中间分析产物
