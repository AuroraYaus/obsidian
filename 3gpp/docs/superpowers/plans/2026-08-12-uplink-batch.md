# 上行链路概念笔记批次 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 1 剩余批次（G4 上行链路）：5 篇概念笔记（DFT-s-OFDM / Power_Control / PRACH / SRS / UL_DL_Differences）+ 同步清单 + 全量验证 + 双推。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-uplink-batch.md` 执行。变更文件：新建概念笔记 5 个、修改图谱入口/术语表 2 个。每个任务「内容 → 验证 → 提交」闭环。

**Tech Stack:** Markdown + LaTeX（--syntax-only）+ 项目 audit 工具链。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- 标题正式化（Rule 16）；带圈数字禁令（第 10 条）；英文术语首现**完整三件套**「中文（English Full Name, ABBR）」（Rule 10——连续两批次 30+ 处返工教训，本计划内容已按此写定，逐字转写即可；**发现裸用不要擅改，在 concerns 报告**）。
- 概念笔记六段式模板（独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联，末行「关系语义：…」）。
- wikilink 只指向已存在或本计划内将创建的目标；创建顺序：E1-E4（独立）→ E5（引用全部四篇，最后建）；E1-E4 内引用批内其他篇属前瞻（E5 后闭合）。
- 协议溯源精确到 TS 编号 + 章节号 + 本地 processed 路径；数值事实以本地 spec 为准（PRACH 前导长度/功控公式实施时核验）。
- 工具缺失（KaTeX/mmdc）显式声明验证缺口。
- 提交后 `git push origin master`（双推，收尾任务统一执行）。

---

### Task E1: 新建概念笔记 `docs/concepts/DFT_sOFDM_上行波形.md`

**Files:**
- Create: `3gpp/docs/concepts/DFT_sOFDM_上行波形.md`

**Interfaces:**
- Produces: 该文件，Task E5（UL_DL_Differences）引用；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 上行波形
  - DFT-s-OFDM
  - SC-FDMA
  - 离散傅里叶变换扩展正交频分复用
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §5.4/§6.3.3; TS 36.211 Rel-19 §5.6"
---

# DFT-s-OFDM 上行波形

DFT-s-OFDM（离散傅里叶变换扩展正交频分复用，Discrete Fourier Transform Spread OFDM）是 NR 上行 PUSCH（物理上行共享信道，Physical Uplink Shared Channel）的一种波形选择——先在频域做 DFT 预编码再走 OFDM 调制，本质是「单载波」传输：峰均比 PAPR（峰均功率比，Peak-to-Average Power Ratio）低，功放效率高。LTE 的 SC-FDMA（单载波频分多址，Single Carrier Frequency Division Multiple Access）是它的前身；NR 同时支持 DFT-s-OFDM 与纯 OFDM（CP-OFDM，循环前缀正交频分复用，Cyclic Prefix OFDM）两种上行波形，按场景切换。

## 独立解释任务

任务目标：讲清 DFT-s-OFDM 的原理（DFT 预编码如何把多子载波变成"等效单载波"）、低 PAPR 优势的根源、与 OFDMA（正交频分多址，Orthogonal Frequency Division Multiple Access）的对比，以及 NR 上行波形选择的配置逻辑。

## 科学定义

### 从 OFDM 到 DFT-s-OFDM

OFDM 多子载波独立调制，时域信号是多路正弦叠加——幅度起伏大（高 PAPR），功放需大回退（back-off）才能线性放大，效率低。DFT-s-OFDM 的改造：在子载波映射之前加一个 DFT（离散傅里叶变换，Discrete Fourier Transform）预编码——把时域符号块整体变换后铺到子载波上，时域波形退化为单载波样式（恒包络近似），PAPR 显著下降。

处理链：数据比特 → 调制符号 → **DFT 预编码（M 点）** → 子载波映射 → IFFT → CP（循环前缀，Cyclic Prefix）插入 → 发射。

### 低 PAPR 的根源与代价

- 根源：单载波信号时域包络近似恒定，PAPR 低（比 OFDM 低 3-6 dB 量级）——功放回退小、效率高，对 UE 电池与功放成本友好。
- 代价：频域分集下降——OFDM 一个符号的错误可以靠纠错跨子载波恢复，DFT-s-OFDM 的符号映射在频域是「展平」的，需要额外考虑（一般靠编码交织补偿）。

### 与 OFDMA 的对比（[[Multiple_Access_多址接入]] 视角）

| 维度 | OFDMA（下行为主） | DFT-s-OFDM（上行可选） |
|:---|:---|:---|
| 波形 | 多载波 | 等效单载波 |
| PAPR | 高（功放回退大） | 低（功放效率高） |
| 频域分集 | 好 | 较弱（编码补偿） |
| 接收机 | 每子载波均衡 | 需 IDFT 解预编码 |
| 使用 | NR 下行 / 上行可选 | LTE 上行 / NR 上行可选 |

