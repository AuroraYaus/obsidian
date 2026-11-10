---
type: definition
aliases:
  - RV
  - Redundancy Version
  - 冗余版本
  - rvidx
  - k0
tags:
  - 3gpp
  - concepts
  - redundancy-version
source_spec: "TS 36.212 Rel-19 §5.1.4.1.2; TS 38.212 Rel-19 §5.4.2.1; TS 38.214 Rel-19 §5.1.3 and §6.1.4"
---

# RV 冗余版本

RV 描述一次传输选取哪一部分编码冗余。接收端用 RV 和协议表确定 rate recovery 的起点或区域，把本次 LLR 放回正确的 circular buffer 或 soft buffer 坐标。一句话本质：**RV 是速率匹配的起点参数——母码比特按 circular buffer 组织，每次传输按 RV 决定的起点取连续 `E` 个比特；接收端据此把本次 LLR 反算回缓冲区坐标，与已有软缓存合并**。

## 解释目标与范围

本节目标：把 RV 解释成 HARQ soft combining 的地址语义，而不是解释成“第几次重传”。

## 起源与演进

(1) **起点：母码比资源长。** 编码后的比特集合（Turbo 3K+12 / LDPC 母码）比本次资源能装的 E 个比特长得多——每次传输只能"截一段"，必须有一个参数说明截哪一段。这个参数就是 RV。

(2) **语义：起点参数，不是计数器。** RV0 通常给出初传常用起点；RV1/2/3 从不同起点取比特——它描述"这次发送母码的哪一部分冗余"，与"第几次重传"解耦：调度可以选择不同 RV 序列，也可以重复某个 RV。

(3) **接收端的角色：坐标恢复。** RV 是 rate recovery 地址生成的必要输入：LLR 必须按 RV 反算回 circular buffer 坐标，才能与旧软缓存正确合并——少了 RV，LLR 写错坐标；少了 HARQ process，新旧 TB 混到同一缓存。

(4) **环形缓冲区模型。** 母码比特集合按环形缓冲区组织，一次传输从 RV 起点取 E 个比特；重复位置的新旧 LLR 作为独立观测相加，未出现位置保留 soft buffer 旧状态（不能当业务 0）——这就是增量冗余的机制：后续传输补充新的校验证据，有效码率随重传逐步降低。

(5) **边界。** RV 必须与 CB 编号、E、Ncb 一起解释，速率匹配逐 CB 执行；LTE 的 rvidx（36.212 §5.1.4.1.2）与 NR 的 rvid（38.212 §5.4.2.1）各自成文。

## 科学定义

冗余版本是信道编码和速率匹配之后的选择参数。发送端通常已经得到一个比本次无线资源可承载长度更长的编码比特集合；速率匹配要从这个集合里抽取本次实际发送的 `E` 个 bit。RV 参与决定抽取起点、窗口或区域，因此它改变的是“这次发送哪部分编码冗余”。

对接收端来说，RV 的核心不是名字，而是坐标。接收机从 demapper 得到的是按空口顺序排列的 LLR 流；只有结合 RV、`E`、`Ncb`、CB 编号和调制阶数等 descriptor 字段，才能把这些 LLR 反向放回 rate matching buffer 或 soft buffer 的正确位置。

## 直观模型

编码后的母码比特集合按环形缓冲区组织；一次传输发送 `E` 个比特，`E` 一般小于缓冲区长度，因此每次只能覆盖环上的一段连续区间，区间的起点由 RV 决定。RV0、RV1、RV2、RV3 对应四个不同的起点：

- RV0 通常给出初传常用起点。
- 其他 RV 从不同区域取比特，覆盖此前未发送或可靠度不足的位置。
- 如果某些位置重复出现，接收端不是覆盖旧值，而是把新旧 LLR 作为独立观测相加。
- 如果某些位置本次没有出现，接收端保留 soft buffer 中的旧状态，不能把它当成业务 `0`。

这就是增量冗余的机制：后续传输并非重复同一起点，而是补充此前未发送或可靠度不足的校验证据，使有效码率随重传逐步降低。

## 数学与接收端动作

发送端的行为可抽象为：

