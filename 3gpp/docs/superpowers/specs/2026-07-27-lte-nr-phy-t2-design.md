---
type: spec
aliases:
  - 2026-07-27-lte-nr-phy-t2-design
tags:
  - 3gpp
  - docs
  - superpowers
  - spec
source_spec: "docs/superpowers/specs/2026-07-27-lte-nr-phy-t2-design.md"
---
# T2.x 系列 PHY 系统背景讲义设计

## 元信息

| 项目 | 内容 |
|:---|:---|
| 设计日期 | 2026-07-27 |
| 范围 | `docs/L1/` 中新增 6 篇 T2.x 前置讲义（LTE/NR 物理层时频资源系统背景 + MCS），现有 T2.1–T2.5 整体后移 +6 |
| 参考源 | TS 38.211 §4（NR 物理信道与调制）、TS 36.211 §4/§6（LTE 帧结构与资源网格）、《5G移动通信系统设计与标准详解》（王映民 & 孙韶辉, 人民邮电出版社, 2020, `references/`）第 4 章 |
| 优先级规则 | 与 TS 38.211/36.211 冲突时以协议为准，讲义中需标注差异 |
| 风格 | 技术手册体，避免教学腔 |

## 搬迁方案

### 重命名清单

| 当前文件名 | 新文件名 |
|:---|:---|
| `T2.1_AWGN_noise_scaling.md` | `T2.7_AWGN_noise_scaling.md` |
| `T2.2_BPSK_QPSK_soft_demapping.md` | `T2.8_BPSK_QPSK_soft_demapping.md` |
| `T2.3_QAM_Max_Log_MAP_demapping.md` | `T2.9_QAM_Max_Log_MAP_demapping.md` |
| `T2.4_fading_channel_LLR_reliability.md` | `T2.10_fading_channel_LLR_reliability.md` |
| `T2.5_LLR_clipping_scaling_quantization.md` | `T2.11_LLR_clipping_scaling_quantization.md` |

### 引用更新范围

以下文件引用了 T2.1–T2.5 的编号，需同步更新（audit/superpowers 历史记录除外）：

| 文件 | 引用了 |
|:---|:---|
| `docs/L1/T1.4_probability_bayes_soft_decoding.md` | T2.2→T2.8, T2.3→T2.9 |
| `docs/L1/T1.5_LLR_soft_decision.md` | T2.2→T2.8, T2.3→T2.9 |
| `docs/L1/T2.8_BPSK_QPSK_soft_demapping.md` | T2.1→T2.7 |
| `docs/L1/T2.9_QAM_Max_Log_MAP_demapping.md` | T2.1→T2.7, T2.2→T2.8, T2.5→T2.11 |
| `docs/L1/T2.10_fading_channel_LLR_reliability.md` | T2.1→T2.7, T2.2→T2.8, T2.3→T2.9 |
| `docs/L1/T2.11_LLR_clipping_scaling_quantization.md` | T2.1→T2.7, T2.4→T2.10 |
| `docs/L1/T3.4_NR_LDPC_segmentation_rules.md` | T2.5→T2.11 |
| `docs/L1/T3.5_NR_Polar_segmentation_crc.md` | T2.5→T2.11 |
| `docs/L1/T4.5_decoder_performance_metrics.md` | T2.1→T2.7 |
| `docs/L2/T9.1_NR_LDPC_rate_recovery_overview.md` | T2.5→T2.11 |
| `docs/L2/T9.2_NR_LDPC_circular_buffer_states.md` | T2.5→T2.11 |
| `docs/L2/T9.4_NR_LDPC_bit_deinterleaving.md` | T2.2→T2.8, T2.3→T2.9, T2.5→T2.11 |
| `docs/L2/T10.7_NR_Polar_rate_recovery.md` | T2.5→T2.11 |
| `docs/L3/T12.2_LTE_Turbo_float_sim_plan.md` | T2.2→T2.8 |
| `docs/L3/T13.1_fixed_point_decoder_requirements.md` | T2.5→T2.11 |

---

## T2.1 — OFDM 原理与子载波间隔基础

### 定位

T2 系列入口。建立 OFDM 多载波传输的物理直觉——子载波正交性、循环前缀机制、IFFT/FFT 实现框架。后续 Numerology、帧结构、资源网格均以此为基础。

### 知识要点

