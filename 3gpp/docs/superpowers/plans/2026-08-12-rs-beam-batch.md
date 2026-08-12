# 参考信号与波束管理概念笔记批次 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按选项 3 批 A（物理层：参考信号谱系 + 波束管理）：5 篇概念笔记（CSI_RS / PTRS / TRS / CRS / Beam_Management）+ 同步清单 + 全量验证 + 双推。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-rs-beam-batch.md` 执行。变更文件：新建概念笔记 5 个、修改图谱入口/术语表 2 个。每个任务「内容 → 验证 → 提交」闭环。

**Tech Stack:** Markdown + LaTeX（--syntax-only）+ 项目 audit 工具链。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- 标题正式化（Rule 16）；带圈数字禁令（第 10 条）；英文术语首现**完整三件套**「中文（English Full Name, ABBR）」（Rule 10——四批次 50+ 处返工教训，本计划内容已按此写定，逐字转写即可；**发现裸用不要擅改，在 concerns 报告**）。
- 概念笔记六段式模板（独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联，末行「关系语义：…」）。
- wikilink 只指向已存在或本计划内将创建的目标；创建顺序：G1-G4（独立，G3/G5 引用 G1）→ G5 最后。
- 协议溯源精确到 TS 编号 + 章节号 + 本地 processed 路径；**CRS 为 LTE 专属制式，须标注制式边界**（本地有 TS 36.211）。
- 工具缺失（KaTeX/mmdc）显式声明验证缺口。
- 提交后 `git push origin master`（双推，收尾任务统一执行）。

---

### Task G1: 新建概念笔记 `docs/concepts/CSI_RS_信道状态信息参考信号.md`

**Files:**
- Create: `3gpp/docs/concepts/CSI_RS_信道状态信息参考信号.md`

**Interfaces:**
- Produces: 该文件，Task G3（TRS）与 G5（Beam）引用；挂在概念图谱入口「发送链路」组（与 DMRS/SRS 同组）。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 信道状态信息参考信号
  - CSI-RS
  - Channel State Information Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §7.4.1.5; TS 38.214 Rel-19 §5.2"
---

# CSI-RS 信道状态信息参考信号

CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）是下行测量参考信号：基站周期性/按需发送已知序列，UE 测量它得到下行信道状态，进而生成 CSI（信道状态信息，Channel State Information）报告（CQI（信道质量指示，Channel Quality Indicator）/PMI（预编码矩阵指示，Precoding Matrix Indicator）/RI（秩指示，Rank Indicator），见 [[Link_Adaptation_链路自适应与CQI]]）。它是链路自适应闭环的测量源，同时服务波束管理（[[Beam_Management_波束管理]]）与时频跟踪（[[TRS_跟踪参考信号]]）。

## 独立解释任务

任务目标：讲清 CSI-RS 的三大用途（CSI 测量/波束管理/跟踪）、时频结构与端口配置（端口数/密度/NZP-CSI-RS 资源集），以及与 DMRS（解调参考信号，Demodulation Reference Signal）和 SRS（探测参考信号，Sounding Reference Signal）在参考信号体系中的分工。

## 科学定义

### 三大用途

1. CSI 测量：UE 测 CSI-RS 的 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio）→ 折算 CQI/PMI/RI 上报（Link_Adaptation 闭环的输入，见 [[Link_Adaptation_链路自适应与CQI]]）。
2. 波束管理：多波束场景下 UE 测各 CSI-RS 波束的 L1-RSRP（层 1 参考信号接收功率，Layer 1 Reference Signal Received Power）→ 波束报告（[[Beam_Management_波束管理]]）。
3. 时频跟踪：配置 trs-Info 的 CSI-RS 兼作 TRS（跟踪参考信号，Tracking Reference Signal）——为定时/频偏跟踪环路提供参考（[[TRS_跟踪参考信号]]、T2.7/T2.8）。

### 时频结构与配置

- 端口数：1/2/4/8/12/16/24/32（协议表给出每端口密度组合）；密度：0.5/1/3 RE（资源元素，Resource Element）/PRB（物理资源块，Physical Resource Block）/端口。
- 配置：NZP-CSI-RS（非零功率 CSI-RS，Non-Zero-Power CSI-RS）资源由 RRC（无线资源控制，Radio Resource Control）配置（CSI-ResourceConfig，TS 38.331），周期/半持续/非周期三类（非周期由 DCI（下行控制信息，Downlink Control Information）触发）。
- 与 DMRS 分工：DMRS 用于 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）解调（与数据同传、UE 专用），CSI-RS 用于测量（独立发送、可多用户共用）——一个服务于"这包数据怎么解"，一个服务于"下次传输怎么配"。

