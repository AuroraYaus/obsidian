""" @file test_python_figure_audits.py
    @brief 测试 Python 图表审计工具集——文字适配静态审计、文字重叠动态审计、文字内边距审计、图片内容边界审计、正文等价审计、元素覆盖审计、项目图片台账审计。
    @date 2025 """

import tempfile
import unittest
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw


class FigureTextFitStaticAuditTests(unittest.TestCase):
    """ @brief 测试 audit_figure_text_fit_static 模块：验证渲染脚本中的静默截断、长直文文字、逐字符换行和缺少布局保护的审计规则。 """

    def test_reports_silent_line_truncation(self):
        """ @brief 验证审计能检测到使用 lines[:2] 切片导致静默截断多余行的情况。 """
        from tools.archive_python_drawing.audit_figure_text_fit_static import audit_paths

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad.py"
            script.write_text(
                "def draw(draw, lines):\n"
                "    for line in lines[:2]:\n"
                "        draw.text((10, 10), line)\n",
                encoding="utf-8",
            )

            findings = audit_paths([script])

        self.assertTrue(any(f.rule == "silent_truncation" for f in findings), findings)

    def test_reports_long_direct_draw_text_literal(self):
        """ @brief 验证审计能检测到 draw.text 使用过长字符串字面量（可能溢出固定尺寸盒子）。 """
        from tools.archive_python_drawing.audit_figure_text_fit_static import audit_paths

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad.py"
            script.write_text(
                "def draw(draw):\n"
                "    draw.text((10, 10), 'This sentence is long enough that it should be wrapped or checked before drawing inside a fixed figure box.')\n",
                encoding="utf-8",
            )

            findings = audit_paths([script])

        self.assertTrue(any(f.rule == "long_direct_text" for f in findings), findings)

    def test_reports_character_by_character_wrapping(self):
        """ @brief 验证审计能检测到逐字符拼接换行逻辑（for ch in text: current += ch）而非使用标准换行函数。 """
        from tools.archive_python_drawing.audit_figure_text_fit_static import audit_paths

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad.py"
            script.write_text(
                "def draw_wrapped(draw, text):\n"
                "    current = ''\n"
                "    for ch in text:\n"
                "        current += ch\n",
                encoding="utf-8",
            )

            findings = audit_paths([script])

        self.assertTrue(any(f.rule == "character_wrap" for f in findings), findings)

    def test_reports_wrapped_text_without_layout_guard(self):
        """ @brief 验证审计能检测到调用 draw_wrapped 但结果 y 坐标未与面板底边比较（无布局保护）。 """
        from tools.archive_python_drawing.audit_figure_text_fit_static import audit_paths

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad.py"
            script.write_text(
                "def draw_wrapped(draw, xy, text, font, fill, width):\n"
                "    return xy[1] + 100\n"
                "\n"
                "def render(draw):\n"
                "    panel = (10, 10, 300, 160)\n"
                "    draw_wrapped(draw, (20, 40), 'long panel note', font, fill, 240)\n",
                encoding="utf-8",
            )

            findings = audit_paths([script])

        self.assertTrue(any(f.rule == "wrapped_without_layout_guard" for f in findings), findings)

    def test_text_fit_audit_exit_code_blocks_long_direct_text(self):
        """ @brief 验证 main() 函数在检测到长直文文字时返回非零退出码（1）。 """
        from tools.archive_python_drawing.audit_figure_text_fit_static import main

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad.py"
            script.write_text(
                "def draw(draw):\n"
                "    draw.text((10, 10), 'This sentence is long enough that it should be wrapped or checked before drawing inside a fixed figure box.')\n",
                encoding="utf-8",
            )

            exit_code = main([str(script)])

        self.assertEqual(1, exit_code)

    def test_allows_nearby_text_fit_ok_comment_for_short_label(self):
        """ @brief 验证带有 TEXT_FIT_OK 注释的短标签 draw.text 调用不产生审计告警。 """
        from tools.archive_python_drawing.audit_figure_text_fit_static import audit_paths

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_ok.py"
            script.write_text(
                "def draw(draw):\n"
                "    # TEXT_FIT_OK: short coordinate label\n"
                "    draw.text((10, 10), 'i=0')\n",
                encoding="utf-8",
            )

            findings = audit_paths([script])

        self.assertEqual([], findings)


