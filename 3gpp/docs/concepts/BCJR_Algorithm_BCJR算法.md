---
type: definition
aliases:
  - BCJR
  - MAP Decoding
  - Forward-Backward Algorithm
  - Log-MAP
  - Max-Log-MAP
tags:
  - 3gpp
  - concepts
  - turbo
  - bcjr
  - algorithm
source_spec: "Bahl-Cocke-Jelinek-Raviv 1974; TS 36.212 algorithmic context"
---

# BCJR / MAP 译码算法

BCJR 是最优逐比特 MAP（最大后验概率，Maximum A Posteriori）译码算法，在网格图上运行前向 α 和后向 β 递归，输出每个信息比特的后验对数似然比（Log-Likelihood Ratio, LLR）。一句话本质：**BCJR 是"双向路网巡游"——α 从起点向终点累积证据、β 从终点向起点累积证据，两条证据在每条边上会合，才得到该比特的可靠度**。

## 独立解释任务

任务目标：解释 BCJR 为什么能给出最优逐比特判决，以及 Log-MAP 与 Max-Log-MAP 两种工程实现之间的精度与复杂度取舍。

## 起源与演进

(1) **起点：Viterbi 的局限。** 序列级硬判决译码（Viterbi）找最可能的整条路径，但 Turbo 迭代需要逐比特的软可靠度。1974 年 Bahl、Cocke、Jelinek、Raviv 四人提出逐比特 MAP 算法（BCJR），输出每个信息比特的后验 LLR——Turbo 迭代的软信息引擎由此而来。

(2) **机制：双向路网。** 网格图上 α 前向递归累积"至此路径的证据"，β 后向递归累积"此后路径的证据"；一条边的总证据 = 两段证据 × 边自身权重。逐比特判决取"该比特为 1 的所有边"与"为 0 的所有边"两类度量之和的对数比。

(3) **工程实现：log 域两档。** Log-MAP 用 $\max^*$（修正项 $\ln(1+e^{-|a-b|})$）精确实现；Max-Log-MAP 丢弃修正项，损失约 0.5 dB，但只需比较与加法——精度与复杂度的经典取舍。

(4) **边界：不止 Turbo。** 任何可用网格描述的码（卷积码、Turbo 分量码）与 ISI 信道均衡都能用 BCJR；TS 36.212 不规定译码器必须采用哪一种公式——算法选择属接收机实现域。

(5) **数值指向。** 某状态两条入边 γ=0.4/0.6、前向 α=0.3/0.2 → α(s)=0.24（未归一化）——多条路径到达同一状态的证据相加（逐拍推演见直观模型）。

## 科学定义

BCJR 在码的网格图上计算三类度量：

- **γ 分支度量**：由信道 LLR 与先验信息给出的状态转移概率。
- **α 前向递归**：

$$\alpha_k(s) = \sum_{s'} \alpha_{k-1}(s') \cdot \gamma_k(s' \to s)$$

- **β 后向递归**：

$$\beta_k(s) = \sum_{s'} \beta_{k+1}(s') \cdot \gamma_{k+1}(s \to s')$$

其中 $k$ 为时间步，$s, s'$ 为网格状态，$s' \to s$ 表示从状态 $s'$ 到 $s$ 的转移边。逐比特判决取"该比特为 1 的所有边"与"该比特为 0 的所有边"两类度量之和的对数比：

$$L(u_k) = \ln \frac{\sum_{(s',s):\, u_k=1} \alpha_{k-1}(s')\, \gamma_k(s' \to s)\, \beta_k(s)}{\sum_{(s',s):\, u_k=0} \alpha_{k-1}(s')\, \gamma_k(s' \to s)\, \beta_k(s)}$$

实际实现全部在 log 域进行：

- **Log-MAP**：$\max^*(a,b) = \max(a,b) + \ln(1+e^{-|a-b|})$，精确实现 BCJR。
- **Max-Log-MAP**：取 $\max^* \approx \max$，丢弃修正项，性能损失约 0.5 dB，但只需比较和加法。

## 直观模型

把网格图看成双向路网：α 递推从起点向终点累积"至此路径的证据"，β 递推从终点向起点累积"此后路径的证据"，一条边被采用的总证据等于两段证据与该边自身权重的乘积。数值例子：某状态有两条入边，边权 γ 分别为 0.4 与 0.6，对应前一状态的 α 为 0.3 与 0.2，则 α(s)=0.4×0.3+0.6×0.2=0.24（未归一化）——多条路径到达同一状态的证据相加。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| BCJR 只用于 Turbo 译码 | 任何可用网格描述的码（卷积码、Turbo 分量码）与符号间干扰（Inter-Symbol Interference, ISI）信道均衡都能用 BCJR。 |
| Max-Log-MAP 与 Log-MAP 等价 | Max-Log-MAP 丢弃修正项 $\ln(1+e^{-\lvert a-b\rvert})$，约损失 0.5 dB 增益。 |
| BCJR 输出硬判决比特 | BCJR 输出逐比特后验 LLR，软信息才能支撑迭代译码。 |
| α、β 各自独立就能给出判决 | 每比特判决需要 α 与 β 在同一条边上会合，二者缺一不可。 |

## 协议锚点

- LTE Turbo 编码结构：TS 36.212 Rel-19 `36212-j30` §5.1.3.2.1、Figure 5.1.3-2。
- 网格终止（尾比特）：TS 36.212 Rel-19 `36212-j30` §5.1.3.2.2。
- CRC 与码块分段：TS 36.212 Rel-19 `36212-j30` §5.1.1、§5.1.2。
- 本地锚点：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`。
- 协议边界：BCJR/Log-MAP/Max-Log-MAP 递推公式属于接收机算法背景，TS 36.212 不规定译码器必须采用哪一种公式。

## 关键要点

1. BCJR 是逐比特最优 MAP 译码，输出后验 LLR——Turbo 迭代的软信息来源。
2. 双向递归：α 前向 + β 后向，判决需要二者在同一条边上会合。
3. Log-MAP 精确（max* + 修正项）；Max-Log-MAP 省修正项、损失约 0.5 dB。
4. 1974 年 BCJR 四人提出；任何网格码/ISI 均衡都可用。
5. TS 36.212 不规定译码器必须用哪种公式——接收机实现域。
6. BCJR 不输出硬判决——软 LLR 才能支撑迭代。

## 图谱关联

- [[RSC_Code_递归系统卷积码]]
- [[Iterative_Decoding_迭代译码]]
- [[Turbo_码]]
- [[LLR_对数似然比]]
- [[Probability_Bayes_概率与贝叶斯]]
- [[概念图谱入口]]
- [[T6.5_BCJR_MAP_decoding_intuition]]
- [[T6.6_Log_MAP_Max_Log_MAP_Turbo]]
- 关系语义：BCJR 是 Turbo 译码的核心引擎。