1. 多载波传输的引入动机——频率选择性衰落信道中单载波均衡复杂度高，多载波将宽带信道分割为若干平坦子信道
2. 子载波正交条件的数学推导——从内积出发：$\int_0^{T} e^{j2\pi f_k t} \cdot e^{-j2\pi f_m t} dt = 0 \iff \Delta f = 1/T_u$，其中 $T_u$ 为有用符号时长
3. 循环前缀（CP）的机制——将 OFDM 符号末尾一段复制到符号前端，使多径时延扩展小于 CP 长度时不产生子载波间干扰（ICI）和符号间干扰（ISI）
4. OFDM 调制解调的 IFFT/FFT 实现——$N$ 点 IFFT 将频域调制符号映射到时域 OFDM 符号，接收端 FFT 还原
5. "载波"（carrier, $f_c$）与"子载波"（subcarrier, $k \cdot \Delta f$）的区分——前者是射频中心频率，后者是基带频域格点
6. **OFDM 符号（OFDM symbol）与调制符号（modulation symbol）的严格区分**——OFDM 符号是时域概念，指一个包含 CP + $N$ 点 IFFT 输出的时间片段，时长 $T_{symbol} = T_u + T_{CP}$；调制符号是频域概念，指星座图上的一个复数点（BPSK = $\pm 1$，QPSK = $\pm 1 \pm j$，16QAM = 16 个格点之一），每个调制符号承载 $Q_m$ 个比特。两者的关系是：一个 OFDM 符号周期内，$N$ 个子载波各承载一个调制符号，即 $N$ 个调制符号并行通过 IFFT 变换为一个 OFDM 符号。在 T3.2 等后续章节中，"调制符号"指的就是后者（constellation symbol），"码块中的比特映射为调制符号"意为编码比特经星座映射后变为复数符号，而非映射为 OFDM 符号

### 协议入口

- TS 38.211 §4.2 — OFDM 基带信号生成公式
- TS 36.211 §6 — LTE OFDM 基带信号生成
- 参考书 §4.2（P73-78）

### 核心公式

| 内容 | 公式 |
|:---|:---|
| OFDM 基带信号 | $s(t) = \sum_{k=0}^{N-1} d_k \cdot e^{j2\pi k\Delta f t}, \quad 0 \leq t < T_u$ |
| 子载波正交条件 | $\Delta f = 1/T_u$ |
| CP 后的完整符号时长 | $T_{symbol} = T_u + T_{CP}$ |
| CP 的多径容忍条件 | $T_{CP} \geq \tau_{max}$（最大多径时延扩展） |

### 前置知识

- 复数与欧拉公式 $e^{j\theta} = \cos\theta + j\sin\theta$
- 傅里叶变换的直觉（时域波形 ↔ 频域谱线，不做严谨数学展开）
- I/Q 分量（同相/正交）的基本概念

### 与后续衔接

- T2.2 展开 $\Delta f = 15 \cdot 2^\mu$ kHz 的具体数值和完整时域层级
- T2.7（AWGN 噪声缩放）中噪声独立加在每个子载波上的前提建立于此处的子载波正交性

### 图示

1. OFDM 调制解调全链路框图（Mermaid flowchart: 调制符号 → IFFT → +CP → 信道 → -CP → FFT → 解调符号）
2. 子载波正交性频域示意图（N 个 sinc 函数在 Δf 整数倍处过零）
3. CP 消除 ISI 的前后对比图

---

## T2.2 — NR Numerology 与时域层级

### 定位

承接 T2.1 的 Δf 概念，展开 NR 的五套 Numerology（μ=0–4）及其对时域结构的完整层级链。核心是一张公式链：从单一参数 μ 可推算出从 OFDM 符号到无线帧的全部时域参数。

### 知识要点

1. NR 引入多套 Numerology 的技术原因——eMBB 大带宽需求对应大 SCS 短符号；uRLLC 低时延对应大 SCS 短时隙；mMTC 广覆盖对应小 SCS 长符号；毫米波频段需大 SCS 对抗多普勒频偏导致的子载波间干扰
2. 核心公式链：$\mu \to \Delta f = 15 \cdot 2^\mu \text{ kHz} \to T_u = 1/\Delta f \to T_{symbol} = T_u + T_{CP} \to T_{slot} = 14 \cdot T_{symbol} \to T_{subframe} = 1\text{ ms} \to T_{frame} = 10\text{ ms}$
3. TS 38.211 Table 4.3.2-1 的完整映射——参数集 μ 与 Δf、CP 类型、每子帧时隙数、每帧时隙数的对应关系
4. 区分"计时单位"（子帧 = 1 ms 恒定，与 μ 无关）和"调度单位"（时隙 = 14 OFDM 符号，实际时长随 μ 变化）
5. 微时隙（mini-slot）的工程用途——uRLLC 抢占调度、高频段模拟波束 TDM 复用、非授权频谱信道抢占

### 协议入口

