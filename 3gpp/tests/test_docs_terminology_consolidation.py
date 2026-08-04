""" @file test_docs_terminology_consolidation.py
    @brief 测试讲义中的术语整合规则——全局术语表是否存在、各课是否禁止局部术语表。
    @date 2025 """

from pathlib import Path
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / 'docs'
LESSON_ROOTS = [DOCS / 'L1', DOCS / 'L2_协议算法', DOCS / 'L3']


class DocsTerminologyConsolidationTest(unittest.TestCase):
    """ @brief 测试 docs 术语整合：验证全局术语表（L0）覆盖核心术语，各课不定义局部术语表。 """

    def test_glossary_exists_with_core_terms(self):
        """ @brief 验证 L0 全局术语表存在且包含 3GPP、LTE、NR、LLR、CRC、HARQ、LDPC、Turbo、Polar 等核心术语。 """
        glossary = DOCS / 'L0' / 'L0_terminology_glossary.md'
        text = glossary.read_text(encoding='utf-8')
        for term in ['3GPP', 'LTE', 'NR', 'LLR', 'CRC', 'HARQ', 'LDPC', 'Turbo', 'Polar']:
            self.assertIn(f'| {term} |', text)

    def test_lesson_chapters_do_not_define_local_glossary_tables(self):
        """ @brief 验证 L1/L2/L3 各课不包含局部术语表（如"术语登场""本节缩写说明"等表头）。 """
        offenders = []
        forbidden = [
            '## 术语登场',
            '## 本节缩写说明',
            '| 缩写 | 全称 |',
            '| 中文名 | 英文全称 | 缩写 |',
        ]
        for root in LESSON_ROOTS:
            for path in sorted(root.glob('T*.md')):
                text = path.read_text(encoding='utf-8')
                for pattern in forbidden:
                    if pattern in text:
                        offenders.append(f'{path.relative_to(PROJECT_ROOT)}: {pattern}')
        self.assertEqual([], offenders)


if __name__ == '__main__':
    unittest.main()
