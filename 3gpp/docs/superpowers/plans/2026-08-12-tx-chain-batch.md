# 发送端镜像概念笔记批次 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 1 最后批次（G2 发送端镜像）：3 篇概念笔记（Modulation_Mapping / RE_Mapping / TX_Chain）+ 同步清单 + 全量验证 + 双推。完成后阶段 1 收官。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-tx-chain-batch.md` 执行。变更文件：新建概念笔记 3 个、修改图谱入口/术语表 2 个。每个任务「内容 → 验证 → 提交」闭环。

**Tech Stack:** Markdown + LaTeX（--syntax-only）+ 项目 audit 工具链。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- 标题正式化（Rule 16）；带圈数字禁令（第 10 条）；英文术语首现**完整三件套**「中文（English Full Name, ABBR）」（Rule 10——三批次 40+ 处返工教训，本计划内容已按此写定，逐字转写即可；**发现裸用不要擅改，在 concerns 报告**）。
- 概念笔记六段式模板（独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联，末行「关系语义：…」）。
- wikilink 只指向已存在或本计划内将创建的目标；创建顺序：F1/F2（独立）→ F3（引用批内全部）。
- 协议溯源精确到 TS 编号 + 章节号 + 本地 processed 路径；星座表归一化因子/RE 映射规则实施时核验本地 j30。
- 工具缺失（KaTeX/mmdc）显式声明验证缺口。
- 提交后 `git push origin master`（双推，收尾任务统一执行）。

---

### Task F1: 新建概念笔记 `docs/concepts/Modulation_Mapping_调制映射.md`

**Files:**
- Create: `3gpp/docs/concepts/Modulation_Mapping_调制映射.md`

**Interfaces:**
- Produces: 该文件，Task F3 引用；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 调制映射
  - Modulation Mapping
  - 星座映射
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §5.1"
---

# Modulation Mapping 调制映射

调制映射（Modulation Mapping）是发送端的比特到符号步骤：把编码后的比特按调制阶数分组，映射成复数调制符号（星座点）。NR 协议（TS 38.211 §5.1）定义了 QPSK（正交相移键控，Quadrature Phase Shift Keying）与 16/64/256QAM（正交幅度调制，Quadrature Amplitude Modulation）的星座表——每个星座点给出归一化的复数值。它是 [[ASK_FSK_PSK_键控调制]] 家族在 NR 协议中的落地，也是软解调（T2.13/T2.14）在发送端的镜像。

## 独立解释任务

任务目标：讲清调制映射的协议定义（星座表结构、比特分组、归一化因子）、各调制阶数的星座几何与能量归一化，以及 Qm（调制阶数，Modulation Order）与 MCS（调制与编码方案，Modulation and Coding Scheme）的关系。

## 科学定义

### 协议结构（TS 38.211 §5.1）

比特流按调制阶数 Qm 分组（QPSK:2、16QAM:4、64QAM:6、256QAM:8 比特/符号），每组映射为一个复数符号 $d = I + jQ$，星座点取值由协议表给出（QPSK 为 Table 5.1-3，16QAM 为 5.1-4、64QAM 为 5.1-5、256QAM 为 5.1-6；表 5.1-1 起还含 π/2-BPSK、BPSK 与 1024QAM）。

### 星座与归一化因子

| 调制 | Qm | 星座点数 | 归一化因子 | 最小点距 |
|:---|:---|:---|:---|:---|
| QPSK | 2 | 4 | $1/\sqrt{2}$ | 2/√2 |
| 16QAM | 4 | 16 | $1/\sqrt{10}$ | 2/√10 |
| 64QAM | 6 | 64 | $1/\sqrt{42}$ | 2/√42 |
| 256QAM | 8 | 256 | $1/\sqrt{170}$ | 2/√170 |

归一化因子让所有调制方式的**平均符号能量为 1**（$E_s = 1$）——这样功率预算与 MCS 无关，星座点距随阶数增大而缩小（256QAM 点距最小、对噪声最敏感——这就是为什么 256QAM 需要高 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio））。

### Qm 与 MCS 的关系

