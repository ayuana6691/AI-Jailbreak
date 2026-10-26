---
id: chen0416ccc-cpu-codex-windows-fast-patch-skill
name: chen0416ccc-cpu/codex-windows-fast-patch-skill
kind: catalog
category: A
summary: "此skills用于指导智能体在 Windows 上恢复 Codex Desktop 升级后失效的本地补丁和能力开关。（Computer Use，插件，破限，codex强制汉化，fast mode，手机远控，会话消失等问题）支持每次使用前自动将skills更新到最新版。/These skills are designed to guide the agent in restoring local patches and feature toggles that have been disabled or invalidated following a Codex Desktop upgrade "
targets: [codex]
clients: [all]
archetype: client-patch
strength: null
status: unverified
language: multi
usage:
  type: doc
  install: null
  uninstall: null
source:
  repo: chen0416ccc-cpu/codex-windows-fast-patch-skill
  path: null
  commit: null
  license: null
  url: "https://github.com/chen0416ccc-cpu/codex-windows-fast-patch-skill"
tags: [catalog, client-patch]
added: 2026-10-26
updated: 2026-10-26
---

# chen0416ccc-cpu/codex-windows-fast-patch-skill

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [chen0416ccc-cpu/codex-windows-fast-patch-skill](https://github.com/chen0416ccc-cpu/codex-windows-fast-patch-skill) |
| ★ | 1,305 |
| 语言 | PowerShell |
| 最近 push | 2026-10-24 |
| 分类 | A |
| 许可 | 未声明（不落正文） |
| 推断适用模型 | codex |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `chen0416ccc-cpu-codex-windows-fast-patch-skill.md` 并在 front matter 里写 `source.repo: chen0416ccc-cpu/codex-windows-fast-patch-skill`。

## 原始简介

此skills用于指导智能体在 Windows 上恢复 Codex Desktop 升级后失效的本地补丁和能力开关。（Computer Use，插件，破限，codex强制汉化，fast mode，手机远控，会话消失等问题）支持每次使用前自动将skills更新到最新版。/These skills are designed to guide the agent in restoring local patches and feature toggles that have been disabled or invalidated following a Codex Desktop upgrade on Windows. Supports auto-updating translations.
