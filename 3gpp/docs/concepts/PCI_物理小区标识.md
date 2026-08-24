---
type: definition
aliases:
  - PCI
  - PCID
  - 物理小区标识
  - Physical Cell Identity
  - 物理小区ID
tags:
  - 3gpp
  - concepts
  - synchronization
  - cell-id
source_spec: "TS 38.211 §7.4.2.1; TS 36.211 §6.11"
queries: 1
---

# PCI 物理小区标识

PCI（物理小区标识，Physical Cell Identity，也写作 PCID）是网络为每个小区分配的物理层编号：UE 通过检测 PSS/SSS 自己推导出服务小区的 PCI，PCI 再作为"种子"决定下行几乎所有参考信号序列、加扰序列与资源位置——它是小区在物理层的"身份证号"。

## 独立解释任务

任务目标：解释 PCI 是什么、UE 怎么从同步信号推导它、它如何影响下行信号生成，以及网络规划时为什么必须同时避免 PCI 冲突与混淆。

## 科学定义

- **LTE**：$\mathrm{PCI} = 3 N_{\mathrm{ID}}^{(1)} + N_{\mathrm{ID}}^{(2)}$，其中 $N_{\mathrm{ID}}^{(1)} \in \{0,\dots,167\}$（小区 ID 组，168 组）、$N_{\mathrm{ID}}^{(2)} \in \{0,1,2\}$（组内编号），共 504 个。$N_{\mathrm{ID}}^{(2)}$ 由 PSS 检测（3 个候选序列），$N_{\mathrm{ID}}^{(1)}$ 由 SSS 检测。
- **NR**：$N_{\mathrm{ID}}^{\mathrm{cell}} = 3 N_{\mathrm{ID}}^{(1)} + N_{\mathrm{ID}}^{(2)}$，$N_{\mathrm{ID}}^{(1)} \in \{0,\dots,335\}$（336 组）、$N_{\mathrm{ID}}^{(2)} \in \{0,1,2\}$，共 1008 个。PSS 的 3 条 m 序列给出 $N_{\mathrm{ID}}^{(2)}$，SSS 的 336 条给出 $N_{\mathrm{ID}}^{(1)}$。
- **序列生成种子**：PCI 注入下行信号的多个环节——PSS/SSS 序列本身；LTE CRS 的频域移位 $v_{\mathrm{shift}} = N_{\mathrm{ID}}^{\mathrm{cell}} \bmod 6$；各物理信道加扰序列初始化 $c_{\mathrm{init}}$ 中的 $N_{\mathrm{ID}}^{\mathrm{cell}}$ 项；NR PBCH DM-RS 与 $i_{\mathrm{SSB}}$ 的联合指示。
- **规划双险**：(1) **冲突（collision）**——相邻同频小区 PCI 相同，参考信号与加扰相互污染、切换目标混淆；(2) **混淆（confusion）**——同一小区的两个邻区 PCI 相同，UE 测量报告无法区分目标小区。规划工具按复用距离分配 PCI 同时规避两者。

## 直观模型

类比身份证号：号码本身不承载信息，但开户、购票、办证都拿它做索引。PCI 同理——它不传数据，但 PSS/SSS 序列、导频频移、加扰码全从它派生；两个小区 PCI 相同就像身份证重号，所有"按号办事"的环节都会出错。数值例子：检测到 $N_{\mathrm{ID}}^{(2)}=1$（PSS 候选 1）、$N_{\mathrm{ID}}^{(1)}=100$，则 $\mathrm{PCI} = 3 \times 100 + 1 = 301$。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PCI 要先由网络配置才知道 | UE 开机后直接从 PSS/SSS 盲检测推导 PCI，不需要任何先验配置——这是小区搜索的核心产出 |
| LTE 与 NR 的 PCI 数量相同 | LTE 504 个（168×3），NR 1008 个（336×3） |
| PCI 相同只影响小区搜索 | PCI 是 CRS 频移与加扰初始化的种子，冲突会污染参考信号与加扰序列，干扰贯穿解调全程 |
| PCI 规划只要相邻不同即可 | 还要避免混淆：同一小区的两个邻区 PCI 相同，测量报告同样无法区分 |

## 协议锚点

- NR 物理小区标识定义：TS 38.211（Rel-19 j30）§7.4.2.1，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30/content.md:3657` 起；PSS/SSS 序列见 §7.4.2.2。
- LTE 同步信号与小区标识：TS 36.211（Rel-19 j30）§6.11，本地 `TS_36.211_36211-j30_s09-sxx`；CRS 频移 $v_{\mathrm{shift}}$ 计算见 §6.10.1.2。
- 加扰初始化含 $N_{\mathrm{ID}}^{\mathrm{cell}}$：LTE 见 TS 36.211 §6.3.1；NR PDSCH 加扰见 TS 38.211 §7.3.1.1（本地 `TS_38.211_38211-j30`）。

## 图谱关联

- [[概念图谱入口]]
- [[PSS_SSS_同步信号与小区搜索]]（PCI 的检测推导来源）
- [[CRS_小区特定参考信号]]（LTE 频移 v_shift 由 PCI 决定）
- [[Gold_序列加扰]]（加扰初始化种子之一）
- [[PBCH_MIB_广播信道]]（PBCH 加扰依赖小区 ID）
- 关系语义：PCI 是下行信号生成的"总种子"——PSS/SSS 检测推导出 PCI（同步笔记），PCI 再注入参考信号频移与加扰初始化（CRS/Gold 笔记），从小区搜索到解调全程参与。
