---
type: definition
aliases:
  - CBG
  - Code Block Group
  - 码块组
  - CBGTI
  - CBGFI
tags:
  - 3gpp
  - concepts
  - cbg
source_spec: "TS 38.214 Rel-19 §5.1.7 and §6.1.5"
queries: 1
---

# CBG 码块组

CBG 是 NR 中把多个 CB 组合成部分重传粒度的对象。它不改变 LDPC 译码核心的校验矩阵，但会影响哪些 CB 被调度、哪些 soft buffer 位置需要合并或保持。

## 独立解释任务

任务目标：解释 CBG 如何把 NR HARQ 从整 TB 重传细化到一组 CB。

## 科学定义

CBG 是 code block group。NR 可以把一个 TB 分成多个 CB，再按规则把 CB 组织成 CBG。调度或反馈可以以 CBG 为粒度表达哪些 CB 组参与传输、重传或保持状态。

## 直观模型

如果 TB 是一本书、CB 是一页，CBG 就是一章。重传时不一定重传整本书，也不一定逐页管理，而是按章节告诉接收端哪些页组需要更新。

CBG 的另一大用武之地是 URLLC（超可靠低时延通信）抢占场景：eMBB 的大块传输被 URLLC 业务中途打孔，只损局部 CB——按组重传受损段即可，无需全量重发（打孔与指示见 [[Preemption_Indication_抢占指示]]）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CBG 改变 LDPC 译码算法 | CBG 改变 HARQ/调度粒度，不改变单个 CB 的 LDPC 矩阵。 |
| 未调度 CBG 应清零 | 未调度通常表示保持旧 soft buffer 状态。 |
| CBG 和 CB 可以混用编号 | CBG 是 CB 的分组，二者粒度不同。 |

## 协议锚点

- NR：TS 38.214 Rel-19 §5.1.7 PDSCH CBG transmission（含 §5.1.7.1 分组公式、§5.1.7.2 接收流程）。
- NR：TS 38.214 Rel-19 §6.1.5 PUSCH CBG transmission（含 §6.1.5.2 发送流程）。
- 本地锚点示例：`3GPP_Rel19/processed/TS_38.214_38214-j30/content.md`。

## CBG 在协议族中的分布（五层职责）

CBG 横跨五层规范，每层回答不同问题——理解协议间联系的关键是"分层职责"：

| 协议层 | 回答的问题 | 代表 TS（本地 Rel-19 资料） |
|:---|:---|:---|
| 物理层过程 | CBG **怎么分组**（$M=\min(N,C)$）、**怎么调度/重传**（CBGTI 语义） | TS 38.214 §5.1.7（PDSCH 侧）/§6.1.5（PUSCH 侧） |
| 信道编码 | CB **从哪来**（TB 分段产生 $C$ 个 CB）、DCI 中 CBGTI/CBGFI **字段位宽** | TS 38.212 §7.2.3（分段）/§7.3.1（DCI 字段） |
| 物理层控制 | CBG 级 HARQ-ACK **反馈码本怎么构造**（每 CBG 一比特、按 CBG 索引升序） | TS 38.213 §9.1.1 CBG-based HARQ-ACK codebook determination |
| RRC 信令 | CBG **怎么配置**（开关、$N$ 取值、CBGFI 是否启用） | TS 38.331：IE `PDSCH-CodeBlockGroupTransmission`（`maxCodeBlockGroupsPerTransportBlock` ∈ {n2,n4,n6,n8}、`codeBlockGroupFlushIndicator`）与 `PUSCH-CodeBlockGroupTransmission` |
| MAC | HARQ 信息组成（NDI/RV/HARQ 进程 ID）与重传管理 | TS 38.321 §5.3.2.2 |

**联系链**：331 打开开关并给出 $N$（"允不允许用、最多几组"）→ 212 把 TB 切成 $C$ 个 CB、在 DCI 里留出 CBGTI/CBGFI 字段（"原料与令牌"）→ 214 把 CB 按 $M=\min(N,C)$ 分组、按 CBGTI 决定本次传哪些组（"怎么分组、传哪几组"）→ 213 定义每 CBG 一比特的反馈码本（"怎么汇报每一组的对错"）→ 321 站在 HARQ 实体角度管理进程与缓存（"重传的账本"）。整条链围绕一个目标：让收发双方对"这次传的是哪几组 CB"达成共同认知。

## 图谱关联

- [[概念图谱入口]]
- [[CB_码块]]
- [[HARQ_混合自动重传请求]]
- [[Soft_Buffer_软缓存]]
- [[LDPC_低密度奇偶校验码]]
- [[T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0]]
- [[T9.6_NR_LDPC_decoder_edge_cases]]
- [[Preemption_Indication_抢占指示]]
- 关系语义：CBG 把 HARQ 部分重传语义映射到一组 CB 的 soft buffer 状态。
