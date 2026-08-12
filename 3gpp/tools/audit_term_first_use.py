#!/usr/bin/env python3
"""@file audit_term_first_use.py
@brief 术语首现终验审计——对 L1/L2/L3 讲义逐词条全位置扫描，确认每个治理词条
       在每篇讲义中的真首现（最早非保护区域出现位置）已配对
       「ABBR（中文，English Full Name）」（含治理认可的并列形态）。
@date 2026-08-12
@note 正式化自治理期临时脚本 /tmp/check_first_use_g*.py（G1-G6 轮次，未入库）。
      终审发现的窗口盲区（同句早位 token 在窗口外伪报、协议引用/入口表误报）
      与全部豁免区判据在本工具内固化；豁免区与判据的权威登记见
      《项目规则与记忆索引.md》第六节第 6 项。

      豁免区判据（终审确认）：
      (a) frontmatter / 标题行 / wikilink / 行内代码 / fenced 代码块 / 公式跨度
      (b) 「## 参考文献」起至文件尾整节
      (c) 协议原文引用：行内“…”/“...”引号内（含全角与半角引号，判据为引号内
          无汉字且长度 >= 30 字符的英文 verbatim 摘录——含中文或短英文的引号
          属作者强调/术语引用，照常扫描）、引用块（>）行
      (d) 协议入口表/证据表：表格行中 content.md: 协议锚点列、协议原文小节英文名列
          （含 § 且无汉字且无全角括号的单元格）；整行无中文上下文的纯定位行
      (e) 术语表文件整文件豁免（L0_terminology_glossary.md + 登记扩展）
      (f) 同句早位 token 遮蔽：行内存在配对即整行判 PAIRED（不要求窗口内）
      (g) 「中文（ABBR, English Full Name）」三件套识别（与拍板形态并列）
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _md_utils import iter_markdown
from audit_lesson_terms import TECH_TERMS  # TECH_TERMS 权威列表（133 项，单一来源）


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 项目级全局缩写（Rule 15）：只在项目早期首次正式引入时讲清全称，
# 后续讲义正文与标题直接使用简称——不参与逐篇首现配对检查。
BASELINE_ABBR = {"3GPP", "LTE", "NR", "UE"}

# 扩展家族词条（TECH_TERMS 之外，G1-G6 治理期间用到的；父任务清单拍板口径）。
# 含中文全称供配对识别；BG1/BG2 不拆配 BG 由词边界自然阻断。
EXTENDED_TERMS = {
    "SC": "逐次消除（Successive Cancellation, SC）",
    "RSC": "递归系统卷积码（Recursive Systematic Convolutional Code, RSC）",
    "BG": "基图（Base Graph, BG）",
    "QC-LDPC": "准循环 LDPC（Quasi-Cyclic LDPC, QC-LDPC）",
    "BP": "置信传播（Belief Propagation, BP）",
    "SPA": "和积算法（Sum-Product Algorithm, SPA）",
    "MS": "最小和（Min-Sum, MS）",
    "NMS": "归一化最小和（Normalized Min-Sum, NMS）",
    "OMS": "偏移最小和（Offset Min-Sum, OMS）",
    "Tanner": "Tanner 图（Tanner Graph）",
}

ALL_TERMS = {**TECH_TERMS, **EXTENDED_TERMS}

# 同形异义守卫（负向前瞻/后瞻）。来源：
#   audit_lesson_terms.py 的 _TERM_PRE_GUARDS/_TERM_POST_GUARDS（MAP/SCL/Qm/DM），
#   叠加 G4b 终审确立的 CSI(?!-)（CSI-RS 不配 CSI），与 H1 任务清单新增：
#   CP(?!-)（CP-OFDM 不配 CP）、HARQ(?!-)（HARQ-ACK 不拆配）、
#   (?<!-)OFDM（DFT-s-OFDM/CP-OFDM 不配 OFDM）、(?<!-)FDMA（SC-FDMA 不配 FDMA）、
#   (?<!-)SC（CA-SCL 不配 SC）。
# BG1/BG2 不拆配 BG、RV0-3 不配 RV、CBGTI/CBGFI 不拆配 CBG、rvidx 不拆配 RV、
# k0 复合名（RV/k0 等）由词边界 (?![A-Za-z0-9]) 与斜杠/连字符守卫自然阻断。
_TERM_PRE_GUARDS = {
    "MAP": r"(?<!Log[-_])",  # Max_Log_MAP / Log-MAP 是独立复合算法名，不拆出 MAP
    "SCL": r"(?<!-)",        # CA-SCL 前缀不拆出 SCL
    "SC": r"(?<!-)",         # CA-SCL 前缀不拆出 SC
    "OFDM": r"(?<!-)",       # DFT-s-OFDM / CP-OFDM 后缀不拆出 OFDM
    "FDMA": r"(?<!-)",       # SC-FDMA 后缀不拆出 FDMA
}
_TERM_POST_GUARDS = {
    "Qm": r"(?!\.)",   # Qm.n（定点 Q 格式，独立登记）不是调制阶数
    "DM": r"(?!-)",    # DM-RS 的 DM 是解调（DeModulation），不是分布匹配
    "CSI": r"(?!-)",   # CSI-RS 不配 CSI
    "CP": r"(?!-)",    # CP-OFDM 不配 CP
    "HARQ": r"(?!-)",  # HARQ-ACK 不拆配
}

TERM_RE = {
    abbr: re.compile(
        rf"(?<![A-Za-z0-9]){_TERM_PRE_GUARDS.get(abbr, '')}{re.escape(abbr)}"
        rf"(?![A-Za-z0-9]){_TERM_POST_GUARDS.get(abbr, '')}"
    )
    for abbr in ALL_TERMS
}

# 术语表文件整文件豁免（豁免区 e）：L0 术语总表（任务点名）+ L2 遗留术语表
# （T13 PS 系列本地术语表，12 行纯表格，2026-08-12 终审登记为豁免区扩展——
# 术语表的表格行本身就是「中文 | English | 释义」配对载体，不要求括号配对形态）。
EXEMPT_GLOSSARY_FILES = {
    (PROJECT_ROOT / "docs" / "L0_协议阅读引导" / "L0_terminology_glossary.md").resolve(),
    (PROJECT_ROOT / "docs" / "L2_协议算法" / "术语表.md").resolve(),
}

# 汉字范围（豁免判据与配对判据共用）
_CN_RE = re.compile(r"[一-鿿]")
_CN2_RE = re.compile(r"[一-鿿]{2,}")
_EN3_RE = re.compile(r"[A-Za-z]{3,}")

# 表格分隔符（排除 \| 转义竖线，如表格内 backtick 内容中的转义管道）
_CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")


def has_cn(seg: str) -> bool:
    """@brief 判断文本是否含汉字。
    @param seg 待检测文本。
    @return 含任意汉字字符（U+4E00-U+9FFF）返回 True。"""
    return bool(_CN_RE.search(seg))


def has_paren_pair(seg: str) -> bool:
    """@brief 判断窗口文本是否构成配对候选：含全角左括号，且括号段内
           含英文（>=3 字母）或中文（>=2 字）——「（中文，English）」形态的
           内容侧判据（G2d 判据的语义化版本）。
    @param seg ABBR 前/后 60 字符窗口。
    @return 构成候选返回 True。"""
    return "（" in seg and (_EN3_RE.search(seg) or _CN2_RE.search(seg))


def inside_existing_pairing(text: str, start: int) -> bool:
    """@brief 判断 match 是否落在同一行某对全角括号内，且该括号组同时含中文与
           英文（即属于某词条的既有 Rule 10 配对文本）——落在其内的子串 token
           （如 CA-SCL 配对文本「CRC 辅助连续消除列表译码，CRC-Aided …」中的 CRC）
           视为非裸奔。
    @param text  已屏蔽保护区域后的全文（行间以换行分隔）。
    @param start 词条匹配起点。
    @return 位于中英混合括号组内返回 True。
    @note 防混淆：括号组内无中英混合（纯数字/纯英文注释）不算配对；
         向后扫描与向前找闭合括号均以行界（\\n）为限。"""
    i = start - 1
    while i >= 0 and text[i] not in "\n":
        if text[i] == "）":
            return False
        if text[i] == "（":
            j = text.find("）", i + 1)
            if j == -1 or "\n" in text[i + 1:j]:
                return False
            seg = text[i + 1:j]
            return has_cn(seg) and _EN3_RE.search(seg)
        i -= 1
    return False


def cn_first_form(text: str, abbr: str, start: int, end: int) -> bool:
    """@brief 「中文（ABBR, English Full Name）」三件套识别（豁免区 g）——
           配对形态为「中文（ABBR, English…）」：ABBR 恰为括号内首 token
           （后随逗号与英文全称），且括号前 <=30 字符内有中文名。
    @param text  已屏蔽保护区域后的全文。
    @param abbr  当前词条缩写。
    @param start 匹配起点（应恰在「（」之后或紧随）。
    @param end   匹配终点。
    @return 三件套形态成立返回 True。
    @note 教训来源：T1.1 L703 LDPC/RNTI 既有形态「低密度奇偶校验码
         （LDPC, Low-Density Parity-Check）」「无线网络临时标识
         （RNTI, Radio Network Temporary Identifier）」——G2d 的 ≤12 字符
         窗口判据只认 ABBR 前置格式（中文（English, ABBR）），本类为 Rule 10
         合法配对且按治理规则不得改写，G6 终审确立与拍板形态并列识别。"""
    o = text.rfind("（", max(0, start - 4), start)
    if o == -1 or "）" in text[o:start]:
        return False
    j = text.find("）", end)
    if j == -1 or "\n" in text[o + 1:j]:
        return False
    seg = text[o + 1:j]
    if not re.match(rf"\s*{re.escape(abbr)}\s*[,，]\s*[A-Za-z]{{3,}}", seg):
        return False
    return has_cn(text[max(0, o - 30):o])


def classify_occurrence(text: str, abbr: str, start: int, end: int) -> str:
    """@brief 对单个词条匹配位置判定配对状态。
    @param text  已屏蔽保护区域后的全文。
    @param abbr  当前词条缩写。
    @param start 匹配起点。
    @param end   匹配终点。
    @return PAIRED / PAIRED(既有配对内) / CHECK(中文紧跟) / UNPAIRED。
    @note 判据链（沿用 G2d/G3a/G3c/G4a 轮次终审口径）：
      1. 位于既有中英混合配对括号组内（CA-SCL 配对文本内的 CRC 等）；
      2. ABBR 后 <=12 字符内出现「（中文/English…」（ABBR 前置配对）；
      3. ABBR 前 <=12 字符内出现「…English）」（中文（English, ABBR）拍板形态）；
      4. ABBR 后 <=12 字符内出现「）」，且前 60 字符内有「（」+英文——
         「中文（English…, ABBR）」式既有配对的末 token 形态；
      5. 「中文（ABBR, English）」三件套（豁免区 g，见 cn_first_form）；
      6. Tanner 特殊判据：后 24 字符内出现中文（讲义既有形态「Tanner 图」）；
      7. 前/后 10 字符内中文紧跟 → CHECK（人工复核桶，非直接判否）；
      8. 其余 → UNPAIRED。"""
    before = text[max(0, start - 60):start].replace("\n", " ")
    after = text[end:end + 60].replace("\n", " ")
    before12 = text[max(0, start - 12):start].replace("\n", " ")
    after12 = text[end:end + 12].replace("\n", " ")

    if inside_existing_pairing(text, start):
        return "PAIRED(既有配对内)"
    if "（" in after12 and has_paren_pair(after):
        return "PAIRED"
    if "）" in before12 and has_paren_pair(before):
        return "PAIRED"
    # 「中文（English…, ABBR）」三件套：ABBR 恰为括号末 token
    if "）" in after12 and "（" in before and _EN3_RE.search(before):
        return "PAIRED"
    # 「中文（ABBR, English）」三件套（豁免区 g）
    if cn_first_form(text, abbr, start, end):
        return "PAIRED"
    # Tanner 图（中文随附）
    if abbr == "Tanner" and _CN_RE.search(text[end:end + 24]):
        return "PAIRED"
    if _CN_RE.search(after[:10]) or _CN_RE.search(before[-10:]):
        return "CHECK(中文紧跟)"
    return "UNPAIRED"


def is_exempt_table_cell(cell: str) -> bool:
    """@brief 判断表格单元格是否属「协议定位列」豁免（豁免区 d）。
    @param cell 单元格原文（含首尾空格）。
    @return 满足以下任一判据返回 True：
      - 含 content.md: 协议锚点（本地证据路径列）；
      - 含 § 且无全角括号 → 协议原文小节英文名列（如 T2.15 L117-118
        「§5.1 UE procedure for receiving PDSCH；…」/「§5.1.1/§5.1.2
        RSRP；…E-UTRA 测量入口」类）。全角括号出现说明单元格含定义/
        叙述性内容（如「技术规范（TS, Technical Specification）…」），
        不属纯定位列，照常扫描。
    @note 判据演进（2026-08-12 H1 终审）：初版要求「§ 且无汉字」导致
         T2.15 L118「…E-UTRA 测量入口」类带短中文标签的定位列漏豁免、
         RSRP/SINR 在入口表内伪报；全库 § 单元格均为协议定位列（含短
         中文标签或仅中文标点），以全角括号为叙述性内容判据即可正确切分。"""
    if "content.md:" in cell:
        return True
    if "§" in cell and "（" not in cell and "）" not in cell:
        return True
    return False


def mask_table_cells(raw_line: str, masked: str) -> str:
    """@brief 表格行豁免区 (d)：把协议锚点列 / 英文小节名列表格单元格整体遮蔽
           （替换为空格，保留 | 分隔符），该行无中文上下文时整行遮蔽。
    @param raw_line 原始表格行。
    @param masked   已屏蔽行内保护区域的行文本（| 位置与原行一致）。
    @return 遮蔽豁免单元格后的行文本。
    @note 判据边界：行内含中文上下文（如「说明 NR 下行接收过程…」列）时
         仅豁免纯协议定位列，不整行豁免；无中文的纯定位行整行豁免。"""
    raw_cells = _CELL_SPLIT_RE.split(raw_line)
    flags = [is_exempt_table_cell(c) for c in raw_cells]
    if not any(has_cn(c) for c in raw_cells):  # 该行无中文上下文、纯协议定位
        flags = [True] * len(raw_cells)
    parts = _CELL_SPLIT_RE.split(masked)
    if len(flags) != len(parts):
        return masked  # 逃逸竖线差异导致的退化：保持原样
    rebuilt = [
        re.sub(r"\S", " ", part) if flag else part
        for flag, part in zip(flags, parts)
    ]
    return "|".join(rebuilt)


_QUOTE_FULLW_RE = re.compile(r"[“]([^”]*)[”]")   # 全角引号对（组 1 为引号内容）
_QUOTE_ASCII_RE = re.compile(r'"([^"\n]*)"')     # 半角引号对（组 1 为引号内容）


def _is_protocol_quote(quote: str) -> bool:
    """@brief 判断引号内容是否属「协议原文引用」（豁免区 c）。
    @param quote 引号内的原文（不含引号本身）。
    @return 无汉字且长度 >= 30 字符的英文引文返回 True。
    @note 教训来源（2026-08-12 H1 终审）：治理期首轮将引号一律豁免导致
         20 处回归——讲义中大量「“QAM（正交幅度调制，Quadrature Amplitude
         Modulation）调制符号”」「“TBCC”表示尾咬卷积码（…）」式作者强调/
         术语引用引号内含合法首现配对（含中文或短英文），豁免后其词条真首现
         被错误后移。协议原文引用在本库中是英文 verbatim 摘录（如
         “The UE shall assume … resource blocks used for the PDSCH …”），
         与作者引用的区分判据：引号内无汉字且长度 >= 30 字符。"""
    if has_cn(quote):
        return False
    return len(quote) >= 30


def mask_line(line: str) -> str:
    """@brief 屏蔽行内保护区域（豁免区 a/c），不改变字符数与 | 位置。
    @param line 原始行文本。
    @return 保护区域替换为等量空格的文本（其余字符原样保留）。
    @note 覆盖：行内公式 $...$、wikilink [[...]]、行内代码 `...`、
         Markdown 链接 [..](..)（含图片）、协议原文引用引号（豁免区 c——
         无汉字的英文 verbatim 摘录须保持原样，不参与首现配对判定）。
         含中文或短英文的引号（作者强调/术语引用）视为讲义正文照常扫描。"""
    s = line
    s = re.sub(r"\$[^$]*\$", " ", s)              # 行内公式
    s = re.sub(r"\[\[[^\]]*\]\]", " ", s)         # wikilink
    s = re.sub(r"`[^`]*`", " ", s)                # 行内代码
    s = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", s)    # Markdown 链接 / 图片
    s = _QUOTE_FULLW_RE.sub(
        lambda m: " " * len(m.group(0)) if _is_protocol_quote(m.group(1)) else m.group(0),
        s)
    s = _QUOTE_ASCII_RE.sub(
        lambda m: " " * len(m.group(0)) if _is_protocol_quote(m.group(1)) else m.group(0),
        s)
    return s


def strip_protected_lines(raw: str) -> tuple[str, list[int]]:
    """@brief 逐行剔除保护区域，重建可扫描文本并建立字符→原行号映射。
    @param raw 文件原文。
    @return (scanned_text, line_map)：line_map[i] 为 scanned_text 第 i 个
            字符在原文件中的 1-based 行号。
    @note 保护区域（豁免区 a/b/c）：frontmatter（--- 之间）、标题行（#）、
         引用块（>）、图片行、fenced 代码块（``` 围栏内）、$$ 公式块、
         「## 参考文献」起至文件尾。行内保护区域由 mask_line 处理。"""
    lines = raw.split("\n")
    out: list[str] = []
    line_map: list[int] = []
    start = 0
    # frontmatter：首行 --- 至闭合 --- 整段豁免
    if lines and lines[0].strip() == "---":
        for i, l in enumerate(lines[1:], start=2):
            if l.strip() == "---":
                start = i
                break
    # 参考文献节：## 参考文献 起至文件尾整节豁免（豁免区 b）
    refs_cut = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith("## 参考文献"):
            refs_cut = i
            break
    in_code = False
    in_math = False
    for lineno in range(start, refs_cut):
        raw_line = lines[lineno]
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if stripped.startswith("$$"):
            in_math = not in_math
            continue
        if in_code or in_math:
            continue
        if (stripped.startswith("#") or stripped.startswith(">")
                or re.match(r"^!\[.*?\]\(.*?\)$", stripped)):
            continue
        masked = mask_line(raw_line)
        if "|" in raw_line:
            masked = mask_table_cells(raw_line, masked)
        out.append(masked)
        line_map.extend([lineno + 1] * len(masked))
        out.append("\n")
        line_map.append(lineno + 1)
    return "".join(out), line_map


def audit_file(path: Path) -> tuple[list[str], list[str]]:
    """@brief 审计单篇讲义：逐词条全位置扫描，输出明细与 PROBLEM 清单。
    @param path 讲义文件路径（术语表文件整文件豁免）。
    @return (detail_lines, problems)：detail_lines 为逐词条明细输出行；
            problems 为未配对真首现的 PROBLEM 行。
    @note 真首现 = 最早匹配位置；判据 = 该位置配对（PAIRED）。同句早位 token
         遮蔽（豁免区 f）：同一行内存在任一定位成 PAIRED 时，整行该词条
         全部判 PAIRED——消除「配对锚点在行内后部、早位 token 在 ≤12 窗口外」
         的伪报（如 T2.3 ARFCN「频点 → ARFCN」链条…协议用 ARFCN（绝对射频
         信道号，Absolute Radio Frequency Channel Number）…」）。"""
    resolved = path.resolve()
    if resolved in EXEMPT_GLOSSARY_FILES:
        return [], []
    raw = path.read_text(encoding="utf-8")
    text, line_map = strip_protected_lines(raw)
    if not line_map:
        return [], []

    per_term: dict[str, list[tuple[int, int, str]]] = {}
    for abbr in sorted(ALL_TERMS):
        if abbr in BASELINE_ABBR:
            continue
        matches: list[tuple[int, int, str]] = []
        rx = TERM_RE[abbr]
        for m in rx.finditer(text):
            start, end = m.span()
            # 连字符复合词守卫（第二道防线）：QC-LDPC 内的 LDPC、HARQ-ACK 的
            # HARQ 等复合词边界（第一道防线是 _TERM_PRE/POST_GUARDS）
            if (start > 0 and text[start - 1] == "-") or (
                    end < len(text) and text[end] == "-"):
                continue
            # k0 斜杠复合名守卫（RV/k0、rvidx/k0、E_r/Ncb/k0 不拆配）
            if abbr == "k0" and start > 0 and text[start - 1] == "/":
                continue
            line = line_map[start] if start < len(line_map) else line_map[-1]
            verdict = classify_occurrence(text, abbr, start, end)
            matches.append((line, start, verdict))
        if not matches:
            continue
        # 同句早位 token 遮蔽（豁免区 f）：行内存在配对即整行判 PAIRED
        final: list[tuple[int, int, str]] = []
        by_line: dict[int, list[tuple[int, str]]] = {}
        for line, pos, verdict in matches:
            by_line.setdefault(line, []).append((pos, verdict))
        for line, items in sorted(by_line.items()):
            paired = any(v.startswith("PAIRED") for _, v in items)
            for pos, verdict in items:
                final.append((line, pos, "PAIRED" if paired else verdict))
        per_term[abbr] = final

    detail: list[str] = []
    problems: list[str] = []
    for abbr in sorted(per_term):
        matches = per_term[abbr]
        first = min(matches, key=lambda t: (t[0], t[1]))
        rest = [m for m in matches if m is not first]
        if not first[2].startswith("PAIRED"):
            problems.append(f"  PROBLEM: {abbr}: 真首现 L{first[0]} = {first[2]}")
        noisy = [f"L{l}={v}" for l, _, v in rest if v != "PAIRED"]
        detail.append(
            f"  {abbr:10s} 真首现 L{first[0]:<4d} {first[2]:18s} 共 {len(matches)} 处"
            + (f" | 后续非PAIRED(无需配对): {noisy}" if noisy else "")
        )
    return detail, problems


def main() -> int:
    """@brief 脚本入口：扫描指定路径下全部讲义，执行术语首现配对终验。
    @usage python3 tools/audit_term_first_use.py <path> [<path> ...]
    @args  paths  一个或多个 Markdown 文件或目录路径（目录递归收集 .md）。
    @env   依赖同目录 _md_utils.py 与 audit_lesson_terms.py（TECH_TERMS 单一来源）。
    @exit_code 0 = 全部讲义真首现已配对（ALL_POSITIONS_FIRST_USE_PAIRED）；
               1 = 存在未配对真首现（HAS_UNPAIRED）。
    @note 输出逐文件明细 + PROBLEM 清单 + 全局汇总；PROBLEM 行需逐条人工
         裁决：真实漏配 → 补配；检查器盲区 → 登记豁免区扩展。"""
    parser = argparse.ArgumentParser(
        description="术语首现配对终验审计（L1/L2/L3 讲义）")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    files = iter_markdown(args.paths)
    problems_by_file: dict[str, list[str]] = {}
    for path in files:
        print(f"=== {path.name} ===")
        detail, file_problems = audit_file(path)
        for line in detail:
            print(line)
        if file_problems:
            print("  FILE_HAS_PROBLEMS")
            for line in file_problems:
                print(line)
            problems_by_file[path.name] = file_problems
        else:
            print("  FILE_OK")

    if problems_by_file:
        total = sum(len(v) for v in problems_by_file.values())
        print(f"\nRESULT: HAS_UNPAIRED  ({total} 处问题, {len(problems_by_file)} 个文件)")
        for name, lines in problems_by_file.items():
            print(f"--- {name} ---")
            for line in lines:
                print(line)
        return 1
    print("\nRESULT: ALL_POSITIONS_FIRST_USE_PAIRED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
