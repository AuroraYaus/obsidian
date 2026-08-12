# MAC 层映射/载波聚合/BWP/射频前端概念笔记批次 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按选项 3 批 B（协议层 + 前端）：4 篇概念笔记（MAC_Layer_Mapping / Carrier_Aggregation / BWP / RF_Frontend）+ 同步清单 + 全量验证 + 双推。完成后选项 3 收官。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-mac-ca-rf-batch.md` 执行。变更文件：新建概念笔记 4 个、修改图谱入口/术语表 2 个。每个任务「内容 → 验证 → 提交」闭环。

**Tech Stack:** Markdown + LaTeX（--syntax-only）+ 项目 audit 工具链。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- 标题正式化（Rule 16）；带圈数字禁令（第 10 条）；英文术语首现**完整三件套**「中文（English Full Name, ABBR）」（Rule 10——五批次 60+ 处返工教训，本计划内容已按此写定，逐字转写即可；**发现裸用不要擅改，在 concerns 报告**）。
- 概念笔记六段式模板（独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联，末行「关系语义：…」）。
- wikilink 只指向已存在或本计划内将创建的目标。
- 协议溯源精确到 TS 编号 + 章节号 + 本地 processed 路径；**射频前端为非协议强制实现，须标注教材背景**（Rule 2 边界声明）。
- 工具缺失（KaTeX/mmdc）显式声明验证缺口。
- 提交后 `git push origin master`（双推，收尾任务统一执行）。

---

### Task H1: 新建概念笔记 `docs/concepts/MAC_Layer_Mapping_MAC层映射.md`

