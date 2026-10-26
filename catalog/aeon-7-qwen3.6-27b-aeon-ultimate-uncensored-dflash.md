---
id: aeon-7-qwen3.6-27b-aeon-ultimate-uncensored-dflash
name: AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash
kind: catalog
category: E
summary: "Fully uncensored, capability-enhanced abliteration of Qwen3.6-27B. NVFP4 + z-lab DFlash speculative decoding (n=12) on the unified ghcr.io/aeon-7/aeon-vllm-ultimate:latest container, tuned for long-context draft acceptance on DGX Spark. 6 HF variants (BF16/NVFP4/MTP/MTP-XS), docker-compose, and Quic"
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
  repo: AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash
  path: null
  commit: null
  license: Apache License 2.0
  url: "https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash"
tags: [catalog, abliteration]
added: 2026-10-26
updated: 2026-10-26
---

# AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash

> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。
> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。

| 字段 | 值 |
|---|---|
| 仓库 | [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash) |
| ★ | 485 |
| 语言 | Python |
| 最近 push | 2026-10-06 |
| 分类 | E |
| 许可 | Apache License 2.0 |
| 推断适用模型 | llama |

## 怎么用

这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：

1. 快速判断这个上游项目值不值得点进去看；
2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，
   在 `prompts/` 下新建 `aeon-7-qwen3.6-27b-aeon-ultimate-uncensored-dflash.md` 并在 front matter 里写 `source.repo: AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash`。

## 原始简介

Fully uncensored, capability-enhanced abliteration of Qwen3.6-27B. NVFP4 + z-lab DFlash speculative decoding (n=12) on the unified ghcr.io/aeon-7/aeon-vllm-ultimate:latest container, tuned for long-context draft acceptance on DGX Spark. 6 HF variants (BF16/NVFP4/MTP/MTP-XS), docker-compose, and QuickStart.
