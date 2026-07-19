#!/usr/bin/env python3
"""Audit centralized lesson terminology rules for the LTE/NR curriculum."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _md_utils import iter_markdown, line_for_offset, strip_code_fences


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GLOSSARY_PATH = PROJECT_ROOT / "docs" / "L0" / "L0_terminology_glossary.md"

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
    errors: list[str] = []
    if not GLOSSARY_PATH.is_file():
        return [f"{GLOSSARY_PATH}: glossary file is missing"]

    text = GLOSSARY_PATH.read_text(encoding="utf-8")
    for abbr in TECH_TERMS:
        if f"| {abbr} |" not in text:
            errors.append(f"{GLOSSARY_PATH}: glossary is missing {abbr}")
    return errors


def main() -> int:
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
