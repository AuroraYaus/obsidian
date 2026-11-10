#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@file    audit_concept_terms.py
@brief   概念笔记术语义务与书面化审计（前置概念 / 记号约定 / 生活比喻）
@date    2026-11-10

@details
按 `docs/audits/lessons/lesson-concept-note-no-metaphor.md` 与
`.claude/rules/documentation.md` 三、概念笔记规范的「术语解释三重义务」做静态检查：

  HARD  生活比喻残留（蛋糕/盘子/好比/像一/相当于/考场/排座/货物/标尺 等）→ FAIL
  HARD  frontmatter `type` 非 definition → FAIL
  WARN  缺 `## 前置概念` → 记为待补
  WARN  缺 `## 符号与记号约定` → 记为待补（2026-11-10 加严：须在首次数学使用之前）
  WARN  `## 直观模型` 为空 → FAIL（该节是模板必检项，空内容等于缺失）

设计口径：比喻与 type 是硬失败（回归检查用），前置概念与记号约定是建议项——
存量 118 篇尚未回填，用 WARN 计数量化工作量，不阻断提交。

@usage
    python3 tools/audit_concept_terms.py                    # 全库 docs/concepts
    python3 tools/audit_concept_terms.py <file-or-dir> ...  # 指定路径
    python3 tools/audit_concept_terms.py --strict docs/concepts   # WARN 也计为失败
    python3 tools/audit_concept_terms.py --list-warn docs/concepts # 逐条列出待补文件

@args
    paths          可选；文件或目录，缺省为 docs/concepts
    --strict       把 WARN 提升为 FAIL
    --list-warn    打印每个待补项的文件名

@env
    无（纯静态文本检查，不依赖网络与第三方库）

@exit_code
    0  通过（或仅有 WARN 且未开 --strict）
    1  存在 FAIL（或 --strict 下存在 WARN）
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = PROJECT_ROOT / "docs" / "concepts"

# 生活比喻检测词表：来自 2026-11-10 用户纠错的实际样本与同类措辞
METAPHOR_PATTERNS = (
    "好比", "像一", "打个比方", "想象一", "犹如",
    "蛋糕", "盘子", "撤盘", "分账", "跑道", "考场", "排座", "考生", "监考",
    "货物", "标尺", "井水不犯河水", "黑暗隧道", "水管",
    # 2026-11-10 第二轮：全文书面化扫描补入的实际样本
    "商场", "电梯", "车站", "站台", "公告屏", "服务台", "车厢", "运货",
    "公路", "车队", "救护车", "车道", "绿灯", "告示牌", "列车",
    "索引卡", "工作单(?!元)", "自由职业", "凭什么", "门禁", "快车道",
)

REQUIRED_SECTIONS = ("## 解释目标与范围", "## 科学定义", "## 直观模型", "## 常见误解", "## 协议锚点", "## 图谱关联")


def _hit(pattern: str, text: str) -> bool:
    """@brief 判断某个比喻模式是否命中（含正则模式）
    @param pattern 词或正则
    @param text 被检查文本
    @return 是否命中
    """
    if "(" in pattern or "[" in pattern:
        return re.search(pattern, text) is not None
    return pattern in text


def split_frontmatter(text: str) -> tuple[str, str]:
    """@brief 拆出 frontmatter 与正文
    @param text  文件全文
    @return (frontmatter, body)；无 frontmatter 时前者为空串
    """
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[3:end], text[end + 4:]


def check_file(path: Path) -> dict:
    """@brief 检查单个概念笔记
    @param path  笔记路径
    @return 含 fail/warn 两个列表的字典
    """
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    fails: list[str] = []
    warns: list[str] = []

    m = re.search(r"^type:\s*(\S+)\s*$", fm, re.MULTILINE)
    if not m or m.group(1) != "definition":
        fails.append(f"frontmatter type 非 definition（实际 {m.group(1) if m else '缺失'}）")

    for sec in REQUIRED_SECTIONS:
        if sec not in body:
            fails.append(f"缺模板章节 {sec}")

    # 直观模型不得为空
    mm = re.search(r"## 直观模型\s*\n+(.*?)(?:\n## |\Z)", body, re.DOTALL)
    if mm and not mm.group(1).strip():
        fails.append("## 直观模型 内容为空")

    hits = [w for w in METAPHOR_PATTERNS if _hit(w, body)]
    if hits:
        fails.append("生活比喻残留： " + "、".join(hits))

    if "## 前置概念" not in body:
        warns.append("缺 ## 前置概念")
    if not re.search(r"^#{2}\s*符号(与记号约定|约定)\s*$", body, re.MULTILINE):
        warns.append("缺 ## 符号与记号约定")

    return {"fails": fails, "warns": warns}


def iter_notes(paths: list[str]) -> list[Path]:
    """@brief 展开待检查文件
    @param paths  CLI 传入的路径列表
    @return 概念笔记路径列表（按名排序）
    """
    if not paths:
        paths = [str(DEFAULT_ROOT)]
    out: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        if p.is_dir():
            out.extend(sorted(p.glob("*.md")))
        elif p.is_file():
            out.append(p)
        else:
            print(f"SKIP 路径不存在: {raw}", file=sys.stderr)
    # 入口类文件不是概念笔记，跳过
    # 清单类与索引类文件不是概念笔记，不适用六段式模板，排除
    return [p for p in out if p.name not in {"概念图谱入口.md", "README.md", "3GPP全流程_缩写概念理论清单.md"}]


def main() -> int:
    """@brief 命令入口
    @return 进程退出码
    """
    ap = argparse.ArgumentParser(description="概念笔记术语义务与书面化审计")
    ap.add_argument("paths", nargs="*", help="文件或目录，缺省 docs/concepts")
    ap.add_argument("--strict", action="store_true", help="把 WARN 提升为 FAIL")
    ap.add_argument("--list-warn", action="store_true", help="逐条列出待补文件")
    args = ap.parse_args()

    notes = iter_notes(args.paths)
    if not notes:
        print("NO_INPUT")
        return 1

    fail_files = 0
    warn_files = 0
    warn_kinds = {"缺 ## 前置概念": 0, "缺 ## 符号与记号约定": 0}

    for p in notes:
        res = check_file(p)
        rel = p.relative_to(PROJECT_ROOT) if PROJECT_ROOT in p.parents else p
        if res["fails"]:
            fail_files += 1
            print(f"FAIL {rel}")
            for f in res["fails"]:
                print(f"     - {f}")
        if res["warns"]:
            warn_files += 1
            for w in res["warns"]:
                warn_kinds[w] = warn_kinds.get(w, 0) + 1
            if args.list_warn:
                print(f"WARN {rel}: " + "；".join(res["warns"]))

    total = len(notes)
    print("---")
    print(f"检查 {total} 篇：FAIL {fail_files} 篇，WARN {warn_files} 篇")
    for k, v in warn_kinds.items():
        print(f"  {k}: {v} 篇")

    if fail_files or (args.strict and warn_files):
        print("CONCEPT_TERMS_AUDIT_FAIL")
        return 1
    print("CONCEPT_TERMS_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