class FigureTextOverlapDynamicAuditTests(unittest.TestCase):
    """ @brief 测试 audit_figure_text_overlap_dynamic 模块：验证运行渲染脚本后检测文字 bbox 重叠的审计规则。 """

    def test_reports_overlapping_text_bboxes(self):
        """ @brief 验证审计能检测到 'Title Text' 和 'Body Text' 两个 draw.text 调用产生的 bbox 重叠。 """
        from tools.archive_python_drawing.audit_figure_text_overlap_dynamic import audit_script

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad_overlap.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw, ImageFont\n"
                "img = Image.new('RGB', (420, 220), 'white')\n"
                "draw = ImageDraw.Draw(img)\n"
                "font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)\n"
                "draw.text((40, 40), 'Title Text', font=font, fill='black')\n"
                "draw.text((40, 50), 'Body Text', font=font, fill='black')\n"
                "img.save(Path('out.png'))\n",
                encoding="utf-8",
            )

            findings = audit_script(script)

        self.assertTrue(any(f.rule == "text_bbox_overlap" for f in findings), findings)

    def test_accepts_non_overlapping_text_bboxes(self):
        """ @brief 验证两个 draw.text 调用之间间距足够（y=40 vs y=100）时通过文字重叠审计。 """
        from tools.archive_python_drawing.audit_figure_text_overlap_dynamic import audit_script

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_ok_overlap.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw, ImageFont\n"
                "img = Image.new('RGB', (420, 220), 'white')\n"
                "draw = ImageDraw.Draw(img)\n"
                "font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)\n"
                "draw.text((40, 40), 'Title Text', font=font, fill='black')\n"
                "draw.text((40, 100), 'Body Text', font=font, fill='black')\n"
                "img.save(Path('out.png'))\n",
                encoding="utf-8",
            )

            findings = audit_script(script)

        self.assertEqual([], findings)


class FigureTextPaddingDynamicAuditTests(unittest.TestCase):
    """ @brief 测试 audit_figure_text_padding_dynamic 模块：验证渲染脚本中文字与圆角矩形框之间的内边距审计。 """

    def test_reports_text_tight_to_rounded_box_edge(self):
        """ @brief 验证审计能检测到文字贴边放置在圆角矩形框内部（padding 不足）。 """
        from tools.archive_python_drawing.audit_figure_text_padding_dynamic import audit_script

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_bad_padding.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw, ImageFont\n"
                "img = Image.new('RGB', (360, 160), 'white')\n"
                "draw = ImageDraw.Draw(img)\n"
                "font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)\n"
                "draw.rounded_rectangle((20, 40, 145, 72), radius=8, fill='blue')\n"
                "draw.text((24, 44), 'N=8 LLR', font=font, fill='white')\n"
                "img.save(Path('out.png'))\n",
                encoding="utf-8",
            )

            findings = audit_script(script)

        self.assertTrue(any(f.rule == "text_box_padding" for f in findings), findings)

    def test_accepts_text_with_padding_inside_rounded_box(self):
        """ @brief 验证文字在圆角矩形框内有足够内边距时通过审计。 """
        from tools.archive_python_drawing.audit_figure_text_padding_dynamic import audit_script

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_ok_padding.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw, ImageFont\n"
                "img = Image.new('RGB', (360, 160), 'white')\n"
                "draw = ImageDraw.Draw(img)\n"
                "font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)\n"
                "draw.rounded_rectangle((20, 40, 170, 82), radius=8, fill='blue')\n"
                "draw.text((44, 50), 'N=8 LLR', font=font, fill='white')\n"
                "img.save(Path('out.png'))\n",
                encoding="utf-8",
            )

            findings = audit_script(script)

        self.assertEqual([], findings)

    def test_skips_large_containers_by_default_but_can_include_them(self):
        """ @brief 验证默认跳过大型容器（白底黑边）的内边距检查，但 include_containers=True 时包含。 """
        from tools.archive_python_drawing.audit_figure_text_padding_dynamic import audit_script

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_container_padding.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw, ImageFont\n"
                "img = Image.new('RGB', (460, 240), 'white')\n"
                "draw = ImageDraw.Draw(img)\n"
                "font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)\n"
                "draw.rounded_rectangle((20, 20, 420, 190), radius=12, fill='white', outline='black')\n"
                "draw.text((24, 24), 'Panel title', font=font, fill='black')\n"
                "img.save(Path('out.png'))\n",
                encoding="utf-8",
            )

            default_findings = audit_script(script)
            container_findings = audit_script(script, include_containers=True)

        self.assertEqual([], default_findings)
        self.assertTrue(any(f.rule == "text_box_padding" for f in container_findings), container_findings)


