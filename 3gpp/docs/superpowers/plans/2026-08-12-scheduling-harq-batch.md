# 调度与 HARQ 进程概念笔记批次 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 1 剩余批次（G3 调度与 HARQ 进程）：4 篇概念笔记（Scheduler / Grant / HARQ_Process / Link_Adaptation）+ 同步清单 + 全量验证 + 双推。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-scheduling-harq-batch.md` 执行。变更文件：新建概念笔记 4 个、修改图谱入口/术语表 2 个。每个任务「内容 → 验证 → 提交」闭环。

**Tech Stack:** Markdown + LaTeX（--syntax-only）+ 项目 audit 工具链。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- 标题正式化（Rule 16）；带圈数字禁令（第 10 条）；英文术语首现**完整三件套**「中文（English Full Name, ABBR）」（Rule 10——控制面批次 15+ 处返工教训，本计划内容已按此写定，逐字转写即可；**发现裸用不要擅改，在 concerns 报告**）。
- 概念笔记六段式模板（独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联，末行「关系语义：…」）。
- wikilink 只指向已存在或本计划内将创建的目标；创建顺序：Scheduler（D1）→ Grant（D2，引用 Scheduler）；HARQ_Process（D3）/Link_Adaptation（D4）独立。
- 协议溯源精确到 TS 编号 + 章节号 + 本地 processed 路径；数值事实以本地 spec 为准（进程数 LTE 8/NR 16 可配、k0/k1/k2、BLER 10%、4-bit CQI、RBG 尺寸表实施时核验）。
- 工具缺失（KaTeX/mmdc）显式声明验证缺口。
- 提交后 `git push origin master`（双推，收尾任务统一执行）。

---

### Task D1: 新建概念笔记 `docs/concepts/Scheduler_MAC调度器与资源分配.md`

**Files:**
- Create: `3gpp/docs/concepts/Scheduler_MAC调度器与资源分配.md`

**Interfaces:**
- Produces: 该文件，Task D2（Grant）引用；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - MAC 调度器
  - 调度器
  - Scheduler
  - 资源分配
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.214 Rel-19 §5.1/§6.1.2; TS 38.321 Rel-19 §5.4/§6.1"
---

# Scheduler MAC 调度器与资源分配

调度器（Scheduler）是 MAC 层每时隙（slot）都要做一次的核心决策单元：决定哪个用户（UE，用户设备，User Equipment）在哪个时频资源上、用多大 MCS（调制与编码方案，Modulation and Coding Scheme）、发多少数据。它把「信道质量（CQI）、业务优先级、QoS 需求、缓冲区状态」综合成资源分配（Resource Allocation）指令，经 DCI（下行控制信息，Downlink Control Information）下发。调度是「从协议到物理资源」的决策层——不理解调度器，就无法理解 DCI 资源字段为什么长那样、descriptor（T9.0）从哪来。

## 独立解释任务

任务目标：讲清调度器在 MAC 层的角色与决策输入、资源分配的单位体系（RBG/VRB 与 PRB 的关系）、NR 资源分配类型（Type 0/1）、频域与时域调度的权衡，以及逻辑信道优先级（LCP）在 MAC 复用中的作用。

## 科学定义

### 调度器角色与决策输入

调度器在 MAC 层、每个 slot 运行一次，输入四类信息：(1) 信道质量——每个 UE 上报的 CQI（信道质量指示，Channel Quality Indicator）/PMI/RI（见 [[Link_Adaptation_链路自适应与CQI]]）；(2) 缓冲区状态——UE 通过 BSR（缓冲区状态报告，Buffer Status Report）告知上行数据量；(3) QoS 需求——逻辑信道的优先级与时延预算；(4) 可用资源——RB（资源块，Resource Block）总数与干扰情况。输出：资源分配 + MCS 选择 + HARQ 进程分配（见 [[HARQ_Process_HARQ进程管理]]）。

### 资源分配的单位体系：RBG 与 VRB

- **PRB（物理资源块，Physical Resource Block）**：网格上的实际频域单位（12 子载波，见 [[Spectrum_and_Frequency_Point_频谱与频点]] 与 T2.3）。
- **RBG（资源块组，Resource Block Group）**：频域分配的最小粒度——一组 PRB（尺寸 P 由 BWP 带宽查表，TS 38.214 §6.1.2.2），位图分配时每 bit 对应一个 RBG。
- **VRB（虚拟资源块，Virtual Resource Block）**：调度器分配的「虚拟编号」，经交织映射到物理 PRB——交织（interleaved VRB 映射，TS 38.214 §6.1.2.3）把连续的虚拟编号打散到不同 PRB，获得频率分集。

