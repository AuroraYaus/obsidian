# TECH_TERMS 结构治理 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 全量治理技术缩写首现配对缺口：工具层（G0：术语表补 9 + TECH_TERMS 登记 105 + 正则防混淆）+ 文件层（G1-G6：124 篇讲义 855 处修复，分 6 轮 SDD）。完成后 Rule 10 逐文件自足全库达标、审计工具全绿（仅清单假阳性）。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-term-governance.md` 执行。阶段 G0（工具层 4 任务）+ 阶段 G1-G6（文件层 6 轮，每轮 3-4 个子任务）。**修复规范**（全局约束）：每篇讲义对每个治理缩写**首次出现处**补「ABBR（中文，English Full Name）」三件套（用户拍板 2026-08-12，同 :14）；中文全称以 L0 术语表为统一口径；只加配对不改其他内容；概念笔记不在治理范围。

**Tech Stack:** Markdown + Python（audit_lesson_terms.py）+ 项目 audit 工具链。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- 配对格式统一「ABBR（中文，English Full Name）」（用户拍板 2026-08-12；与本会话 104 篇概念笔记及既有讲义正文一致；TECH_TERMS 字典值为查阅口径「中文全称（English Full Name, ABBR）」，非正文配对格式）；中文全称以 `docs/L0_协议阅读引导/L0_terminology_glossary.md` 术语表为准（如 MAC=媒体接入控制层，非介质访问控制）。
- **只加配对、不改内容**：修复仅插入三件套于首现处，不得改写句子、不得动代码块内文本（代码块内缩写豁免惯例）、不得删改既有配对。
- 特殊处理清单（防误配）：CA-SCL 不得匹配 CA；Max_Log_MAP 不得匹配 MAP；Qm.n 定点格式不得匹配 Qm；SCL 与 CA-SCL 独立词条；DM-RS 与 DMRS 按术语表别名方案统一。
- 带圈数字禁令（第 10 条）；标题正式化（Rule 16）。
- 工具缺失显式声明验证缺口。
- 提交后 `git push origin master`（双推，阶段收尾统一执行）。

---

## 阶段 G0：工具层（4 任务）

### Task T1: L0 术语表补 9 项未登记缩写

**Files:**
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（「## 调制、信道与性能」节或合适位置追加 9 项）

**Interfaces:**
- Produces: 9 项术语表行（SSB/SRS/CORESET/CCE/REG/OFDM/CP/IFFT/FFT），T2 的 audit_glossary 覆盖检查依赖。

- [ ] **Step 1: 追加 9 项**

Run: `grep -n "^| OFDM \|^| CP \|^| FFT " 3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`
Expected: 统计存量（盘点：9 项均未登记）。在「## 调制、信道与性能」节（`| PAPR |` 行后或合适位置）追加（3 列格式，中文全称与既有笔记配对一致）：

```markdown
| OFDM | 正交频分复用 | Orthogonal Frequency Division Multiplexing；多载波调制，子载波正交重叠。→ [[DFT_sOFDM_上行波形]] |
| CP | 循环前缀 | Cyclic Prefix；OFDM 符号前部冗余，消除 ISI/ICI。 |
| FFT | 快速傅里叶变换 | Fast Fourier Transform；OFDM 接收端时频变换。 |
| IFFT | 逆快速傅里叶变换 | Inverse Fast Fourier Transform；OFDM 发送端频时变换。 |
| SSB | 同步信号块 | Synchronization Signal Block；PSS+SSS+PBCH 一体。→ [[PSS_SSS_同步信号与小区搜索]] |
| SRS | 探测参考信号 | Sounding Reference Signal；上行信道探测。→ [[SRS_探测参考信号]] |
| CORESET | 控制资源集 | Control Resource Set；PDCCH 可占用的时频资源块。→ [[PDCCH_物理下行控制信道]] |
| CCE | 控制信道单元 | Control Channel Element；PDCCH 分配最小单位（6 REG）。 |
| REG | 资源元素组 | Resource Element Group；1 PRB × 1 符号。 |
```

- [ ] **Step 2: 验证**

Run:

```bash
cd 3gpp && grep -c "^| OFDM \|^| CP \|^| FFT \|^| IFFT \|^| SSB \|^| SRS \|^| CORESET \|^| CCE \|^| REG " docs/L0_协议阅读引导/L0_terminology_glossary.md
```

