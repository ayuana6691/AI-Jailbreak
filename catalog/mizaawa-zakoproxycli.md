---
id: mizaawa-zakoproxycli
name: mizaawa/ZakoProxyCLI
kind: catalog
category: A
summary: 基于Rust编写的中转API破甲项目，支持Responses / Chat Completions / Anthropic Messages API，支持ChatGPT/Claude/Grok/Gemini/Deepseek/Glm/Kimi等大多数主流模型
targets: [claude, gemini, deepseek, glm, kimi, grok]
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
  repo: mizaawa/ZakoProxyCLI
  path: null
  commit: null
  license: MIT License
  url: "https://github.com/mizaawa/ZakoProxyCLI"
tags: [catalog]
added: 2026-10-26
updated: 2026-10-26
---

# mizaawa/ZakoProxyCLI

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [mizaawa/ZakoProxyCLI](https://github.com/mizaawa/ZakoProxyCLI) |
| ★ | 145 |
| 语言 | Rust |
| 最近 push | 2026-10-25 |
| 分类 | A |
| 许可 | MIT License |
| 推断适用模型 | claude, gemini, deepseek, glm, kimi, grok |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `mizaawa-zakoproxycli.md` 并在 front matter 里写 `source.repo: mizaawa/ZakoProxyCLI`。

## 原始简介

基于Rust编写的中转API破甲项目，支持Responses / Chat Completions / Anthropic Messages API，支持ChatGPT/Claude/Grok/Gemini/Deepseek/Glm/Kimi等大多数主流模型