### 资源分配类型（NR，TS 38.214 §5.1.2）

| 类型 | 机制 | 使用 |
|:---|:---|:---|
| Type 0 | 位图逐 RBG 指示（每 bit 一个 RBG 是否分配） | DCI 1_1/0_1（非回退） |
| Type 1 | RIV（资源指示值，Resource Indication Value）编码「起始 RB + 长度」 | DCI 1_1/0_1；DCI 1_0/0_0（回退） |
| 动态切换 | 由 DCI 的 frequency domain resource assignment 字段最高位指示 Type 0/1 | 高层配置后动态选择 |

### 频域与时域调度

- 频域调度：把信道质量好的 RB 分给相应 UE（频率选择性调度）——PF（比例公平，Proportional Fair）调度器在「吞吐最大化」与「用户公平」间折中：$P_{i,k}$ 分数 = 瞬时速率/平均速率，取分最高的配对。
- 时域调度：NR 支持 slot 级调度与 mini-slot（1-13 符号）低时延调度；DCI 的时域资源分配字段（TDRA，时域资源分配，Time Domain Resource Allocation）从高层配置表索引出起始符号+长度。

### 逻辑信道优先级（LCP）与 MAC 复用

一个 UE 的上行数据可能来自多个逻辑信道（数据/信令），MAC 复用器按 LCP（逻辑信道优先级，Logical Channel Prioritization）规则组装 MAC PDU：先装高优先级逻辑信道，受优先级比特率（PBR，Prioritized Bit Rate）约束——保证控制信令不被大流量数据饿死。

## 直观模型

调度器像餐厅经理：每桌（UE）报「今天胃口（CQI）、想吃什么（BSR）、几点的预约（QoS）」；经理在餐桌布局（资源网格）上排座（分配 RBG），大桌（低码率）坐宽位置，熟客（高优先级）优先——每桌的「点菜单」（DCI）就是调度结果。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 调度器在物理层 | 调度器在 MAC 层，PHY 只负责执行 DCI 指定的参数 |
| VRB 就是 PRB | VRB 是虚拟分配单位，经交织映射到 PRB——两者编号不同 |
| Type 0 一定优于 Type 1 | Type 0 位图灵活但 DCI 开销大、粒度粗（RBG）；Type 1 紧凑（RIV）——按场景选 |
| 调度只看信道质量 | 还看 QoS 优先级、公平性、缓冲区状态、功率约束——多目标优化 |

## 协议锚点

- 资源分配类型：TS 38.214（Rel-19 j30）§5.1.2，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- RBG 尺寸与 VRB 交织：TS 38.214 §6.1.2.2/§6.1.2.3，本地同卷。
- 调度与优先级处理：TS 38.321（Rel-19 j20）§5.4/§6.1，本地 `TS_38.321_38321-j20`。
- descriptor 衔接：T9.0（`docs/L2_协议算法/T9.0_TS38214_MCS_TBS_decoder_descriptor.md`）。
- 与 MCS/TBS 关系：[[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]。

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[HARQ_Process_HARQ进程管理]]
- [[Link_Adaptation_链路自适应与CQI]]
- 关系语义：调度器是控制面与数据面的汇合点——它消费 CQI（链路自适应）产出 DCI（PDCCH 盲检的对象），决定 HARQ 进程与 RV（进程管理），最终生成译码器 descriptor（T9.0）的源头。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Scheduler_MAC调度器与资源分配.md" && grep -c "^## " "docs/concepts/Scheduler_MAC调度器与资源分配.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Scheduler_MAC调度器与资源分配.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Link_Adaptation_链路自适应与CQI]]`/`[[HARQ_Process_HARQ进程管理]]` 指向 D3/D4 将创建的笔记（计划内前瞻引用，不检查存在性）；`[[DCI_下行控制信息]]`/`[[PDCCH_物理下行控制信道]]`（控制面批次已创建，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Scheduler_MAC调度器与资源分配.md" && git commit -m "docs(concepts): 新增 Scheduler MAC 调度器与资源分配概念笔记（RBG/VRB/Type 0-1/LCP）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task D2: 新建概念笔记 `docs/concepts/Scheduling_Grant_调度与授权.md`