Expected: `9`。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "docs(sync): 术语表补 9 项未登记缩写（SSB/SRS/CORESET/CCE/REG/OFDM/CP/IFFT/FFT）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task T2: TECH_TERMS 登记 105 项

**Files:**
- Modify: `3gpp/tools/audit_lesson_terms.py`（TECH_TERMS 字典追加 62 项）

**Interfaces:**
- Consumes: T1 术语表 9 项（audit_glossary 覆盖检查）。
- Produces: TECH_TERMS 105 项全量（现有 43 + 新增 62），T3 正则防混淆后全库 glossary 检查通过。

- [ ] **Step 1: TECH_TERMS 追加 62 项**

在 `TECH_TERMS` 字典末尾（`"TBCC": ...` 行后）追加以下条目（格式与既有一致 `"ABBR": "中文全称（English Full Name, ABBR）"`；中文全称以术语表为准）：

```python
    "PDCCH": "物理下行控制信道（Physical Downlink Control Channel, PDCCH）",
    "PUCCH": "物理上行控制信道（Physical Uplink Control Channel, PUCCH）",
    "PDSCH": "物理下行共享信道（Physical Downlink Shared Channel, PDSCH）",
    "PUSCH": "物理上行共享信道（Physical Uplink Shared Channel, PUSCH）",
    "PBCH": "物理广播信道（Physical Broadcast Channel, PBCH）",
    "MIB": "主信息块（Master Information Block, MIB）",
    "SIB": "系统信息块（System Information Block, SIB）",
    "PSS": "主同步信号（Primary Synchronization Signal, PSS）",
    "SSS": "辅同步信号（Secondary Synchronization Signal, SSS）",
    "SSB": "同步信号块（Synchronization Signal Block, SSB）",
    "RNTI": "无线网络临时标识（Radio Network Temporary Identifier, RNTI）",
    "NDI": "新数据指示（New Data Indicator, NDI）",
    "RV": "冗余版本（Redundancy Version, RV）",
    "PMI": "预编码矩阵指示（Precoding Matrix Indicator, PMI）",
    "RI": "秩指示（Rank Indicator, RI）",
    "CQI": "信道质量指示（Channel Quality Indicator, CQI）",
    "RBG": "资源块组（Resource Block Group, RBG）",
    "VRB": "虚拟资源块（Virtual Resource Block, VRB）",
    "SRS": "探测参考信号（Sounding Reference Signal, SRS）",
    "PTRS": "相位跟踪参考信号（Phase Tracking Reference Signal, PTRS）",
    "TRS": "跟踪参考信号（Tracking Reference Signal, TRS）",
    "CRS": "小区特定参考信号（Cell-specific Reference Signal, CRS）",
    "CSI-RS": "信道状态信息参考信号（Channel State Information Reference Signal, CSI-RS）",
    "CORESET": "控制资源集（Control Resource Set, CORESET）",
    "CCE": "控制信道单元（Control Channel Element, CCE）",
    "REG": "资源元素组（Resource Element Group, REG）",
    "RE": "资源元素（Resource Element, RE）",
    "PRB": "物理资源块（Physical Resource Block, PRB）",
    "BWP": "带宽部分（Bandwidth Part, BWP）",
    "LCID": "逻辑信道标识（Logical Channel Identity, LCID）",
    "ADC": "模数转换器（Analog-to-Digital Converter, ADC）",
    "OFDM": "正交频分复用（Orthogonal Frequency Division Multiplexing, OFDM）",
    "CP": "循环前缀（Cyclic Prefix, CP）",
    "DFT": "离散傅里叶变换（Discrete Fourier Transform, DFT）",
    "IFFT": "逆快速傅里叶变换（Inverse Fast Fourier Transform, IFFT）",
    "FFT": "快速傅里叶变换（Fast Fourier Transform, FFT）",
    "MIMO": "多输入多输出（Multiple-Input Multiple-Output, MIMO）",
    "PRACH": "物理随机接入信道（Physical Random Access Channel, PRACH）",
    "UE": "用户设备（User Equipment, UE）",
    "RRC": "无线资源控制（Radio Resource Control, RRC）",
    "CBG": "码块组（Code Block Group, CBG）",
    "BCJR": "BCJR 算法（Bahl-Cocke-Jelinek-Raviv Algorithm, BCJR）",
    "MAP": "最大后验概率（Maximum A Posteriori, MAP）",
    "CA-SCL": "CRC 辅助连续消除列表译码（CRC-Aided Successive Cancellation List, CA-SCL）",
    "SCL": "连续消除列表译码（Successive Cancellation List, SCL）",
    "1024QAM": "1024 阶正交幅度调制（1024 Quadrature Amplitude Modulation, 1024QAM）",
    "Qm": "调制阶数（Modulation Order, Qm）",
    "SNR": "信噪比（Signal-to-Noise Ratio, SNR）",
    "SINR": "信干噪比（Signal-to-Interference-plus-Noise Ratio, SINR）",
    "BER": "比特错误率（Bit Error Rate, BER）",
    "FER": "误帧率（Frame Error Rate, FER）",
    "TDL": "抽头时延线（Tapped Delay Line, TDL）",
    "OCC": "正交覆盖码（Orthogonal Cover Code, OCC）",
    "SIMO": "单输入多输出（Single-Input Multiple-Output, SIMO）",
    "SISO": "软入软出（Soft-Input Soft-Output, SISO）",
    "CSI": "信道状态信息（Channel State Information, CSI）",
    "MMSE": "最小均方误差（Minimum Mean Square Error, MMSE）",
    "ZF": "迫零（Zero-Forcing, ZF）",
    "MF": "匹配滤波（Matched Filter, MF）",
    "MRC": "最大比合并（Maximum Ratio Combining, MRC）",
    "ML": "最大似然（Maximum Likelihood, ML）",
    "DMRS": "解调参考信号（Demodulation Reference Signal, DMRS）",
    "RSRP": "参考信号接收功率（Reference Signal Received Power, RSRP）",
    "PS": "概率整形（Probabilistic Shaping, PS）",
    "DM": "分布匹配（Distribution Matching, DM）",
    "ESS": "枚举球面整形（Enumerative Sphere Shaping, ESS）",
    "MB": "麦克斯韦-玻尔兹曼（Maxwell-Boltzmann, MB）",
    "SBPM": "整形比特位置映射（Shaped Bit Position Mapping, SBPM）",
    "GS": "几何整形（Geometric Shaping, GS）",
    "DUT": "被测设备（Device Under Test, DUT）",
    "DMA": "直接内存访问（Direct Memory Access, DMA）",
    "SVA": "系统 Verilog 断言（SystemVerilog Assertions, SVA）",
    "UVM": "通用验证方法学（Universal Verification Methodology, UVM）",
    "STA": "静态时序分析（Static Timing Analysis, STA）",
    "PPA": "功耗性能面积（Power Performance Area, PPA）",
    "DAC": "数模转换器（Digital-to-Analog Converter, DAC）",
    "PAPR": "峰均功率比（Peak-to-Average Power Ratio, PAPR）",
    "EVM": "误差矢量幅度（Error Vector Magnitude, EVM）",
    "PA": "功率放大器（Power Amplifier, PA）",
    "LUT": "查找表（Look-Up Table, LUT）",
    "CORDIC": "坐标旋转数字计算（Coordinate Rotation Digital Computer, CORDIC）",
    "SE": "频谱效率（Spectral Efficiency, SE）",
    "MACs": "乘加运算（Multiply-Accumulate operations, MACs）",
    "ROM": "只读存储器（Read-Only Memory, ROM）",
    "Hadamard": "哈达玛（Hadamard）",
    "Cholesky": "乔列斯基分解（Cholesky Decomposition, Cholesky）",
    "FR1": "频率范围 1（Frequency Range 1, FR1）",
    "FR2": "频率范围 2（Frequency Range 2, FR2）",
    "DFT-s-OFDM": "离散傅里叶变换扩展正交频分复用（Discrete Fourier Transform Spread OFDM, DFT-s-OFDM）",
    "SC-FDMA": "单载波频分多址（Single Carrier Frequency Division Multiple Access, SC-FDMA）",
```