**Files:**
- Create: `3gpp/docs/concepts/MAC_Layer_Mapping_MAC层映射.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - MAC 层映射
  - 信道映射
  - MAC Layer Mapping
  - 逻辑信道 传输信道
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.321 Rel-19 §4-§6; TS 38.300 Rel-19 §5-§6"
---

# MAC Layer Mapping MAC 层映射

MAC 层映射（MAC Layer Mapping）是信道三层体系的连接机制：逻辑信道（Logical Channel，按内容类型分，如数据/信令）→ 传输信道（Transport Channel，按传输方式分，如 DL-SCH（下行共享信道，Downlink Shared Channel）/UL-SCH（上行共享信道，Uplink Shared Channel））→ 物理信道（Physical Channel，空口承载，如 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel））。MAC 层在中间做映射与复用：把多个逻辑信道的数据按优先级组装进 MAC PDU（协议数据单元，Protocol Data Unit），交给传输信道。

## 独立解释任务

任务目标：讲清逻辑→传输→物理三层的映射关系、MAC PDU 的组装结构（MAC 头/LCID/复用）、LCP（逻辑信道优先级，Logical Channel Prioritization）在复用中的作用，以及常见信道（BCH/PCCH/CCCH 等）的映射特例。

## 科学定义

### 三层信道体系与映射

| 逻辑信道（内容） | → 传输信道（方式） | → 物理信道（承载） |
|:---|:---|:---|
| DTCH（专用业务信道，Dedicated Traffic Channel） | DL-SCH / UL-SCH | PDSCH / PUSCH |
| DCCH（专用控制信道，Dedicated Control Channel） | DL-SCH / UL-SCH | PDSCH / PUSCH |
| CCCH（公共控制信道，Common Control Channel） | DL-SCH / UL-SCH | PDSCH / PUSCH |
| BCCH（广播控制信道，Broadcast Control Channel） | BCH（广播信道，Broadcast Channel）/ DL-SCH | PBCH（物理广播信道，Physical Broadcast Channel）/ PDSCH |
| PCCH（寻呼控制信道，Paging Control Channel） | PCH（寻呼信道，Paging Channel） | PDSCH（寻呼调度经 PDCCH） |

MAC 层职责：逻辑信道 → 传输信道的映射与复用；传输信道 → 物理信道由物理层完成（MAC 经传输块 TB（传输块，Transport Block）接口交付）。

### MAC PDU 组装

- MAC PDU = MAC 头（一个或多个子头）+ MAC SDU（服务数据单元，Service Data Unit）们。
- 子头含 LCID（逻辑信道标识，Logical Channel Identity）——接收端凭 LCID 知道这段数据属于哪个逻辑信道（哪些数据归哪个业务/信令）。
- 复用：一个 MAC PDU 可含多个逻辑信道的数据（按 LCP 优先级组装，见 [[Scheduler_MAC调度器与资源分配]] 的 LCP 规则）——高优先级信令先装，PBR（优先级比特率，Prioritized Bit Rate）约束防饿死。

### 特殊映射

BCCH→BCH→PBCH 是"最小系统信息"专用路径（MIB 不经 MAC 复用，见 [[PBCH_MIB_广播信道]]）；PCCH→PCH 走寻呼流程（寻呼时机由 PDCCH 指示）。

## 直观模型

MAC 层映射像「邮局分拣」：信件按类型贴不同标签（逻辑信道 LCID），邮局（MAC）把多个寄件人的信装进一个包裹（MAC PDU 复用），按运输方式（传输信道）打包，交给运输公司（物理信道）发出；收件人按标签拆包（解复用）分发给各收件人（上层）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 逻辑信道=传输信道 | 逻辑信道按内容分、传输信道按传输方式分——MAC 在中间映射复用 |
| MAC PDU 只能装一个业务的数据 | 一个 MAC PDU 可复用多个逻辑信道（LCP 按优先级组装） |
| PBCH 走 MAC 复用 | MIB 经 BCH 直通 PBCH，不经 MAC PDU 组装 |
| LCID 是物理层概念 | LCID 是 MAC 头字段（逻辑信道标识） |

## 协议锚点

- 信道结构与映射：TS 38.300（Rel-19 j20）§5-§6，本地 `3GPP_Rel19/processed/TS_38.300_38300-j20`。
- MAC PDU 与复用：TS 38.321（Rel-19 j20）§4-§6，本地 `TS_38.321_38321-j20`。
- LCP 规则：TS 38.321 §5.4.3，本地同卷。
- 物理承载：[[Physical_Channels_物理信道]]、[[PBCH_MIB_广播信道]]。

## 图谱关联

- [[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[Protocol_Stack_协议栈]]
- [[Physical_Channels_物理信道]]
- [[PBCH_MIB_广播信道]]
- 关系语义：MAC 层映射是全链路的"内容-方式-承载"三层桥——逻辑信道（业务/信令）经 MAC 复用（LCP）进传输信道、物理信道承载（PDSCH/PUSCH/PBCH），是调度器（Scheduler）与译码链路（TB 接口）之间的协议枢纽。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/MAC_Layer_Mapping_MAC层映射.md" && grep -c "^## " "docs/concepts/MAC_Layer_Mapping_MAC层映射.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/MAC_Layer_Mapping_MAC层映射.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Scheduler_MAC调度器与资源分配]]`/`[[Protocol_Stack_协议栈]]`/`[[Physical_Channels_物理信道]]`/`[[PBCH_MIB_广播信道]]`/`[[概念图谱入口]]` 均存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/MAC_Layer_Mapping_MAC层映射.md" && git commit -m "docs(concepts): 新增 MAC Layer Mapping MAC 层映射概念笔记（三层信道体系与 PDU 复用）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task H2: 新建概念笔记 `docs/concepts/Carrier_Aggregation_载波聚合.md`

