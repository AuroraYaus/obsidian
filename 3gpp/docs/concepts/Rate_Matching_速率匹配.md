---
type: definition
aliases:
  - Rate Matching
  - Rate Recovery
  - 速率匹配
  - 解速率匹配
  - de-rate matching
tags:
  - 3gpp
  - concepts
  - rate-matching
source_spec: "TS 36.212 Rel-19 §5.1.4; TS 38.212 Rel-19 §5.4.1 and §5.4.2"
queries: 1
---

# Rate Matching 速率匹配

速率匹配把编码后比特适配到本次可发送资源；接收端的 rate recovery 则把收到的 LLR 放回编码器母码或 circular buffer 坐标。它是 HARQ/RV 和译码核心之间的地址桥。一句话本质：**速率匹配是"按资源截长"的环节——母码是全书，本次传输只按 RV 起点挑 E 页打印，接收端再按页码放回原书**。

## 独立解释任务

任务目标：解释速率匹配如何连接无线资源数量、RV 和译码器输入坐标。

## 起源与演进

(1) **起点：母码长度与资源容量几乎总不相等。** 编码器输出的母码长度（Turbo 3K+12、LDPC 依基图、Polar 幂次长）与本次资源能装的比特数几乎总不相等——需要一个"按资源截长"的环节，这就是速率匹配。

(2) **链条：从资源算到每码块输出。** 总可用比特 G 由 PRB 数 × 可用 RE × 调制阶数 × 层数决定（TBS 查表源头 TS 36.213 §7.1.7 / 38.214 §5.1.3）；G 再按调制符号粒度切给各码块，得每码块输出 E（NR LDPC 见 TS 38.212 §5.4.2.1，LTE Turbo 见 TS 36.212 §5.1.4.1.2）。

(3) **机制：RV 起点 + 比特选择。** 从循环缓存按 RV 起点连续取出 E 个比特（打孔/重复/比特选择），输出序列记作 $e_k$（$k=0,\ldots,E-1$）——RV 换起点，重传就换一段母码。

(4) **与分段的边界。** K+/K- 是编码前的码块长度（受交织器合法表约束，最多差 24），e/E 是编码后的输出长度（受本次调度资源约束），两者隔着一整个编码器。

(5) **接收端与三制式。** rate recovery 把空口顺序 LLR 按地址放回母码坐标，punctured/filler/unknown 三种位置的 LLR 语义必须用 mask 区分——这是译码前的最后一道地址桥。三制式各有独立条款：LTE Turbo（36.212 §5.1.4）、NR Polar（38.212 §5.4.1）、NR LDPC（38.212 §5.4.2）。

## 科学定义

编码器输出的母码长度通常不等于本次无线资源承载的 bit 数。速率匹配通过 puncturing、repetition、shortening、interleaving 和 bit selection 等操作选择实际发送序列。接收端执行 rate recovery，把空口顺序 LLR 恢复到译码器需要的母码位置。

### G 值与 E 值的定量关系

G 是整张 TB 本次可用的编码比特总预算，$E_r$ 是其中分给第 r 个码块的切片。TS 38.212 §5.4.2.1 把两者定义在同一条款：G 是 "the total number of coded bits available for transmission of the transport block"，$E_r$ 是 "the rate matching output sequence length for the r-th coded block"。

对 PDSCH，G 由资源侧相乘得到：

$$G=N_{RE}\cdot Q_m\cdot N_L$$

其中 $N_{RE}$ 来自 TS 38.214 §5.1.3.2 第 1 步（每 PRB 的 $12N_{symb}^{sh}-N_{DMRS}^{PRB}-N_{oh}^{PRB}$ 个 RE，上限 156，再乘 PRB 数），$Q_m$ 是调制阶数，$N_L$ 是层数。38.214 第 2 步的 $TBS_{temp}=N_{RE}\cdot R\cdot Q_m\cdot\nu$ 与 G 共用同一个 $N_{RE}\cdot Q_m\cdot\nu$ 乘积：G 是编码后的预算，$TBS_{temp}$ 是编码前的预算，两者相差目标码率 R。

