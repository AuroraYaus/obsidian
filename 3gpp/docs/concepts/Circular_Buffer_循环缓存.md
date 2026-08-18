---
type: definition
aliases:
  - Circular Buffer
  - 循环缓存
  - CircBuf
  - Puncturing
  - Shortening
tags:
  - 3gpp
  - concepts
  - harq
  - circular-buffer
  - rate-matching
source_spec: "TS 36.212 §5.1.4; TS 38.212 §5.4"
queries: 1
---

# Circular Buffer 循环缓存

CircBuf（循环缓存，Circular Buffer）是速率匹配的核心数据结构：编码比特按系统位→校验位顺序写入环形缓存，RV（冗余版本，Redundancy Version）定义起始位置 $k_0$，按输出长度 $E$ 读取。

## 独立解释任务

任务目标：解释循环缓存如何用单一环形结构同时表达打孔、重复与不同 RV 起点，以及 LTE 与 NR 的结构差异。

## 科学定义

循环缓存长度记为 $N_{cb}$，输出序列按下式循环读取：

$$e_j = w_{(k_0 + j) \bmod N_{cb}}, \quad j = 0,1,\dots,E-1$$

其中 $w$ 为缓存内容，$k_0$ 为 RV 决定的起点，$E$ 为本次传输比特数；下标越界时模 $N_{cb}$ 绕回。LTE 的 $N_{cb}=3K_{\Pi}$：系统位、第一校验位、第二校验位各自经子块交织（sub-block interleaver）后顺序拼接。NR LDPC 的循环缓存由基图（Base Graph, BG）与提升因子决定，前 $2Z_c$ 位总是打孔，永不发送。

- **结构**：系统位在前，校验位在后。
- **Puncturing 打孔**：跳过比特→码率提高。
- **Shortening 缩短**：末尾比特不发送，接收端已知为 0。
- **Repetition 重复**：循环读取超过缓存长度→码率降低。
- **NR LDPC**：前 2Zc 比特总是打孔。

## 直观模型

类比循环播放列表：RV 决定从哪首歌开始播，$E$ 决定播多长，超出列表末尾就绕回开头。数值例子：LTE 每段交织长度 $K_{\Pi}=132$，缓存总长 396；RV=0 从系统位起点读 $E=300$ 位，相当于丢弃末尾 96 个校验位（打孔，码率提高）；若 $E=500$，读满 396 位后绕回头部再读 104 位（重复，码率降低）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 打孔位接收端直接丢弃 | 打孔位在接收端填 0 并标记为 unknown，其 LLR 参与后续解码但权重为零。 |
| RV=0 总是不打孔 | 打孔与 RV 的组合由协议表决定；NR LDPC 前 $2Z_c$ 位在任何 RV 下都不发送。 |
| 重复读取等于简单重发 | 重复与 RV 起点配合实现增量冗余，不同 RV 携带不同校验子集。 |
| LTE 与 NR 循环缓存结构相同 | LTE 是三段 $3K_{\Pi}$ 结构（Turbo）；NR LDPC 是按基图组织的单段环形结构，且固定打孔前 $2Z_c$ 位。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 `36212-j30` §5.1.4.1.1（子块交织与 NULL 填充）、Table 5.1.4-1（列间置换）、§5.1.4.1.2（bit collection 生成循环缓存）。
- NR：TS 38.212 Rel-19 `38212-j30` §5.4.2（LDPC rate matching 的 bit selection）、§5.4.2.1（bit selection 过程）。
- 本地锚点：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`（段落 791-965）；`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md:1175-1309`。

## 图谱关联

- [[Rate_Matching_速率匹配]]
- [[RV_冗余版本]]
- [[HARQ_混合自动重传请求]]
- [[Soft_Buffer_软缓存]]
- [[Incremental_Redundancy_增量冗余]]
- [[概念图谱入口]]
- [[T7.2_LTE_subblock_deinterleaver_circular_buffer]]
- [[T9.2_NR_LDPC_circular_buffer_states]]
- 关系语义：CircBuf 桥接编码器和调制器，适配码长到物理资源。
