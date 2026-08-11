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
    "OSI": "开放式系统互联参考模型（Open Systems Interconnection Reference Model, OSI）",
    "PDCP": "分组数据汇聚协议（Packet Data Convergence Protocol, PDCP）",
    "SDAP": "服务数据适配协议（Service Data Adaptation Protocol, SDAP）",
    "RLC": "无线链路控制层（Radio Link Control, RLC）",
    "UL-SCH": "上行共享信道（Uplink Shared Channel, UL-SCH）",
    "DL-SCH": "下行共享信道（Downlink Shared Channel, DL-SCH）",
    "UCI": "上行控制信息（Uplink Control Information, UCI）",
    "DCI": "下行控制信息（Downlink Control Information, DCI）",
}

TECH_TERM_RE = {
    abbr: re.compile(rf"(?<![A-Za-z0-9]){re.escape(abbr)}(?![A-Za-z0-9])")
    for abbr in TECH_TERMS
}


def audit_technical_first_use(path: Path) -> list[str]:
    """@brief  检查单份讲义是否残留了自建术语表（分散的术语定义违反集中管理原则）。
    @param  path  待审计的 Markdown 文件路径。
    @return       违规列表；空列表表示该文件未违反术语集中化规则。
    @note  术语表文件本身不检查，因为它是唯一的合法定义源。"""
    errors: list[str] = []
    if path.resolve() == GLOSSARY_PATH.resolve():
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
