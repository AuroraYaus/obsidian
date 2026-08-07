#!/usr/bin/env python3
""" @file convert_foreignobject_to_text.py
    @brief   将 Mermaid SVG 中的 foreignObject 元素转换为原生 SVG <text> 元素，
             解决浏览器缩放时 foreignObject 内 HTML 文字不跟随缩放的问题。
    @date    2026-07-19 """

import re
import sys
from html import unescape
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """ @brief  从 HTML 片段中提取文本行，按 <br/> 标签分割。
        @note   用于解析 foreignObject 内的多行 HTML 文本，提取纯文本行列表。
                继承自 HTMLParser，逐标签累积文本，遇到 <br/> 即切行。 """

    def __init__(self):
        """ @brief 初始化提取器，准备接收 HTML 数据。 """
        super().__init__()
        self.lines = []
        self.current = ""

    def handle_starttag(self, tag, attrs):
        """ @brief 处理开始标签，遇到 <br/> 时将当前累积文本作为一行保存。
            @param tag   标签名
            @param attrs 标签属性列表 """
        if tag == "br":
            self.lines.append(self.current)
            self.current = ""

    def handle_data(self, data):
        """ @brief 累积 HTML 文本节点中的字符内容。
            @param data HTML 文本节点内容 """
        self.current += data

    def get_lines(self):
        """ @brief 返回提取到的所有文本行，去除首尾空白。
            @return 非空文本行列表，每行为一条标签文本 """
        if self.current:
            self.lines.append(self.current)
        return [ln.strip() for ln in self.lines if ln.strip() or not self.lines]


