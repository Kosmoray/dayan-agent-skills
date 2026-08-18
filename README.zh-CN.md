<p align="center"><img src="assets/dayan-mark.svg" width="104" alt="大衍"></p>

<h1 align="center">大衍 AGENT SKILLS</h1>

<p align="center"><strong>问题选对。点一下，装上解决办法。</strong></p>

<p align="center">一个包含 56 个 AI Agent Skill 的公开母包：把模糊需求变成可验收任务、把演示讲清楚、把发版风险挑出来、先读懂代码库，或先给 Agent 划清边界。</p>

<p align="center">
  <a href="https://kosmoray.github.io/dayan-agent-skills/"><strong>按问题选 Skill</strong></a>
  ·
  <a href="docs/quickstart.md"><strong>60 秒安装</strong></a>
  ·
  <a href="docs/demos/control-library.html">看一屏证明</a>
  ·
  <a href="README.md">English</a>
  ·
  <a href="https://github.com/Kosmoray/dayan-agent-skills"><strong>★ 解决过一次麻烦就点个 Star</strong></a>
</p>

<p align="center"><a href="https://kosmoray.github.io/dayan-agent-skills/"><img src="assets/hero.svg" alt="按常见 AI Agent 问题选择对应的大衍 Skill"></a></p>

## 你要解决什么问题？点这个。

| 你要做的事 | 点这个 Skill | 你会拿到 |
| --- | --- | --- |
| 把一句模糊需求变成可验收任务 | [`dayan-wenzhen`](skills/dayan-wenzhen/SKILL.md) | 带权限、证据和停止信号的可证伪任务契约 |
| 把 AI 做的演示讲明白 | [`dayan-deck`](skills/dayan-deck/SKILL.md) | 每页一个叙事任务，加上结构验证器 |
| 在发布前揪出真正的风险 | [`dayan-adversarial-reviewer`](skills/dayan-adversarial-reviewer/SKILL.md) | 有证据的 `BLOCK`、`CONCERNS` 或 `CLEAN` 裁决 |
| 改代码前先读懂陌生仓库 | [`dayan-orient`](skills/dayan-orient/SKILL.md) | 仓库地图和安全的第一步改动路线 |
| 让 Agent 知道能做什么、该拒绝什么 | [`dayan-agent-designer`](skills/dayan-agent-designer/SKILL.md) | 带评测入口的 Agent 边界规格 |

在线[问题选择器](https://kosmoray.github.io/dayan-agent-skills/)会给每条路线配一条可复制安装命令和一个可视化证明。所有能力继续放在同一个母包：克隆一次，按需安装，56 个 Public Beta Skill 共用一条贡献与发布历史。

### 跑一条路线

先克隆一次，再把你需要的单个 Skill 安装进临时 home：

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

把 `dayan-wenzhen` 换成上表对应的 Skill 即可。[快速开始](docs/quickstart.md) · [浏览全部 56 个 Skill](docs/skills.md) · [兼容性证据](docs/compatibility.md) · [检查究竟证明什么](docs/control-layer-vs-prompt-collection.md) · [分享包](docs/share-kit.md)

## 可复制样例与产物 fixture

仓库现在有 [11 个脱敏可复制样例](examples/runs/README.md)，包括：

- [Wenzhen 模糊需求](examples/runs/wenzhen-fuzzy-request.md)：把一句泛泛的 AI 改造需求收成可证伪任务契约。
- [Deck 提纲成稿](examples/runs/deck-from-outline.md)：把一个实用提纲收成可验证演示请求。
- [对抗审查裁决](examples/runs/adversarial-review-verdict.md)：把发版描述收成具体的 BLOCK / CONCERNS / CLEAN 审查。
- [API 分页契约审查](examples/runs/api-review-pagination-contract.md)：在客户端依赖前阻断无上限接口。
- [开源文档 AI 可见性](examples/runs/ai-seo-open-source-docs.md)：让 AI 助手更准确引用仓库声明。

同时新增 [12 个产物 fixture](docs/fixtures/README.md)，展示仓库地图、Agent 设计、守门 Hook、API 审查、AI 可见性审计、视觉演示 brief、架构决策、Agent 包、响应式 UI 验收、verifier 规划、假阳性审查和权限账本的可复制输出形态。

再用公开 [Playbook](docs/playbooks/README.md) 判断你的重复工作应该做成清单、Skill、验证器、Hook 还是 Agent。想做小贡献时，从 [Good first issues](docs/good-first-issues.md) 开始。

如果想看 Skill 背后的方法论和工具层，读 [核心知识地图](docs/core-knowledge.md) 与 [公开工具目录](docs/tooling.md)。

## 按任务选能力

| 创作 Create | 思考 Think | 构建 Build | 验证与增长 Verify & Grow |
| --- | --- | --- | --- |
| [Deck](skills/dayan-deck/SKILL.md) | [Wenzhen](skills/dayan-wenzhen/SKILL.md) | [Agent Designer](skills/dayan-agent-designer/SKILL.md) | [Adversarial Reviewer](skills/dayan-adversarial-reviewer/SKILL.md) |
| [Huashu Design](skills/dayan-huashu-design/SKILL.md) | [Plan](skills/dayan-plan/SKILL.md) | [Agent Factory](skills/dayan-agent-factory/SKILL.md) | [AI SEO](skills/dayan-ai-seo/SKILL.md) |
| [HTML](skills/dayan-html/SKILL.md) | [Orient](skills/dayan-orient/SKILL.md) | [Hook Factory](skills/dayan-hook-factory/SKILL.md) |  |
| [Diagram](skills/dayan-diagram/SKILL.md) |  |  |  |

56 个 Skill 均在同一个母包内提供 Public Beta 安装。旗舰 Skill 有独立验证器，Core Library 通过统一公开包合同、安装矩阵和离线生命周期 smoke 验证，并在 catalog 中明确真实宿主版本证据边界。

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

验证一屏定位 Demo：

```bash
python3 scripts/verify_control_demo.py
```

验证公开分享包：

```bash
python3 scripts/verify_share_kit.py
```

## 开源原则

- 结果先于仪式；
- 证据先于完成声明；
- 通用 AI 控制与验证机制默认公开；
- 花钱、凭证、发布、高风险判断仍保留人工权力；
- 失败样例和停止条件也是产品的一部分。

如果它帮你少重造了一次 AI 护栏，欢迎给仓库一个 Star。

## License

[MIT](LICENSE)。