- TS 38.211 §4.3.2 — Numerology，Table 4.3.2-1: Supported transmission numerologies
- TS 38.211 §4.3.1 — 帧结构定义，$N_{slot}^{frame,\mu}$、$N_{slot}^{subframe,\mu}$
- 参考书 §4.2（P77-78）+ §4.3.1（P79-82）

### 核心公式

| 参数 | 表达式 | 备注 |
|:---|:---|:---|
| 子载波间隔 | $\Delta f = 15 \cdot 2^\mu$ [kHz]，$\mu \in \{0,1,2,3,4\}$ | NR Rel-15 定义；μ=2 还可选扩展 CP |
| 基本时间单位 | $T_c = 1/(\Delta f_{max} \cdot N_f)$，$\Delta f_{max}=480$ kHz，$N_f=4096$ | TS 38.211 §4.1；$T_c \approx 0.509$ ns |
| 有用符号时长 | $T_u = 1/\Delta f$ | 不含 CP 的 IFFT/FFT 窗口 |
| 每子帧时隙数 | $N_{slot}^{subframe,\mu} = 2^\mu$ | 1 ms 子帧为固定计时锚点 |
| 每帧时隙数 | $N_{slot}^{frame,\mu} = 10 \cdot 2^\mu$ | 无线帧 = 10 ms |
| 每时隙 OFDM 符号数 | $N_{symb}^{slot} = 14$（普通 CP）或 12（扩展 CP, 仅 μ=2） | TS 38.211 Table 4.3.2-1 |
| 时隙时长 | $T_{slot} = N_{symb}^{slot} \cdot (1/\Delta f + T_{CP})$ | μ=0 → 1 ms, μ=3 → 0.125 ms |

**完整层级链**：

$$T_{frame} = 10\text{ ms} = 10 \cdot T_{subframe} = 10 \cdot 2^\mu \cdot N_{symb}^{slot} \cdot (1/\Delta f + T_{CP})$$

### 关键参数速查表

| μ | Δf (kHz) | $T_u$ (μs) | 每子帧时隙数 | 每帧时隙数 | $T_{slot}$ (ms) | CP 类型 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 15 | 66.67 | 1 | 10 | 1.000 | Normal |
| 1 | 30 | 33.33 | 2 | 20 | 0.500 | Normal |
| 2 | 60 | 16.67 | 4 | 40 | 0.250 | Normal / Extended |
| 3 | 120 | 8.33 | 8 | 80 | 0.125 | Normal |
| 4 | 240 | 4.17 | 16 | 160 | 0.0625 | Normal |

### 前置知识

- Δf 与 $T_u$ 的基本关系（T2.1 — 子载波正交条件）
- $T_{CP}$ 的作用（T2.1 — 消除 ISI/ICI）
- 毫秒与微秒的时间单位换算

### 与后续衔接

- T2.3 展开频域维度——同一 μ 下的 PRB、CRB、Point A 频域网格
- T2.5 对比 LTE 固定 μ=0 的帧结构（FDD Type 1、TDD Type 2）

### 图示

1. NR 帧结构层级分解图（frame → subframe → slot → symbol 递归分解，μ=0,1,2 三列对比）
2. 不同 SCS 符号边界对齐示意图（15 kHz 的 1 个 symbol = 30 kHz 的 2 个 symbol）
3. 微时隙与普通时隙调度对比图（微时隙起始于时隙内任意符号位置）

---

## T2.3 — NR 频域资源网格：RE、PRB、CRB、Point A、BWP

### 定位

T2.2 建立了 NR 时域层级。本节补上频域维度，构成完整的二维资源网格，覆盖 NR 频域资源分配的五级概念链：Point A → CRB → BWP → PRB → RE。

### 知识要点

1. 资源粒子（RE）的二维定义——1 OFDM 符号 × 1 子载波，是物理层最小的资源粒度，地址表示为 $(k, l)$
2. 物理资源块（PRB）的频域定义——连续 $N_{sc}^{RB} = 12$ 子载波，与子载波间隔无关，此设计简化了不同 Numerology 间的参考信号图样共享和资源分配
3. Point A 的角色——整个载波的频域公共参考原点，位于系统带宽的最低可用频率处，CRB 0 的子载波 0 与之对齐，由 RRC 高层信令配置
4. 公共资源块（CRB）的编号规则——以 Point A 为原点，在系统带宽内对所有 PRB 进行统一绝对编号（$n_{CRB}^\mu$），不同 Numerology 的 CRB 网格各自独立
5. 带宽部分（BWP）的定义——一个载波内连续 CRB 的子集，UE 可在激活 BWP 上工作而无需感知整个系统带宽；每 UE 最多 4 个 BWP，任意时刻仅 1 个激活
6. CRB 到 PRB 的偏移关系与参考信号生成——以 CRB 为绝对参考生成 DM-RS 序列，保证不同 BWP 的 UE 在相同物理位置时生成相同的参考序列，维持 DM-RS 端口正交性

