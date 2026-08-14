---
type: definition
aliases:
  - Channel Polarization
  - 信道极化
  - Polar Transform
  - Frozen Bits
tags:
  - 3gpp
  - concepts
  - polar
  - polarization
source_spec: "Arikan 2009; TS 38.212 §5.3"
---

# 信道极化

## 独立解释任务

任务目标：解释极化码（Polar Code）的理论基石信道极化（Channel Polarization）——$N=2^n$ 个相同信道经生成矩阵变换后可靠性向两端分化的现象，以及信息位（Information Bit）与冻结位（Frozen Bit）的放置规则。

信道极化决定 NR 控制信道（PDCCH 承载的下行控制信息、PUCCH/PUSCH 承载的上行控制信息）Polar 编码与译码所用的信息集合，贯穿发送端 Polar 编码与接收端 SC/SCL 译码全链。

## 科学定义

Polar 码的基础变换核：

$$G_2 = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$$

$N$ 阶生成矩阵 $G_N = G_2^{\otimes n}$（Arikan 原始构造中还有位反转置换 $B_N$，NR 实现把它并入可靠性序列的索引约定）。对 $N$ 个独立且相同的二进制信道 $W$ 做 $G_N$ 变换后，得到 $N$ 个 bit-channel $W_N^{(i)},\ i=0,\dots,N-1$：当 $N\to\infty$ 时，一部分 bit-channel 容量趋于 1（完全可靠），另一部分趋于 0（完全噪声），其余占比趋于零。可靠位置放信息位，不可靠位置放冻结位（收发双方约定、NR 约定为 0）。冻结集 $\mathcal{F}$ 与信息集 $\mathcal{I}$ 必须互补且覆盖全部位置：

$$\mathcal{I}\cap\mathcal{F}=\varnothing, \qquad \mathcal{I}\cup\mathcal{F}=\{0,1,\dots,N-1\}$$

NR 的可靠性排序由 TS 38.212 §5.3.1.2 的可靠性序列 $Q$ 给出，母码最大长度 $N_{\max}=1024$（Table 5.3.1.2-1 共 1024 项），实际码长 $N$ 取表中所有小于 $N$ 的索引并保持相对顺序。

## 直观模型

$N=4$ 手算：取冻结集 $\{0,1\}$、信息集 $\{2,3\}$，输入 $\mathbf{u}=[0,0,a,b]$，经 $G_4$ 的 GF(2) 异或变换后信息位 $a,b$ 扩散到多个输出位。$N=2$ 的极简直觉：$x_0=u_0$、$x_1=u_0\oplus u_1$——判 $u_0$ 只有 $x_0$ 一个观测（弱），判 $u_1$ 有 $x_0,x_1$ 两个观测（强）："好的更好、差的更差"，递归放大即极化。注意这里的"极化"是编码变换后 bit 位置可靠性的分化，与天线极化无关。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 信道极化是天线极化 | 信道极化是编码变换后 bit-channel 可靠性向两端分化，与天线/电磁极化无关。 |
| 冻结位是编码后被删掉的比特 | 冻结位是编码前输入位置的固定值（通常 0），编码后仍参与输出。 |
| 冻结位与打孔位是一回事 | 冻结位是编码前约束；打孔位是编码输出未发送、接收端缺观测。 |
| 冻结位取值可以随便定 | 收发双方必须用同一约定（NR 约定 0）与同一 frozen mask。 |
| 信息位按自然顺序排 | NR 按 TS 38.212 Table 5.3.1.2-1 可靠性序列选信息位，不是自然顺序。 |

## 协议锚点

- TS 38.212 §5.3.1 Polar coding 与 §5.3.1.2 Polar sequence。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 815-837、873-943；Table 5.3.1.2-1 见 `tables/table_0012.csv/html`（1024 项）。信道极化理论本身源自 Arikan 2009 论文，非 3GPP 标准文件。
- 讲义：`docs/L2_协议算法/T10.2_channel_polarization_frozen_bits.md`；可靠性序列完整复现见 `docs/L2_协议算法/T10.3_NR_Polar_reliability_sequence.md`。

## 图谱关联

- [[Polar_码]]
- [[SCL_Decoding_SCL译码]]
- [[CA_SCL_CRC辅助SCL]]
- [[Information_Theory_信息论基础]]
- [[GF2_伽罗瓦域]]
- [[PDCCH_物理下行控制信道]]
- [[概念图谱入口]]
- [[T10.2_channel_polarization_frozen_bits]]
- [[T10.3_NR_Polar_reliability_sequence]]
- 关系语义：信道极化是 Polar 码理论基石，信息集/冻结集贯穿编码与译码全链。
