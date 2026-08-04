# MIMO 接收机与检测器讲义系列实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 完成 5 篇 L2 讲义（T12.1-T12.5，MIMO 接收机与检测器系列）+ L2 入口 M12 章节 + 概念笔记回链，每篇 500-800 行、≥1 个通过视觉验证的 SVG 图、1 个可运行的内嵌 numpy 验证。

**Architecture:** 每篇讲义独立任务（正文 + SVG + numpy 验证 + 提交），执行顺序 T12.1 → T12.5（有依赖：T12.2-12.5 引用 T12.1 的总览概念）。讲义素材来自已提交的概念笔记（Detector_Comparison/Diversity_Combining/Channel_Estimation/MMSE_均衡/Sphere_Decoding/CSI_SINR/MIMO_多天线系统）与外部语料（`/home/yys/AGENT/3GPP_FULL_LINK/reproduction_output/deep_dive/` MIMO01/PHY01/PS02——只读引用，不复制）。

**Tech Stack:** Obsidian markdown、LaTeX（\tag 编号）、手写 SVG（cairosvg 验证）、numpy 2.5.1 内嵌代码、git。

## Global Constraints

- 讲义模板（范本 `3gpp/docs/L2_协议算法/T8.1_NR_LDPC_decoder_chain_overview.md`）：frontmatter（`type: algorithm`、aliases、tags 含 `l2`/`lesson`、source_spec）→ `# T12.x 中文标题` → `## 本节学习目标`（叙事 intro + "学完本节后，应能做到：" 6-8 条可检验 bullets + 系列内衔接段）→ `## 前置知识检查`（表格 `| 前置项 | 本节需要达到的程度 |`）→ 内容章节 → `## 小结`（收束 + 指向下一篇）
- 每篇 **500-800 行**（`wc -l` 验证），内容有广度和深度：数学推导、协议锚点、工程代价、生活类比、数值实例、表格
- **每篇 ≥1 个 SVG 图**（硬性要求）：存 `3gpp/docs/L2_协议算法/assets/T12.x_<英文主题>.svg`；**强制视觉验证**：(1) Y 坐标扫描（全部 `<text>/<rect>/<line>` 的 y 属性，相邻间距 ≥ 8 px，违规必须修复）(2) PNG 预览（`cairosvg` 转 PNG 后**用 Read 工具肉眼检查无文字/图形交叠**）——两步证据记入实施报告
- **内嵌 numpy 验证**：每篇 1 个 python 代码围栏（本计划给出完整代码，逐字使用），必须实际运行，输出与讲义断言一致，输出记入实施报告
- 合规红线：Rule 10（英文术语首现"中文（English）"）、Rule 16（标题口语化禁止）、Rule 20（LaTeX 可渲染）、Rule 8（每篇至少 1 个生活类比）
- 协议锚点：TS 38.211 §7.3.1.3（层映射/单码字≤4层）、§5.1（星座）、§7.4.1.1（DMRS）；TS 38.214 §5.1.3（MCS/TBS）；本地锚点 `3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`
- 文件名：`T12.x_<english_snake_case>.md`；wikilink 全部可解析（新讲义引用的概念笔记/T2.x 均存在）
- 每篇 图谱衔接：讲义内 `[[概念笔记]]` 链接 + 概念笔记侧回链由 Task 6 统一补

---

### Task 1: T12.1 MIMO 接收链路总览

**Files:**
- Create: `3gpp/docs/L2_协议算法/T12.1_mimo_receiver_chain_overview.md`（500-800 行）
- Create: `3gpp/docs/L2_协议算法/assets/T12.1_mimo_receiver_chain.svg`（SVG 图）

**Interfaces:**
- Produces: T12.1 讲义与 SVG；T12.2-12.5 引用其总览概念（每 RE 模型、H_eff、功率归一化），文件名/标题不得更改

- [ ] **Step 1: 写讲义正文**

