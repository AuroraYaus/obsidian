---
type: definition
aliases:
  - CPICH
  - P-CPICH
  - 公共导频信道
  - 主公共导频信道
  - Common Pilot Channel
tags:
  - 3gpp
  - concepts
  - umts
  - pilot
source_spec: "TS 25.211 §5.3.3; TS 36.133 §8.1.2.4.1"
queries: 1
---

# CPICH 公共导频信道

CPICH（公共导频信道，Common Pilot Channel）是 WCDMA（UMTS）下行公共导频信道：小区用主扰码扩频、以固定功率连续发射的已知导频序列，供 UE 做相干解调的相位参考与切换/重选测量。主公共导频信道 P-CPICH 每个小区仅一个；它是 LTE CRS 与 NR SSB 在"公共参考"角色上的前身。

## 独立解释任务

任务目标：解释 P-CPICH 在 WCDMA 体系里的角色——它怎么发、UE 拿它做什么、LTE/NR 如何继承它的职能，以及知识库为什么会在 TS 36.133 互操作测量里反复遇到它。

## 科学定义

- **发射方式**：固定信道化码 $C_{\mathrm{ch},256,0}$、扩频因子 SF=256、固定速率 30 kbps（每时隙 10 个 QPSK 符号，1500 时隙/秒 × 10 符号 × 2 bit = 30 kbit/s），用小区主扰码（primary scrambling code）加扰；公共信道不做功率控制，恒定功率发射。
- **P-CPICH 与 S-CPICH**：P-CPICH 每小区唯一、覆盖全小区、码道固定；S-CPICH（辅公共导频信道）可选，配合波束赋形天线指向特定区域，可用任意 SF=256 信道化码。
- **三大用途**：(1) 相位参考——WCDMA 下行各信道（SCH/P-CCPCH/PICH 等）不自带导频，信道估计统一借用 P-CPICH；(2) 测量——CPICH RSCP（接收信号码功率）与 CPICH Ec/No（码片能量/噪声密度比）是小区选择、重选、切换的核心测量量；(3) 小区识别——小区搜索第三步靠检测 P-CPICH 的主扰码确认小区。
- **演进继承**：LTE 的 CRS 广播式参考信号、NR 的 SSB 继续扮演"小区级公共参考"角色，但解调参考（DM-RS）与测量参考的职能在 4G/5G 已分化。

## 直观模型

类比灯塔：塔本身不运货，但所有船靠它的光定位。P-CPICH 就是小区的常亮灯塔——内容 UE 本来就知道，UE 对比"收到的信号"与"本该有的信号"反推信道，再比亮度判断远近（RSCP/Ec/No 测量）。数值例子：30 kbps 固定速率意味着每个时隙恰好 10 个已知符号，UE 每时隙都能刷新一次信道估计。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CPICH 承载广播信息 | CPICH 是纯导频，不承载任何数据；广播信道 BCH 由 P-CCPCH 承载 |
| P-CPICH 与 P-CCPCH 是同一个东西 | 一字之差、角色相反：P-CPICH 供参考（导频），P-CCPCH 载数据（广播）——拼写混淆高发区 |
| CPICH 在 LTE/NR 中仍然存在 | LTE/NR 没有 CPICH；"公共参考"职能由 CRS（LTE）与 SSB（NR）继承 |
| RSCP 是接收功率绝对值 | CPICH RSCP 是解扩后的码功率；切换判决主要看比值量 CPICH Ec/No |

## 协议锚点

- 主定义：TS 25.211（WCDMA 物理信道与映射）§5.3.3 下行公共物理信道族。**本地 processed 库未收录 TS 25 系列**（仅 36/38 系列），本节以本地 36.133 互操作测量为锚点。
- 本地锚点（LTE 对 UTRA 的互操作测量）：TS 36.133（Rel-19 j50）§8.1.2.4.1（E-UTRAN FDD – UTRAN FDD 测量，CPICH RSCP/Ec-No 测量与滤波规则），本地 `3GPP_Rel19/processed/TS_36.133_36133-j50_s00-11/full.md:14677` 起；§A.9.3（UTRAN FDD CPICH RSCP 绝对精度测试），本地 `TS_36.133_36133-j50_sA.9-XX/full.md:12266`。
- 演进对照：LTE CRS 见 TS 36.211 §6.10.1；NR SSB 见 TS 38.211 §7.4.2.2/§7.4.3（本地 `TS_36.211_36211-j30_s09-sxx`/`TS_38.211_38211-j30`）。

## 图谱关联

- [[概念图谱入口]]
- [[Pilot_导频]]（导频/参考信号的通用原理）
- [[CRS_小区特定参考信号]]（LTE 的公共参考继承者）
- [[PSS_SSS_同步信号与小区搜索]]（WCDMA 小区搜索同样围绕主扰码/P-CPICH 展开）
- [[PCCPCH_主公共控制物理信道]]（一字之差的辨析对象）
- [[Spreading_扩频与解扩]]（SF=256 扩频背景）
- 关系语义：CPICH 是"公共参考信号"一脉的起点——WCDMA 靠它做相位参考与测量，LTE 用 CRS、NR 用 SSB/CSI-RS 延续同一职能；36.133 的 UTRA 互操作测量把它保留在 LTE 侧的测量对象里。