（注：TECH_TERMS 已含 43 项；以上新增 62 项合计 105 项。若有与既有重复的条目（如 MIMO 已含？）以 grep 现状为准去重；CA 的载波聚合语义与 CA-SCL 冲突，**不登记 CA**（T3 处理）。）

- [ ] **Step 2: 验证 Python 语法与 glossary 覆盖**

Run:

```bash
cd 3gpp && python3 -c "import ast; ast.parse(open('tools/audit_lesson_terms.py').read()); print('PY_SYNTAX_OK')" && python3 tools/audit_lesson_terms.py docs 2>&1 | tail -3
```

Expected: PY_SYNTAX_OK；audit 输出仅剩清单文件假阳性（`3GPP全流程_缩写概念理论清单.md:21`）或全 PASS（T1 术语表补全后 audit_glossary 对 9 项通过）。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/tools/audit_lesson_terms.py" && git commit -m "feat(tools): audit_lesson_terms TECH_TERMS 全量登记 105 项（结构治理 G0-T2）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task T3: 正则防混淆与歧义处理

**Files:**
- Modify: `3gpp/tools/audit_lesson_terms.py`（TECH_TERM_RE 构造 + 特殊处理）

**Interfaces:**
- Consumes: T2 TECH_TERMS 105 项。
- Produces: 防混淆正则（CA 不匹配 CA-SCL 等），T4 验证依赖。