章节结构与要点（按序）：
1. `## 本节学习目标`：叙事 intro 从"L1 讲完单天线软解调，接收端如何扩展到多天线"切入；bullets：画接收链路地图（RE 网格→均衡→软解调→LLR 向量）；写每 RE 模型 y=H·P·x+n 并解释四个量的维度；说明层域等效信道 H_eff=H·P 与"接收机只关心 H_eff"；推导发射功率归一化 E‖Px‖²=‖P‖_F²E_s 与 ‖P‖_F=1 时天线域总功率恒等；说明单码字 ≤4 层约束（TS 38.211 §7.3.1.3）与 transpose/ctranspose 约定；论证"译码器对 RE 网格不可见"（衔接 T2.6）
2. `## 前置知识检查`：表格引用 L1 T2.6（RE 网格→LLR）、T2.14（QAM 软解调）、T2.15（衰落信道）、概念笔记 MIMO_多天线系统、LLR_对数似然比
3. `## 从单天线到多天线：为什么需要矩阵模型`：生活类比（"多个话筒录同一场音乐会"）；单天线 y=hx+n 到多天线 y=Hx+n 的过渡；H 的维度与物理含义（每元素是 Tx-Rx 天线对的复增益）
4. `## 每 RE 的线性 MIMO 模型`：y=H·P·x+n 完整定义（H∈C^{Nrx×Ntx}、x∈C^{Nlayers}、n~CN(0,σ²I)）；发射端 x 是层域符号；预编码 P 的作用；数值实例表（Ntx=2/Nrx=2/Nlayers=2 的维度对照）
5. `## 层域等效信道 H_eff`：H_eff=H·P 的推导与含义；"接收机不需要知道 P，只需要 H_eff"（DMRS 走预编码的直接后果，衔接 T12.5）；天线域 vs 层域信道估计的区分
6. `## 发射功率归一化`：E‖Px‖²=‖P‖_F²E_s 推导；DFT/Hadamard/Identity 三种预编码器各归一到 ‖P‖_F=1；'none' 模式也过归一化的陷阱（Nlayers>1 时每层功率 E_s/L）；单码字 ≤4 层约束
7. `## 接收机从 RE 网格到 LLR`：接收链路流程图文字描述（OFDM 解调→信道估计→预编码逆处理→检测→软解调→CSI 加权→LLR 向量）；**译码器对 RE 网格不可见**——new_pdsch_decode 输出一维 LLR 向量，MIMO 全部在上游剥离（衔接 T2.6 的既有原则）
8. `## 内嵌验证：功率守恒`：本计划 Task 1 的 numpy 代码（见 Step 2），讲解预期输出（‖P‖_F=1 时层域/天线域总功率相等）
9. `## 小结`：总结地图 + 指向 T12.2（分集与合并）

- [ ] **Step 2: 生成 SVG 图 `T12.1_mimo_receiver_chain.svg`**

主题：**MIMO 接收链路流程图**（横向流程：`天线域信号 y` → `OFDM 解调` → `信道估计(H_est)` → `预编码逆处理(H_eff=H·P)` → `检测器(MMSE/Sphere)` → `软解调+CSI 加权` → `一维 LLR 向量 → 译码器`）。布局规格：7 个流程框横向排列（框尺寸建议 150×54px、间距 40px），框下方标注维度变化（如 `C^{Nrx×Nfft}` → … → `C^{G×1}`）；SVG 画布宽建议 1350×320px；**所有 `<text>/<rect>/<line>` 相邻 y 间距 ≥ 8 px**（框内文字与框边距 ≥ 6px 视觉不重叠即可，文字行间距 ≥ 8px）。
必须执行视觉验证并记录输出：
```bash
# (1) Y 坐标扫描（必须）
python3 - <<'EOF'
import re
svg = open('3gpp/docs/L2_协议算法/assets/T12.1_mimo_receiver_chain.svg').read()
ys = []
for tag in ('text','rect','line'):
    for m in re.finditer(r'<%s[^>]*\by="([0-9.]+)"' % tag, svg):
        ys.append((tag, float(m.group(1))))
ys.sort(key=lambda t: t[1])
gaps = [(round(b[1]-a[1],1), a, b) for a,b in zip(ys, ys[1:]) if b[1]-a[1] < 8]
print(f"{len(ys)} 个 y 元素；最小间距 = {min(b[1]-a[1] for a,b in zip(ys,ys[1:])) if len(ys)>1 else 'n/a'}")
print("间距<8px:", gaps if gaps else "无 ✓")
EOF
# (2) PNG 预览（必须肉眼检查）
cairosvg 3gpp/docs/L2_协议算法/assets/T12.1_mimo_receiver_chain.svg -o /tmp/t12_1_preview.png
```
然后用 Read 工具打开 `/tmp/t12_1_preview.png` 肉眼确认无文字交叠、无元素重叠；把 PNG 检查结论写入报告。若 Y 扫描或肉眼发现交叠，修复 SVG 后重新验证，直到通过。

- [ ] **Step 3: 运行内嵌 numpy 验证代码**（完整代码，逐字嵌入讲义 `## 内嵌验证` 节并运行）

