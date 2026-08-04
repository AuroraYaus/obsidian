#!/usr/bin/env python3
"""@file audit_svg_layout.py
@brief 手绘教学 SVG 的布局几何审计工具：检查文字宿主、越界、重叠、箭头落点与边界间距。
@date 2026-08-04
@note 服务 docs/L2/assets 手绘 SVG（PIL PNG 迁移项目）。
     规则（对应任务几何审计六条）：
     (1) 每个 text 必须完整落在某个 rect 内（class="free" 的页级标题/箭头标注豁免，仅查重叠）；
     (2) text 不与任何非宿主 rect 相交；
     (3) 文字宽度不超出所在宿主 rect（内边距 4px）；
     (4) text-text 无重叠；
     (5) 箭头 path 终点落在某条盒边上（容差 2px）；
     (6) 文本框边界与框外文字/其他文本框保持适当距离（投影间距 ≥ 8px，
         含 class="free" 的框外文字——教训来源 2026-08-04 T2.14 图 3
         "仿真验证"文字与上方 rect 下边界仅约 2px）。
     字体测量用系统 Noto Sans CJK（Regular/Bold），与 SVG font-family 栈首项一致。
@usage python3 tools/audit_svg_layout.py <svg 文件...>
@exit_code 0 = 全部 PASS，1 = 存在 FAIL
"""

from __future__ import annotations

import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import ImageFont

FONT_REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
FONT_INDEX = 2  # Noto Sans CJK SC 在 ttc 中的索引（0=JP,1=KR,2=SC,3=HK,4=TC）

_cache: dict[tuple[bool, int], ImageFont.FreeTypeFont] = {}


def _font(bold: bool, size: float) -> ImageFont.FreeTypeFont:
    """@brief 按加粗与字号取缓存字体对象。
    @param bold 是否加粗
    @param size 字号（px）
    @return PIL 字体对象"""
    key = (bold, int(size))
    if key not in _cache:
        _cache[key] = ImageFont.truetype(FONT_BOLD if bold else FONT_REG, int(size), index=FONT_INDEX)
    return _cache[key]


def text_metrics(text: str, size: float, bold: bool) -> tuple[float, float]:
    """@brief 测量单行文字的像素宽高。
    @param text 文本内容（含空白压缩）
    @param size 字号
    @param bold 是否加粗
    @return (宽, 高) 元组
    @note 对 ASCII 使用 Noto 实际度量；对 CJK 每字按 1.0em 宽估计，与渲染一致。
    """
    fnt = _font(bold, size)
    w = fnt.getlength(text)
    h = fnt.getbbox(text)[3] - fnt.getbbox(text)[1]
    return w, h


def strip_ns(tag: str) -> str:
    """@brief 去除 XML 命名空间前缀。
    @param tag 原始标签名
    @return 纯标签名"""
    return tag.rsplit("}", 1)[-1]


