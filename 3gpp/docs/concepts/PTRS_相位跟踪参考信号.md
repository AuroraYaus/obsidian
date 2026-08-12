---
type: definition
aliases:
  - 相位跟踪参考信号
  - PTRS
  - Phase Tracking Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §7.4.1.4/§6.4.1.2; TS 38.214 Rel-19 §5.1.6.3/§6.2.3"
---

# PTRS 相位跟踪参考信号

PTRS（相位跟踪参考信号，Phase Tracking Reference Signal）解决高频段的相位噪声问题：毫米波/高频下振荡器相位噪声使接收信号产生公共相位误差（CPE，Common Phase Error），破坏星座旋转。PTRS 提供已知相位基准，接收端用它估计并补偿 CPE。它随数据一起发送（DL 在 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）、UL 在 PUSCH（物理上行共享信道，Physical Uplink Shared Channel）），密度随子载波间隔与调制阶数调整。

## 独立解释任务

任务目标：讲清相位噪声问题与 CPE 的影响、PTRS 的补偿原理（相位基准）、时频密度配置（与 SCS（子载波间隔，Subcarrier Spacing）和调制阶数的关系），以及 DL/UL PTRS 的部署差异。

## 科学定义

### 相位噪声与 CPE

高频段（FR2 毫米波）本地振荡器相位噪声显著：所有子载波共享同一相位误差（公共相位误差 CPE）——星座整体旋转，且随符号变化。CPE 若不补偿，256QAM（正交幅度调制，Quadrature Amplitude Modulation）等高阶调制的星座点距小、误码率急剧上升。

### PTRS 补偿原理

PTRS 是与数据同传的已知序列：接收端估计 PTRS 位置的相位偏移 → 插值得到每个符号的 CPE → 对数据符号做相位旋转校正（去旋转）。它只占少量 RE（资源元素，Resource Element），密度远低于 DMRS（解调参考信号，Demodulation Reference Signal）——因为 CPE 在频域近似恒定，只需少量频域点即可插值。

### 密度配置（与 SCS/调制阶数的关系）

| 维度 | 规则 |
|:---|:---|
| 频域密度 | 每 K 个 RB 一个 PTRS RE——SCS 越大 K 越大（大 SCS 相位噪声更小，可更稀疏） |
| 时域密度 | 每 L 个符号一个 PTRS——调制阶数越高 L 越小（高阶调制对相位更敏感，需更密） |
| 存在条件 | 仅配置了 PTRS 且调度资源足够时发送；未配置则无（data 传输照常） |

### DL/UL 差异

- DL PTRS：随 PDSCH 发送（TS 38.211 §7.4.1.4），与 DMRS 端口关联。
- UL PTRS：随 PUSCH 发送（TS 38.211 §6.4.1.2），DFT-s-OFDM 波形下与变换预编码交互（见 [[DFT_sOFDM_上行波形]]）。

## 直观模型

PTRS 像「画框上的水平仪」：画家（发送端）画完后给一条已知的水平线（PTRS），装裱师（接收端）发现画歪了（CPE）就按水平线整体摆正（相位校正）——画本身（数据）不用重画。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PTRS 是测量用的 | PTRS 是补偿相位噪声（CPE）的，不是 CSI 测量源 |
| PTRS 密度越高越好 | 高密度开销大——按 SCS/调制阶数自适应（大 SCS 稀疏、高阶调制加密） |
| 相位噪声只在毫米波有 | 低频也有但影响小——FR2 是主要应用场景 |
| PTRS 独立发送 | PTRS 随数据同传（PDSCH/PUSCH 内） |

## 协议锚点

- DL PTRS：TS 38.211（Rel-19 j30）§7.4.1.4，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- UL PTRS：TS 38.211 §6.4.1.2，本地同卷。
- 密度参数（timeDensity/frequencyDensity）：TS 38.214（Rel-19 j30）§5.1.6.3/§6.2.3，本地 `TS_38.214_38214-j30`。
- 相位噪声背景：T2.17（`docs/L1_基础/T2.17_OFDM_impairments_to_LLR.md` 手算例子提及）。

## 图谱关联

- [[概念图谱入口]]
- [[DMRS_解调参考信号]]
- [[CSI_RS_信道状态信息参考信号]]
- [[DFT_sOFDM_上行波形]]
- 关系语义：PTRS 是高频段可靠传输的保障——补偿 CPE 让高阶调制（256QAM）在高 SCS 下可用，与 DMRS（解调）/CSI-RS（测量）共同构成参考信号体系，UL 侧与 DFT-s-OFDM 波形交互。
