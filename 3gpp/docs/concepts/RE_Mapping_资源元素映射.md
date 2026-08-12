---
type: definition
aliases:
  - 资源元素映射
  - RE 映射
  - Resource Element Mapping
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §6.3.1.6/§7.3.1.5/§7.4.1"
---

# RE Mapping 资源元素映射

资源元素映射（Resource Element Mapping）把调制符号放进时频网格：按规则把符号序列填入 RB（资源块，Resource Block）内的 RE（资源元素，Resource Element，一个子载波×一个符号），同时避让参考信号占用的位置。它把「符号流」变成「网格」，是发送端物理信道处理的倒数第二环（预编码后、OFDM 生成前），也是接收端解映射（LLR 提取）的镜像。

## 独立解释任务

任务目标：讲清 RE 映射的填充规则（先频后时、符号到 (k,l) 的坐标映射）、参考信号避让（DMRS/CSI-RS/PTRS 占位与 rate matching around RS），以及 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）RE 映射的差异。

## 科学定义

### 填充规则

- 网格坐标：RE = (k, l)——k 是子载波索引（频域）、l 是符号索引（时域）；一个 RB 含 12 子载波 × 14 符号（常规 CP，见 [[Spectrum_and_Frequency_Point_频谱与频点]] 与 T2.3）。
- 先频后时：符号序列按「先填满频域（一个符号内所有子载波）、再推进时域」的顺序填入——与接收端解映射顺序一致（T2.6 的 LLR 提取顺序）。
- 分配粒度：PDSCH/PUSCH 按 RB 分配（调度器给的 RB 集，见 [[Scheduler_MAC调度器与资源分配]]），映射只发生在分配的 RB 内。

### 参考信号避让

网格里不是所有 RE 都放数据：DMRS（解调参考信号，Demodulation Reference Signal）/CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）/PTRS（相位跟踪参考信号，Phase Tracking Reference Signal）占用固定位置（TS 38.211 §7.4.1 位置表）——数据符号跳过这些 RE，接收端在译码前把这些位置置为中性 LLR（或按 RS 已知值处理）。这就是 **rate matching around RS**：发送端绕开 RS 打孔，接收端逆过程恢复。

### PDSCH/PUSCH 差异

- 下行 PDSCH：DMRS 占符号 2/3 等固定位置（front-loaded），CSI-RS 按配置插入；映射后经 OFDM 生成（多载波）。
- 上行 PUSCH：DMRS 位置由配置（映射类型 A/B）决定；DFT-s-OFDM 波形下先做变换预编码（DFT）再映射到连续子载波（见 [[DFT_sOFDM_上行波形]]）。

## 直观模型

RE 映射像「考场排座」：座位（RE）按行列（频域×时域）编号，考生（符号）按先排完一行再排下一行的顺序入座（先频后时）；监考老师（参考信号）占固定座位（DMRS/CSI-RS），考生绕开这些座位坐（rate matching around RS）——考完（接收端）按同样规则找回每个人的答卷（LLR）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| RE 映射可以随意排 | 先频后时是协议规定，收发必须一致（顺序错=LLR 错位） |
| 参考信号位置可自由选择 | DMRS/CSI-RS 位置由协议表+配置决定（TS 38.211 §7.4.1） |
| rate matching 是速率匹配的另一种叫法 | rate matching around RS 是「绕开参考信号打孔」，与信道编码的速率匹配（rate matching）是不同概念 |
| 映射在 OFDM 生成后 | 映射在预编码后、OFDM（IFFT）生成前——顺序：符号→层映射→预编码→RE 映射→OFDM |

## 协议锚点

- PDSCH RE 映射：TS 38.211（Rel-19 j30）§7.3.1.5，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- PUSCH RE 映射：TS 38.211 §6.3.1.6，本地同卷。
- 参考信号位置：TS 38.211 §7.4.1（DMRS/CSI-RS/PTRS 位置表），本地同卷。
- 网格坐标基础：T2.3（`docs/L1_基础/T2.3_NR_frequency_resource_grid.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[DMRS_解调参考信号]]
- [[Scheduler_MAC调度器与资源分配]]
- [[Modulation_Mapping_调制映射]]
- 关系语义：RE 映射是符号流到网格的最后一跳——填充规则（先频后时）与参考信号避让（rate matching around RS）决定接收端 LLR 提取顺序（T2.6）；调度器分配的 RB 集是映射范围，调制映射（批内）产出待映射符号。
