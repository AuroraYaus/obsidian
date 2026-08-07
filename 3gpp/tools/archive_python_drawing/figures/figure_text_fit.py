#!/usr/bin/env python3
"""
@file figure_text_fit.py
@brief PIL 教学图渲染的文本排版工具 — 自动换行、CJK 检测、字体加载
@date 2026-07-19

为 tools/figures/render_*.py 提供文本排版基础能力：
- wrap_text()    — 按像素宽度自动换行（支持中英文混排、超长 token 拆分）
- text_width()   — 计算文本像素宽度
- font()         — 加载 CJK 兼容字体（Noto Sans CJK → DejaVu Sans 回退）

核心难点：中文没有空格分词，需要逐字符判断是否超出宽度，
同时处理英文单词的完整换行（不截断单词）和中文标点的悬挂处理。

@note  依赖 Pillow (PIL) 库，字体文件需系统中已安装 Noto Sans CJK 或 DejaVu Sans。
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Protocol

from PIL import ImageFont


class TextMeasure(Protocol):
    """
    @brief 文本测量协议 — 任何具有 textbbox 方法的对象

    PIL 的 ImageDraw.Draw 对象满足此协议，用于计算文本的包围盒。
    使用 Protocol 而非具体类型，便于测试时注入 mock 对象。
    """
    def textbbox(self, xy, text: str, font=None):
        """ @brief 返回文本的包围盒 (left, top, right, bottom)。
            @param xy 文本起始坐标 (x, y)。
            @param text 待测量的文本字符串。
            @param font 字体对象（可选）。
            @return 文本包围盒四元组。
        """
        ...


# 将文本拆分为 token 的规则（英文单词、空格、换行、单字符）
TOKEN_RE = re.compile(r"[A-Za-z0-9_./'()+\[\]=:;-]+|[ \t]+|\n|.")

# 检测 CJK 字符的正则（Unicode 中日韩统一表意文字区间）
CJK_RE = re.compile(r"[㐀-鿿]")

# 终端标点集合（中英文），用于 rebalance_short_final_line 的尾行调整
TERMINAL_PUNCTUATION = set("。，、；：？！,.!?;:")


def text_width(draw: TextMeasure, text: str, fnt) -> int:
    """
    @brief 计算文本在当前字体下的像素宽度

    @param draw  实现了 TextMeasure 协议的绘图对象（如 ImageDraw.Draw）
    @param text  待测量的文本字符串
    @param fnt   PIL 字体对象
    @return      文本的像素宽度
    """
    bbox = draw.textbbox((0, 0), text, font=fnt)
    return bbox[2] - bbox[0]


def split_oversize_token(draw: TextMeasure, token: str, fnt, width: int) -> list[str]:
    """
    @brief 将超长 token 按像素宽度拆分为多个片段

    当单个 token（如长 URL 或无空格的中文长字符串）超过给定宽度时，
    逐字符回退找到可容纳的最长前缀，递归拆分剩余部分。

    @param draw   文本测量对象
    @param token  待拆分的超长 token
    @param fnt    字体对象
    @param width  最大像素宽度
    @return       拆分后的片段列表
    """
    parts: list[str] = []
    remaining = token
    while remaining and text_width(draw, remaining, fnt) > width:
        split = len(remaining) - 1
        while split > 1 and text_width(draw, remaining[:split], fnt) > width:
            split -= 1
        parts.append(remaining[:split])
        remaining = remaining[split:]
    if remaining:
        parts.append(remaining)
    return parts


def visual_units(text: str) -> int:
    """
    @brief 统计文本中"视觉单位"的数量（CJK 字符 + 终端标点）

    用于 rebalance_short_final_line 判断尾行是否过短需要调整。
    CJK 字符是方形的，每个占一个视觉单位；标点同理。

    @param text  待统计的文本
    @return      视觉单位计数
    """
    return sum(1 for ch in text if CJK_RE.match(ch) or ch in TERMINAL_PUNCTUATION)


def rebalance_short_final_line(lines: list[str]) -> list[str]:
    """
    @brief 调整过短的尾行 — 将前一行末尾的字符借到尾行

    当最后一行过短（如仅有一个标点符号结尾）时，从前一行末尾
    回借 CJK 字符或标点，使尾行至少包含 3 个视觉单位。
    避免中文排版中"孤字成行"的不良视觉效果。

    @param lines  换行后的文本行列表
    @return       调整后的行列表
    """
    if len(lines) < 2:
        return lines

    final = lines[-1].strip()
    if not final:
        return lines

    has_ascii_word = any(ch.isascii() and ch.isalnum() for ch in final)
    if has_ascii_word and not all(ch in TERMINAL_PUNCTUATION for ch in final):
        return lines

    if not all(ch in TERMINAL_PUNCTUATION for ch in final) and visual_units(final) > 2:
        return lines

    previous = lines[-2].rstrip()
    while previous and visual_units(final) < 3:
        ch = previous[-1]
        if not (CJK_RE.match(ch) or ch in TERMINAL_PUNCTUATION):
            break
        previous = previous[:-1].rstrip()
        final = ch + final

    if previous and final != lines[-1].strip():
        lines[-2] = previous
        lines[-1] = final
    return lines


def wrap_text(draw: TextMeasure, text: str, fnt, width: int) -> list[str]:
    """
    @brief 按像素宽度自动换行（支持中英文混排）

    核心算法：
    1. tokenize — 将文本按 TOKEN_RE 拆分为英文单词、空格、换行、单字符
    2. 逐 token 拼接，当累积宽度超过 width 时换行
    3. 换行符 "\\n" 强制换行
    4. 超长 token 用 split_oversize_token 强制拆分
    5. 最后用 rebalance_short_final_line 调整尾行

    @param draw   文本测量对象（ImageDraw.Draw 或 mock）
    @param text   待换行的原始文本
    @param fnt    PIL 字体对象
    @param width  行最大像素宽度
    @return       换行后的文本行列表
    """
    lines: list[str] = []
    current = ""
    for token in TOKEN_RE.findall(text):
        if token == "\n":
            lines.append(current)
            current = ""
            continue

        candidate = current + token
        if text_width(draw, candidate, fnt) <= width or not current:
            current = candidate
            if text_width(draw, current, fnt) > width:
                parts = split_oversize_token(draw, current, fnt, width)
                lines.extend(parts[:-1])
                current = parts[-1] if parts else ""
            continue

        if current.strip():
            lines.append(current.rstrip())
        current = token.lstrip()
        if text_width(draw, current, fnt) > width:
            parts = split_oversize_token(draw, current, fnt, width)
            lines.extend(parts[:-1])
            current = parts[-1] if parts else ""

    if current.strip() or not lines:
        lines.append(current.rstrip())
    return rebalance_short_final_line(lines)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """
    @brief 加载 CJK 兼容字体

    优先级：Noto Sans CJK → DejaVu Sans。
    Noto Sans CJK 支持中日韩字符，适用于 3GPP 图表的术语标注。
    DejaVu Sans 作为英文回退字体（覆盖 ASCII 和扩展拉丁字符）。

    @param size  字号（像素）
    @param bold  True 加载粗体变体
    @return      PIL FreeTypeFont 对象
    @throws      FileNotFoundError 当两个字体都不存在时
    """
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
        if bold
        else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    raise FileNotFoundError(
        "No suitable font found. Install Noto Sans CJK or DejaVu Sans."
    )