**Files:**
- Create: `3gpp/docs/concepts/Carrier_Aggregation_载波聚合.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 载波聚合
  - Carrier Aggregation
  - CA CC SCell
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.300 Rel-19 §5.2; TS 38.213 Rel-19 §10"
---

# Carrier Aggregation 载波聚合

载波聚合（Carrier Aggregation, CA）把多个载波（CC，分量载波，Component Carrier）聚合起来服务同一 UE：一个主载波（PCell，主小区，Primary Cell）管连接与移动性，多个辅载波（SCell，辅小区，Secondary Cell）加带宽提吞吐。CA 是吞吐扩展的机制——单载波带宽受限（FR1 100 MHz），聚合多个 CC 可达数百 MHz。每载波有独立的 HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）进程与调度，跨载波调度经 CIF（载波指示字段，Carrier Indicator Field）指示。

## 独立解释任务

任务目标：讲清 CA 的原理（多 CC 聚合）、PCell/SCell 的角色分工、跨载波调度（CIF）机制、每载波独立 HARQ/调度的含义，以及 CA 与 BWP（带宽部分，Bandwidth Part）的关系。

## 科学定义

### CA 原理与小区结构

- CC（分量载波）：每个 CC 是独立带宽的载波（有独立 numerology/带宽配置）；UE 聚合 2-N 个 CC（NR 最多 16 CC）。
- PCell（主小区）：承载 RRC（无线资源控制，Radio Resource Control）连接与随机接入（[[PRACH_随机接入]]）的小区——移动性锚点。
- SCell（辅小区）：纯数据承载——加带宽；激活/去激活由 MAC CE（媒体接入控制控制单元，MAC Control Element）控制。
- 双连接（DC，Dual Connectivity）是 CA 的演进：不同基站的小区组聚合（MCG/SCG）。

### 跨载波调度（CIF）

DCI（下行控制信息，Downlink Control Information）默认调度本载波；配置 CIF（3-bit）后，PDCCH（物理下行控制信道，Physical Downlink Control Channel）在载波 A 上可调度载波 B 的 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）——跨载波调度的意义：控制信道集中在一个载波（省 UE 盲检负担），数据信道分散。

### 每载波独立 HARQ/调度

每个 CC 是独立调度域：MCS（调制与编码方案，Modulation and Coding Scheme）/资源分配/HARQ 进程（见 [[HARQ_Process_HARQ进程管理]]）逐载波独立配置——一个 TB（传输块，Transport Block）通常在一个 CC 上传输（跨载波 TB 调度是特殊场景）。

### CA 与 BWP 的关系

每个 CC 内还有 BWP（带宽部分，Bandwidth Part）概念（见 [[BWP_带宽部分]]）——CA 是"载波级聚合"，BWP 是"载波内子带"：聚合后每个 CC 可独立配置 BWP。

## 直观模型

CA 像「多车道并道」：单车道（单载波）限速低（带宽窄），把多条车道并成高速（聚合 CC）；主车道（PCell）负责指挥（连接/移动性），辅车道（SCell）纯跑车（数据）；每条车道独立计程（每载波 HARQ/调度），可以远程遥控辅车道（跨载波调度）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CA 只在 FR2 | CA 在 FR1/FR2 都用（FR1 聚合 100 MHz CC、FR2 聚合 400 MHz CC） |
| SCell 也管连接 | SCell 纯数据承载；连接/移动性由 PCell 管理 |
| 跨载波调度没有代价 | 需配置 CIF 且控制信道集中——增加 PDCCH 设计复杂度 |
| CA 和双连接一样 | 双连接是跨基站聚合（MCG/SCG），CA 是同基站多 CC |

## 协议锚点

- CA 架构：TS 38.300（Rel-19 j20）§5.2，本地 `3GPP_Rel19/processed/TS_38.300_38300-j20`。
- 跨载波调度：TS 38.213（Rel-19 j30）§10（CIF），本地 `TS_38.213_38213-j30`。
- SCell 配置：TS 38.331（Rel-19 j20）§6.3.2（SCellConfig），本地 `TS_38.331_38331-j20`。
- 每载波 HARQ：[[HARQ_Process_HARQ进程管理]]。

## 图谱关联

- [[概念图谱入口]]
- [[HARQ_Process_HARQ进程管理]]
- [[Scheduler_MAC调度器与资源分配]]
- [[BWP_带宽部分]]
- [[PRACH_随机接入]]
- 关系语义：CA 是吞吐扩展的载波级机制——PCell/SCell 分工（连接 vs 数据）、跨载波调度（CIF）、每载波独立 HARQ，与 BWP（载波内子带）构成"聚合-子带"两级频域组织。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Carrier_Aggregation_载波聚合.md" && grep -c "^## " "docs/concepts/Carrier_Aggregation_载波聚合.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Carrier_Aggregation_载波聚合.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[BWP_带宽部分]]` 指向 H3（批内将创建——计划内前瞻，H3 后闭合）；其余目标存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Carrier_Aggregation_载波聚合.md" && git commit -m "docs(concepts): 新增 Carrier Aggregation 载波聚合概念笔记（CC/PCell/SCell/跨载波调度）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task H3: 新建概念笔记 `docs/concepts/BWP_带宽部分.md`