MCS 索引（见 [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]] 与 T9.0）直接给出 Qm 与目标码率 R——调度器选 MCS 即选调制阶数；DCI（下行控制信息，Downlink Control Information）里只有 MCS 索引，Qm 由表查得（[[DCI_下行控制信息]] 的 descriptor 映射）。

### 与键控调制家族的衔接

QPSK 是 [[ASK_FSK_PSK_键控调制]] 家族 PSK 的 2 bit/符号形态；16QAM 及以上是「幅度+相位联合键控」——QAM 是 PSK 的推广（家族演进见键控调制笔记）。

## 直观模型

调制映射像「点菜编号」：菜谱（星座表）上每个菜（星座点）有编号（比特组合）和坐标（复数值）；厨师（发送端）按编号出菜（发符号），客人（接收端）按坐标认菜（软解调）——菜谱要统一（协议表），才能对上号。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 星座图是设计自由发挥 | 星座点由协议表逐点规定（TS 38.211 Table 5.1-x），收发必须一致 |
| 256QAM 一定比 QPSK 好 | 256QAM 频谱效率高但点距小、对噪声敏感——高 SINR 场景才用 |
| 归一化因子可省略 | 省略会改变符号能量——功率口径、LLR 缩放全乱（T2.16 衔接） |
| Qm 在 DCI 里直接传 | DCI 只传 MCS 索引，Qm/R 查表得（T9.0） |

## 协议锚点

- 调制映射表：TS 38.211（Rel-19 j30）§5.1（V19.3.0 中为 5.1.x 公式形式，表号对应历史版本编号——Table 5.1-1 起，QPSK 为 Table 5.1-3），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- MCS/Qm 关系：TS 38.214（Rel-19 j30）§5.1.3（MCS 表），本地 `TS_38.214_38214-j30`。
- 软解调镜像：T2.13（BPSK/QPSK）/T2.14（QAM Max-Log-MAP），`docs/L1_基础/`。

## 图谱关联

- [[概念图谱入口]]
- [[ASK_FSK_PSK_键控调制]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[RE_Mapping_资源元素映射]]
- 关系语义：调制映射是发送端物理信道处理的第二环（加扰后）——比特变符号，星座表是收发一致的契约；Qm 由 MCS 决定（调度），符号能量归一化保证功率口径，接收端软解调（T2.13/T2.14）是它的精确镜像。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/Modulation_Mapping_调制映射.md" && grep -c "^## " "docs/concepts/Modulation_Mapping_调制映射.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/Modulation_Mapping_调制映射.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过（归一化因子公式块级/行内）；圈号无新增 FAIL。
注意：wikilink `[[RE_Mapping_资源元素映射]]` 指向 F2（批内将创建——计划内前瞻，F2 后闭合）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/Modulation_Mapping_调制映射.md" && git commit -m "docs(concepts): 新增 Modulation Mapping 调制映射概念笔记（TS 38.211 §5.1 星座表）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task F2: 新建概念笔记 `docs/concepts/RE_Mapping_资源元素映射.md`

**Files:**
- Create: `3gpp/docs/concepts/RE_Mapping_资源元素映射.md`

**Interfaces:**
- Produces: 该文件，Task F3 引用；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 资源元素映射
  - RE 映射
  - Resource Element Mapping
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §6.3.1.6/§7.3.1.5/§7.4.1"
---

# RE Mapping 资源元素映射

资源元素映射（Resource Element Mapping）把调制符号放进时频网格：按规则把符号序列填入 RB（资源块，Resource Block）内的 RE（资源元素，Resource Element，一个子载波×一个符号），同时避让参考信号占用的位置。它把「符号流」变成「网格」，是发送端物理信道处理的倒数第二环（预编码后、OFDM 生成前），也是接收端解映射（LLR 提取）的镜像。

## 独立解释任务

任务目标：讲清 RE 映射的填充规则（先频后时、符号到 (k,l) 的坐标映射）、参考信号避让（DMRS/CSI-RS/PTRS 占位与 rate matching around RS），以及 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）RE 映射的差异。

## 科学定义

### 填充规则