```python
import numpy as np

def build_precoder(mode, Nt, Nl):
    """构造预编码器并做 Frobenius 归一化（‖P‖_F = 1）。"""
    if mode == 'dft':
        P = np.exp(-2j*np.pi*np.arange(Nt)[:,None]*np.arange(Nl)[None,:]/Nt)
    elif mode == 'hadamard':
        P = np.array([[1,1],[1,-1]], dtype=complex)[:, :Nl]
    elif mode == 'identity':
        P = np.eye(Nt, Nl, dtype=complex)
    return P / np.linalg.norm(P, 'fro')

rng = np.random.default_rng(0)
for Nt, Nl in [(2,1),(2,2),(4,2),(4,4)]:
    P = build_precoder('dft', Nt, Nl)
    x = rng.standard_normal((Nl, 1000)) + 1j*rng.standard_normal((Nl, 1000))
    E_in  = np.mean(np.sum(np.abs(x)**2, axis=0))        # 层域总功率
    E_out = np.mean(np.sum(np.abs(P @ x)**2, axis=0))    # 天线域总功率
    assert abs(np.linalg.norm(P,'fro') - 1.0) < 1e-12
    assert abs(E_out - E_in) < 1e-10, (Nt, Nl, E_out, E_in)
    print(f"Nt={Nt} Nl={Nl}: ‖P‖_F={np.linalg.norm(P,'fro'):.6f}  层域功率={E_in:.4f}  天线域功率={E_out:.4f}  守恒✓")
```
预期：4 行全部打印"守恒✓"（无 AssertionError）。运行命令：`python3 - <<'EOF' ... EOF`（从讲义中提取代码运行），输出记入报告。

- [ ] **Step 4: 结构/行数/死链验证**

```bash
wc -l 3gpp/docs/L2_协议算法/T12.1_mimo_receiver_chain_overview.md          # 预期 500-800
grep -c "^## " 3gpp/docs/L2_协议算法/T12.1_mimo_receiver_chain_overview.md # 预期 ≥6（学习目标/前置检查/各章节/小结）
# 死链：讲义内全部 [[...]] 链接目标必须存在
grep -oE "\[\[[^]]+\]\]" 3gpp/docs/L2_协议算法/T12.1_mimo_receiver_chain_overview.md | sed 's/\[\[//;s/\]\]//;s/|.*//' | while read -r l; do
  find 3gpp -name "${l}.md" | grep -q . || echo "DEAD: $l"; done; echo "link check done"
```
预期：无 DEAD 输出；行数在范围内。

- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/L2_协议算法/T12.1_mimo_receiver_chain_overview.md 3gpp/docs/L2_协议算法/assets/T12.1_mimo_receiver_chain.svg
git commit -m "docs(lectures): T12.1 MIMO 接收链路总览（含 SVG 图与功率守恒验证）"
```

---

### Task 2: T12.2 分集与合并

**Files:**
- Create: `3gpp/docs/L2_协议算法/T12.2_diversity_combining_mrc.md`（500-800 行）
- Create: `3gpp/docs/L2_协议算法/assets/T12.2_diversity_combining.svg`（SVG 图）

**Interfaces:**
- Consumes: T12.1 的总览模型（y=H·P·x+n、层域概念）
- Produces: T12.2 讲义；T12.3 引用"MMSE 单层 = 正则化 MRC"

- [ ] **Step 1: 写讲义正文**

章节结构与要点：
1. `## 本节学习目标`：intro 从"一条链路深衰落就断，多天线为什么更稳"切入；bullets：解释分集收益来源（独立拷贝）；推导 MRC 合并与 SNR_out=‖h‖²/σ²；说明分集阶数与深衰落概率 P(‖h‖²<ε)~ε^N/N!；用 32 天线实例（χ²₆₄、+15 dB、0-6 dB 下 256QAM 可行）说明工程收益；区分分集与波束赋形；说明 MMSE 单层 = 正则化 MRC
2. `## 前置知识检查`：L1 T2.15（衰落与 LLR）、概念笔记 Diversity_Combining、MIMO_多天线系统、T12.1
3. `## 分集：多份独立拷贝`：生活类比（"32 个人分别听同一句话"）；分集阶数定义；为什么独立才有效（相关拷贝不带来阶数）
4. `## MRC 合并推导`：1×N 模型 y=h·x+n（h∈C^N）；加权合并 ŝ=wᴴy；SNR 最大化求解 → w∝h（共轭匹配）；SNR_out=‖h‖²/σ²；χ² 分布说明（‖h‖²~χ²₂ₙ）
5. `## 深衰落概率与分集阶数`：P(‖h‖²<ε) 的渐近 ε^N/N! 推导（χ²₂ₙ 在 0 附近 CDF）；N=1/2/4 对比表（ε=0.01 时概率 5e-3/2.5e-5/2e-8 量级）；"分集让深衰落指数变稀"
6. `## 32 天线实例：从 χ²₆₄ 到 +15 dB`：10log₁₀(32)=15.05 dB 推导；test_simo 场景（1×32、MMSE→MRC、0-6 dB 下 256QAM 可行）；阵列增益 vs 分集收益的区分
7. `## MMSE 单层 = 正则化 MRC`：分母 ‖h‖²+σ² 的由来；深衰落避免除零；衔接 T12.3 线性检测器
8. `## 内嵌验证：深衰落概率蒙特卡洛`（Step 2 代码）
9. `## 小结`：指向 T12.3（线性检测器，MMSE 是 MRC 的多天线矩阵推广）

- [ ] **Step 2: 生成 SVG `T12.2_diversity_combining.svg`**

