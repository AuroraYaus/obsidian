---
type: definition
aliases:
  - SCL
  - Successive Cancellation List
  - 列表译码
  - Path Metric
tags:
  - 3gpp
  - concepts
  - polar
  - algorithm
  - scl
source_spec: "Algorithmic; TS 38.212 Polar decoder context"
---

# SCL 列表译码

## 独立解释任务

任务目标：解释逐次消除列表译码（Successive Cancellation List, SCL）的路径分裂、路径度量（Path Metric, PM）更新与剪枝机制，说明列表大小 $L$ 的工程含义与 L=1 退化为 SC 的关系。

SCL 是 NR Polar 控制信道接收链的译码核心，位于 rate recovery 之后、CRC 辅助选择（CA-SCL）之前。

## 科学定义

SCL 在每个信息位同时保留 0/1 两个候选，用 PM 度量路径与 LLR 证据的一致性。本知识库约定 PM 越小越好。LLR 域的 PM 更新精确式为：

$$\Delta PM(b,L)=\ln\!\left(1+\exp\!\left(-(1-2b)L\right)\right)$$

$$PM_{\mathrm{new}}=PM_{\mathrm{old}}+\Delta PM(b,L)$$

$b\in\{0,1\}$ 为候选比特，$L$ 为当前位 LLR。工程近似式：若 $b$ 与硬判决（$L$ 的符号）一致则 $\Delta PM\approx 0$，不一致则 $\Delta PM\approx |L|$——只需比较符号并加绝对值。每个信息位分裂出 $2L$ 条临时路径，按 PM 排序剪枝保留最小的 $L$ 条；冻结位不分裂，直接强制约定值（通常 0）。$L=1$ 退化为逐次消除（Successive Cancellation, SC）；NR 工程常用 $L=8$；$L$ 翻倍时 $f/g$ 计算、LLR 状态、路径存储与复制带宽都近似线性增长。

## 直观模型

$N=4,\ L=2$ 的路径表走读：$u_0,u_1$ 为冻结位（强制 0，PM 不变）；$u_2$ 为信息位、LLR=2.2，分裂出两条候选：$\Delta PM(u_2=0)=2.2$、$\Delta PM(u_2=1)=0$，路径 PM 分别为 2.2 与 0.0。$u_3$ 为信息位、LLR=1.1：两条路径各自再分裂，四条候选 PM 为 2.2、3.3、0.0、6.0，排序剪枝保留 0.0 与 2.2 两条。类比：迷宫每遇岔路不急着选一条，同时派 $L$ 支小队探索，定期按"偏离证据程度"（PM）淘汰落后小队。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PM 越大越好 | 本知识库约定 PM 越小越好（负对数似然惩罚）；方向反了剪枝全错。 |
| 冻结位也分裂 | 冻结位强制约定值，不分裂、不更新 PM。 |
| $L$ 越大性能必然更好 | $L$ 增大降低丢正确路径概率，但复杂度、SRAM 与复制带宽近似线性增长。 |
| PM 最小的路径一定输出 | 最终输出由 CRC（CA-SCL）决定，PM 最小路径可能 CRC 不过。 |
| SCL 是 3GPP 规定的算法 | 协议只规定 Polar 编码与码结构，SCL 与 PM 公式是接收机实现选择。 |

## 协议锚点

- TS 38.212 §5.3.1 Polar coding、§5.3.1.2 Polar sequence：决定信息集/冻结集与译码树结构。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 815-943。
- TS 38.212 §5.4.1 Polar rate matching：译码前 rate recovery 的协议依据。本地：`content.md` 行 1019-1125。SCL/PM 公式为非 3GPP 标准的接收机算法。
- 讲义：`docs/L2_协议算法/T10.5_Polar_SCL_decoding.md`；SC 基础见 `docs/L2_协议算法/T10.4_Polar_SC_decoding.md`。

## 图谱关联

- [[Channel_Polarization_信道极化]]
- [[CA_SCL_CRC辅助SCL]]
- [[Polar_码]]
- [[LLR_对数似然比]]
- [[PDCCH_物理下行控制信道]]
- [[概念图谱入口]]
- [[T10.5_Polar_SCL_decoding]]
- [[T10.4_Polar_SC_decoding]]
- 关系语义：SCL 是 Polar 译码核心算法，向上承接信息集/冻结集，向下交给 CA-SCL 做最终选择。
