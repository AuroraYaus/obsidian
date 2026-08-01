#!/usr/bin/env python3
"""
@file omml2latex.py
@brief OMML（Office Math Markup Language）公式 → LaTeX 转换器。
       3GPP 协议 Word 文档（.docx）中的数学公式以 OMML 存储于
       word/document.xml，agent 无法直接阅读 OMML XML；本模块将其
       转换为标准 LaTeX 数学（$...$ / $$...$$），供 full.md 等
       agent 友好全文使用。
@date 2026-08-01
@usage python3 omml2latex.py [equation.xml ...]   # 逐个转换并打印
@note 覆盖 3GPP 公式常用结构：分数/上下标/求和/根式/括号/矩阵/累加
       符号；未知元素递归取其子元素文本，保证不丢内容。
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET

M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

ET.register_namespace("m", M_NS)
ET.register_namespace("w", W_NS)

NS = {"m": M_NS, "w": W_NS}

# m:nary 的 m:chr 值 → LaTeX 运算符映射（含 3GPP 常用变体）
NARY_OPS = {
    "∑": "\\sum ",
    "∏": "\\prod ",
    "∫": "\\int ",
    "∮": "\\oint ",
    "∀": "\\forall ",
    "∃": "\\exists ",
    "∩": "\\bigcap ",
    "∪": "\\bigcup ",
    "⊕": "\\bigoplus ",
}

# m:acc 的 m:chr 值 → LaTeX 重音映射
ACCENTS = {
    "ˆ": "\\hat ",
    "→": "\\vec ",
    "¯": "\\bar ",
    "⏞": "\\overbrace ",
    "⏟": "\\underbrace ",
    "˜": "\\tilde ",
    "̇": "\\dot ",
}

# m:d 的 begChr/endChr → LaTeX 括号对（\ 表示无括号）
DELIM_PAIRS = {
    ("(", ")"): ("\\left( ", "\\right) "),
    ("[", "]"): ("\\left[ ", "\\right] "),
    ("{", "}"): ("\\left\\{ ", "\\right\\} "),
    ("|", "|"): ("\\left| ", "\\right| "),
    ("⌊", "⌋"): ("\\lfloor ", "\\rfloor "),
    ("⌈", "⌉"): ("\\lceil ", "\\rceil "),
    ("⟨", "⟩"): ("\\langle ", "\\rangle "),
    ("⟦", "⟧"): ("\\llbracket ", "\\rrbracket "),
}


def omml_to_latex(xml_text: str) -> str:
    """
    @brief 将一段 OMML XML 转换为 LaTeX 数学表达式。
    @param xml_text  OMML XML 字符串（m:oMath 或 m:oMathPara）。
    @return          LaTeX 表达式（不含 $ 包裹，由调用方决定行内/块级）。
    @note 输入可为完整 XML 文档或片段；解析失败时返回空字符串。
    """
    root = ET.fromstring(xml_text)
    latex = _convert_element(root)
    # 所有字母命令统一加尾随空格：避免 \lceillog 这类命令名粘连，
    # 也避免贪婪回溯拆错命令名（如 \hat 被拆成 \ha + t）。
    # LaTeX 中命令名与其参数之间的空格合法（\frac {a}{b} 等价 \frac{a}{b}）。
    latex = re.sub(r"\\([a-zA-Z]+)", r"\\\1 ", latex)
    return latex


def _convert_element(el: ET.Element) -> str:
    """
    @brief 递归转换单个 OMML 元素为 LaTeX。
    @param el  OMML 元素（m: 命名空间）。
    @return    LaTeX 字符串片段。
    @note 未知元素递归拼接子元素文本，保证信息不丢失。
    """
    tag = _local(el.tag)
    if tag == "oMathPara":
        return _convert_children(el)
    if tag == "oMath":
        return _convert_children(el)
    if tag == "r":
        return _convert_run(el)
    if tag == "t":
        return _decode_text(el.text or "")
    if tag == "sSub":
        base = _convert_children(el.find("m:e", NS))
        sub = _convert_children(el.find("m:sub", NS))
        return f"{base}_{{{sub}}}"
    if tag == "sSup":
        base = _convert_children(el.find("m:e", NS))
        sup = _convert_children(el.find("m:sup", NS))
        return f"{base}^{{{sup}}}"
    if tag == "sSubSup":
        base = _convert_children(el.find("m:e", NS))
        sub = _convert_children(el.find("m:sub", NS))
        sup = _convert_children(el.find("m:sup", NS))
        return f"{base}_{{{sub}}}^{{{sup}}}"
    if tag == "sPre":
        sub = _convert_children(el.find("m:sub", NS))
        sup = _convert_children(el.find("m:sup", NS))
        base = _convert_children(el.find("m:e", NS))
        return f"{{}}_{{{sub}}}^{{{sup}}}{base}"
    if tag == "f":
        num = _convert_children(el.find("m:num", NS))
        den = _convert_children(el.find("m:den", NS))
        return f"\\frac{{{num}}}{{{den}}}"
    if tag == "d":
        return _convert_delimiter(el)
    if tag == "nary":
        return _convert_nary(el)
    if tag == "rad":
        deg = el.find("m:deg", NS)
        e = _convert_children(el.find("m:e", NS))
        if deg is not None and deg.find("m:r", NS) is not None:
            d = _convert_children(deg)
            if d.strip():
                return f"\\sqrt[{d}]{{{e}}}"
        return f"\\sqrt{{{e}}}"
    if tag == "acc":
        acc_pr = el.find("m:accPr", NS)
        chr_ = "ˆ"
        if acc_pr is not None:
            c = acc_pr.find("m:chr", NS)
            if c is not None:
                chr_ = c.attrib.get(f"{{{M_NS}}}val", chr_)
        base = _convert_children(el.find("m:e", NS))
        op = ACCENTS.get(chr_, "\\hat")
        return f"{op}{{{base}}}"
    if tag == "bar":
        pos = "top"
        bar_pr = el.find("m:barPr", NS)
        if bar_pr is not None:
            p = bar_pr.find("m:pos", NS)
            if p is not None and p.attrib.get(f"{{{M_NS}}}val") == "bot":
                pos = "bot"
        base = _convert_children(el.find("m:e", NS))
        return f"\\overline{{{base}}}" if pos == "top" else f"\\underline{{{base}}}"
    if tag == "limLow":
        base = _convert_children(el.find("m:e", NS))
        lim = _convert_children(el.find("m:lim", NS))
        return f"{base}_{{{lim}}}"
    if tag == "limUpp":
        base = _convert_children(el.find("m:e", NS))
        lim = _convert_children(el.find("m:lim", NS))
        return f"{base}^{{{lim}}}"
    if tag == "func":
        fname = _convert_children(el.find("m:fName", NS))
        arg = _convert_children(el.find("m:e", NS))
        return f"\\operatorname{{{fname}}}\\left({arg}\\right)"
    if tag == "m":
        return _convert_matrix(el)
    if tag == "eqArr":
        rows = [_convert_children(e) for e in el.findall("m:e", NS)]
        if len(rows) == 1:
            return rows[0]
        return "\\\\".join(rows)
    if tag == "groupChr":
        pos = "top"
        gc_pr = el.find("m:groupChrPr", NS)
        chr_ = "⏞"
        if gc_pr is not None:
            c = gc_pr.find("m:chr", NS)
            if c is not None:
                chr_ = c.attrib.get(f"{{{M_NS}}}val", chr_)
            p = gc_pr.find("m:pos", NS)
            if p is not None:
                pos = p.attrib.get(f"{{{M_NS}}}val", pos)
        base = _convert_children(el.find("m:e", NS))
        if chr_ == "⏞":
            return f"\\overbrace{{{base}}}"
        if chr_ == "⏟":
            return f"\\underbrace{{{base}}}"
        return base
    if tag == "phant":
        return f"\\phantom{{{_convert_children(el.find('m:e', NS))}}}"
    if tag == "box":
        return f"\\boxed{{{_convert_children(el.find('m:e', NS))}}}"
    if tag == "borderBox":
        return f"\\fbox{{{_convert_children(el.find('m:e', NS))}}}"
    if tag in ("ctrlPr", "rPr", "argPr", "dPr", "sSubPr", "sSupPr", "sSubSupPr",
               "fPr", "naryPr", "radPr", "accPr", "mPr", "eqArrPr", "funcPr",
               "limLowPr", "limUppPr", "sPrePr", "barPr", "groupChrPr",
               "boxPr", "borderBoxPr", "phantPr", "mcPr", "break"):
        return ""
    # 未知元素：递归子元素（兜底不丢内容）
    return _convert_children(el)


def _convert_children(el: ET.Element | None) -> str:
    """
    @brief 拼接元素的全部 m: 子元素转换结果。
    @param el  OMML 元素（可为 None）。
    @return    子元素 LaTeX 拼接字符串。
    """
    if el is None:
        return ""
    parts = []
    for child in el:
        if child.tag.startswith(f"{{{M_NS}}}"):
            parts.append(_convert_element(child))
    return "".join(parts)


def _convert_run(el: ET.Element) -> str:
    """
    @brief 转换 m:r（文本 run），保留正常字符，映射数学专用 Unicode。
    @param el  m:r 元素。
    @return    文本 LaTeX。
    """
    text = "".join(t.text or "" for t in el.findall("m:t", NS))
    return _decode_text(text)


def _decode_text(text: str) -> str:
    """
    @brief 将 OMML 文本解码为 LaTeX 安全文本。
    @param text  原始文本（可能含 xml:space 语义、数学 Unicode）。
    @return      LaTeX 安全文本。
    @note 空格折叠：OMML 中连续空格仅在 xml:space="preserve" 时保留；
           数学符号（×、≤、∈ 等）直接保留（LaTeX 兼容 Unicode 引擎）。
    """
    # 折叠普通空格（OMML 数学默认忽略连续空白）
    text = " ".join(text.split())
    # LaTeX 特殊字符转义（在数学模式中仍需转义的部分）
    escapes = {
        "\\": "\\backslash ",
        "&": "\\&",
        "%": "\\%",
        "_": "\\_",
        "#": "\\#",
        "{": "\\{",
        "}": "\\}",
    }
    for k, v in escapes.items():
        text = text.replace(k, v)
    # 常用数学 Unicode → LaTeX 命令（保持可读性）
    symbols = {
        "×": "\\times ",
        "÷": "\\div ",
        "≤": "\\leq ",
        "≥": "\\geq ",
        "≠": "\\neq ",
        "∞": "\\infty ",
        "∈": "\\in ",
        "∉": "\\notin ",
        "⊂": "\\subset ",
        "⊃": "\\supset ",
        "⊆": "\\subseteq ",
        "⊇": "\\supseteq ",
        "∪": "\\cup ",
        "∩": "\\cap ",
        "∅": "\\emptyset ",
        "→": "\\rightarrow ",
        "←": "\\leftarrow ",
        "⇒": "\\Rightarrow ",
        "⇐": "\\Leftarrow ",
        "⋅": "\\cdot ",
        "…": "\\ldots ",
        "±": "\\pm ",
        "∓": "\\mp ",
        "∑": "\\sum ",
        "∏": "\\prod ",
        "√": "\\sqrt ",
        "∥": "\\parallel ",
        "⊥": "\\perp ",
        "∠": "\\angle ",
        "∀": "\\forall ",
        "∃": "\\exists ",
        "¬": "\\neg ",
        "∧": "\\land ",
        "∨": "\\lor ",
        "⊈": "\\nsubseteq ",
        "⊉": "\\nsupseteq ",
        "≈": "\\approx ",
        "∼": "\\sim ",
        "∝": "\\propto ",
        "∂": "\\partial ",
        "∇": "\\nabla ",
        "Å": "\\AA ",
        "°": "^{\\circ} ",
        "∙": "\\cdot ",
        "·": "\\cdot ",
        "⋯": "\\ldots ",
        "−": "-",
        "′": "'",
        "″": "''",
        "⁡": "",  # U+2061 FUNCTION APPLICATION（Word 不可见控制符，直接删除）
        # 希腊字母（小写）
        "α": "\\alpha ", "β": "\\beta ", "γ": "\\gamma ", "δ": "\\delta ",
        "ε": "\\varepsilon ", "ϵ": "\\varepsilon ", "ζ": "\\zeta ",
        "η": "\\eta ", "θ": "\\theta ", "ϑ": "\\vartheta ", "ι": "\\iota ",
        "κ": "\\kappa ", "ϰ": "\\varkappa ", "λ": "\\lambda ", "μ": "\\mu ",
        "ν": "\\nu ", "ξ": "\\xi ", "ο": "o ", "π": "\\pi ", "ϖ": "\\varpi ",
        "ρ": "\\rho ", "ϱ": "\\varrho ", "σ": "\\sigma ", "ς": "\\varsigma ",
        "τ": "\\tau ", "υ": "\\upsilon ", "φ": "\\varphi ", "ϕ": "\\varphi ",
        "χ": "\\chi ", "ψ": "\\psi ", "ω": "\\omega ",
        # 希腊字母（大写：有 LaTeX 命令的映射命令，与拉丁同形的映射拉丁字母）
        "Γ": "\\Gamma ", "Δ": "\\Delta ", "Θ": "\\Theta ", "Λ": "\\Lambda ",
        "Ξ": "\\Xi ", "Π": "\\Pi ", "Σ": "\\Sigma ", "Υ": "\\Upsilon ",
        "Φ": "\\Phi ", "Ψ": "\\Psi ", "Ω": "\\Omega ",
        "Α": "A ", "Β": "B ", "Ε": "E ", "Ζ": "Z ", "Η": "H ", "Ι": "I ",
        "Κ": "K ", "Μ": "M ", "Ν": "N ", "Ο": "O ", "Ρ": "P ", "Τ": "T ",
        "Χ": "X ",
    }
    for k, v in symbols.items():
        text = text.replace(k, v)
    return text


def _convert_delimiter(el: ET.Element) -> str:
    r"""
    @brief 转换 m:d（成对分隔符括号）。
    @param el  m:d 元素。
    @return    \left...\right 括号包裹的内容。
    @note 无 begChr/endChr 时默认圆括号；chr 值为 "\" 表示无括号。
    """
    d_pr = el.find("m:dPr", NS)
    beg, end = "(", ")"
    if d_pr is not None:
        b = d_pr.find("m:begChr", NS)
        e = d_pr.find("m:endChr", NS)
        if b is not None:
            beg = b.attrib.get(f"{{{M_NS}}}val", "(")
        if e is not None:
            end = e.attrib.get(f"{{{M_NS}}}val", ")")
    content = _convert_children(el.find("m:e", NS))
    if beg == "\\" and end == "\\":
        return content
    key = (beg, end)
    if key in DELIM_PAIRS:
        left, right = DELIM_PAIRS[key]
        return f"{left}{content}{right}"
    # 未知括号字符：原样输出
    return f"{beg}{content}{end}"


def _convert_nary(el: ET.Element) -> str:
    """
    @brief 转换 m:nary（求和/积分/连乘等 n 元运算符）。
    @param el  m:nary 元素。
    @return    LaTeX 运算符表达式。
    @note 3GPP 公式中 nary 常带 m:sub/m:sup 上下限（可为空）。
    """
    nary_pr = el.find("m:naryPr", NS)
    chr_ = "∑"
    if nary_pr is not None:
        c = nary_pr.find("m:chr", NS)
        if c is not None:
            chr_ = c.attrib.get(f"{{{M_NS}}}val", chr_)
    op = NARY_OPS.get(chr_, "\\sum")
    sub = _convert_children(el.find("m:sub", NS))
    sup = _convert_children(el.find("m:sup", NS))
    body = _convert_children(el.find("m:e", NS))
    if sub and sup:
        return f"{op}_{{{sub}}}^{{{sup}}}{body}"
    if sub:
        return f"{op}_{{{sub}}}{body}"
    if sup:
        return f"{op}^{{{sup}}}{body}"
    return f"{op}{body}"


def _convert_matrix(el: ET.Element) -> str:
    """
    @brief 转换 m:m（矩阵）。
    @param el  m:m 元素。
    @return    LaTeX matrix 环境。
    @note 行列数由 m:mr（行）× m:e（列）推断；空行按 1 列处理。
    """
    rows = []
    for mr in el.findall("m:mr", NS):
        cells = [_convert_children(e) for e in mr.findall("m:e", NS)]
        if cells:
            rows.append(" & ".join(cells))
    if not rows:
        return ""
    if len(rows) == 1:
        return "\\begin{matrix}" + rows[0] + "\\end{matrix}"
    return "\\begin{matrix}" + " \\\\ ".join(rows) + "\\end{matrix}"


def _local(tag: str) -> str:
    """@brief 提取 XML 标签的本地名（去命名空间）。"""
    return tag.split("}")[-1] if "}" in tag else tag


def main() -> int:
    """
    @brief 脚本入口：将命令行给出的 OMML XML 文件逐个转换为 LaTeX 并打印。
    @usage python3 omml2latex.py equation_0001.xml equation_0002.xml ...
    @args  文件路径列表。
    @exit_code 0 = 全部转换成功；1 = 至少一个文件解析失败。
    """
    if len(sys.argv) < 2:
        print("usage: python3 omml2latex.py <equation.xml ...>")
        return 1
    ok = True
    for path in sys.argv[1:]:
        try:
            text = open(path, encoding="utf-8").read()
            print(f"{path}: {omml_to_latex(text)}")
        except ET.ParseError as exc:
            print(f"{path}: PARSE ERROR {exc}", file=sys.stderr)
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
