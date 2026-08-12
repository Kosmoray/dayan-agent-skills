<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/dayan-mark-on-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/dayan-mark.svg">
    <img src="assets/dayan-mark.svg" width="104" alt="大衍">
  </picture>
</p>

<h1 align="center">大衍 AGENT SKILLS</h1>

<p align="center"><strong>给概率性 AI 装上一层可控机制。</strong></p>

<p align="center">
  <a href="docs/quickstart.md"><strong>60 秒开始试用</strong></a>
  ·
  <a href="https://kosmoray.github.io/dayan-agent-skills/">在线演示</a>
  ·
  <a href="README.md">English</a>
  ·
  <a href="https://github.com/Kosmoray/dayan-agent-skills"><strong>★ 收藏这套控制层</strong></a>
</p>

## 为什么做

AI 刚兴起时，像一台纯手动胶片相机：能力很强，但光圈、快门、对焦都要使用者自己控制。

Skill、harness、hook 和 verifier，就是 AI 的半自动模式：

- Skill 选择工作流；
- harness 保持过程稳定；
- hook 拦截可预见的错误；
- verifier 检查结果是否配得上它的完成声明。

这些机制迟早会成为行业公共能力。与其藏着等待别人重新发明，不如率先命名、实现、验证并公开。

## 56 个 Skill，一个能力母舰

公开库现已覆盖工程质量、研究决策、Agent 系统、内容设计与产品架构；所有 Star、Issue、贡献者和发布历史继续集中在一个仓库。

[60 秒开始试用](docs/quickstart.md) · [按任务选择 Skill](docs/choose-a-skill.md) · [阅读 Playbook](docs/playbooks/README.md) · [浏览 56 个 Skill](docs/skills.md) · [查看机器可读证据](catalog.json)

## 先从这里开始

不要先翻 56 个目录。先按你要阻止的问题选入口：

| 你的问题 | 先用 | 作用 |
| --- | --- | --- |
| 任务模糊或风险高 | [`dayan-wenzhen`](skills/dayan-wenzhen/SKILL.md) | 先生成可证伪任务契约，避免 AI 把错问题写得很漂亮 |
| 演示或报告讲不清 | [`dayan-deck`](skills/dayan-deck/SKILL.md) | 每页一个任务，并验证演示结构 |
| 发版前审查太软 | [`dayan-adversarial-reviewer`](skills/dayan-adversarial-reviewer/SKILL.md) | 分开检查失败模式、维护陷阱和信任边界 |
| 代码库不熟 | [`dayan-orient`](skills/dayan-orient/SKILL.md) | 先建立仓库地图，再开始改动 |
| Agent 职责不清 | [`dayan-agent-designer`](skills/dayan-agent-designer/SKILL.md) | 定义职责、工具、记忆、边界和评估 |

最快的安全试用方式是安装到临时 home：

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills
DAYAN_TEST_HOME="$(mktemp -d)"

python3 installers/install.py dayan-wenzhen \
  --agent codex \
  --home "$DAYAN_TEST_HOME"

python3 skills/dayan-wenzhen/scripts/verify_contract.py \
  skills/dayan-wenzhen/examples/starter-contract.json
