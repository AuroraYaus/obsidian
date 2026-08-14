""" @file test_diagram_audit_tools.py
    @brief 测试 Mermaid 图表审计工具和 Python 渲染脚本输出审计工具。
    @date 2025 """

import tempfile
import unittest
from pathlib import Path

from PIL import Image


class MermaidDiagramAuditTests(unittest.TestCase):
    """ @brief 测试 audit_mermaid_diagrams 模块：验证 Mermaid 图表中的有序列表节点标签、subgraph 命名等规则。 """

    def test_reports_ordered_list_syntax_in_node_label(self) -> None:
        """ @brief 验证审计能检测到节点标签中使用有序列表语法（如 "1. Configure descriptor"）。 """
        from tools.audit_mermaid_diagrams import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "```mermaid\n"
                "flowchart LR\n"
                "  A[\"1. Configure descriptor\"] --> B[\"Decode\"]\n"
                "```\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], render=False)

        self.assertTrue(any(f.rule == "ordered_list_label" for f in findings), findings)

    def test_reports_subgraph_display_name_without_id(self) -> None:
        """ @brief 验证审计能检测到 subgraph 仅有显示文本而无 ID 的情况。 """
        from tools.audit_mermaid_diagrams import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "```mermaid\n"
                "flowchart TB\n"
                "  subgraph Core Process\n"
                "    A[Input] --> B[Output]\n"
                "  end\n"
                "```\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], render=False)

        self.assertTrue(any(f.rule == "subgraph_name_without_id" for f in findings), findings)

    def test_accepts_skill_compatible_flowchart(self) -> None:
        """ @brief 验证使用规范 subgraph ID、classDef 和 stage 类的 Mermaid 图通过审计。 """
        from tools.audit_mermaid_diagrams import audit_markdown_files

        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "lesson.md"
            md.write_text(
                "```mermaid\n"
                "flowchart LR\n"
                "  subgraph core[\"Core Process\"]\n"
                "    A[\"Step 1 - Descriptor\"] --> B[\"Step 2 - Address trace\"]\n"
                "  end\n"
                "  B --> C[\"Decoder output\"]\n"
                "  classDef stage fill:#e7f5ff,stroke:#1971c2,stroke-width:2px\n"
                "  class A,B,C stage\n"
                "```\n",
                encoding="utf-8",
            )

            findings = audit_markdown_files([md], render=False)

        self.assertEqual([], findings)


class PythonFigureOutputAuditTests(unittest.TestCase):
    """ @brief 测试 audit_python_figure_outputs 模块：验证 Python 渲染脚本的输出 PNG 是否正确生成。 """

    def test_reports_script_that_exits_zero_without_png_output(self) -> None:
        """ @brief 验证审计能检测到脚本正常退出但未生成声明 PNG 输出的情况。 """
        from tools.archive_python_drawing.audit_python_figure_outputs import audit_scripts

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "render_no_output.py"
            script.write_text("print('ok')\n", encoding="utf-8")

            findings = audit_scripts([script], project_root=Path(tmp))

        self.assertTrue(any(f.rule == "missing_png_output" for f in findings), findings)

    def test_accepts_script_that_writes_declared_png(self) -> None:
        """ @brief 验证脚本正确生成声明的 PNG 输出时通过审计。 """
        from tools.archive_python_drawing.audit_python_figure_outputs import audit_scripts

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "render_ok.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw\n"
                "OUT = Path('assets/out.png')\n"
                "OUT.parent.mkdir(exist_ok=True)\n"
                "img = Image.new('RGB', (320, 180), 'white')\n"
                "draw = ImageDraw.Draw(img)\n"
                "draw.rectangle((40, 40, 280, 140), outline='black', width=3)\n"
                "img.save(OUT)\n",
                encoding="utf-8",
            )

            findings = audit_scripts([script], project_root=root)

        self.assertEqual([], findings)

    def test_ignores_function_local_png_path_variables_as_declared_outputs(self) -> None:
        """ @brief 验证审计忽略函数局部变量声明的 PNG 输出路径，不将其视为模块级输出声明。 """
        from tools.archive_python_drawing.audit_python_figure_outputs import audit_scripts

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "render_ok.py"
            script.write_text(
                "from pathlib import Path\n"
                "from PIL import Image, ImageDraw\n"
                "ASSET_DIR = Path('assets')\n"
                "def main():\n"
                "    ASSET_DIR.mkdir(exist_ok=True)\n"
                "    out = ASSET_DIR / 'actual.png'\n"
                "    img = Image.new('RGB', (320, 180), 'white')\n"
                "    draw = ImageDraw.Draw(img)\n"
                "    draw.rectangle((40, 40, 280, 140), outline='black', width=3)\n"
                "    img.save(out)\n"
                "if __name__ == '__main__':\n"
                "    main()\n",
                encoding="utf-8",
            )

            findings = audit_scripts([script], project_root=root)

        self.assertEqual([], findings)

    def test_does_not_attribute_preexisting_recent_png_to_script(self) -> None:
        """ @brief 验证审计不会将已存在的 PNG 文件误判为脚本生成的新输出。 """
        from tools.archive_python_drawing.audit_python_figure_outputs import audit_scripts

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            asset_dir = root / "assets"
            asset_dir.mkdir()
            preexisting = asset_dir / "recent.png"
            Image.new("RGB", (320, 180), "white").save(preexisting)
            script = root / "render_no_output.py"
            script.write_text("print('ok')\n", encoding="utf-8")

            findings = audit_scripts([script], project_root=root)

        self.assertTrue(any(f.rule == "missing_png_output" for f in findings), findings)


if __name__ == "__main__":
    unittest.main()
