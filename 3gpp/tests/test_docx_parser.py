""" @file test_docx_parser.py
    @brief 测试 .docx 解析器和导出器——段落、标题、公式、表格、图片的提取与可追溯产物导出。
    @date 2025 """

import csv
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.word_extract.docx_parser import parse_docx
from tools.word_extract.exporter import export_document


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="png" ContentType="image/png"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image1.png"/>
</Relationships>
"""

DOCUMENT_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <w:body>
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>1 Scope</w:t></w:r>
    </w:p>
    <w:p><w:r><w:t>Hello </w:t></w:r><w:r><w:t>3GPP</w:t></w:r></w:p>
    <w:p>
      <m:oMath>
        <m:r><m:t>E</m:t></m:r>
        <m:r><m:t>=</m:t></m:r>
        <m:r><m:t>mc</m:t></m:r>
      </m:oMath>
    </w:p>
    <w:p>
      <w:r>
        <w:drawing>
          <a:blip r:embed="rId5"/>
        </w:drawing>
      </w:r>
    </w:p>
    <w:tbl>
      <w:tr>
        <w:tc>
          <w:tcPr><w:gridSpan w:val="2"/></w:tcPr>
          <w:p><w:r><w:t>Merged head</w:t></w:r></w:p>
        </w:tc>
      </w:tr>
      <w:tr>
        <w:tc>
          <w:tcPr><w:vMerge w:val="restart"/></w:tcPr>
          <w:p><w:r><w:t>A1</w:t></w:r></w:p>
        </w:tc>
        <w:tc><w:p><w:r><w:t>B1</w:t></w:r></w:p></w:tc>
      </w:tr>
      <w:tr>
        <w:tc>
          <w:tcPr><w:vMerge/></w:tcPr>
          <w:p/>
        </w:tc>
        <w:tc><w:p><w:r><w:t>B2</w:t></w:r></w:p></w:tc>
      </w:tr>
    </w:tbl>
  </w:body>
</w:document>
"""


def make_docx(path: Path) -> None:
    """
    @brief 在内存中构造一个合法的 DOCX ZIP 文档并写入磁盘。

    通过 Python zipfile 模块按 OOXML 规范组装 [Content_Types].xml、
    _rels/.rels、word/document.xml、word/_rels/document.xml.rels
    和 word/media/image1.png，生成一个可用于测试 docx_parser 和
    exporter 的标准 DOCX 文件。

    @param path  目标文件路径，ZIP/DOCX 将写入此位置。
    @note        生成的 DOCX 包含 1 个一级标题、2 个正文段落、
                 1 个 OMML 公式、1 个含 vMerge/gridSpan 的表格
                 和 1 个内嵌图片引用，覆盖解析器的核心要素。
    """
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("[Content_Types].xml", CONTENT_TYPES)
        zf.writestr("_rels/.rels", ROOT_RELS)
        zf.writestr("word/document.xml", DOCUMENT_XML)
        zf.writestr("word/_rels/document.xml.rels", DOC_RELS)
        zf.writestr("word/media/image1.png", b"\x89PNG\r\n\x1a\nfake")


class DocxParserTests(unittest.TestCase):
    """ @brief 测试 docx_parser 和 exporter：验证 .docx 解析提取段落/标题/公式/表格/图片，以及导出可追溯产物的完整性。 """

    def test_parse_docx_extracts_paragraphs_headings_equations_tables_and_media(self):
        """ @brief 验证 parse_docx 正确提取段落文本、标题标记、公式 XML、表格合并单元格和图片引用。 """
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "38331-j20.docx"
            make_docx(path)

            doc = parse_docx(path)

        self.assertEqual(doc.source_name, "38331-j20.docx")
        self.assertEqual([p.text for p in doc.paragraphs[:2]], ["1 Scope", "Hello 3GPP"])
        self.assertTrue(doc.paragraphs[0].is_heading)
        self.assertEqual(len(doc.equations), 1)
        self.assertIn("<m:oMath", doc.equations[0].xml)
        self.assertEqual(len(doc.tables), 1)
        self.assertEqual(doc.tables[0].rows[0][0].colspan, 2)
        self.assertEqual(doc.tables[0].rows[1][0].rowspan, 2)
        self.assertEqual(len(doc.media), 1)
        self.assertEqual(doc.media[0].relationship_id, "rId5")
        self.assertEqual(doc.media[0].target, "media/image1.png")

    def test_export_document_writes_traceable_artifacts(self):
        """ @brief 验证 export_document 生成完整的可追溯产物：source.docx、document.xml、content.md、README、sections、tables（HTML/CSV）、equations 和 media。 """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "38331-j20.docx"
            output = root / "out"
            make_docx(source)
            doc = parse_docx(source)

            metadata = export_document(doc, output)

            doc_dir = output / "TS_38.331_38331-j20"
            self.assertEqual(metadata["spec"], "TS 38.331")
            self.assertTrue((doc_dir / "source.docx").exists())
            self.assertTrue((doc_dir / "document.xml").exists())
            self.assertTrue((doc_dir / "content.md").exists())
            self.assertTrue((doc_dir / "README.md").exists())
            self.assertTrue((doc_dir / "sections.jsonl").exists())
            self.assertTrue((doc_dir / "tables" / "table_0001.html").exists())
            self.assertTrue((doc_dir / "tables" / "table_0001.csv").exists())
            self.assertTrue((doc_dir / "equations" / "equation_0001.xml").exists())
            self.assertTrue((doc_dir / "media" / "image1.png").exists())

            html = (doc_dir / "tables" / "table_0001.html").read_text()
            self.assertIn('colspan="2"', html)
            self.assertIn('rowspan="2"', html)
            with (doc_dir / "tables" / "table_0001.csv").open(newline="") as f:
                rows = list(csv.reader(f))
            self.assertEqual(rows[0], ["Merged head", ""])
            section = json.loads((doc_dir / "sections.jsonl").read_text().splitlines()[0])
            self.assertEqual(section["section"], "1")
            self.assertEqual(section["title"], "Scope")
            readme = (doc_dir / "README.md").read_text()
            self.assertIn("TS 38.331", readme)
            self.assertIn("source.docx", readme)
            self.assertIn("Table artifacts", readme)
            self.assertIn("Equation artifacts", readme)


if __name__ == "__main__":
    unittest.main()
