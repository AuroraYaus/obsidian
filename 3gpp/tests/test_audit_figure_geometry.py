""" @file test_audit_figure_geometry.py
    @brief 测试 tools.audit_figure_geometry 模块——审计渲染脚本中的几何辅助函数（箭头、布局、边界点）使用情况。
    @date 2025 """

import tempfile
import unittest
from pathlib import Path

import tools.audit_figure_geometry as audit


class FigureGeometryAuditTest(unittest.TestCase):
    """ @brief 测试 audit_figure_geometry 模块：验证渲染脚本中的箭头绘制、文字对齐、边界点计算等几何审计规则。 """

    def write_script(self, root: Path, text: str) -> Path:
        """@brief 在临时目录中创建测试用的渲染脚本文件

        将测试用例中内联的 Python 代码写入临时文件，供 audit_file() 读取审计。

        @param root  临时目录的 Path 对象
        @param text  要写入的 Python 源代码文本
        @return      创建的脚本文件 Path"""
        path = root / "render_sample.py"
        path.write_text(text, encoding="utf-8")
        return path

    def test_good_script_uses_geometry_helpers_and_visual_checklist(self) -> None:
        """ @brief 验证使用 draw_centered_lines、boundary_point、connect_arrow 等几何辅助函数和视觉检查清单的脚本通过审计。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
from PIL import ImageDraw

def draw_centered_lines(draw, box, lines):
    draw.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), lines[0], anchor="mm")

def boundary_point(box, toward):
    return box[2], (box[1] + box[3]) / 2

def connect_arrow(draw, src, dst):
    arrow(draw, boundary_point(src, dst), boundary_point(dst, src))

def audit_geometry_assertions():
    assert flow_to_table_gap >= 80
    assert title_to_node_gap >= 36
    assert bottom_margin >= 48

def draw_table(draw, rows):
    for cell_box in rows:
        draw_centered_lines(draw, cell_box, ["cell"])

def draw_note(draw, note_box):
    draw_centered_lines(draw, note_box, ["读图顺序", "工程检查点"])
''',
            )

            self.assertEqual(audit.audit_file(path), [])

    def test_bad_script_reports_fixed_arrows_left_aligned_cells_and_fixed_bottom_note(self) -> None:
        """ @brief 验证审计能检测到固定坐标箭头、左对齐单元格文字和固定 y 轴底部注释三种不良模式。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def arrow(draw, start, end):
    draw.line((start, end))

def draw_table(draw):
    draw.text((x + 16, y + 22), cell)

def draw_checks(draw):
    y = 1100
    for line in checks:
        draw.text((100, y), line)
        y += 52
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("boundary_point" in finding for finding in findings))
            self.assertTrue(any("cell text appears left/top aligned" in finding for finding in findings))
            self.assertTrue(any("bottom/note block appears to use fixed y layout" in finding for finding in findings))

    def test_curved_arrow_join_is_reported(self) -> None:
        """ @brief 验证审计能检测到使用 joint='curve' 的曲线箭头连接。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def polyline_arrow(draw, points):
    draw.line(points, fill="#000", width=4, joint="curve")
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("joint='curve'" in finding for finding in findings))

    def test_curve_connector_inside_arrow_helper_is_reported(self) -> None:
        """ @brief 验证审计能检测到 arrow 辅助函数内部使用了 draw.arc 曲线连接器。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def arrow(draw, start, end):
    draw.arc((0, 0, 100, 100), 0, 90, fill="#000", width=4)
    draw.polygon([end, (end[0] - 10, end[1] - 5), (end[0] - 10, end[1] + 5)])
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("curve/arc/Bezier-style" in finding for finding in findings))

    def test_plain_arrow_helper_with_polyline_path_is_reported(self) -> None:
        """ @brief 验证审计能检测到普通 arrow 辅助函数使用了多段折线路径（非 elbow_arrow）。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def arrow(draw, start, end):
    line_end = (end[0] - 12, end[1])
    points = [start, (start[0] + 30, start[1]), line_end]
    draw.line(points, fill="#000", width=4)
    draw.polygon([end, (end[0] - 10, end[1] - 5), (end[0] - 10, end[1] + 5)])
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("multi-segment path" in finding for finding in findings))

    def test_plain_arrow_helper_with_named_three_point_path_is_reported(self) -> None:
        """ @brief 验证审计能检测到普通 arrow 辅助函数使用命名变量定义三段路径（非 elbow_arrow）。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def boundary_point(box, toward):
    return box[2], (box[1] + box[3]) / 2

def arrow(draw, start, end):
    line_end = (end[0] - 12, end[1])
    shaft = [start, ((start[0] + end[0]) / 2, start[1] + 30), line_end]
    draw.line(shaft, fill="#000", width=4)
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("draws a 3-point path" in finding for finding in findings))

    def test_elbow_arrow_allows_named_three_point_path(self) -> None:
        """ @brief 验证 elbow_arrow 函数允许使用命名三段路径（mid 参数明确说明折线意图）。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def segment_intersects_rect(segment, rect):
    return False

def elbow_arrow(draw, start, mid, end):
    shaft = [start, mid, end]
    draw.line(shaft, fill="#000", width=4)
''',
            )

            findings = audit.audit_file(path)

            self.assertEqual(findings, [])

    def test_arrowhead_without_vector_math_is_reported(self) -> None:
        """ @brief 验证审计能检测到箭尖绘制未使用向量方向数学（使用了硬编码偏移量）。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
