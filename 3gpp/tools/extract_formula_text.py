#!/usr/bin/env python3
"""
@file extract_formula_text.py
@brief 从 LibreOffice 导出的公式 SVG 中提取公式文本（agent 可读）。
       3GPP 文档的 OLE 公式以 wmf 嵌入（无 OMML 文本），经 libreoffice
       转 SVG 后，公式字符以 <text>/<tspan> 元素保留（含坐标）。
       本工具按坐标重组公式文本：y 分层识别上下标，x 排序拼接主行，
       并映射 Symbol 字体编码（U+F020-F0FF）为标准数学字符。
@date 2026-08-01
@usage python3 extract_formula_text.py --dir media_svg \
        [--output formula_text.json]
@args --dir       SVG 目录（默认 media_svg）。
@args --output    输出 JSON（公式名 → {text, layers}），默认 stdout 汇总。
@note 提取质量分级：含未映射字符或多层嵌套的公式标记为 complex，
       供上层决定是否保留 SVG 显示。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Symbol 字体标准映射（Adobe Symbol Encoding，U+F020-U+F0FF）
# 0x20-0x7E 区：ASCII 数学符号
SYMBOL_MAP = {
    0x20: " ", 0x21: "!", 0x22: "∀", 0x23: "#", 0x24: "∃", 0x25: "%",
    0x26: "∈", 0x27: "∋", 0x28: "(", 0x29: ")", 0x2A: "∗", 0x2B: "+",
    0x2C: ",", 0x2D: "−", 0x2E: ".", 0x2F: "/",
    0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 0x34: "4",
    0x35: "5", 0x36: "6", 0x37: "7", 0x38: "8", 0x39: "9",
    0x3A: ":", 0x3B: ";", 0x3C: "<", 0x3D: "=", 0x3E: ">", 0x3F: "?",
    0x40: "∝",
    # 希腊小写（0x41-0x5A）
    0x41: "α", 0x42: "β", 0x43: "χ", 0x44: "δ", 0x45: "ε", 0x46: "φ",
    0x47: "γ", 0x48: "η", 0x49: "ι", 0x4A: "ϕ", 0x4B: "κ", 0x4C: "λ",
    0x4D: "μ", 0x4E: "ν", 0x4F: "ο", 0x50: "π", 0x51: "θ", 0x52: "ρ",
    0x53: "σ", 0x54: "τ", 0x55: "υ", 0x56: "ς", 0x57: "ω", 0x58: "ξ",
    0x59: "ψ", 0x5A: "ζ",
    0x5B: "{", 0x5C: "|", 0x5D: "}", 0x5E: "~",
    # 希腊大写（0x61-0x7A）
    0x61: "Α", 0x62: "Β", 0x63: "Χ", 0x64: "Δ", 0x65: "Ε", 0x66: "Φ",
    0x67: "Γ", 0x68: "Η", 0x69: "Ι", 0x6A: "ϑ", 0x6B: "Κ", 0x6C: "Λ",
    0x6D: "Μ", 0x6E: "Ν", 0x6F: "Ο", 0x70: "Π", 0x71: "Θ", 0x72: "Ρ",
    0x73: "Σ", 0x74: "Τ", 0x75: "Υ", 0x76: "ς", 0x77: "Ω", 0x78: "Ξ",
    0x79: "Ψ", 0x7A: "Ζ",
    0x7B: "{", 0x7C: "|", 0x7D: "}", 0x7E: "~",
    # 数学符号区（0xA0-0xFF）
    0xA0: "€", 0xA1: "≤", 0xA2: "±", 0xA3: "≥", 0xA4: "×", 0xA5: "÷",
    0xA6: "↔", 0xA7: "←", 0xA8: "↑", 0xA9: "→", 0xAA: "↓", 0xAB: "°",
    0xAC: "±", 0xAD: "″", 0xAE: "≥", 0xAF: "×",
    0xB0: "∝", 0xB1: "∂", 0xB2: "•", 0xB3: "÷", 0xB4: "≠", 0xB5: "≡",
    0xB6: "≈", 0xB7: "…", 0xB8: "⏐", 0xB9: "⎯", 0xBA: "↵", 0xBB: "ℵ",
    0xBC: "ℶ", 0xBD: "ℷ", 0xBE: "ℸ", 0xBF: "⎛", 0xC0: "⎜", 0xC1: "⎝",
    0xC2: "⎡", 0xC3: "⎢", 0xC4: "⎣", 0xC5: "⎧", 0xC6: "⎨", 0xC7: "⎩",
    0xC8: "⎪", 0xC9: "⎫", 0xCA: "⎬", 0xCB: "⎭", 0xCC: "⎮", 0xCD: "⎯",
    0xCE: "⎰", 0xCF: "⎱",
    0xD0: "ℵ", 0xD1: "ℶ", 0xD2: "ℷ", 0xD3: "ℸ", 0xD4: "∧", 0xD5: "∨",
    0xD6: "∩", 0xD7: "∪", 0xD8: "∫", 0xD9: "∴", 0xDA: "∼", 0xDB: "≅",
    0xDC: "≈", 0xDD: "≠", 0xDE: "≡", 0xDF: "≤", 0xE0: "≥", 0xE1: "⊂",
    0xE2: "⊃", 0xE3: "⊄", 0xE4: "⊅", 0xE5: "⊆", 0xE6: "⊇", 0xE7: "⊕",
    0xE8: "⊗", 0xE9: "⊥", 0xEA: "⋅", 0xEB: "√", 0xEC: "√", 0xED: "⌠",
    0xEE: "∞", 0xEF: "⌡", 0xF0: "⌢", 0xF1: "◊", 0xF2: "◊", 0xF3: "→",
    0xF4: "↓", 0xF5: "↔", 0xF6: "⇒", 0xF7: "⇐", 0xF8: "⇔", 0xF9: "∀",
    0xFA: "∂", 0xFB: "∃", 0xFC: "∅", 0xFD: "∇", 0xFE: "∈", 0xFF: "∉",
}


def decode_symbol(text: str) -> tuple[str, bool]:
    """
    @brief 解码 Symbol 字体文本为数学字符。
    @param text  原始文本（含 U+F020-U+F0FF 码点）。
    @return      (解码文本, 是否含未映射字符)。
    """
    out = []
    unknown = False
    for ch in text:
        cp = ord(ch)
        if 0xF020 <= cp <= 0xF0FF:
            mapped = SYMBOL_MAP.get(cp - 0xF000)
            if mapped:
                out.append(mapped)
            else:
                out.append("?")
                unknown = True
        else:
            out.append(ch)
    return "".join(out), unknown


def extract_items(svg_text: str) -> list[tuple[float, float, str, bool]]:
    """
    @brief 提取 SVG 中的文本项（坐标 + 解码文本）。
    @param svg_text  SVG 文本。
    @return          [(x, y, 文本, 是否含未知字符), ...]。
    """
    items: list[tuple[float, float, str, bool]] = []
    for m in re.finditer(r"<text\b[^>]*>.*?</text>", svg_text, re.S):
        t = m.group(0)
        xm = re.search(r'\bx="([-0-9.]+)"', t)
        ym = re.search(r'\by="([-0-9.]+)"', t)
        if not (xm and ym):
            continue
        spans = re.findall(r"<tspan[^>]*>([^<]*)</tspan>", t)
        raw = "".join(spans)
        decoded, unknown = decode_symbol(raw)
        if decoded.strip():
            items.append((float(xm.group(1)), float(ym.group(1)), decoded, unknown))
    return items


def compose_formula(items: list[tuple[float, float, str, bool]]) -> tuple[str, int, bool, bool]:
    """
    @brief 按坐标重组公式文本（上下标感知）。
    @param items  文本项列表。
    @return       (重组文本, y 层数, 是否含未知字符, 是否不可靠)。
    @note 算法：y 聚类分层 → 主行（字符最多层）→ 按 x 顺序扫描全部项，
           主行项直接拼接，高于主行的层输出为 ^{...}（上标），
           低于主行的层输出为 _{...}（下标），并按 x 位置就近插入。
           不可靠判定：非主行层含 >3 字符（如矩阵行/多字符分数被误判
           为上下标）或含未知字符——此类公式保留 SVG 显示。
    """
    if not items:
        return "", 0, False, True
    # y 聚类分层：相邻 y 差 > 60 视为不同层（同行字符基线差通常 <60，
    # 上下标偏移通常 >80；阈值取中间值）
    ys_sorted = sorted(y for _, y, _, _ in items)
    layer_ids: dict[float, int] = {}
    cur = 0
    prev = ys_sorted[0]
    for y in ys_sorted:
        if y - prev > 60:
            cur += 1
        layer_ids[y] = cur
        prev = y
    layer_map: dict[int, list[tuple[float, str, bool]]] = {}
    for x, y, txt, unk in items:
        layer_map.setdefault(layer_ids[y], []).append((x, txt, unk))
    # 主行 = 字符数最多的层
    main_key = max(layer_map, key=lambda k: sum(len(t) for _, t, _ in layer_map[k]))
    unknown = any(u for _, _, _, u in items)
    # 按 x 合并扫描：主行直拼，上下标就近插入
    all_items = sorted(items, key=lambda v: (v[0], v[1]))
    out: list[str] = []
    for x, y, txt, _ in all_items:
        layer = layer_ids[y]
        if layer == main_key:
            out.append(txt)
        elif layer < main_key:
            out.append(f"^{{{txt}}}")
        else:
            out.append(f"_{{{txt}}}")
    text = "".join(out)
    # 不可靠判定：
    #   1) 含未知字符
    #   2) 非主行层含多字符（>3）——矩阵行/多字符分数被误判为上下标
    #   3) 聚类错乱特征：连续多个上下标标记（>3 个）或以上下标开头
    #      （主行选择错误时大量字符被当上下标）
    sup_count = len(re.findall(r"\^\{", text))
    sub_count = len(re.findall(r"_\{", text))
    unreliable = (
        unknown
        or any(
            sum(len(t) for _, t, _ in layer_map[k]) > 3 and k != main_key
            for k in layer_map
        )
        or (sup_count + sub_count) > 3
        or text.startswith(("^{", "_{"))
    )
    return text, len(layer_map), unknown, unreliable


def extract_file(path: Path) -> dict:
    """
    @brief 提取单个 SVG 的公式文本。
    @param path  SVG 文件路径。
    @return      {"text": 重组文本, "layers": y 层数, "unknown": 是否含未知字符}。
    """
    svg = path.read_text(encoding="utf-8")
    items = extract_items(svg)
    text, layers, unknown, unreliable = compose_formula(items)
    return {"file": path.name, "text": text, "layers": layers,
            "unknown": unknown, "unreliable": unreliable}


def main() -> int:
    """
    @brief 脚本入口：批量提取 SVG 公式文本。
    @usage python3 extract_formula_text.py --dir media_svg --output formula_text.json
    @args --dir     SVG 目录（默认 media_svg）。
    @args --output  输出 JSON 路径（默认打印汇总）。
    @exit_code 0 = 成功。
    """
    parser = argparse.ArgumentParser(description="Extract formula text from formula SVGs")
    parser.add_argument("--dir", default="media_svg", help="Directory of formula SVGs")
    parser.add_argument("--output", default=None, help="Output JSON path")
    args = parser.parse_args()

    svg_dir = Path(args.dir)
    results = [extract_file(f) for f in sorted(svg_dir.glob("*.svg"))]
    if args.output:
        Path(args.output).write_text(
            json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8"
        )
    simple = sum(1 for r in results if r["layers"] <= 1 and not r["unknown"])
    print(f"提取 {len(results)} 个公式: 简单(单层无未知) {simple}, 复杂 {len(results) - simple}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