## 直观模型

CSI-RS 像「体检中心的检测设备」：定期体检（周期发送）或临时加检（非周期触发），体检报告（CSI 报告）决定下次饮食方案（MCS（调制与编码方案，Modulation and Coding Scheme）/波束配置）；DMRS 是"吃饭时的试菜"（解调当次数据），CSI-RS 是"定期的营养评估"（规划后续传输）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CSI-RS 只用于 CSI 上报 | 还用于波束管理与时频跟踪（trs-Info 配置） |
| CSI-RS 是 UE 发的 | CSI-RS 是基站下行发送、UE 测量；上行对应 SRS（UE 发） |
| DMRS 和 CSI-RS 可以互换 | DMRS 解调（与数据同传），CSI-RS 测量（独立配置）——分工不同 |
| CSI-RS 密度越高越好 | 密度高测量准但开销大——按场景配置（移动性/多用户） |

## 协议锚点

- CSI-RS 结构与配置：TS 38.211（Rel-19 j30）§7.4.1.5，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- CSI 报告：TS 38.214（Rel-19 j30）§5.2，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- 配置参数：TS 38.331（Rel-19 j20）§6.3.2（CSI-ResourceConfig），本地 `3GPP_Rel19/processed/TS_38.331_38331-j20`。
- 测量衔接：[[CSI_SINR]]、T2.11（`docs/L1_基础/`）。

## 图谱关联

- [[概念图谱入口]]
- [[Link_Adaptation_链路自适应与CQI]]
- [[DMRS_解调参考信号]]
- [[SRS_探测参考信号]]
- [[Beam_Management_波束管理]]
- [[TRS_跟踪参考信号]]
- 关系语义：CSI-RS 是下行测量体系的核心——为链路自适应（CSI 报告）供数、为波束管理（L1-RSRP）供测、经 trs-Info 兼任跟踪（TRS），与 DMRS（解调）/SRS（上行探测）构成参考信号体系的下行测量半边。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/CSI_RS_信道状态信息参考信号.md" && grep -c "^## " "docs/concepts/CSI_RS_信道状态信息参考信号.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/CSI_RS_信道状态信息参考信号.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Beam_Management_波束管理]]`/`[[TRS_跟踪参考信号]]` 指向 G5/G3（批内将创建——计划内前瞻，G3/G5 后闭合）；`[[Link_Adaptation_链路自适应与CQI]]`/`[[DMRS_解调参考信号]]`/`[[SRS_探测参考信号]]`/`[[CSI_SINR]]` 存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/CSI_RS_信道状态信息参考信号.md" && git commit -m "docs(concepts): 新增 CSI-RS 信道状态信息参考信号概念笔记（测量/波束/跟踪三用途）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G2: 新建概念笔记 `docs/concepts/PTRS_相位跟踪参考信号.md`