$E_r$ 的分配规则：令 $X=G/(N_LQ_m)$（以"每层一个调制符号"为单位的符号组数），$C'$ 为本次调度的 CB 数（无 CBGTI 时 $C'=C$），$R_{rem}=\mathrm{mod}(X,C')$。若 CBGTI 指示第 r 个 CB 未调度，$E_r=0$；否则前 $C'-R_{rem}$ 个调度 CB 取

$$E_r=N_LQ_m\left\lfloor\frac{X}{C'}\right\rfloor$$

后 $R_{rem}$ 个调度 CB 取

$$E_r=N_LQ_m\left\lceil\frac{X}{C'}\right\rceil$$

由此得到三条不变量：$\sum_r E_r=G$；每个 $E_r$ 都是 $N_LQ_m$ 的整数倍（调制符号对齐，保证 §5.4.2.2 的 $E_r/Q_m$ 行交织不出现半行）；$E_r$ 只由 G、$C'$、$N_L$、$Q_m$ 决定，与 $N_{cb}$、RV 无关。

数值例：$N_{RE}=1000$、$Q_m=4$、$N_L=2$ 时 $G=8000$、$X=1000$。C=3 且无 CBG：$R_{rem}=1$，前 2 个 CB 各得 $8\times333=2664$ bit，最后 1 个得 $8\times334=2672$ bit，合计 8000。若 CBGTI 只调度 3 个 CB 中的 2 个：$C'=2$、$R_{rem}=0$，两个调度 CB 各得 4000 bit，未调度 CB 的 $E_r=0$，合计仍是 8000。

接收端拿到的 LLR 流长度就是 G；它必须用同一组参数（TBS→C、$N_{RE}/Q_m/N_L$→G、CBGTI→C'）重算 $E_r$，再按 $E_r$ 切片。切片错一位，第 r 个 CB 之后的所有 LLR 都会错位——这正是 "$E_r$ 切分错，后续译码可能照常运行但 CRC 全部失败" 的根因。$E_r$ 与 $N_{cb}$ 的关系还决定比特选择的行为：$E_r<N_{cb}$ 时只取一段（打孔/缩短），$E_r>N_{cb}$ 时在循环缓存内绕回（重复）。

## 直观模型

速率匹配像从一本完整教材里按本次课时挑页打印。RV 告诉你从哪里开始挑，资源数量告诉你挑多少页。接收端拿到打印页后，要按页码放回原书，而不是按收到顺序直接阅读。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| rate recovery 只是补零 | 它是带地址和 mask 的反向映射。 |
| RV 只影响 HARQ | RV 直接影响 rate recovery 地址。 |
| punctured、filler、unknown 都一样 | 三者 LLR 语义不同，必须用 mask 区分。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.4 Turbo rate matching（G/E 分配见 §5.1.4.1.2）。
- NR Polar：TS 38.212 Rel-19 §5.4.1。
- NR LDPC：TS 38.212 Rel-19 §5.4.2；G、$E_r$、$C'$ 的定量关系在 §5.4.2.1，比特交织在 §5.4.2.2，级联输出 $g_0,\ldots,g_{G-1}$ 在 §5.5。
- 资源侧 G 来源：TS 38.214 Rel-19 §5.1.3.2（$N_{RE}$、$Q_m$、$\nu$、TBS）；CBG 调度：§5.1.7。

## 速率匹配在协议族中的分布（五层职责）

速率匹配横跨五层规范，每层回答不同问题——理解协议间联系的关键是"分层职责"：

| 协议层 | 回答的问题 | 代表 TS（本地 Rel-19 资料） |
|:---|:---|:---|
| 信道编码 | **算法本体**：母码按 RV 起点截出每 CB 的 E 比特（比特选择） | TS 36.212 §5.1.4（Turbo）/TS 38.212 §5.4.1（Polar）/§5.4.2（LDPC） |
| 物理层过程 | **可用资源总数 G 从哪来**（MCS/PRB 数 → TBS → G → 每 CB 输出 E） | TS 38.214 §5.1.3（NR PDSCH TBS）/TS 36.213 §7.1.7（LTE TBS） |
| 物理层控制 | **MCS/RV/资源分配由谁指示** | TS 38.212 §7.3（DCI 字段） |
| RRC 信令 | **哪些 RE 不能用**（rateMatchPattern 打孔/避让） | TS 38.331（RateMatchPattern IE） |
| MAC | **调度决策与 HARQ 信息**（TB 大小、重传 RV 选择） | TS 38.321 §5.3.2.2 |

**联系链**：MAC 决定 TB 大小与调度 → 213/214 定出总资源 G 与 TBS → 212 把母码按 RV 起点截出每 CB 的 E 比特 → 331 挖掉 rateMatchPattern 覆盖的 RE → 接收端 rate recovery 把 LLR 放回母码坐标（本笔记职责）。

## 关键要点

1. 速率匹配 = 按本次资源把母码截成 E 比特；$E_r$ 由总预算 G、调度码块数 $C'$ 与调制符号粒度 $N_LQ_m$ 分配，$\sum_r E_r=G$。
2. K+/K-（分段，编码前）与 e/E（速率匹配，编码后）是链条两端，勿混。
3. RV 决定从循环缓存哪个起点开始取比特——RV 换档 = 重传换母码片段。
4. rate recovery 是带地址与 mask 的反向映射，不是简单补零。
5. punctured/filler/unknown 三种位置 LLR 语义不同，必须区分。
6. 三制式各有独立条款：36.212 §5.1.4 / 38.212 §5.4.1 / §5.4.2。

## 图谱关联

- [[Circular_Buffer_循环缓存]]
- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[RV_冗余版本]]
- [[Soft_Buffer_软缓存]]
- [[CBG_码块组]]
- [[CB_码块]]
- [[TB_传输块]]
- [[Segmentation_码块分段]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[Polar_码]]
- [[T7.1_LTE_Turbo_de_rate_matching_overview]]
- [[T8.0_TS38212_chapter5_decoder_side_map]]
- [[T9.1_NR_LDPC_rate_recovery_overview]]
- [[T10.7_NR_Polar_rate_recovery]]
- [[E_Value_G_Value_E值与G值]]
- 关系语义：rate matching/recovery 决定 LLR 从空口顺序到译码核心坐标的映射；G 是整 TB 的总编码比特预算，$E_r$ 是切给第 r 个 CB 的份额，$\sum E_r=G$，CBG 未调度的 CB 取 $E_r=0$。