主题：**分集合并示意**：左侧 N 条独立衰落支路（每条：`h_i` 信道框 + `y_i` 接收符号框，纵向排列 N=4），汇入中间"共轭加权 + 求和"节点（w_i=h_i*），右侧输出 `ŝ` + `SNR_out=‖h‖²/σ²` 标注；顶部或底部加一行"分集阶数 N → 深衰落概率 ε^N/N!"。布局：画布 900×420px；4 条支路纵向间距 ≥ 60px；文字间距 ≥ 8px。执行与 Task 1 Step 2 相同的 Y 扫描 + cairosvg PNG + Read 肉眼检查，证据记入报告。

- [ ] **Step 3: 运行内嵌 numpy 验证**

```python
import numpy as np
rng = np.random.default_rng(2)
print("分集阶数 N 与深衰落概率 P(‖h‖²<ε)：蒙特卡洛 vs 理论渐近 ε^N/(N!·2^N)")
for N in [1, 2, 4]:
    h2 = np.sum(np.abs(rng.standard_normal((N, 1_000_000)))**2, axis=0)
    print(f"N={N}: ", end="")
    for eps in [1e-2, 1e-3]:
        p_sim = np.mean(h2 < eps)
        p_th  = eps**N / (np.math.factorial(N) * 2**N)
        print(f"ε={eps}: 模拟={p_sim:.2e} 渐近={p_th:.2e} 比值={p_sim/p_th:.2f}", end="   ")
    print()
```
预期：比值接近 1（ε 越小越接近；N 越大偏离出现越早属正常渐近效应，讲义中说明）。运行 + 输出记入报告。

- [ ] **Step 4: 结构/行数/死链验证**（同 Task 1 Step 4 命令，文件换为 T12.2）
- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/L2_协议算法/T12.2_diversity_combining_mrc.md 3gpp/docs/L2_协议算法/assets/T12.2_diversity_combining.svg
git commit -m "docs(lectures): T12.2 分集与合并（MRC/分集阶数/蒙特卡洛验证）"
```

---

### Task 3: T12.3 线性检测器 MF/ZF/MMSE

**Files:**
- Create: `3gpp/docs/L2_协议算法/T12.3_linear_detectors_mf_zf_mmse.md`（500-800 行）
- Create: `3gpp/docs/L2_协议算法/assets/T12.3_detector_sinr_comparison.svg`（SVG 图）

**Interfaces:**
- Consumes: T12.1（每 RE 模型）、T12.2（MMSE=正则化 MRC 单层情形）
- Produces: T12.3 讲义；T12.4 引用其 MMSE 基线

- [ ] **Step 1: 写讲义正文**

章节结构与要点：
1. `## 本节学习目标`：bullets：写出 MF/ZF/MMSE 三个滤波公式；解释 σ²→0/∞ 两极限；完成 MMSE 目标函数最小化推导（含 Woodbury 恒等式）；证明 csi≥1 恒成立；解释无偏化归一化（effective_csi/mmse_gain/β=(csi−1)/csi）；说明 0/0 与 ∞ 放大机理与 ±31 裁剪吸收；给定点除法保护写法（csi_safe）
2. `## 前置知识检查`：L1 T2.14（Max-Log-MAP）、T2.16（LLR 裁剪）、概念笔记 MMSE_均衡、Detector_Comparison、T12.1/T12.2
3. `## 线性检测器家族`：生活类比（"四种听法"）；线性滤波 ŝ=Wᴴy 的统一框架；MF/ZF/MMSE 都是 W 的不同选择
4. `## MF 与 ZF：两个极限`：MF ŝ=Hᴴy（σ²→∞ 极限：只有噪声时匹配滤波最优）；ZF ŝ=(HᴴH)⁻¹Hᴴy（σ²→0 极限：完全消干扰、噪声放大 σ²/|h|² 量级）；数值例子表（条件数大的 H 下 ZF 噪声放大）
5. `## MMSE：正则化折中`：J(W)=E‖Wy−x‖² 最小化；Wirtinger 求导（或给出结论 + 直观说明）；W=Hᴴ(HHᴴ+σ²I)⁻¹ 与 Woodbury 等价形式 (HᴴH+σ²I)⁻¹Hᴴ（4×4 而非 32×32）；后验 MSE=σ²(HᴴH+σ²I)⁻¹；csi=1+SINR_out≥1 恒成立（关键下界）
6. `## 无偏化归一化与危险点`：normalize_mmse_demod_input 三步（effective_csi=max(csi−n_var,0)、mmse_gain、ŝ/gain）；β=(csi−1)/csi 偏置；0/0 与 ∞ 放大机理（csi→0）；放大倍率表（2×/11×/101×/1001×）；±31 裁剪吸收（BLER 损失 <0.02 dB）；定点除法保护 `csi_safe = (csi < EPSILON) ? EPSILON : csi`
7. `## 内嵌验证：SINR 对比与 csi≥1`（Step 2 代码）
8. `## 小结`：MMSE 是工程默认；指向 T12.4（Sphere 是更贵的 0 dB 参考）