- [ ] **Step 1: 检查与修正正则**

Read `tools/audit_lesson_terms.py` 中 TECH_TERM_RE 构造与使用处，核对并落实：
1. **CA-SCL vs CA**：TECH_TERMS 不登记 CA（载波聚合）——确认无 CA 条目即可（盘点已核实 CA 的载波聚合语义在讲义零使用；若 audit 逻辑会匹配 CA-SCL 子串则确认 `(?<![A-Za-z0-9])CA(?![A-Za-z0-9])` 对 "CA-SCL" 的匹配行为——连字符后是 `-` 非字母数字，负向前瞻不阻断，会误匹配——需在 TECH_TERM_RE 或使用处排除，如 `CA(?!-)`）。
2. **MAP vs Max_Log_MAP**：`(?<![A-Za-z0-9])MAP(?![A-Za-z0-9])` 对 "Max_Log_MAP" 中的 MAP——前缀 `_` 非字母数字，负向后瞻不阻断——需排除 `MAP(?<!Log_)` 或使用处处理（核对工具当前行为后决定最小修正）。
3. **Qm vs Qm.n**：`(?<![A-Za-z0-9])Qm(?![A-Za-z0-9])` 对 "Qm.n"——后缀 `.` 非字母数字，负向前瞻不阻断——需排除 `Qm(?!\.)`。
4. **SCL vs CA-SCL**：独立词条（CA-SCL 单独登记，SCL 匹配 "CA-SCL" 子串？`(?<![A-Za-z0-9])SCL(?![A-Za-z0-9])` 对 "CA-SCL"——前缀 `-` 非字母数字会匹配——需排除或确认盘点口径）。
5. **DM-RS vs DMRS**：术语表是否加 DM-RS 别名行（盘点：13 文件用 DM-RS 变体）——在术语表「调制、信道与性能」节加 `| DM-RS | 解调参考信号 | Demodulation Reference Signal；DMRS 连字符变体。→ [[DMRS_解调参考信号]] |`，TECH_TERMS 登记 DM-RS 为独立词条或文件层统一拼写（T3 定方案：**术语表加别名行 + TECH_TERMS 加 DM-RS 词条**，文件层不改拼写）。
6. 核对 `TECH_TERM_RE` 是否实际被使用（此前审查发现可能是死代码）——如实报告使用状态；若未使用则防混淆修正仅保证未来启用时安全，并在报告说明。

- [ ] **Step 2: 验证**

Run:

```bash
cd 3gpp && python3 -c "
import re, sys
sys.path.insert(0, 'tools')
from audit_lesson_terms import TECH_TERMS, TECH_TERM_RE
# 断言防混淆
for pat, bad in [('CA', 'CA-SCL'), ('MAP', 'Max_Log_MAP'), ('Qm', 'Qm.n'), ('SCL', 'CA-SCL')]:
    r = re.compile(rf'(?<![A-Za-z0-9]){re.escape(pat)}(?![A-Za-z0-9])')
    print(pat, 'matches' if r.search(bad) else 'safe', bad)
" 2>&1 | tail -6
```

Expected: 记录每个模式对混淆串的匹配状态；对误匹配项落实修正（修正方式：使用处过滤或正则特化，以最少改动为准）后复跑断言显示 safe。

- [ ] **Step 3: 提交**

