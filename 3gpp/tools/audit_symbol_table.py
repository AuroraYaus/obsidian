#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@file    audit_symbol_table.py
@brief   概念笔记数学符号前置定义审计（每个符号必须在首次使用前解释）
@date    2026-11-10

@details
用户 2026-11-10 要求：单篇概念文档中每一个数学符号在使用前都必须有详细解释。
本工具把该要求变成可执行检查，口径如下：

  1. 从正文抽取全部数学片段（行内 $...$ 与独立 $$...$$）。
  2. 从片段中抽取「符号」：拉丁/希腊字母及其下标、上标（如 N_{RE}, E_r, Q_m, Z_c,
     k_0, C', TBS_{temp}, \\nu）。运算符（\\min、\\lfloor、\\sum、\\cdot、\\bmod 等）
     与纯数字不计入符号集，它们由「记号约定」文字说明承担。
  3. 找到 `## 符号与记号约定`（兼容旧名 `## 符号约定` / `### 记号约定`）小节，
     该小节必须出现在任何数学片段之前；小节内出现的符号视为已定义。
  4. 任何在首次出现之前未被该小节覆盖的符号 → FAIL，并给出首次出现的行号。

设计取舍：只做「是否在符号表里出现过」的静态判定，不判断解释质量——解释质量由
人工评审与 `## 前置概念` 的写法纪律承担。这样规则可自动化、不会因措辞变化误报。

@usage
    python3 tools/audit_symbol_table.py                      # 全库 docs/concepts
    python3 tools/audit_symbol_table.py <file-or-dir> ...
    python3 tools/audit_symbol_table.py --show-symbols docs/concepts/E_Value_G_Value_E值与G值.md

@args
    paths           可选；文件或目录，缺省 docs/concepts
    --show-symbols  打印每篇抽取到的符号集合（调试用）

@env
    无（纯静态文本检查）

@exit_code
    0  全部通过
    1  存在未在前置符号小节定义的符号，或缺该小节
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = PROJECT_ROOT / "docs" / "concepts"

# 运算符与结构性命令：不是符号，由「记号约定」的文字说明承担
OPERATOR_CMDS = {
    "min", "max", "lfloor", "rfloor", "lceil", "rceil", "sum", "prod", "int",
    "cdot", "times", "bmod", "mod", "log", "ln", "exp", "Pr", "frac", "le", "ge",
    "leq", "geq", "ne", "neq", "approx", "left", "right", "quad", "qquad", "text",
    "mathrm", "operatorname", "begin", "end", "matrix", "dots", "ldots", "cdots",
    "mid", "vert", "infty", "partial", "Delta", "in", "forall", "exists", "to",
}

# 符号小节标题（按优先级）
SECTION_RE = re.compile(r"^#{2,3}\s*(符号与记号约定|符号约定|记号约定)\s*$", re.MULTILINE)
MATH_RE = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.DOTALL)
# 符号 token：字母（或 \cmd）+ 可选上下标组；上下标允许单字符或 {...}
# base：LaTeX 命令，或多字母大写标识（TBS/NRE/DMRS，仅当后接上下标），或单字母
# 下标/上标允许一层嵌套花括号，使 \text{DMRS}、\mathcal{A} 这类写法整体成为一个记号，
# 避免被拆成 D/M/R/S、A 等单字母而误报「符号未定义」。
_GROUP = r"(?:[^{}]|\{[^{}]*\})*"
TOKEN_RE = re.compile(
    r"(\\[A-Za-z]+|[A-Za-z]{2,6}(?=[_^])|[A-Za-z])"
    r"(?:_(?:\{(" + _GROUP + r")\}|([A-Za-z0-9])))?"
    r"(?:\^(?:\{(" + _GROUP + r")\}|([A-Za-z0-9])))?"
)


def split_frontmatter(text: str) -> tuple[str, str]:
    """@brief 拆出 frontmatter 与正文
    @param text 文件全文
    @return (frontmatter, body)
    """
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[3:end], text[end + 4:]


def canonical(base: str, sub: str, sup: str) -> str:
    """@brief 生成符号的规范键
    @param base 主体（字母或 \\cmd）
    @param sub  下标（可为空）
    @param sup  上标（可为空）
    @return 形如 N_RE、E_r、TBS_temp、nu 的键
    """
    def clean(part: str) -> str:
        """去掉 \\text{...} / \\mathrm{...} 等包装，只保留内容"""
        if not part:
            return part
        for cmd in ("\\text", "\\mathrm", "\\mathit", "\\mathbf"):
            part = part.replace(cmd + "{", "").replace("}", "")
        return part

    key = base[1:] if base.startswith("\\") else base
    if sub:
        key += "_" + clean(sub)
    if sup:
        key += "^" + clean(sup)
    return key