- 网格坐标：RE = (k, l)——k 是子载波索引（频域）、l 是符号索引（时域）；一个 RB 含 12 子载波 × 14 符号（常规 CP，见 [[Spectrum_and_Frequency_Point_频谱与频点]] 与 T2.3）。
- 先频后时：符号序列按「先填满频域（一个符号内所有子载波）、再推进时域」的顺序填入——与接收端解映射顺序一致（T2.6 的 LLR 提取顺序）。
- 分配粒度：PDSCH/PUSCH 按 RB 分配（调度器给的 RB 集，见 [[Scheduler_MAC调度器与资源分配]]），映射只发生在分配的 RB 内。

### 参考信号避让

网格里不是所有 RE 都放数据：DMRS（解调参考信号，Demodulation Reference Signal）/CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）/PTRS（相位跟踪参考信号，Phase Tracking Reference Signal）占用固定位置（TS 38.211 §7.4.1 位置表）——数据符号跳过这些 RE，接收端在译码前把这些位置置为中性 LLR（或按 RS 已知值处理）。这就是 **rate matching around RS**：发送端绕开 RS 打孔，接收端逆过程恢复。

### PDSCH/PUSCH 差异

- 下行 PDSCH：DMRS 占符号 2/3 等固定位置（front-loaded），CSI-RS 按配置插入；映射后经 OFDM 生成（多载波）。
- 上行 PUSCH：DMRS 位置由配置（映射类型 A/B）决定；DFT-s-OFDM 波形下先做变换预编码（DFT）再映射到连续子载波（见 [[DFT_sOFDM_上行波形]]）。

## 直观模型

RE 映射像「考场排座」：座位（RE）按行列（频域×时域）编号，考生（符号）按先排完一行再排下一行的顺序入座（先频后时）；监考老师（参考信号）占固定座位（DMRS/CSI-RS），考生绕开这些座位坐（rate matching around RS）——考完（接收端）按同样规则找回每个人的答卷（LLR）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| RE 映射可以随意排 | 先频后时是协议规定，收发必须一致（顺序错=LLR 错位） |
| 参考信号位置可自由选择 | DMRS/CSI-RS 位置由协议表+配置决定（TS 38.211 §7.4.1） |
| rate matching 是速率匹配的另一种叫法 | rate matching around RS 是「绕开参考信号打孔」，与信道编码的速率匹配（rate matching）是不同概念 |
| 映射在 OFDM 生成后 | 映射在预编码后、OFDM（IFFT）生成前——顺序：符号→层映射→预编码→RE 映射→OFDM |

## 协议锚点

- PDSCH RE 映射：TS 38.211（Rel-19 j30）§7.3.1.5，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- PUSCH RE 映射：TS 38.211 §6.3.1.6，本地同卷。
- 参考信号位置：TS 38.211 §7.4.1（DMRS/CSI-RS/PTRS 位置表），本地同卷。
- 网格坐标基础：T2.3（`docs/L1_基础/T2.3_NR_frequency_resource_grid.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[DMRS_解调参考信号]]
- [[Scheduler_MAC调度器与资源分配]]
- [[Modulation_Mapping_调制映射]]
- 关系语义：RE 映射是符号流到网格的最后一跳——填充规则（先频后时）与参考信号避让（rate matching around RS）决定接收端 LLR 提取顺序（T2.6）；调度器分配的 RB 集是映射范围，调制映射（批内）产出待映射符号。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/RE_Mapping_资源元素映射.md" && grep -c "^## " "docs/concepts/RE_Mapping_资源元素映射.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/RE_Mapping_资源元素映射.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink `[[Modulation_Mapping_调制映射]]`（F1 已创建，存在）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/RE_Mapping_资源元素映射.md" && git commit -m "docs(concepts): 新增 RE Mapping 资源元素映射概念笔记（先频后时/参考信号避让）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task F3: 新建概念笔记 `docs/concepts/TX_Chain_发送端处理链总览.md`

**Files:**
- Create: `3gpp/docs/concepts/TX_Chain_发送端处理链总览.md`

**Interfaces:**
- Consumes: F1/F2 批内两篇 + 既有 Gold_序列加扰/Precoding/Layer_Mapping。
- Produces: 该文件（阶段 1 收官篇）；挂在概念图谱入口「发送链路」组。

- [ ] **Step 1: 写完整概念笔记**

```markdown
---
type: definition
aliases:
  - 发送端处理链
  - 发送链
  - TX Chain
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.212 Rel-19 §5; TS 38.211 Rel-19 §5-§7 综合"
---

