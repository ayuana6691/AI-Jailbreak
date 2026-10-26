#!/usr/bin/env python3
"""把 sources/sources.json 里的上游仓库批量转成 catalog 卡。

设计约束（为什么这样写）：
  1. **不复制上游正文**。catalog 卡只登记链接、元数据、许可证，正文是一段
     由本仓库生成的说明。这样既避开许可证争议，也让卡片可以批量生成。
  2. **幂等**。同样的 sources 跑两遍必须产出完全相同的文件，否则
     `build_index.py --check` 和 CI 会一直报脏。
  3. **可与人工卡共存**。人工写的 prompt 卡不会被覆盖：生成器只在
     `kind: catalog` 的卡上动手，遇到同名 id 直接跳过并报告。

用法：
    python scripts/gen_catalog.py                # 生成/更新
    python scripts/gen_catalog.py --dry-run      # 只看会生成什么
    python scripts/gen_catalog.py --limit 50     # 只取前 50 个
    python scripts/gen_catalog.py --prune        # 删除已不在 sources 里的 catalog 卡
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import cards as cards_lib, models as models_lib, sources as src_lib  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "catalog"

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

# 只收录这些分类：A/B 中文破甲生态、C 英文越狱工具、E 去审查模型。
# D（提示词注入研究）、F（红队基准/防御）、G（弱相关）默认不收——
# 它们多是论文与工具清单，不是"拿来就能用的破甲"。
DEFAULT_CATS = ("A", "B", "C", "E")

SLUG_BAD = re.compile(r"[^a-z0-9._-]+")

# 噪声过滤：这些词命中的是「AI 应用/媒体生成/通用工具」，不是破甲资源。
NOISE = re.compile(
    r"\b(video|image generat|photo|music|voice|tts|chatbot ui|webui|studio|"
    r"platform|marketplace|api gateway|proxy pool|one-api|new-api)\b",
    re.IGNORECASE,
)

# 必须至少命中一个「确实是破甲/越狱」的信号，才允许进 catalog。
SIGNAL = re.compile(
    r"破甲|破限|越狱|pojia|jailbreak|abliterat|uncensor|de-?censor|"
    r"refusal (removal|steering)|prompt injection|system prompt|"
    r"red.?team|adversarial prompt|uncensored (model|llm|chat)",
    re.IGNORECASE,
)


def is_relevant(repo: dict) -> bool:
    """双闸门：必须有破甲信号，且不是明显的应用/工具噪声。"""
    text = f"{repo.get('full_name', '')} {repo.get('description', '')}"
    if not SIGNAL.search(text):
        return False
    if NOISE.search(text) and not re.search(r"jailbreak|破甲|破限|越狱|abliterat|uncensor", text, re.I):
        return False
    return True


def make_id(full_name: str) -> str:
    """owner/name -> owner--name，转小写，非法字符归一为 '-'。"""
    slug = full_name.replace("/", "--").lower()
    slug = SLUG_BAD.sub("-", slug).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:64]


def targets_for(repo: dict) -> list[str]:
    """从仓库名/简介里推断适用模型。推不出来就落 all。"""
    text = f"{repo.get('full_name', '')} {repo.get('description', '')}".lower()
    hits: list[str] = []
    for fam in models_lib.FAMILIES:
        if fam["key"] == "universal":
            continue
        for pat in fam["repo_patterns"]:
            if re.search(pat, text, re.IGNORECASE):
                # 用家族里最短的 card_target 作为代表 id
                rep = sorted(fam["card_targets"], key=len)[0]
                if rep not in hits:
                    hits.append(rep)
                break
    return hits or ["all"]


def archetype_for(repo: dict, cat: str) -> str:
    text = f"{repo.get('full_name', '')} {repo.get('description', '')}".lower()
    if cat == "E" or re.search(r"abliterat|uncensor|refusal", text):
        return "abliteration"
    if re.search(r"hook|plugin|patch|installer|inject", text):
        return "client-patch"
    if re.search(r"benchmark|evaluat|red.?team", text):
        return "methodology"
    return "catalog"


def render_card(repo: dict, card_id: str, today: str) -> str:
    name = repo.get("full_name", "")
    desc = (repo.get("description") or "").strip() or "（上游未提供简介）"
    stars = int(repo.get("stars") or 0)
    lang = repo.get("language") or "—"
    pushed = (repo.get("pushed_at") or "")[:10] or "—"
    lic = repo.get("license")
    targets = targets_for(repo)
    archetype = archetype_for(repo, repo.get("category", "Z"))

    lines = [
        "---",
        f"id: {card_id}",
        f"name: {_q(name)}",
        "kind: catalog",
        f"category: {repo.get('category', 'Z')}",
        f"summary: {_q(desc[:300])}",
        "targets: [" + ", ".join(targets) + "]",
        "clients: [all]",
        f"archetype: {archetype}",
        "strength: null",
        "status: unverified",
        "language: multi",
        "usage:",
        "  type: doc",
        "  install: null",
        "  uninstall: null",
        "source:",
        f"  repo: {_q(name)}",
        "  path: null",
        "  commit: null",
        f"  license: {_q(lic) if lic else 'null'}",
        f"  url: {_q(repo.get('url') or 'https://github.com/' + name)}",
        "tags: [" + ", ".join(["catalog"] + ([archetype] if archetype != "catalog" else [])) + "]",
        f"added: {today}",
        f"updated: {today}",
        "---",
        "",
        f"# {name}",
        "",
        "> 本卡由 `scripts/gen_catalog.py` 自动生成，只登记元数据与链接，**不包含上游正文**。",
        "> 需要正文请到上游仓库获取；上游许可为 null 时尤其如此。",
        "",
        "| 字段 | 值 |",
        "|---|---|",
        f"| 仓库 | [{name}]({repo.get('url') or 'https://github.com/' + name}) |",
        f"| ★ | {stars:,} |",
        f"| 语言 | {lang} |",
        f"| 最近 push | {pushed} |",
        f"| 分类 | {repo.get('category', 'Z')} |",
        f"| 许可 | {lic or '未声明（不落正文）'} |",
        f"| 推断适用模型 | {', '.join(targets)} |",
        "",
        "## 怎么用",
        "",
        "这张卡不能直接 `pojia apply`——它没有可注入正文。用它做两件事：",
        "",
        "1. 快速判断这个上游项目值不值得点进去看；",
        "2. 如果你审过正文并认为可靠，可以把它提升成 `kind: prompt` 卡片，",
        f"   在 `prompts/` 下新建 `{card_id}.md` 并在 front matter 里写 `source.repo: {name}`。",
        "",
        "## 原始简介",
        "",
        desc,
        "",
    ]
    return "\n".join(lines)


def _q(value: str) -> str:
    """YAML 值转义：含特殊字符时加双引号。"""
    s = str(value)
    if s == "" or s != s.strip() or any(c in s for c in ":#[]{}'\"") or s.lower() in ("null", "true", "false", "yes", "no"):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def main() -> int:
    ap = argparse.ArgumentParser(description="从 sources 生成 catalog 卡")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="只处理 star 最高的前 N 个")
    ap.add_argument("--min-stars", type=int, default=0, help="star 低于此值的不生成")
    ap.add_argument("--cats", default=",".join(DEFAULT_CATS), help="只收录这些分类，逗号分隔")
    ap.add_argument("--prune", action="store_true", help="删除已不在 sources 中的 catalog 卡")
    args = ap.parse_args()

    cats = {c.strip().upper() for c in args.cats.split(",") if c.strip()}
    data = src_lib.load(ROOT)
    repos = data.get("repos", [])
    if not repos:
        print("sources 为空，先跑 python scripts/scan.py", file=sys.stderr)
        return 2

    # 人工卡（非 catalog）的 id，必须让路
    existing = cards_lib.load_cards(ROOT)
    manual_ids = {c.id for c in existing if c.kind != "catalog"}

    today = dt.date.today().isoformat()
    candidates = [
        r for r in repos
        if r.get("category") in cats
        and int(r.get("stars") or 0) >= args.min_stars
        and not r.get("archived")
        and not r.get("fork")
        and is_relevant(r)
    ]
    candidates.sort(key=lambda r: (-int(r.get("stars") or 0), r.get("full_name", "")))
    if args.limit:
        candidates = candidates[: args.limit]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = skipped_manual = unchanged = 0
    produced: set[str] = set()

    for repo in candidates:
        card_id = make_id(repo.get("full_name", ""))
        if not card_id:
            continue
        if card_id in manual_ids:
            skipped_manual += 1
            continue
        produced.add(card_id)
        path = OUT_DIR / f"{card_id}.md"
        content = render_card(repo, card_id, today)
        old = path.read_text(encoding="utf-8") if path.exists() else None
        # 只比较去掉 updated 行的内容，避免每天无意义 diff
        if old is not None and _stable(old) == _stable(content):
            unchanged += 1
            continue
        if not args.dry_run:
            path.write_text(content, encoding="utf-8", newline="\n")
        written += 1

    pruned = 0
    if args.prune and not args.dry_run:
        for path in OUT_DIR.glob("*.md"):
            if path.stem not in produced:
                path.unlink()
                pruned += 1

    print(f"候选 {len(candidates)} 个（分类 {','.join(sorted(cats))}）")
    print(f"写入 {written}  未变 {unchanged}  因人工卡让路 {skipped_manual}  清理 {pruned}")
    if args.dry_run:
        print("--dry-run：未写盘")
    return 0


def _stable(text: str) -> str:
    """去掉 updated 行后比较，保证日常重跑不产生 diff。"""
    return "\n".join(l for l in text.splitlines() if not l.startswith("updated:"))


if __name__ == "__main__":
    raise SystemExit(main())
