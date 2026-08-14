---
type: definition
aliases:
  - RSC
  - Recursive Systematic Convolutional Code
  - 递归系统卷积码
tags:
  - 3gpp
  - concepts
  - turbo
  - rsc
  - encoder
source_spec: "TS 36.212 §5.1.3"
---

# RSC 递归系统卷积码

## 独立解释任务

任务目标：解释递归系统卷积码（Recursive Systematic Convolutional Code, RSC）的"递归"与"系统"两重结构，说明它为什么是 Turbo 码组成编码器的必然选择。在 LTE/NR 译码链路中的位置：RSC 是 LTE Turbo 编码器的基本组成单元——两个 8 状态 RSC 并行级联，译码端由 BCJR 算法沿对应网格（Trellis）译码。

## 科学定义

卷积码（Convolutional Code）的输出不仅由当前输入决定，还由过去 $m$ 个输入决定；$m$ 个寄存器产生 $2^m$ 个状态。"系统"指系统位直通输出（$x_k=u_k$），保证原始比特在码字中；"递归"指编码器含反馈回路。生成多项式统一写成：

$$
G(D)=\left[1,\ \frac{g_p(D)}{g_f(D)}\right]
$$

其中 $D$ 表示延迟一拍，$g_p(D)$ 为前馈多项式，$g_f(D)$ 为反馈多项式，分式表示二进制多项式意义下的递归滤波。LTE 组成编码器为 8 状态（$m=3$ 个寄存器），生成多项式 $G(D)=\left[1,(1+D+D^3)/(1+D^2+D^3)\right]$。反馈结构使有限冲激响应变为无限冲激响应，距离谱显著优于非递归码；交织后两个 RSC 看到的输入近似独立，这是 Turbo 迭代增益的来源。

## 直观模型

用 2 寄存器玩具 RSC（非 LTE 结构）手算。定义反馈内部比特 $v_k=u_k\oplus s_{2,k}$、校验 $p_k=v_k\oplus s_{1,k}\oplus s_{2,k}$、状态更新 $s_{1,k+1}=v_k$、$s_{2,k+1}=s_{1,k}$。初始状态 $(0,0)$，输入 $\mathbf{u}=[1,0,1,1]$，逐拍计算：(1) $k=0$：状态 $(0,0)$、$v_0=1$、$p_0=1$、下一状态 $(1,0)$；(2) $k=1$：状态 $(1,0)$、$v_1=0$、$p_1=1$、下一状态 $(0,1)$；(3) $k=2$：状态 $(0,1)$、$v_2=0$、$p_2=1$、下一状态 $(0,0)$；(4) $k=3$：状态 $(0,0)$、$v_3=1$、$p_3=1$、下一状态 $(1,0)$。系统输出 $\mathbf{x}=[1,0,1,1]$，校验输出 $\mathbf{p}=[1,1,1,1]$。注意 $k=1$ 时输入为 0 但 $p_1=1$——历史状态参与了校验，这正是"递归记忆"的体现。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 系统位与输入相同所以冗余无用 | 校验位提供跨时间约束；系统位让网格结构与译码初始化更简单。 |
| 递归只是把输入循环一遍 | 反馈把有限冲激响应变成无限冲激响应，显著改善距离谱。 |
| RSC 可以单独作为完整码 | 单独 RSC 纠错能力有限，必须与交织器加第二个 RSC 并行级联成 Turbo 码。 |
| 8 状态指 8 个寄存器 | 状态数 $2^m$；8 状态对应 $m=3$ 个寄存器。 |
| 生成多项式可以自行设计 | LTE 固定 $G(D)=\left[1,(1+D+D^3)/(1+D^2+D^3)\right]$，译码器必须与之匹配。 |

## 协议锚点

- TS 36.212 Rel-19 `36212-j30` §5.1.3（Turbo 编码总则）：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md` 行 683-703。
- TS 36.212 §5.1.3.2.1（两个 8 状态组成编码器结构）：`content.md` 行 721-745，`sections.jsonl` paragraph 403。
- TS 36.212 Figure 5.1.3-2（编码器结构图）：Word XML 邻近段落与 relationship `rId87 -> media/image79.wmf`。

## 图谱关联

- [[Turbo_码]]
- [[BCJR_Algorithm_BCJR算法]]
- [[Iterative_Decoding_迭代译码]]
- [[TBCC_咬尾卷积码]]
- [[GF2_伽罗瓦域]]
- [[T6.2_RSC_code_foundation]]
- [[T6.3_LTE_Turbo_encoder_trellis_termination]]
- [[概念图谱入口]]
- 关系语义：RSC 是 Turbo 编码的基本单元。