**Files:**
- Create: `3gpp/docs/concepts/PTRS_相位跟踪参考信号.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 相位跟踪参考信号
  - PTRS
  - Phase Tracking Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §7.4.1.2/§6.4.1.2; TS 38.214 Rel-19 §5.1.6.3/§6.2.3"
---

# PTRS 相位跟踪参考信号

PTRS（相位跟踪参考信号，Phase Tracking Reference Signal）解决高频段的相位噪声问题：毫米波/高频下振荡器相位噪声使接收信号产生公共相位误差（CPE，Common Phase Error），破坏星座旋转。PTRS 提供已知相位基准，接收端用它估计并补偿 CPE。它随数据一起发送（DL 在 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）、UL 在 PUSCH（物理上行共享信道，Physical Uplink Shared Channel）），密度随子载波间隔与调制阶数调整。

## 独立解释任务

任务目标：讲清相位噪声问题与 CPE 的影响、PTRS 的补偿原理（相位基准）、时频密度配置（与 SCS（子载波间隔，Subcarrier Spacing）和调制阶数的关系），以及 DL/UL PTRS 的部署差异。

## 科学定义

### 相位噪声与 CPE

高频段（FR2（频率范围 2，Frequency Range 2）毫米波）本地振荡器相位噪声显著：所有子载波共享同一相位误差（公共相位误差 CPE）——星座整体旋转，且随符号变化。CPE 若不补偿，256QAM（正交幅度调制，Quadrature Amplitude Modulation）等高阶调制的星座点距小、误码率急剧上升。

### PTRS 补偿原理

PTRS 是与数据同传的已知序列：接收端估计 PTRS 位置的相位偏移 → 插值得到每个符号的 CPE → 对数据符号做相位旋转校正（去旋转）。它只占少量 RE（资源元素，Resource Element），密度远低于 DMRS（解调参考信号，Demodulation Reference Signal）——因为 CPE 在频域近似恒定，只需少量频域点即可插值。

### 密度配置（与 SCS/调制阶数的关系）

| 维度 | 规则 |
|:---|:---|
| 频域密度 | 每 K 个 RB 一个 PTRS RE——调度带宽越大 K 越大（NRB 阈值决定 K=2/4，默认 2） |
| 时域密度 | 每 L 个符号一个 PTRS——调制阶数越高 L 越小（高阶调制对相位更敏感，需更密） |
| 存在条件 | 仅配置了 PTRS 且调度资源足够时发送；未配置则无（data 传输照常） |

### DL/UL 差异

- DL PTRS：随 PDSCH 发送（TS 38.211 §7.4.1.2），与 DMRS 端口关联。
- UL PTRS：随 PUSCH 发送（TS 38.211 §6.4.1.2），DFT-s-OFDM 波形下与变换预编码交互（见 [[DFT_sOFDM_上行波形]]）。

## 直观模型

PTRS 像「画框上的水平仪」：画家（发送端）画完后给一条已知的水平线（PTRS），装裱师（接收端）发现画歪了（CPE）就按水平线整体摆正（相位校正）——画本身（数据）不用重画。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PTRS 是测量用的 | PTRS 是补偿相位噪声（CPE）的，不是 CSI 测量源 |
| PTRS 密度越高越好 | 高密度开销大——按 SCS/调制阶数自适应（大 SCS 稀疏、高阶调制加密） |
| 相位噪声只在毫米波有 | 低频也有但影响小——FR2 是主要应用场景 |
| PTRS 独立发送 | PTRS 随数据同传（PDSCH/PUSCH 内） |

## 协议锚点

- DL PTRS：TS 38.211（Rel-19 j30）§7.4.1.2，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- UL PTRS：TS 38.211 §6.4.1.2，本地同卷。
- 密度参数（timeDensity/frequencyDensity）：TS 38.214（Rel-19 j30）§5.1.6.3/§6.2.3，本地 `TS_38.214_38214-j30`。
- 相位噪声背景：T2.17（`docs/L1_基础/T2.17_OFDM_impairments_to_LLR.md` 手算例子提及）。

## 图谱关联

- [[概念图谱入口]]
- [[DMRS_解调参考信号]]
- [[CSI_RS_信道状态信息参考信号]]
- [[DFT_sOFDM_上行波形]]
- 关系语义：PTRS 是高频段可靠传输的保障——补偿 CPE 让高阶调制（256QAM）在高 SCS 下可用，与 DMRS（解调）/CSI-RS（测量）共同构成参考信号体系，UL 侧与 DFT-s-OFDM 波形交互。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/PTRS_相位跟踪参考信号.md" && grep -c "^## " "docs/concepts/PTRS_相位跟踪参考信号.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/PTRS_相位跟踪参考信号.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[CSI_RS_信道状态信息参考信号]]`（G1 已创建，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/PTRS_相位跟踪参考信号.md" && git commit -m "docs(concepts): 新增 PTRS 相位跟踪参考信号概念笔记（CPE 补偿与密度配置）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G3: 新建概念笔记 `docs/concepts/TRS_跟踪参考信号.md`

**Files:**
- Create: `3gpp/docs/concepts/TRS_跟踪参考信号.md`

**Interfaces:**
- Consumes: G1（CSI_RS，wikilink 引用）。
- Produces: 该文件；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 跟踪参考信号
  - TRS
  - Tracking Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §7.4.1.5; TS 38.214 Rel-19 §5.1.6"
---

# TRS 跟踪参考信号

