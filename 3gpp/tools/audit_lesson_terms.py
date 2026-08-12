#!/usr/bin/env python3
"""@file audit_lesson_terms.py
@brief 审计 Markdown 讲义中的术语首现规则——每份讲义不得自带术语表，
       所有技术缩写必须在全局术语表中统一定义，避免知识碎片化。
@date 2026-07-22

本工具扫描 L1/L2/L3 讲义，检查三个硬性约束：
1. 讲义正文中禁止出现自建术语表（集中化管理要求）
2. 全局术语表必须覆盖所有核心技术缩写
3. 发现违规即审计失败，阻断知识库不一致状态
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _md_utils import iter_markdown, line_for_offset, strip_code_fences


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GLOSSARY_PATH = PROJECT_ROOT / "docs" / "L0_协议阅读引导" / "L0_terminology_glossary.md"

# 整文件豁免（禁自建术语表检查）：术语表文件 + 概念清单索引（docs/concepts/ 下，
# 非讲义，其 `| 缩写 | 全称 |` 表头是清单自身的表格骨架，不构成"讲义自建术语表"）。
# 排除策略边界：同形/独立登记复合词（Log-MAP、CA-SCL、Qm.n、DM-RS）用
# _PRE/_POST_GUARDS 按词形排除；概念清单索引属整文件语义豁免——仅非讲义文件
# 且表头属自身骨架时才允许整文件豁免，讲义正文一律不得豁免（见 _TERM_POST_GUARDS 注释）。
EXEMPT_TERM_TABLE_FILES = {
    GLOSSARY_PATH.resolve(),
    (PROJECT_ROOT / "docs" / "concepts" / "3GPP全流程_缩写概念理论清单.md").resolve(),
}

TECH_TERMS = {
    "3GPP": "第三代合作伙伴计划（3rd Generation Partnership Project, 3GPP）",
    "LTE": "长期演进（Long Term Evolution, LTE）",
    "NR": "新空口（New Radio, NR）",
    "AWGN": "加性白高斯噪声（Additive White Gaussian Noise, AWGN）",
    "LLR": "对数似然比（Log-Likelihood Ratio, LLR）",
    "BPSK": "二进制相移键控（Binary Phase Shift Keying, BPSK）",
    "QPSK": "正交相移键控（Quadrature Phase Shift Keying, QPSK）",
    "QAM": "正交幅度调制（Quadrature Amplitude Modulation, QAM）",
    "CRC": "循环冗余校验（Cyclic Redundancy Check, CRC）",
    "HARQ": "混合自动重传请求（Hybrid Automatic Repeat Request, HARQ）",
    "TB": "传输块（Transport Block, TB）",
    "CB": "码块（Code Block, CB）",
    "RTL": "寄存器传输级（Register Transfer Level, RTL）",
    "ASIC": "专用集成电路（Application-Specific Integrated Circuit, ASIC）",
    "LDPC": "低密度奇偶校验码（Low-Density Parity-Check Code, LDPC）",
    "Turbo": "Turbo 码（Turbo Code）",
    "Polar": "极化码（Polar Code）",
    "BLER": "块错误率（Block Error Rate, BLER）",
    "MCS": "调制与编码方案（Modulation and Coding Scheme, MCS）",
    "TBS": "传输块大小（Transport Block Size, TBS）",
    "SRAM": "静态随机存取存储器（Static Random-Access Memory, SRAM）",
    "MAC": "媒体接入控制层（Medium Access Control, MAC）",
    "ARFCN": "绝对射频信道号（Absolute Radio Frequency Channel Number, ARFCN）",
    "GSCN": "全球同步信道号（Global Synchronization Channel Number, GSCN）",
    "OFDMA": "正交频分多址（Orthogonal Frequency Division Multiple Access, OFDMA）",
    "CDMA": "码分多址（Code Division Multiple Access, CDMA）",
    "TDMA": "时分多址（Time Division Multiple Access, TDMA）",
    "FDMA": "频分多址（Frequency Division Multiple Access, FDMA）",
    "WCDMA": "宽带码分多址（Wideband Code Division Multiple Access, WCDMA）",
    "ASK": "幅度键控（Amplitude Shift Keying, ASK）",
    "FSK": "频移键控（Frequency Shift Keying, FSK）",
    "PSK": "相移键控（Phase Shift Keying, PSK）",
    "DSSS": "直接序列扩频（Direct Sequence Spread Spectrum, DSSS）",
    "TBCC": "咬尾卷积码（Tail Biting Convolutional Code, TBCC）",
    "OSI": "开放式系统互联参考模型（Open Systems Interconnection Reference Model, OSI）",
    "PDCP": "分组数据汇聚协议（Packet Data Convergence Protocol, PDCP）",
    "SDAP": "服务数据适配协议（Service Data Adaptation Protocol, SDAP）",
    "RLC": "无线链路控制层（Radio Link Control, RLC）",
    "UL-SCH": "上行共享信道（Uplink Shared Channel, UL-SCH）",
    "DL-SCH": "下行共享信道（Downlink Shared Channel, DL-SCH）",
    "UCI": "上行控制信息（Uplink Control Information, UCI）",
    "DCI": "下行控制信息（Downlink Control Information, DCI）",
    "PDCCH": "物理下行控制信道（Physical Downlink Control Channel, PDCCH）",
    "PUCCH": "物理上行控制信道（Physical Uplink Control Channel, PUCCH）",
    "PDSCH": "物理下行共享信道（Physical Downlink Shared Channel, PDSCH）",
    "PUSCH": "物理上行共享信道（Physical Uplink Shared Channel, PUSCH）",
    "PBCH": "物理广播信道（Physical Broadcast Channel, PBCH）",
    "MIB": "主信息块（Master Information Block, MIB）",
    "SIB": "系统信息块（System Information Block, SIB）",
    "PSS": "主同步信号（Primary Synchronization Signal, PSS）",
    "SSS": "辅同步信号（Secondary Synchronization Signal, SSS）",
    "SSB": "同步信号块（Synchronization Signal Block, SSB）",
    "RNTI": "无线网络临时标识（Radio Network Temporary Identifier, RNTI）",
    "NDI": "新数据指示（New Data Indicator, NDI）",
    "RV": "冗余版本（Redundancy Version, RV）",
    "PMI": "预编码矩阵指示（Precoding Matrix Indicator, PMI）",
    "RI": "秩指示（Rank Indicator, RI）",
    "CQI": "信道质量指示（Channel Quality Indicator, CQI）",
    "RBG": "资源块组（Resource Block Group, RBG）",
    "VRB": "虚拟资源块（Virtual Resource Block, VRB）",
    "SRS": "探测参考信号（Sounding Reference Signal, SRS）",
    "PTRS": "相位跟踪参考信号（Phase Tracking Reference Signal, PTRS）",
    "TRS": "跟踪参考信号（Tracking Reference Signal, TRS）",
    "CRS": "小区特定参考信号（Cell-specific Reference Signal, CRS）",
    "CSI-RS": "信道状态信息参考信号（Channel State Information Reference Signal, CSI-RS）",
    "CORESET": "控制资源集（Control Resource Set, CORESET）",
    "CCE": "控制信道单元（Control Channel Element, CCE）",
    "REG": "资源元素组（Resource Element Group, REG）",
    "RE": "资源元素（Resource Element, RE）",
    "PRB": "物理资源块（Physical Resource Block, PRB）",
    "BWP": "带宽部分（Bandwidth Part, BWP）",
    "LCID": "逻辑信道标识（Logical Channel Identity, LCID）",
    "ADC": "模数转换器（Analog-to-Digital Converter, ADC）",
    "OFDM": "正交频分复用（Orthogonal Frequency Division Multiplexing, OFDM）",
    "CP": "循环前缀（Cyclic Prefix, CP）",
    "DFT": "离散傅里叶变换（Discrete Fourier Transform, DFT）",
    "IFFT": "逆快速傅里叶变换（Inverse Fast Fourier Transform, IFFT）",
    "FFT": "快速傅里叶变换（Fast Fourier Transform, FFT）",
    "MIMO": "多输入多输出（Multiple-Input Multiple-Output, MIMO）",
    "PRACH": "物理随机接入信道（Physical Random Access Channel, PRACH）",
    "UE": "用户设备（User Equipment, UE）",
    "RRC": "无线资源控制（Radio Resource Control, RRC）",
    "CBG": "码块组（Code Block Group, CBG）",
    "BCJR": "BCJR 算法（Bahl-Cocke-Jelinek-Raviv Algorithm, BCJR）",
    "MAP": "最大后验概率（Maximum A Posteriori, MAP）",
    "CA-SCL": "CRC 辅助连续消除列表译码（CRC-Aided Successive Cancellation List, CA-SCL）",
    "SCL": "连续消除列表译码（Successive Cancellation List, SCL）",
    "1024QAM": "1024 阶正交幅度调制（1024 Quadrature Amplitude Modulation, 1024QAM）",
    "Qm": "调制阶数（Modulation Order, Qm）",
    "SNR": "信噪比（Signal-to-Noise Ratio, SNR）",
    "SINR": "信干噪比（Signal-to-Interference-plus-Noise Ratio, SINR）",
    "BER": "比特错误率（Bit Error Rate, BER）",
    "FER": "误帧率（Frame Error Rate, FER）",
    "TDL": "抽头时延线（Tapped Delay Line, TDL）",
    "OCC": "正交覆盖码（Orthogonal Cover Code, OCC）",
    "SIMO": "单入多出（Single-Input Multiple-Output, SIMO）",
    "SISO": "软入软出（Soft-Input Soft-Output, SISO）",
    "CSI": "信道状态信息（Channel State Information, CSI）",
    "MMSE": "最小均方误差（Minimum Mean Square Error, MMSE）",
    "ZF": "迫零（Zero-Forcing, ZF）",
    "MF": "匹配滤波（Matched Filter, MF）",
    "MRC": "最大比合并（Maximum Ratio Combining, MRC）",
    "ML": "最大似然（Maximum Likelihood, ML）",
    "DMRS": "解调参考信号（Demodulation Reference Signal, DMRS）",
    "DM-RS": "解调参考信号（Demodulation Reference Signal, DM-RS）",
    "RSRP": "参考信号接收功率（Reference Signal Received Power, RSRP）",
    "PS": "概率整形（Probabilistic Shaping, PS）",
    "DM": "分布匹配（Distribution Matching, DM）",
    "ESS": "枚举球面整形（Enumerative Sphere Shaping, ESS）",
    "MB": "麦克斯韦-玻尔兹曼（Maxwell-Boltzmann, MB）",
    "SBPM": "整形比特位置映射（Shaped Bit Position Mapping, SBPM）",
    "GS": "几何整形（Geometric Shaping, GS）",
    "DUT": "被测设备（Device Under Test, DUT）",
    "DMA": "直接内存访问（Direct Memory Access, DMA）",
    "SVA": "系统 Verilog 断言（SystemVerilog Assertions, SVA）",
    "UVM": "通用验证方法学（Universal Verification Methodology, UVM）",
    "STA": "静态时序分析（Static Timing Analysis, STA）",
    "PPA": "功耗性能面积（Power Performance Area, PPA）",
    "DAC": "数模转换器（Digital-to-Analog Converter, DAC）",
    "PAPR": "峰均功率比（Peak-to-Average Power Ratio, PAPR）",
    "EVM": "误差矢量幅度（Error Vector Magnitude, EVM）",
    "PA": "功率放大器（Power Amplifier, PA）",
    "LUT": "查找表（Look-Up Table, LUT）",
    "CORDIC": "坐标旋转数字计算（Coordinate Rotation Digital Computer, CORDIC）",
    "SE": "频谱效率（Spectral Efficiency, SE）",
    "MACs": "乘加运算（Multiply-Accumulate operations, MACs）",
    "ROM": "只读存储器（Read-Only Memory, ROM）",
    "Hadamard": "阿达玛矩阵（Hadamard Matrix, Hadamard）",
    "Cholesky": "乔列斯基分解（Cholesky Decomposition, Cholesky）",
    "FR1": "频率范围 1（Frequency Range 1, FR1）",
    "FR2": "频率范围 2（Frequency Range 2, FR2）",
    "DFT-s-OFDM": "离散傅里叶变换扩展正交频分复用（Discrete Fourier Transform Spread OFDM, DFT-s-OFDM）",
    "SC-FDMA": "单载波频分多址（Single Carrier Frequency Division Multiple Access, SC-FDMA）",
}

# 防混淆守卫（负向断言）：登记缩写是更长复合词/独立词条的子串时，排除子串误匹配——
#   MAP：排除 Log_MAP/Log-MAP 前缀（Max_Log_MAP、Log-MAP 是独立复合算法名，讲义正文与
#        wikilink 均有使用）；Qm：排除 Qm.n 后缀（定点 Q 格式，术语表独立登记）；
#   SCL：排除 CA-SCL 前缀（CA-SCL 已独立登记，其内 SCL 子串不重复计数）。
# CA（载波聚合）未登记 TECH_TERMS（讲义零使用，仅术语表有行）；将来登记时必须加
#   "CA": r"(?!-)" 守卫，否则 "CA-SCL" 会被 CA 误匹配（连字符不阻断词边界）。
_TERM_PRE_GUARDS = {
    "MAP": r"(?<!Log[-_])",
    "SCL": r"(?<!-)",
}
_TERM_POST_GUARDS = {
    "Qm": r"(?!\.)",   # Qm.n（定点 Q 格式）不是调制阶数
    "DM": r"(?!-)",    # DM-RS 的 DM 是解调（DeModulation），不是分布匹配（Distribution Matching）
}

TECH_TERM_RE = {
    abbr: re.compile(
        rf"(?<![A-Za-z0-9]){_TERM_PRE_GUARDS.get(abbr, '')}{re.escape(abbr)}"
        rf"(?![A-Za-z0-9]){_TERM_POST_GUARDS.get(abbr, '')}"
    )
    for abbr in TECH_TERMS
}


def audit_technical_first_use(path: Path) -> list[str]:
    """@brief  检查单份讲义是否残留了自建术语表（分散的术语定义违反集中管理原则）。
    @param  path  待审计的 Markdown 文件路径。
    @return       违规列表；空列表表示该文件未违反术语集中化规则。
    @note  豁免文件见 EXEMPT_TERM_TABLE_FILES：术语表是唯一合法定义源；
          概念清单索引（3GPP全流程_缩写概念理论清单.md）非讲义，其表格骨架
          不触发禁自建术语表检查（T4 裁定，2026-08-12）。"""
    errors: list[str] = []
    if path.resolve() in EXEMPT_TERM_TABLE_FILES:
        return errors

    text = strip_code_fences(path.read_text(encoding="utf-8"))
    forbidden = [
        "## 术语登场",
        "## 本节缩写说明",
        "## 本节术语",
        "| 缩写 | 全称 |",
        "| 中文名 | 英文全称 | 缩写 |",
    ]
    for pattern in forbidden:
        idx = text.find(pattern)
        if idx >= 0:
            errors.append(
                f"{path}:{line_for_offset(text, idx)}: local terminology table remains: {pattern}"
            )
    return errors


def audit_glossary() -> list[str]:
    """@brief  验证全局术语表是否覆盖了所有核心技术缩写——
             缺失的术语会导致讲义中出现裸奔缩写，破坏可读性保障。
    @return  缺失条目列表；空列表表示术语表完整。
    @note   术语表缺失视为硬错误，因为它是所有讲义术语首现的权威来源。"""
    errors: list[str] = []
    if not GLOSSARY_PATH.is_file():
        return [f"{GLOSSARY_PATH}: glossary file is missing"]

    text = GLOSSARY_PATH.read_text(encoding="utf-8")
    for abbr in TECH_TERMS:
        if f"| {abbr} |" not in text:
            errors.append(f"{GLOSSARY_PATH}: glossary is missing {abbr}")
    return errors


def main() -> int:
    """@brief    脚本入口：扫描指定路径下的 Markdown 文件，执行术语首现规则审计。
    @usage    python audit_lesson_terms.py <path> [<path> ...]
    @args     paths  一个或多个 Markdown 文件或目录路径。
    @env      无外部依赖（仅标准库）
    @exit_code       0 = 所有文件通过审计；1 = 发现违规或术语表缺失。
    @note    审计失败时将输出详细错误行号和违规内容，便于定位修复点。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    files = iter_markdown(args.paths)

    errors: list[str] = []
    errors.extend(audit_glossary())
    for path in files:
        errors.extend(audit_technical_first_use(path))

    if errors:
        print("LESSON_TERM_AUDIT_FAIL")
        for error in errors:
            print(error)
        return 1

    print("LESSON_TERM_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