**Files:**
- Create: `3gpp/docs/concepts/Scheduling_Grant_调度与授权.md`

**Interfaces:**
- Consumes: Task D1 的 Scheduler 笔记（wikilink 引用）。
- Produces: 该文件；挂在概念图谱入口「协议结构」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 调度授权
  - Grant
  - UL grant
  - DL assignment
  - 半静态调度 SPS
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.214 Rel-19 §5.1/§6.1; TS 38.321 Rel-19 §5.4"
---

# Scheduling Grant 调度与授权

调度授权（Scheduling Grant）是调度器决策的「送达方式」：基站把「这次给你多少资源、怎么收/发」写进 DCI（下行控制信息，Downlink Control Information）——下行叫 DL assignment（下行调度分配），上行叫 UL grant（上行授权）。授权有动态与半静态两种形态：动态授权每个时隙（slot）由 DCI 逐次下发；半静态（SPS/configured grant）一次配置、周期复用，省去重复信令。Grant 是 [[Scheduler_MAC调度器与资源分配]] 的输出、[[PDCCH_物理下行控制信道]] 盲检的收获、[[DCI_下行控制信息]] 字段的用途落地。

## 独立解释任务

任务目标：讲清动态授权与半静态授权（SPS/configured grant）的机制与区别、DL assignment 与 UL grant 的处理差异、DCI 资源分配字段如何解析成实际资源，以及免授权（grant-free）在低时延场景的定位。

## 科学定义

### 动态调度与授权流程

1. 调度器决策（见 [[Scheduler_MAC调度器与资源分配]]）→ 生成 DCI（0_x 上行/1_x 下行，见 [[DCI_下行控制信息]]）→ PDCCH 盲检下发。
2. UE 在搜索空间盲检到 DCI（RNTI 匹配）→ 解析资源分配字段（频域/时域/MCS/HARQ 进程号/NDI/RV/TPC）→ 按字段在对应 slot 收（DL assignment 指示 PDSCH）或发（UL grant 指示 PUSCH）。
3. 时序由 DCI 时域字段的 k0（PDSCH 相对 PDCCH 的 slot 偏移）/k1（HARQ-ACK 相对 PDSCH 的 slot 偏移）/k2（PUSCH 相对 PDCCH 的 slot 偏移）决定（见 [[HARQ_Process_HARQ进程管理]]）。

### 半静态授权：SPS 与 configured grant

| 机制 | 下行 | 上行 | 配置方式 |
|:---|:---|:---|:---|
| SPS（半静态调度，Semi-Persistent Scheduling） | PDSCH 周期资源 | — | RRC 配置周期 + DCI 激活/释放 |
| configured grant Type 1 | — | PUSCH 周期资源 | RRC 配置全部参数（周期/时频/MCS），无需 DCI |
| configured grant Type 2 | — | PUSCH 周期资源 | RRC 配置半参 + DCI 激活 |

用途：VoIP 周期小包、URLLC 低时延——省去每包一次 PDCCH 盲检与 DCI 开销。激活/释放都经 DCI（CS-RNTI 加扰）确认。

### 免授权（grant-free）与多用户调度

- 免授权：configured grant 的扩展——UE 按配置直接发，无需等 grant（URLLC 时延关键场景）；冲突时靠 HARQ 重传与免授权资源池管理。
- MU-MIMO（多用户 MIMO，Multi-User MIMO）配对：调度器把同一 RB 分给多个 UE 的不同层（依赖 PMI/RI，见 [[Link_Adaptation_链路自适应与CQI]]）——一个 DCI 只对一个 UE，但一个 RB 可承载多个 UE 的层。

## 直观模型

Grant 像「工作单」：动态授权是「每单派一次」（经理每次打电话交代）；SPS/configured grant 是「签订长期合同」（一次签约，周期执行，取消时发通知）；免授权是「自由职业」（不用等单，但可能撞单）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| UL grant 是给下行的 | UL grant（0_x DCI）调度上行 PUSCH，DL assignment（1_x）调度下行 PDSCH |
| SPS 已过时 | SPS/configured grant 仍是 VoIP/URLLC 的主流省信令机制 |
| 授权一定是动态的 | 半静态授权周期复用，激活/释放经 DCI；免授权连 DCI 都不需要 |
| 一个 RB 同时只给一个 UE | MU-MIMO 下同一 RB 可多 UE 多层（PMI/RI 决定） |