class ImageContentBoundsAuditTests(unittest.TestCase):
    """ @brief 测试 audit_image_content_bounds 模块：验证图片底部空白区域过多的审计规则。 """

    def test_reports_excessive_bottom_blank_space(self):
        """ @brief 验证审计能检测到底部空白超过 120px 且比例超过 20% 的图片。 """
        from tools.audit_image_content_bounds import audit_images

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.png"
            img = Image.new("RGB", (400, 600), "white")
            draw = ImageDraw.Draw(img)
            draw.rectangle((40, 40, 360, 300), fill="black")
            img.save(path)

            findings = audit_images([path], max_bottom_pixels=120, max_bottom_ratio=0.20)

        self.assertTrue(any(f.rule == "excessive_bottom_blank" for f in findings), findings)

    def test_accepts_reasonable_bottom_margin(self):
        """ @brief 验证底部空白在合理范围内时通过审计。 """
        from tools.audit_image_content_bounds import audit_images

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ok.png"
            img = Image.new("RGB", (400, 380), "white")
            draw = ImageDraw.Draw(img)
            draw.rectangle((40, 40, 360, 300), fill="black")
            img.save(path)

            findings = audit_images([path], max_bottom_pixels=120, max_bottom_ratio=0.20)

        self.assertEqual([], findings)