### 协议入口

- TS 38.211 §4.4.1 — 资源粒子（Resource element）
- TS 38.211 §4.4.2 — 资源块（Resource block, PRB）
- TS 38.211 §4.4.4 — 公共资源块（CRB），Point A
- TS 38.211 §4.4.5 — 带宽部分（BWP），PRB 与 CRB 的映射关系
- 参考书 §4.3.2（P82-86）

### 核心概念层级

```
Point A（频域公共参考原点，RRC 信令配置）
  └── CRB（Common Resource Block，以 Point A 为起点对全系统带宽绝对编号）
        └── BWP（Bandwidth Part，CRB 范围内的连续子集，每 UE 最多 4 个，1 个激活）
              └── PRB（Physical Resource Block，BWP 内的局部编号，12 子载波）
                    └── RE（Resource Element，1 符号 × 1 子载波）
```

### 核心公式

| 概念 | 定义 | 备注 |
|:---|:---|:---|
| RE | $(k, l)$，$k$ 为频域子载波索引，$l$ 为时域 OFDM 符号索引 | TS 38.211 §4.4.1 |
| PRB | 频域上连续 $N_{sc}^{RB} = 12$ 子载波 | 与 SCS 无关 |
| CRB | $n_{CRB}^\mu = \lfloor k / N_{sc}^{RB} \rfloor$，从 Point A 开始编号 | 上标 μ 表示各 Numerology 独立编号 |
| PRB（BWP 内） | $n_{PRB}^\mu = n_{CRB}^\mu - N_{BWP,i}^{start,\mu}$ | $N_{BWP,i}^{start,\mu}$ 为 BWP $i$ 的起始 CRB 偏移 |
| BWP 带宽 | $N_{BWP,i}^{size,\mu}$ PRB | 取值范围依赖信道带宽和 SCS（TS 38.101） |

### 前置知识

- 子载波间隔 Δf 的取值（T2.2）
- OFDM 符号的结构（T2.1）
- 帧与时隙的时域层级（T2.2）

### 与后续衔接

- T2.5 对比 LTE 的频域资源格（36.211 PRB 定义、LTE 无 Point A/BWP 概念）
- T2.6 将 RE 网格与译码器输入建立联系——每个 RE 承载一个复数调制符号，解调后输出 $Q_m$ 个 LLR

### 图示

1. 时频二维资源网格示意图（横轴 OFDM 符号 $l$、纵轴子载波 $k$，标注 RE 最小格、PRB = 12×14 色块）
2. Point A → CRB → BWP → PRB 的频域偏移关系图
3. 不同 SCS 的 PRB 网格嵌套关系（15 kHz PRB 频域跨度 180 kHz = 2 × 30 kHz PRB 频域跨度）

---

## T2.4 — MCS、调制阶数与目标码率

### 定位

T2.1–T2.3 构建了完整的时频资源网格。网格建好之后，调度层需要回答一个问题：每个 RE 里装多少比特？MCS（调制与编码策略，Modulation and Coding Scheme）就是回答这个问题的调度参数——它决定调制阶数 $Q_m$、目标码率 $R$ 和频谱效率 $Q_m \cdot R$，进而通过资源分配推导出 TBS。

本讲是 T9.0（TS 38.214 MCS/TBS decoder descriptor）的前置概念基础。T9.0 从调度工程和 descriptor 视角展开 MCS/TBS 的细节；此处建立概念定义、查表流程和参数间的公式关系。

### 知识要点

