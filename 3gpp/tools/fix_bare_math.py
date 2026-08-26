#!/usr/bin/env python3
"""
@file    fix_bare_math.py
@brief   批量修复讲义中未加 $ 围栏的裸数学标记（一次性迁移脚本）。
         输入为 audit_latex_render.py 的 bare math 报告行，逐行精确包裹。
@date    2026-08-26
@note    规则来源：CLAUDE.md 纠错固化（2026-08-26 T2.0 裸标记教训）。
         仅处理报告命中的 (文件, 行, token)；纯文本替换（不用正则模式
         作替换串，避免 \| 字面残留）；智能扩展 max|token| / |token|
         整体包裹；跳过已被 $ 包裹的 token（防嵌套包裹）。
@usage   python3 fix_bare_math.py <hits.txt>
@args    hits.txt  audit_latex_render.py --syntax-only 输出的 bare math 行
@exit_code  0 = 成功，1 = 解析失败
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path


def is_wrapped(line: str, start: int, end: int) -> bool:
    """@brief 判断 [start,end) 区间是否已落在某对 $ 围栏之内（含紧邻）。
    扫描行内所有 $ 位置，若 token 起点位于某对 $ 之间则视为已包裹。"""
    # 快速路径：紧邻 $ 直接判定
    if (start > 0 and line[start - 1] == "$") or (end < len(line) and line[end] == "$"):
        return True
    # 慢速路径：token 位于任意 $...$ 对内
    dollar_positions = [i for i, ch in enumerate(line) if ch == "$"]
    for i in range(0, len(dollar_positions) - 1, 2):
        open_pos, close_pos = dollar_positions[i], dollar_positions[i + 1]
        if open_pos < start and end <= close_pos:
            return True
    return False


def wrap_token(line: str, token: str) -> tuple[str, int]:
    """@brief 在行内把裸 token 包上 $；支持 max|token| / |token| 整体扩展。
    @param line   原始行文本。
    @param token  待包裹的裸标记（如 x(n)、q_h、|q_h|）。
    @return (更新后行, 替换次数)。"""
    updated = line
    count = 0
    # 由长到短尝试整体表达式，命中即停
    candidates = [f"max|{token}|", f"|{token}|", token]
    for candidate in candidates:
        if candidate not in updated:
            continue
        # 检查每个出现的 candidate 是否已被包裹
        search_from = 0
        replaced_any = False
        while True:
            idx = updated.find(candidate, search_from)
            if idx == -1:
                break
            if not is_wrapped(updated, idx, idx + len(candidate)):
                updated = updated[:idx] + f"${candidate}$" + updated[idx + len(candidate):]
                replaced_any = True
                search_from = idx + len(candidate) + 2
            else:
                search_from = idx + len(candidate)
        if replaced_any:
            count += replaced_any
            break
    return updated, count


def main() -> int:
    """@brief 解析审计报告并按行包裹裸标记。
    @return 0 = 成功"""
    hits_file = Path(sys.argv[1])
    hits: dict[Path, dict[int, set[str]]] = defaultdict(lambda: defaultdict(set))
    for line in hits_file.read_text(encoding="utf-8").splitlines():
        match = __import__("re").match(r"^(.+?):(\d+): bare math \w+ '(.+?)' missing \$ fences$", line)
        if not match:
            continue
        path, lineno, token = match.group(1), int(match.group(2)), match.group(3)
        hits[Path(path)][lineno].add(token)

    for path, lines in sorted(hits.items()):
        text = path.read_text(encoding="utf-8")
        raw_lines = text.splitlines()
        for lineno, tokens in sorted(lines.items()):
            original = raw_lines[lineno - 1]
            updated = original
            for token in sorted(tokens, key=len, reverse=True):
                updated, count = wrap_token(updated, token)
                if count == 0:
                    print(f"WARN: {path}:{lineno}: token {token!r} not found: {original!r}")
            raw_lines[lineno - 1] = updated
        trailing = "\n" if text.endswith("\n") else ""
        path.write_text("\n".join(raw_lines) + trailing, encoding="utf-8")
        print(f"fixed: {path} ({sum(len(v) for v in lines.values())} tokens on {len(lines)} lines)")

    print("ALL_BARE_MATH_FIXED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