```bash
cd /home/yys/AGENT/obsidian && git add "3gpp/tools/audit_lesson_terms.py" "3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md" && git commit -m "feat(tools): 术语正则防混淆（CA/MAP/Qm/SCL 歧义）+ DM-RS 别名行（结构治理 G0-T3）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task T4: 工具层验证

**Files:**
- 无新增；FAIL 则修复对应文件。

**Interfaces:**
- Consumes: T1-T3 全部改动。
- Produces: G0 收官证据——audit_lesson_terms 全库 PASS（仅清单假阳性）+ glossary 覆盖全过。

- [ ] **Step 1: 运行验证**

Run:

```bash
cd 3gpp && python3 tools/audit_lesson_terms.py docs 2>&1 | tail -5 && python3 tools/audit_circled_digits.py 2>&1 | tail -1
```

Expected: audit_lesson_terms 仅剩 `3GPP全流程_缩写概念理论清单.md:21` 假阳性（或不剩——若工具豁免路径更新则 PASS）；circled OK。任何新 FAIL → Step 2 修复复跑。

- [ ] **Step 2: 提交（如有修复）**

```bash
cd /home/yys/AGENT/obsidian && git add -A 3gpp && git commit -m "fix(tools): G0 工具层验证修复（如无修复跳过此步）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## 阶段 G1-G6：文件层（框架——轮内任务在每轮执行时生成）

**修复规范**（每轮子任务统一遵守）：
1. 轮内文件清单由轮任务给出（每轮 ~20-25 篇，按层分）。
2. 每篇讲义：对**每个**在 TECH_TERMS 105 项中的缩写，定位**首次出现处**（词边界），插入「中文（English Full Name, ABBR）」三件套——中文全称从术语表行取（与 T2 登记的 TECH_TERMS 条目一致）。
3. 只加配对：不改写句子、不删改既有内容、不动代码块内文本（代码块豁免）、不动 LaTeX/表格结构（表格单元格内首现可用紧凑形式）。
4. 防混淆清单：CA-SCL/Max_Log_MAP/Qm.n/SCL 按 T3 结论处理（独立词条各自配对，不互相误配）。
5. 每轮验证：`python3 tools/audit_lesson_terms.py <轮范围路径>`（若支持路径）+ headings + circled；修复后该范围术语审计应 PASS（或仅剩假阳性）。
6. 每轮提交（每子任务 1-2 个 commit，按篇分批提交便于审查）。

**轮次定义**（篇数按实施时 ls 实测为准，编号区间为盘点时参考）：

| 轮 | 范围 | 预估篇数 | 重灾篇（子任务内优先） |
|:---|:---|:---|:---|
| G1 | L1_基础 前段（T1.x-T2.x 前半） | ~22 | T2.0(24)/T2.3(21)/T2.8(23) |
| G2 | L1_基础 后段（T2.x 后半-T5.x） | ~21 | T2.10(21)/T2.11(21)/T3.x |
| G3 | L2_协议算法 前段（T6-T8） | ~20 | T8.x |
| G4 | L2_协议算法 中段（T9-T10） | ~20 | T9.x/T10.x |
| G5 | L2_协议算法 后段（T11-T13） | ~19 | T13.6(25)/T11.x |
| G6 | L3_工程实现（T17-T21） | ~30 | T21.x |

每轮执行时：提取轮定义 → 拆 3-4 个子任务（每子任务 6-8 篇，重灾篇独立）→ 逐子任务 dispatch implementer（携带修复规范 + 该子任务文件清单 + 术语表中文全称参考）→ 子任务审查 → 轮验证 → 提交。轮内不设独立 PLAN，直接按本框架执行并更新 ledger。

**文件层收尾**（G6 完成后）：全库审计（6 项）全绿（仅清单假阳性）+ 双推 + 治理总结（修复处数统计、Rule 10 达标声明）。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——策略（先工具后文件批量）→ 阶段 G0/G1-G6；总量（全量 105 缩写/855 处/124 篇）→ T2 全量登记 + 6 轮全量修复。
- 占位符：G1-G6 轮内任务按框架生成（修复规范已完整定义，无 TBD）；G0 四任务全文写入。
- 一致性：TECH_TERMS 中文全称与术语表行一致（统一口径）；T3 防混淆与盘点特殊处理清单一致；修复规范与 Rule 10 逐文件自足一致。
- 风险登记：855 处量大（每轮严格限定范围）；同名歧义以 T3 核对为准；DM-RS 别名方案 T3 定。