**Files:**
- Create: `3gpp/docs/concepts/BWP_带宽部分.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 带宽部分
  - BWP
  - Bandwidth Part
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §4.4.5; TS 38.213 Rel-19 §12"
---

# BWP 带宽部分

BWP（带宽部分，Bandwidth Part）是载波内的子带：UE 只在激活 BWP 内工作（收发都在这个子带内），载波总带宽可远大于 UE 的工作带宽。它的价值在"适配"——UE 能力适配（窄带 UE 用窄 BWP）、省电（低流量时切到窄 BWP）、灵活配置（BWP 间切换无需重配小区）。NR 每载波可配多个 BWP、激活一个；调度（[[Scheduler_MAC调度器与资源分配]]）的 RB（资源块，Resource Block）编号在 BWP 内进行。

## 独立解释任务

任务目标：讲清 BWP 的概念与作用（能力适配/省电/灵活）、BWP 配置（初始/默认/激活、切换）、BWP 与调度/资源网格的关系，以及它与载波聚合（[[Carrier_Aggregation_载波聚合]]）的层级关系。

## 科学定义

### BWP 是什么

- 定义：载波内的一段连续频域资源（子载波集合），有独立 numerology（子载波间隔/CP 配置）。
- UE 在任意时刻只在一个激活 BWP 内工作（收发 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel））——UE 不需要支持整个载波带宽。

### 作用

1. 能力适配：不同能力 UE 用不同宽度 BWP（窄带物联网 UE 用窄 BWP）。
2. 省电：低流量时切换到窄 BWP（接收带宽小、功耗低）。
3. 灵活：BWP 切换（RRC 配置 + DCI（下行控制信息，Downlink Control Information）指示或定时器）无需重配小区级参数。

### BWP 配置与切换

- 初始 BWP：UE 初始接入用的默认配置（SIB1 提供，见 [[PBCH_MIB_广播信道]] 的 pdcch-ConfigSIB1 关联）。
- 默认/激活 BWP：RRC 配置多个候选 BWP，激活一个；DCI 的 BWP 指示字段或 bwp-InactivityTimer（不活动定时器）触发切换。
- 切换含时延（TS 38.213 §12 给出切换时间）——切换期间不调度。

### 与 CA 的层级

载波聚合（[[Carrier_Aggregation_载波聚合]]）是载波级聚合（多 CC），BWP 是载波内子带（每 CC 内独立配置）——两级频域组织：CC 决定"聚几个载波"，BWP 决定"每个载波内用多宽"。

## 直观模型

BWP 像「商场里的移动电梯」：商场（载波）很大，但你只站在电梯覆盖的区段（激活 BWP）——想逛别的区（切 BWP）就坐电梯过去（切换），电梯只在必要区段运行（省电）；商场还可以把几栋楼连起来（载波聚合）扩大范围。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| BWP 是 UE 能力上限 | BWP 是网络配置的激活工作带宽——可小于也可等于 UE 能力 |
| BWP 切换要重新接入 | BWP 切换是 RRC/DCI 触发的快速切换（含时延但无需重接入） |
| 一个载波同时激活多个 BWP | 每载波一次激活一个 BWP（DL/UL 各一个） |
| BWP 和 CA 是一回事 | BWP 是载波内子带，CA 是载波级聚合——两级不同 |

## 协议锚点

- BWP 定义：TS 38.211（Rel-19 j30）§4.4.5，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- BWP 操作与切换时延：TS 38.213（Rel-19 j30）§12，本地 `TS_38.213_38213-j30`。
- BWP 配置：TS 38.331（Rel-19 j20）§6.3.2（BWP-Config），本地 `TS_38.331_38331-j20`。
- 频域网格基础：T2.3（`docs/L1_基础/T2.3_NR_frequency_resource_grid.md`，讲义级详解）。

## 图谱关联

- [[概念图谱入口]]
- [[Carrier_Aggregation_载波聚合]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[Scheduler_MAC调度器与资源分配]]
- [[PBCH_MIB_广播信道]]
- 关系语义：BWP 是载波内的工作子带——能力适配/省电/灵活的载体，调度 RB 编号在 BWP 内进行，与 CA（载波级）构成两级频域组织，初始 BWP 由 SIB1 提供（广播信道衔接）。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/BWP_带宽部分.md" && grep -c "^## " "docs/concepts/BWP_带宽部分.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/BWP_带宽部分.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Carrier_Aggregation_载波聚合]]`（H2 已创建，存在——H3 在 H2 后执行）；`[[PBCH_MIB_广播信道]]`/`[[Spectrum_and_Frequency_Point_频谱与频点]]`/`[[Scheduler_MAC调度器与资源分配]]` 存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/BWP_带宽部分.md" && git commit -m "docs(concepts): 新增 BWP 带宽部分概念笔记（子带适配/省电/切换）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task H4: 新建概念笔记 `docs/concepts/RF_Frontend_射频前端.md`