def arrow(draw, start, end):
    draw.line((start, end), fill="#000", width=4)
    draw.polygon([end, (end[0] - 10, end[1] - 5), (end[0] - 10, end[1] + 5)])
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("without visible vector-direction math" in finding for finding in findings))

    def test_vector_arrowhead_requires_vector_shortened_shaft(self) -> None:
        """ @brief 验证审计能检测到向量箭尖的箭杆未沿两个向量分量缩短（仅沿 x 轴缩短）。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
import math

def boundary_point(box, toward):
    return box[2], (box[1] + box[3]) / 2

def arrow(draw, start, end):
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    ux, uy = vx / length, vy / length
    head_len = 18
    line_end = (ex - head_len, ey)
    draw.line([start, line_end], fill="#000", width=4)
    px, py = -uy, ux
    draw.polygon([
        (ex, ey),
        (ex - ux * head_len + px * 8, ey - uy * head_len + py * 8),
        (ex - ux * head_len - px * 8, ey - uy * head_len - py * 8),
    ])
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("does not visibly shorten the shaft along both vector components" in finding for finding in findings))

    def test_vector_arrow_with_vector_shortened_shaft_passes(self) -> None:
        """ @brief 验证向量箭尖的箭杆沿两个向量分量正确缩短时通过审计。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
import math

def boundary_point(box, toward):
    return box[2], (box[1] + box[3]) / 2

def arrow(draw, start, end):
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    ux, uy = vx / length, vy / length
    head_len = 18
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill="#000", width=4)
    px, py = -uy, ux
    draw.polygon([
        (ex, ey),
        (ex - ux * head_len + px * 8, ey - uy * head_len + py * 8),
        (ex - ux * head_len - px * 8, ey - uy * head_len - py * 8),
    ])
''',
            )

            findings = audit.audit_file(path)

            self.assertEqual(findings, [])

    def test_vector_arrowhead_requires_perpendicular_wing_points(self) -> None:
        """ @brief 验证审计能检测到箭尖翼点未使用垂直向量分量（使用了硬编码偏移量）。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
import math

def boundary_point(box, toward):
    return box[2], (box[1] + box[3]) / 2

def arrow(draw, start, end):
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    ux, uy = vx / length, vy / length
    head_len = 18
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill="#000", width=4)
    draw.polygon([
        (ex, ey),
        (ex - ux * head_len - 8, ey - uy * head_len - 5),
        (ex - ux * head_len - 8, ey - uy * head_len + 5),
    ])
''',
            )

            findings = audit.audit_file(path)

            self.assertTrue(any("arrowhead wing points" in finding for finding in findings))

    def test_vector_arrowhead_with_perpendicular_wing_points_passes(self) -> None:
        """ @brief 验证箭尖翼点使用垂直向量分量（px, py = -uy, ux）时通过审计。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_script(
                Path(tmp),
                '''
import math

def boundary_point(box, toward):
    return box[2], (box[1] + box[3]) / 2

def arrow(draw, start, end):
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    ux, uy = vx / length, vy / length
    head_len = 18
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill="#000", width=4)
    px, py = -uy, ux
    draw.polygon([
        (ex, ey),
        (ex - ux * head_len + px * 8, ey - uy * head_len + py * 8),
        (ex - ux * head_len - px * 8, ey - uy * head_len - py * 8),
    ])
''',
            )

            findings = audit.audit_file(path)

            self.assertEqual(findings, [])

    def test_collect_files_filters_missing_paths(self) -> None:
        """ @brief 验证 collect_files 能过滤掉不存在的文件路径，只返回实际存在的文件。 """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = self.write_script(
                root,
                '''
def draw_centered_lines(draw, box, lines):
    draw.text((0, 0), lines[0], anchor="mm")
def boundary_point(box, toward):
    return (0, 0)
def connect_arrow(draw, src, dst):
    pass
def draw_table(draw):
    draw_centered_lines(draw, (0, 0, 1, 1), ["cell"])
def draw_note(draw):
    assert bottom_margin >= 48
''',
            )
            missing = root / "missing.py"

            files = audit.collect_files([existing, missing])

            self.assertEqual(files, [existing])

    def test_audit_file_runs_without_crash(self):
        """@brief 审计工具主入口可运行（HISTORICAL_FOCUS 已随 --focus-only 删除）。
        @note 2026-08-07 L 级修复删除空 dict 后，原存在性测试同步更新。"""
        from tools import audit_figure_geometry as audit
        self.assertTrue(hasattr(audit, "audit_file"))
        self.assertTrue(callable(audit.audit_file))