# TX Chain 发送端处理链总览

发送端处理链（TX Chain）是数据从 MAC 层到天线的完整加工流水线：传输信道处理（CRC（循环冗余校验，Cyclic Redundancy Check）附着→码块分段→信道编码→速率匹配→码块级联）把 TB（传输块，Transport Block）变成编码比特流；物理信道处理（加扰→调制映射→层映射→预编码→RE 映射→OFDM（正交频分复用，Orthogonal Frequency Division Multiplexing）生成）把比特流变成时域波形。它是整个知识库「接收端译码链路」的镜像——理解发送端每一环，才能理解接收端为什么那样逆着做（T0.1 的「发送端顺序与接收端逆序」）。

## 独立解释任务

任务目标：把发送端全链（传输信道处理 + 物理信道处理）串成一张完整地图，逐环标注与接收端/译码链路（T2.0/T6-T10）的镜像关系，并串联既有发送端笔记（加扰/预编码/层映射）与批内两篇（调制映射/RE 映射）。

## 科学定义

### 传输信道处理（TS 38.212 §5）

```
TB → CRC 附着（TB CRC）→ 码块分段（+CB（码块，Code Block）CRC）→ 信道编码（Turbo/LDPC/Polar）
→ 速率匹配 → 码块级联 → 编码比特流
```

每环的接收端镜像：CRC 校验（T7.4/T9.5）、CB 切分（T3.2-T3.5）、译码（T6/T8/T10）、速率恢复（T7/T9）、LLR（对数似然比，Log-Likelihood Ratio）拼接（T2.6）——发送端编码链的每一环在接收端都有一个逆操作。

### 物理信道处理（TS 38.211 §5-§7）

```
编码比特流 → 加扰（[[Gold_序列加扰]]）→ 调制映射（[[Modulation_Mapping_调制映射]]）
→ 层映射（[[Layer_Mapping_层映射]]）→ 预编码（[[Precoding_预编码]]）
→ RE 映射（[[RE_Mapping_资源元素映射]]）→ OFDM 生成（IFFT+CP）→ 射频
```

接收端镜像：解扰（T2.6 的逆）、软解调 LLR（T2.13/T2.14）、MIMO（多输入多输出，Multiple-Input Multiple-Output）检测（T12/T2.12）、解映射、FFT/同步（T2.7/T2.8）。

### 与接收端译码链路的关系

发送端处理链不是孤立知识——它与 [[Protocol_Stack_协议栈]] 的 L1 层对应、与 T0.1 阅读地图的「发送端规则→接收端逆流程」翻译表对应；调度器（[[Scheduler_MAC调度器与资源分配]]）产出的 descriptor 就是发送端参数的镜像（MCS/Qm/RV 等，见 [[DCI_下行控制信息]]）。

## 直观模型

发送端处理链像「食品加工流水线」：原料（TB）经清洗（CRC）、切块（分段）、腌制（编码）、包装（速率匹配）、贴标（加扰）、造型（调制）、分拣（层映射/预编码）、入盒（RE 映射）、装车（OFDM）——接收端是一条反向流水线，每个环节都有对应的「拆解」工位。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 发送端是接收端的简单倒序 | 逆序但不等价——发送端打孔在接收端是 LLR 置零、重复在接收端是 LLR 累加（T0.1 明示） |
| 加扰是加密 | 加扰（Gold 序列异或）是随机化干扰、不是安全加密（[[Gold_序列加扰]]） |
| 物理信道处理只有比特→符号 | 还有调制映射/层映射/预编码/RE 映射/OFDM——除加扰外的完整五环 |
| 理解译码不需要发送端 | 不理解发送端编码链，就无法解释接收端为什么这样逆着做（T0.1 的翻译表） |

## 协议锚点

