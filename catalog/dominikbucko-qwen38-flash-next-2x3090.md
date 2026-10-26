---
id: dominikbucko-qwen38-flash-next-2x3090
name: DominikBucko/qwen38-flash-next-2x3090
kind: catalog
category: E
summary: "Qwen3.8-Flash-Next on 2× RTX 3090: with 128 GB RAM up to 4,191 tok/s prefill · 111.5 tok/s decode (131K prompt), full 256K window at 2,865 tok/s; with 64 GB RAM 3,410 tok/s prefill · 84 tok/s decode. New: opt-in uncensored mode (runtime abliteration, no new weights)."
targets: [llama]
clients: [all]
archetype: abliteration
strength: null
status: unverified
language: multi
usage:
  type: doc
  install: null
  uninstall: null
source:
  repo: DominikBucko/qwen38-flash-next-2x3090
  path: null
  commit: null
  license: Apache License 2.0
  url: "https://github.com/DominikBucko/qwen38-flash-next-2x3090"
tags: [catalog, abliteration]
added: 2026-10-26
updated: 2026-10-26
---

# DominikBucko/qwen38-flash-next-2x3090

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [DominikBucko/qwen38-flash-next-2x3090](https://github.com/DominikBucko/qwen38-flash-next-2x3090) |
| ★ | 126 |
| 语言 | Python |
| 最近 push | 2026-10-15 |
| 分类 | E |
| 许可 | Apache License 2.0 |
| 推断适用模型 | llama |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `dominikbucko-qwen38-flash-next-2x3090.md` 并在 front matter 里写 `source.repo: DominikBucko/qwen38-flash-next-2x3090`。

## 原始简介

Qwen3.8-Flash-Next on 2× RTX 3090: with 128 GB RAM up to 4,191 tok/s prefill · 111.5 tok/s decode (131K prompt), full 256K window at 2,865 tok/s; with 64 GB RAM 3,410 tok/s prefill · 84 tok/s decode. New: opt-in uncensored mode (runtime abliteration, no new weights).