1. MCS 在协议栈中的调度位置——MAC 调度器根据 UE 上报的 CQI（信道质量指示）和可用资源选择 MCS 索引；PHY 层根据 MCS 索引查 TS 38.214 表格确定 $Q_m$ 和 $R$
2. MCS 索引到调制参数的一对一映射——TS 38.214 Table 5.1.3.1-1（64QAM 表）、Table 5.1.3.1-2（256QAM 表）、Table 5.1.3.1-3（1024QAM 低频谱效率表）分别定义不同范围的 MCS 索引与 $Q_m$、$R$ 的对应关系
3. 调制阶数 $Q_m$ 定义每个调制符号承载的比特数（BPSK=1, QPSK=2, 16QAM=4, 64QAM=6, 256QAM=8, 1024QAM=10），是物理层最直接的吞吐量杠杆
4. 目标码率 $R$ = 信息比特数 / 编码后比特数（速率匹配后），决定编码冗余度——$R$ 越低冗余越高，抗噪声能力越强
5. 频谱效率 $SE = Q_m \cdot R$ [bit/s/Hz]，物理直觉：每子载波（Hz）每 OFDM 符号（s）传输的信息比特数
6. MCS 表格的设计逻辑——低 MCS（0–4）对应 QPSK + 低码率，适合小区边缘或低 SINR；中 MCS（5–16）逐步提升码率和调制阶数，覆盖各种信道条件；高 MCS（17–28）对应 64QAM + 高码率，适合小区中心高 SINR；索引 29/30/31 保留用于重传（QPSK/16QAM/64QAM，$R$ 由 DCI 隐式指示）
7. 256QAM 和 1024QAM 扩展表的使用前提——UE 能力上报支持后，gNB 可通过 RRC 配置启用对应的 MCS 表（$MCS\_Table$），但 MCS 索引空间仍为 0–31
8. MCS 与 CQI 的关系——UE 测量 SINR 后根据"BLER ≤ 0.1"目标查 CQI 表（TS 38.214 Table 5.2.2.1-1），上报 4-bit CQI 索引；gNB 据此选择 MCS（NR 不强制 CQI→MCS 的绑定关系，调度器有实现自由度）
9. 从 MCS 到 TBS 的两步流程——先查 MCS 表得到 $Q_m$ 和 $R$，再结合资源分配（$N_{RE}$、层数 $v$）按 TS 38.214 §5.1.3.2 的公式计算 TBS
10. LTE MCS 的关键差异——LTE MCS 表（TS 36.213 Table 7.1.7.1-1）仅 32 行，最高支持 64QAM（256QAM 为 Rel-12 新增）；TBS 通过 $I_{TBS}$ 间接查表（Table 7.1.7.2.1-1）而非 NR 的公式计算；LTE 无 BWP/Numerology → 同一 MCS 在不同带宽下的 TBS 表差异巨大

### 协议入口

- TS 38.214 §5.1.3 — MCS 索引与调制阶数、目标码率的映射（下行）
- TS 38.214 §5.1.3.1 — MCS Table 5.1.3.1-1/2/3
- TS 38.214 §5.1.3.2 — TBS 计算
- TS 38.214 §5.2.2 — CQI 定义与 CQI 表
- TS 38.214 §6.1.4 — 上行 MCS 表
- TS 36.213 §7.1.7 — LTE MCS 与 TBS（下行）
- 参考书 §6.4.5（CQI 和 MCS）+ §6.4.1（TBS 设计）

### NR MCS 表核心片段

| MCS Index $I_{MCS}$ | $Q_m$ | $R \times 1024$ | 频谱效率 [bit/s/Hz] |
|:---:|:---:|:---:|:---:|
| 0 | 2 | 120 | 0.2344 |
| 1 | 2 | 157 | 0.3066 |
| 2 | 2 | 193 | 0.3770 |
| 3 | 2 | 251 | 0.4902 |
| 4 | 2 | 308 | 0.6016 |
| 5 | 2 | 379 | 0.7402 |
| 6 | 2 | 449 | 0.8770 |
| 7 | 2 | 526 | 1.0273 |
| 8 | 2 | 602 | 1.1758 |
| 9 | 2 | 679 | 1.3262 |
| 10 | 4 | 340 | 1.3281 |
| 11 | 4 | 378 | 1.4766 |
| 12 | 4 | 434 | 1.6953 |
| 13 | 4 | 490 | 1.9141 |
| 14 | 4 | 553 | 2.1602 |
| 15 | 4 | 616 | 2.4063 |
| 16 | 4 | 658 | 2.5703 |
| 17 | 6 | 466 | 2.7305 |
| 18 | 6 | 517 | 3.0293 |
| 19 | 6 | 567 | 3.3223 |
| 20 | 6 | 616 | 3.6094 |
| 21 | 6 | 666 | 3.9023 |
| 22 | 6 | 719 | 4.2129 |
| 23 | 6 | 772 | 4.5234 |
| 24 | 6 | 822 | 4.8164 |
| 25 | 6 | 873 | 5.1152 |
| 26 | 6 | 910 | 5.3320 |
| 27 | 6 | 948 | 5.5547 |
| 28 | 6 | — | 保留（$R$ 由 DCI RV 隐式指示） |
| 29 | 2 | — | 保留（重传，$R$ 由 DCI 隐式指示） |
| 30 | 4 | — | 保留（重传，$R$ 由 DCI 隐式指示） |
| 31 | 6 | — | 保留（重传，$R$ 由 DCI 隐式指示） |

