---
id: omgitsbase-llmash
name: omgitsbase/llmash
kind: catalog
category: E
summary: "Ollama-compatible LLM server on a tuned llama.cpp fork. Same commands, API and model store as Ollama, up to 4x Ollama's decode speed and 2.8x vLLM's in our benchmarks, from custom CUDA kernels, MTP speculation and its own 3-bit builds. Uncensors models in one command. Windows and Linux, NVIDIA."
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
  repo: omgitsbase/llmash
  path: null
  commit: null
  license: MIT License
  url: "https://github.com/omgitsbase/llmash"
tags: [catalog, abliteration]
added: 2026-10-26
updated: 2026-10-26
---

# omgitsbase/llmash

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [omgitsbase/llmash](https://github.com/omgitsbase/llmash) |
| ★ | 35 |
| 语言 | C++ |
| 最近 push | 2026-10-25 |
| 分类 | E |
| 许可 | MIT License |
| 推断适用模型 | llama |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `omgitsbase-llmash.md` 并在 front matter 里写 `source.repo: omgitsbase/llmash`。

## 原始简介

Ollama-compatible LLM server on a tuned llama.cpp fork. Same commands, API and model store as Ollama, up to 4x Ollama's decode speed and 2.8x vLLM's in our benchmarks, from custom CUDA kernels, MTP speculation and its own 3-bit builds. Uncensors models in one command. Windows and Linux, NVIDIA.
