---
type: definition
aliases:
  - PCCPCH
  - P-CCPCH
  - 主公共控制物理信道
  - Primary Common Control Physical Channel
tags:
  - 3gpp
  - concepts
  - umts
  - broadcast
source_spec: "TS 25.211 §5.3.3; TS 25.221; TS 36.133 §8.1.2.4.3"
queries: 1
---

# PCCPCH 主公共控制物理信道

PCCPCH（主公共控制物理信道，Primary Common Control Physical Channel）是承载广播信道 BCH 的下行公共物理信道，存在于 TD-SCDMA（写 PCCPCH）与 WCDMA（写 P-CCPCH）两代 3G 制式中——它是 UE 开机后读到的第一块系统信息的物理载体，与 P-CPICH（主公共导频信道）一字之差、职能相反。

## 独立解释任务

任务目标：解释 PCCPCH 在两代 3G 制式中的形态差异（TD-SCDMA 与 WCDMA 参数不同）、它与 BCH 的承载关系、与 P-CPICH 的一字之差辨析，以及知识库 36.133 里 PCCPCH RSCP 测量的由来。

## 科学定义

- **共性**：承载 BCH（广播信道），内容为系统广播信息（PLMN、码配置、邻区等）；公共信道全小区接收，无功率控制、以固定参考功率发射；不携带导频符号——信道估计统一借用 P-CPICH。
- **TD-SCDMA（PCCPCH）**：固定占用 TS0 时隙，使用两个 SF=16 信道化码组成的双码道，QPSK 调制，以小区最大功率发射（TS 25.221，1.28 Mcps TDD）。
- **WCDMA（P-CCPCH）**：固定速率 30 kbps、SF=256、信道化码 $C_{\mathrm{ch},256,1}$——码树上紧邻 P-CPICH 的 $C_{\mathrm{ch},256,0}$；每个时隙前 256 chips 预留给 SCH（同步信道），P-CCPCH 与 SCH 时分共存。
- **测量**：UTRA TDD 的 PCCPCH RSCP 是 LTE 侧对 UTRA TDD 的互操作测量量（TS 36.133 §8.1.2.4.3），出现在本地 36.133 测量表格中。

## 直观模型

类比小区门口的公告栏：内容人人可读、位置固定、长期有效。UE 开机第一件事就是去公告栏读"本小区说明书"（BCH），而"怎么把公告栏上的字读清楚"靠旁边那盏常亮灯（P-CPICH 导频做信道估计）。数值例子：WCDMA 中 P-CPICH 用码道 0、P-CCPCH 用码道 1——码树上相邻的两个码，正是"一字之差"的物理来源。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PCCPCH 与 P-CPICH 是同一信道的两种写法 | 不同信道：PCCPCH 承载 BCH 广播数据，P-CPICH 是纯导频参考 |
| PCCPCH 只在 TD-SCDMA 存在 | WCDMA 也有，写作 P-CCPCH（带连字符）；两者参数不同（TS0/SF=16 双码道 vs 30 kbps/SF=256） |
| PCCPCH 自带导频便于解调 | 3G 公共信道不携带导频，信道估计统一借用 P-CPICH；WCDMA 时隙前 256 chips 还预留给 SCH |
| LTE/NR 里有 PCCPCH | LTE/NR 用 PBCH 承载 MIB 取代之；PCCPCH 只出现在 3G 制式与 36.133 的 UTRA 互操作测量里 |

## 协议锚点

- 主定义：TS 25.211（WCDMA 物理信道与映射）§5.3.3 下行公共物理信道族（P-CCPCH）；TD-SCDMA 物理信道见 TS 25.221（1.28 Mcps TDD）。**本地 processed 库未收录 TS 25 系列**（仅 36/38 系列），本节以本地 36.133 互操作测量为锚点。
- 本地锚点：TS 36.133（Rel-19 j50）§8.1.2.4.3（E-UTRAN TDD – UTRAN TDD 测量，P-CCPCH RSCP 测量与 1.28 Mcps TDD 参数），本地 `3GPP_Rel19/processed/TS_36.133_36133-j50_s00-11/full.md:14844` 起。
- 演进对照：LTE/NR 广播承载 PBCH——TS 36.211 §6.6（本地 `TS_36.211_36211-j30_s06-s08`）与 TS 38.211 §7.3.3（本地 `TS_38.211_38211-j30`）。

## 图谱关联

- [[概念图谱入口]]
- [[PBCH_MIB_广播信道]]（LTE/NR 中广播承载的继任者）
- [[CPICH_公共导频信道]]（一字之差的辨析对象，且为其解调提供信道估计）
- [[PSS_SSS_同步信号与小区搜索]]（广播读取前的小区搜索流程）
- [[Pilot_导频]]（公共信道借导频解调的原理背景）
- 关系语义：PCCPCH 是 3G 时代"广播"的物理载体，其职能在 LTE/NR 由 PBCH 继承；它与 P-CPICH 构成"载数据 vs 供参考"的配对——名字相邻、码道相邻、职能相反，是信道缩写混淆的经典来源。
