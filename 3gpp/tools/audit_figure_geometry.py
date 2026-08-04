#!/usr/bin/env python3
"""
@file    audit_figure_geometry.py
@brief   静态审计 Python 教学图渲染脚本中的几何风险模式。
         检测箭头连接方式、多段路径、弯曲连接、向 量箭头一致性等潜在布局错误，
         避免生成误导学生的几何变形图。
@date    2026-07-22

Static audit for Python figure geometry-risk patterns.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path


DEFAULT_PATHS = [Path("tools/figures")]

HISTORICAL_FOCUS = {
    # T6.3/T7.5/T8.1/T8.2/T8.3/T8.4 的 PIL 渲染脚本已删除：图已改为手绘 SVG
    # docs/L2_协议算法/assets/T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.svg 等
    # render_t12_1_golden_model_layout.py 已删除：图已改为手绘 SVG
    # docs/L3_工程实现/assets/T12.1_golden_model_project_layout.svg
}

GEOMETRY_HELPERS = (
    "boundary_point",
    "connect_arrow",
    "draw_centered",
    "draw_centered_lines",
    "draw_wrapped_centered",
    "center_text",
    "text_center",
    "anchor=\"mm\"",
    "anchor='mm'",
)

MIN_GAP_HINTS = (
    "flow_to_table",
    "title_to_node",
    "bottom_margin",
    "spacing",
    "gap",
    "min_top",
)

LEFT_TOP_TEXT_RE = re.compile(
    r"draw\.text\(\(\s*(?:x|cx|box\[0\]|b\[0\]|cell\[0\])\s*[+,-]\s*\d+"
    r"\s*,\s*(?:y|cy|box\[1\]|b\[1\]|cell\[1\])\s*[+,-]\s*\d+"
)

FIXED_NOTE_Y_RE = re.compile(
    r"(?:def\s+draw_(?:checks|note|notes|legend|footer)|读图顺序|工程检查点|风险|要点)"
    r"[\s\S]{0,600}?\n\s*y\s*=\s*\d+[\s\S]{0,500}?\n\s*y\s*\+=\s*\d+",
    re.MULTILINE,
)

ARROW_FUNCTION_RE = re.compile(r"def\s+arrow\s*\([^)]*start[^)]*end[^)]*\)\s*:")
FUNCTION_RE = re.compile(r"^def\s+\w+\s*\(", re.MULTILINE)
DIRECT_TO_TIP_LINE_PATTERNS = (
    "draw.line((start, end)",
    "draw.line((start[0], start[1], end[0], end[1])",
    "draw.line((start[0], start[1], end[0], end[1]),",
)
CROSSING_RISK_RE = re.compile(r"\b(?:polyline_arrow|elbow_arrow)\s*\(")
CROSSING_ASSERT_HELPERS = (
    "assert_no_unrelated_crossing",
    "segment_intersects_rect",
)
CURVED_ARROW_JOIN_RE = re.compile(r"draw\.line\([^)]*joint\s*=\s*[\"']curve[\"']", re.DOTALL)
CURVE_CONNECTOR_RE = re.compile(
    r"\b(?:arc|pieslice|chord|bezier|curve|spline)\b|"
    r"(?:cubic|quadratic|Path\.CURVE|CURVE3|CURVE4)",
    re.IGNORECASE,
)
ARROW_LIKE_NAME_RE = re.compile(r"^def\s+\w*arrow\w*\s*\(", re.MULTILINE)
ARROW_DRAW_LINE_RE = re.compile(
    r"draw\.line\(\s*(?P<arg>\[[^\n]*\]|[A-Za-z_][A-Za-z0-9_]*|line_points)",
    re.DOTALL,
)
POLYLINE_ALLOW_NAMES = ("polyline", "elbow", "feedback", "route", "loop")
VECTOR_ARROW_TOKENS = (
    "math.hypot",
    "math.atan2",
    " / length",
    " / dist",
    "ux",
    "uy",
    "unit",
)
VECTOR_LINE_END_RE = re.compile(
    r"(?:line_end|end)\s*=\s*\("
    r"[^)]*-\s*(?:(?:ux|unit_x|dx\s*/\s*(?:length|dist))\s*\*\s*[^,)]*|[^,)]*\*\s*(?:ux|unit_x)),"
    r"[^)]*-\s*(?:(?:uy|unit_y|dy\s*/\s*(?:length|dist))\s*\*\s*[^,)]*|[^,)]*\*\s*(?:uy|unit_y))",
    re.DOTALL,
)
VECTOR_LINE_POINTS_RE = re.compile(
    r"line_points\s*=\s*[^\n]*"
    r"\([^)]*-\s*(?:(?:ux|unit_x)\s*\*\s*[^,)]*|[^,)]*\*\s*(?:ux|unit_x)),"
    r"[^)]*-\s*(?:(?:uy|unit_y)\s*\*\s*[^,)]*|[^,)]*\*\s*(?:uy|unit_y))",
    re.DOTALL,
)
FIXED_AXIS_LINE_END_RE = re.compile(
    r"line_end\s*=\s*\([^)]*(?:x1|ex|end\[0\])\s*-\s*head_[a-z_]*\s*,"
    r"\s*(?:y1|ey|end\[1\])\s*\)",
    re.DOTALL,
)
ARROWHEAD_WING_VECTOR_RE = re.compile(
    r"(?:px|perp_x)\s*,\s*(?:py|perp_y)\s*="
    r"|(?:px|perp_x)\s*=\s*"
    r"|(?:math\.sin\(angle\)|math\.cos\(angle\))"
    r"|(?:-\s*(?:uy|unit_y)\s*,\s*(?:ux|unit_x))",
    re.DOTALL,
)
ARROWHEAD_FIXED_WING_RE = re.compile(
    r"draw\.polygon\(\s*\[[\s\S]{0,500}?"
    r"(?:ex|x1|end\[0\])\s*-\s*(?:ux|unit_x|head_len|head_[a-z_]+)[^,\n]*-\s*\d+"
    r"[\s\S]{0,500}?"
    r"(?:ey|y1|end\[1\])\s*-\s*(?:uy|unit_y|head_len|head_[a-z_]+)[^,\n]*[+-]\s*\d+",
    re.DOTALL,
)


def is_draw_line_call(node: ast.Call) -> bool:
    """
    @brief   检查 AST 节点是否为 draw.line() 调用。
             用于在 AST 遍历中快速筛选出箭头绘制的关键语句，避免对所有函数调用进行无差别检查。
    @param   node  待检查的 AST Call 节点。
    @return  若调用是 draw.line() 则返回 True，否则返回 False。
    """
    func = node.func
    return isinstance(func, ast.Attribute) and func.attr == "line"


def assigned_point_list_lengths(fn: ast.FunctionDef) -> dict[str, int]:
    """
    @brief   收集函数体内被赋值的列表/元组的长度。
             用于判断箭头路径是否为多段路径——若变量名被赋值为 ≥3 个元素的列表，
             则该变量可能是多段折线的点集，需要进一步审查。
    @param   fn  待分析的 AST 函数定义节点。
    @return  变量名到列表/元组长度的映射字典；未赋值的变量不在字典中出现。
    @note    仅处理顶层赋值语句，嵌套解包和推导式中的赋值不参与长度推断。
    """
    assigned: dict[str, int] = {}
    for node in ast.walk(fn):
        if not isinstance(node, ast.Assign):
            continue
        value = node.value
        if isinstance(value, (ast.List, ast.Tuple)):
            value_len = len(value.elts)
        else:
            continue
        for target in node.targets:
            if isinstance(target, ast.Name):
                assigned[target.id] = value_len
    return assigned


def audit_arrow_function_ast(path: Path, text: str) -> list[str]:
    """
    @brief   基于 AST 对箭头辅助函数进行深度几何审计。
             检查箭头是否使用了弯曲连接 (joint='curve')、是否绘制了多段路径、
             箭身是否与箭头方向共线、箭头翼点是否由法向量推导——这些是教学图中
             箭头看起来歪斜或不流畅的根本原因。
    @param   path   被审计脚本的文件路径，用于在发现中定位问题行。
    @param   text   脚本的完整源代码文本，供正则回退检查使用。
    @return  几何审计发现列表，每个元素是格式化的发现字符串。
    @note    本函数同时使用 AST 遍历和正则回退——AST 用于精确的节点级检测，
             正则用于 AST 无法覆盖的复杂模式匹配。
    """
    findings: list[str] = []
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return findings

    for fn in [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]:
        name = fn.name
        if "arrow" not in name.lower():
            continue
        allows_polyline = any(token in name.lower() for token in POLYLINE_ALLOW_NAMES)
        assigned_lengths = assigned_point_list_lengths(fn)

        for node in ast.walk(fn):
            if not isinstance(node, ast.Call) or not is_draw_line_call(node) or not node.args:
                continue

            for keyword in node.keywords:
                if keyword.arg == "joint" and isinstance(keyword.value, ast.Constant) and keyword.value.value == "curve":
                    findings.append(
                        f"{path}:{node.lineno}: arrow helper '{name}' uses joint='curve'; "
                        "ordinary flow arrows must stay visually straight, and avoidance routes must be explicit straight segments"
                    )

            first_arg = node.args[0]
            point_count: int | None = None
            if isinstance(first_arg, ast.List):
                point_count = len(first_arg.elts)
            elif isinstance(first_arg, ast.Name):
                point_count = assigned_lengths.get(first_arg.id)

            if point_count is not None and point_count >= 3 and not allows_polyline:
                findings.append(
                    f"{path}:{node.lineno}: arrow helper '{name}' draws a {point_count}-point path; "
                    "ordinary arrow helpers must draw one straight shaft from start to vector-shortened line_end. "
                    "Use a polyline/elbow helper only for documented avoidance routes with crossing assertions."
                )

    return findings


def collect_files(paths: list[Path]) -> list[Path]:
    """
    @brief   从给定的路径列表中收集所有 .py 文件。
             目录会被展开为其中所有 .py 文件，文件直接添加——这是统一文件入口，
             避免每个审计函数重复实现文件遍历逻辑。
    @param   paths  路径列表，可混合目录和文件。
    @return  按文件名排序的 .py 文件路径列表。
    @note    不存在的路径被静默跳过，不抛异常。
    """
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.glob("*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return files


def line_for_offset(text: str, offset: int) -> int:
    """
    @brief   将文本中的字符偏移量转换为行号（1-based）。
             正则匹配返回的是字符位置，而审计报告需要人类可读的行号。
    @param   text    源文本。
    @param   offset  字符偏移量（0-based）。
    @return  1-based 行号。
    """
    return text.count("\n", 0, offset) + 1


def has_any(text: str, needles: tuple[str, ...]) -> bool:
    """
    @brief   检查文本中是否包含任意一个给定的子串。
             用于快速判断脚本中是否存在某些关键模式，决定是否需要深入审计。
    @param   text     要搜索的文本。
    @param   needles  待匹配的子串元组。
    @return  若存在任意匹配则返回 True，否则返回 False。
    """
    return any(needle in text for needle in needles)


def function_name(block: str) -> str:
    """
    @brief   从函数定义块中提取函数名。
             用于在按函数分段审计时标记当前上下文属于哪个函数。
    @param   block  函数定义的源代码块文本。
    @return  函数名字符串；若匹配失败则返回空字符串。
    """
    match = re.match(r"def\s+(\w+)\s*\(", block)
    return match.group(1) if match else ""


def audit_file(path: Path) -> list[str]:
    """
    @brief   对单个 Python 脚本执行全部几何审计规则。
             这是几何审计的核心引擎——汇总 AST 审计、正则模式匹配、
             历史关注列表检查、箭头连接完整性验证等所有维度的检查结果。
    @param   path  待审计的 .py 文件路径。
    @return  该文件的所有几何审计发现列表。
    @note    每个发现字符串格式为 "path:line: 问题描述"。
             历史关注文件（HISTORICAL_FOCUS）有额外的强制性检查，
             因为这些文件曾出现过几何问题。
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[str] = audit_arrow_function_ast(path, text)

    if ARROW_FUNCTION_RE.search(text) and "boundary_point" not in text:
        findings.append(
            f"{path}: arrow(start,end) exists without boundary_point helper; "
            "verify arrows connect true node boundaries"
        )

    if CROSSING_RISK_RE.search(text) and not has_any(text, CROSSING_ASSERT_HELPERS):
        findings.append(
            f"{path}: polyline/elbow arrow exists without segment-rectangle crossing assertion; "
            "add assert_no_unrelated_crossing() or document why no node bbox is available"
        )

    for idx, line_text in enumerate(lines):
        if not LEFT_TOP_TEXT_RE.search(line_text):
            continue
        context = "\n".join(lines[max(0, idx - 35) : idx + 1])
        table_context = (
            "draw_table" in context
            or "row_h" in context
            or "headers" in context
            or "for cell" in context
            or "Comparison matrix" in context
            or "Descriptor" in context
        )
        if not table_context:
            continue
        line = idx + 1
        findings.append(
            f"{path}:{line}: cell text appears left/top aligned; "
            "use centered table-cell helper unless this is a paragraph block"
        )

    note_match = FIXED_NOTE_Y_RE.search(text)
    if note_match:
        line = line_for_offset(text, note_match.start())
        findings.append(
            f"{path}:{line}: bottom/note block appears to use fixed y layout; "
            "use bbox-based centered/adaptive layout or record paragraph exception"
        )

    curved_join = CURVED_ARROW_JOIN_RE.search(text)
    if curved_join:
        line = line_for_offset(text, curved_join.start())
        findings.append(
            f"{path}:{line}: arrow/polyline path uses joint='curve'; "
            "ordinary flow and avoidance routes must render as explicit straight segments unless a curved connector is justified"
        )

    is_focus = path.name in HISTORICAL_FOCUS
    if is_focus and not has_any(text, GEOMETRY_HELPERS):
        findings.append(
            f"{path}: historical focus figure lacks recognized centering/boundary helpers"
        )

    if is_focus and not has_any(text, MIN_GAP_HINTS):
        findings.append(
            f"{path}: historical focus figure lacks explicit gap/bottom-margin assertion hints"
        )

    function_starts = [m.start() for m in FUNCTION_RE.finditer(text)]
    function_starts.append(len(text))
    for idx, start in enumerate(function_starts[:-1]):
        block = text[start : function_starts[idx + 1]]
        name = function_name(block)
        arrow_like = bool(ARROW_LIKE_NAME_RE.match(block))

        if arrow_like:
            curve_match = CURVE_CONNECTOR_RE.search(block)
            if curve_match:
                line = line_for_offset(text, start + curve_match.start())
                findings.append(
                    f"{path}:{line}: arrow helper contains curve/arc/Bezier-style drawing token "
                    f"'{curve_match.group(0)}'; ordinary flow arrows must be straight, and avoidance routes "
                    "must be explicit straight segments with a documented reason"
                )

            line_calls = list(ARROW_DRAW_LINE_RE.finditer(block))
            draws_multi_segment = False
            for call in line_calls:
                arg = call.group("arg").strip()
                if arg in {"points", "line_points"}:
                    draws_multi_segment = True
                    break
                if arg.startswith("[") and arg.count("(") >= 3:
                    draws_multi_segment = True
                    break
            allows_polyline = any(token in name.lower() for token in POLYLINE_ALLOW_NAMES)
            if draws_multi_segment and not allows_polyline:
                line = line_for_offset(text, start + line_calls[0].start()) if line_calls else line_for_offset(text, start)
                findings.append(
                    f"{path}:{line}: arrow helper '{name}' appears to draw a multi-segment path; "
                    "use a straight shaft for ordinary arrow() helpers, or rename/document as an avoidance polyline "
                    "with segment-rectangle assertions"
                )

            if "draw.polygon" in block and not any(token in block for token in VECTOR_ARROW_TOKENS):
                line = line_for_offset(text, start)
                findings.append(
                    f"{path}:{line}: arrow helper '{name}' draws an arrowhead without visible vector-direction math; "
                    "arrowhead orientation must be derived from the actual line segment or final polyline segment"
                )

            if "draw.polygon" in block and any(token in block for token in VECTOR_ARROW_TOKENS):
                has_vector_shortened_shaft = VECTOR_LINE_END_RE.search(block) or VECTOR_LINE_POINTS_RE.search(block)
                if "line_end" not in block and "line_points" not in block and "end =" not in block:
                    line = line_for_offset(text, start)
                    findings.append(
                        f"{path}:{line}: arrow helper '{name}' computes a vector arrowhead but no explicit vector-shortened "
                        "line_end was found; the shaft must stop on the same actual line vector before the arrowhead"
                    )
                elif not has_vector_shortened_shaft:
                    line = line_for_offset(text, start)
                    findings.append(
                        f"{path}:{line}: arrow helper '{name}' does not visibly shorten the shaft along both vector components; "
                        "line_end must be derived from the actual start/end or final-segment unit vector so arrowhead and shaft stay collinear"
                    )
                elif FIXED_AXIS_LINE_END_RE.search(block):
                    line = line_for_offset(text, start)
                    findings.append(
                        f"{path}:{line}: arrow helper '{name}' contains a fixed-axis line_end pattern; "
                        "straight and diagonal arrows must use vector-shortened shaft endpoints"
                    )
                has_vector_wings = ARROWHEAD_WING_VECTOR_RE.search(block)
                if not has_vector_wings or ARROWHEAD_FIXED_WING_RE.search(block):
                    line = line_for_offset(text, start)
                    findings.append(
                        f"{path}:{line}: arrow helper '{name}' arrowhead wing points are not visibly derived "
                        "from the actual segment normal vector; compute wing points around the same vector "
                        "backoff point using the final segment unit vector and perpendicular vector"
                    )

        if "draw.polygon" not in block:
            continue
        if "line_points" in block:
            continue
        if not any(pattern in block for pattern in DIRECT_TO_TIP_LINE_PATTERNS):
            continue
        if "line_end" in block:
            continue
        line = line_for_offset(text, start)
        findings.append(
            f"{path}:{line}: arrow line appears to draw directly to arrow tip; "
            "stop the line before the arrowhead so shaft and head direction stay visually consistent"
        )

    return findings


def main() -> int:
    """
    @brief   图几何审计入口——扫描渲染脚本中的箭头连接、弯曲路径和向量一致性。
    @usage   python audit_figure_geometry.py [paths...] [--focus-only]
    @args    paths        待审计的 .py 文件或目录路径，默认为 tools/figures。
             --focus-only 仅审计 HISTORICAL_FOCUS 中的历史高风险脚本。
    @exit_code  0 = 通过审计，1 = 存在几何风险发现。
    @note    输出包含格式化的发现列表（按 path:line 定位）和聚合状态行。
             历史关注脚本有更严格的检查，因为其几何复杂度更高。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    parser.add_argument(
        "--focus-only",
        action="store_true",
        help="audit only scripts with known historical visual-geometry risks",
    )
    args = parser.parse_args()

    files = collect_files(args.paths)
    if args.focus_only:
        files = [path for path in files if path.name in HISTORICAL_FOCUS]

    findings: list[str] = []
    for path in files:
        findings.extend(audit_file(path))

    if findings:
        print("FIGURE_GEOMETRY_AUDIT_FAIL")
        print("\n".join(findings))
        return 1

    print("FIGURE_GEOMETRY_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
