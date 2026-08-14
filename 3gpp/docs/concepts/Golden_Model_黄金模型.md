---
type: definition
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

## 独立解释任务

任务目标：解释黄金参考模型（Golden Model）的定义、工程布局与证据链要求——可复现输入、可解释协议身份、可回放随机性、可对比输出、可归档证据，并说明它为何成为定点化与寄存器传输级（Register Transfer Level, RTL）实现的正确性基准。在 LTE/NR 译码链路中，Golden Model 位于算法与硬件之间：Python 浮点模型先按 TS 36.212/38.212 协议链路验证译码算法，其输出性能上界与失败帧证据随后被 C/C++ 定点模型和 RTL 在比特精确（bit-exact）回归中逐项比对。

## 科学定义

Golden Model 是用浮点精度实现的译码参考模型，负责给出定点化与硬件实现不可超越的性能上界。若实现侧（定点/RTL）的块错误率（Block Error Rate, BLER）记为 $\mathrm{BLER}_{\mathrm{impl}}$，则：

$$
\mathrm{BLER}_{\mathrm{impl}}(E_b/N_0)\ge \mathrm{BLER}_{\mathrm{golden}}(E_b/N_0)
\tag{1}
$$

任何实现侧误差（量化、饱和、近似）只会让曲线变差，不会变好。工程布局按"稳定公共层 + 三类算法私有层"组织：`common/` 承载 descriptor、schema、seed、logging、metrics、vectors、evidence；`lte_turbo/`、`nr_ldpc/`、`nr_polar/` 分别承接 TS 36.212 与 TS 38.212 的协议链路；`vectors/` 区分 protocol、toy、random、regression 四类向量；`runs/` 归档每次运行的完整证据。随机性必须使用分层 seed 且禁止 Python 内置 `hash()`，可复现的派生算法为：

$$
s_{\mathrm{stage}}=\mathrm{uint64\_le}\left(\mathrm{SHA256}\left(\mathrm{canonical\_json}(s_{\mathrm{global}},\mathrm{run\_name},\mathrm{stage},\mathrm{frame\_id})\right)[0:8]\right)
\tag{2}
$$

式 (2) 中 $s_{\mathrm{global}}$ 是全局种子，`stage` 区分 payload/noise/edge_injection 等随机过程，`canonical_json` 表示字段排序、UTF-8 编码、无多余空白的规范化 JSON，`[0:8]` 取摘要前 8 字节按 little-endian 解释为 64 bit 整数。分层 seed 保证新增一个 stage 不会改变旧 stage 的随机序列。三类译码器的输出统一为公共 `DecodeResult`（decoded_bits、crc_pass、iterations_used、stop_reason），算法私有差异放入 `family_debug`。

## 直观模型

以一次失败帧的证据链为例。某次 LTE Turbo smoke test 第 137 帧失败，散装脚本可能只输出一行 `frame=137 crc_fail`，无法定位根因。按 Golden Model 布局，同一失败形成完整链条：(1) `run_id`（如 `2026-06-20T000000Z_lte_turbo_smoke`）定位运行目录；(2) `vector_id`（`lte_turbo_dl_sch_tb1024_rv0_seed20260620_f137_cb0`）唯一定位标准、信道、长度、冗余版本（Redundancy Version, RV）、seed 与码块（Code Block, CB）序号；(3) `protocol_refs` 指向 TS 36.212 §5.1.1/§5.1.2/§5.1.3.2/§5.1.4.1 说明 CRC、分段、Turbo 编码与速率匹配的来源；(4) `input_llr_hash` 确认重跑时 LLR 输入未变；(5) `seed_state` 记录 global/payload/noise 各层 seed；(6) `status` 说明 `crc_pass=false, stop_reason=MAX_ITER, iterations=8`；(7) `replay_command` 直接复现同一失败。replay 只读取归档输入与 seed state 复算，不重新随机生成关键输入——这样同一失败第二天也能逐字段复现。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| Golden Model 的代码一定完美 | 它是后续模型的参考基准，自身也必须经协议向量与回归验证。 |
| 只保存 seed 就能复现失败 | 还须分层 seed、resolved config、归档输入数组与协议 descriptor。 |
| 协议参数不需要写来源 | 每个 K/Zc/RV/CRC 类型都必须回链 TS 章节、本地路径或上游讲义。 |
| 三类译码器可以各写一套 status | 公共 `DecodeResult` 字段固定，算法私有差异放 `family_debug`，否则 scoreboard 要写三套。 |
| Golden Model 工程布局是 3GPP 规定 | 3GPP 只规定被仿真对象（CRC、编码、速率匹配），不规定包名、日志字段或种子格式。 |

## 协议锚点

- LTE 向量字段来源：TS 36.212 Rel-19 `36212-j30` §5.1.1、§5.1.2、§5.1.3.2、§5.1.4.1，本地 `3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`、`sections.jsonl`。
- NR LDPC 向量字段来源：TS 38.212 Rel-19 `38212-j30` §5.1、§5.2.2、§5.3.2、§5.4.2，本地 `3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`、`sections.jsonl`。
- NR Polar 向量字段来源：TS 38.212 Rel-19 `38212-j30` §5.1、§5.2.1、§5.3.1、§5.4.1、§6.3、§7.3。
- 系统级参数背景：TS 38.214 Rel-19 `38214-j30` §5.1.3、§6.1.4，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30/`。
- 标注：Golden Model 工程本身非 3GPP 标准内容——协议不规定 Python 包名、配置文件名、日志字段或随机种子格式；本节只登记向量来源，不重写协议公式。
- 本地讲义锚点：`docs/L3_工程实现/T17.1_python_golden_model_project_layout.md`。

## 图谱关联

- [[概念图谱入口]]
- [[Turbo_码]]
- [[LDPC_低密度奇偶校验码]]
- [[Polar_码]]
- [[Bit_Exact_Regression_比特精确回归]]
- [[Fixed_Point_Numbers_定点数]]
- [[T17.1_python_golden_model_project_layout]]
- [[T17.2_LTE_Turbo_float_sim_plan]]
- [[T17.3_NR_LDPC_float_sim_plan]]
- [[T17.4_NR_Polar_float_sim_plan]]
- [[T17.5_BER_BLER_curve_reporting]]
- 关系语义：Golden Model 是定点模型和 RTL 的正确性基准，所有 bit-exact 回归都与 Golden Model 比对。