- 传输信道处理：TS 38.212（Rel-19 j30）§5（CRC/分段/编码/速率匹配），本地 `3GPP_Rel19/processed/TS_38.212_38212-j30`。
- 物理信道处理：TS 38.211（Rel-19 j30）§5-§7（调制/层映射/预编码/RE 映射/OFDM），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 镜像对照：T0.1（`docs/L0_协议阅读引导/T0.1_LTE_NR_decoder_protocol_reading_map.md`）、T2.0（接收端总览）。

## 图谱关联

- [[概念图谱入口]]
- [[Gold_序列加扰]]
- [[Modulation_Mapping_调制映射]]
- [[Layer_Mapping_层映射]]
- [[Precoding_预编码]]
- [[RE_Mapping_资源元素映射]]
- 关系语义：发送端处理链是全链路的上半身——传输信道处理（编码链）与物理信道处理（波形链）两段共 11 环，每环都有接收端镜像（译码链路/软解调/MIMO 检测），与 T0.1 的「发送端规则→接收端逆流程」翻译表互为表里，至此「发送端→接收端」全链路知识闭环。
```

- [ ] **Step 2: 验证结构、LaTeX、圈号**

Run:

```bash
cd 3gpp && test -f "docs/concepts/TX_Chain_发送端处理链总览.md" && grep -c "^## " "docs/concepts/TX_Chain_发送端处理链总览.md" && python3 tools/audit_latex_render.py --syntax-only "docs/concepts/TX_Chain_发送端处理链总览.md" 2>&1 | tail -2 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: `6`；latex 通过；圈号无新增 FAIL。
注意：wikilink 批内两篇（F1/F2 已创建，存在）+ 既有发送端笔记（Gold/Layer_Mapping/Precoding 存在）；fenced 代码块（处理链图）内无 wikilink。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/TX_Chain_发送端处理链总览.md" && git commit -m "docs(concepts): 新增 TX Chain 发送端处理链总览概念笔记（11 环全景，阶段 1 收官）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task F4: 同步清单（图谱入口 3 行 + L0 术语总表补缺 + 索引 3 行 + 计数修正）

**Files:**
- Modify: `3gpp/docs/concepts/概念图谱入口.md`（「发送链路」组 3 行）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（术语补缺 + 索引 3 行 + 引言计数）

**Interfaces:**
- Consumes: Task F1-F3 三个笔记名。
- Produces: 术语总表补缺 + 挂载 3 行 + 索引 3 行。

- [ ] **Step 1: 图谱入口挂载 3 行**

Run: `grep -n "DFT_sOFDM_上行波形\|PRACH_随机接入" 3gpp/docs/concepts/概念图谱入口.md`
Expected: 行号 M（「发送链路」组内）。在组内（DFT_sOFDM 行后）追加：

```markdown
- [[Modulation_Mapping_调制映射]]
- [[RE_Mapping_资源元素映射]]
- [[TX_Chain_发送端处理链总览]]
```

- [ ] **Step 2: 术语总表补缺**

Run: `grep -c "^| RE \|^| 调制阶数 \|^| Qm " 3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`
Expected: 若 RE/Qm 已登记则跳过；若缺则在「## 系统与协议」节（`| TA |` 行后）追加：

```markdown
| RE | 资源元素 | Resource Element；一个子载波×一个符号的时频最小单位。→ [[RE_Mapping_资源元素映射]] |
| Qm | 调制阶数 | Modulation Order；每符号承载比特数（QPSK 2/16QAM 4/64QAM 6/256QAM 8）。→ [[Modulation_Mapping_调制映射]] |
```

- [ ] **Step 3: 概念笔记索引区追加 3 行（2 列格式）**

在「### 协议、信道与信号」分区末尾（`[[UL_DL_Differences_上下行差异]]` 行后）追加：

```markdown
| [[Modulation_Mapping_调制映射]] | TS 38.211 §5.1 星座表与归一化因子。 |
| [[RE_Mapping_资源元素映射]] | 符号到网格的填充规则与参考信号避让。 |
| [[TX_Chain_发送端处理链总览]] | 发送端 11 环处理链全景（阶段 1 收官）。 |
```