- [ ] **Step 2: 生成 SVG `T12.3_detector_sinr_comparison.svg`**

主题：**MF/ZF/MMSE 检测器 SINR 对比**（柱状图或点线图）：横轴 SNR（-5 到 15 dB 分 5 点）、纵轴输出 SINR（dB）；三条线/柱：MF（饱和）、ZF（随 SNR 上移但被条件数放大噪声）、MMSE（最上）；图例 + 标注"csi ≥ 1 恒成立"。数据用讲义内验证代码同款配置生成（可先在 python 里算好数据再画 SVG——SVG 数值必须与验证代码输出一致，讲义中说明）。布局：画布 820×460px；坐标轴/刻度/文字间距 ≥ 8px。执行 Y 扫描 + PNG 肉眼检查。

- [ ] **Step 3: 运行内嵌 numpy 验证**

```python
import numpy as np
rng = np.random.default_rng(3)
Nt, Nr, Nl, snr_db = 4, 4, 2, 10.0
H = (rng.standard_normal((Nr, Nt)) + 1j*rng.standard_normal((Nr, Nt)))/np.sqrt(2)
P = np.eye(Nt, Nl, dtype=complex)
H_eff = H @ P
sigma2 = 10**(-snr_db/10)
G_mmse = np.linalg.inv(H_eff.conj().T @ H_eff + sigma2*np.eye(Nl)) @ H_eff.conj().T
csi = 1.0/(sigma2*np.diag(np.linalg.inv(H_eff.conj().T @ H_eff + sigma2*np.eye(Nl))))
assert np.all(csi >= 1.0), "csi ≥ 1 恒成立被违反"
def post_sinr(G, H_eff, sigma2, l):
    w = G[l]
    sig = np.abs(w.conj() @ H_eff[:, l])**2
    interf = sum(np.abs(w.conj() @ H_eff[:, j])**2 for j in range(H_eff.shape[1]) if j != l)
    return sig/(interf + sigma2*np.sum(np.abs(w)**2))
sinr = [post_sinr(G_mmse, H_eff, sigma2, l) for l in range(Nl)]
print("csi(理论 1+SINR):", np.round(csi, 6))
print("实测 SINR+1:     ", np.round(1+np.array(sinr), 6))
print("匹配:", np.allclose(csi, 1+np.array(sinr), rtol=1e-6))
```
预期：csi 全 ≥1、且 csi == 1+SINR_out（MMSE 均衡后恒等式）。运行 + 输出记入报告。

- [ ] **Step 4: 结构/行数/死链验证**（同 Task 1 Step 4，文件换为 T12.3）
- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/L2_协议算法/T12.3_linear_detectors_mf_zf_mmse.md 3gpp/docs/L2_协议算法/assets/T12.3_detector_sinr_comparison.svg
git commit -m "docs(lectures): T12.3 线性检测器 MF/ZF/MMSE（推导/SINR 验证/csi≥1）"
```

---

### Task 4: T12.4 球面检测与检测器选择

**Files:**
- Create: `3gpp/docs/L2_协议算法/T12.4_sphere_detection_detector_selection.md`（500-800 行）
- Create: `3gpp/docs/L2_协议算法/assets/T12.4_sphere_search_tree.svg`（SVG 图）

**Interfaces:**
- Consumes: T12.3（MMSE 基线）、T12.1（每 RE 模型）
- Produces: T12.4 讲义；T12.5 引用检测器输出→LLR 路径

- [ ] **Step 1: 写讲义正文**

章节结构与要点：
1. `## 本节学习目标`：bullets：写 ML 检测问题与穷举复杂度 2^(Qm·Nlayers)；解释半径约束 ‖y−Hs‖²≤r²；画 QR 树搜索的分层累加与剪枝；对比 FP 与 SE 枚举策略；说明白化（y/√n_var、H/√n_var）与 LLR 符号约定；解释低 SNR 复杂度爆炸；给出三检测器对比表（复杂度/性能/面积/适用域）
2. `## 前置知识检查`：L1 T2.14、概念笔记 Sphere_Decoding、Detector_Comparison、T12.1/T12.3
3. `## ML 检测：精确但昂贵`：argmin‖y−Hs‖²；候选数 2^(Qm·Nlayers)（256QAM×4=2³² 不可穷举）；生活类比（"把所有组合试一遍"）
4. `## 半径约束与 QR 树搜索`：‖y−Hs‖²≤r² 的几何含义（球内格点）；QR 分解 y=Qz：‖Qᴴy−Rs‖² 上三角结构；逐层部分距离累加、深度优先、r 随最优解收缩；剪枝条件（部分距离已超 r 即剪）
5. `## FP 与 SE：两种枚举策略`：Fincke-Pohst（按星座顺序区间枚举、半径收缩慢）vs Schnorr-Euchner（按部分距离从小到大展开、平均快 2-3 倍）；comm.SphereDecoder 为 SE 类
6. `## 白化与 LLR 符号约定`：检测前 y/√n_var、H/√n_var（内嵌 σ²，无需 CSI 加权）；Sphere 解码器 LLR 符号与 NR 约定相反需 ×(−1)；纯实数输入需 complex() 强转
7. `## 低 SNR 复杂度爆炸`：球半径需覆盖 χ² 噪声能量 → 低 SNR 球内格点 ∝(r²/σ²)^Nlayers 爆炸 → 退化穷举；"仅高 SNR 使用"的工程结论
8. `## 三检测器对比与选择`：对比表（MMSE 4×4：~100 MACs/tone、~95K gates、20 cycles/tone、1-3 dB 损失；Sphere：~100-1000 MACs、~150K gates、50-500 cycles/tone、0 dB、仅高 SNR）；选择准则（场景/硬件预算/延迟确定性）
9. `## 内嵌验证：剪枝与穷举一致性`（Step 2 代码）
10. `## 小结`：Sphere 是 ML 参考；指向 T12.5（估计误差如何破坏检测前提）

