#!/usr/bin/env python3
"""
@file consolidate_docs_terms.py
@brief 将各节讲义中重复出现的术语缩写集中收纳到全局术语总表，并从各节正文中移除分散的术语说明
       小节和前置缩写表格，最终统一替换全名展开为缩写，使讲义更聚焦教学内容而非机械重复解释。
@date 2026-07-22
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = PROJECT_ROOT / "docs"
LESSON_ROOTS = [DOCS_ROOT / "L1", DOCS_ROOT / "L2_协议算法", DOCS_ROOT / "L3"]
GLOSSARY_PATH = DOCS_ROOT / "L0" / "L0_terminology_glossary.md"
READING_MAP = DOCS_ROOT / "L1" / "T0.1_LTE_NR_decoder_protocol_reading_map.md"

GLOSSARY_GROUPS: list[tuple[str, list[tuple[str, str, str]]]] = [
    (
        "系统与协议缩写",
        [
            ("3GPP", "第三代合作伙伴计划", "3rd Generation Partnership Project；LTE/NR 协议规范来源。"),
            ("LTE", "长期演进", "Long Term Evolution；4G 蜂窝系统，本项目关注其 Turbo 数据译码链路。"),
            ("NR", "新空口", "New Radio；5G 空口系统，本项目关注其 LDPC 数据译码和 Polar 控制译码链路。"),
            ("MAC", "媒体接入控制层", "Medium Access Control；调度、HARQ process 和上层交付上下文来源。"),
            ("UL-SCH", "上行共享信道", "Uplink Shared Channel；上行数据传输信道。"),
            ("DL-SCH", "下行共享信道", "Downlink Shared Channel；下行数据传输信道。"),
            ("UCI", "上行控制信息", "Uplink Control Information；NR Polar 或 small block coding 的常见控制负载来源。"),
            ("DCI", "下行控制信息", "Downlink Control Information；PDCCH 盲检、CRC/RNTI 和 Polar 译码相关。"),
            ("PDSCH", "物理下行共享信道", "Physical Downlink Shared Channel；下行数据或 PCH 承载入口。"),
            ("DM-RS", "解调参考信号", "Demodulation Reference Signal；接收端估计数据符号附近信道的参考信号。"),
            ("CSI-RS", "信道状态信息参考信号", "Channel State Information Reference Signal；用于信道状态测量、报告和相关接收过程。"),
            ("RSRP", "参考信号接收功率", "Reference Signal Received Power；描述参考信号功率强弱。"),
            ("SINR", "信干噪比", "Signal to Interference plus Noise Ratio；描述信号相对干扰和噪声的强弱。"),
        ],
    ),
    (
        "译码对象与算法",
        [
            ("LLR", "对数似然比", "Log-Likelihood Ratio；译码器输入软信息，通常用符号表示倾向、幅度表示可靠度。"),
            ("CRC", "循环冗余校验", "Cyclic Redundancy Check；用于错误检测，不负责纠错。"),
            ("HARQ", "混合自动重传请求", "Hybrid Automatic Repeat Request；通过重传和软合并提升可靠性。"),
            ("TB", "传输块", "Transport Block；信道编码/译码链路最终交付的整体数据对象。"),
            ("CB", "码块", "Code Block；TB 分段后由译码核心逐块处理的工作单元。"),
            ("CBG", "码块组", "Code Block Group；NR LDPC 中可作为部分重传粒度的一组 CB。"),
            ("LDPC", "低密度奇偶校验码", "Low-Density Parity-Check Code；NR 数据业务的主要信道编码家族。"),
            ("Turbo", "Turbo 码", "Turbo Code；LTE 数据业务的主要信道编码家族。"),
            ("Polar", "极化码", "Polar Code；NR 控制信息译码的主要编码家族。"),
            ("BCJR", "BCJR 算法", "Bahl、Cocke、Jelinek、Raviv 提出的后验概率译码算法；名称来自作者姓氏。"),
            ("MAP", "最大后验概率", "Maximum A Posteriori；基于观测后后验概率选择最可能路径或比特。"),
            ("SCL", "连续消除列表译码", "Successive Cancellation List；Polar 译码中保留多条候选路径的算法。"),
            ("CA-SCL", "CRC 辅助 SCL", "CRC-aided SCL；用 CRC 在 Polar SCL 候选路径中辅助最终选择。"),
        ],
    ),
    (
        "调制、信道与性能",
        [
            ("AWGN", "加性白高斯噪声", "Additive White Gaussian Noise；入门链路仿真的常用噪声模型。"),
            ("BPSK", "二进制相移键控", "Binary Phase Shift Keying；每个符号承载一个比特的调制方式。"),
            ("QPSK", "正交相移键控", "Quadrature Phase Shift Keying；每个复符号承载两个比特的调制方式。"),
            ("QAM", "正交幅度调制", "Quadrature Amplitude Modulation；用幅度和相位承载多比特信息的调制家族。"),
            ("MCS", "调制与编码方案", "Modulation and Coding Scheme；调度侧选择调制阶数和目标码率的索引。"),
            ("TBS", "传输块大小", "Transport Block Size；调度侧得到的 TB 比特规模。"),
            ("BLER", "块错误率", "Block Error Rate；多帧统计中块译码失败比例。"),
            ("BER", "比特错误率", "Bit Error Rate；按比特统计的错误比例。"),
            ("FER", "帧错误率", "Frame Error Rate；按帧统计的错误比例。"),
            ("SNR", "信噪比", "Signal-to-Noise Ratio；信号功率与噪声功率的比值。"),
            ("RV", "冗余版本", "Redundancy Version；速率匹配循环缓存中的不同起点或区域选择。"),
            ("PRB", "物理资源块", "Physical Resource Block；物理层资源分配的基本频域块。"),
            ("RE", "资源元素", "Resource Element；一个 OFDM 符号和一个子载波位置上的资源单元。"),
        ],
    ),
    (
        "工程实现与验证",
        [
            ("RTL", "寄存器传输级", "Register Transfer Level；用寄存器、组合逻辑、状态机和接口描述硬件的层级。"),
            ("ASIC", "专用集成电路", "Application-Specific Integrated Circuit；RTL 综合、布局布线后面向芯片实现的形态。"),
            ("SRAM", "静态随机存取存储器", "Static Random-Access Memory；常用于 LLR、消息、soft buffer 和 trace 存储。"),
            ("DUT", "待测设计", "Device Under Test；被 testbench 驱动、观测和判定的 RTL 模块。"),
            ("DMA", "直接存储器访问", "Direct Memory Access；硬件按地址搬移输入 LLR、输出比特和 trace 的数据通路。"),
            ("SVA", "SystemVerilog 断言", "SystemVerilog Assertion；用时钟化属性检查接口不变量。"),
            ("UVM", "通用验证方法学", "Universal Verification Methodology；SystemVerilog 验证框架。"),
            ("STA", "静态时序分析", "Static Timing Analysis；用时钟、延迟和约束计算路径是否满足时序。"),
            ("SDC", "Synopsys 设计约束", "Synopsys Design Constraints；描述时钟、输入输出延迟、false path、multicycle path 等约束。"),
            ("PPA", "功耗、性能、面积", "Power, Performance, Area；硬件实现常用综合权衡指标。"),
        ],
    ),
    (
        "基础概念",
        [
            ("向量", "vector", "一排或一列数字；本项目里常是一串 `0/1` 比特或 LLR。"),
            ("矩阵", "matrix", "按行和列排成的数字表。"),
            ("奇偶校验矩阵", "parity-check matrix", "用来检查比特串是否满足若干奇偶规则的矩阵。"),
            ("校验子", "syndrome", "校验结果；全零表示校验规则通过，非零表示至少有规则没通过。"),
            ("概率", "probability", "描述事件发生可能性的数值。"),
            ("条件概率", "conditional probability", "在某个条件已经发生时另一个事件发生的概率。"),
            ("先验概率", "prior probability", "看到观测证据之前的概率判断。"),
            ("似然", "likelihood", "给定假设时看到当前观测的支持程度。"),
            ("后验概率", "posterior probability", "看到观测证据之后更新得到的概率判断。"),
            ("证据", "evidence", "支撑协议结论或工程结论的本地文件、表格、公式、日志或测试输出。"),
            ("贝叶斯公式", "Bayes' rule", "把先验、似然和后验联系起来的概率公式。"),
            ("硬判决", "hard decision", "只输出 `0` 或 `1`，不保留可靠度。"),
            ("软判决", "soft decision", "不只输出倾向，还保留可靠度。"),
            ("似然比", "likelihood ratio", "两个假设的似然或概率相除后得到的支持度比较。"),
            ("裁剪", "clipping", "把太大的数限制在最大范围内。"),
            ("饱和", "saturation", "计算结果超过表示范围时停在边界值。"),
            ("熵", "entropy", "描述不确定性的量。"),
            ("互信息", "mutual information", "描述观测和原始信息之间共享信息量的量。"),
            ("信道容量", "channel capacity", "给定信道条件下理论可可靠传输的最高信息率。"),
            ("码率", "code rate", "信息比特数与编码后比特数的比例。"),
            ("编码增益", "coding gain", "使用纠错编码后达到同等误码表现所节省的信噪比。"),
            ("高斯随机变量", "Gaussian random variable", "服从高斯分布的随机变量。"),
            ("噪声方差", "noise variance", "噪声离散程度的平方量纲指标。"),
            ("噪声标准差", "noise standard deviation", "噪声方差的平方根。"),
            ("每比特能量与噪声谱密度比", "$E_b/N_0$", "按每个信息比特能量归一化的信噪比指标。"),
            ("每符号能量与噪声谱密度比", "$E_s/N_0$", "按每个调制符号能量归一化的信噪比指标。"),
            ("调制阶数", "$Q_m$", "每个调制符号承载的比特数。"),
            ("星座图", "constellation diagram", "调制符号在复平面上的点集。"),
            ("同相分量", "in-phase component, I", "复数信号的 I 分量。"),
            ("正交分量", "quadrature component, Q", "复数信号的 Q 分量。"),
            ("Gray 映射", "Gray mapping", "相邻星座点只差一个比特的映射方式。"),
            ("软解调", "soft demapping", "把接收符号转换成逐比特软信息的过程。"),
            ("逐比特 LLR", "bit-wise LLR", "每个编码比特对应一个 LLR。"),
        ],
    ),
]

EXPANSION_REPLACEMENTS = [
    ("第三代合作伙伴计划（3rd Generation Partnership Project）", "3GPP"),
    ("第三代合作伙伴计划（3rd Generation Partnership Project, 3GPP）", "3GPP"),
    ("长期演进（Long Term Evolution）", "LTE"),
    ("长期演进（Long Term Evolution, LTE）", "LTE"),
    ("新空口（New Radio）", "NR"),
    ("新空口（New Radio, NR）", "NR"),
    ("对数似然比（Log-Likelihood Ratio）", "LLR"),
    ("对数似然比（Log-Likelihood Ratio, LLR）", "LLR"),
    ("循环冗余校验（Cyclic Redundancy Check）", "CRC"),
    ("循环冗余校验（Cyclic Redundancy Check, CRC）", "CRC"),
    ("混合自动重传请求（Hybrid Automatic Repeat Request）", "HARQ"),
    ("混合自动重传请求（Hybrid Automatic Repeat Request, HARQ）", "HARQ"),
    ("传输块（Transport Block）", "TB"),
    ("传输块（Transport Block, TB）", "TB"),
    ("码块（Code Block）", "CB"),
    ("码块（Code Block, CB）", "CB"),
    ("寄存器传输级（Register Transfer Level）", "RTL"),
    ("寄存器传输级（Register Transfer Level, RTL）", "RTL"),
    ("专用集成电路（Application-Specific Integrated Circuit）", "ASIC"),
    ("专用集成电路（Application-Specific Integrated Circuit, ASIC）", "ASIC"),
    ("低密度奇偶校验码（Low-Density Parity-Check Code）", "LDPC"),
    ("低密度奇偶校验码（Low-Density Parity-Check Code, LDPC）", "LDPC"),
    ("Turbo 码（Turbo Code）", "Turbo"),
    ("极化码（Polar Code）", "Polar"),
    ("块错误率（Block Error Rate）", "BLER"),
    ("块错误率（Block Error Rate, BLER）", "BLER"),
    ("调制与编码方案（Modulation and Coding Scheme）", "MCS"),
    ("调制与编码方案（Modulation and Coding Scheme, MCS）", "MCS"),
    ("传输块大小（Transport Block Size）", "TBS"),
    ("传输块大小（Transport Block Size, TBS）", "TBS"),
    ("静态随机存取存储器（Static Random-Access Memory）", "SRAM"),
    ("静态随机存取存储器（Static Random-Access Memory, SRAM）", "SRAM"),
    ("媒体接入控制层（Medium Access Control）", "MAC"),
    ("媒体接入控制层（Medium Access Control, MAC）", "MAC"),
    ("上行共享信道（Uplink Shared Channel）", "UL-SCH"),
    ("上行共享信道（Uplink Shared Channel, UL-SCH）", "UL-SCH"),
    ("下行共享信道（Downlink Shared Channel）", "DL-SCH"),
    ("下行共享信道（Downlink Shared Channel, DL-SCH）", "DL-SCH"),
    ("上行控制信息（Uplink Control Information）", "UCI"),
    ("上行控制信息（Uplink Control Information, UCI）", "UCI"),
    ("下行控制信息（Downlink Control Information）", "DCI"),
    ("下行控制信息（Downlink Control Information, DCI）", "DCI"),
    ("二进制相移键控（Binary Phase Shift Keying）", "BPSK"),
    ("正交相移键控（Quadrature Phase Shift Keying）", "QPSK"),
    ("正交幅度调制（Quadrature Amplitude Modulation）", "QAM"),
    ("加性白高斯噪声（Additive White Gaussian Noise）", "AWGN"),
    ("物理资源块（Physical Resource Block）", "PRB"),
    ("资源元素（Resource Element）", "RE"),
    ("冗余版本（Redundancy Version）", "RV"),
    ("码块组（Code Block Group, CBG）", "CBG"),
    ("码块组（Code Block Group）", "CBG"),
    ("比特错误率（Bit Error Rate, BER）", "BER"),
    ("帧错误率（Frame Error Rate, FER）", "FER"),
    ("待测设计（Device Under Test, DUT）", "DUT"),
    ("直接存储器访问（Direct Memory Access, DMA）", "DMA"),
    ("SystemVerilog Assertion, SVA", "SVA"),
    ("通用验证方法学（Universal Verification Methodology, UVM）", "UVM"),
    ("静态时序分析（Static Timing Analysis, STA）", "STA"),
    ("Synopsys Design Constraints, SDC", "SDC"),
]

LEAD_IN_PATTERNS = [
    "本节第一次作为主角使用的缩写如下，后文直接使用简称：",
    "本节第一次作为主角使用的缩写先列清楚，后文直接使用简称：",
    "这里先把几个缩写讲清楚，避免在协议定位表里裸写英文简称：",
]


def render_glossary() -> str:
    """
    @brief 将 GLOSSARY_GROUPS 内置术语字典渲染为 Markdown 格式的全局术语总表，
           按"系统与协议缩写""译码对象与算法"等分组组织，使读者可一站式查阅。
    @return 完整的 Markdown 文本，包含标题、分组表格和术语说明。
    """
    lines = [
        "# 译码讲义术语总表",
        "",
        "本章集中收纳 `docs/` 作者讲义中反复出现的术语、缩写和简要解释。其他讲义正文默认直接使用这些简称；只有当某一节正在讲解概念本身时，才在正文中补充上下文说明。",
        "",
    ]
    for heading, rows in GLOSSARY_GROUPS:
        lines.extend([f"## {heading}", "", "| 术语 | 中文/常用名 | 说明 |", "|:---|:---|:---|"])
        for term, cn, note in rows:
            lines.append(f"| {term} | {cn} | {note} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def is_term_heading(line: str) -> bool:
    """
    @brief 判断当前行是否为讲义内分散术语小节的标题，
           用于定位需要移除的冗余术语块边界。
    @param line 讲义中的一行文本。
    @return True 表示该行是"术语登场"/"本节缩写说明"/"本节术语"之一。
    """
    return line.strip() in {"## 术语登场", "## 本节缩写说明", "## 本节术语"}


def is_section_heading(line: str) -> bool:
    """
    @brief 判断当前行是否为 Markdown 二级标题。
    @param line 讲义中的一行文本。
    @return True 表示该行以 ## 开头。
    """
    return line.startswith("## ")


def is_non_terminology_heading(line: str) -> bool:
    """
    @brief 判断当前行是否为非术语/非缩写类的二级标题，
           在 remove_term_sections 中用于确定删除块的结束边界。
    @param line 讲义中的一行文本。
    @return True 表示该行是二级标题且不含"术语"或"缩写"关键字。
    @note 避免误删非术语内容：遇到不明确的标题会选择保留而非冒险删除。
    """
    if not is_section_heading(line):
        return False
    stripped = line.strip()
    return not ("术语" in stripped or "缩写" in stripped)


def remove_term_sections(text: str) -> str:
    """
    @brief 从讲义正文中删除分散的"术语登场""本节缩写说明"等冗余术语小节，
           使其不再在各文件间重复出现。
    @param text 讲义的原始 Markdown 全文。
    @return 删除术语小节后的文本，保留空白行格式完整性。
    @note 删除前会清理小节前的多余空行以避免产生双倍空行；
          遇到不明确的同类标题时会保留内容，防止误删正文。
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if is_term_heading(lines[i]):
            # Remove one blank line before a deleted heading to avoid double gaps.
            while out and out[-1] == "":
                out.pop()
            i += 1
            while i < len(lines):
                if is_non_terminology_heading(lines[i]):
                    break
                if is_section_heading(lines[i]) and not is_term_heading(lines[i]):
                    # Unknown terminology-like heading: keep it rather than risk deleting content.
                    break
                i += 1
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out).rstrip() + "\n"