```text
tx_bits = select(circular_buffer, RV, E)
```

接收端的反操作不是简单把第 `k` 个 LLR 写到第 `k` 个译码输入位置，而是：

```text
addr = inverse_rate_matching_address(RV, k, descriptor)
soft_buffer[addr] = saturating_add(soft_buffer[addr], rx_llr[k])
```

其中 `descriptor` 至少需要说明 HARQ process、CB 编号、RV、`E`、`Ncb`、调制阶数、是否新数据、CRC 状态和 soft buffer 生命周期。少了 RV，LLR 会写错坐标；少了 HARQ process，新旧 TB 会混到同一个缓存；少了 CRC 状态，缓存释放和保留会失控。

## 协议边界

LTE Turbo 中，`rvidx` 出现在 TS 36.212 Rel-19 §5.1.4.1.2 的 bit selection and pruning 语境中。它与 circular buffer、`Ncb`、`E` 和 soft buffer size 一起决定 rate matching 输出。

NR LDPC 中，`rvid` 出现在 TS 38.212 Rel-19 §5.4.2.1 的 LDPC bit selection 语境中。接收端要用同一套 RV/k0 规则恢复编码位置，再把 LLR 送入 LDPC 译码和 HARQ soft buffer。

TS 38.214 Rel-19 §5.1.3 和 §6.1.4 提供 PDSCH/PUSCH 调度上下文。调度侧告诉接收端本次传输使用哪个 RV、MCS、TBS 等字段；译码器侧把这些字段转成 rate recovery 和 buffer 管理动作。

## 常见误解

| 误解 | 为什么错 | 正确理解 |
|:---|:---|:---|
| RV 等于重传次数 | 调度可以选择不同 RV 序列，也可能重复某个 RV。 | RV 是冗余选择参数，不是计数器。 |
| 新 RV 一定没有重复位置 | circular buffer、limited buffer 和窗口长度可能导致重复。 | 重复位置应 LLR 累加，未出现位置保持。 |
| RV 只影响发送端 | 接收端必须用 RV 做反速率匹配地址生成。 | RV 是接收端 LLR 坐标恢复的必要输入。 |
| CRC fail 后丢掉旧 LLR | 失败传输仍可能提供有用软证据。 | HARQ soft buffer 通常保留同一 TB 的软信息等待重传。 |
| RV 可以脱离 CB 处理 | 速率匹配通常逐 CB 执行。 | RV 必须和 CB descriptor、`E`、`Ncb` 一起解释。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.4.1.2 Turbo bit selection and pruning。
- NR：TS 38.212 Rel-19 §5.4.2.1 LDPC bit selection。
- NR：TS 38.214 Rel-19 §5.1.3 PDSCH；§6.1.4 PUSCH 的调度上下文。

## 关键要点

1. RV 是冗余选择参数：决定"这次发送母码的哪一段"，不是重传计数器。
2. RV0 初传常用，RV1/2/3 从不同起点取比特，补充未见过或可靠度不足的位置。
3. 接收端用 RV 反算 LLR 坐标——rate recovery 地址生成的必要输入。
4. 重复位置 LLR 相加（独立观测合并），未出现位置保留旧软缓存。
5. RV 需与 CB 编号、E、Ncb 一起解释，速率匹配逐 CB 执行。
6. LTE rvidx 与 NR rvid 分属 36.212 §5.1.4.1.2 / 38.212 §5.4.2.1 各自条款。

## 图谱关联

- [[Chase_Combining_Chase合并]]
- [[Incremental_Redundancy_增量冗余]]
- [[Circular_Buffer_循环缓存]]
- [[概念图谱入口]]
- [[HARQ_混合自动重传请求]]
- [[Soft_Buffer_软缓存]]
- [[Rate_Matching_速率匹配]]
- [[T4.3_HARQ_soft_combining_basics]]
- [[T7.3_LTE_HARQ_soft_buffer_RV]]
- [[T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0]]
- [[E_Value_G_Value_E值与G值]]
- 关系语义：RV 规定重传证据在 rate matching buffer 中的坐标，是 HARQ soft combining 的地址来源。
