---
id: zju-llm-safety-darwin
name: ZJU-LLM-Safety/DARWIN
kind: catalog
category: C
summary: DARWIN is a self-evolving LLM jailbreak framework that grows a reusable strategy pool through external extraction, sandbox filtering, history-memory retrieval, Markov-based strategy selection, and reflective/genetic evolution.
targets: [all]
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
  repo: ZJU-LLM-Safety/DARWIN
  path: null
  commit: null
  license: null
  url: "https://github.com/ZJU-LLM-Safety/DARWIN"
tags: [catalog]
added: 2026-10-26
updated: 2026-10-26
---

# ZJU-LLM-Safety/DARWIN

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [ZJU-LLM-Safety/DARWIN](https://github.com/ZJU-LLM-Safety/DARWIN) |
| ★ | 82 |
| 语言 | Python |
| 最近 push | 2026-09-28 |
| 分类 | C |
| 许可 | 未声明（不落正文） |
| 推断适用模型 | all |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `zju-llm-safety-darwin.md` 并在 front matter 里写 `source.repo: ZJU-LLM-Safety/DARWIN`。

## 原始简介

DARWIN is a self-evolving LLM jailbreak framework that grows a reusable strategy pool through external extraction, sandbox filtering, history-memory retrieval, Markov-based strategy selection, and reflective/genetic evolution.