- [ ] **Step 4: 引言计数修正**

术语总表引言与索引区引言「（92 篇）」→ 修正为实测数（`ls docs/concepts/*.md | grep -v "概念图谱入口\|3GPP全流程" | wc -l`，应为 95）。

- [ ] **Step 5: 验证同步完整性**

Run:

```bash
cd 3gpp && grep -c "Modulation_Mapping_调制映射\|RE_Mapping_资源元素映射\|TX_Chain_发送端处理链总览" docs/concepts/概念图谱入口.md docs/L0_协议阅读引导/L0_terminology_glossary.md && grep -c "^| RE \|^| Qm " docs/L0_协议阅读引导/L0_terminology_glossary.md
```

Expected: 图谱入口 3 处、术语表 ≥5 处（3 索引 + 2 条目）、2 项术语行齐全（输出 `2`）。

- [ ] **Step 6: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/concepts/概念图谱入口.md" "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "docs(sync): 图谱入口挂载发送端三篇 + L0 术语总表登记 RE/Qm + 计数修正

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task F5: 全量验证

**Files:**
- 无新增；FAIL 则修复对应文件。

**Interfaces:**
- Consumes: Task F1-F4 全部改动 + 历次批次全部改动（合流验证）。

- [ ] **Step 1: 运行全部审计**

```bash
cd 3gpp && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_latex_render.py --syntax-only docs/concepts && python3 tools/audit_circled_digits.py && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs
```

Expected: 各工具 PASS/OK。**已知处置**：`3GPP全流程_缩写概念理论清单.md:21` 存量假阳性不改；link_integrity 在 F1-F4 落地后应无新 FAIL（F1 的前瞻链接在 F2 创建后闭合）；任何新 FAIL → Step 2 修复后复跑，直到全绿。

- [ ] **Step 2: 修复 FAIL 并复跑**

按工具输出逐条修复，复跑 Step 1 全部命令。

- [ ] **Step 3: 提交（如有修复）**

```bash
cd /home/yys/AGENT/obsidian && git add -A 3gpp && git commit -m "fix(docs): 发送端批次审计修复（如无修复跳过此步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task F6: 双推提交

**Files:**
- 无代码变更。

**Interfaces:**
- Consumes: Task F1-F5 全部提交。

- [ ] **Step 1: 确认工作区干净**

Run: `git status --porcelain` → 空输出。

- [ ] **Step 2: 推送双远端**

```bash
cd /home/yys/AGENT/obsidian && git push origin master 2>&1 | tail -4
```

Expected: Gitee 与 GitHub 两处 `master -> master`；单远端失败必须报告处理。

- [ ] **Step 3: 登记执行证据 + 阶段 1 收官登记**

工具缺失（KaTeX/mmdc）在此汇报中显式声明验证缺口；**阶段 1 收官声明**：G1-G5 概念笔记铺开全部完成（本批次后概念笔记 95 篇）；下一阶段候选：阶段 2（控制信道/上行深化讲义）或结构治理（TECH_TERMS 全库配对：PDCCH/PUCCH/PBCH/NDI/RI/TA 等 30+ 缩写全库治理）。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——批次内容（G2 三篇）→ Task F1-F3；工具不扩 TECH_TERMS → Task F5。同步清单 → Task F4。
- 占位符：无 TBD/TODO；三篇笔记全文写入任务步骤。
- 一致性：wikilink 创建顺序正确（F1 引用 F2 的前瞻在 F2 创建后闭合、F3 收尾引用全部）；术语配对完整三件套（三批次 40+ 处返工教训——F1-F3 内容已按「中文（English Full Name, ABBR）」写定）；数值自洽（Qm 2/4/6/8、归一化因子 √2/√10/√42/√170、星座点数 4/16/64/256）。
- 双链：F3 收尾篇↔F1/F2 互链 + 既有发送端笔记（Gold/Layer_Mapping/Precoding）全链；F1/F2 与控制面/调度批次（MCS_Table/Scheduler/DCI）双链。
- 阶段 1 收官登记：本批次完成后概念笔记 95 篇，阶段 1（G1-G5）全量完成。