TRS（跟踪参考信号，Tracking Reference Signal）维持 UE 的时频跟踪环路：接收端需要持续跟踪定时偏移与频偏（移动、时钟漂移、多普勒），TRS 提供可预测的参考信号供跟踪环路使用。NR 的 TRS 不是独立信号——它是配置了 trs-Info 的 CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）子集（见 [[CSI_RS_信道状态信息参考信号]]），周期性发送、结构紧凑，是定时同步（T2.7）与频偏同步（T2.8）在连接态的持续输入。

## 独立解释任务

任务目标：讲清 TRS 的用途（时频跟踪）、与 CSI-RS 的关系（trs-Info 子集配置）、时频结构与周期，以及它如何衔接定时/频偏同步（T2.7/T2.8）的跟踪环路。

## 科学定义

### 为什么需要持续跟踪

小区搜索（[[PSS_SSS_同步信号与小区搜索]]）只在初始接入做一次粗同步；连接态中 UE 移动、时钟漂移、多普勒使定时/频偏持续变化——需要周期参考信号驱动跟踪环路（PLL 类）维持细同步。TRS 就是这个"持续参考"。

### TRS = 配置了 trs-Info 的 CSI-RS

NR 协议不定义独立 TRS 信号：RRC 配置 CSI-RS 资源时设 trs-Info = true，该资源即作 TRS 用。特点：
- 周期发送（常见 10/20/40 ms）、固定时频结构（两簇符号对，便于前后相关做时延/频偏估计）。
- 与普通 CSI-RS 的差异在用途与密度优化（TRS 侧重跟踪精度而非宽带 CSI 测量）。

### 与同步链路的衔接

TRS 相关输出驱动：定时跟踪（FFT 窗口微调，T2.7 的跟踪环）、频偏跟踪（CFO（载波频偏，Carrier Frequency Offset）精估计，T2.8 的跟踪环）——是连接态时频同步的"心跳"。

## 直观模型

TRS 像「道路上的里程桩」：初始接入是"问一次路"（PSS/SSS），连接态开车时每隔一段看一次里程桩（TRS）校正车速表（时钟）和方向（频率）——不看会越开越偏。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| TRS 是独立信号 | TRS 是配置了 trs-Info 的 CSI-RS 子集——无独立序列 |
| TRS 用于 CSI 上报 | TRS 用于时频跟踪，CSI 测量用普通 CSI-RS 配置 |
| 同步只在初始接入做 | 初始接入粗同步后，连接态靠 TRS 持续跟踪 |
| TRS 和 PSS/SSS 一样只在固定位置 | TRS 周期/结构由 RRC 配置（trs-Info 资源） |

## 协议锚点

- TRS 配置（trs-Info）：TS 38.211（Rel-19 j30）§7.4.1.5（CSI-RS 含 trs-Info），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 跟踪过程：TS 38.214（Rel-19 j30）§5.1.6，本地 `TS_38.214_38214-j30`。
- 同步链路衔接：T2.7（定时同步）/T2.8（CFO/SFO），`docs/L1_基础/`。

## 图谱关联

- [[概念图谱入口]]
- [[CSI_RS_信道状态信息参考信号]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[Timing_Sync_定时同步]]
- 关系语义：TRS 是连接态时频同步的持续输入——作为 CSI-RS 的 trs-Info 子集存在，与初始接入的 PSS/SSS 粗同步衔接，驱动 T2.7/T2.8 的跟踪环路，是全链路"同步保持"环节。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/TRS_跟踪参考信号.md" && grep -c "^## " "docs/concepts/TRS_跟踪参考信号.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/TRS_跟踪参考信号.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[CSI_RS_信道状态信息参考信号]]`（G1 已创建，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/TRS_跟踪参考信号.md" && git commit -m "docs(concepts): 新增 TRS 跟踪参考信号概念笔记（trs-Info 子集与时频跟踪）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G4: 新建概念笔记 `docs/concepts/CRS_小区特定参考信号.md`