def remove_lead_in_tables(text: str) -> str:
    """
    @brief 删除讲义中以引导句开头、后跟缩写表格的"前置缩写介绍"段落，
           其功能已被全局术语总表替代，保留会造成重复和维护负担。
    @param text 讲义的原始 Markdown 全文。
    @return 删除引导句和跟随的表格后剩余的文本。
    @note 仅匹配 LEAD_IN_PATTERNS 中预设的引导句式；
          删除时会连同引导句后的连续 Markdown 表格行一并移除。
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped in LEAD_IN_PATTERNS:
            while out and out[-1] == "":
                out.pop()
            i += 1
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            if i < len(lines) and lines[i].lstrip().startswith("|"):
                while i < len(lines) and (lines[i].lstrip().startswith("|") or lines[i].strip() == ""):
                    if lines[i].startswith("## "):
                        break
                    i += 1
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out).rstrip() + "\n"


def remove_orphan_abbreviation_tables(text: str) -> str:
    """
    @brief 删除讲义中无引导句、直接出现的孤立缩写表格（以特定表头开头），
           这些表格在术语集中后成为冗余碎片。
    @param text 讲义的原始 Markdown 全文。
    @return 删除孤立缩写表格后的文本，保留表格前后格式。
    @note 仅删除以预设表头行（如"| 缩写 | 全称 |"）开头的连续表格行；
          删除前会清理表前空行以避免残留空白。
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if (
            i + 1 < len(lines)
            and lines[i].strip() in {"| 缩写 | 全称 |", "| 中文名 | 英文全称 | 缩写 | 在本节中的作用 |"}
            and lines[i + 1].lstrip().startswith("|")
        ):
            while out and out[-1] == "":
                out.pop()
            i += 2
            while i < len(lines) and (lines[i].lstrip().startswith("|") or lines[i].strip() == ""):
                i += 1
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out).rstrip() + "\n"