## 协议锚点

- 资源分配与 grant：TS 38.214（Rel-19 j30）§5.1/§6.1，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- configured grant：TS 38.321（Rel-19 j20）§5.4，本地 `TS_38.321_38321-j20`。
- SPS 配置：TS 38.331（Rel-19 j20）§6.3.2（SPS-Config/ConfiguredGrantConfig），本地 `TS_38.331_38331-j20`。
- DCI 字段解析：[[DCI_下行控制信息]]（`docs/concepts/DCI_下行控制信息.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[HARQ_Process_HARQ进程管理]]
- 关系语义：Grant 是调度链路的中枢——调度器产出决策（Scheduler）、DCI 承载字段（DCI）、PDCCH 盲检送达（PDCCH）、HARQ 进程与 k 时序执行（HARQ_Process）、UE 侧按 grant 收发的数据流进入译码链路（T9.0）。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Scheduling_Grant_调度与授权.md" && grep -c "^## " "docs/concepts/Scheduling_Grant_调度与授权.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Scheduling_Grant_调度与授权.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Scheduler_MAC调度器与资源分配]]`（D1 已创建，存在）、`[[HARQ_Process_HARQ进程管理]]`/`[[Link_Adaptation_链路自适应与CQI]]`（D3/D4 前瞻）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Scheduling_Grant_调度与授权.md" && git commit -m "docs(concepts): 新增 Scheduling Grant 调度与授权概念笔记（动态/SPS/configured grant）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task D3: 新建概念笔记 `docs/concepts/HARQ_Process_HARQ进程管理.md`