**Files:**
- Create: `3gpp/docs/concepts/CRS_小区特定参考信号.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 小区特定参考信号
  - CRS
  - Cell-specific Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 36.211 Rel-19 §6.10"
---

# CRS 小区特定参考信号

CRS（小区特定参考信号，Cell-specific Reference Signal）是 LTE 的下行参考信号：每个子帧、几乎全带宽发送，供解调、测量与同步使用。它「广播式」存在——小区内所有 UE 共用同一 CRS，这与 NR 的设计哲学（[[DMRS_解调参考信号]]/[[CSI_RS_信道状态信息参考信号]] 按 UE/用途专用化）形成鲜明代际对比。CRS 是 LTE 专属制式（TS 36.211），理解它是读懂「为什么 NR 抛弃 CRS」的关键。

## 独立解释任务

任务目标：讲清 CRS 的结构（端口/位置/周期）与用途（解调/测量/同步）、与 NR 参考信号体系（DMRS/CSI-RS）的设计对比，以及 NR 弃用 CRS 的动机（开销与灵活性）。

## 科学定义

### CRS 结构与用途（TS 36.211 §6.10）

- 结构：端口 0-3（最多 4 天线端口）、每子帧发送（1 ms 周期）、全带宽（与小区带宽同宽）、固定频域位置（按小区 ID（物理小区标识，Physical Cell Identity）偏移）。
- 用途三合一：(1) 解调——LTE 无专用 DMRS（Rel-8 起），PDSCH（物理下行共享信道，Physical Downlink Shared Channel）解调依赖 CRS 信道估计；(2) 测量——RSRP（参考信号接收功率，Reference Signal Received Power）/RSRQ 测量；(3) 同步——时间/频率跟踪。

### 与 NR 参考信号体系的对比

| 维度 | LTE CRS | NR DMRS/CSI-RS |
|:---|:---|:---|
| 覆盖 | 小区级广播（所有 UE 共用） | UE 专用/按需配置 |
| 发送 | 每子帧、全带宽 | 按需（时隙内、分配带宽内） |
| 开销 | 恒定（最高 4 端口 × 全带宽） | 随配置（低开销） |
| 波束 | 全向（无波束概念） | 可波束成形（DMRS/CSI-RS 随波束） |
| 解调 | CRS 兼任 | DMRS 专用（数据同传） |

### NR 弃用 CRS 的动机

(1) 开销：CRS 恒定占用资源，NR 按需配置省资源；(2) 灵活性：NR 支持多波束/多用户（MU-MIMO，多用户 MIMO，Multi-User MIMO），UE 专用 DMRS 可随波束与调度变化，CRS 无法适配；(3) 前向兼容：CRS 全带宽发送限制带宽动态扩展。代价：NR 接收端必须依赖 DMRS 解调（每传输都要做信道估计，见 [[Channel_Estimation_信道估计]]）。

## 直观模型

CRS 像「24 小时全城广播的电台」：所有居民（UE）共用同一信号（解调/测量/同步全靠它）——简单但费电（开销恒定）；NR 像「按需点播」：每次节目（数据传输）配专属字幕（DMRS），不定期插播路况（CSI-RS 测量）——省资源但每次都要现配。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| NR 也有 CRS | NR 无 CRS——LTE 专属（TS 36.211）；NR 用 DMRS/CSI-RS/PTRS/TRS |
| CRS 是 UE 专用信号 | CRS 是小区级广播（所有 UE 共用），NR 才 UE 专用化 |
| CRS 和 DMRS 一样只用于解调 | CRS 三合一（解调/测量/同步），DMRS 只管解调 |
| LTE 没有测量参考信号 | CRS 兼任测量（RSRP/RSRQ），NR 用 CSI-RS 专职测量 |

## 协议锚点

- CRS 结构：TS 36.211（Rel-19 j30）§6.10，本地 `3GPP_Rel19/processed/TS_36.211_*`。
- CRS 用途（RSRP 测量）：TS 36.214（Rel-19 j30）§5.1.1，本地 `TS_36.214_*`。
- **制式边界**：CRS 为 LTE 专属，NR 体系见 [[DMRS_解调参考信号]]/[[CSI_RS_信道状态信息参考信号]]——勿混用。

## 图谱关联

- [[概念图谱入口]]
- [[DMRS_解调参考信号]]
- [[CSI_RS_信道状态信息参考信号]]
- [[Channel_Estimation_信道估计]]
- [[PSS_SSS_同步信号与小区搜索]]
- 关系语义：CRS 是 LTE 参考信号体系的代表——理解它与 NR（DMRS/CSI-RS）的设计对比，就是理解「广播式 vs 按需式」两代物理层哲学的分水岭；信道估计（Channel_Estimation）在 LTE 以 CRS 为源、在 NR 以 DMRS 为源。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/CRS_小区特定参考信号.md" && grep -c "^## " "docs/concepts/CRS_小区特定参考信号.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/CRS_小区特定参考信号.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[CSI_RS_信道状态信息参考信号]]`（G1 已创建，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/CRS_小区特定参考信号.md" && git commit -m "docs(concepts): 新增 CRS 小区特定参考信号概念笔记（LTE 专属与 NR 设计对比）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G5: 新建概念笔记 `docs/concepts/Beam_Management_波束管理.md`