def replace_expansions(text: str) -> str:
    """
    @brief 将讲义正文中的术语全名展开（如"第三代合作伙伴计划（3GPP）"）替换为缩写（如"3GPP"），
           减少冗余文字，使行文更紧凑，读者通过术语总表查全称即可。
    @param text 讲义的原始 Markdown 全文。
    @return 完成全名到缩写替换后的文本。
    @note 替换按模式长度降序执行，优先匹配长模式避免短模式覆盖长模式；
          额外包含少数 fixup 替换（如 NR LDPC 中间空格、3GPP 协议等硬编码修补）。
    """
    for old, new in sorted(EXPANSION_REPLACEMENTS, key=lambda item: len(item[0]), reverse=True):
        text = text.replace(old, new)
    text = text.replace("NR低密度奇偶校验码", "NR LDPC")
    text = text.replace("把3GPP", "把 3GPP")
    text = text.replace("新增3GPP", "新增 3GPP")
    text = text.replace("不是3GPP", "不是 3GPP")
    text = text.replace("解释3GPP", "解释 3GPP")
    text = text.replace("设计3GPP", "设计 3GPP")
    text = text.replace("不是NR", "不是 NR")
    text = text.replace("3GPP协议", "3GPP 协议")
    text = text.replace("传输块CRC", "TB CRC")
    text = text.replace("DUT可以是LTE Turbo单引擎、NR LDPC单引擎、NR Polar单引擎", "DUT 可以是 LTE Turbo 单引擎、NR LDPC 单引擎、NR Polar 单引擎")
    text = text.replace("本节所有矩阵和数字都是教学例子，不是NRconformance vector。", "本节所有矩阵和数字都是教学例子，不是 NR conformance vector。")
    text = text.replace("每篇讲义首次出现关键缩写时展开全称；本节后续不机械重复 3GPP/LTE/NR 全称。", "全项目重复术语集中到术语总表；各讲义正文不再机械重复全称。")
    text = text.replace("| 登记表 T9.3 | 解释 CBG 英文全称、中文含义、CB/TB 层级 | “TB、CB 与 CBG 的层级”。 |", "| 登记表 T9.3 | 说明 CBG、CB 与 TB 的层级关系 | “TB、CB 与 CBG 的层级”。 |")
    text = text.replace("| CBG 是 Code Block Group，CBGTI 是 Code Block Group Transmission Information | TS 38.212 缩写表 | `3GPP_Rel19/processed/TS_38.212_38212-j30/content.md:461-463` |", "| CBG/CBGTI 的协议缩写来源 | TS 38.212 缩写表 | `3GPP_Rel19/processed/TS_38.212_38212-j30/content.md:461-463` |")
    text = text.replace("| HARQ 是 Hybrid Automatic repeat Request | TS 38.212 缩写表 | `3GPP_Rel19/processed/TS_38.212_38212-j30/content.md:501` |", "| HARQ 的协议缩写来源 | TS 38.212 缩写表 | `3GPP_Rel19/processed/TS_38.212_38212-j30/content.md:501` |")
    return text