- [ ] **Step 2: 生成 SVG `T12.4_sphere_search_tree.svg`**

主题：**2×2 QPSK QR 树搜索示意**：树形图——根节点 → 第一层 4 个节点（s0 候选，标注部分距离 d1）→ 第二层每个子节点 4 个叶子（s1 候选，标注累积距离 d1+d2）；被剪枝的叶子用虚线/灰显 + "pruned: d1>r²" 标注；最优路径高亮。布局：画布 900×520px；层间垂直间距 ≥ 90px、同层节点水平间距 ≥ 30px；文字间距 ≥ 8px。执行 Y 扫描 + PNG 肉眼检查。

- [ ] **Step 3: 运行内嵌 numpy 验证**

```python
import numpy as np
rng = np.random.default_rng(4)
Nl = 2
QPSK = np.array([1+1j, 1-1j, -1+1j, -1-1j])/np.sqrt(2)
H = (rng.standard_normal((2, Nl)) + 1j*rng.standard_normal((2, Nl)))/np.sqrt(2)
def ml_detect(y):
    best, dmin = None, np.inf
    for s0 in QPSK:
        for s1 in QPSK:
            s = np.array([s0, s1]); d = np.sum(np.abs(y - H@s)**2)
            if d < dmin: dmin, best = d, s
    return best, dmin
def prune_detect(y, r2):
    best, dmin = None, np.inf
    for s0 in QPSK:
        partial = np.abs(y[0] - (H[0,0]*s0 + H[0,1]*QPSK))**2   # 第一层部分距离
        for k, s1 in enumerate(QPSK):
            if partial[k] > r2: continue                          # 剪枝：部分距离已超半径
            s = np.array([s0, s1]); d = np.sum(np.abs(y - H@s)**2)
            if d < dmin: dmin, best = d, s
    return best, dmin
for trial in range(200):
    x = QPSK[rng.integers(0, 4, Nl)]
    y = H @ x + 0.1*(rng.standard_normal(2) + 1j*rng.standard_normal(2))/np.sqrt(2)
    s_ml, d_ml = ml_detect(y)
    s_pr, d_pr = prune_detect(y, d_ml)          # r² = 穷举最优距离 → 必含 ML 解
    assert np.all(s_ml == s_pr) and abs(d_ml - d_pr) < 1e-12, f"trial {trial} 不一致"
print("200 次随机实例：半径剪枝枚举与穷举 ML 结果完全一致 ✓")
```
预期：打印"完全一致 ✓"（无 AssertionError）。运行 + 输出记入报告。

