#!/usr/bin/env python3
"""
@file    audit_lesson_depth.py
@brief   分类审计讲义的"教学深度"——判断讲义是真正的教学笔记还是协议索引。
         通过检查必需章节完整性、理论基础信号密度、协议引用密度、
         边界声明数量和具体示例标记，识别出"薄"讲义——即那些看起来更像
         协议规范索引而非面向零基础学生的教学材料的文档。
@date    2026-07-22

Triage whether lessons look like teachable notes rather than protocol indexes.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## 本节学习目标",
    "## 前置知识检查",
    "## 资料与协议边界",
    "## 执行与证据记录",
    "## 参考文献",
]

THEORY_HINTS = [
    "名称",
    "来源",
    "历史",
    "解决",
    "问题",
    "误解",
    "直观",
    "例子",
    "手算",
    "定义",
    "推导",
    "符号",
    "接收端",
    "工程后果",
]

BOUNDARY_PATTERNS = [
    "只定位",
    "只作为",
    "只标出",
    "不展开",
    "不复现",
    "不要求",
    "未核验",
    "待后续",
    "后续.*再",
    "后续.*展开",
    "后续.*精读",
    "留到",
]

# L3 工程篇分层口径（2026-08-14 审核裁定）：docs/L3_工程实现/ 的主题为
# 综合/功耗/后端/SoC 协同等工程域，协议理论信号少属主题性质（非深度不足），
# 因此理论信号与篇幅阈值按层放宽；协议索引风险仅在理论信号几乎缺失时提示。
# 口径变更与理由的权威登记见《项目规则与记忆索引.md》六.6 与 PLAN.md。
L3_DIR_MARKER = "L3_工程实现"
THEORY_MIN_L12 = 16
THEORY_MIN_L3 = 8
CHARS_MIN_L12 = 9000
CHARS_MIN_L3 = 5000
PROTO_INDEX_THEORY_MAX_L12 = 24
PROTO_INDEX_THEORY_MAX_L3 = 10

# 非讲义目录（2026-08-14 审核裁定，与 audit_term_first_use.py 豁免区 h/i/j 对齐）：
# 概念笔记（六段式，非讲义模板）、计划/设计文档、审计台账、L0 阅读引导
# （type: spec 导航文件）——不属于讲义深度审计范围。
NON_LESSON_DIRS = ("concepts", "superpowers", "audits", "L0_协议阅读引导")


def audit_file(path: Path) -> list[str]:
    """
    @brief   对单个 Markdown 讲义执行教学深度审计。
             综合评估七大维度：(1) 必需章节完整性，(2) 讲义长度，
             (3) 理论基础信号密度（名称/来源/历史/问题/例子等 14 个维度），
             (4) 协议引用密度，(5) 边界/延迟声明数量，
             (6) 具体手工示例标记，(7) 协议索引风险综合评分。
    @param   path  Markdown 讲义文件路径。
    @return  教学深度发现列表，每个元素描述一项不足。
    @note    协议索引风险判断采用双重阈值：协议引用>=20 且理论分数<24，
             因为真正的教学文档应该同时包含大量协议引用和充分的理论解释。
             单方面满足（如仅大量引用但理论分数达标）不触发该警告。
             L3 工程篇（docs/L3_工程实现/）按分层口径放宽（2026-08-14 裁定）：
             理论阈值 16→8、篇幅阈值 9000→5000、协议索引理论上限 24→10——
             综合/功耗/后端主题协议理论少属主题性质，见模块常量注释。
    """
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    for section in REQUIRED_SECTIONS:
        if section not in text:
            findings.append(f"{path}: missing required section {section}")

    is_l3 = L3_DIR_MARKER in path.parts
    theory_min = THEORY_MIN_L3 if is_l3 else THEORY_MIN_L12
    chars_min = CHARS_MIN_L3 if is_l3 else CHARS_MIN_L12
    proto_theory_max = PROTO_INDEX_THEORY_MAX_L3 if is_l3 else PROTO_INDEX_THEORY_MAX_L12

    theory_score = sum(text.count(hint) for hint in THEORY_HINTS)
    boundary_score = sum(len(re.findall(pattern, text)) for pattern in BOUNDARY_PATTERNS)
    protocol_hits = len(re.findall(r"TS\s+3[68]\.\d+|§\d|Table\s+\d|协议定位|协议证据", text))
    chars = len(text)

    if chars < chars_min:
        findings.append(f"{path}: very short lesson ({chars} chars)")
    if theory_score < theory_min:
        findings.append(f"{path}: weak zero-foundation theory signals (score={theory_score})")
    if protocol_hits >= 20 and theory_score < proto_theory_max:
        findings.append(
            f"{path}: protocol-index risk (protocol_hits={protocol_hits}, theory_score={theory_score})"
        )
    if boundary_score >= 12:
        findings.append(f"{path}: too many deferral/boundary phrases (count={boundary_score})")

    # A lesson can be long but still thin if it has no concrete example language.
    if not re.search(r"手算例子|数值例子|教学例子|小型.*例子|例题", text):
        findings.append(f"{path}: missing concrete worked example marker")

    return findings


def iter_markdown(paths: list[Path]) -> list[Path]:
    """Collect lesson .md files, recursing into subdirectories.

    @brief   从路径列表中收集所有讲义 Markdown 文件（T*.md 模式）。
             递归遍历子目录以确保深层嵌套的讲义也能被覆盖，
             同时去重避免同一文件被多次审计。
    @param   paths  路径列表，可混合文件和目录。
    @return  按文件名排序的去重 Markdown 文件路径列表。
    @note    仅匹配 T*.md 模式——这是本项目的讲义命名约定。
             教训（2026-08-14 审核）：L2 M16 系列曾用 M16.x 命名，逃逸本审计
             数周（M 前缀不在 T*.md 匹配内）；已改名 T16.x 回归约定。
             命名约定即工具契约——新增讲义必须 T*.md，禁用 M 前缀文件名。
             另（2026-08-14 审核）：T 开头的概念笔记（Turbo_码/TB_传输块/TDL_
             信道模型等）会被 T*.md 误收为讲义——按 NON_LESSON_DIRS 排除
             concepts/audits/superpowers/L0 目录，与 audit_term_first_use.py
             的非讲义豁免口径（h/i/j）对齐。
    """
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            if not any(d in path.parts for d in NON_LESSON_DIRS):
                files.append(path)
        elif path.is_dir():
            files.extend(
                sorted(
                    p for p in path.rglob("T*.md")
                    if not any(d in p.parts for d in NON_LESSON_DIRS)
                )
            )
    return sorted(set(files))


def main() -> int:
    """
    @brief   讲义深度审计入口——检测讲义是否为真正的教学笔记而非协议索引。
    @usage   python audit_lesson_depth.py <paths...> [--strict]
    @args    paths    必选，待审计的 Markdown 讲义文件或目录路径。
             --strict 严格模式——存在发现时返回非零退出码；
                      默认模式下即使有发现也返回 0（仅报告分类结果）。
    @env     无外部依赖（仅标准库）
    @exit_code  在 --strict 模式下：0 = 无发现，1 = 存在深度不足的发现。
                在默认模式下：始终为 0（分类性审计，非阻断性）。
    @note    本审计为分类性（triage）审计，默认不阻断 CI。
             使用 --strict 可在质量门禁中将深度不足视为阻断条件。
             讲义文件的命名约定为 T*.md（T1.1, T2.3 等）。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return non-zero when triage findings are present",
    )
    args = parser.parse_args()

    findings: list[str] = []
    for path in iter_markdown(args.paths):
        findings.extend(audit_file(path))

    if findings:
        print("LESSON_DEPTH_AUDIT_TRIAGE")
        print("\n".join(findings))
        return 1 if args.strict else 0

    print("LESSON_DEPTH_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