**Files:**
- Create: `3gpp/docs/concepts/HARQ_Process_HARQ进程管理.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「HARQ 与速率匹配」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - HARQ 进程
  - 进程管理
  - HARQ Process
  - NDI
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.321 Rel-19 §5.3; TS 38.214 Rel-19 §5.1"
---

# HARQ Process HARQ 进程管理

HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）进程管理解决「重传怎么组织」：每次传输属于哪个进程、是新传还是重传、软缓存写哪个地址、何时反馈——这些语义由 DCI（下行控制信息，Downlink Control Information）里的 HARQ 进程号与 NDI（新数据指示，New Data Indicator）字段驱动。它是软合并（T4.3/T7.3/T9.3）的调度侧伴侣：没有进程管理，软缓存就不知道把 LLR 累加到哪。

## 独立解释任务

任务目标：讲清 HARQ 进程的编号与状态机、进程数（LTE/NR 差异）、NDI 翻转语义、k0/k1/k2 时序链，以及同步/异步 HARQ 的区别，并衔接软合并与软缓存（T7.3/T9.3/T9.7）。

## 科学定义

### HARQ 进程：状态机与编号

一个 HARQ 进程跟踪一条「传输-反馈-重传」链：进程处于空（idle）或进行中（占用，等待 ACK/NACK 或已调度重传）。DCI 的 HARQ process number 字段（3-4 bit）指示本次传输用哪个进程；同一进程的重传与初传共享软缓存地址（LLR 证据相加，见 [[Chase_Combining_Chase合并]]/[[Incremental_Redundancy_增量冗余]]）。

### 进程数（LTE vs NR）

| 制式 | DL 进程数 | UL 进程数 | 时序 |
|:---|:---|:---|:---|
| LTE | 8（固定） | 8（FDD）/更多（TDD） | 同步 HARQ（固定时序） |
| NR | 2-16（高层配置，常见 16） | 2-16 | 异步 HARQ（灵活时序） |

同步 HARQ：重传在固定时间（如 8 ms 后）发生，进程号可由时间推导；异步 HARQ：重传时间由调度器自由安排，进程号必须显式携带——NR 用异步换调度灵活性。

### NDI 翻转语义

NDI（新数据指示，New Data Indicator）是 DCI 里 1 bit：与**同一进程**上次传输相比，NDI 翻转（0→1 或 1→0）= 新传（清空软缓存、覆盖写）；NDI 不翻转 = 重传（增量写、LLR 相加，见 T9.7）。**关键**：NDI 必须与 HARQ 进程号联合看——不同进程的 NDI 无比较意义。

### k0/k1/k2 时序链

DCI 时域资源分配字段（TDRA，时域资源分配，Time Domain Resource Allocation）从高层配置表索引出三个偏移（TS 38.214 §5.1.2.1，slot 粒度）：

```
slot n: PDCCH(DCI) ──k0──→ PDSCH (DL assignment)
slot n+k0: PDSCH 接收与译码
slot n+k0+k1: PUCCH HARQ-ACK 上报（k1 在 DCI 中指示，见 [[PUCCH_上行控制信道与UCI]]）
slot n: PDCCH(UL grant) ──k2──→ PUSCH
```

默认值：k0=0、k1=1、k2=0（未配置表时）。

### 重传限制与失败

- maxHARQ-Tx：同一进程最大传输次数（超过后停止重传，数据交上层处理）。
- HARQ 失败 ≠ 数据丢失：RLC（无线链路控制层）层还有 ARQ 重传兜底（见 [[Protocol_Stack_协议栈]] 的层2 结构）。

## 直观模型

HARQ 进程像「快递单号」：每个包裹（TB）一个单号（进程号），「是否换新包裹」看单子上的标记翻转（NDI）——同一个单号（同进程）不翻转就是补发（重传合并），翻转就是新包裹（新传清缓存）。快递员（调度器）可以自由安排补发时间（异步）或固定时间补发（同步）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| NDI 翻转就一定新传 | 必须结合 HARQ 进程号——同进程内比较才有意义 |
| 进程数 = 软缓存数 | 软缓存按进程×TB 分配（T9.3），但进程数是协议概念、软缓存大小是工程概念 |
| NR 也是同步 HARQ | LTE 是同步（固定 8 ms），NR 是异步（调度自由安排，进程号显式携带） |
| HARQ 失败 = 数据丢失 | 层2 的 RLC ARQ 在 HARQ 之上兜底（AM 模式） |

## 协议锚点

- HARQ 实体与进程：TS 38.321（Rel-19 j20）§5.3，本地 `3GPP_Rel19/processed/TS_38.321_38321-j20`。
- k0/k1/k2 时域分配：TS 38.214（Rel-19 j30）§5.1.2.1（PDSCH）/§6.1.2.1（PUSCH），本地 `TS_38.214_38214-j30`。
- HARQ-ACK 时序：TS 38.213（Rel-19 j30）§9.1，本地 `TS_38.213_38213-j30`。
- 软合并语义：[[HARQ_混合自动重传请求]]、T7.3/T9.3（`docs/L2_协议算法/`）、T9.7（CB 增量写）。

## 图谱关联

- [[概念图谱入口]]
- [[HARQ_混合自动重传请求]]
- [[DCI_下行控制信息]]
- [[PUCCH_上行控制信道与UCI]]
- [[Chase_Combining_Chase合并]]
- 关系语义：HARQ 进程管理是软合并的调度侧语义——DCI 的进程号/NDI/RV 决定软缓存地址与读写模式（T9.7 覆盖写 vs 增量写），k1 决定 HARQ-ACK 反馈时序（PUCCH），是下行译码闭环到上行反馈的关键一环。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/HARQ_Process_HARQ进程管理.md" && grep -c "^## " "docs/concepts/HARQ_Process_HARQ进程管理.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/HARQ_Process_HARQ进程管理.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[PUCCH_上行控制信道与UCI]]`/`[[DCI_下行控制信息]]`（控制面批次已创建，存在）；`[[Chase_Combining_Chase合并]]`/`[[Incremental_Redundancy_增量冗余]]`/`[[Protocol_Stack_协议栈]]`（既有，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/HARQ_Process_HARQ进程管理.md" && git commit -m "docs(concepts): 新增 HARQ Process HARQ 进程管理概念笔记（进程状态机/NDI/k 时序）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task D4: 新建概念笔记 `docs/concepts/Link_Adaptation_链路自适应与CQI.md`

**Files:**
- Create: `3gpp/docs/concepts/Link_Adaptation_链路自适应与CQI.md`

**Interfaces:**
- Produces: 该文件；挂在概念图谱入口「信道与接收链路」组；D1（Scheduler）引用它。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 链路自适应
  - Link Adaptation
  - CQI PMI RI
  - 信道状态信息 CSI
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.214 Rel-19 §5.2; TS 38.213 Rel-19 §9; TS 38.331 Rel-19 §6.3.2"
---

# Link Adaptation 链路自适应与CQI

