---
type: definition
aliases:
  - PCFICH
  - 物理控制格式指示信道
  - 控制格式指示
  - CFI
tags:
  - 3gpp
  - concepts
  - lte
  - control-channel
source_spec: "TS 36.211 §6.7; TS 36.212 §5.3.4"
queries: 1
---

# PCFICH 物理控制格式指示信道

## 符号与记号约定
| 符号 | 含义与取值 | 协议锚点 |
|:---|:---|:---|
| $N_{\mathrm{DL}}^{\mathrm{RB}}$ | 下行系统带宽包含的资源块数，取 6 至 110，单位为资源块；由高层配置的下行带宽换算得到，取值不大于 10 时控制格式指示的取值范围改为 2、3、4。 | TS 36.212 §5.3.4 |
| $N_{\mathrm{ID}}^{\mathrm{cell}}$ | 小区标识，取 0 至 503，无量纲；由终端在小区搜索阶段从主同步信号与辅同步信号解出，是控制格式指示信道起始频域位置的唯一决定量。 | TS 36.211 §6.7.4 |
| $v_{\mathrm{shift}}$ | 频域起始偏移，取 0 至 5，单位为资源元素；由小区标识对 6 取模得到，使相邻小区的该信道在频域上错开而不重叠。 | 由 TS 36.211 §6.7.4 导出 |

运算符与记号惯例：$v_{\mathrm{shift}}=N_{\mathrm{ID}}^{\mathrm{cell}}\bmod 6$ 中的取模保证四个资源元素组的起点始终落在 0 至 5 之内，相邻小区的偏移因此必然错开；上标 `RB` 与 `cell` 是纯限定标记，不表示乘方；下标 `DL` 表示下行方向，与上行带宽的记号区分。

PCFICH（物理控制格式指示信道，Physical Control Format Indicator Channel）是 LTE 下行物理信道：每个子帧第 1 个 OFDM 符号上的 16 个资源元素（RE）承载 CFI（控制格式指示），指示本子帧控制区域（PDCCH 的时频范围）占用的 OFDM 符号数——它是 UE 解码 PDCCH 之前必须先读的先决信道。一句话本质：**PCFICH 是控制区域宽度的先决指示信道——时频位置由小区 ID 固定、载荷只有 CFI 一个取值（1/2/3，窄带宽 2/3/4）、在首符号全带宽上分散为 4 个 REG；终端先解出 CFI，才能确定 PDCCH 的符号范围并开始盲检**。

## 解释目标与范围

本节目标：解释 PCFICH 为什么是 LTE 下行接收的"先决信道"——它承载什么信息、放在哪里、怎么编码、UE 为什么必须先解它，以及 NR 为什么把这个角色整个删掉了。

## 前置概念

正交频分复用（Orthogonal Frequency Division Multiplexing, OFDM）把系统带宽划分为若干子载波、把时间划分为若干符号，一个子载波在一个符号上的最小时频单元称为资源元素（Resource Element, RE）；LTE 的一个资源块由 12 个子载波与 7 个符号组成。

资源元素组（Resource Element Group, REG）是控制信道映射的基本单位，一个 REG 由同一符号上四个相邻可用资源元素组成；控制信道以 REG 为单位分配，频率分集与参考信号开销因此同时得到照顾。

物理下行控制信道（Physical Downlink Control Channel, PDCCH）承载下行控制信息（Downlink Control Information, DCI），终端并不知道每个控制信道候选的确切位置与格式，必须在搜索空间内逐个候选尝试译码，这一过程称为盲检（Blind Decoding）。

控制格式指示（Control Format Indicator, CFI）是一个取值为 1、2、3 的整数，表示本子帧控制区域占用几个 OFDM 符号；窄带宽下取值改为 2、3、4，因为同样大小的下行控制信息需要更多符号才装得下。

小区特定参考信号（Cell-specific Reference Signal, CRS）是在整个带宽上均匀分布的已知序列，终端用它估计信道系数；该信道的解调与译码都要先有参考信号估计出的信道，因此它是前置条件。

## 起源与演进

(1) **起点：LTE 控制区域的动态宽度。** PDCCH 占几个 OFDM 符号每子帧可变——UE 必须先知道这个数才能定位 PDCCH 开始盲检。

(2) **CFI 编码与映射。** CFI（1/2/3，窄带宽 2/3/4）查表编码为 32 bit 码字、QPSK 得 16 符号，组成 4 个 REG 均匀分散在第一个符号全带宽上——分散是可靠性的设计来源。

(3) **先决性。** 位置固定、无需盲检、第一符号——解 PCFICH 是解 PDCCH 的前提。

(4) **起始位置由小区 ID 决定（$v_{\mathrm{shift}} = N_{\mathrm{ID}}^{\mathrm{cell}} \bmod 6$）**——相邻小区错开、互不重叠。