### NR 上行波形配置

- NR 上行 PUSCH 由高层配置 transformPrecoding（变换预编码开关）：开 → DFT-s-OFDM，关 → CP-OFDM；PUCCH（物理上行控制信道，Physical Uplink Control Channel）format 4 也用 DFT-s-OFDM（见 [[PUCCH_上行控制信道与UCI]]）。
- LTE 上行全用 SC-FDMA（TS 36.211 §5.6），无选择。

## 直观模型

OFDM 像「多车道并排运输」：每车道（子载波）一辆车（符号），车流起伏大（高 PAPR）；DFT-s-OFDM 像「单车道列车」：货物（符号）排成一列整体出发（DFT 预编码），速度均匀、油耗低（低 PAPR、功放省电）——代价是灵活度不如多车道。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| DFT-s-OFDM 就是 OFDM 加个变换 | 变换改变了波形本质——从多载波变等效单载波，PAPR 特性完全不同 |
| SC-FDMA 与 DFT-s-OFDM 是两种技术 | 同一技术家族：LTE 称 SC-FDMA，NR 称 DFT-s-OFDM（DFT 预编码 OFDM） |
| 低 PAPR 没有代价 | 频域分集下降，靠编码/交织补偿 |
| NR 上行只用 DFT-s-OFDM | NR 上行可配 CP-OFDM（transformPrecoding 关），DFT-s-OFDM 是选项之一 |

## 协议锚点

- DFT-s-OFDM 信号生成：TS 38.211（Rel-19 j30）§5.4，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- PUSCH 物理结构：TS 38.211 §6.3.3，本地同卷。
- transformPrecoding 配置：TS 38.331（Rel-19 j20）§6.3.2（PUSCH-Config），本地 `TS_38.331_38331-j20`。
- LTE SC-FDMA：TS 36.211（Rel-19 j30）§5.6，本地 `TS_36.211_*`。
- PAPR 背景：T2.18（`docs/L1_基础/T2.18_OFDM_PAPR_power_amplifier.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[Multiple_Access_多址接入]]
- [[PUCCH_上行控制信道与UCI]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[T2.18_OFDM_PAPR_power_amplifier]]
- 关系语义：DFT-s-OFDM 是上行链路的数据波形（PUSCH 选项）——与 OFDMA（下行/多址）构成波形对照，低 PAPR 特性衔接 T2.18 功放问题，PUCCH format 4 复用同一波形，是全链路「上行半边」的物理层入口。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/DFT_sOFDM_上行波形.md" && grep -c "^## " "docs/concepts/DFT_sOFDM_上行波形.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/DFT_sOFDM_上行波形.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[PUCCH_上行控制信道与UCI]]`（控制面批次已创建，存在）；`[[T2.18_OFDM_PAPR_power_amplifier]]`（L1 讲义存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/DFT_sOFDM_上行波形.md" && git commit -m "docs(concepts): 新增 DFT-s-OFDM 上行波形概念笔记（SC-FDMA 原理与 PAPR 优势）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E2: 新建概念笔记 `docs/concepts/Power_Control_上行功率控制.md`

**Files:**
- Create: `3gpp/docs/concepts/Power_Control_上行功率控制.md`

**Interfaces:**
- Produces: 该文件，Task E5 引用；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 功率控制
  - 上行功率控制
  - Power Control
  - TPC PHR
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.213 Rel-19 §7; TS 38.321 Rel-19 §5.4.6"
---

# Power Control 上行功率控制

上行功率控制（Power Control）决定 UE 用多大功率发射：既不能太小（基站收不到），也不能太大（干扰邻区、浪费电池）。它分两层——开环（open-loop）按路损补偿粗略定功率，闭环（closed-loop）用 TPC（发射功率控制命令，Transmit Power Control Command）逐次微调；PHR（功率余量报告，Power Headroom Report）把 UE 的功率余量反馈给调度器。功控是上行链路与下行最大的机制差异之一（下行固定功率、上行闭环调节）。

## 独立解释任务

任务目标：讲清开环/闭环两层功控机制、功控公式的组成项（P0/α/PL/ΔTF/f）、TPC 命令的累计与 DCI 携带方式、PHR 的作用，以及功控与调度（Scheduler）的联动。

## 科学定义

### 为什么需要上行功控

下行功率由基站统一管理（多用户共享、干扰可控）；上行每个 UE 独立发射——近处 UE 功率过大淹没远处 UE（远近效应，见 [[Multiple_Access_多址接入]]），功率过小基站收不到。功控让每个 UE 的到达功率恰到好处。

### 开环与闭环