链路自适应（Link Adaptation）让传输速率跟着信道走：UE 测量下行信道（CSI-RS）的 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio），折算成 CQI（信道质量指示，Channel Quality Indicator）上报，基站据此选择 MCS（调制与编码方案，Modulation and Coding Scheme）——信道好就传得快、信道差就传得稳。它由 CSI（信道状态信息，Channel State Information）反馈环路驱动，是 [[Scheduler_MAC调度器与资源分配]] 的频率选择性调度与 MCS 选择的上游输入。

## 独立解释任务

任务目标：讲清链路自适应闭环（测量→CQI→MCS→反馈→修正）、CQI/PMI/RI 三件报告的内容与作用、CQI 报告的周期/非周期与宽带/子带类型，以及 outer loop 如何用 ACK/NACK 校准 CQI 误差。

## 科学定义

### 链路自适应闭环

```
UE 测 CSI-RS SINR（T2.11）→ 折算 CQI（满足 BLER≤10% 的最大可支持 MCS）
→ PUCCH/PUSCH 上报（见 [[PUCCH_上行控制信道与UCI]]）
→ gNB 调度器选 MCS/资源（[[Scheduler_MAC调度器与资源分配]]）
→ 传输 → UE 译码（BLER 目标验证）→ ACK/NACK
→ outer loop：连续 NACK 下调 SINR 折算偏置、连续 ACK 上调（校准 CQI 误差）
```

### CQI/PMI/RI 三件报告

| 报告 | 内容 | 作用 |
|:---|:---|:---|
| CQI（信道质量指示，Channel Quality Indicator） | 4-bit 索引（0-15），每值对应一个调制阶数+码率组合 | 决定 MCS 选择 |
| PMI（预编码矩阵指示，Precoding Matrix Indicator） | 码本索引，指示期望的预编码矩阵 | 波束/层成形（与 [[Precoding_预编码]] 衔接） |
| RI（秩指示，Rank Indicator） | 建议的传输层数 | 决定 MIMO 层数与码率换算 |

三件合称 CSI；CQI 按 RI 假设折算（层数不同码率口径不同）。CQI 表定义在 TS 38.214 §5.2.2.1（4-bit 表与 5-bit 表）。

### CQI 报告类型

| 维度 | 类型 | 承载 |
|:---|:---|:---|
| 触发 | 周期（RRC 配置周期）/ 非周期（DCI 触发） | 周期走 PUCCH，非周期走 PUSCH（容量大） |
| 频域粒度 | 宽带（一个 CQI 覆盖全带宽）/ 子带（每子带一个 CQI） | 宽带省开销、子带支持频率选择性调度 |

### 为什么需要 outer loop

CQI 是 UE 的「预测」——测量误差、信道变化、干扰波动都会让它偏乐观/悲观。outer loop 用真实传输结果（ACK/NACK）修正：NACK 说明 CQI 偏乐观（降低折算 SINR 偏置），连续 ACK 说明偏悲观（上调）——把实际 BLER 拉回目标值（10%）。它是闭环的自校准层。

## 直观模型

链路自适应像「自助餐配菜」：顾客（UE）先报「我胃口怎么样」（CQI 报 SINR 折算），厨师（调度器）按胃口配菜量（MCS）；吃完反馈「咸淡」（ACK/NACK），厨师调盐（outer loop 修正）——下一次配菜更准。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CQI 越高越好 | CQI 反映可支持的 MCS 上限，调度器还要结合资源/QoS 选实际 MCS |
| CQI 就是 SINR | CQI 是 SINR 按 BLER 目标折算后的索引——同样的 SINR 可对应不同 CQI（不同 BLER 目标） |
| PMI/RI 只影响下行 | 上行也用 SRS 与 PMI/RI 相关反馈（TDD 互易性/码本） |
| 一次上报就够了 | CQI 会过时，周期/非周期上报持续跟踪信道变化 |

## 协议锚点

- CSI 报告配置与 CQI 表：TS 38.214（Rel-19 j30）§5.2，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- PUCCH/PUSCH 承载 CSI：TS 38.213（Rel-19 j30）§9.2，本地 `TS_38.213_38213-j30`。
- CSI 配置参数：TS 38.331（Rel-19 j20）§6.3.2（CSI-ReportConfig），本地 `TS_38.331_38331-j20`。
- 测量侧衔接：T2.11（CSI/SINR，`docs/L1_基础/`）、[[CSI_SINR]]。

## 图谱关联