def update_reading_map_link(text: str) -> str:
    """
    @brief 在阅读地图文档的"前置知识检查"小节前插入全局术语入口链接，
           确保读者从入口文档就能导航到术语总表。
    @param text 阅读地图文档的原始 Markdown 全文。
    @return 插入术语入口段落后（或已存在时不动）的文本。
    @note 幂等操作：如果链接已存在则跳过，防止重复插入。
    """
    if "../L0/L0_terminology_glossary.md" in text:
        return text
    marker = "## 前置知识检查\n"
    note = (
        "## 全局术语入口\n\n"
        "全项目重复使用的术语、缩写和简要解释集中在 "
        "[译码讲义术语总表](../L0/L0_terminology_glossary.md)。本节和后续讲义默认直接使用这些简称，正文只在需要讲解概念本身时补充上下文。\n\n"
    )
    if marker in text:
        return text.replace(marker, note + marker, 1)
    return text


def process_lessons() -> int:
    """
    @brief 遍历 L1/L2/L3 所有讲义，依次执行术语删除、引导表移除、孤立表格清理
           和全名替换，对阅读地图额外插入术语总表链接。
    @return 实际被修改的讲义文件数量。
    @note 各文件仅当内容真正发生变化时才写入磁盘，避免无意义的时间戳更新。
    """
    changed = 0
    for root in LESSON_ROOTS:
        for path in sorted(root.glob("T*.md")):
            old = path.read_text(encoding="utf-8")
            new = remove_term_sections(old)
            new = remove_lead_in_tables(new)
            new = remove_orphan_abbreviation_tables(new)
            new = replace_expansions(new)
            if path == READING_MAP:
                new = update_reading_map_link(new)
            if new != old:
                path.write_text(new, encoding="utf-8")
                changed += 1
    return changed


def main() -> int:
    """
    @brief 脚本入口：默认干运行（dry-run）检查变更范围；指定 --write 后执行术语集中化操作，
           首先生成全局术语总表，再逐文件处理讲义。
    @return 0 表示成功或干运行完毕；非 0 表示异常。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if not args.write:
        print("dry_run=1")
        return 0

    GLOSSARY_PATH.write_text(render_glossary(), encoding="utf-8")
    changed = process_lessons()
    print(f"glossary={GLOSSARY_PATH}")
    print(f"changed_lessons={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