- 开环（open-loop）：UE 测量下行路损（PL，路径损耗，Path Loss，从 RS 功率与实测接收功率推算），按 `P0 + α·PL` 补偿——粗略对齐，无反馈。
- 闭环（closed-loop）：基站根据实际接收 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio）发 TPC 命令（+1/-1 dB 等），UE 累计调整（f 累计项）——精细校正。

### 功控公式（PUSCH 为例，TS 38.213 §7.1）

$$
P_{\mathrm{PUSCH}} = P_0 + \alpha \cdot PL + \Delta_{\mathrm{TF}} + f(\mathrm{TPC})
$$

| 项 | 含义 | 来源 |
|:---|:---|:---|
| P0 | 目标接收功率基准 | RRC 配置（开环偏置） |
| α | 路损补偿系数（0-1，部分补偿省干扰） | RRC 配置 |
| PL | 下行路径损耗估计 | UE 测量 |
| ΔTF | 传输格式补偿（MCS（调制与编码方案，Modulation and Coding Scheme）相关） | 按 MCS 查表 |
| f(TPC) | 闭环累计项（TPC 命令累加，含饱和） | DCI 的 TPC 字段（见 [[DCI_下行控制信息]]） |

PUCCH（物理上行控制信道，Physical Uplink Control Channel）/SRS（探测参考信号，Sounding Reference Signal）/PRACH（物理随机接入信道，Physical Random Access Channel）各有独立功控参数集（TS 38.213 §7.2/§7.3/§7.4）。

### TPC 与 PHR

- TPC：DCI 里的 2-bit 字段（见 [[DCI_下行控制信息]] 字段表），发 TPC 命令（-1/0/+1/+3 dB 等），UE 按累积项 f 调整——这就是「闭环」的执行通道。
- PHR（功率余量报告，Power Headroom Report）：UE 周期性/触发式上报「最大功率 - 当前发射功率」的余量（MAC 层，TS 38.321 §5.4.6）——调度器据此决定是否给 UE 分配更多资源（余量足=可加大 MCS/带宽）。

## 直观模型

功控像「对讲机音量调节」：开环是「按距离估算音量」（P0+α·PL），闭环是「对方说大点/小点」（TPC 命令），PHR 是「我还能再大声多少」（余量报告）——三者配合让通话质量刚好够用又不吵到邻居。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 上行功控和下行一样 | 下行固定功率+调度控制，上行闭环功控（开环+闭环两层） |
| 功控只在物理层 | TPC 在 DCI（物理层），PHR 在 MAC 层（TS 38.321）——跨层机制 |
| α=1 一定最好 | 部分补偿（α<1）在干扰受限场景反而更优（减少对邻区干扰） |
| PHR 越大越好 | PHR 大说明有功率余量，调度器可加大资源；但长期满功率说明覆盖边缘 |

## 协议锚点

- 功控公式与参数：TS 38.213（Rel-19 j30）§7，本地 `3GPP_Rel19/processed/TS_38.213_38213-j30`。
- PHR：TS 38.321（Rel-19 j20）§5.4.6，本地 `TS_38.321_38321-j20`。
- TPC 字段：[[DCI_下行控制信息]]（`docs/concepts/DCI_下行控制信息.md`）、TS 38.212 §7.3。
- 与调度联动：[[Scheduler_MAC调度器与资源分配]]。

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[Scheduler_MAC调度器与资源分配]]
- [[Multiple_Access_多址接入]]
- [[PUCCH_上行控制信道与UCI]]
- 关系语义：上行功控是链路自适应（[[Link_Adaptation_链路自适应与CQI]]）的上行镜像——TPC 命令经 DCI 闭环微调，PHR 反馈给调度器（[[Scheduler_MAC调度器与资源分配]]）决定资源，PUCCH/SRS/PRACH 各有功控参数集，是上行链路「功率维度」的完整闭环。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Power_Control_上行功率控制.md" && grep -c "^## " "docs/concepts/Power_Control_上行功率控制.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Power_Control_上行功率控制.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过（含功控公式块级）；圈号无新增 FAIL。
注意：wikilink `[[Link_Adaptation_链路自适应与CQI]]`（调度批次已创建，存在）——关系语义行引用；`[[DCI_下行控制信息]]`/`[[PUCCH_上行控制信道与UCI]]` 存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Power_Control_上行功率控制.md" && git commit -m "docs(concepts): 新增 Power Control 上行功率控制概念笔记（开环/闭环/TPC/PHR）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E3: 新建概念笔记 `docs/concepts/PRACH_随机接入.md`

**Files:**
- Create: `3gpp/docs/concepts/PRACH_随机接入.md`

**Interfaces:**
- Produces: 该文件，Task E5 引用；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 随机接入
  - 随机接入信道
  - PRACH
  - RACH
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §6.3.3; TS 38.213 Rel-19 §8; TS 38.321 Rel-19 §5.1"
---