```

## 可复制样例

- [Wenzhen 模糊需求](examples/runs/wenzhen-fuzzy-request.md)：把一句泛泛的 AI 改造需求收成可证伪任务契约。
- [Deck 提纲成稿](examples/runs/deck-from-outline.md)：把一个实用提纲收成可验证演示请求。
- [对抗审查裁决](examples/runs/adversarial-review-verdict.md)：把发版描述收成具体的 BLOCK / CONCERNS / CLEAN 审查。

再用公开 [Playbook](docs/playbooks/README.md) 判断你的重复工作应该做成清单、Skill、验证器、Hook 还是 Agent。

## 按任务选能力

| 创作 Create | 思考 Think | 构建 Build | 验证与增长 Verify & Grow |
| --- | --- | --- | --- |
| [Deck](skills/dayan-deck/SKILL.md) | [Wenzhen](skills/dayan-wenzhen/SKILL.md) | [Agent Designer](skills/dayan-agent-designer/SKILL.md) | [Adversarial Reviewer](skills/dayan-adversarial-reviewer/SKILL.md) |
| [Huashu Design](skills/dayan-huashu-design/SKILL.md) | [Plan](skills/dayan-plan/SKILL.md) | [Agent Factory](skills/dayan-agent-factory/SKILL.md) | [AI SEO](skills/dayan-ai-seo/SKILL.md) |
| [HTML](skills/dayan-html/SKILL.md) | [Orient](skills/dayan-orient/SKILL.md) | [Hook Factory](skills/dayan-hook-factory/SKILL.md) |  |
| [Diagram](skills/dayan-diagram/SKILL.md) |  |  |  |

56 个 Skill 均在同一个母包内提供 Public Beta 安装。旗舰 Skill 有独立验证器，Core Library 通过统一公开包合同验证，并在 catalog 中明确剩余运行时证据。

## 三个重点入口

### `dayan-deck` · Public Beta

把主题、提纲或资料变成一个自包含、文字可编辑的 HTML 演示：

- 每页只承担一个叙事任务；
- 统一视觉与动效语法；
- 支持键盘、打印、响应式与 reduced-motion；
- 附带确定性结构验证器；
- 明确区分结构通过、视觉质量、事实准确性和 PPTX 可编辑性。

[阅读 Skill](skills/dayan-deck/SKILL.md) · [打开在线 Starter](https://kosmoray.github.io/dayan-agent-skills/) · [查看验证器](skills/dayan-deck/scripts/verify_deck.py)

### `dayan-adversarial-reviewer` · Public Beta

在合并或发布前，用三种明确区分的视角审查一项具体变更：

- 失败模式：异常输入、重复执行、半完成、并发、中断与回滚；
- 维护者视角：隐式约定、职责混杂和回归陷阱；
- 信任边界：外部输入、权限、文件、环境变量、日志与凭证；
- 输出有证据的 `BLOCK`、`CONCERNS` 或 `CLEAN` 裁决；
- 同时交付人类可读 Markdown 与机器可验证 JSON；
- 附带通过/阻断样例和确定性验证器。

[阅读 Skill](skills/dayan-adversarial-reviewer/SKILL.md) · [查看审查量表](skills/dayan-adversarial-reviewer/references/rubric.md) · [查看验证器](skills/dayan-adversarial-reviewer/scripts/verify_review.py)

### `dayan-wenzhen` · Public Beta

在 AI 急着给方案前，把一个模糊、高影响或已被“解法”绑架的请求收成可检验的任务契约：

- 先分诊工作类型、风险、当前允许动作、放行权与最低证据；
- 只提出可被现实推翻的“当前最佳问题假设”；
- 只问会改变路线的问题；
- 同时保留替代路径、第三路径和缩小/推迟下注；
- 以最小可逆试验、暂停信号、检查点与继续证据收口；
- 同时产出人可读 Markdown 与机器可验证 JSON。

[阅读 Skill](skills/dayan-wenzhen/SKILL.md) · [查看契约结构](skills/dayan-wenzhen/references/contract-schema.md) · [查看验证器](skills/dayan-wenzhen/scripts/verify_contract.py)

## 一分钟安装

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills

python3 installers/install.py dayan-deck \
  --agent codex \
  --home "$HOME"
```

把 `dayan-deck` 替换为上表任一名称，即可安装对应 Public Beta Skill。

Claude Code：

```bash
python3 installers/install.py dayan-deck \
  --agent claude-code \
  --home "$HOME"
```

Beta 安装器只负责全新安装，遇到已有目录会停止，不会覆盖用户文件。

## 机器可读状态

[`catalog.json`](catalog.json) 逐项记录公开版本、示例、验证器、风险等级与尚未补齐的运行时证据，不把“已经打包”冒充“所有环境都已验证”。

## 开源原则

- 结果先于仪式；
- 证据先于完成声明；
- 通用 AI 控制与验证机制默认公开；
- 花钱、凭证、发布、高风险判断仍保留人工权力；
- 失败样例和停止条件也是产品的一部分。

如果它帮你少重造了一次 AI 护栏，欢迎给仓库一个 Star。

## License

[MIT](LICENSE)。