class PythonFigureBodyEquivalentAuditTests(unittest.TestCase):
    """ @brief 测试 audit_python_figure_body_equivalents 模块：验证正文中等价图/等价表、资产引用、元标签与图片生成散文的审计规则。 """

    def test_reports_png_without_nearby_equivalent_marker(self):
        """ @brief 验证审计能检测到 PNG 图片嵌入后附近无正文等价标记（如"Mermaid 等价图""Markdown 等价表"）。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/a.png)\n\n"
                "图说明：这是 Python 生成图片。\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=16)

        self.assertEqual(1, len(findings), findings)
        self.assertEqual("missing_body_equivalent", findings[0].rule)

    def test_accepts_nearby_mermaid_equivalent_marker(self):
        """ @brief 验证 PNG 嵌入附近有完整 Mermaid 等价图和等价表时通过审计。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/a.png)\n\n"
                "图片内容正文等价：Mermaid 等价图\n\n"
                "```mermaid\n"
                "flowchart LR\n"
                "  A[\"Protocol config: K/E/RV\"] --> B[\"Rate recovery address trace\"]\n"
                "  B --> C[\"Decoder input LLR vector\"]\n"
                "  C --> D[\"CRC and metric outputs\"]\n"
                "```\n"
                "\n"
                "| 等价项 | 正文表达 |\n"
                "|:---|:---|\n"
                "| 输入 | descriptor 记录 K、E、RV、调制阶数和 mask hash。 |\n"
                "| 地址 | rate recovery 生成每个接收 LLR 对应的母码地址，并记录 RV 窗口、skip 位置和写回顺序。 |\n"
                "| 输出 | decoder input LLR、CRC 结果、迭代次数、first mismatch 和失败 replay 字段。 |\n"
                "| 边界 | punctured 位置保持 unknown，shortened 位置给 known-zero 约束，repeated 位置累加并饱和。 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=16)

        self.assertEqual([], findings)

    def test_rejects_body_png_embed_even_with_nearby_equivalent(self):
        """ @brief 验证当 allow_body_image_embeds=False 时，即使有完整等价图/表仍拒绝 PNG 嵌入（正文不应直接引用图片）。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/a.png)\n\n"
                "图片内容正文等价：Mermaid 等价图\n\n"
                "```mermaid\n"
                "flowchart LR\n"
                "  A[\"Protocol config: K/E/RV\"] --> B[\"Rate recovery address trace\"]\n"
                "  B --> C[\"Decoder input LLR vector\"]\n"
                "  C --> D[\"CRC and metric outputs\"]\n"
                "```\n"
                "\n"
                "| 等价项 | 正文表达 |\n"
                "|:---|:---|\n"
                "| 输入 | descriptor 记录 K、E、RV、调制阶数和 mask hash。 |\n"
                "| 地址 | rate recovery 生成每个接收 LLR 对应的母码地址，并记录 RV 窗口、skip 位置和写回顺序。 |\n"
                "| 输出 | decoder input LLR、CRC 结果、迭代次数、first mismatch 和失败 replay 字段。 |\n"
                "| 边界 | punctured 位置保持 unknown，shortened 位置给 known-zero 约束，repeated 位置累加并饱和。 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=16, allow_body_image_embeds=False)

        self.assertTrue(any(f.rule == "body_image_embed_disallowed" for f in findings), findings)

    def test_accepts_retained_asset_marker_with_nearby_equivalent(self):
        """ @brief 验证"原图片资产"标记配合等价图/表（allow_body_image_embeds=False）时通过审计。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "原图片资产：`assets/a.png`\n\n"
                "图片内容正文等价：Mermaid 等价图\n\n"
                "```mermaid\n"
                "flowchart LR\n"
                "  A[\"Protocol config: K/E/RV\"] --> B[\"Rate recovery address trace\"]\n"
                "  B --> C[\"Decoder input LLR vector\"]\n"
                "  C --> D[\"CRC and metric outputs\"]\n"
                "```\n"
                "\n"
                "| 等价项 | 正文表达 |\n"
                "|:---|:---|\n"
                "| 输入 | descriptor 记录 K、E、RV、调制阶数和 mask hash。 |\n"
                "| 地址 | rate recovery 生成每个接收 LLR 对应的母码地址，并记录 RV 窗口、skip 位置和写回顺序。 |\n"
                "| 输出 | decoder input LLR、CRC 结果、迭代次数、first mismatch 和失败 replay 字段。 |\n"
                "| 边界 | punctured 位置保持 unknown，shortened 位置给 known-zero 约束，repeated 位置累加并饱和。 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=16, allow_body_image_embeds=False)

        self.assertEqual([], findings)

    def test_reports_retained_asset_marker_without_nearby_equivalent(self):
        """ @brief 验证仅有"原图片资产"标记但无等价内容时审计报告缺失等价标记。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "原图片资产：`assets/a.png`\n\n"
                "图说明：历史 PNG 已保留。\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=8, allow_body_image_embeds=False)

        self.assertTrue(any(f.rule == "missing_body_equivalent" for f in findings), findings)

    def test_rejects_meta_equivalent_labels_in_lesson_body(self):
        """ @brief 验证审计能检测到等价表中使用元标签（如"图片":"assets/a.png""生成脚本":"tools/..."). """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "原图片资产：`assets/a.png`\n\n"
                "图片内容正文等价：Mermaid 等价图\n\n"
                "| 等价项 | 正文表达 |\n"
                "|:---|:---|\n"
                "| 图片 | `assets/a.png` |\n"
                "| 生成脚本 | `tools/figures/render.py` |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], forbid_meta_labels=True)

        self.assertTrue(any(f.rule == "body_meta_label_disallowed" for f in findings), findings)

    def test_rejects_image_generation_prose_in_lesson_body(self):
        """ @brief 验证审计能检测到讲义正文中出现图片生成散文（如"由 tools/figures/render.py 生成"）。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "## 接收端流程\n\n"
                "图 T1-1 由 `tools/figures/render.py` 生成，输出到 `docs/L2_协议算法/assets/figure.png`。读图顺序为：A 到 B。\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], forbid_meta_labels=True, forbid_image_prose=True)

        self.assertTrue(any(f.rule == "body_image_prose_disallowed" for f in findings), findings)

    def test_allows_image_generation_prose_in_evidence_section(self):
        """ @brief 验证"执行与证据记录"章节中的图片生成散文不产生审计告警。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "## 接收端流程\n\n"
                "```mermaid\nflowchart LR\nA --> B\n```\n\n"
                "## 执行与证据记录\n\n"
                "| 项目 | 记录 |\n"
                "|:---|:---|\n"
                "| 图片脚本 | `tools/figures/render.py` |\n"
                "| 图片输出 | `docs/L2_协议算法/assets/figure.png` |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], forbid_meta_labels=True, forbid_image_prose=True)

        self.assertEqual([], findings)

    def test_accepts_nearby_markdown_table_marker(self):
        """ @brief 验证 PNG 嵌入附近有"Markdown 等价表"和包含具体字段/含义的表时通过审计。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/a.png)\n\n"
                "Markdown 等价表\n\n"
                "| 字段 | 含义 |\n"
                "|:---|:---|\n"
                "| input descriptor | 记录 K、E、RV、调制阶数和协议证据路径。 |\n"
                "| address trace | 每个 rx LLR 写回的 circular-buffer 或 codeword 地址。 |\n"
                "| mask state | 区分 unknown、known zero、punctured、shortened 和 repeated。 |\n"
                "| output evidence | 保存 CRC、迭代次数、first mismatch 和 replay command。 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=8)

        self.assertEqual([], findings)

    def test_rejects_placeholder_mermaid_equivalent(self):
        """ @brief 验证审计能检测到 Mermaid 等价图中使用通用占位符节点（如"读图顺序为""相邻正文表格承接字段"），而非具体内容。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/a.png)\n\n"
                "图片内容正文等价：Mermaid 等价图\n\n"
                "```mermaid\n"
                "flowchart LR\n"
                "  N0[\"读图顺序为：Protocol Config\"]\n"
                "  N1[\"相邻正文表格承接字段、边界和工程检查点\"]\n"
                "  N0 --> N1\n"
                "```\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=12)

        self.assertTrue(any(f.rule == "low_quality_body_equivalent" for f in findings), findings)


class PythonFigureDirectExecutionTests(unittest.TestCase):
    """ @brief 测试渲染脚本的直接执行——验证模块导入路径和等价内容质量审计。 """

    def test_shared_text_fit_helper_imports_when_script_is_executed_by_path(self):
        """ @brief 验证 render_lte_turbo_interleaver_table.py 通过 subprocess 直接执行时不出现 ModuleNotFoundError。 """
        root = Path(__file__).resolve().parents[1]
        script = root / "tools/archive_python_drawing/figures/render_lte_turbo_interleaver_table.py"

        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=root,
            text=True,
            capture_output=True,
            timeout=30,
        )

        self.assertNotIn("ModuleNotFoundError: No module named 'tools'", proc.stderr)
        self.assertEqual(0, proc.returncode, proc.stderr[-2000:])

    def test_rejects_generic_table_equivalent(self):
        """ @brief 验证审计能检测到等价表中使用通用模板文字（如"图片中的关键字段、流程或矩阵含义由正文表格化承接"）而非具体内容。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/a.png)\n\n"
                "图片内容正文等价：Markdown 等价表\n\n"
                "| 等价项 | 正文表达 |\n"
                "|:---|:---|\n"
                "| 图片 | `assets/a.png` |\n"
                "| 图中信息 1 | 图片中的关键字段、流程或矩阵含义由正文表格化承接。 |\n"
                "| 阅读方式 | 以本表和相邻正文为主，PNG 只作为视觉辅助；字段、流程和边界不得只存在于图片像素中。 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=12)

        self.assertTrue(any(f.rule == "low_quality_body_equivalent" for f in findings), findings)

    def test_rejects_generic_decoder_pipeline_equivalent(self):
        """ @brief 验证审计能检测到 Mermaid 等价图中使用通用流水线节点（如"输入字段""地址/状态转换""译码器消费""验证输出"）而非具体协议字段。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![figure](assets/t8.png)\n\n"
                "图片内容正文等价：Mermaid 等价图\n\n"
                "```mermaid\n"
                "flowchart LR\n"
                "  N0[\"输入字段\"]\n"
                "  N1[\"地址/状态转换\"]\n"
                "  N2[\"译码器消费\"]\n"
                "  N3[\"验证输出\"]\n"
                "  N0 --> N1\n"
                "  N1 --> N2\n"
                "  N2 --> N3\n"
                "```\n"
                "\n"
                "| 等价项 | 正文表达 |\n"
                "|:---|:---|\n"
                "| 图片 | `assets/t8.png` |\n"
                "| 生成脚本 | `tools/figures/render_t8.py` |\n"
                "| 图中节点 | 输入字段 |\n"
                "| 图中节点 | 地址/状态转换 |\n"
                "| 图中节点 | 译码器消费 |\n"
                "| 图中节点 | 验证输出 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=20)

        self.assertTrue(any(f.rule == "low_quality_body_equivalent" for f in findings), findings)

    def test_accepts_split_figure_group_sharing_one_equivalent(self):
        """ @brief 验证两张分图共享一个等价表且表内包含具体字段（row index, column index, set index, shift value）时通过审计。 """
        from tools.archive_python_drawing.audit_python_figure_body_equivalents import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "# Lesson\n\n"
                "![part 1](assets/a_part1.png)\n\n"
                "![part 2](assets/a_part2.png)\n\n"
                "图片内容正文等价：Markdown 等价表\n\n"
                "| 字段 | 含义 |\n"
                "|:---|:---|\n"
                "| source | 两张分图是同一张协议长表的连续片段，正文等价表共同解释列结构和读表规则。 |\n"
                "| row index | 基矩阵行组；空白 row index 继承上一条非空 row group。 |\n"
                "| column index | 基矩阵列组；与 row index 共同定位一个有效 edge 位置。 |\n"
                "| set index | 当前 Zc 先映射到 iLS，再读取对应 set-index 列的 shift value。 |\n"
                "| shift value | 数值 0 是有效零移位，未列出的 row/column 位置才是全零子块。 |\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], window_lines=20)

        self.assertEqual([], findings)


class PythonFigureElementCoverageAuditTests(unittest.TestCase):
    """ @brief 测试 audit_python_figure_element_coverage 模块：验证渲染脚本中的可见文字在讲义正文中的覆盖情况审计。 """

    def test_reports_missing_visible_text_from_render_script(self):
        """ @brief 验证审计能检测到渲染脚本中有 'CN Unit' 和 'Sign product, min1, min2, argmin' 但讲义中未覆盖。 """
        from tools.archive_python_drawing.audit_python_figure_element_coverage import audit_pair

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "render.py"
            lesson = root / "lesson.md"
            script.write_text(
                "def render(draw):\n"
                "    draw.text((10, 10), 'CN Unit')\n"
                "    draw.text((10, 40), 'Sign product, min1, min2, argmin')\n",
                encoding="utf-8",
            )
            lesson.write_text("# Lesson\n\n这里只讲 VN RMW，没有覆盖校验节点。\n", encoding="utf-8")

            findings = audit_pair(script, lesson)

        self.assertTrue(any(f.rule == "missing_visible_text_element" and "CN Unit" in f.message for f in findings), findings)
        self.assertTrue(any("Sign product, min1, min2, argmin" in f.message for f in findings), findings)

    def test_accepts_chinese_expansion_when_key_terms_are_covered(self):
        """ @brief 验证渲染脚本中的英文关键词（Layered Controller 等）在讲义中文展开中已覆盖时通过审计。 """
        from tools.archive_python_drawing.audit_python_figure_element_coverage import audit_pair

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "render.py"
            lesson = root / "lesson.md"
            script.write_text(
                "def card(draw, rect, title, body, fill):\n"
                "    pass\n"
                "def render(draw):\n"
                "    card(draw, (0, 0, 1, 1), 'Layered Controller', 'Iteration, layer, local index and valid/stall control.', '#fff')\n",
                encoding="utf-8",
            )
            lesson.write_text(
                "# Lesson\n\n"
                "Layered Controller 负责产生 iteration、layer、local index，以及 valid/stall 控制，"
                "它把每一轮 row group 的调度约束展开成逐拍信号。\n",
                encoding="utf-8",
            )

            findings = audit_pair(script, lesson)

        self.assertEqual([], findings)

    def test_extracts_visible_text_from_assigned_lists_and_tables(self):
        """ @brief 验证元素覆盖审计能从赋值列表（titles/bodies）和二维列表（rows）中提取可见文字并检查讲义覆盖。 """
        from tools.archive_python_drawing.audit_python_figure_element_coverage import audit_pair

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "render.py"
            lesson = root / "lesson.md"
            script.write_text(
                "titles = ['LOAD', 'CHECK']\n"
                "bodies = ['Latch descriptor and schedule hash.', 'Full-H syndrome, optional CRC gate.']\n"
                "rows = [['QC address', 'BG/Zc/iLS/shift/local', 'edge_hash, shift_dir']]\n",
                encoding="utf-8",
            )
            lesson.write_text(
                "# Lesson\n\n"
                "LOAD 状态锁存 descriptor 与 schedule hash。CHECK 状态执行 Full-H syndrome 和可选 CRC gate。"
                "QC address 使用 BG/Zc/iLS/shift/local，并暴露 edge_hash、shift_dir。\n",
                encoding="utf-8",
            )

            findings = audit_pair(script, lesson)

        self.assertEqual([], findings)


class ProjectImageInventoryAuditTests(unittest.TestCase):
    """ @brief 测试 audit_project_image_inventory 模块：验证项目图片台账（inventory/migration）的完整性审计。 """

    def test_reports_body_image_missing_from_inventory_and_migration_ledger(self):
        """ @brief 验证审计能检测到讲义中引用的 PNG 未在 image_asset_inventory 和 migration ledger 中登记。 """
        from tools.audit_project_image_inventory import audit_project

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lesson_dir = root / "docs/L2_协议算法"
            asset_dir = lesson_dir / "assets"
            audit_dir = root / "docs/audits"
            asset_dir.mkdir(parents=True)
            audit_dir.mkdir(parents=True)

            (asset_dir / "figure.png").write_bytes(b"png")
            (lesson_dir / "T1.md").write_text(
                "# Lesson\n\n![figure](assets/figure.png)\n\n",
                encoding="utf-8",
            )
            (audit_dir / "image_asset_inventory.md").write_text(
                "# Inventory\n\n| Asset | Script |\n|:---|:---|\n",
                encoding="utf-8",
            )
            (audit_dir / "python_figure_to_body_content_migration.md").write_text(
                "# Migration\n\n| Lesson | Image | Script | Equivalent type | Status | Body location |\n|:---|:---|:---|:---|:---|:---|\n",
                encoding="utf-8",
            )

            findings = audit_project(root)

        rules = {finding.rule for finding in findings}
        self.assertIn("missing_inventory_row", rules)
        self.assertIn("missing_migration_row", rules)

    def test_accepts_ledger_classified_asset_without_body_reference(self):
        """ @brief 验证图片仅存在于台账中（讲义正文无 img 引用）且 migration 标记为 body_text_represented 时通过审计。 """
        from tools.audit_project_image_inventory import audit_project

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lesson_dir = root / "docs/L2_协议算法"
            asset_dir = lesson_dir / "assets"
            audit_dir = root / "docs/audits"
            asset_dir.mkdir(parents=True)
            audit_dir.mkdir(parents=True)

            (asset_dir / "figure.png").write_bytes(b"png")
            (lesson_dir / "T1.md").write_text(
                "# Lesson\n\n## 接收端流程\n\n```mermaid\nflowchart LR\nA --> B\n```\n\n",
                encoding="utf-8",
            )
            (audit_dir / "image_asset_inventory.md").write_text(
                "# Inventory\n\n"
                "| Asset | Script |\n"
                "|:---|:---|\n"
                "| `docs/L2_协议算法/assets/figure.png` | `tools/figures/render.py` |\n",
                encoding="utf-8",
            )
            (audit_dir / "python_figure_to_body_content_migration.md").write_text(
                "# Migration\n\n"
                "| Lesson | Image | Script | Equivalent type | Status | Body location |\n"
                "|:---|:---|:---|:---|:---|:---|\n"
                "| `docs/L2_协议算法/T1.md` | `assets/figure.png` | `tools/figures/render.py` | Mermaid | body_text_represented; asset_retained | `docs/L2_协议算法/T1.md:3` |\n",
                encoding="utf-8",
            )

            findings = audit_project(root)

        self.assertEqual([], findings)

    def test_accepts_evidence_only_asset_when_inventory_and_migration_mark_it(self):
        """ @brief 验证台账中标记为 evidence_only 的图片（非当前正文引用）在 inventory 和 migration 均登记时通过审计。 """
        from tools.audit_project_image_inventory import audit_project

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lesson_dir = root / "docs/L2_协议算法"
            asset_dir = lesson_dir / "assets"
            audit_dir = root / "docs/audits"
            asset_dir.mkdir(parents=True)
            audit_dir.mkdir(parents=True)

            (asset_dir / "part1.png").write_bytes(b"png")
            (asset_dir / "full.png").write_bytes(b"png")
            (lesson_dir / "T1.md").write_text(
                "# Lesson\n\n![part](assets/part1.png)\n\n",
                encoding="utf-8",
            )
            (audit_dir / "image_asset_inventory.md").write_text(
                "# Inventory\n\n"
                "| Asset | Script |\n"
                "|:---|:---|\n"
                "| `docs/L2_协议算法/assets/part1.png` | `tools/figures/render.py` |\n"
                "| `docs/L2_协议算法/assets/full.png` | `tools/figures/render.py` |\n",
                encoding="utf-8",
            )
            (audit_dir / "python_figure_to_body_content_migration.md").write_text(
                "# Migration\n\n"
                "| Lesson | Image | Script | Equivalent type | Status | Body location |\n"
                "|:---|:---|:---|:---|:---|:---|\n"
                "| `docs/L2_协议算法/T1.md` | `assets/part1.png` | `tools/figures/render.py` | Markdown 等价表 | present_quality_pass; body_referenced | `docs/L2_协议算法/T1.md:3` |\n"
                "| `docs/L2_协议算法/T1.md` | `assets/full.png` | `tools/figures/render.py` | not_applicable | evidence_only; not_current_body_reference | `docs/L2_协议算法/T1.md:3` |\n",
                encoding="utf-8",
            )

            findings = audit_project(root)

        self.assertEqual([], findings)


if __name__ == "__main__":
    unittest.main()
