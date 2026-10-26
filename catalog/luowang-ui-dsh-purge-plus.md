---
id: luowang-ui-dsh-purge-plus
name: luowang-ui/dsh-purge-plus
kind: catalog
category: C
summary: "Purge Community Plus - DeepSeek Harness jailbreak plugin, adapted for DSH Desktop 0.2.1-rc.x. Fixes #119 host crash and the toolFilter preset-registration failure."
targets: [deepseek]
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
  repo: luowang-ui/dsh-purge-plus
  path: null
  commit: null
  license: MIT License
  url: "https://github.com/luowang-ui/dsh-purge-plus"
tags: [catalog, client-patch]
added: 2026-10-26
updated: 2026-10-26
---

# luowang-ui/dsh-purge-plus

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [luowang-ui/dsh-purge-plus](https://github.com/luowang-ui/dsh-purge-plus) |
| ★ | 53 |
| 语言 | JavaScript |
| 最近 push | 2026-10-17 |
| 分类 | C |
| 许可 | MIT License |
| 推断适用模型 | deepseek |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `luowang-ui-dsh-purge-plus.md` 并在 front matter 里写 `source.repo: luowang-ui/dsh-purge-plus`。

## 原始简介

Purge Community Plus - DeepSeek Harness jailbreak plugin, adapted for DSH Desktop 0.2.1-rc.x. Fixes #119 host crash and the toolFilter preset-registration failure.