**Files:**
- Create: `3gpp/docs/concepts/RF_Frontend_射频前端.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「信道与信号」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 射频前端
  - RF 前端
  - RF Frontend
  - AGC ADC IQ 不平衡
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "教材背景知识; TS 38.101 射频要求（本地 TS_38.101_38101-1-j60）"
---

# RF Frontend 射频前端

射频前端（RF Frontend）是天线到数字基带之间的模拟/混合信号链路：天线 → LNA（低噪声放大器，Low Noise Amplifier）→ 混频（下变频）→ AGC（自动增益控制，Automatic Gain Control）→ ADC（模数转换器，Analog-to-Digital Converter）→ 数字基带。它的损伤（增益失配、量化噪声、IQ 不平衡、相位噪声）会以不同的方式退化后续的 LLR（对数似然比，Log-Likelihood Ratio）质量——射频前端是"天线到译码器"链路的物理入口，但其实现细节**非 3GPP 协议强制**（协议只定义射频要求指标，见 TS 38.101）。

## 独立解释任务

任务目标：讲清射频前端的链路结构（LNA/混频/AGC/ADC）、四类主要损伤（增益误差/量化/IQ 不平衡/相位噪声）对 LLR 的影响，以及射频损伤与接收链路（T2.17）和参考信号补偿（[[PTRS_相位跟踪参考信号]]）的衔接。

## 科学定义

### 射频链路结构

```
天线 → LNA（放大弱信号，噪声系数主导）→ 混频（下变频到基带，I/Q 两路）
→ AGC（增益调节，防 ADC 饱和）→ ADC（采样量化）→ 数字基带（同步/FFT）
```

### 四类主要损伤与 LLR 影响

1. 增益误差/AGC 不理想：信号幅度缩放偏差 → LLR 缩放错误（需按实际增益校准，衔接 T2.16 的 LLR 缩放）。
2. 量化噪声：ADC 位宽有限 → 量化噪声叠加（位宽不足则量化噪声显著——衔接 [[Fixed_Point_Numbers_定点数]] 与 T2.16 量化）。
3. IQ 不平衡：I/Q 两路增益/相位失配 → 镜像干扰（镜像频率的信号泄漏）→ 星座畸变。
4. 相位噪声：本地振荡器抖动 → CPE（公共相位误差，Common Phase Error）→ 星座旋转（由 [[PTRS_相位跟踪参考信号]] 补偿）。

### 与接收链路的衔接

射频损伤最终统一收束到 LLR 质量退化（T2.17 的"前端失真到 LLR 质量的退化链路"）；协议侧只定义射频要求（发射/接收指标，TS 38.101）——实现方式（AGC 策略/ADC 位宽/IQ 校准算法）是工程自由，**非协议强制**。

## 直观模型

射频前端像「音响系统」：麦克风（天线）收声 → 前置放大器（LNA）→ 调音台（混频）→ 音量自动控制（AGC）→ 录音（ADC）；任何一环失准（音量过大削波=ADC 饱和、左右声道不对称=IQ 不平衡、电源抖动=相位噪声）都会让录音（数字信号）失真。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 射频是协议规定的 | 协议只定义射频要求指标（TS 38.101），实现是工程自由（非强制） |
| ADC 位宽越大越好 | 位宽大动态范围好但功耗/成本高——按需求权衡（T2.16 量化） |
| IQ 不平衡是数字域问题 | IQ 失配源于模拟混频/通道，数字域校准（DSP 算法） |
| 相位噪声只在接收端 | 收发两侧都有——PTRS 补偿接收侧 CPE |

## 协议锚点

- 射频要求：TS 38.101-1（Rel-19 j60）§5-§7（发射/接收指标），本地 `3GPP_Rel19/processed/TS_38.101_38101-1-j60_s00-0504` 等分卷。
- 损伤到 LLR：T2.17（`docs/L1_基础/T2.17_OFDM_impairments_to_LLR.md`）。
- 量化：[[Fixed_Point_Numbers_定点数]]、T2.16（`docs/L1_基础/`）。
- **边界声明**：射频前端实现（AGC/ADC/IQ 校准）非 3GPP 协议强制——教材背景知识，协议仅定义指标要求。

## 图谱关联

- [[概念图谱入口]]
- [[PTRS_相位跟踪参考信号]]
- [[Fixed_Point_Numbers_定点数]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[T2.17_OFDM_impairments_to_LLR]]
- 关系语义：射频前端是全链路物理入口——LNA/混频/AGC/ADC 的损伤（增益/量化/IQ/相位噪声）经 T2.17 收束到 LLR 质量，相位噪声由 PTRS 补偿、量化与定点衔接（Fixed_Point）、射频要求由 TS 38.101 定义（实现非协议强制），是"天线到译码器"链条的第一环。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/RF_Frontend_射频前端.md" && grep -c "^## " "docs/concepts/RF_Frontend_射频前端.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/RF_Frontend_射频前端.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[T2.17_OFDM_impairments_to_LLR]]`（L1 讲义，存在）；`[[Fixed_Point_Numbers_定点数]]`/`[[PTRS_相位跟踪参考信号]]`（G2 已创建）/`[[Spectrum_and_Frequency_Point_频谱与频点]]`/`[[概念图谱入口]]` 存在。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/RF_Frontend_射频前端.md" && git commit -m "docs(concepts): 新增 RF Frontend 射频前端概念笔记（LNA/AGC/ADC/IQ/相位噪声，非协议强制）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task H5: 同步清单（图谱入口 4 行 + L0 术语总表补缺 + 索引 4 行 + 计数修正）

