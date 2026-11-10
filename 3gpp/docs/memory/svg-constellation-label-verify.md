---
name: svg-constellation-label-verify
description: 星座图的比特标签必须用协议映射式反推核对（正向+反向 round-trip），「抄成邻点标签」在几何审计与肉眼检查下都隐形
metadata:
  type: feedback
---

2026-11-10 修 16QAM 映射符号时发现 `T2.1_16qam_constellation_carrier.svg` 4 个带标签点里 3 个错：`1011/0100/1110` 标在 (-3,+1)/(+3,-3)/(-1,-1) 上，规范应为 `1010/0111/1100`。

**根因**：错误形态是"抄邻点"（三个错标都是相邻点的正确标签）；`audit_svg_layout.py` 只查几何不查语义，目检也看不出标签与坐标不匹配。

**How to apply**：
1. 带比特标签的星座图，生成后必须跑 round-trip 核对：由坐标按映射式反推标签，与图内标签逐点比对，对照表贴进交付报告。
2. 正向（比特→坐标）与反向（坐标→标签）都要算；只做正向会漏错位。
3. 同一图多处出现标签（星座面板 + 波形面板）必须同步改。
4. 改后重渲 PNG 目检两面板一致。
5. 以 `Modulation_Constellations_调制星座.md` 及其配图的 16 点标签为权威参照（已程序化核对 16/16）。

相关：[[svg-audit-blind-spots]]、[[svg-render-cjk-font]]
