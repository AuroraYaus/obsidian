#!/usr/bin/env python3
"""
@file    audit_frontmatter_types.py
@brief   审计文档 frontmatter `type` 字段与文档角色的一致性，防复发
         2026-08-14 审核发现的 65 篇讲义 type 误标问题（L1 41 篇标
         definition、L3 24 篇标 spec，应为 algorithm）。
@date    2026-08-14
@note    分类语义权威定义见 .claude/rules/documentation.md §2.1：
         algorithm = 讲义（T/TX 编号正文）、definition = 概念笔记
         （English_中文 六段式）、spec = 导航入口/规则/术语表。
         检查范围限定三类语义明确的文件；docs/audits/、docs/superpowers/、
         3GPP全流程_缩写概念理论清单.md 等内部工作文档豁免（语义未定，
         不强行归类）。教训来源：2026-08-14 全库审核——type 字段错标
         使 Obsidian 按类型过滤/查询静默失效，且无工具检查（口径
         登记于《项目规则与记忆索引.md》六.9 与 lessons/
         lesson-audit-governance-2026-08-14.md 教训二）。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# 项目根（3gpp/），docs 与 tools 的相对锚点。
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / "docs"

# 讲义目录：T*.md / TX*.md 文件必须 type: algorithm。
LECTURE_DIRS = ("L1_基础", "L2_协议算法", "L3_工程实现")
LECTURE_NAME_RE = re.compile(r"^(T\d.*|TX\d.*)\.md$")

# 概念笔记：docs/concepts/ 下 English_中文.md 必须 type: definition；
# 概念图谱入口是导航文件，单独归入 spec。
CONCEPT_DIR = "concepts"
CONCEPT_NAME_RE = re.compile(r"^[A-Za-z0-9]+_.+\.md$")

# 导航/规则/术语表：type: spec（相对 PROJECT_ROOT 的路径）。
SPEC_FILES = {
    "docs/3GPP_讲义入口.md",
    "docs/L0_协议阅读引导/T0.1_LTE_NR_decoder_protocol_reading_map.md",
    "docs/L0_协议阅读引导/L0_术语入口.md",
    "docs/L0_协议阅读引导/L0_terminology_glossary.md",
    "docs/L1_基础/L1_基础入口.md",
    "docs/L2_协议算法/L2_协议算法入口.md",
    "docs/L2_协议算法/术语表.md",
    "docs/L3_工程实现/L3_工程实现入口.md",
    "docs/concepts/概念图谱入口.md",
}

# 豁免（不检查 type）：内部工作文档，语义未定不强行归类。
EXEMPT_PATTERNS = (
    re.compile(r"^docs/(audits|superpowers)/"),
    re.compile(r"^docs/concepts/3GPP全流程_缩写概念理论清单\.md$"),
)


def extract_type(path: Path) -> str | None:
    """@brief 解析 Markdown frontmatter 中的 `type:` 字段值。
    @param path 待解析的 Markdown 文件路径。
    @return   type 字段值；无 frontmatter 或无 type 字段时返回 None。
    @note     frontmatter 必须是文件开头第一个 `---` 围栏块；
              type 行按 `type: <值>`（允许任意空白）匹配。"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    m = re.search(r"^---\n(.*?)\n---", text, flags=re.DOTALL)
    if not m:
        return None
    tm = re.search(r"^type:\s*(.+)$", m.group(1), flags=re.MULTILINE)
    return tm.group(1).strip() if tm else None


def collect_targets() -> list[tuple[Path, str]]:
    """@brief 按文档角色收集需要检查 type 一致性的文件与期望值。
    @return  (文件路径, 期望 type 值) 列表。
    @note    三类角色：讲义（algorithm）、概念笔记（definition）、
             导航/规则/术语表（spec）；豁免清单直接跳过。"""
    targets: list[tuple[Path, str]] = []
    for d in LECTURE_DIRS:
        layer = DOCS / d
        if not layer.is_dir():
            continue
        for f in sorted(layer.glob("*.md")):
            if LECTURE_NAME_RE.match(f.name):
                targets.append((f, "algorithm"))
    concept_dir = DOCS / CONCEPT_DIR
    if concept_dir.is_dir():
        for f in sorted(concept_dir.glob("*.md")):
            if CONCEPT_NAME_RE.match(f.name):
                targets.append((f, "definition"))
    for rel in sorted(SPEC_FILES):
        f = PROJECT_ROOT / rel
        if f.is_file():
            targets.append((f, "spec"))
    return targets


def is_exempt(path: Path) -> bool:
    """@brief 判断文件是否属豁免范围（内部工作文档）。
    @param path 待判断文件路径。
    @return  命中豁免模式时返回 True。"""
    rel = str(path.relative_to(PROJECT_ROOT))
    return any(p.match(rel) for p in EXEMPT_PATTERNS)


def main() -> int:
    """@brief 脚本入口：全库 frontmatter type 一致性审计。
    @usage python3 tools/audit_frontmatter_types.py
    @args  无（固定扫描 docs/ 下三类语义明确的文件）。
    @env   无外部依赖（仅标准库）。
    @exit_code 0 = 全部文件 type 与角色一致；1 = 存在不一致（列出明细）。
    @note  与 audit_link_integrity.py 等 vault 级审计同风格：
           发现即打印明细并在末尾输出汇总行。"""
    failures: list[str] = []
    checked = 0
    for path, expected in collect_targets():
        if is_exempt(path):
            continue
        checked += 1
        actual = extract_type(path)
        if actual != expected:
            failures.append(
                f"{path.relative_to(PROJECT_ROOT)}: type={actual!r}, 期望 {expected!r}"
            )
    if failures:
        print("FRONTMATTER_TYPE_AUDIT_FAIL")
        print("\n".join(failures))
        print(f"共 {len(failures)} 处不一致（检查 {checked} 个文件）")
        return 1
    print(f"FRONTMATTER_TYPE_AUDIT_OK（检查 {checked} 个文件）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