(5) **NR 的删除逻辑。** CORESET 是频域资源块、由 MIB 的 pdcch-ConfigSIB1 直接指示——不需要每子帧动态指示符号数，PCFICH 被收编。

## 科学定义

- **承载内容**：CFI（Control Format Indicator），取值 1/2/3，对应控制区域 OFDM 符号数；系统带宽 $N_{\mathrm{DL}}^{\mathrm{RB}} \le 10$ 时取 2/3/4（窄带宽需要更多符号才装得下同样大小的 DCI）。PCFICH 只承载这一个数，不承载任何调度内容。
- **信道编码**：CFI 按 TS 36.212 §5.3.4 表 5.3.4-1 查表编码为 32 bit 码字，QPSK 调制后得 16 个调制符号。
- **资源映射**：16 RE 组成 4 个 REG（资源元素组，每 REG 4 RE），全部落在子帧第 1 个 OFDM 符号，4 个 REG 在整个带宽上均匀分散；起始频域位置由小区 ID 决定（$v_{\mathrm{shift}} = N_{\mathrm{ID}}^{\mathrm{cell}} \bmod 6$），相邻小区 PCFICH 错开、互不重叠。
- **发射方式**：与 PBCH 相同的天线端口集（小区特定参考信号端口），调制为 QPSK（TS 36.211 表 6.7.2-1）。
- **先决性**：UE 必须先知道控制区域占几个符号，才能定位 PDCCH 的时频范围开始盲检——解 PCFICH 是解 PDCCH 的前提，PCFICH 因此放在位置固定、无需盲检的第一符号。

## 直观模型

它的设计约束是「必须先被读到、且只携带一个数」：位置固定、内容极短、在带宽上分散放置。数值例子：20 MHz 带宽（100 RB）下 4 个 REG 各相隔约 25 RB 分散在带宽上，任何窄带干扰都很难同时打掉全部 4 个 REG——分散放置是 PCFICH 可靠性的设计来源。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PCFICH 承载调度信息 | PCFICH 只承载 CFI 一个数（控制区域符号数）；调度信息在 PDCCH 里的 DCI 中 |
| 每个子帧都要盲检 PCFICH | PCFICH 的时频位置固定（由小区 ID 决定），UE 直接解，不需要盲检——盲检发生在 PDCCH |
| NR 也有 PCFICH | NR 删除了 PCFICH：CORESET 是频域资源块，由 MIB 的 pdcch-ConfigSIB1 直接指示，不需要每子帧动态指示符号数 |
| CFI 越大越好 | CFI 越大控制区域越大、留给 PDSCH 的资源越少——CFI 是控制开销与数据容量的折中 |

## 协议锚点

- LTE PCFICH 物理结构：TS 36.211（Rel-19 j30）§6.7（§6.7.1 加扰、§6.7.2 调制、§6.7.4 RE 映射），本地 `3GPP_Rel19/processed/TS_36.211_36211-j30_s06-s08/content.md:857` 起。
- CFI 信道编码：TS 36.212（Rel-19 j30）§5.3.4（§5.3.4.1 channel coding + Table 5.3.4-1 CFI 32 bit 码字），本地 `3GPP_Rel19/processed/TS_36.212_36212-j30/content.md:5583` 起。
- NR 对照（无 PCFICH）：PDCCH/CORESET 见 TS 38.211 §7.3.2（本地 `TS_38.211_38211-j30`）；MIB 的 pdcch-ConfigSIB1 字段见 TS 38.331 §6.2.2（本地 `TS_38.331_38331-j20`）。

## 关键要点

1. PCFICH 只承载 CFI 一个数——控制区域符号数。
2. 位置固定（小区 ID 决定）、无需盲检——盲检发生在 PDCCH。
3. 4 个 REG 均匀分散第一符号——抗窄带干扰。
4. CFI 是控制开销与数据容量的折中，不是越大越好。
5. NR 删除 PCFICH——CORESET 由 MIB 直接指示。
6. 解 PCFICH 依赖 CRS 信道估计。

## 图谱关联

- [[概念图谱入口]]
- [[PDCCH_物理下行控制信道]]（PCFICH 指示的控制区域即 PDCCH 的时频范围）
- [[DCI_下行控制信息]]（PDCCH 承载的调度内容本体）
- [[PBCH_MIB_广播信道]]（同为 LTE 控制域成员、同天线端口发射；NR 中 MIB 取代了 PCFICH 的职能）
- [[CRS_小区特定参考信号]]（PCFICH 解调依赖 CRS 信道估计）
- [[Physical_Channels_物理信道]]
- 关系语义：PCFICH 是 LTE 下行控制域的先决信道——先解 PCFICH 得到控制区域符号数，才能定位并盲检 PDCCH 拿到 DCI；NR 时代这一职能被 MIB 的 pdcch-ConfigSIB1 收编。
