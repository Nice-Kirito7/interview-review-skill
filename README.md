# Interview Review Skill · 面试复盘与项目宝典

把一次面试的逐字稿，变成下一次面试能用上的问答与练习。

**状态：v0.1 草案。尚未完成真实逐字稿端到端验证。** 当前提供 skill 指令、维护规则和虚构示例。自动检查只验证文件结构，不证明复盘质量。

## 它解决什么问题

面试后整理了很多笔记，下一次仍在相同的追问上卡住；简历不断更换项目，旧笔记混在一起，答案也逐渐不一致。

这个 skill 将复盘连接到长期积累：

```text
逐字稿 + 当前宝典 + 已确认的项目事实
                   ↓
还原问题与追问 → 找到具体卡点 → 改写可口述 QA
                   ↓
对应项目 MASTER / 公共题库 / 下一轮针对性练习
```

MASTER 指长期维护的面试问答笔记。每个重点项目各有一份，通用原理放公共题库；项目退出简历后保留历史，新项目独立积累。

## 核心设计

- **保留真实追问链**：记录当时问了什么、实际怎么答、缺在哪里，而不只摘题目。
- **答案可以开口讲**：主答直接回应，细节放折叠追问；待核实或未落地内容以短标记和备注承接。
- **项目事实有边界**：设计、实现、接入、效果验证分别记录，优化表达不制造经历或指标。
- **增量维护**：优先补已有题，保留稳定题号、来源和链接；重复输入不重复建题。
- **适应项目更替**：项目按“当前展示、候选、历史”管理，复习范围随简历与岗位调整。

## 从哪里开始

先阅读 [skill 指令](skills/interview-review/SKILL.md) 和 [虚构示例](examples/walkthrough.md)，判断是否符合自己的复盘方式。**克隆仓库不会安装或启用 skill。**

手动试用时，将 `skills/interview-review/` 整个目录提供给支持读取本地文件的助手，并明确要求先读取其中的 `SKILL.md`。这只是一种人工加载方式，不保证所有产品自动识别。

示例请求：

```text
请先读取 skills/interview-review/SKILL.md，再复盘我提供的逐字稿。
保留主问题和连续追问，关联实际回答及时间戳。
先诊断并整理候选 QA，本轮不要修改 MASTER。
```

已经具备安装后的 skill 调用能力时，也可以用 `$interview-review` 指定工作流。具体安装位置与调用方式以使用环境的文档为准。

准备材料：逐字稿是主要输入；已有 MASTER、项目更正记录和岗位描述可按需补充。缺少材料时应说明局限，不补造事实。完整规则见 [MASTER 维护方法](skills/interview-review/references/maintenance.md)。

## 输入与输出

| 输入 | 输出 |
|---|---|
| 面试逐字稿 | 主问题及追问索引、实际回答映射 |
| 项目材料和事实确认 | 有依据的诊断、可口述主答与追问 |
| 当前 MASTER | 定点归并提案，或在已授权范围内执行更新 |
| 岗位要求与准备时间（可选） | 少量优先练习及复习入口 |

本仓库仅保存通用工作流与虚构材料。真实逐字稿、音频、简历、个人 MASTER、公司内部代码及凭证应保存在自己的私有工作目录。

## 仓库结构

```text
skills/interview-review/   可复用 skill 包
examples/walkthrough.md   虚构输入与人工编写的预期示意
docs/evaluation.md        行为验证场景和结果记录
scripts/validate.py       文件结构及本地文档链接检查
.github/workflows/        自动结构检查
```

## 验证与开发

需要 Python 3.10 或以上版本。以下命令只安装检查工具依赖，不安装 skill：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

结构检查覆盖 YAML 元信息、skill 引用、相对文档链接和示例文件。行为质量需要另按 [验证清单](docs/evaluation.md) 执行，人工示例不算模型实测。

## 当前限制与下一步

- 模型、上下文和材料完整度会影响结果；尚无定量质量结论。
- 目前不提供录音转写、图形界面、自动同步或独立运行的应用。
- 下一步先完成真实逐字稿验证，检查追问覆盖、事实边界与归并准确性，再据结果改进。
- 多项目迁移与重复输入场景仍需验证，不承诺所有笔记格式即插即用。

欢迎通过 Issue 提交**脱敏或虚构的最小案例**，说明具体失败与期望行为。参与方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可与参考

本项目采用 [MIT 许可证](LICENSE)。许可证允许复用，不授予原仓库写入权限。

编写过程使用 AI 辅助，工作流围绕实际面试复盘需求设计；目前未以真实面试结果验证成效。

方法参考：[OpenAI Skills 文档](https://learn.chatgpt.com/docs/build-skills)、[interview-coach](https://github.com/qijin-3/qi_Skills/blob/main/skills/career/interview-coach/SKILL.md)、[InterviewForge](https://github.com/K1XE/InterviewForge/blob/main/skill/interviewforge/SKILL.md)。后两者用于比较复盘思路，本仓库不包含它们的脚本、模板或素材。
