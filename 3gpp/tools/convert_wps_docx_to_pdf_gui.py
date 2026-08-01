#!/usr/bin/env python3
"""
@file convert_wps_docx_to_pdf_gui.py
@brief 通过 WPS Office 的 GUI 路径批量将 3GPP Word 文件导出为 PDF。
       由于本机 WPS 未提供可验证的无头转换接口（如 --convert-to pdf），
       此脚本操控 X11 窗口（xdotool + wmctrl + OCR）模拟鼠标点击，
       依次打开 source.docx、点击 PDF 导出按钮、处理字体嵌入提示对话框。
       目的是弥补无头路径不可用时的自动化缺口，避免手工逐个导出上百份协议文档。
@date 2026-07-22
@note 需要运行中的 X11/Wayland 会话且已安装 WPS、xdotool、wmctrl、tesseract、pdfinfo。
       无头 CI 场景请使用 extract_3gpp_word.py 配合 LibreOffice。
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image


ROOT = Path("3GPP_Rel19/processed")
WPS = Path("/usr/bin/wps")


def run(cmd: list[str], *, check: bool = True, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    """
    @brief 运行外部命令并捕获 stdout/stderr 文本输出，
           统一包装 subprocess.run，减少每次调用时的样板参数。
    @param cmd 命令及其参数列表。
    @return CompletedProcess 对象，含 stdout/stderr 文本。
    """
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check, timeout=timeout)


def sh(script: str, *, check: bool = True, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    """
    @brief 通过 bash -lc 执行 shell 脚本片段，
           用于 pkill 等需要 shell 解析的场景。
    @param script 要执行的 bash 脚本字符串。
    @return CompletedProcess 对象，含 stdout/stderr 文本。
    """
    return subprocess.run(["bash", "-lc", script], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check, timeout=timeout)


def wmctrl_lines() -> list[str]:
    """
    @brief 调用 wmctrl -lx 获取当前所有 X11 窗口列表，
           用于按窗口类名筛选 WPS 窗口。
    @return 每行为一个窗口记录的字符串列表。
    """
    proc = run(["wmctrl", "-lx"], check=False)
    return proc.stdout.splitlines()


def close_wps() -> None:
    """
    @brief 强制结束所有 WPS 相关进程（wpsoffice/wpscloudsvr/promecefpluginhost），
           为下一轮导出提供干净的初始状态。
    @note 使用 pkill 批量终止，忽略进程不存在时的错误；
          执行后等待 2 秒确保进程彻底退出。
    """
    sh(
        "pkill -f '/opt/kingsoft/wps-office/office6/wpsoffice|"
        "/opt/kingsoft/wps-office/office6/wpscloudsvr|"
        "/opt/kingsoft/wps-office/office6/wps /wps|"
        "/opt/kingsoft/wps-office/office6/promecefpluginhost' || true",
        check=False,
    )
    time.sleep(2.0)


def search_window(name: str) -> str | None:
    """
    @brief 通过窗口名称查找匹配的 X11 窗口 ID，
           返回最后一个匹配（通常是最新创建的）。
    @param name 窗口标题中的子串，用于 xdotool search --name 模糊匹配。
    @return 匹配的窗口 ID 字符串，未找到时返回 None。
    @note 返回最后一个匹配，因为在多个同名窗口中通常最新的是目标窗口。
    """
    proc = run(["xdotool", "search", "--name", name], check=False)
    ids = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    return ids[-1] if ids else None


def search_windows(name: str) -> list[str]:
    """
    @brief 通过窗口名称查找所有匹配的 X11 窗口 ID（不限定最新）。
    @param name 窗口标题中的子串。
    @return 所有匹配窗口的 ID 字符串列表。
    """
    proc = run(["xdotool", "search", "--name", name], check=False)
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def window_geometry(win: str) -> tuple[int, int] | None:
    """
    @brief 获取指定 X11 窗口的宽高尺寸，用于排序候选内容窗口。
    @param win X11 窗口 ID 字符串。
    @return (width, height) 元组，窗口不存在或无法获取时返回 None。
    """
    proc = run(["xwininfo", "-id", win], check=False)
    if proc.returncode != 0:
        return None
    width = height = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("Width:"):
            width = int(line.split(":", 1)[1].strip())
        elif line.startswith("Height:"):
            height = int(line.split(":", 1)[1].strip())
    if width is None or height is None:
        return None
    return width, height


def content_window_candidates(name: str) -> list[str]:
    """
    @brief 获取与指定名称匹配的 WPS 内容窗口候选列表，
           优先通过 wmctrl -lx 按类名 wps.wps 精确筛选，面积大的优先。
           由于 WPS 同时暴露外层装饰窗口和内层内容窗口（同名），
           此函数尽量选取内层内容窗口以保证相对坐标点击有效。
    @param name 窗口标题中的子串。
    @return 按面积降序排列的候选窗口 ID 列表。
    """
    lines = wmctrl_lines()
    wins = []
    for line in lines:
        parts = line.split(None, 4)
        if len(parts) >= 5 and parts[2] == "wps.wps" and name in parts[4]:
            wins.append(parts[0])
    if not wins:
        wins = search_windows(name)
    # WPS exposes an outer decorated window and an inner content window with the
    # same title. Prefer the wmctrl wps.wps content window; relative clicks are
    # only valid there.
    scored: list[tuple[int, str]] = []
    for win in wins:
        geom = window_geometry(win)
        if geom is None:
            continue
        w, h = geom
        scored.append((w * h, win))
    return [win for _, win in sorted(scored, reverse=True)]


def window_screenshot(win: str, path: Path) -> Image.Image | None:
    """
    @brief 对指定窗口截图并加载为 PIL Image，用于后续像素级按钮检测和 OCR。
    @param win X11 窗口 ID。
    @param path 截图保存路径（PNG）。
    @return PIL Image 对象（RGB 模式），截图失败返回 None。
    """
    proc = run(["import", "-window", win, str(path)], check=False)
    if proc.returncode != 0 or not path.exists():
        return None
    return Image.open(path).convert("RGB")


def find_blue_button_center(win: str, *, tmp_name: str) -> tuple[int, int] | None:
    """
    @brief 通过像素颜色检测 WPS 界面中蓝色按钮的中心坐标，
           用于定位"确定"/"输出PDF"等 WPS 统一风格按钮。
           在窗口下半部分扫描饱和度蓝色像素，用连通域算法找出最大蓝色区域并计算质心。
    @param win X11 窗口 ID。
    @return (x, y) 按钮中心像素坐标，未找到符合条件的蓝色区域时返回 None。
    @note 依赖 WPS UI 中按钮的蓝色调 (b>150, g>80, r<90) 的启发式规则；
          最小连通域阈值 200 像素，过滤噪声。
    """
    img = window_screenshot(win, Path(f"/tmp/{tmp_name}_{win}.png"))
    if img is None:
        return None
    w, h = img.size
    # WPS primary buttons are saturated blue. Detect the largest blue component
    # in the lower half, then click its center.
    mask: set[tuple[int, int]] = set()
    pix = img.load()
    for y in range(h // 2, h):
        for x in range(w):
            r, g, b = pix[x, y]
            if b > 150 and g > 80 and r < 90 and b - r > 80 and b - g > 20:
                mask.add((x, y))
    if not mask:
        return None

    seen: set[tuple[int, int]] = set()
    best: list[tuple[int, int]] = []
    for p in list(mask):
        if p in seen:
            continue
        stack = [p]
        seen.add(p)
        comp: list[tuple[int, int]] = []
        while stack:
            qx, qy = stack.pop()
            comp.append((qx, qy))
            for nx, ny in ((qx + 1, qy), (qx - 1, qy), (qx, qy + 1), (qx, qy - 1)):
                np = (nx, ny)
                if np in mask and np not in seen:
                    seen.add(np)
                    stack.append(np)
        if len(comp) > len(best):
            best = comp
    if len(best) < 200:
        return None
    xs = [p[0] for p in best]
    ys = [p[1] for p in best]
    return (sum(xs) // len(xs), sum(ys) // len(ys))


def find_text_center(win: str, targets: list[str], *, tmp_name: str) -> tuple[int, int] | None:
    """
    @brief 通过 OCR（Tesseract）识别窗口中的文字目标（如"确定"按钮文字），
           返回匹配文本区域的几何中心坐标，作为鼠标点击位置。
           优先尝试 token 级直接匹配，失败时按行拼接中文字符后重试。
    @param win X11 窗口 ID。
    @param targets 要搜索的目标文本列表，按优先级降序排列。
    @return (x, y) 匹配区域中心坐标，未找到时返回 None。
    @note 使用 chi_sim+eng 语言包和 PSM 6（uniform block of text）；
          中文字符在 OCR 中可能被拆分为多个 token，因此增加按行拼接的逻辑。
    """
    img_path = Path(f"/tmp/{tmp_name}_{win}.png")
    img = window_screenshot(win, img_path)
    if img is None:
        return None
    tsv_base = Path(f"/tmp/{tmp_name}_{win}")
    proc = run(
        [
            "tesseract",
            str(img_path),
            str(tsv_base),
            "-l",
            "chi_sim+eng",
            "--psm",
            "6",
            "tsv",
        ],
        check=False,
        timeout=20,
    )
    tsv_path = tsv_base.with_suffix(".tsv")
    if proc.returncode != 0 or not tsv_path.exists():
        return None
    rows: list[dict[str, str]] = []
    with tsv_path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            text = (row.get("text") or "").strip().replace(" ", "")
            if not text:
                continue
            row["text_norm"] = text
            rows.append(row)

    def row_box(row: dict[str, str]) -> tuple[int, int, int, int]:
        """@brief  从 OCR 输出行中提取包围盒坐标。
        @param  row  OCR 输出行的字典，含 left/top/width/height 字段。
        @return      (left, top, width, height) 四元组整数。"""
        left = int(float(row["left"]))
        top = int(float(row["top"]))
        width = int(float(row["width"]))
        height = int(float(row["height"]))
        return left, top, width, height

    for target in targets:
        target_norm = target.replace(" ", "")
        # First try direct OCR token containment.
        matches = [r for r in rows if target_norm in r["text_norm"] or r["text_norm"] in target_norm]
        if matches:
            lefts: list[int] = []
            tops: list[int] = []
            rights: list[int] = []
            bottoms: list[int] = []
            for r in matches:
                left, top, width, height = row_box(r)
                lefts.append(left)
                tops.append(top)
                rights.append(left + width)
                bottoms.append(top + height)
            return ((min(lefts) + max(rights)) // 2, (min(tops) + max(bottoms)) // 2)

        # Then try line-level concatenation, useful when Chinese text is split.
        by_line: dict[tuple[str, str, str], list[dict[str, str]]] = {}
        for r in rows:
            key = (r.get("block_num", ""), r.get("par_num", ""), r.get("line_num", ""))
            by_line.setdefault(key, []).append(r)
        for line_rows in by_line.values():
            line_text = "".join(r["text_norm"] for r in sorted(line_rows, key=lambda x: int(float(x["left"]))))
            if target_norm not in line_text:
                continue
            lefts = []
            tops = []
            rights = []
            bottoms = []
            for r in line_rows:
                left, top, width, height = row_box(r)
                lefts.append(left)
                tops.append(top)
                rights.append(left + width)
                bottoms.append(top + height)
            return ((min(lefts) + max(rights)) // 2, (min(tops) + max(bottoms)) // 2)
    return None


def ocr_window_text(win: str, *, tmp_name: str) -> str:
    """
    @brief 对窗口截图执行 OCR 并返回去空格后的纯文本，
           用于语义验证（如判断字体提示对话框的语义而非依赖像素坐标）。
    @param win X11 窗口 ID。
    @return 去空格后的 OCR 识别文本，失败时返回空字符串。
    """
    img_path = Path(f"/tmp/{tmp_name}_{win}.png")
    img = window_screenshot(win, img_path)
    if img is None:
        return ""
    out_base = Path(f"/tmp/{tmp_name}_{win}_text")
    proc = run(
        ["tesseract", str(img_path), str(out_base), "-l", "chi_sim+eng", "--psm", "6"],
        check=False,
        timeout=20,
    )
    out_path = out_base.with_suffix(".txt")
    if proc.returncode != 0 or not out_path.exists():
        return ""
    return out_path.read_text(encoding="utf-8", errors="ignore").replace(" ", "")


def prompt_image_embed_fallback(win: str) -> tuple[int, int] | None:
    """
    @brief 字体嵌入提示对话框的回退处理：通过 OCR 确认对话框确为字体提示后，
           使用几何比例（72% 宽度、91% 高度）定位"以图片形式嵌入"按钮。
           仅在 OCR 确认对话框语义正确时才使用几何回退，防止误点到其他窗口。
    @param win X11 窗口 ID。
    @return (x, y) 按钮坐标，语义不匹配时返回 None。
    @note OCR 可能把"嵌入"误识别为"庶入"，因此匹配逻辑检查周边稳定词（字体/PDF/输出）而非仅匹配按钮文字。
    """
    text = ocr_window_text(win, tmp_name="wps_font_prompt_text")
    # Do not use this fallback unless the prompt is clearly the font embedding
    # dialog and the two choices are visible in OCR output. OCR may misread
    # "嵌入" as "庶入", so match the surrounding stable words too.
    has_image_choice = "图片形式" in text or ("图片" in text and "继续输出" in text)
    has_alt_choice = "相似字体" in text
    has_font_context = "字体" in text and ("PDF" in text or "输出" in text)
    if not (has_image_choice and has_alt_choice and has_font_context):
        return None
    img = window_screenshot(win, Path(f"/tmp/wps_font_prompt_fallback_{win}.png"))
    if img is None:
        return None
    w, h = img.size
    # In this verified WPS font prompt, the bottom row has two buttons:
    # left = 以图片形式嵌入, right = 替换相似字体. Use geometry only after
    # OCR has proven this exact dialog semantics.
    return (int(w * 0.72), int(h * 0.91))


def wait_window(name: str, timeout_s: float) -> str | None:
    """
    @brief 轮询等待指定名称的窗口出现，用于 GUI 自动化中等待对话框/文档窗口弹出。
    @param name 窗口标题子串。
    @param timeout_s 最大等待秒数。
    @return 窗口 ID 字符串，超时返回 None。
    """
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        win = search_window(name)
        if win:
            return win
        time.sleep(0.5)
    return None


def wait_no_window(name: str, timeout_s: float) -> bool:
    """
    @brief 轮询等待指定名称的窗口消失，用于确认对话框已关闭、操作已完成。
    @param name 窗口标题子串。
    @param timeout_s 最大等待秒数。
    @return True 表示窗口在超时前消失，False 表示超时后仍存在。
    """
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if not search_window(name):
            return True
        time.sleep(0.5)
    return False


def wait_pdf(pdf: Path, min_size: int = 1024, timeout_s: float = 180.0) -> bool:
    """
    @brief 等待 PDF 文件生成并稳定（文件大小不再变化 2 秒以上），
           期间持续处理可能弹出的字体提示对话框。
    @param pdf 期望的 PDF 文件路径。
    @param min_size 最小文件大小（字节），过滤不完整写入。
    @param timeout_s 最大等待秒数（默认 3 分钟，大文档需更长）。
    @return True 表示 PDF 已稳定生成，False 表示超时。
    @note 轮询间隔 1 秒，同时调用 handle_font_prompt() 消除字体对话框阻塞。
    """
    deadline = time.time() + timeout_s
    last_size = -1
    stable_since: float | None = None
    while time.time() < deadline:
        handle_font_prompt()
        if pdf.exists():
            size = pdf.stat().st_size
            if size >= min_size:
                if size == last_size:
                    stable_since = stable_since or time.time()
                    if time.time() - stable_since >= 2.0:
                        return True
                else:
                    stable_since = None
                    last_size = size
        time.sleep(1.0)
    return False


def verify_pdf(pdf: Path) -> tuple[bool, str]:
    """
    @brief 使用 pdfinfo 验证 PDF 文件合法性并提取页数，
           用于确认 WPS 导出的 PDF 可被标准工具读取。
    @param pdf PDF 文件路径。
    @return (is_valid, pages_str) 元组，is_valid 表示文件合法且有 Pages 字段，
           pages_str 为页数字符串（"UNKNOWN" 表示无法提取）。
    """
    proc = run(["pdfinfo", str(pdf)], check=False)
    text = proc.stdout + proc.stderr
    ok = proc.returncode == 0 and "Pages:" in text
    pages = "UNKNOWN"
    for line in text.splitlines():
        if line.startswith("Pages:"):
            pages = line.split(":", 1)[1].strip()
            break
    return ok, pages


def confirm_export_dialog(export_win: str) -> None:
    """
    @brief 在 WPS PDF 导出对话框中定位并点击"确定"按钮以开始导出。
    @param export_win 导出对话框的 X11 窗口 ID。
    @throws RuntimeError 当 OCR 无法定位确认按钮时抛出，避免在无效状态下盲目点击。
    """
    run(["xdotool", "windowactivate", "--sync", export_win], check=False)
    time.sleep(0.2)
    center = find_text_center(export_win, ["确定", "确定(O)", "OK"], tmp_name="wps_export_dialog")
    if center is None:
        raise RuntimeError("Cannot locate export dialog confirm button by text OCR")
    run(["xdotool", "mousemove", "--window", export_win, str(center[0]), str(center[1])], check=False)
    run(["xdotool", "click", "1"], check=False)


def handle_font_prompt() -> None:
    """
    @brief 检测并消除 WPS 字体嵌入提示对话框，
           通过两种已验证布局的窗口内相对坐标依次尝试点击"以图片形式嵌入"按钮，
           每次点击后检查提示是否消失以避免无效重试。
    @note 此对话框可能在 PDF 导出过程中多次弹出，因此被 wait_pdf 持续轮询调用；
          使用固定相对坐标（965,510 和 965,585）而非 OCR，因为中文按钮文字 OCR 识别率不稳定。
    """
    candidates = content_window_candidates("提示")
    prompt_win = candidates[-1] if candidates else None
    if not prompt_win:
        return
    run(["xdotool", "windowactivate", "--sync", prompt_win], check=False)
    time.sleep(0.1)
    # The "以图片形式嵌入" button appears in two verified layouts. Try both
    # content-window-relative positions, checking after each click whether the
    # prompt has closed. This is faster and more reliable than OCR for this WPS
    # dialog, whose Chinese button text is often misrecognized.
    for x, y in ((965, 510), (965, 585)):
        run(["xdotool", "mousemove", "--window", prompt_win, str(x), str(y)], check=False)
        run(["xdotool", "click", "1"], check=False)
        time.sleep(0.5)
        if not content_window_candidates("提示"):
            return


def export_one(docx: Path, *, dry_run: bool = False) -> tuple[str, str]:
    """
    @brief 将单个 .docx 文件通过 WPS GUI 导出为 PDF，
           涵盖打开文档、点击导出按钮、处理更新提示和字体对话框、等待 PDF 稳定、
           验证合法性，最后关闭 WPS 的完整流程。
    @param docx 源 .docx 文件路径。
    @return (status, pages) 元组，status 为操作状态码字符串（如 "converted_ok"/"failed_open_window"），
           pages 为 PDF 页数或 "-"。
    @note 若 PDF 已存在则跳过导出（幂等），干运行时返回 "dry_run"；
         导出失败后整个批量过程会停止，避免连续错误。
    """
    pdf = docx.with_name("source.pdf")
    if pdf.exists():
        ok, pages = verify_pdf(pdf)
        return ("skip_existing_ok" if ok else "skip_existing_bad", pages)
    if dry_run:
        return "dry_run", "-"

    close_wps()
    subprocess.Popen(
        [str(WPS), str(docx.resolve())],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    doc_win = wait_window("source.docx - WPS Office", 45)
    if not doc_win:
        return "failed_open_window", "-"

    run(["xdotool", "windowactivate", "--sync", doc_win], check=False)
    time.sleep(0.1)

    # Dismiss the update prompt if it appears.
    update_win = search_window("更新")
    if update_win:
        run(["xdotool", "windowactivate", "--sync", update_win], check=False)
        run(["xdotool", "key", "Escape"], check=False)
        time.sleep(1.0)
        run(["xdotool", "windowactivate", "--sync", doc_win], check=False)

    # Verified on this WPS layout: the toolbar button just right of File, second
    # icon, opens the same "输出 PDF 文件" dialog.
    run(["xdotool", "mousemove", "--window", doc_win, "330", "110"], check=False)
    run(["xdotool", "click", "1"], check=False)
    export_win = wait_window("输出 PDF 文件", 10)
    if not export_win:
        # Fallback through the File menu: Alt+F, then F for 输出为PDF(F).
        run(["xdotool", "windowactivate", "--sync", doc_win], check=False)
        run(["xdotool", "key", "alt+f"], check=False)
        time.sleep(0.4)
        run(["xdotool", "key", "f"], check=False)
        export_win = wait_window("输出 PDF 文件", 10)
    if not export_win:
        return "failed_export_dialog", "-"

    confirm_export_dialog(export_win)
    time.sleep(1.0)
    handle_font_prompt()

    if not wait_pdf(pdf, timeout_s=1200):
        return "failed_pdf_timeout", "-"

    ok, pages = verify_pdf(pdf)
    close_wps()
    return ("converted_ok" if ok else "converted_bad_pdfinfo", pages)


def collect_docs(root: Path) -> list[Path]:
    """
    @brief 在指定根目录下递归收集所有 source.docx 和 source.doc 文件，
           按路径排序以保证处理顺序可重现。
    @param root 搜索根目录（通常为 3GPP_Rel19/processed）。
    @return 按路径排序的文档文件列表。
    """
    docs = sorted(root.glob("*/source.docx")) + sorted(root.glob("*/source.doc"))
    return sorted(docs)


def main() -> int:
    """
    @brief 脚本入口：收集所有待导出文档，逐一通过 WPS GUI 导出为 PDF，
           记录状态和页数到 TSV 报告文件，遇到失败立即停止。
    @return 0 表示全部成功或干运行完毕；1 表示至少一个文档导出失败。
    @note 现有 PDF 自动跳过（幂等导出）；
          报告输出路径默认为 docs/audits/wps_pdf_conversion_report.tsv。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=Path, default=Path("docs/audits/wps_pdf_conversion_report.tsv"))
    args = parser.parse_args()

    docs = [p for p in collect_docs(args.root) if not p.with_name("source.pdf").exists()]
    if args.limit:
        docs = docs[: args.limit]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8") as f:
        f.write("document\tstatus\tpages\tpdf\n")
        for i, docx in enumerate(docs, 1):
            print(f"[{i}/{len(docs)}] {docx}", flush=True)
            status, pages = export_one(docx, dry_run=args.dry_run)
            pdf = docx.with_name("source.pdf")
            f.write(f"{docx.parent.name}\t{status}\t{pages}\t{pdf}\n")
            f.flush()
            print(f"  -> {status} pages={pages}", flush=True)
            if not status.endswith("_ok") and status not in {"dry_run"}:
                print(f"Stopping after failure: {docx}", file=sys.stderr)
                return 1
    return 0


# @brief 通过 WPS GUI 批量导出 3GPP Word 文件为 PDF。
# @usage python tools/convert_wps_docx_to_pdf_gui.py [--root PATH] [--limit N] [--dry-run] [--report PATH]
# @args --root     搜索根目录，默认 3GPP_Rel19/processed。
# @args --limit    最多处理文件数，0 表示不限制。
# @args --dry-run  不执行导出，仅收集列表。
# @args --report   报告输出路径，默认 docs/audits/wps_pdf_conversion_report.tsv。
# @exit_code 0 全部成功或干运行；1 有文件导出失败。
if __name__ == "__main__":
    raise SystemExit(main())