**Files:**
- Create: `3gpp/docs/concepts/Beam_Management_波束管理.md`

**Interfaces:**
- Consumes: G1（CSI_RS）等批内/既有笔记。
- Produces: 该文件（批次收尾篇）；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 波束管理
  - Beam Management
  - 波束失败恢复 BFR
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.213 Rel-19 §6; TS 38.331 Rel-19 §6.3.2"
---

# Beam Management 波束管理

波束管理（Beam Management）管理高频段（FR2）的定向传输：基站与 UE 用窄波束收发，需要先找到最佳波束对（beam pair），并在波束失效时快速恢复。流程分四步——波束测量（SSB/CSI-RS 波束的 L1-RSRP）、波束报告（UE 上报最佳波束）、波束指示（TCI 状态切换下行波束）、波束失败恢复（BFR，Beam Failure Recovery，检测+恢复）。它是 FR2 可靠性的核心机制，与 [[PSS_SSS_同步信号与小区搜索]]（SSB 波束扫描）、[[CSI_RS_信道状态信息参考信号]]（波束测量源）、[[PRACH_随机接入]]（BFR 专用前导）紧密衔接。

## 独立解释任务

任务目标：讲清波束管理的四步流程（测量/报告/指示/恢复）、SSB 与 CSI-RS 在波束测量中的分工、TCI 状态机制，以及 BFR 的检测与恢复过程。

## 科学定义

### 为什么需要波束管理

FR2 毫米波路径损耗大，需窄波束定向增益；但窄波束意味着「盲区」——波束对准错误/被遮挡（人体/建筑）即信号中断。波束管理就是「找到、保持、恢复」最佳波束对的全流程。

### 四步流程

1. 波束测量：基站周期发 SSB 波束（同步栅格扫描，见 [[PSS_SSS_同步信号与小区搜索]]）与 CSI-RS 波束（[[CSI_RS_信道状态信息参考信号]]）——UE 测各波束的 L1-RSRP（层 1 参考信号接收功率，Layer 1 Reference Signal Received Power）。
2. 波束报告：UE 上报最佳波束（SSBRI/CRI（CSI-RS 资源指示，CSI-RS Resource Indicator）+ L1-RSRP）。
3. 波束指示：基站用 TCI（传输配置指示，Transmission Configuration Indication）状态切换 PDSCH/PDCCH 的准共址（QCL，Quasi Co-Location）假设——「这次传输与哪个参考信号同方向」。
4. 波束失败恢复（BFR）：波束失败检测（下行参考信号质量低于门限）→ UE 用专用 PRACH 前导（或免竞争资源）发恢复请求 → 基站配置新波束（TCI 更新）——与随机接入（[[PRACH_随机接入]]）的 BFR 触发场景衔接。

### TDD 互易性

TDD（时分双工，Time Division Duplexing）下上下行同频，可用上行 SRS（探测参考信号，Sounding Reference Signal）探测替代下行波束测量（互易性，见 [[SRS_探测参考信号]]）——省下行测量开销。

## 直观模型

波束管理像「手电筒照路」：初始不知道路在哪，先四面八方扫一遍（SSB 波束扫描），找到最亮的照法（波束报告）；走路时定期确认方向（CSI-RS 波束测量），手电筒坏了（波束失败）就换备用方案（BFR 恢复请求）——方向对了才走得快（吞吐），方向错了寸步难行（中断）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 波束管理只在初始接入 | 初始扫描后连接态持续测量/指示/恢复——四步是循环不是一次性 |
| BFR 就是重做随机接入 | BFR 用专用前导/资源快速恢复，与初始随机接入（竞争）不同 |
| 波束只与下行有关 | 上行也有波束（SRS 探测/上行 TCI），TDD 互易性联动 |
| TCI 是物理层参数 | TCI 由 RRC/MAC-CE 配置、DCI 指示（跨层机制） |

## 协议锚点

