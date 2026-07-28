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
  <a href="https://kosmoray.github.io/dayan-agent-skills/"><strong>打开 Dayan Deck 演示</strong></a>
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

## 当前可用

### `dayan-deck` · Public Beta

把主题、提纲或资料变成一个自包含、文字可编辑的 HTML 演示：

- 每页只承担一个叙事任务；
- 统一视觉与动效语法；
- 支持键盘、打印、响应式与 reduced-motion；
- 附带确定性结构验证器；
- 明确区分结构通过、视觉质量、事实准确性和 PPTX 可编辑性。

[阅读 Skill](skills/dayan-deck/SKILL.md) · [打开在线 Starter](https://kosmoray.github.io/dayan-agent-skills/) · [查看验证器](skills/dayan-deck/scripts/verify_deck.py)

## 一分钟安装

```bash
git clone https://github.com/Kosmoray/dayan-agent-skills.git
cd dayan-agent-skills

python3 installers/install.py dayan-deck \
  --agent codex \
  --home "$HOME"
```

Claude Code：

```bash
python3 installers/install.py dayan-deck \
  --agent claude-code \
  --home "$HOME"
```

Beta 安装器只负责全新安装，遇到已有目录会停止，不会覆盖用户文件。

## 接下来公开什么

首批 12 个候选分成四组：Create、Think、Build、Verify & Grow。目前只有 `dayan-deck` 已作为 beta 发布，其余名称是公开路线图，不代表已经达到生产可用状态。机器可读状态见 [`catalog.json`](catalog.json)。

## 开源原则

- 结果先于仪式；
- 证据先于完成声明；
- 通用 AI 控制与验证机制默认公开；
- 花钱、凭证、发布、高风险判断仍保留人工权力；
- 失败样例和停止条件也是产品的一部分。

如果它帮你少重造了一次 AI 护栏，欢迎给仓库一个 Star。

## License

[MIT](LICENSE)。
