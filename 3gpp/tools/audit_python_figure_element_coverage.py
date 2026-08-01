#!/usr/bin/env python3
"""@file audit_python_figure_element_coverage.py
@brief 审计 Python 图片渲染脚本中的可见文本元素是否在讲义正文中得到了覆盖——
       与 body-equivalent 审计互补，深入到元素级别验证每个 label/title/表项
       都在正文中有对应描述。
@date 2026-07-22

相比 body-equivalent 检查（只确认"有等价块存在"），本审计更严格：
1. 用 AST 解析图片生成脚本，提取所有可见文本元素
2. 对每个元素检查其在对应讲义正文中是否可被检索到
3. 支持中英文术语别名表，允许中文正文覆盖英文脚本术语
4. 覆盖率不足（最多 4 个 term 中至少 1 个存在）即报缺失
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_LEDGER = Path("docs/audits/python_figure_to_body_content_migration.md")
RENDER_CALLS = {"text", "card", "centered", "draw_table", "box"}
NON_VISIBLE_KEYWORDS = {
    "anchor",
    "align",
    "direction",
    "embedded_color",
    "fill",
    "font",
    "gap",
    "language",
    "layout_engine",
    "outline",
    "radius",
    "spacing",
    "stroke_fill",
}
MIN_TOKEN_LEN = 2
SKIP_TEXTS = {
    "",
    "-",
    "#fff",
    "#ffffff",
    "white",
    "black",
}
ENGLISH_STOPWORDS = {
    "and",
    "or",
    "the",
    "a",
    "an",
    "to",
    "of",
    "in",
    "on",
    "for",
    "with",
    "by",
    "from",
    "is",
    "are",
    "as",
    "new",
    "old",
    "current",
    "optional",
}
TERM_ALIASES = {
    "accumulates": ("累加",),
    "access": ("访问",),
    "argmin": ("argmin",),
    "avoids": ("避免",),
    "bank": ("bank",),
    "banks": ("banks", "bank"),
    "connection": ("连接",),
    "debug": ("调试",),
    "descriptor": ("descriptor",),
    "edge": ("edge", "边"),
    "equal": ("一致", "等价"),
    "excludes": ("排除",),
    "forever": ("无限",),
    "hardware": ("硬件",),
    "hash": ("hash",),
    "keeps": ("保证", "保持"),
    "latch": ("锁存",),
    "matters": ("重要",),
    "message": ("message", "消息"),
    "min1": ("min1",),
    "min2": ("min2",),
    "object": ("对象",),
    "parallel": ("并行",),
    "replaces": ("替换",),
    "required": ("必须",),
    "schedule": ("schedule", "调度"),
    "sign": ("sign", "符号"),
    "target": ("目标",),
    "trace": ("trace",),
    "why": ("为什么",),
}


@dataclass(frozen=True)
class Finding:
    script: Path
    lesson: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.lesson}:{self.line}: {self.rule}: {self.script}: {self.message}"


@dataclass(frozen=True)
class Element:
    text: str
    line: int
    source: str


def normalize_text(text: str) -> str:
    """@brief  规范化文本：合并连续空白字符为单空格并去除首尾空白。
    @param  text  原始文本字符串。
    @return       规范化后的单行文本。"""
    return re.sub(r"\s+", " ", text).strip()


def flatten_strings(value: ast.AST) -> list[str]:
    """@brief  从 AST 节点值中递归提取所有字符串常量——无论是单字符串、
             f-string、列表、元组还是字典，所有嵌套字符串都会被扁平化输出。
    @param  value  AST 节点（常量为字符串或容器）。
    @return        提取出的字符串列表。
    @note   仅处理基本 Python 字面量形式，不支持复杂表达式或变量引用。"""
    if isinstance(value, ast.Constant) and isinstance(value.value, str):
        return [value.value]
    if isinstance(value, ast.JoinedStr):
        parts = []
        for item in value.values:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                parts.append(item.value)
        return ["".join(parts)] if parts else []
    if isinstance(value, (ast.List, ast.Tuple, ast.Set)):
        out: list[str] = []
        for item in value.elts:
            out.extend(flatten_strings(item))
        return out
    if isinstance(value, ast.Dict):
        out: list[str] = []
        for item in list(value.keys) + list(value.values):
            if item is not None:
                out.extend(flatten_strings(item))
        return out
    return []


def is_visible_text(text: str) -> bool:
    """@brief  判断提取出的文本是否属于"可见文本元素"——
             排除颜色值、纯数字标点、文件路径等非语义性字符串。
    @param  text  规范化后的文本字符串。
    @return       True 表示该文本应作为可见元素参与覆盖率检查。
    @note   至少包含一个字母或中文字符才被视为可见文本。"""
    text = normalize_text(text)
    if text in SKIP_TEXTS:
        return False
    if text.startswith("#") and re.fullmatch(r"#[0-9A-Fa-f]{3,8}", text):
        return False
    if re.fullmatch(r"[(),.\d\s-]+", text):
        return False
    if text.endswith((".png", ".py", ".ttf", ".ttc")):
        return False
    return bool(re.search(r"[A-Za-z\u4e00-\u9fff]", text))


def call_name(node: ast.Call) -> str:
    """@brief  从 Call AST 节点中提取函数名（支持 `func()` 和 `obj.method()` 两种形式）。
    @param  node  ast.Call 节点。
    @return       函数名或方法名；无法识别则返回空字符串。"""
    func = node.func
    if isinstance(func, ast.Attribute):
        return func.attr
    if isinstance(func, ast.Name):
        return func.id
    return ""


def extract_elements(script: Path) -> list[Element]:
    """@brief  用 AST 解析图片生成脚本，提取所有可见文本元素——
             追踪渲染调用（text/card/draw_table 等）中的参数和
             特殊赋值语句（title/subtitle/bodies 等）中的值。
    @param  script  图片生成 Python 脚本路径。
    @return         去重后的可见文本元素列表。
    @note   会过滤 NON_VISIBLE_KEYWORDS 中的非视觉参数（如 font/gap/fill）。
    @throws SyntaxError  脚本存在语法错误时被上层捕获。"""
    tree = ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
    elements: list[Element] = []

    for node in ast.walk(tree):
        strings: list[str] = []
        source = type(node).__name__
        if isinstance(node, ast.Call) and call_name(node) in RENDER_CALLS:
            source = f"call:{call_name(node)}"
            for arg in node.args:
                strings.extend(flatten_strings(arg))
            for keyword in node.keywords:
                if keyword.arg in NON_VISIBLE_KEYWORDS:
                    continue
                strings.extend(flatten_strings(keyword.value))
        elif isinstance(node, ast.Assign):
            target_names = {target.id for target in node.targets if isinstance(target, ast.Name)}
            if any(name in target_names for name in {"title", "subtitle", "titles", "bodies", "rows", "headers", "fsm_titles", "fsm_bodies"}):
                source = "assignment"
                strings.extend(flatten_strings(node.value))

        for text in strings:
            text = normalize_text(text)
            if is_visible_text(text):
                elements.append(Element(text=text, line=getattr(node, "lineno", 1), source=source))

    return dedupe_elements(elements)


def dedupe_elements(elements: list[Element]) -> list[Element]:
    """@brief  去重元素列表，保留首次出现（按文本的小写形式判重）。
    @param  elements  原始元素列表。
    @return           去重后的元素列表，保持首次出现顺序。
    @note   大小写不敏感，避免同一术语的不同大小写被重复审计。"""
    out: list[Element] = []
    seen: set[str] = set()
    for element in elements:
        key = element.text.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(element)
    return out


def split_terms(text: str) -> list[str]:
    """@brief  将元素文本拆分为独立的搜索词条——
             中文字符按单字/词组分割，英文按单词和数字分割，过滤停用词和过短词。
    @param  text  元素文本字符串。
    @return       有意义的搜索词条列表。
    @note   英文停用词（and/the/of 等）被过滤，长度 <2 的词也被排除。"""
    text = text.replace("/", " ")
    raw_terms = re.findall(r"[A-Za-z][A-Za-z0-9_-]*|[0-9]+(?:\.[0-9]+)*|[\u4e00-\u9fff]+", text)
    terms: list[str] = []
    for term in raw_terms:
        clean = term.strip(".,;:()[]{}")
        if len(clean) < MIN_TOKEN_LEN:
            continue
        if clean.lower() in ENGLISH_STOPWORDS:
            continue
        terms.append(clean)
    return terms


def term_present(term: str, lesson_text: str) -> bool:
    """@brief  检查单个词条（含别名）是否在讲义正文中存在——
             英文词条使用词边界匹配，中文词条使用子串匹配。
    @param  term         原始词条。
    @param  lesson_text  讲义全文文本。
    @return              True 表示词条或至少一个别名存在于正文中。"""
    candidates = (term,) + TERM_ALIASES.get(term.lower(), ())
    return any(candidate_present(candidate, lesson_text) for candidate in candidates)


def candidate_present(term: str, lesson_text: str) -> bool:
    """@brief  \u5e95\u5c42\u8bcd\u6761\u5b58\u5728\u6027\u68c0\u67e5\u2014\u2014\u533a\u5206\u4e2d\u82f1\u6587\u7684\u5339\u914d\u7b56\u7565

    @param  term         \u5019\u9009\u8bcd\u6761\uff08\u539f\u8bcd\u6216\u522b\u540d\uff09
    @param  lesson_text  \u8bb2\u4e49\u5168\u6587\u6587\u672c
    @return              True \u8868\u793a\u8bcd\u6761\u5728\u8bb2\u4e49\u4e2d\u88ab\u627e\u5230
    @note   \u4e2d\u6587\u4f7f\u7528\u5b50\u4e32\u5339\u914d\uff08\u4e2d\u6587\u8bcd\u8fb9\u754c\u5929\u7136\u660e\u786e\uff09\uff1b
             \u82f1\u6587\u4f7f\u7528\u5b8c\u6574\u7684\u8bcd\u8fb9\u754c\u6b63\u5219\uff08\u9632\u6b62 "re" \u8bef\u5339\u914d "request"\uff09"""
    if re.search(r"[\u4e00-\u9fff]", term):
        return term in lesson_text
    return re.search(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", lesson_text, re.IGNORECASE) is not None


def element_covered(element: Element, lesson_text: str) -> bool:
    """@brief  \u5224\u65ad\u4e00\u4e2a\u53ef\u89c1\u6587\u672c\u5143\u7d20\u662f\u5426\u88ab\u8bb2\u4e49\u6b63\u6587\u8986\u76d6

    \u82e5\u5143\u7d20\u5168\u6587\u76f4\u63a5\u51fa\u73b0\u5728\u8bb2\u4e49\u4e2d\u5219\u76f4\u63a5\u901a\u8fc7\uff0c\u5426\u5219\u5c06\u5176\u62c6\u5206\u4e3a\u8bcd\u6761\uff0c
    \u6309"\u81f3\u5c11 1 \u4e2a\u6709\u6548 term \u88ab\u8986\u76d6\uff08\u4e0a\u9650 4 \u4e2a\uff09"\u7684\u5bbd\u677e\u7b56\u7565\u5224\u5b9a\u3002

    @param  element      \u5f85\u68c0\u67e5\u7684\u53ef\u89c1\u6587\u672c\u5143\u7d20
    @param  lesson_text  \u8bb2\u4e49\u5168\u6587\u6587\u672c
    @return              True \u8868\u793a\u5143\u7d20\u5df2\u88ab\u6b63\u6587\u8986\u76d6"""
    text = element.text
    if text in lesson_text:
        return True
    terms = split_terms(text)
    if not terms:
        return True
    required = max(1, min(len(terms), 4))
    present = sum(1 for term in terms if term_present(term, lesson_text))
    return present >= required


def audit_pair(script: Path, lesson: Path) -> list[Finding]:
    """@brief  对单个 (脚本, 讲义) 对执行元素级覆盖率审计。
    @param  script  图片生成 Python 脚本路径。
    @param  lesson  对应的讲义 Markdown 文件路径。
    @return         覆盖率不足的元素 Findings 列表；空列表表示全覆盖。"""
    findings: list[Finding] = []
    lesson_text = lesson.read_text(encoding="utf-8")
    for element in extract_elements(script):
        if not element_covered(element, lesson_text):
            findings.append(
                Finding(
                    script=script,
                    lesson=lesson,
                    line=element.line,
                    rule="missing_visible_text_element",
                    message=f"{element.text!r} from {element.source} is not covered in lesson body",
                )
            )
    return findings


def parse_ledger_rows(ledger: Path) -> list[tuple[Path, Path]]:
    """@brief  从迁移台账中解析所有标记为 `body_text_represented` 状态的
             脚本-讲义配对，用于批量元素覆盖审计。
    @param  ledger  迁移台账文件路径。
    @return         (脚本路径, 讲义路径) 二元组列表，去重排序。
    @note   仅提取状态包含 `body_text_represented` 的行，
             脚本列支持逗号分隔的多脚本值。"""
    rows: list[tuple[Path, Path]] = []
    if not ledger.exists():
        return rows
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        lesson = cells[0].strip("`")
        scripts = cells[2].strip("`")
        status = cells[4]
        if "body_text_represented" not in status:
            continue
        for script in [part.strip() for part in scripts.split(",")]:
            if script.startswith("tools/figures/") and script.endswith(".py"):
                rows.append((Path(script), Path(lesson)))
    return sorted(set(rows))


def audit_ledger(ledger: Path = DEFAULT_LEDGER) -> list[Finding]:
    """@brief  按迁移台账全量执行元素覆盖审计——读取所有 body_text_represented 行，
             对每对 (脚本, 讲义) 调用 audit_pair 并汇总。
    @param  ledger  迁移台账文件路径（默认指向标准台账）。
    @return         所有覆盖不足的 Findings 汇总列表。"""
    findings: list[Finding] = []
    for script, lesson in parse_ledger_rows(ledger):
        if not script.exists() or not lesson.exists():
            continue
        findings.extend(audit_pair(script, lesson))
    return findings


def main(argv: list[str] | None = None) -> int:
    """@brief    脚本入口：审计图片渲染脚本的可见文本元素在讲义正文中的覆盖率。
    @param    argv  命令行参数列表（sys.argv）。
    @usage    python audit_python_figure_element_coverage.py [SCRIPT LESSON]  (显式模式)
              python audit_python_figure_element_coverage.py [--ledger <path>] [--summary]  (台账模式)
    @args     SCRIPT LESSON  显式指定 (脚本, 讲义) 对进行单对审计。
    @args     --ledger <path>  迁移台账路径（默认 docs/audits/python_figure_to_body_content_migration.md）。
    @args     --summary        按讲义路径分组汇总输出。
    @exit_code                 0 = 全覆盖；1 = 存在未覆盖元素。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Optional explicit script/lesson pair: SCRIPT LESSON")
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER), help="Migration ledger to audit")
    parser.add_argument("--summary", action="store_true", help="Print findings grouped by lesson path")
    args = parser.parse_args(argv)

    if args.paths:
        if len(args.paths) != 2:
            parser.error("explicit mode requires exactly SCRIPT LESSON")
        findings = audit_pair(Path(args.paths[0]), Path(args.paths[1]))
    else:
        findings = audit_ledger(Path(args.ledger))

    if findings:
        print(f"PYTHON_FIGURE_ELEMENT_COVERAGE_AUDIT_FAIL count={len(findings)}")
        if args.summary:
            counts: dict[Path, int] = {}
            for finding in findings:
                counts[finding.lesson] = counts.get(finding.lesson, 0) + 1
            for lesson, count in sorted(counts.items(), key=lambda item: (-item[1], str(item[0]))):
                print(f"{lesson}: {count}")
        else:
            for finding in findings:
                print(finding.format())
        return 1
    print("PYTHON_FIGURE_ELEMENT_COVERAGE_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
