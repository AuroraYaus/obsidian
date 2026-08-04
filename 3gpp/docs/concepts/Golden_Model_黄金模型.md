---
type: algorithm
aliases:
  - Golden Model
  - 黄金模型
  - Float Reference Model
  - Python Simulation
  - BLER Baseline
tags:
  - 3gpp
  - concepts
  - engineering
  - simulation
  - golden-model
source_spec: "Engineering methodology; verified against TS 36.212/38.212 codec procedures"
---

# Golden Model 黄金模型

Golden Model 是用 Python 实现的浮点精度译码参考模型，作为定点化、RTL 实现和 bit-exact 回归验证的"黄金标准"。Golden Model 的输出是 BER/BLER 性能上界。

## 核心子概念

- **工程布局**：可复现、可追踪、可回放的 Python 项目结构。输入协议参数+噪声种子→输出 metrics.csv。
- **Turbo 浮点仿真**：按 TS 36.212 协议比特链路实现，Log-MAP/Max-Log-MAP 可选，生成 BLER vs Eb/N0 曲线。
- **LDPC 浮点仿真**：支持 BG1/BG2 切换、Zc 提升、SPA/MS/NMS/OMS 可选、分层/flooding 调度可选。
- **Polar 浮点仿真**：SC/SCL/CA-SCL 可选，L=1/4/8/16 可配，可靠性序列查表。
- **BLER 报告**：metrics.csv → 瀑布曲线 + error floor → 可复现性能证据。每个 SNR 点至少 1000 个 TB 错误。

## 图谱关联

- [[概念图谱入口]]
- [[Turbo_码]]
- [[LDPC_低密度奇偶校验码]]
- [[Polar_码]]
- [[T17.1_python_golden_model_project_layout]]
- [[T17.2_LTE_Turbo_float_sim_plan]]
- [[T17.3_NR_LDPC_float_sim_plan]]
- [[T17.4_NR_Polar_float_sim_plan]]
- [[T17.5_BER_BLER_curve_reporting]]
- 关系语义：Golden Model 是定点模型和 RTL 的正确性基准，所有 bit-exact 回归都与 Golden Model 比对。