- 波束管理过程：TS 38.213（Rel-19 j30）§6（波束失败检测/恢复），本地 `3GPP_Rel19/processed/TS_38.213_38213-j30`。
- TCI/QCL 配置：TS 38.331（Rel-19 j20）§6.3.2（TCI-State），本地 `TS_38.331_38331-j20`。
- 波束测量报告：TS 38.214（Rel-19 j30）§5.2（CSI 报告含 L1-RSRP），本地 `TS_38.214_38214-j30`。
- 衔接：[[PSS_SSS_同步信号与小区搜索]]、[[CSI_RS_信道状态信息参考信号]]、[[PRACH_随机接入]]。

## 图谱关联

- [[概念图谱入口]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[CSI_RS_信道状态信息参考信号]]
- [[PRACH_随机接入]]
- [[SRS_探测参考信号]]
- [[Link_Adaptation_链路自适应与CQI]]
- 关系语义：波束管理是 FR2 可靠性的核心——SSB 波束扫描（初始）+ CSI-RS 波束测量（持续）+ TCI 指示（切换）+ BFR（恢复）四步闭环，与随机接入（BFR 前导）、SRS（TDD 互易性）、链路自适应（L1-RSRP 报告）联动，是参考信号体系与移动性机制的汇合点。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Beam_Management_波束管理.md" && grep -c "^## " "docs/concepts/Beam_Management_波束管理.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Beam_Management_波束管理.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink 全部批内/既有（CSI_RS G1 已创建、PSS_SSS/PRACH/SRS/Link_Adaptation 既有）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Beam_Management_波束管理.md" && git commit -m "docs(concepts): 新增 Beam Management 波束管理概念笔记（测量/报告/指示/BFR 四步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G6: 同步清单（图谱入口 5 行 + L0 术语总表 4 项 + 索引 5 行 + 计数修正）

**Files:**
- Modify: `3gpp/docs/concepts/概念图谱入口.md`（「发送链路」组 5 行）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（「系统与协议」节 4 项 + 索引 5 行 + 引言计数）

**Interfaces:**
- Consumes: Task G1-G5 五个笔记名。
- Produces: 术语总表 4 项（PTRS/TRS/CRS/BFR——CSI-RS 已有）+ 挂载 5 行 + 索引 5 行。

- [ ] **Step 1: 图谱入口挂载 5 行**

Run: `grep -n "SRS_探测参考信号\|DFT_sOFDM_上行波形" 3gpp/docs/concepts/概念图谱入口.md`
Expected: 行号 M（「发送链路」组内）。在组内（SRS 行后或合适位置）追加：

```markdown
- [[CSI_RS_信道状态信息参考信号]]
- [[PTRS_相位跟踪参考信号]]
- [[TRS_跟踪参考信号]]
- [[CRS_小区特定参考信号]]
- [[Beam_Management_波束管理]]
```

- [ ] **Step 2: 术语总表新增 4 项**

在「## 系统与协议」节（`| Qm |` 行后）追加：

```markdown
| PTRS | 相位跟踪参考信号 | Phase Tracking Reference Signal；补偿相位噪声 CPE，随数据同传。→ [[PTRS_相位跟踪参考信号]] |
| TRS | 跟踪参考信号 | Tracking Reference Signal；时频跟踪用，CSI-RS 的 trs-Info 子集。→ [[TRS_跟踪参考信号]] |
| CRS | 小区特定参考信号 | Cell-specific Reference Signal；LTE 专属广播式下行参考信号。→ [[CRS_小区特定参考信号]] |
| BFR | 波束失败恢复 | Beam Failure Recovery；波束失效检测与恢复过程。→ [[Beam_Management_波束管理]] |
```

- [ ] **Step 3: 概念笔记索引区追加 5 行（2 列格式）**

在「### 协议、信道与信号」分区末尾（`[[TX_Chain_发送端处理链总览]]` 行后）追加：

```markdown
| [[CSI_RS_信道状态信息参考信号]] | 下行测量参考信号（CSI 测量/波束/跟踪三用途）。 |
| [[PTRS_相位跟踪参考信号]] | 相位噪声 CPE 补偿，随数据同传。 |
| [[TRS_跟踪参考信号]] | CSI-RS 的 trs-Info 子集，时频跟踪。 |
| [[CRS_小区特定参考信号]] | LTE 专属广播式参考信号（解调/测量/同步）。 |
| [[Beam_Management_波束管理]] | 波束测量/报告/指示/BFR 四步闭环。 |
```