- [ ] **Step 4: 结构/行数/死链验证**（同 Task 1 Step 4，文件换为 T12.4）
- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/L2_协议算法/T12.4_sphere_detection_detector_selection.md 3gpp/docs/L2_协议算法/assets/T12.4_sphere_search_tree.svg
git commit -m "docs(lectures): T12.4 球面检测与检测器选择（QR 树/剪枝一致性验证）"
```

---

### Task 5: T12.5 信道估计与 LLR 可靠度

**Files:**
- Create: `3gpp/docs/L2_协议算法/T12.5_channel_estimation_llr_reliability.md`（500-800 行）
- Create: `3gpp/docs/L2_协议算法/assets/T12.5_ls_wiener_mse.svg`（SVG 图）

**Interfaces:**
- Consumes: T12.3（无偏化归一化、CSI 加权）、T12.1（H_eff）
- Produces: T12.5 讲义（系列收尾篇）

- [ ] **Step 1: 写讲义正文**

章节结构与要点：
1. `## 本节学习目标`：bullets：区分完美估计与实际估计（DMRS-based）；写 LS 估计与噪声放大 1/|X|²；写维纳滤波 Ĥ=R(R+σ²I)⁻¹Ĥ_LS 并说明低 SNR 优势与 O(N³) 代价；列举估计误差三途径（均衡偏置/CSI 失真/噪声方差失配）与 256QAM 0.08 翻转实例；说明 DMRS 走预编码→H_eff 直接估计；解释 CSI 加权 LLR×csi 与 ±31 裁剪的误差预算衔接
2. `## 前置知识检查`：L1 T2.16（LLR 裁剪）、概念笔记 Channel_Estimation、CSI_SINR、T12.1/T12.3
3. `## 完美估计：仿真的上界`：nrPerfectChannelEstimate 由 path_gains/path_filters 合成零误差；上界参考用途；n_var=mean(|noise_grid|²) 实测噪声方差
4. `## DMRS 实际估计：LS 与维纳滤波`：生活类比（"用已知尺子量地形"——与概念笔记一致但展开）；LS Ĥ_LS=Y_DMRS/X_DMRS 推导与噪声放大 1/|X|²；维纳滤波 Ĥ=R_HH(R_HH+σ²I)⁻¹Ĥ_LS（利用信道统计先验）；低 SNR 显著优、高 SNR 趋同；O(N_DMRS³) 代价；DMRS type1 配置与开销（12 RE/PRB、7.14%）
5. `## 估计误差三途径`：均衡输出偏置（ĤW≠I）、CSI 失真（过度自信/保守）、噪声方差失配；256QAM d_min≈0.16、偏移超 0.08 硬判决翻转的数值实例
6. `## DMRS 走预编码：H_eff 直接估计`：DMRS 层域插入后与数据同乘 P；DMRS-based 估计直接给 H_eff；接收机无需知道 P（衔接 T12.1）
7. `## CSI 加权与误差预算`：LLR_out=LLR×csi（逐 RE 可靠度）；sphere 路径不再乘 csi（已含 σ² 内嵌）；±31 裁剪吸收归一化放大；估计误差进入译码器输入可靠度（衔接 L1 T2.16/T2.15）
8. `## 内嵌验证：LS vs 维纳滤波 MSE`（Step 2 代码）
9. `## 小结`：系列收束——接收链路全图回顾（T12.1→T12.5），指向下一系列（概率整形算法系列，规划中）

- [ ] **Step 2: 生成 SVG `T12.5_ls_wiener_mse.svg`**

主题：**LS vs 维纳滤波估计 MSE 曲线**：横轴 SNR（-5 到 20 dB）、纵轴 MSE（dB 或对数刻度）；两条曲线：LS（直线，MSE=σ²，斜率 -1）与维纳（低 SNR 显著低于 LS、高 SNR 收敛到 LS）；图例 + "低 SNR 维纳优势区"阴影标注。数据必须与 Step 3 验证代码输出一致（先在 python 里算好再画）。布局：画布 820×460px；文字/刻度间距 ≥ 8px。执行 Y 扫描 + PNG 肉眼检查。

- [ ] **Step 3: 运行内嵌 numpy 验证**

```python
import numpy as np
rng = np.random.default_rng(5)
snr_db = np.arange(-5, 21, 5)
N_dmrs = 12
print("LS vs 维纳滤波信道估计 MSE（12 个 DMRS 子载波，单位功率信道）：")
for snr in snr_db:
    sigma2 = 10**(-snr/10)
    H_true = (rng.standard_normal(N_dmrs) + 1j*rng.standard_normal(N_dmrs))/np.sqrt(2)
    X = np.ones(N_dmrs, dtype=complex)
    n = np.sqrt(sigma2/2)*(rng.standard_normal(N_dmrs) + 1j*rng.standard_normal(N_dmrs))
    Y = H_true*X + n
    H_ls = Y/X
    R = np.eye(N_dmrs)
    H_w  = R @ np.linalg.inv(R + sigma2*np.eye(N_dmrs)) @ H_ls
    mse_ls = np.mean(np.abs(H_ls - H_true)**2)
    mse_w  = np.mean(np.abs(H_w  - H_true)**2)
    print(f"SNR={snr:3d} dB: LS={mse_ls:.4f} (≈σ²={sigma2:.4f})  维纳={mse_w:.4f}  改善={10*np.log10(mse_ls/mse_w):.2f} dB")
```
预期：LS MSE ≈ σ²（随 SNR 单调降）；维纳改善在低 SNR 大（-5 dB 时 >5 dB）、高 SNR 趋近 0 dB（与讲义断言一致）。运行 + 输出记入报告。

