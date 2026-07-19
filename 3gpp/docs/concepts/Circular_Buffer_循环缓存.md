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
---

# Circular Buffer 循环缓存

CircBuf 是速率匹配的核心数据结构：编码比特按系统位→校验位顺序写入环形缓存，RV 定义起始位置 k₀，按输出长度 E 读取。

- **结构**：系统位在前，校验位在后。
- **Puncturing 打孔**：跳过比特→码率提高。
- **Shortening 缩短**：末尾比特不发送，接收端已知为 0。
- **Repetition 重复**：循环读取超过缓存长度→码率降低。
- **NR LDPC**：前 2Zc 比特总是打孔。

## 图谱关联

- [[Rate_Matching_速率匹配]]
- [[RV_冗余版本]]
- [[HARQ_混合自动重传请求]]
- [[T7.2_LTE_subblock_deinterleaver_circular_buffer]]
- [[T9.2_NR_LDPC_circular_buffer_states]]
- 关系语义：CircBuf 桥接编码器和调制器，适配码长到物理资源。
