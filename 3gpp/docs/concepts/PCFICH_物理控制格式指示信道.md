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

PCFICH（物理控制格式指示信道，Physical Control Format Indicator Channel）是 LTE 下行物理信道：每个子帧第 1 个 OFDM 符号上的 16 个资源元素（RE）承载 CFI（控制格式指示），告诉 UE 本子帧控制区域（PDCCH 的地盘）占用几个 OFDM 符号——它是 UE 解码 PDCCH 之前必须先读的第一块"路牌"。

## 独立解释任务

任务目标：解释 PCFICH 为什么是 LTE 下行接收的"先决信道"——它承载什么信息、放在哪里、怎么编码、UE 为什么必须先解它，以及 NR 为什么把这个角色整个删掉了。

## 科学定义

- **承载内容**：CFI（Control Format Indicator），取值 1/2/3，对应控制区域 OFDM 符号数；系统带宽 $N_{\mathrm{DL}}^{\mathrm{RB}} \le 10$ 时取 2/3/4（窄带宽需要更多符号才装得下同样大小的 DCI）。PCFICH 只承载这一个数，不承载任何调度内容。
- **信道编码**：CFI 按 TS 36.212 §5.3.4 表 5.3.4-1 查表编码为 32 bit 码字，QPSK 调制后得 16 个调制符号。
- **资源映射**：16 RE 组成 4 个 REG（资源元素组，每 REG 4 RE），全部落在子帧第 1 个 OFDM 符号，4 个 REG 在整个带宽上均匀分散；起始频域位置由小区 ID 决定（$v_{\mathrm{shift}} = N_{\mathrm{ID}}^{\mathrm{cell}} \bmod 6$），相邻小区 PCFICH 错开、互不重叠。
- **发射方式**：与 PBCH 相同的天线端口集（小区特定参考信号端口），调制为 QPSK（TS 36.211 表 6.7.2-1）。
- **先决性**：UE 必须先知道控制区域占几个符号，才能定位 PDCCH 的时频范围开始盲检——解 PCFICH 是解 PDCCH 的前提，PCFICH 因此放在位置固定、无需盲检的第一符号。

## 直观模型

类比进商场先看门口的"今日开放楼层"告示牌：牌子固定、内容就一个数、人人都能先读到。数值例子：20 MHz 带宽（100 RB）下 4 个 REG 各相隔约 25 RB 分散在带宽上，任何窄带干扰都很难同时打掉全部 4 个 REG——分散放置是 PCFICH 可靠性的设计来源。

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

## 图谱关联

- [[概念图谱入口]]
- [[PDCCH_物理下行控制信道]]（PCFICH 指示的控制区域就是 PDCCH 的地盘）
- [[DCI_下行控制信息]]（PDCCH 承载的调度内容本体）
- [[PBCH_MIB_广播信道]]（同为 LTE 控制域成员、同天线端口发射；NR 中 MIB 取代了 PCFICH 的职能）
- [[CRS_小区特定参考信号]]（PCFICH 解调依赖 CRS 信道估计）
- [[Physical_Channels_物理信道]]
- 关系语义：PCFICH 是 LTE 下行控制域的"开锁钥匙"——先解 PCFICH 得到控制区域符号数，才能定位并盲检 PDCCH 拿到 DCI；NR 时代这一职能被 MIB 的 pdcch-ConfigSIB1 收编。