def convert(svg_content):
    """ @brief  将 SVG 内容中所有 foreignObject 块转换为原生 SVG <text> 元素，
                保证文字在浏览器缩放时随 SVG 矢量缩放而非固定像素。
        @param  svg_content 原始 SVG 字符串（通常由 mmdc 或 Mermaid 渲染器生成）
        @return 转换后的 SVG 字符串，所有 foreignObject 已替换为 <text> + <tspan>
        @note   支持三种标签类型：节点标签 (.label)、边标签 (.edgeLabel > .label)、
                子图/集群标签 (.cluster-label)。每种类型的正则匹配结构略有不同，
                需分别处理。转换时保留颜色、字号、字体族等样式信息。
        @throws 无显式抛出异常；正则匹配失败时回退返回原始 HTML 片段。 """

    # --- node labels: <g class="label" transform="translate(x,y)"><foreignObject>...</foreignObject></g> ---
    node_fo = re.compile(
        r'(<g class="label"[^>]*transform="translate\(([^)]+)\)"[^>]*>)'
        r'(.*?<foreignObject[^>]*>(.*?)</foreignObject>.*?)'
        r'(</g>)',
        re.DOTALL,
    )

    def _node_repl(m):
        """ @brief  节点标签替换回调：将匹配到的 .label > foreignObject 转为 <text>。
            @param  m 正则匹配对象，含 translate 坐标和 foreignObject 内 HTML
            @return 替换后的 SVG 片段（<g><text>...</text></g>），失败时返回原始匹配文本
            @note   单行文本直接嵌入 <text>；多行文本使用 <tspan> 逐行渲染，
                    垂直居中对齐，行高为字号的 1.5 倍。 """
        g_open = m.group(1)
        tx, ty = m.group(2).split(",")
        html_inner = m.group(4)
        g_close = m.group(5)

        extr = TextExtractor()
        try:
            extr.feed(unescape(html_inner))
        except Exception:
            return m.group(0)
        lines = extr.get_lines()
        if not lines:
            return m.group(0)

        color_m = re.search(r"color:\s*([^;\"]+)", html_inner)
        text_color = color_m.group(1).strip() if color_m else "#333"

        fs_m = re.search(r"font-size:\s*(\d+)px", html_inner)
        font_size = fs_m.group(1) if fs_m else "14"

        lh = int(font_size) * 1.5
        x, y = float(tx), float(ty)

        if len(lines) == 1:
            return (
                f'<g transform="translate({x},{y})">'
                f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
                f'font-family="trebuchet ms,verdana,arial,sans-serif" '
                f'y="{lh * 0.35:.1f}">{lines[0]}</text>'
                f"</g>"
            )

        total_h = lh * len(lines)
        start_y = -total_h / 2 + lh * 0.8
        tspans = "\n".join(
            f'<tspan x="0" y="{start_y + i * lh:.1f}">{ln}</tspan>'
            for i, ln in enumerate(lines)
        )
        return (
            f'<g transform="translate({x},{y})">'
            f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
            f'font-family="trebuchet ms,verdana,arial,sans-serif">\n{tspans}\n</text>'
            f"</g>"
        )

    result = node_fo.sub(_node_repl, svg_content)

    # --- edge labels: <g class="edgeLabel"><g class="label" transform="..."><foreignObject>...</foreignObject></g></g> ---
    edge_fo = re.compile(
        r'(<g class="edgeLabel"[^>]*>)'
        r'(<g class="label"[^>]*transform="translate\(([^)]+)\)"[^>]*>)'
        r'(.*?<foreignObject[^>]*>(.*?)</foreignObject>.*?)'
        r"(</g>)\s*(</g>)",
        re.DOTALL,
    )

    def _edge_repl(m):
        """ @brief  边标签替换回调：将 edgeLabel > .label > foreignObject 转为 <text>。
            @param  m 正则匹配对象，含 translate 坐标、背景矩形和 foreignObject 内 HTML
            @return 替换后的 SVG 片段，保留背景矩形 <rect>（若存在），失败时返回原始匹配文本
            @note   边标签有双层 <g> 包裹（edgeLabel → label），与节点标签结构不同。
                    需额外保留背景矩形以维持边标签的视觉外观。 """
        prefix = m.group(1)
        tx, ty = m.group(3).split(",")
        mid = m.group(4)  # between g.label open and foreignObject
        html_inner = m.group(5)
        suffix = m.group(7)

        extr = TextExtractor()
        try:
            extr.feed(unescape(html_inner))
        except Exception:
            return m.group(0)
        lines = extr.get_lines()
        if not lines:
            return m.group(0)

        color_m = re.search(r"color:\s*([^;\"]+)", html_inner)
        text_color = color_m.group(1).strip() if color_m else "#333"

        fs_m = re.search(r"font-size:\s*(\d+)px", html_inner)
        font_size = fs_m.group(1) if fs_m else "14"

        # Preserve background rect if present
        bkg_m = re.search(r"(<rect[^>]*>)", mid)
        bkg = bkg_m.group(1) if bkg_m else ""

        lh = int(font_size) * 1.5
        x, y = float(tx), float(ty)

        if len(lines) == 1:
            return (
                f'{prefix}<g transform="translate({x},{y})">{bkg}'
                f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
                f'font-family="trebuchet ms,verdana,arial,sans-serif" '
                f'y="{lh * 0.35:.1f}">{lines[0]}</text>'
                f"</g>{suffix}"
            )

        total_h = lh * len(lines)
        start_y = -total_h / 2 + lh * 0.8
        tspans = "\n".join(
            f'<tspan x="0" y="{start_y + i * lh:.1f}">{ln}</tspan>'
            for i, ln in enumerate(lines)
        )
        return (
            f'{prefix}<g transform="translate({x},{y})">{bkg}'
            f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
            f'font-family="trebuchet ms,verdana,arial,sans-serif">\n{tspans}\n</text>'
            f"</g>{suffix}"
        )

    result = edge_fo.sub(_edge_repl, result)

    # --- cluster labels: <g class="cluster-label" transform="..."><foreignObject>...</foreignObject></g> ---
    cluster_fo = re.compile(
        r'(<g class="cluster-label"[^>]*transform="translate\(([^)]+)\)"[^>]*>)'
        r'(.*?<foreignObject[^>]*>(.*?)</foreignObject>.*?)'
        r"(</g>)",
        re.DOTALL,
    )

    def _cluster_repl(m):
        """ @brief  子图/集群标签替换回调：将 .cluster-label > foreignObject 转为 <text>。
            @param  m 正则匹配对象，含 translate 坐标和 foreignObject 内 HTML
            @return 替换后的 SVG 片段，失败时返回原始匹配文本
            @note   集群标签使用 text-anchor="start"（左对齐），与节点/边标签的 middle
                    居中不同，以适配子图标题通常靠左的布局惯例。 """
        g_open = m.group(1)
        tx, ty = m.group(2).split(",")
        html_inner = m.group(4)
        g_close = m.group(5)

        extr = TextExtractor()
        try:
            extr.feed(unescape(html_inner))
        except Exception:
            return m.group(0)
        lines = extr.get_lines()
        if not lines:
            return m.group(0)

        color_m = re.search(r"color:\s*([^;\"]+)", html_inner)
        text_color = color_m.group(1).strip() if color_m else "#333"

        fs_m = re.search(r"font-size:\s*(\d+)px", html_inner)
        font_size = fs_m.group(1) if fs_m else "14"

        lh = int(font_size) * 1.5
        x, y = float(tx), float(ty)

        if len(lines) == 1:
            return (
                f'<g transform="translate({x},{y})">'
                f'<text font-size="{font_size}px" fill="{text_color}" '
                f'font-family="trebuchet ms,verdana,arial,sans-serif" '
                f'y="{lh * 0.35:.1f}">{lines[0]}</text>'
                f"</g>"
            )

        total_h = lh * len(lines)
        start_y = -total_h / 2 + lh * 0.8
        tspans = "\n".join(
            f'<tspan x="0" y="{start_y + i * lh:.1f}">{ln}</tspan>'
            for i, ln in enumerate(lines)
        )
        return (
            f'<g transform="translate({x},{y})">'
            f'<text font-size="{font_size}px" fill="{text_color}" '
            f'font-family="trebuchet ms,verdana,arial,sans-serif">\n{tspans}\n</text>'
            f"</g>"
        )

    return cluster_fo.sub(_cluster_repl, result)


def main() -> int:
    """ @brief     命令行入口：读取输入 SVG 文件，将所有 foreignObject 转换为原生 <text>，
                   输出结果并打印转换统计。
        @usage     python3 convert_foreignobject_to_text.py input.svg output.svg
        @args      input.svg   输入 SVG 文件路径（Mermaid/mmdc 导出的原始 SVG）
        @args      output.svg  输出 SVG 文件路径（转换后的原生 text SVG）
        @env       无外部依赖（仅标准库）
        @exit_code 0  转换成功；1  参数不足、文件不存在或解析异常
        @note      参数不足时由 IndexError 自然传播（退出码 1）。"""
    inp, outp = sys.argv[1], sys.argv[2]
    svg = open(inp).read()
    result = convert(svg)
    fo_before = svg.count("<foreignObject")
    fo_after = result.count("<foreignObject")
    text_before = svg.count("<text")
    text_after = result.count("<text")
    open(outp, "w").write(result)
    print(f"foreignObject: {fo_before} → {fo_after}")
    print(f"native <text>:  {text_before} → {text_after}")
    print(f"Output: {outp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
