---
id: z91772524-ai-pojia-next
name: z91772524-ai/pojia-next
kind: catalog
category: A
summary: 一个脚本搞定 DSH / WorkBuddy / ZCode / Codex / Cursor / Claude 六客户端的提示词与人格替换：零依赖、双击即用、可自证、改前备份、一键还原。另附【免装 Python 的单文件 exe】；DSH 自动区分官方桌面版 / 社区桌面版。附 bandit/semgrep 扫描与 SHA256 校验。
targets: [codex, claude, deepseek, glm]
clients: [all]
archetype: catalog
strength: null
status: unverified
language: multi
usage:
  type: doc
  install: null
  uninstall: null
source:
  repo: z91772524-ai/pojia-next
  path: null
  commit: null
  license: MIT License
  url: "https://github.com/z91772524-ai/pojia-next"
tags: [catalog]
added: 2026-10-26
updated: 2026-10-26
---

# z91772524-ai/pojia-next

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [z91772524-ai/pojia-next](https://github.com/z91772524-ai/pojia-next) |
| ★ | 791 |
| 语言 | Python |
| 最近 push | 2026-10-25 |
| 分类 | A |
| 许可 | MIT License |
| 推断适用模型 | codex, claude, deepseek, glm |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `z91772524-ai-pojia-next.md` 并在 front matter 里写 `source.repo: z91772524-ai/pojia-next`。

## 原始简介

一个脚本搞定 DSH / WorkBuddy / ZCode / Codex / Cursor / Claude 六客户端的提示词与人格替换：零依赖、双击即用、可自证、改前备份、一键还原。另附【免装 Python 的单文件 exe】；DSH 自动区分官方桌面版 / 社区桌面版。附 bandit/semgrep 扫描与 SHA256 校验。