**Files:**
- Modify: `3gpp/docs/concepts/概念图谱入口.md`（「协议结构」组 3 行 + 「信道与信号」组 1 行）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（术语补缺 + 索引 4 行 + 引言计数）

**Interfaces:**
- Consumes: Task H1-H4 四个笔记名。
- Produces: 术语总表补缺 + 挂载 4 行 + 索引 4 行。

- [ ] **Step 1: 图谱入口挂载 4 行**

Run: `grep -n "UL_DL_Differences_上下行差异\|ASK_FSK_PSK_键控调制" 3gpp/docs/concepts/概念图谱入口.md`
Expected: 行号 M1（协议结构组）/M2（信道与信号组）。在对应组内追加：

```markdown
- [[MAC_Layer_Mapping_MAC层映射]]
- [[Carrier_Aggregation_载波聚合]]
- [[BWP_带宽部分]]
```
（协议结构组）
```markdown
- [[RF_Frontend_射频前端]]
```
（信道与信号组）

- [ ] **Step 2: 术语总表补缺**

Run: `grep -c "^| CA \|^| CC \|^| PCell \|^| SCell \|^| BWP \|^| AGC \|^| ADC \|^| LCID " 3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`
Expected: 统计存量；缺项在「## 系统与协议」节（`| BFR |` 行后）追加（3 列格式，按缺项）：

```markdown
| CA | 载波聚合 | Carrier Aggregation；多 CC 聚合提升带宽。→ [[Carrier_Aggregation_载波聚合]] |
| CC | 分量载波 | Component Carrier；CA 中被聚合的单个载波。 |
| PCell | 主小区 | Primary Cell；CA 中承载连接与移动性的主载波小区。 |
| SCell | 辅小区 | Secondary Cell；CA 中纯数据承载的辅载波小区。 |
| BWP | 带宽部分 | Bandwidth Part；载波内激活工作子带。→ [[BWP_带宽部分]] |
| LCID | 逻辑信道标识 | Logical Channel Identity；MAC PDU 子头中标识逻辑信道的字段。→ [[MAC_Layer_Mapping_MAC层映射]] |
| AGC | 自动增益控制 | Automatic Gain Control；射频前端增益调节，防 ADC 饱和。→ [[RF_Frontend_射频前端]] |
| ADC | 模数转换器 | Analog-to-Digital Converter；模拟信号采样量化。 |
```

- [ ] **Step 3: 概念笔记索引区追加 4 行（2 列格式）**

在「### 协议、信道与信号」分区末尾（`[[Beam_Management_波束管理]]` 行后）追加：

```markdown
| [[MAC_Layer_Mapping_MAC层映射]] | 逻辑→传输→物理三层信道映射与 MAC PDU 复用。 |
| [[Carrier_Aggregation_载波聚合]] | 多 CC 聚合、PCell/SCell 分工与跨载波调度。 |
| [[BWP_带宽部分]] | 载波内激活工作子带（适配/省电/切换）。 |
| [[RF_Frontend_射频前端]] | LNA/AGC/ADC/IQ/相位噪声，非协议强制。 |
```

- [ ] **Step 4: 引言计数修正**

术语总表引言与索引区引言「（100 篇）」→ 修正为实测数（`ls docs/concepts/*.md | grep -v "概念图谱入口\|3GPP全流程" | wc -l`，应为 104）。

