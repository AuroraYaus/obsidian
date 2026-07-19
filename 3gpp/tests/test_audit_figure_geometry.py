import tempfile
import unittest
from pathlib import Path

import tools.audit_figure_geometry as audit


class FigureGeometryAuditTest(unittest.TestCase):
    def write_script(self, root: Path, text: str) -> Path:
        path = root / "render_sample.py"
        path.write_text(text, encoding="utf-8")
        return path

    def test_good_script_uses_geometry_helpers_and_visual_checklist(self) -> None:
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

    def test_recently_reported_ldpc_scripts_are_historical_focus(self) -> None:
        expected = {
            "render_nr_ldpc_decoder_chain_overview.py",
            "render_nr_ldpc_base_graph_selection.py",
            "render_nr_ldpc_lifting_qc_matrix.py",
            "render_ldpc_tanner_syndrome.py",
        }

        self.assertLessEqual(expected, audit.HISTORICAL_FOCUS)


if __name__ == "__main__":
    unittest.main()