- [ ] **Step 4: 引言计数修正**

术语总表引言与索引区引言「（95 篇）」→ 修正为实测数（`ls docs/concepts/*.md | grep -v "概念图谱入口\|3GPP全流程" | wc -l`，应为 100）。

- [ ] **Step 5: 验证同步完整性**

Run:

```bash
cd 3gpp && grep -c "CSI_RS_信道状态信息参考信号\|PTRS_相位跟踪参考信号\|TRS_跟踪参考信号\|CRS_小区特定参考信号\|Beam_Management_波束管理" docs/concepts/概念图谱入口.md docs/L0_协议阅读引导/L0_terminology_glossary.md && grep -c "^| PTRS \|^| TRS \|^| CRS \|^| BFR " docs/L0_协议阅读引导/L0_terminology_glossary.md
```

Expected: 图谱入口 5 处、术语表 ≥9 处（5 索引 + 4 条目）、4 项术语行齐全（输出 `4`）。

- [ ] **Step 6: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/概念图谱入口.md" "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "docs(sync): 图谱入口挂载参考信号与波束五篇 + L0 术语总表登记 PTRS/TRS/CRS/BFR + 计数修正

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G7: 全量验证

**Files:**
- 无新增；FAIL 则修复对应文件。

**Interfaces:**
- Consumes: Task G1-G6 全部改动 + 历次批次全部改动（合流验证）。

- [ ] **Step 1: 运行全部审计**

```bash
cd 3gpp && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_latex_render.py --syntax-only docs/concepts && python3 tools/audit_circled_digits.py && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs
```

Expected: 各工具 PASS/OK。**已知处置**：`3GPP全流程_缩写概念理论清单.md:21` 存量假阳性不改；link_integrity 在 G1-G6 落地后应无新 FAIL（G1 的前瞻链接在 G3/G5 创建后闭合）；任何新 FAIL → Step 2 修复后复跑，直到全绿。

- [ ] **Step 2: 修复 FAIL 并复跑**

按工具输出逐条修复，复跑 Step 1 全部命令。

- [ ] **Step 3: 提交（如有修复）**

```bash
cd /home/yys/AGENT/obsidian && git add -A 3gpp && git commit -m "fix(docs): 参考信号与波束批次审计修复（如无修复跳过此步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task G8: 双推提交

**Files:**
- 无代码变更。

**Interfaces:**
- Consumes: Task G1-G7 全部提交。

- [ ] **Step 1: 确认工作区干净**

Run: `git status --porcelain` → 空输出。

- [ ] **Step 2: 推送双远端**

```bash
cd /home/yys/AGENT/obsidian && git push origin master 2>&1 | tail -4
```

Expected: Gitee 与 GitHub 两处 `master -> master`；单远端失败必须报告处理。

- [ ] **Step 3: 登记执行证据**

工具缺失（KaTeX/mmdc）在此汇报中显式声明验证缺口；批 A 完成后登记选项 3 剩余批 B（MAC 层映射/CA/BWP/射频前端）为下一批次。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——批次组织（批 A 物理层 5 篇）→ Task G1-G5；工具不扩 TECH_TERMS → Task G7。同步清单 → Task G6。
- 占位符：无 TBD/TODO；五篇笔记全文写入任务步骤。
- 一致性：wikilink 创建顺序正确（G1 CSI_RS 先建，G2/G3/G4 独立、G5 Beam 收尾引用；G1 引用 G3/G5 的前瞻在 G3/G5 创建后闭合）；术语配对完整三件套（四批次 50+ 处返工教训——G1-G5 内容已按「中文（English Full Name, ABBR）」写定）；数值自洽（CSI-RS 端口 1-32、PTRS 密度 SCS/Qm 自适应、CRS 端口 0-3/LTE 专属、TRS 周期 10/20/40 ms）。
- 双链：G5 收尾篇↔G1/G3 互链 + 既有（PSS_SSS/PRACH/SRS/Link_Adaptation/Timing_Sync）全链；参考信号四篇（DMRS/CSI_RS/PTRS/TRS/CRS/SRS）体系内互链。
- 批 B 登记：MAC 层映射/CA/BWP/射频前端为选项 3 下一批次。