# PRACH 随机接入

随机接入（Random Access）是 UE 与网络建立上行同步与连接的第一步：UE 在 PRACH（物理随机接入信道，Physical Random Access Channel）上发前导（preamble）——一个精心选择的序列，让基站既能检测「有人来了」又能估计「时间提前量 TA（定时提前，Timing Advance）」。完整的随机接入过程（RACH procedure）分四步（Msg1-Msg4）或两步（MsgA），从「发前导」到「竞争解决」，是 UE 从空闲态进入连接态的必经之路，也是小区搜索（[[PSS_SSS_同步信号与小区搜索]]）之后的下一环。

## 独立解释任务

任务目标：讲清 PRACH 前导的结构与作用（检测/TA 估计）、四步随机接入流程（Msg1-Msg4）每步的语义、两步 RACH 的动机，以及 PRACH 时频资源与根序列配置。

## 科学定义

### 前导（preamble）与 PRACH 物理结构

- 前导：基于 ZC（Zadoff-Chu）序列生成——LTE 长前导 839 长、NR 长前导 139 长（TS 38.211 §6.3.3.1）；同一小区用同一根序列的不同循环移位生成多前导（UE 随机选一个，冲突即竞争）。
- PRACH 时频资源：专用时隙/频域位置（由 SIB1 的 prach-ConfigurationIndex 配置，见 [[PBCH_MIB_广播信道]] 的 SIB1 衔接）；频域上 NR 前导（139 子载波）占约 12 个 PRB（物理资源块，Physical Resource Block），LTE 长前导（839 子载波）占 6 个 PRB；频域 occasion 数（msg1-FDM）可配 1/2/4/8。
- 用途：(1) 检测——基站相关检测识别「有 UE 接入」与哪个前导（竞争解决的基础）；(2) TA 估计——前导到达时间相对期望位置的偏移即 TA，基站随后用 RAR（随机接入响应，Random Access Response）告知 UE 调整发射定时（上行同步）。

### 四步随机接入（Contention-based，CBRA）

```
Msg1: UE 发 PRACH 前导（随机选）
Msg2: 基站回 RAR（RA-RNTI 加扰的 PDCCH/PDSCH：定时提前 + 临时 C-RNTI + UL grant）
Msg3: UE 用 UL grant 发 RRC 连接请求（含 UE 标识）
Msg4: 基站回竞争解决消息（冲突的 UE 中胜者收到确认）
```

竞争的本质：多个 UE 可能选同一前导（Msg1 冲突）——Msg3/Msg4 的 UE 标识交换解决竞争（TS 38.321 §5.1）。

### 两步随机接入（2-step RACH）

MsgA = 前导 + PUSCH 载荷一步发出，MsgB 合并 RAR 与竞争解决——减少信令往返（低时延，URLLC 与大规模 IoT 场景）；代价是前导/PUSCH 资源关联配置更复杂（TS 38.213 §8.1A）。

### 触发场景

初始接入、RRC 重建立、切换（handover 目标小区）、RRC 连接恢复（inactive→active）、上行失步后的数据到达、波束失败恢复（BFR，Beam Failure Recovery）。

## 直观模型

随机接入像「新房客入住登记」：先按门铃（Msg1 前导，让人知道有人来了），门卫回话「我在几号窗口等你」（Msg2 RAR），报上姓名（Msg3 连接请求），门卫确认「好，就是你」（Msg4 竞争解决）；要是两个人同时按同一个门铃（前导冲突），就看谁先报上名（竞争解决）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 随机接入只用于初始接入 | 还用于切换/重建/恢复/失步后数据——任何需要上行同步的场景 |
| 前导是随机数 | 前导是 ZC 序列的循环移位，结构确定、随机性在「选哪个」 |
| 竞争总是坏事 | 竞争是免调度接入的固有代价，Msg3/4 机制解决；还有非竞争接入（切换时基站指定前导） |
| RACH 过程在物理层完成 | 跨层：前导在物理层（PRACH），过程控制（RAR/竞争解决）在 MAC 层（TS 38.321 §5.1） |

## 协议锚点

- PRACH 物理结构与前导序列：TS 38.211（Rel-19 j30）§6.3.3，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 随机接入过程：TS 38.213（Rel-19 j30）§8，本地 `TS_38.213_38213-j30`；MAC 层过程 TS 38.321（Rel-19 j20）§5.1，本地 `TS_38.321_38321-j20`。
- 前导配置来源：SIB1（TS 38.331 §6.2.2 RACH-ConfigCommon），本地 `TS_38.331_38331-j20`。
- 与小区搜索衔接：[[PSS_SSS_同步信号与小区搜索]]、[[PBCH_MIB_广播信道]]。

## 图谱关联

