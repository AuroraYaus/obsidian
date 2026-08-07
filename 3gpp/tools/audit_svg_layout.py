#!/usr/bin/env python3
"""@file audit_svg_layout.py
@brief 手绘教学 SVG 的布局几何审计工具：检查文字宿主、越界、重叠、箭头落点与边界间距。
@date 2026-08-04
@note 服务 docs/L2_协议算法/assets 手绘 SVG（PIL PNG 迁移项目）。
     规则：
     R1  每个 text 必须完整落在某个 rect 内（class="free" 的页级标题/箭头标注豁免）；
     R2  text 不与任何非宿主 rect 相交；
     R3  文字宽度不超出所在宿主 rect（内边距 4px）；
     R4  text-text 无重叠；
     R5  箭头 path 终点落在某条盒边上（容差 2px）；
     R6  文本框边界与框外文字/其他文本框保持适当距离（投影间距 ≥ 8px，
         含 class="free" 的框外文字——教训来源 2026-08-04 T2.10 图 3
         "仿真验证"文字与上方 rect 下边界仅约 2px）；重叠/接触也按间距不足报；
     R7  rect-rect 部分重叠禁止（完全嵌套容器豁免）；
     R8  free 文字与任意 rect 的重叠禁止（教训来源 2026-08-04 T2.10 图 1：
         '组内 Δk=2' 标注压住图例色块——旧版 R2 对 free 文字整体豁免，
         且 R6 只在间距 >0 时报，重叠/接触反而漏报）；
     R9  polygon（箭头三角）与任意 rect/text 的重叠禁止（教训来源 2026-08-04
         T2.10 图 1：Δk 箭头三角压网格 l=13 列——旧版完全不解析 polygon）。
     旋转文字：不支持 transform="rotate"（旧版按未旋转 bbox 计算产生误判）；
         旋转轴标签必须用 tspan 逐字竖排（教训来源 2026-08-04 T2.10 图 1
         频域轴标签压 k 行标签）。
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
    w = fnt.getlength(text) * 1.08  # +8% 安全系数：渲染可能 fallback 到更宽字体
    h = fnt.getbbox(text)[3] - fnt.getbbox(text)[1]
    return w, h


def strip_ns(tag: str) -> str:
    """@brief 去除 XML 命名空间前缀。
    @param tag 原始标签名
    @return 纯标签名"""
    return tag.rsplit("}", 1)[-1]


def parse_svg(path: Path) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    """@brief 解析 SVG：收集矩形、文字、箭头 path、箭头三角 polygon。
    @param path SVG 文件路径
    @return (rects, texts, paths, polygons) 四个列表，元素为几何字典
    @note rect 元素含 x/y/w/h/rx；text 元素含 x/y/size/bold/class/text；
     path 元素只收集含 M/L 且以 L 结尾、用作箭头的路径（忽略纯装饰 path）；
     polygon 元素收集包围盒（箭头三角），供 R9 检查。
    """
    tree = ET.parse(path)
    root = tree.getroot()
    rects: list[dict] = []
    texts: list[dict] = []
    paths: list[dict] = []
    polygons: list[dict] = []
    circles: list[dict] = []

    # 解析 <style> 中的 CSS class 规则（font-size / font-weight）：
    # 教训来源 2026-08-04 T10.9 图 '三角交织后' 标题按 class="label"(14px) 渲染
    # 超出面板 42px，旧版工具不解析 CSS，按默认 12px 度量而漏检。
    css_classes: dict[str, dict[str, str]] = {}
    for st in root.iter():
        if strip_ns(st.tag) != "style" or not st.text:
            continue
        for m in re.finditer(r"\.([A-Za-z0-9_-]+)\s*\{([^}]*)\}", st.text):
            cls, body = m.group(1), m.group(2)
            props = {}
            for pm in re.finditer(r"(font-size|font-weight)\s*:\s*([^;]+);?", body):
                props[pm.group(1)] = pm.group(2).strip()
            if props:
                css_classes[cls] = props

    def walk(el: ET.Element, inherit: dict | None = None) -> None:
        """@brief 递归遍历 SVG 元素树，跳过 defs 子树；继承 <g> 上的
        font-size / font-weight / text-anchor 属性（消除存量 SVG 假阳性）。
        @param el 当前 XML 元素
        @param inherit 祖先 <g> 继承的属性字典
        @return None"""
        nonlocal rects, texts, paths, polygons, circles
        if strip_ns(el.tag) == "defs":
            return
        tag = strip_ns(el.tag)
        inh = dict(inherit or {})
        for attr in ("font-size", "font-weight", "text-anchor"):
            if el.get(attr) is not None:
                inh[attr] = el.get(attr)
        # <g transform="translate(dx,dy)"> 平移继承：烘焙进子元素坐标
        # 教训来源 2026-08-05 T2.19 频域曲线在 translate(440,0) 组内，
        # 未解析导致 R11/R5 误报与真实坐标 bug 漏检。
        tr = el.get("transform", "")
        m = re.search(r"translate\(([-\d.]+),\s*([-\d.]+)\)", tr)
        if m:
            dx = float(m.group(1)); dy = float(m.group(2))
            inh["_dx"] = inh.get("_dx", 0.0) + dx
            inh["_dy"] = inh.get("_dy", 0.0) + dy
        if tag == "circle":
            circles.append(
                {
                    "cx": float(el.get("cx", "0")) + inh.get("_dx", 0.0),
                    "cy": float(el.get("cy", "0")) + inh.get("_dy", 0.0),
                    "r": float(el.get("r", "0")),
                }
            )
        elif tag == "polygon":
            pts_txt = el.get("points", "")
            nums = [float(v) for v in re.findall(r"[\d.]+", pts_txt)]
            if len(nums) >= 6:  # 至少一个三角形
                xs = nums[0::2]
                ys = nums[1::2]
                polygons.append(
                    {
                        "x": min(xs),
                        "y": min(ys),
                        "x1": max(xs),
                        "y1": max(ys),
                        "pts": list(zip(xs, ys)),
                    }
                )
        elif tag == "rect":
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
            cls_style = css_classes.get(el.get("class", ""), {})
            css_size = cls_style.get("font-size", "")
            css_fw = cls_style.get("font-weight", "")
            size = float((inh.get("font-size") or el.get("font-size") or css_size or "12").replace("px", ""))
            fw = inh.get("font-weight") or el.get("font-weight") or css_fw or ""
            bold = "700" in fw or "bold" in fw.lower()
            # tspan 局部加粗：任一行加粗则整 text 按 bold 度量（保守，防低估超边）
            # 教训来源 2026-08-04 T11.1 档案卡片 '<tspan bold>算法本质</tspan>' 超边
            for child in el.iter():
                if strip_ns(child.tag) == "tspan":
                    tfw = child.get("font-weight", "")
                    if "700" in tfw or "bold" in tfw.lower():
                        bold = True
            anchor = inh.get("text-anchor") or el.get("text-anchor") or "start"
            # 多行文本：优先取子 tspan 的 (x, y, 文本) 行列表（父 text 常无 x/y 仅作容器）；
            # 无 tspan 时用自身 x/y 作为单行。
            lines: list[tuple[float, float, str]] = []
            tx = float(el.get("x", "0")) + inh.get("_dx", 0.0)
            ty = float(el.get("y", "0")) + inh.get("_dy", 0.0)
            has_own_xy = el.get("x") is not None and el.get("y") is not None
            for child in el.iter():
                if strip_ns(child.tag) != "tspan":
                    continue
                t = "".join(child.itertext()).strip()
                if not t:
                    continue
                cx = float(child.get("x", tx)) + inh.get("_dx", 0.0)
                cy = float(child.get("y", ty)) + inh.get("_dy", 0.0)
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
            move_idx: list[int] = []  # M 起点索引（子路径分段点）
            cur: tuple[float, float] | None = None
            _dx, _dy = inh.get("_dx", 0.0), inh.get("_dy", 0.0)
            for cmd, a, b in tok_re.findall(d):
                if cmd == "M":
                    cur = (float(a) + _dx, float(b) + _dy)
                    pts.append(cur)
                    move_idx.append(len(pts) - 1)
                elif cmd == "L":
                    cur = (float(a) + _dx, float(b) + _dy)
                    pts.append(cur)
                elif cmd == "H":
                    cur = (float(a) + _dx, cur[1] + _dy)
                    pts.append(cur)
                elif cmd == "V":
                    cur = (cur[0] + _dx, float(a) + _dy)
                    pts.append(cur)
            if len(pts) < 2:
                return
            paths.append({"pts": pts, "move_idx": move_idx})
        for child in el:
            walk(child, inh)

    walk(root)
    W, H = 0.0, 0.0
    vw = root.get("viewBox")
    if vw:
        parts = vw.replace(",", " ").split()
        if len(parts) == 4:
            W, H = float(parts[2]), float(parts[3])
    if W <= 0:
        W = float(root.get("width", "0") or 0)
    if H <= 0:
        H = float(root.get("height", "0") or 0)
    return rects, texts, paths, polygons, circles, W, H


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
    """@brief 审计单个 SVG 文件的九条几何规则。
    @param path SVG 文件路径
    @return (是否全部通过, 发现列表)
    @note 每条发现格式 "规则编号: 描述"；R8/R9 教训来源见文件头 @note。
    """
    rects, texts, paths, polygons, circles, canvas_w, canvas_h = parse_svg(path)
    # 背景底板 rect（覆盖 ≥95% 画布）：R6/R8/R9 豁免
    bg_rects = {
        id(r)
        for r in rects
        if canvas_w > 0 and canvas_h > 0 and r["w"] >= 0.95 * canvas_w and r["h"] >= 0.95 * canvas_h
    }
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
    # 宿主文字（完全在某个非背景 rect 内）不参与 R6：其内边距由 R3 管理，
    # 相邻无缝小格（如 26x22 导频格）内的居中文字与邻格间距物理上无法 ≥8px
    #（教训来源 2026-08-04 T2.10 图 2 'Ĥ' 标签与相邻导频格间距 1.1px 误报）。
    hosted_texts: set[int] = set()
    for j, t in enumerate(texts):
        tb = text_box(t)
        for r in rects:
            if id(r) in bg_rects:
                continue
            if inside(tb[0] + 1, tb[1] + 1, r) and inside(tb[2] - 1, tb[3] - 1, r):
                hosted_texts.add(j)
                break
    # 6a: rect 边界 vs 外部 text（含 class="free" 的框外文字；宿主文字跳过）
    for i, r in enumerate(rects):
        if id(r) in bg_rects:
            continue
        rb = (r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"])
        for j, t in enumerate(texts):
            if j in hosted_texts:
                continue  # 宿主文字，间距规则不适用
            tb = text_box(t)
            if inside(tb[0] + 1, tb[1] + 1, r) and inside(tb[2] - 1, tb[3] - 1, r):
                continue  # 宿主文字，间距规则不适用
            dx = max(rb[0] - tb[2], tb[0] - rb[2], 0.0)
            dy = max(rb[1] - tb[3], tb[1] - rb[3], 0.0)
            if boxes_overlap(tb, rb, 0.0):
                # 重叠/接触也按间距不足报（旧版只报 dx>0 or dy>0，重叠反而漏报）
                fail(
                    "R6",
                    f"rect[{i}] ({r['x']:.0f},{r['y']:.0f},{r['w']:.0f}x{r['h']:.0f}) 与外部 "
                    f"text[{j}] '{t['text'][:18]}' 重叠/接触（间距 0px < {MIN_GAP}px）",
                )
            elif (dx > 0 or dy > 0) and dx < MIN_GAP and dy < MIN_GAP:
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

    # (8) free 文字与任意 rect 的重叠禁止（网格格、图例色块等都在内）
    #     教训来源：2026-08-04 T2.10 图 1 '组内 Δk=2' 压住"数据 RE"图例色块，
    #     旧版 R2 对 free 文字整体豁免导致漏报。
    #     豁免：文字 bbox 完全被 rect 包含（宿主关系，如说明框内的内容文字）。
    for i, t in enumerate(texts):
        if t["cls"] != "free":
            continue
        tb = text_box(t)
        for j, r in enumerate(rects):
            if id(r) in bg_rects:
                continue
            rb = (r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"])
            if tb[0] >= rb[0] - 0.5 and tb[1] >= rb[1] - 0.5 and tb[2] <= rb[2] + 0.5 and tb[3] <= rb[3] + 0.5:
                continue  # 完全在 rect 内：宿主关系，非遮盖
            if boxes_overlap(tb, rb, 0.0):
                fail(
                    "R8",
                    f"free text[{i}] '{t['text'][:20]}' 与 rect[{j}] "
                    f"({r['x']:.0f},{r['y']:.0f},{r['w']:.0f}x{r['h']:.0f}) 重叠",
                )

    # (9) polygon（箭头三角）与任意 rect/text 的重叠禁止
    #     教训来源：2026-08-04 T2.10 图 1 Δk 箭头三角压网格 l=13 列，
    #     旧版完全不解析 polygon 元素。
    #     豁免：贴边箭头（尖端恰好停在盒边上）——bbox 必然与目标盒接触，
    #     用精确重叠面积（1px 采样）+ 阈值判定，只报真正的侵入。
    TRI_OVERLAP_THRESHOLD = 15.0  # px^2：贴边接触通常 <10，真侵入通常 >40

    def tri_rect_area(tri: dict, rb: tuple[float, float, float, float]) -> float:
        """@brief 三角形与矩形重叠面积（1px 采样近似）。
        @param tri 三角形包围盒字典（含原始点坐标由调用方传入）
        @param rb 矩形 (x0,y0,x1,y1)
        @return 重叠面积 px^2
        @note 对 12x12 量级的箭头三角，1px 采样 144 点，误差可忽略。"""
        pts = tri["pts"]
        x0, y0, x1, y1 = rb
        area = 0.0
        for px in range(math.floor(min(p[0] for p in pts)), math.ceil(max(p[0] for p in pts))):
            for py in range(math.floor(min(p[1] for p in pts)), math.ceil(max(p[1] for p in pts))):
                # 点在三角形内（重心法）
                (ax, ay), (bx, by), (cx, cy) = pts[0], pts[1], pts[2]
                v0x, v0y = cx - ax, cy - ay
                v1x, v1y = bx - ax, by - ay
                v2x, v2y = px + 0.5 - ax, py + 0.5 - ay
                d00 = v0x * v0x + v0y * v0y
                d01 = v0x * v1x + v0y * v1y
                d11 = v1x * v1x + v1y * v1y
                d20 = v2x * v0x + v2y * v0y
                d21 = v2x * v1x + v2y * v1y
                denom = d00 * d11 - d01 * d01
                if denom == 0:
                    continue
                v = (d11 * d20 - d01 * d21) / denom
                w = (d00 * d21 - d01 * d20) / denom
                u = 1.0 - v - w
                if u >= 0 and v >= 0 and w >= 0 and x0 <= px + 0.5 <= x1 and y0 <= py + 0.5 <= y1:
                    area += 1.0
        return area

    for k, p in enumerate(polygons):
        pb = (p["x"], p["y"], p["x1"], p["y1"])
        for j, r in enumerate(rects):
            if id(r) in bg_rects:
                continue
            rb = (r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"])
            if boxes_overlap(pb, rb, 0.0) and tri_rect_area(p, rb) > TRI_OVERLAP_THRESHOLD:
                fail(
                    "R9",
                    f"polygon[{k}] ({p['x']:.0f},{p['y']:.0f},{p['x1']:.0f}x{p['y1']:.0f}) "
                    f"侵入 rect[{j}] ({r['x']:.0f},{r['y']:.0f},{r['w']:.0f}x{r['h']:.0f}) "
                    f"面积 {tri_rect_area(p, rb):.0f}px² > {TRI_OVERLAP_THRESHOLD:.0f}px²",
                )
        for j, t in enumerate(texts):
            tb = text_box(t)
            if boxes_overlap(pb, tb, 0.0) and tri_rect_area(p, tb) > TRI_OVERLAP_THRESHOLD:
                fail("R9", f"polygon[{k}] 侵入 text[{j}] '{t['text'][:20]}'")

    # (10) circle（图模型节点等图形元素）必须完整位于某个 rect 内且距该
    #      rect 边界 ≥ 8px——教训来源 2026-08-04 T11.1 图 Polar 解码树叶子
    #      距面板右缘仅 13px 贴边，旧版 R1-R9 只查 text/rect/polygon，
    #      circle 与面板边沿的贴边完全不查。
    for k, c in enumerate(circles):
        if c["r"] <= 0:
            continue
        cx, cy, r = c["cx"], c["cy"], c["r"]
        hosts = [rct for rct in rects
                 if id(rct) not in bg_rects
                 and rct["x"] <= cx - r and rct["y"] <= cy - r
                 and cx + r <= rct["x"] + rct["w"] and cy + r <= rct["y"] + rct["h"]]
        if not hosts:
            continue  # 自由散布的装饰/数据点（星座点、散点）不在任何 rect 内属正常设计，豁免
        host = min(hosts, key=lambda rct: rct["w"] * rct["h"])
        gap = min(cx - r - host["x"], cy - r - host["y"],
                  host["x"] + host["w"] - (cx + r), host["y"] + host["h"] - (cy + r))
        # 阈值随半径缩放：小数据点（r<=5）允许 6px，大节点 8px
        CIRCLE_MIN_GAP = max(6.0, r)
        if gap < CIRCLE_MIN_GAP:
            fail("R10", f"circle[{k}] ({cx:.0f},{cy:.0f},r={r:.0f}) 距宿主 rect 边界 "
                        f"仅 {gap:.1f}px < {CIRCLE_MIN_GAP}px（贴边）")

    # (11) 曲线 path（≥8 点的 polyline，如波形/曲线）与文字的重叠检查
    #      教训来源 2026-08-05 T2.0 图 1 时域波形与注释文字重叠 9px，
    #      R4/R8 只查 text-text 与 text-rect，path 与 text 不查。
    #      判据：曲线逐线段与 text bbox 的最近距离 < 4px（真实压字才报，
    #      bbox 整体判据会因曲线包围盒虚大而误报——2026-08-05 T8.3 五区边界线教训）。
    CURVE_TEXT_MIN_DIST = 4.0
    curves = [pth for pth in paths if len(pth["pts"]) >= 8]
    for k, pth in enumerate(curves):
        pts = pth["pts"]
        for j, t in enumerate(texts):
            tb = text_box(t)
            hit = False
            move_set = set(pth.get("move_idx", []))
            for seg_i in range(len(pts) - 1):
                if seg_i + 1 in move_set:
                    continue  # 抬笔段（M 新起点前无真实线段），跳过——2026-08-05 教训
                x1, y1 = pts[seg_i]
                x2, y2 = pts[seg_i + 1]
                # 线段到矩形 bbox 的最近距离（9 点采样，覆盖长线段）
                dmin = float("inf")
                for si in range(9):
                    px = x1 + (x2 - x1) * si / 8
                    py = y1 + (y2 - y1) * si / 8
                    dx = max(tb[0] - px, px - tb[2], 0.0)
                    dy = max(tb[1] - py, py - tb[3], 0.0)
                    dmin = min(dmin, math.hypot(dx, dy))
                if dmin < CURVE_TEXT_MIN_DIST:
                    hit = True
                    break
            if hit:
                fail("R11", f"曲线 path[{k}] 与 text[{j}] '{t['text'][:18]}' "
                            f"最近距离 < {CURVE_TEXT_MIN_DIST}px（线段穿过文字）")

    return ok, findings


def main() -> int:
    """@brief 审计入口：逐个审计传入的 SVG 文件。
    @usage python3 tools/audit_svg_layout.py docs/L2_协议算法/assets/xxx.svg [...]
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