（256QAM/1024QAM 扩展表见 TS 38.214 Table 5.1.3.1-2/3；讲义标注协议出处，仅复现关键行说明设计逻辑）

### 核心公式

| 参数 | 表达式 | 说明 |
|:---|:---|:---|
| 调制阶数与目标码率 | $Q_m, R = MCS\_Table(I_{MCS})$ | TS 38.214 Table 5.1.3.1-1 查表 |
| 频谱效率 | $SE = Q_m \cdot R$ | 单位 bit/s/Hz，衡量每子载波-符号的信息比特数 |
| 信息比特中间量 | $N_{info} = N_{RE} \cdot R \cdot Q_m \cdot v$ | $v$ 为 MIMO 层数，$N_{RE}$ 来自资源分配与参考信号扣除 |
| TBS 量化 | 若 $N_{info} \leq 3824$：分步查表量化；否则分段公式量化 | TS 38.214 §5.1.3.2，两级量化规则 |
| 有效码率 | $R_{eff} = (TBS + TB\_CRC) / (N_{RE} \cdot Q_m)$ | 实际有效码率，略高于目标码率 $R$（含 TB CRC 开销） |

### 前置知识

- 调制阶数 $Q_m$ 的含义（相关概念在 T2.1 中已引入 16QAM/64QAM/256QAM 的 $Q_m$ 值）
- 码率 $R$ 的基本概念（信息比特占编码后比特的比例，T1.6 信息论中已出现）
- PRB 和 RE 的资源分配（T2.3）
- 信道质量（CQI/SINR）的直觉（LTE 链路预算中已出现，不做展开）

### 与后续衔接

- T2.6（资源网格到译码器输入）使用此处的 $Q_m$ 和 $N_{RE}$ 计算 LLR 序列长度 $L = N_{RE} \cdot Q_m$
- T3.2–T3.5（码块分段）使用此处的 TBS 决定码块数 $C$ 和各码块长度 $K_r$
- T9.0（TS 38.214 MCS/TBS decoder descriptor）从调度工程视角展开 MCS/TBS 在 descriptor 中的字段和工程细节——本讲是其概念前置

### 图示

1. MCS 索引 → 查表 → $Q_m$ → $R$ → 频谱效率的查表流程图（Mermaid）
2. TS 38.214 Table 5.1.3.1-1 的 $Q_m$ 阶梯 vs 频谱效率 $SE$ 散点图（标注 QPSK/16QAM/64QAM 三个平台的 SE 覆盖范围）
3. LTE vs NR MCS 表格逻辑对比（LTE 间接 $I_{TBS}$ 查 TBS vs NR 公式计算，LTE 无 256QAM/1024QAM）

---

## T2.5 — LTE 帧结构与时频资源

### 定位

在 NR 时频结构（T2.2–T2.3）之后回退到 LTE 的固定参数框架。LTE 仅支持 μ=0（15 kHz SCS），帧结构基于 FDD Type 1 / TDD Type 2 两类固定配置。本节建立 LTE 与 NR 时频资源概念的关键对照，避免在阅读 36.212 译码链路时误用 NR 术语。

### 知识要点

1. LTE 无线帧的两类双工结构——Type 1（FDD，上下行各 10 子帧频率分离）和 Type 2（TDD，5 ms / 10 ms 切换周期，7 种标准上下行配置）
2. LTE 的时域层级与 NR 的关键差异——子帧在 LTE 中既是计时单位也是调度单位，不存在 NR 的"时隙"独立调度概念；LTE 一个子帧（1 ms）= 2 个时隙（0.5 ms 各含 7 个普通 CP OFDM 符号）
3. LTE 资源块的频域定义——$N_{sc}^{RB} = 12$ 子载波，与时隙绑定构成物理资源块对（PRB pair, 12 SC × 1 ms），此频域-时域绑定在 NR 中已解除
4. LTE 资源网格的统一性——单一 SCS 决定单一 PRB 频域带宽（180 kHz），无 BWP / Point A / CRB 概念；资源映射的绝对参考点为 $k=0$（DC 子载波，载波中心频率）
5. RE 映射中下行控制区域（PDCCH，占子帧前 1–3 OFDM 符号）与数据区域（PDSCH）的时分分离——此设计在 NR 中已被更灵活的 CORESET + 符号级调度替代

### 协议入口

- TS 36.211 §4 — 帧结构，Type 1 / Type 2 定义
- TS 36.211 §6.2 — 下行资源网格
- TS 36.211 §6.2.3 — 资源块
- TS 36.211 §6.2.2 — 资源粒子
- 参考书 §4.2（LTE 固定 SCS 背景）+ §4.3（时频资源 NR/LTE 对比段落）