- [[概念图谱入口]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[PBCH_MIB_广播信道]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- 关系语义：随机接入是小区搜索的下一环——PSS/SSS/PBCH 让 UE 找到小区并读到 SIB1（含 PRACH 配置），Msg2/Msg4 经 PDCCH（RA-RNTI（随机接入无线网络临时标识，Random Access Radio Network Temporary Identifier））与 PDSCH 下发，TA 与 UL grant 建立上行同步与首个上行传输（Msg3），接入后进入调度（Scheduler）主导的数据传输。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/PRACH_随机接入.md" && grep -c "^## " "docs/concepts/PRACH_随机接入.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/PRACH_随机接入.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[PSS_SSS_同步信号与小区搜索]]`/`[[PBCH_MIB_广播信道]]`（控制面批次已创建，存在）；RACH 过程图用 fenced 代码块（非 Mermaid）——代码块内无 wikilink。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/PRACH_随机接入.md" && git commit -m "docs(concepts): 新增 PRACH 随机接入概念笔记（前导/四步 RACH/两步 RACH）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E4: 新建概念笔记 `docs/concepts/SRS_探测参考信号.md`

**Files:**
- Create: `3gpp/docs/concepts/SRS_探测参考信号.md`

**Interfaces:**
- Produces: 该文件，Task E5 引用；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 探测参考信号
  - SRS
  - Sounding Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §6.4.1; TS 38.214 Rel-19 §6.2"
---

# SRS 探测参考信号

SRS（探测参考信号，Sounding Reference Signal）是 UE 发给基站的「探针」：基站用它测量上行信道质量，获得上行 CSI（信道状态信息，Channel State Information）——用于上行频选调度、上行波束管理，以及在 TDD（时分双工，Time Division Duplexing）下利用信道互易性推算下行预编码。它是参考信号体系（[[DMRS_解调参考信号]] 之外）的上行专属成员，与下行 CSI-RS 遥相呼应。

## 独立解释任务

任务目标：讲清 SRS 的用途（上行探测/频选调度/波束/TDD 互易性）、时频结构（梳状 comb 与符号数）、资源配置（RRC 周期 + DCI 触发非周期），以及它与上行链路自适应（Link_Adaptation）的关系。

## 科学定义

### SRS 的用途

1. 上行信道探测：基站从 SRS 估计每 RB（资源块，Resource Block）的上行 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio）——频选调度（把好 RB 分给 UE）与链路自适应的输入。
2. 上行波束管理：多波束场景下基站测各波束质量。
3. **TDD 互易性**：TDD 上下行同频，信道互易——基站用上行 SRS 估计信道，反推下行预编码（无需 UE 报 PMI（预编码矩阵指示，Precoding Matrix Indicator），省反馈开销；见 [[Link_Adaptation_链路自适应与CQI]] 的 TDD 互易性）。

### 时频结构（TS 38.211 §6.4.1）

- 梳状（comb）：SRS 只在每 N 个子载波上发一个（comb 2/4/8）——多个 UE 可交错复用同一符号资源（comb 交错 + 循环移位正交）。
- 时域：1/2/4（可配至 14）个符号，可配周期（1-320 ms，RRC（无线资源控制，Radio Resource Control）配置）+ 非周期触发（DCI 触发）。
- 频域：可宽带（覆盖整个 BWP（带宽部分，Bandwidth Part））或部分带宽（跳频探测）。

### 资源配置

- 周期/半持续 SRS：RRC 配置（SRS-Config，TS 38.331 §6.3.2）周期发送。
- 非周期 SRS：DCI（下行控制信息，Downlink Control Information）触发（TS 38.214 §6.2）——按需探测，省资源。
- 与功率控制：SRS 有独立功控参数集（见 [[Power_Control_上行功率控制]]）。

## 直观模型

SRS 像「给基站的地质探测仪」：每隔一段（comb）打一个探孔（符号），基站看探孔数据（SINR）决定在哪钻井（分配 RB）——探孔太密浪费（资源），太稀看不清（信道估计不准）；TDD 场景下探孔数据还能反推地下的情况（互易性→下行预编码）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| SRS 是下行信号 | SRS 是 UE 发的上行探测信号；下行对应的是 CSI-RS |
| SRS 只用于上行调度 | 还用于波束管理与 TDD 互易性下行预编码 |
| SRS 越多越好 | SRS 占上行资源，周期/触发式按需配置权衡 |
| 互易性对所有场景成立 | 仅 TDD 同频成立；FDD（频分双工，Frequency Division Duplexing）需 PMI 反馈 |

## 协议锚点

- SRS 物理结构：TS 38.211（Rel-19 j30）§6.4.1，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- SRS 触发与用途：TS 38.214（Rel-19 j30）§6.2，本地 `TS_38.214_38214-j30`。
- SRS 配置：TS 38.331（Rel-19 j20）§6.3.2（SRS-Config），本地 `TS_38.331_38331-j20`。
- 参考信号体系：[[DMRS_解调参考信号]]。

## 图谱关联

- [[概念图谱入口]]
- [[Link_Adaptation_链路自适应与CQI]]
- [[Power_Control_上行功率控制]]
- [[DMRS_解调参考信号]]
- [[Channel_Estimation_信道估计]]
- 关系语义：SRS 是上行链路的「眼睛」——为频选调度、波束与 TDD 互易性（下行预编码）提供信道信息，与下行 CSI-RS 构成参考信号体系的上下行对照，是链路自适应闭环的上行测量入口。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/SRS_探测参考信号.md" && grep -c "^## " "docs/concepts/SRS_探测参考信号.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/SRS_探测参考信号.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Power_Control_上行功率控制]]` 指向 E2（本批内将创建——E4 在 E2 后执行则存在；若 E4 先于 E2 执行则为计划内前瞻，E5 后闭合）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/SRS_探测参考信号.md" && git commit -m "docs(concepts): 新增 SRS 探测参考信号概念笔记（comb 结构/TDD 互易性）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E5: 新建概念笔记 `docs/concepts/UL_DL_Differences_上下行差异.md`

**Files:**
- Create: `3gpp/docs/concepts/UL_DL_Differences_上下行差异.md`

**Interfaces:**
- Consumes: E1-E4 四篇批内笔记（全部引用）。
- Produces: 该文件（批次收尾篇）；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 上下行差异
  - UL DL Differences
  - 上行链路 下行链路
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.211/38.213 综合; T7.5 先例对照"
---

# UL DL Differences 上下行差异

上行（UL，上行链路，Uplink）与下行（DL，下行链路，Downlink）共享同一套译码核心（Turbo/LDPC/Polar、软解调、HARQ），但物理层与协议机制差异显著：波形（OFDMA 下行 vs DFT-s-OFDM 上行可选）、功率（下行固定 vs 上行闭环功控）、定时（下行同步 vs 上行 TA（定时提前，Timing Advance））、参考信号（下行 CSI-RS/DMRS vs 上行 SRS/DMRS）、调度（DL assignment vs UL grant）、反馈方向（HARQ-ACK/CSI 全部上行承载）。理解这些差异是「全链路」视角的收束——LTE 有 T7.5（译码差异）先例，本篇做 NR 物理层/协议层全景对照。

## 独立解释任务

任务目标：系统对照 NR 上下行在波形、功率、定时、参考信号、调度、反馈、多址七个维度的差异，衔接批内四篇（DFT-s-OFDM/功控/PRACH/SRS）与既有控制面/调度笔记，形成上行链路的全景收束。

## 科学定义

### 七维度对照表

| 维度 | 下行（DL） | 上行（UL） |
|:---|:---|:---|
| 波形 | CP-OFDM（多载波，见 [[DFT_sOFDM_上行波形]]） | DFT-s-OFDM（低 PAPR）或 CP-OFDM（可配） |
| 功率控制 | 基站固定功率+调度分配 | 开环+闭环功控（[[Power_Control_上行功率控制]]） |
| 定时 | UE 被动同步（PSS/SSS 跟踪） | TA（定时提前）主动对齐基站接收窗（[[PRACH_随机接入]] 建立） |
| 参考信号 | CSI-RS（测量）/DMRS（解调） | SRS（探测）/DMRS（解调，见 [[SRS_探测参考信号]]） |
| 调度 | DL assignment（1_x DCI） | UL grant（0_x DCI，见 [[Scheduling_Grant_调度与授权]]） |
| 反馈 | —（反馈全在上行） | HARQ-ACK/CSI/SR 经 PUCCH/PUSCH（[[PUCCH_上行控制信道与UCI]]） |
| 多址 | 广播/共享（OFDMA 全网） | 多用户复用（comb/时频分，见 [[Multiple_Access_多址接入]]） |

### 差异的根源

1. **发射端不对称**：下行一个基站服务多 UE（功控/调度集中化），上行多 UE 各自发射（功率/定时/干扰各自管理）——这是波形（低 PAPR）、功控（闭环）、TA（同步）三类差异的共同根源。
2. **反馈方向单一**：所有控制反馈（ACK/CSI/SR）只能上行承载——上行是「控制信息汇聚方向」，PUCCH/PUSCH 的复用设计由此而来。
3. **信道互易**：TDD 同频使上行测量（SRS）可服务下行（预编码）——FDD 无此便利（PMI 反馈）。

### 与 LTE T7.5 的对照

LTE 已有 T7.5（LTE 下行与上行译码差异，`docs/L2_协议算法/T7.5_LTE_DL_UL_decoding_differences.md`）——从译码器视角对照 DL/UL 的协议链路、参数来源与 HARQ 上下文。本篇是物理层/协议层全景对照，两者互补：T7.5 讲「同一译码核心在 DL/UL 的接收差异」，本篇讲「物理层与协议机制的全景差异」。

## 直观模型

下行像「广播电台」：一个台（基站）发，所有收音机（UE）收，功率统一、时间统一；上行像「多对讲机同时说话」：每个人（UE）自己调节音量（功控）、对齐通话节奏（TA）、报自己的位置（SRS）——不对称的两端，机制自然不同。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 上行下行只有波形不同 | 波形只是七维度之一——功率/定时/参考信号/调度/反馈机制全不同 |
| TA 是下行概念 | TA 是上行发射定时调整（UE 提前发射抵消传播时延），由 RACH 建立 |
| 上下行译码完全一样 | 译码核心一样，但速率匹配/HARQ 上下文/descriptor 来源有差异（T7.5 详述） |
| TDD 互易性所有场景可用 | 仅 TDD 同频；FDD 上行探测不能直接用于下行（需 PMI） |

## 协议锚点

- 波形：TS 38.211 §5.3/§5.4（CP-OFDM/DFT-s-OFDM），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 功控：TS 38.213 §7（本地 `TS_38.213_38213-j30`）。
- 定时提前：TS 38.213 §4.2（TA 命令）、TS 38.321 §5.2（MAC 层 TA 处理）。
- 参考信号：TS 38.211 §7.4.1（DL）/§6.4.1（UL SRS）。
- LTE 先例：T7.5（`docs/L2_协议算法/T7.5_LTE_DL_UL_decoding_differences.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[DFT_sOFDM_上行波形]]
- [[Power_Control_上行功率控制]]
- [[PRACH_随机接入]]
- [[SRS_探测参考信号]]
- [[Multiple_Access_多址接入]]
- 关系语义：上下行差异是全链路的收束视角——波形/功控/TA/参考信号/调度/反馈七维度对照（本批四篇 + 控制面批次），与 LTE T7.5 的译码视角互补，为「上行链路」的知识闭环画上句号。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/UL_DL_Differences_上下行差异.md" && grep -c "^## " "docs/concepts/UL_DL_Differences_上下行差异.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/UL_DL_Differences_上下行差异.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink 批内四篇（E1-E4 已创建，存在）+ 控制面/调度批次笔记全部存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/UL_DL_Differences_上下行差异.md" && git commit -m "docs(concepts): 新增 UL DL Differences 上下行差异概念笔记（七维度全景对照，批次收尾）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E6: 同步清单（图谱入口 5 行 + L0 术语总表 5 项 + 索引 5 行 + 计数修正）

**Files:**
- Modify: `3gpp/docs/concepts/概念图谱入口.md`（「发送链路」组 3 行 + 「协议结构」组 2 行）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（「系统与协议」节 5 项 + 索引 5 行 + 引言计数）

**Interfaces:**
- Consumes: Task E1-E5 五个笔记名。
- Produces: 术语总表 5 项 + 挂载 5 行 + 索引 5 行。

- [ ] **Step 1: 图谱入口挂载 5 行**

Run: `grep -n "Physical_Channels_物理信道\|MCS_Table_Effective_Code_Rate" 3gpp/docs/concepts/概念图谱入口.md`
Expected: 行号 M1（发送链路组）/M2（协议结构组）。在对应组内追加：

```markdown
- [[DFT_sOFDM_上行波形]]
- [[PRACH_随机接入]]
- [[SRS_探测参考信号]]
```
（发送链路组）
```markdown
- [[Power_Control_上行功率控制]]
- [[UL_DL_Differences_上下行差异]]
```
（协议结构组）

- [ ] **Step 2: 术语总表新增 5 项**

在「## 系统与协议」节（`| SPS |` 行后）追加：

```markdown
| DFT-s-OFDM | 离散傅里叶变换扩展正交频分复用 | Discrete Fourier Transform Spread OFDM；NR 上行可选波形（低 PAPR）。→ [[DFT_sOFDM_上行波形]] |
| SC-FDMA | 单载波频分多址 | Single Carrier Frequency Division Multiple Access；LTE 上行波形，DFT-s-OFDM 前身。 |
| TPC | 发射功率控制命令 | Transmit Power Control Command；DCI 携带的闭环功控命令。→ [[Power_Control_上行功率控制]] |
| PHR | 功率余量报告 | Power Headroom Report；UE 上报功率余量，MAC 层。 |
| TA | 定时提前 | Timing Advance；UE 上行发射定时调整，RACH 建立。→ [[PRACH_随机接入]] |
```

- [ ] **Step 3: 概念笔记索引区追加 5 行（2 列格式）**

在「### 协议、信道与信号」分区末尾（`[[Link_Adaptation_链路自适应与CQI]]` 行后）追加：

```markdown
| [[DFT_sOFDM_上行波形]] | NR 上行 DFT-s-OFDM 波形原理与低 PAPR 优势。 |
| [[Power_Control_上行功率控制]] | 开环/闭环功控、TPC 与 PHR。 |
| [[PRACH_随机接入]] | 前导、四步/两步随机接入过程。 |
| [[SRS_探测参考信号]] | 上行探测、comb 结构与 TDD 互易性。 |
| [[UL_DL_Differences_上下行差异]] | 上下行七维度全景对照。 |
```

- [ ] **Step 4: 引言计数修正**

术语总表引言与索引区引言「（87 篇）」→ 修正为实测数（`ls docs/concepts/*.md | grep -v "概念图谱入口\|3GPP全流程" | wc -l`，应为 92）。

- [ ] **Step 5: 验证同步完整性**

Run:

```bash
cd 3gpp && grep -c "DFT_sOFDM_上行波形\|Power_Control_上行功率控制\|PRACH_随机接入\|SRS_探测参考信号\|UL_DL_Differences_上下行差异" docs/concepts/概念图谱入口.md docs/L0_协议阅读引导/L0_terminology_glossary.md && grep -c "^| DFT-s-OFDM \|^| SC-FDMA \|^| TPC \|^| PHR \|^| TA " docs/L0_协议阅读引导/L0_terminology_glossary.md
```

Expected: 图谱入口 5 处、术语表 ≥10 处（5 索引 + 5 条目）、5 项术语行齐全（输出 `5`）。

- [ ] **Step 6: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/概念图谱入口.md" "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "docs(sync): 图谱入口挂载上行五篇 + L0 术语总表登记 DFT-s-OFDM/SC-FDMA/TPC/PHR/TA + 计数修正

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E7: 全量验证

**Files:**
- 无新增；FAIL 则修复对应文件。

**Interfaces:**
- Consumes: Task E1-E6 全部改动 + 历次批次全部改动（合流验证）。

- [ ] **Step 1: 运行全部审计**

```bash
cd 3gpp && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_latex_render.py --syntax-only docs/concepts && python3 tools/audit_circled_digits.py && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs
```

Expected: 各工具 PASS/OK。**已知处置**：`3GPP全流程_缩写概念理论清单.md:21` 存量假阳性不改；link_integrity 在 E1-E6 落地后应无新 FAIL（E1-E4 的前瞻链接在 E5 创建后闭合）；任何新 FAIL → Step 2 修复后复跑，直到全绿。

- [ ] **Step 2: 修复 FAIL 并复跑**

按工具输出逐条修复，复跑 Step 1 全部命令。

- [ ] **Step 3: 提交（如有修复）**

```bash
cd /home/yys/AGENT/obsidian && git add -A 3gpp && git commit -m "fix(docs): 上行批次审计修复（如无修复跳过此步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task E8: 双推提交

**Files:**
- 无代码变更。

**Interfaces:**
- Consumes: Task E1-E7 全部提交。

- [ ] **Step 1: 确认工作区干净**

Run: `git status --porcelain` → 空输出。

- [ ] **Step 2: 推送双远端**

```bash
cd /home/yys/AGENT/obsidian && git push origin master 2>&1 | tail -4
```

Expected: Gitee 与 GitHub 两处 `master -> master`；单远端失败必须报告处理。

- [ ] **Step 3: 登记执行证据**

工具缺失（KaTeX/mmdc）在此汇报中显式声明验证缺口；登记 TA/SRS/PHR/SC-FDMA/TPC TECH_TERMS 全库治理（并入阶段 2 前置任务清单）。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——批次内容（G4 全量 5 篇）→ Task E1-E5；工具不扩 TECH_TERMS → Task E7。同步清单 → Task E6。
- 占位符：无 TBD/TODO；五篇笔记全文写入任务步骤。
- 一致性：wikilink 创建顺序正确（E1-E4 独立、E5 收尾引用全部；E1 的 PUCCH 引用与 E4 的 Power_Control 引用在对应批次篇创建后闭合）；术语配对完整三件套（连续两批次 30+ 处返工教训——E1-E5 内容已按「中文（English Full Name, ABBR）」写定）；数值自洽（LTE 前导 839/NR 139、comb 2/4/8、功控公式五参数、RACH 四步/两步）。
- 双链：E5 收尾篇↔E1-E4 互链闭环；批内篇与控制面/调度批次笔记（PUCCH/DCI/Scheduler/Link_Adaptation/Multiple_Access 等）双链。
- 阶段 2 前置登记更新：TA（15 篇）/SRS/PHR/SC-FDMA/TPC 并入 TECH_TERMS 全库治理清单（与 PDCCH/PUCCH/PBCH/NDI/RI 合并）。

