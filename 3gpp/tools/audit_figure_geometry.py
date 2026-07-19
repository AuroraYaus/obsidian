#!/usr/bin/env python3
"""Static audit for Python figure geometry-risk patterns."""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path


DEFAULT_PATHS = [Path("tools/figures")]

HISTORICAL_FOCUS = {
    "render_lte_turbo_encoder_structure.py",
    "render_lte_dl_ul_decoder_context.py",
    "render_nr_polar_channel_polarization.py",
    "render_nr_polar_rate_recovery_flow.py",
    "render_nr_polar_sc_decoding_tree.py",
    "render_turbo_ldpc_polar_algorithm_comparison.py",
    "render_lte_nr_rate_matching_comparison.py",
    "render_nr_ldpc_decoder_chain_overview.py",
    "render_nr_ldpc_base_graph_selection.py",
    "render_nr_ldpc_lifting_qc_matrix.py",
    "render_ldpc_tanner_syndrome.py",
    "render_harq_soft_buffer_comparison.py",
    "render_t12_1_golden_model_layout.py",
    "render_t14_1_lte_turbo_rtl_microarchitecture.py",
    "render_t14_2_nr_ldpc_rtl_microarchitecture.py",
    "render_t14_3_nr_polar_rtl_microarchitecture.py",
    "render_t14_4_unified_decoder_subsystem.py",
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
    func = node.func
    return isinstance(func, ast.Attribute) and func.attr == "line"


def assigned_point_list_lengths(fn: ast.FunctionDef) -> dict[str, int]:
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
    return text.count("\n", 0, offset) + 1


def has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)


def function_name(block: str) -> str:
    match = re.match(r"def\s+(\w+)\s*\(", block)
    return match.group(1) if match else ""


def audit_file(path: Path) -> list[str]:
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