### LTE vs NR 时频参数完整对比

| 概念 | LTE | NR |
|:---|:---|:---|
| SCS | 固定 15 kHz | $\Delta f = 15 \cdot 2^\mu$ kHz, μ=0–4 |
| 无线帧 | 10 ms, $T_f = 307200 \times T_s$ | 10 ms, $T_f = 10 \cdot T_{subframe}$ |
| 子帧 | 1 ms = 2 slots, 基本调度单位 | 1 ms, 仅计时单位 |
| 时隙（slot） | 0.5 ms, 7 OFDM 符号（普通 CP） | 14 OFDM 符号, 实际时长随 μ 变 |
| 基本时间单位 | $T_s = 1/(15000 \times 2048) = 32.552$ ns | $T_c = 1/(480000 \times 4096) \approx 0.509$ ns |
| PRB | 12 SC × 1 slot（时频二维绑定） | 12 SC（纯频域定义，与 slot 解耦） |
| PRB pair | 12 SC × 1 子帧（2 slots），调度最小粒度 | 无对应概念 |
| 频域参考点 | DC 子载波（$k=0$），载波中心频率 | Point A，载波可用频率下边界 |
| 频域资源编排 | 无 BWP/CRB，直接以 PRB 分配 | CRB → BWP → PRB 三级映射 |
| 控制区域 | PDCCH 固定占子帧前 1–3 OFDM 符号 | CORESET，频域任意位置，符号级灵活配置 |
| $Q_m$ 最大值 | 8（256QAM） | 10（1024QAM, NR Rel-15 晚期引入） |

### LTE TDD 上下行配置速查

| 配置 | 切换周期 | 子帧号 → 方向（D=下行, U=上行, S=特殊子帧） |
|:---:|:---:|:---|
| 0 | 5 ms | D S U U U D S U U U |
| 1 | 5 ms | D S U U D D S U U D |
| 2 | 5 ms | D S U D D D S U D D |
| 3 | 10 ms | D S U U U D D D D D |
| 4 | 10 ms | D S U U D D D D D D |
| 5 | 10 ms | D S U D D D D D D D |
| 6 | 5 ms | D S U U U D S U U D |

（特殊子帧 S 含 DwPTS / GP / UpPTS 三区域，具体 OFDM 符号数由高层配置的 special subframe configuration 决定）

### 前置知识

- FDD 与 TDD 的基本区分（双工方式）
- OFDM 符号与子载波的关系（T2.1）
- NR 的时域（T2.2）和频域（T2.3）框架

### 与后续衔接

- T2.6 汇总两套框架并提供从 RE 网格到解调输入的跨制式统一视角
- LTE 译码链路（T6-T7）的所有参数（TBS、PRB 数、Qm、速率匹配参数）均以此处定义的资源网格为起点

### 图示

1. LTE Type 1（FDD）帧结构：上下行各 1 个载波，子帧按频率分离
2. LTE Type 2（TDD）帧结构：单载波，子帧按时间分离，标注 D/S/U 和切换周期
3. LTE vs NR 时域层级并排对比图（帧→子帧→时隙→符号，标注关键差异）

---

## T2.6 — 从资源网格到译码器输入

### 定位

T2 系列的收尾章节。T2.1–T2.4 构建了 LTE 和 NR 的完整时频资源框架，本节将所有框架汇入一条端到端数据流：RE 网格上的复数调制符号 → 译码器输入端的 LLR 序列。定义解调与译码之间的接口边界。

### 知识要点

1. RE 网格到 LLR 序列的完整数据流——RE → 信道估计与均衡 → 复数调制符号 → 软解调器 → 逐比特 LLR → 码字（codeword）级 LLR 序列 → 码块切分 → 译码器
2. 调制阶数 $Q_m$ 对 RE-to-LLR 转换的量化影响——每 RE 承载比特数 = $Q_m$（BPSK=1, QPSK=2, 16QAM=4, 64QAM=6, 256QAM=8, 1024QAM=10），解调后每 RE 输出 $Q_m$ 个 LLR
3. 有效数据 RE 的计算——$N_{RE}^{data} = N_{PRB} \cdot N_{symb}^{data} \cdot 12 - N_{RE}^{RS}$，需扣除控制区域、DM-RS、CSI-RS、SSB 等占用的 RE
4. LLR 序列在下游的切分——码字级 LLR 流按 TBS/CB 边界切割为 $C$ 个码块，每个码块的 LLR 向量长度为 $E_r$（经速率恢复后）
5. 译码器对 RE 网格的不可见性——译码器看到的是按码块组织的一维 LLR 向量，不感知 BWP、PRB、DM-RS 位置、symbol 编号等物理映射细节；这些信息已在解调前被处理和剥离
6. puncturing 和未观测 RE 的处理——发送端打孔或接收端未观测的 RE 位置在 LLR 序列中填充中性值（$LLR = 0$，表示不偏向比特 0 也不偏向比特 1）
7. LTE 与 NR 在此环节的差异范围——差异仅存在于 RE 网格层和速率匹配层；到译码器输入接口（一维 LLR 向量）时，两制式已收敛为统一抽象