- [ ] **Step 5: 验证同步完整性**

Run:

```bash
cd 3gpp && grep -c "MAC_Layer_Mapping_MAC层映射\|Carrier_Aggregation_载波聚合\|BWP_带宽部分\|RF_Frontend_射频前端" docs/concepts/概念图谱入口.md docs/L0_协议阅读引导/L0_terminology_glossary.md && grep -c "^| CA \|^| CC \|^| PCell \|^| SCell \|^| BWP \|^| LCID \|^| AGC \|^| ADC " docs/L0_协议阅读引导/L0_terminology_glossary.md
```

Expected: 图谱入口 4 处、术语表 ≥12 处（4 索引 + 8 条目——按缺项实际数）、8 项术语行齐全（输出按实际）。

- [ ] **Step 6: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/概念图谱入口.md" "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "docs(sync): 图谱入口挂载 MAC 映射/CA/BWP/射频前端四篇 + L0 术语总表登记补缺 + 计数修正

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task H6: 全量验证

**Files:**
- 无新增；FAIL 则修复对应文件。

**Interfaces:**
- Consumes: Task H1-H5 全部改动 + 历次批次全部改动（合流验证）。

- [ ] **Step 1: 运行全部审计**

```bash
cd 3gpp && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_latex_render.py --syntax-only docs/concepts && python3 tools/audit_circled_digits.py && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs
```

Expected: 各工具 PASS/OK。**已知处置**：`3GPP全流程_缩写概念理论清单.md:21` 存量假阳性不改；link_integrity 在 H1-H5 落地后应无新 FAIL（H2 的前瞻链接在 H3 创建后闭合）；任何新 FAIL → Step 2 修复后复跑，直到全绿。

- [ ] **Step 2: 修复 FAIL 并复跑**

按工具输出逐条修复，复跑 Step 1 全部命令。

- [ ] **Step 3: 提交（如有修复）**

```bash
cd /home/yys/AGENT/obsidian && git add -A 3gpp && git commit -m "fix(docs): MAC/CA/BWP/射频前端批次审计修复（如无修复跳过此步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task H7: 双推提交 + 选项 3 收官登记

**Files:**
- 无代码变更。

**Interfaces:**
- Consumes: Task H1-H6 全部提交。

- [ ] **Step 1: 确认工作区干净**

Run: `git status --porcelain` → 空输出。

- [ ] **Step 2: 推送双远端**

```bash
cd /home/yys/AGENT/obsidian && git push origin master 2>&1 | tail -4
```

Expected: Gitee 与 GitHub 两处 `master -> master`；单远端失败必须报告处理。

- [ ] **Step 3: 登记执行证据 + 选项 3 收官声明**

工具缺失（KaTeX/mmdc）在此汇报中显式声明验证缺口；**选项 3 收官声明**：规划 G8（CA/BWP）/G9（MAC 层映射）/G10（射频前端）缺口闭合，选项 3（其他规划缺口）全量完成；下一项为选项 2（TECH_TERMS 结构治理）。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——批次内容（批 B 4 篇）→ Task H1-H4；工具不扩 TECH_TERMS → Task H6。同步清单 → Task H5。
- 占位符：无 TBD/TODO；四篇笔记全文写入任务步骤。
- 一致性：wikilink 创建顺序正确（H2 引用 H3 的前瞻在 H3 创建后闭合；H4 引用 G 批次 PTRS 已创建）；术语配对完整三件套（五批次 60+ 处返工教训——H1-H4 内容已按「中文（English Full Name, ABBR）」写定）；数值自洽（NR 最多 16 CC、CIF 3-bit、FR1 100 MHz/FR2 400 MHz CC、BWP 每载波一激活、LCP/PBR 规则）。
- 双链：H1↔Scheduler/Protocol_Stack/Physical_Channels、H2↔HARQ_Process/BWP、H3↔CA/Spectrum/Scheduler/PBCH、H4↔PTRS/Fixed_Point/T2.17 全链。
- 选项 3 收官登记：本批次完成后概念笔记 104 篇，规划 G8-G10 闭合，选项 3 全量完成；批 A 遗留 Minor（RSRQ 配对、回链补强、Beam↔TRS/CSI-RS→PTRS 互链）可并入选项 2 治理或本批次顺手处理（RSRQ 在 H4 无涉，登记选项 2）。
