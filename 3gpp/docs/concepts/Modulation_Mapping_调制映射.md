---
type: definition
aliases:
  - 调制映射
  - Modulation Mapping
  - 星座映射
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §5.1"
---

# Modulation Mapping 调制映射

调制映射（Modulation Mapping）是发送端的比特到符号步骤：把编码后的比特按调制阶数分组，映射成复数调制符号（星座点）。NR 协议（TS 38.211 §5.1）定义了 QPSK（正交相移键控，Quadrature Phase Shift Keying）与 16/64/256QAM（正交幅度调制，Quadrature Amplitude Modulation）的星座表——每个星座点给出归一化的复数值。它是 [[ASK_FSK_PSK_键控调制]] 家族在 NR 协议中的落地，也是软解调（T2.13/T2.14）在发送端的镜像。

## 独立解释任务

任务目标：讲清调制映射的协议定义（星座表结构、比特分组、归一化因子）、各调制阶数的星座几何与能量归一化，以及 Qm（调制阶数，Modulation Order）与 MCS（调制与编码方案，Modulation and Coding Scheme）的关系。

## 科学定义

### 协议结构（TS 38.211 §5.1）

比特流按调制阶数 Qm 分组（QPSK:2、16QAM:4、64QAM:6、256QAM:8 比特/符号），每组映射为一个复数符号 $d = I + jQ$，星座点取值由协议表给出（Table 5.1-1 起：QPSK 4 点、16QAM 16 点、64QAM 64 点、256QAM 256 点）。

### 星座与归一化因子

| 调制 | Qm | 星座点数 | 归一化因子 | 最小点距 |
|:---|:---|:---|:---|:---|
| QPSK | 2 | 4 | $1/\sqrt{2}$ | 2/√2 |
| 16QAM | 4 | 16 | $1/\sqrt{10}$ | 2/√10 |
| 64QAM | 6 | 64 | $1/\sqrt{42}$ | 2/√42 |
| 256QAM | 8 | 256 | $1/\sqrt{170}$ | 2/√170 |

归一化因子让所有调制方式的**平均符号能量为 1**（$E_s = 1$）——这样功率预算与 MCS 无关，星座点距随阶数增大而缩小（256QAM 点距最小、对噪声最敏感——这就是为什么 256QAM 需要高 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio））。

### Qm 与 MCS 的关系

MCS 索引（见 [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]] 与 T9.0）直接给出 Qm 与目标码率 R——调度器选 MCS 即选调制阶数；DCI（下行控制信息，Downlink Control Information）里只有 MCS 索引，Qm 由表查得（[[DCI_下行控制信息]] 的 descriptor 映射）。

### 与键控调制家族的衔接

QPSK 是 [[ASK_FSK_PSK_键控调制]] 家族 PSK 的 2 bit/符号形态；16QAM 及以上是「幅度+相位联合键控」——QAM 是 PSK 的推广（家族演进见键控调制笔记）。

## 直观模型

调制映射像「点菜编号」：菜谱（星座表）上每个菜（星座点）有编号（比特组合）和坐标（复数值）；厨师（发送端）按编号出菜（发符号），客人（接收端）按坐标认菜（软解调）——菜谱要统一（协议表），才能对上号。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 星座图是设计自由发挥 | 星座点由协议表逐点规定（TS 38.211 Table 5.1-x），收发必须一致 |
| 256QAM 一定比 QPSK 好 | 256QAM 频谱效率高但点距小、对噪声敏感——高 SINR 场景才用 |
| 归一化因子可省略 | 省略会改变符号能量——功率口径、LLR 缩放全乱（T2.16 衔接） |
| Qm 在 DCI 里直接传 | DCI 只传 MCS 索引，Qm/R 查表得（T9.0） |

## 协议锚点

- 调制映射表：TS 38.211（Rel-19 j30）§5.1（Table 5.1-1 起），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- MCS/Qm 关系：TS 38.214（Rel-19 j30）§5.1.3（MCS 表），本地 `TS_38.214_38214-j30`。
- 软解调镜像：T2.13（BPSK/QPSK）/T2.14（QAM Max-Log-MAP），`docs/L1_基础/`。

## 图谱关联

- [[概念图谱入口]]
- [[ASK_FSK_PSK_键控调制]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[RE_Mapping_资源元素映射]]
- 关系语义：调制映射是发送端物理信道处理的第二环（加扰后）——比特变符号，星座表是收发一致的契约；Qm 由 MCS 决定（调度），符号能量归一化保证功率口径，接收端软解调（T2.13/T2.14）是它的精确镜像。