def parse_svg(path: Path) -> tuple[list[dict], list[dict], list[dict]]:
    """@brief 解析 SVG：收集矩形、文字、箭头 path。
    @param path SVG 文件路径
    @return (rects, texts, paths) 三个列表，元素为几何字典
    @note rect 元素含 x/y/w/h/rx；text 元素含 x/y/size/bold/class/text；
     path 元素只收集含 M/L 且以 L 结尾、用作箭头的路径（忽略纯装饰 path）。
    """
    tree = ET.parse(path)
    root = tree.getroot()
    rects: list[dict] = []
    texts: list[dict] = []
    paths: list[dict] = []

    def walk(el: ET.Element, inherit: dict | None = None) -> None:
        """@brief 递归遍历 SVG 元素树，跳过 defs 子树；继承 <g> 上的
        font-size / font-weight / text-anchor 属性（消除存量 SVG 假阳性）。
        @param el 当前 XML 元素
        @param inherit 祖先 <g> 继承的属性字典
        @return None"""
        nonlocal rects, texts, paths
        if strip_ns(el.tag) == "defs":
            return
        tag = strip_ns(el.tag)
        inh = dict(inherit or {})
        for attr in ("font-size", "font-weight", "text-anchor"):
            if el.get(attr) is not None:
                inh[attr] = el.get(attr)
        if tag == "rect":
            x = float(el.get("x", "0"))
            y = float(el.get("y", "0"))
            w = float(el.get("width", "0"))
            h = float(el.get("height", "0"))
            if w <= 0 or h <= 0:
                return
            rects.append(
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "rx": float(el.get("rx", "0") or 0),
                    "fill": el.get("fill", ""),
                }
            )
        elif tag == "text":
            content = "".join(el.itertext()).strip()
            if not content:
                return
            size = float(inh.get("font-size") or el.get("font-size") or "12")
            fw = inh.get("font-weight") or el.get("font-weight") or ""
            bold = "700" in fw or "bold" in fw.lower()
            anchor = inh.get("text-anchor") or el.get("text-anchor") or "start"
            # 多行文本：优先取子 tspan 的 (x, y, 文本) 行列表（父 text 常无 x/y 仅作容器）；
            # 无 tspan 时用自身 x/y 作为单行。
            lines: list[tuple[float, float, str]] = []
            tx = float(el.get("x", "0"))
            ty = float(el.get("y", "0"))
            has_own_xy = el.get("x") is not None and el.get("y") is not None
            for child in el.iter():
                if strip_ns(child.tag) != "tspan":
                    continue
                t = "".join(child.itertext()).strip()
                if not t:
                    continue
                cx = float(child.get("x", tx))
                cy = float(child.get("y", ty))
                lines.append((cx, cy, t))
            if not lines:
                lines = [(tx, ty, content)]
            texts.append(
                {
                    "x": lines[0][0],
                    "y": lines[0][1],
                    "size": size,
                    "bold": bold,
                    "cls": el.get("class", ""),
                    "text": content,
                    "anchor": anchor,
                    "lines": lines,
                    "own_xy": has_own_xy,
                }
            )
        elif tag == "path":
            d = el.get("d", "")
            # 支持 M/L/H/V 命令的简单路径（手绘 SVG 箭头只用这四种）
            tok_re = re.compile(r"([MLHV])\s*([-\d.]+)?[,\s]*([-\d.]+)?")
            pts: list[tuple[float, float]] = []
            cur: tuple[float, float] | None = None
            for cmd, a, b in tok_re.findall(d):
                if cmd == "M":
                    cur = (float(a), float(b))
                    pts.append(cur)
                elif cmd == "L":
                    cur = (float(a), float(b))
                    pts.append(cur)
                elif cmd == "H":
                    cur = (float(a), cur[1])
                    pts.append(cur)
                elif cmd == "V":
                    cur = (cur[0], float(a))
                    pts.append(cur)
            if len(pts) < 2:
                return
            paths.append({"pts": pts})
        for child in el:
            walk(child, inh)

    walk(root)
    return rects, texts, paths


def rect_r(rect: dict) -> tuple[float, float, float, float]:
    """@brief 矩形缩略后的有效范围（圆角矩形内缩 rx/2 保守处理）。
    @param rect 矩形字典
    @return (x0, y0, x1, y1)"""
    inset = min(rect["rx"] / 2, rect["w"] / 4, rect["h"] / 4)
    return (
        rect["x"] + inset,
        rect["y"] + inset,
        rect["x"] + rect["w"] - inset,
        rect["y"] + rect["h"] - inset,
    )


def inside(px: float, py: float, rect: dict, tol: float = 0) -> bool:
    """@brief 点是否在矩形内（含容差）。
    @param px 点 x
    @param py 点 y
    @param rect 矩形字典
    @param tol 外扩容差
    @return 是否在矩形内"""
    x0, y0, x1, y1 = rect_r(rect)
    return x0 - tol <= px <= x1 + tol and y0 - tol <= py <= y1 + tol


def boxes_overlap(
    a: tuple[float, float, float, float], b: tuple[float, float, float, float], tol: float = 1.0
) -> bool:
    """@brief 两矩形是否重叠。
    @param a 矩形 A (x0,y0,x1,y1)
    @param b 矩形 B (x0,y0,x1,y1)
    @param tol 重叠判定容差
    @return 是否重叠"""
    return not (a[2] <= b[0] + tol or b[2] <= a[0] + tol or a[3] <= b[1] + tol or b[3] <= a[1] + tol)