def extract_symbols(text: str) -> list[tuple[str, int]]:
    """@brief 抽取数学片段中的符号及其在全文中的偏移
    @param text 全文
    @return [(规范键, 偏移)] 按出现顺序
    """
    out: list[tuple[str, int]] = []
    for m in MATH_RE.finditer(text):
        body = m.group(1) or m.group(2) or ""
        base_off = m.start()
        for tm in TOKEN_RE.finditer(body):
            base = tm.group(1)
            if base.startswith("\\") and base[1:] in OPERATOR_CMDS:
                continue
            sub = tm.group(2) or tm.group(3) or ""
            sup = tm.group(4) or tm.group(5) or ""
            if len(base) == 1 and base.isdigit():
                continue
            out.append((canonical(base, sub.strip(), sup.strip()), base_off + tm.start()))
    return out


def check_file(path: Path, show: bool = False) -> tuple[bool, list[str]]:
    """@brief 检查单篇笔记的符号前置定义
    @param path 笔记路径
    @param show 是否打印抽取到的符号集
    @return (是否通过, 问题列表)
    """
    text = path.read_text(encoding="utf-8")
    _, body = split_frontmatter(text)
    problems: list[str] = []

    first_math = MATH_RE.search(body)
    if not first_math:
        return True, []

    sec = SECTION_RE.search(body)
    if not sec:
        return False, ["缺 `## 符号与记号约定`（或 `## 符号约定`）小节"]
    if sec.start() > first_math.start():
        problems.append(
            f"符号小节位于首次数学使用之后（第 {body[:sec.start()].count(chr(10)) + 1} 行 vs 第 {body[:first_math.start()].count(chr(10)) + 1} 行）"
        )

    # 小节文本范围：到下一个同级或更高级标题
    level = 2 if sec.group(0).startswith("## ") else 3
    rest = body[sec.end():]
    stop = re.search(r"^#{2,%d}\s" % level, rest, re.MULTILINE)
    sec_text = rest[: stop.start()] if stop else rest
    defined = {canonical(m.group(1), (m.group(2) or m.group(3) or "").strip(), (m.group(4) or m.group(5) or "").strip())
               for m in TOKEN_RE.finditer(sec_text)
               if not (m.group(1).startswith("\\") and m.group(1)[1:] in OPERATOR_CMDS)}

    seen: set[str] = set()
    for key, off in extract_symbols(body):
        if key in seen:
            continue
        seen.add(key)
        if key in defined:
            continue
        line = body[:off].count("\n") + 1
        problems.append(f"符号 {key} 在首次使用（第 {line} 行）前未定义")

    if show:
        print(f"    symbols({len(seen)}): " + ", ".join(sorted(seen)))
        print(f"    defined({len(defined)}): " + ", ".join(sorted(defined)))
    return (len(problems) == 0), problems


def iter_notes(paths: list[str]) -> list[Path]:
    """@brief 展开待检查文件
    @param paths CLI 路径列表
    @return 笔记路径列表
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
    return [p for p in out if p.name not in {"概念图谱入口.md", "README.md"}]


def main() -> int:
    """@brief 命令入口
    @return 退出码
    """
    ap = argparse.ArgumentParser(description="概念笔记符号前置定义审计")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--show-symbols", action="store_true")
    args = ap.parse_args()

    notes = iter_notes(args.paths)
    if not notes:
        print("NO_INPUT")
        return 1

    bad = 0
    for p in notes:
        ok, problems = check_file(p, args.show_symbols)
        rel = p.relative_to(PROJECT_ROOT) if PROJECT_ROOT in p.parents else p
        if not ok:
            bad += 1
            print(f"FAIL {rel}")
            for pr in problems:
                print(f"     - {pr}")
        elif args.show_symbols:
            print(f"PASS {p.name}")

    print("---")
    print(f"检查 {len(notes)} 篇：FAIL {bad} 篇")
    if bad:
        print("SYMBOL_TABLE_AUDIT_FAIL")
        return 1
    print("SYMBOL_TABLE_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
