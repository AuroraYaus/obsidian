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
---

# CBG 码块组

CBG 是 NR 中把多个 CB 组合成部分重传粒度的对象。它不改变 LDPC 译码核心的校验矩阵，但会影响哪些 CB 被调度、哪些 soft buffer 位置需要合并或保持。

## 独立解释任务

任务目标：解释 CBG 如何把 NR HARQ 从整 TB 重传细化到一组 CB。

## 科学定义

CBG 是 code block group。NR 可以把一个 TB 分成多个 CB，再按规则把 CB 组织成 CBG。调度或反馈可以以 CBG 为粒度表达哪些 CB 组参与传输、重传或保持状态。

## 直观模型

如果 TB 是一本书、CB 是一页，CBG 就是一章。重传时不一定重传整本书，也不一定逐页管理，而是按章节告诉接收端哪些页组需要更新。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CBG 改变 LDPC 译码算法 | CBG 改变 HARQ/调度粒度，不改变单个 CB 的 LDPC 矩阵。 |
| 未调度 CBG 应清零 | 未调度通常表示保持旧 soft buffer 状态。 |
| CBG 和 CB 可以混用编号 | CBG 是 CB 的分组，二者粒度不同。 |

## 协议锚点

- NR：TS 38.214 Rel-19 §5.1.7 PDSCH CBG transmission。
- NR：TS 38.214 Rel-19 §6.1.5 PUSCH CBG transmission。
- 本地锚点示例：`3GPP_Rel19/processed/TS_38.214_38214-j30/content.md`。

## 图谱关联

- [[概念图谱入口]]
- [[CB_码块]]
- [[HARQ_混合自动重传请求]]
- [[Soft_Buffer_软缓存]]
- [[LDPC_低密度奇偶校验码]]
- [[T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0]]
- [[T9.6_NR_LDPC_decoder_edge_cases]]
- 关系语义：CBG 把 HARQ 部分重传语义映射到一组 CB 的 soft buffer 状态。