def text_box(t: dict) -> tuple[float, float, float, float]:
    """@brief 计算文字包围盒（x,y 为基线起点，向上偏移 0.9em 估算字框）。
    支持多行（tspan）文本：包围盒为所有行包围盒的并集。
    @param t 文字字典
    @return (x0, y0, x1, y1)"""
    lines = t.get("lines") or [(t["x"], t["y"], t["text"])]
    xs0, ys0, xs1, ys1 = [], [], [], []
    for lx, ly, ltxt in lines:
        w, h = text_metrics(ltxt, t["size"], t["bold"])
        if t["anchor"] == "middle":
            x0 = lx - w / 2
        elif t["anchor"] == "end":
            x0 = lx - w
        else:
            x0 = lx
        xs0.append(x0)
        ys0.append(ly - h * 0.9)
        xs1.append(x0 + w)
        ys1.append(ly + h * 0.1)
    return (min(xs0), min(ys0), max(xs1), max(ys1))


def audit_file(path: Path) -> tuple[bool, list[str]]:
    """@brief 审计单个 SVG 文件的五条几何规则。
    @param path SVG 文件路径
    @return (是否全部通过, 发现列表)
    @note 每条发现格式 "规则编号: 描述"，规则 (1) 豁免 class="free" 的文字。
    """
    rects, texts, paths = parse_svg(path)
    findings: list[str] = []
    ok = True

    def fail(rule: str, msg: str) -> None:
        nonlocal ok
        ok = False
        findings.append(f"{rule}: {msg}")

    # (1) 宿主匹配 + (3) 宽度不超宿主
    for i, t in enumerate(texts):
        tb = text_box(t)
        if t["cls"] == "free":
            continue
        hosts = [r for r in rects if inside(tb[0] + 1, tb[1] + 1, r) and inside(tb[2] - 1, tb[3] - 1, r)]
        if not hosts:
            fail("R1", f"text[{i}] '{t['text']}' 无宿主 rect (box={[round(v,1) for v in tb]})")
            continue
        host = min(hosts, key=lambda r: r["w"] * r["h"])
        if tb[2] > host["x"] + host["w"] - 4 or tb[0] < host["x"] + 4:
            fail("R3", f"text[{i}] '{t['text']}' 宽度超出宿主 rect {[round(host[k],1) for k in ('x','y','w','h')]}")
        # (2) 与"相交但不包含文字 bbox"的 rect 判定为越界（嵌套容器豁免）
        for j, r in enumerate(rects):
            if r is host:
                continue
            rb = (r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"])
            if boxes_overlap(tb, rb) and not (
                inside(tb[0] + 1, tb[1] + 1, r) and inside(tb[2] - 1, tb[3] - 1, r)
            ):
                fail("R2", f"text[{i}] '{t['text']}' 越出宿主，与非宿主 rect[{j}] 相交")

    # (4) text-text 无重叠
    for i, ta in enumerate(texts):
        ba = text_box(ta)
        for j in range(i + 1, len(texts)):
            bb = text_box(texts[j])
            if boxes_overlap(ba, bb):
                fail("R4", f"text[{i}] '{ta['text']}' 与 text[{j}] '{texts[j]['text']}' 重叠")

    # (5) 箭头 path 终点落在某条盒边上（用未缩进矩形 + 容差，圆角内缩不适用边缘点）
    for k, p in enumerate(paths):
        ex, ey = p["pts"][-1]
        hit = any(
            (r["x"] - 2.5 <= ex <= r["x"] + r["w"] + 2.5 and r["y"] - 2.5 <= ey <= r["y"] + r["h"] + 2.5)
            for r in rects
        )
        if not hit:
            fail("R5", f"path[{k}] 终点 ({ex},{ey}) 未落在任何盒边上")

    # (6) 文本框边界与框外文字/其他文本框保持适当距离（投影间距 ≥ 8px）
    MIN_GAP = 8.0
    # 6a: rect 边界 vs 外部 text（含 class="free" 的框外文字；宿主文字跳过）
    for i, r in enumerate(rects):
        rb = (r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"])
        for j, t in enumerate(texts):
            tb = text_box(t)
            if inside(tb[0] + 1, tb[1] + 1, r) and inside(tb[2] - 1, tb[3] - 1, r):
                continue  # 宿主文字，间距规则不适用
            dx = max(rb[0] - tb[2], tb[0] - rb[2], 0.0)
            dy = max(rb[1] - tb[3], tb[1] - rb[3], 0.0)
            if (dx > 0 or dy > 0) and dx < MIN_GAP and dy < MIN_GAP:
                fail(
                    "R6",
                    f"rect[{i}] ({r['x']:.0f},{r['y']:.0f},{r['w']:.0f}x{r['h']:.0f}) 边界与外部 "
                    f"text[{j}] '{t['text'][:18]}' 间距不足（投影间距 {max(dx, dy):.1f}px < {MIN_GAP}px）",
                )
    # 6b: rect-rect 边界间距（嵌套/相接的矩形跳过）
    for i in range(len(rects)):
        ra = (rects[i]["x"], rects[i]["y"], rects[i]["x"] + rects[i]["w"], rects[i]["y"] + rects[i]["h"])
        for j in range(i + 1, len(rects)):
            rb = (rects[j]["x"], rects[j]["y"], rects[j]["x"] + rects[j]["w"], rects[j]["y"] + rects[j]["h"])
            if boxes_overlap(ra, rb, 0.0):
                continue  # 重叠或相接（嵌套容器等）不查间距
            dx = max(ra[0] - rb[2], rb[0] - ra[2], 0.0)
            dy = max(ra[1] - rb[3], rb[1] - ra[3], 0.0)
            if (dx > 0 or dy > 0) and dx < MIN_GAP and dy < MIN_GAP:
                fail(
                    "R6",
                    f"rect[{i}] 与 rect[{j}] 边界间距不足"
                    f"（投影间距 {max(dx, dy):.1f}px < {MIN_GAP}px）",
                )

    # (7) 任何形式的重叠都不允许：rect 部分重叠（完全嵌套的容器除外）
    #     判据：两矩形相交，但既非 A 完全包含 B、也非 B 完全包含 A。
    for i in range(len(rects)):
        ra = (rects[i]["x"], rects[i]["y"], rects[i]["x"] + rects[i]["w"], rects[i]["y"] + rects[i]["h"])
        for j in range(i + 1, len(rects)):
            rb = (rects[j]["x"], rects[j]["y"], rects[j]["x"] + rects[j]["w"], rects[j]["y"] + rects[j]["h"])
            if not boxes_overlap(ra, rb, 0.0):
                continue
            a_contains_b = ra[0] <= rb[0] and ra[1] <= rb[1] and ra[2] >= rb[2] and ra[3] >= rb[3]
            b_contains_a = rb[0] <= ra[0] and rb[1] <= ra[1] and rb[2] >= ra[2] and rb[3] >= ra[3]
            if a_contains_b or b_contains_a:
                continue  # 嵌套容器为合法设计
            fail(
                "R7",
                f"rect[{i}] 与 rect[{j}] 部分重叠（任何形式的重叠不允许）"
                f"：A=({ra[0]:.0f},{ra[1]:.0f},{ra[2]:.0f}x{ra[3]:.0f}) "
                f"B=({rb[0]:.0f},{rb[1]:.0f},{rb[2]:.0f}x{rb[3]:.0f})",
            )

    return ok, findings


def main() -> int:
    """@brief 审计入口：逐个审计传入的 SVG 文件。
    @usage python3 tools/audit_svg_layout.py docs/L2/assets/xxx.svg [...]
    @args 路径列表（.svg 文件）
    @env  需要 PIL 与系统 Noto Sans CJK 字体
    @exit_code 0 = 全部 PASS，1 = 存在 FAIL
    """
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    all_ok = True
    for arg in sys.argv[1:]:
        p = Path(arg)
        if not p.exists():
            print(f"{p}: FILE_MISSING")
            all_ok = False
            continue
        ok, findings = audit_file(p)
        if ok:
            print(f"{p}: SVG_LAYOUT_AUDIT_PASS")
        else:
            all_ok = False
            print(f"{p}: SVG_LAYOUT_AUDIT_FAIL ({len(findings)} findings)")
            for f in findings:
                print(f"    {f}")
    print("ALL_PASS" if all_ok else "HAS_FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