### 协议入口

- TS 38.211 §5 — 调制映射（Modulation mapper），调制阶数 $Q_m$
- TS 36.211 §7 — 调制映射（LTE 侧）
- TS 38.212 §5 / TS 36.212 §5 — 码块分段，决定 LLR 流到 CB 的切分边界
- T2.8（BPSK/QPSK 软解调）、T2.9（QAM 软解调 / Max-Log-MAP）——软解调详细公式在此展开

### 完整数据流

```
RE 网格（LTE 或 NR，时频二维）
  │
  ├─ 信道估计（DM-RS / CSI-RS 辅助，均衡前）
  ├─ 均衡（ZF / MMSE / ML）
  │
  ▼
每个数据 RE 的接收调制符号（modulation symbol）y = h · x + n
  │  注：这里的"符号"是星座图上的复数调制符号，承载 Q_m 个比特，
  │  不是时域的 OFDM 符号（OFDM symbol）。区分定义见 T2.1 要点 6。
  ├─ 软解调器（T2.8 / T2.9 详述）
  │
  ▼
每个数据 RE → Q_m 个逐比特 LLR
  │
  ├─ PDSCH/PUSCH 码字级映射与速率恢复
  │
  ▼
一维 LLR 序列（总长度 = N_RE^data · Q_m）
  │
  ├─ TB/CB 边界切分（T3.2–T3.5）
  │
  ▼
每个 CB 的 LLR 向量（长度 E_r，进入译码器核心）
  │
  ▼
译码器 core（Turbo / LDPC / Polar）
```

### 核心公式

| 步骤 | 表达式 | 说明 |
|:---|:---|:---|
| 有效数据 RE 数 | $N_{RE}^{data} = N_{PRB} \cdot N_{symb}^{data} \cdot 12 - N_{RE}^{RS}$ | 扣除控制区域和参考信号占用的 RE |
| 码字级 LLR 总长度 | $L = N_{RE}^{data} \cdot Q_m$ | 解调后的一维 LLR 序列总长度 |
| 每 CB 的 LLR 长度 | $E_r = f_{rate\_recovery}(L, r, C)$ | 第 $r$ 个码块经速率恢复后的 LLR 向量长度 |
| 未观测 RE 填充 | $LLR_{unobserved} = 0$ | puncturing 位置和速率匹配未发送位置的中性 LLR |

### 前置知识

- RE、PRB 的定义（T2.3）
- 调制阶数 $Q_m$ 的含义（T2.8 BPSK/QPSK, T2.9 QAM）
- 码块分段的基本概念（T3.2–T3.5）
- AWGN 下软解调的基本思路（T2.7 AWGN 模型）

### 与后续衔接

- T2.7（AWGN 噪声缩放）紧接此处的 LLR 输出，量化噪声对译码器输入可靠性的影响
- T3 系列（CRC/分段）展开 TBS→CB 的具体拆分规则
- T7/T9（速率恢复）展开 $E_r$ 和 circular buffer 的具体分配算法
- T4.6（decoder interface contracts）中 descriptor 的 RE/BWP/RB 字段直接来自此处的资源网格定义

### 图示

1. RE 网格到译码器输入的端到端数据流图（标注每步操作和对应本文章节引用）
2. LTE vs NR 数据流差异范围对比表（差异仅存在于 RE 网格层和速率匹配层，译码器输入接口相同）

---

## 参考文献

- 3GPP TS 38.211 Rel-19: NR; Physical channels and modulation, §4
- 3GPP TS 36.211 Rel-19: LTE; Physical channels and modulation, §4, §6
- 3GPP TS 38.212 Rel-19: NR; Multiplexing and channel coding, §5
- 3GPP TS 36.212 Rel-19: LTE; Multiplexing and channel coding, §5
- 王映民, 孙韶辉 等. 5G移动通信系统设计与标准详解. 人民邮电出版社, 2020. 第4章. （本地路径: `references/5G移动通信系统设计与标准详解.pdf`）