- [[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[CSI_SINR]]
- [[PUCCH_上行控制信道与UCI]]
- 关系语义：链路自适应把「信道质量」变成「传输参数」——CSI 测量（T2.11）→ CQI/PMI/RI 上报（PUCCH/PUSCH）→ 调度器选 MCS（MCS 表）→ 传输；outer loop 用 HARQ 反馈（ACK/NACK）校准，是物理层与 MAC 层耦合最紧的闭环。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Link_Adaptation_链路自适应与CQI.md" && grep -c "^## " "docs/concepts/Link_Adaptation_链路自适应与CQI.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Link_Adaptation_链路自适应与CQI.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Scheduler_MAC调度器与资源分配]]`（D1 已创建）、`[[CSI_SINR]]`/`[[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]`/`[[Precoding_预编码]]`（既有，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Link_Adaptation_链路自适应与CQI.md" && git commit -m "docs(concepts): 新增 Link Adaptation 链路自适应与CQI 概念笔记（闭环/CQI/PMI/RI/outer loop）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task D5: 同步清单（图谱入口 4 行 + L0 术语总表 8 项 + 索引 4 行 + 计数修正）

**Files:**
- Modify: `3gpp/docs/concepts/概念图谱入口.md`（「协议结构」组 2 行 + 「HARQ 与速率匹配」组 1 行 + 「信道与接收链路」组 1 行）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（「系统与协议」节 8 项 + 索引 4 行 + 引言计数）

**Interfaces:**
- Consumes: Task D1-D4 四个笔记名。
- Produces: 术语总表 8 项 + 挂载 4 行 + 索引 4 行。

- [ ] **Step 1: 图谱入口挂载 4 行**

Run: `grep -n "MCS_Table_Effective_Code_Rate\|Rate_Matching_速率匹配\|Diversity_Combining_分集与合并" 3gpp/docs/concepts/概念图谱入口.md`
Expected: 行号 M1（协议结构组）/M2（HARQ 组）/M3（信道与接收链路组）。在对应组内追加：

```markdown
- [[Scheduler_MAC调度器与资源分配]]
- [[Scheduling_Grant_调度与授权]]
```
（协议结构组 MCS 行后）
```markdown
- [[HARQ_Process_HARQ进程管理]]
```
（HARQ 组 Rate_Matching 行后）
```markdown
- [[Link_Adaptation_链路自适应与CQI]]
```
（信道与接收链路组 Diversity_Combining 行后）

- [ ] **Step 2: 术语总表新增 8 项**

在「## 系统与协议」节（`| TBCC |` 行后）追加：

```markdown
| 调度器 | 调度器 | Scheduler；MAC 层每 slot 决策用户/资源/MCS 的单元。→ [[Scheduler_MAC调度器与资源分配]] |
| RBG | 资源块组 | Resource Block Group；频域分配最小粒度，位图分配单位。 |
| VRB | 虚拟资源块 | Virtual Resource Block；调度分配单位，经交织映射到 PRB。 |
| CQI | 信道质量指示 | Channel Quality Indicator；4-bit 索引映射 MCS/码率，BLER 目标约束。→ [[Link_Adaptation_链路自适应与CQI]] |
| PMI | 预编码矩阵指示 | Precoding Matrix Indicator；期望预编码矩阵的码本索引。 |
| RI | 秩指示 | Rank Indicator；建议的传输层数。 |
| NDI | 新数据指示 | New Data Indicator；同进程内翻转=新传、不翻转=重传。→ [[HARQ_Process_HARQ进程管理]] |
| SPS | 半静态调度 | Semi-Persistent Scheduling；周期资源免逐次 DCI 的调度机制。 |
```

- [ ] **Step 3: 概念笔记索引区追加 4 行（2 列格式）**

在「### 协议、信道与信号」分区末尾（`[[PUCCH_上行控制信道与UCI]]` 行后）追加：

```markdown
| [[Scheduler_MAC调度器与资源分配]] | MAC 调度器决策与 RBG/VRB/Type 0-1 资源分配。 |
| [[Scheduling_Grant_调度与授权]] | 动态授权与 SPS/configured grant 机制。 |
| [[HARQ_Process_HARQ进程管理]] | HARQ 进程状态机、NDI 翻转与 k0/k1/k2 时序。 |
| [[Link_Adaptation_链路自适应与CQI]] | CQI/PMI/RI 反馈闭环与 outer loop 校准。 |
```

- [ ] **Step 4: 引言计数修正**

术语总表引言与索引区引言「（83 篇）」→ 修正为实测数（`ls docs/concepts/*.md | grep -v "概念图谱入口\|3GPP全流程" | wc -l`，应为 87）。

- [ ] **Step 5: 验证同步完整性**

Run:

```bash
cd 3gpp && grep -c "Scheduler_MAC调度器与资源分配\|Scheduling_Grant_调度与授权\|HARQ_Process_HARQ进程管理\|Link_Adaptation_链路自适应与CQI" docs/concepts/概念图谱入口.md docs/L0_协议阅读引导/L0_terminology_glossary.md && grep -c "^| 调度器 \|^| RBG \|^| VRB \|^| CQI \|^| PMI \|^| RI \|^| NDI \|^| SPS " docs/L0_协议阅读引导/L0_terminology_glossary.md
```

Expected: 图谱入口 4 处、术语表 ≥8 处（4 索引 + 4 条目含链接）、8 项术语行齐全（输出 `8`）。

- [ ] **Step 6: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/概念图谱入口.md" "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "docs(sync): 图谱入口挂载调度四篇 + L0 术语总表登记 8 项（调度器/RBG/VRB/CQI/PMI/RI/NDI/SPS）+ 计数修正

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task D6: 全量验证

**Files:**
- 无新增；FAIL 则修复对应文件。

**Interfaces:**
- Consumes: Task D1-D5 全部改动 + 控制面批次全部改动（合流验证）。

- [ ] **Step 1: 运行全部审计**

```bash
cd 3gpp && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_latex_render.py --syntax-only docs/concepts && python3 tools/audit_circled_digits.py && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs
```

Expected: 各工具 PASS/OK。**已知处置**：`3GPP全流程_缩写概念理论清单.md:21` 存量假阳性不改；link_integrity 在 D1-D5 落地后应无新 FAIL（D1/D2 的前瞻链接在 D3/D4 创建后闭合）；任何新 FAIL → Step 2 修复后复跑，直到全绿。

- [ ] **Step 2: 修复 FAIL 并复跑**

按工具输出逐条修复，复跑 Step 1 全部命令。

- [ ] **Step 3: 提交（如有修复）**

```bash
cd /home/yys/AGENT/obsidian && git add -A 3gpp && git commit -m "fix(docs): 调度批次审计修复（如无修复跳过此步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task D7: 双推提交

**Files:**
- 无代码变更。

**Interfaces:**
- Consumes: Task D1-D6 全部提交。

- [ ] **Step 1: 确认工作区干净**

Run: `git status --porcelain` → 空输出。

- [ ] **Step 2: 推送双远端**

```bash
cd /home/yys/AGENT/obsidian && git push origin master 2>&1 | tail -4
```

Expected: Gitee 与 GitHub 两处 `master -> master`；单远端失败必须报告处理。

- [ ] **Step 3: 登记执行证据**

工具缺失（KaTeX/mmdc）在此汇报中显式声明验证缺口；登记 NDI/RI/CQI/PMI/RBG/VRB TECH_TERMS 全库治理（合并 PDCCH/PUCCH/PBCH）为阶段 2 前置任务。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——批次内容（G3 调度 4 篇）→ Task D1-D4；工具不扩 TECH_TERMS → Task D6（验证不含工具修改）。同步清单 → Task D5。
- 占位符：无 TBD/TODO；四篇笔记全文写入任务步骤。
- 一致性：wikilink 创建顺序正确（D1 Scheduler 先建，D2 Grant 引用；D3/D4 独立；D1 引用 D3/D4 的前瞻在 D3/D4 创建后闭合）；术语配对完整三件套（控制面批次 15+ 处返工教训——D1-D4 内容已按「中文（English Full Name, ABBR）」写定）；数值自洽（LTE 8/NR 2-16 进程、k0=0/k1=1/k2=0、BLER 10%、4-bit CQI 0-15、RBG 尺寸查表）。
- 双链：Scheduler↔Grant（D1/D2 互链）、Scheduler↔Link_Adaptation（D1/D4 互链）、HARQ_Process↔DCI/PUCCH（D3 引用控制面批次已建目标）、Link_Adaptation↔Scheduler/MCS_Table/CSI_SINR/PUCCH 全链。
- 阶段 2 前置登记：NDI（39 篇）/RI（26 篇）/CQI/PMI/RBG/VRB TECH_TERMS 全库治理（与 PDCCH/PUCCH/PBCH 合并）。

