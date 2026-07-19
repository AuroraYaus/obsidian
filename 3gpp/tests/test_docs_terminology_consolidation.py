from pathlib import Path
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / 'docs'
LESSON_ROOTS = [DOCS / 'L1', DOCS / 'L2', DOCS / 'L3']


class DocsTerminologyConsolidationTest(unittest.TestCase):
    def test_glossary_exists_with_core_terms(self):
        glossary = DOCS / 'L0' / 'L0_terminology_glossary.md'
        text = glossary.read_text(encoding='utf-8')
        for term in ['3GPP', 'LTE', 'NR', 'LLR', 'CRC', 'HARQ', 'LDPC', 'Turbo', 'Polar']:
            self.assertIn(f'| {term} |', text)

    def test_lesson_chapters_do_not_define_local_glossary_tables(self):
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