- [ ] **Step 4: 结构/行数/死链验证**（同 Task 1 Step 4，文件换为 T12.5）
- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/L2_协议算法/T12.5_channel_estimation_llr_reliability.md 3gpp/docs/L2_协议算法/assets/T12.5_ls_wiener_mse.svg
git commit -m "docs(lectures): T12.5 信道估计与 LLR 可靠度（LS/维纳/MSE 验证）"
```

---

### Task 6: L2 入口 M12 章节 + 概念笔记回链 + 全量校验

**Files:**
- Modify: `3gpp/docs/L2_协议算法/L2_协议算法入口.md`（M11 之后新增 M12 章节）
- Modify: `3gpp/docs/concepts/Detector_Comparison_检测器对比.md`、`Diversity_Combining_分集与合并.md`、`Channel_Estimation_信道估计.md`、`MMSE_均衡.md`、`Sphere_Decoding_球面检测.md`、`CSI_SINR.md`（各加 1-2 条讲义回链）

**Interfaces:**
- Consumes: Task 1-5 的 5 个文件名（即链接名）

- [ ] **Step 1: L2 入口加 M12 章节**

在 `## M11 LTE/NR 译码对比` 章节末尾之后新增（格式与既有模块一致）：
```markdown
## M12 MIMO 接收机与检测器

- [[T12.1_mimo_receiver_chain_overview]]
- [[T12.2_diversity_combining_mrc]]
- [[T12.3_linear_detectors_mf_zf_mmse]]
- [[T12.4_sphere_detection_detector_selection]]
- [[T12.5_channel_estimation_llr_reliability]]
```

- [ ] **Step 2: 概念笔记回链（6 篇各 1 条）**

在对应笔记的 图谱关联 列表中追加（链接名 = 讲义文件名）：
- `Detector_Comparison_检测器对比.md`：`- [[T12.3_linear_detectors_mf_zf_mmse]]`、`- [[T12.4_sphere_detection_detector_selection]]`
- `Diversity_Combining_分集与合并.md`：`- [[T12.2_diversity_combining_mrc]]`
- `Channel_Estimation_信道估计.md`：`- [[T12.5_channel_estimation_llr_reliability]]`
- `MMSE_均衡.md`：`- [[T12.3_linear_detectors_mf_zf_mmse]]`
- `Sphere_Decoding_球面检测.md`：`- [[T12.4_sphere_detection_detector_selection]]`
- `CSI_SINR.md`：`- [[T12.5_channel_estimation_llr_reliability]]`
（仅追加，不动存量行；若某篇已是六段式合规文件则插在 `- 关系语义：…` 行之前）

- [ ] **Step 3: 全量校验**

```bash
# (1) 死链（L2 新增 5 篇 + concepts 全部）
grep -oE "\[\[[^]]+\]\]" 3gpp/docs/L2_协议算法/T12*.md 3gpp/docs/concepts/*.md | sed 's/.*\[\[//;s/\]\].*//;s/|.*//' | sort -u | while read -r l; do
  find 3gpp -name "${l}.md" | grep -q . || echo "DEAD: $l"; done; echo "link scan done"
# (2) 5 篇行数
wc -l 3gpp/docs/L2_协议算法/T12*.md
# (3) 5 个 SVG 全部存在
ls -la 3gpp/docs/L2_协议算法/assets/T12.*.svg
# (4) 入口 M12 章节
grep -n "M12" 3gpp/docs/L2_协议算法/L2_协议算法入口.md
```
预期：仅输出 link scan done（无 DEAD）、行数各 500-800、5 个 SVG 存在、M12 章节在位。

- [ ] **Step 4: Commit**

```bash
git add 3gpp/docs/L2_协议算法/L2_协议算法入口.md 3gpp/docs/concepts/Detector_Comparison_检测器对比.md 3gpp/docs/concepts/Diversity_Combining_分集与合并.md 3gpp/docs/concepts/Channel_Estimation_信道估计.md 3gpp/docs/concepts/MMSE_均衡.md 3gpp/docs/concepts/Sphere_Decoding_球面检测.md 3gpp/docs/concepts/CSI_SINR.md
git commit -m "docs(lectures): L2 入口 M12 章节与概念笔记回链"
```

---

## Self-Review（编写者自查）

1. **Spec 覆盖**：5 篇篇目/锚点 → Task 1-5；每篇 500-800 行 + ≥1 SVG（强制视觉验证）+ 1 内嵌 numpy → 各任务 Step 1-3；L2 入口 M12 → Task 6 Step 1；概念笔记回链 → Task 6 Step 2；验收 1-8 条 → 各任务验证步骤 + Task 6 Step 3 ✓
2. **占位符扫描**：无 TBD/TODO；每篇章节要点、SVG 规格、numpy 代码均完整给出 ✓
3. **类型一致性**：文件名（T12.1-T12.5）在 Task 1-5 创建与 Task 6 入口/回链中完全一致；SVG 文件名与讲义引用一致；numpy 代码在讲义与验证步骤中一致（Task 3/5 的 SVG 数据来源引用对应验证代码）✓
4. **SVG 规则**：每个含 SVG 的任务都包含 Y 扫描命令 + cairosvg PNG + Read 肉眼检查，符合 CLAUDE.md 第 4 条与 spec 验收 2 ✓
