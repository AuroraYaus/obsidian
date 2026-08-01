/**
 * @file    build_t2_t3_overview.js
 * @brief   Generate a ~32-slide PPT covering 3GPP T2.1–T3.5 lessons
 * @date    2026-07-25
 * @usage   node build_t2_t3_overview.js
 * @output  ~/Downloads/3GPP_T2_T3_Overview.pptx
 */

const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");
const os = require("os");

// ============================================================
// Color palette: Ocean Gradient
// ============================================================
const C = {
  navy:     "065A82",
  teal:     "1C7293",
  midnight: "21295C",
  white:    "FFFFFF",
  offWhite: "F4F7FA",
  lightBlue:"D6E8F0",
  accent:   "F39C12",
  red:      "C0392B",
  green:    "27AE60",
  gray:     "7F8C8D",
  darkGray: "2C3E50",
  black:    "1A1A1A",
};

// ============================================================
// Helpers
// ============================================================
function imgBase64(filePath) {
  const buf = fs.readFileSync(filePath);
  return `image/png;base64,${buf.toString("base64")}`;
}

function addContentSlide(pres, title, contentFn) {
  const s = pres.addSlide();
  s.background = { fill: C.white };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.9, fill: { color: C.navy } });
  s.addText(title, { x: 0.5, y: 0.1, w: 9, h: 0.7, fontSize: 22, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.85, w: 2, h: 0.04, fill: { color: C.accent } });
  contentFn(s);
  return s;
}

function addSectionSlide(pres, title, number) {
  const s = pres.addSlide();
  s.background = { fill: C.midnight };
  s.addText(number, { x: 0.5, y: 1.0, w: 2, h: 1.2, fontSize: 64, fontFace: "Arial Black", color: C.accent, margin: 0 });
  s.addText(title, { x: 0.5, y: 2.4, w: 9, h: 1.2, fontSize: 32, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.8, w: 1.5, h: 0.06, fill: { color: C.accent } });
  return s;
}

function nestedBullets(main, sub) {
  const result = [];
  result.push({ text: main, options: { bullet: true, breakLine: true, indentLevel: 0, fontSize: 15, fontFace: "Calibri", color: C.black, bold: true } });
  sub.forEach((t, i) => {
    result.push({ text: t, options: { bullet: true, breakLine: i < sub.length - 1, indentLevel: 1, fontSize: 13, fontFace: "Calibri", color: C.darkGray } });
  });
  return result;
}

// ============================================================
// Main
// ============================================================
function main() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "3GPP Project";
  pres.title = "3GPP LTE/NR 译码链路：从软信息到码块分段";

  // ====== Slide 1: Cover ======
  {
    const s = pres.addSlide();
    s.background = { fill: C.midnight };
    s.addText("3GPP LTE/NR 译码链路", { x: 0.5, y: 1.2, w: 9, h: 1.2, fontSize: 44, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
    s.addText("从软信息生成到码块分段", { x: 0.5, y: 2.5, w: 9, h: 0.8, fontSize: 28, fontFace: "Calibri Light", color: C.accent, margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.5, w: 2, h: 0.06, fill: { color: C.accent } });
    s.addText("T2.1 AWGN → T3.5 NR Polar 分段", { x: 0.5, y: 3.8, w: 9, h: 0.5, fontSize: 14, fontFace: "Calibri", color: C.lightBlue, margin: 0 });
    s.addText("10 篇讲义 · 3 大模块 · 32 页幻灯片", { x: 0.5, y: 4.3, w: 9, h: 0.5, fontSize: 14, fontFace: "Calibri", color: C.gray, margin: 0 });
  }

  // ====== Slide 2: Agenda ======
  addContentSlide(pres, "课程路线图", (s) => {
    const mods = [
      { title: "模块一：软信息生成", sub: "T2.1 AWGN 噪声缩放 → T2.5 LLR 量化", color: C.teal },
      { title: "模块二：错误检测", sub: "T3.1 CRC 家族：TB CRC / CB CRC / 控制信息 CRC", color: C.accent },
      { title: "模块三：码块分段", sub: "T3.2 TB/CB/filler 框架 → T3.5 NR Polar", color: C.navy },
    ];
    mods.forEach((m, i) => {
      const yBase = 1.3 + i * 1.3;
      s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: yBase, w: 0.15, h: 0.8, fill: { color: m.color } });
      s.addText(m.title, { x: 0.9, y: yBase, w: 8, h: 0.45, fontSize: 20, fontFace: "Arial Black", color: C.black, bold: true, margin: 0 });
      s.addText(m.sub, { x: 0.9, y: yBase + 0.45, w: 8, h: 0.35, fontSize: 13, fontFace: "Calibri", color: C.gray, margin: 0 });
    });
  });

  // ====== Module 1: 软信息生成 ======
  addSectionSlide(pres, "模块一：软信息生成", "01");

  // T2.1 (2 slides)
  addContentSlide(pres, "T2.1 AWGN 信道与噪声缩放", (s) => {
    s.addText([
      ...nestedBullets("AWGN 信道模型四要素", [
        "A (Additive): 噪声叠加在信号上, 不乘性改变信号幅度",
        "W (White): 功率谱密度平坦, 任意两时刻的噪声样本独立",
        "G (Gaussian): 噪声幅度服从高斯分布, 热噪声的自然模型",
        "N (Noise): 接收端无法消除的随机干扰",
      ]),
      ...nestedBullets("核心指标转换链", [
        "Eb/N0 (每信息比特信噪比) → Es/N0 (每符号信噪比) → SNR",
        "关键桥梁: Es/N0 = Eb/N0 + 10log10(R × Qm) [dB]",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T2.1 BPSK LLR 推导与噪声失配", (s) => {
    s.addText([
      ...nestedBullets("BPSK 下的 LLR 精确公式", [
        "发送: x ∈ {+1, -1}, 接收: y = x + n, n ~ N(0, σ²)",
        "LLR = ln[P(x=+1|y)/P(x=-1|y)] = 2y/σ²",
        "LLR 符号 = 硬判决方向, |LLR| 大小 = 判决置信度",
      ]),
      ...nestedBullets("噪声方差失配的影响", [
        "σ² 低估 → LLR 幅度偏大 → 译码器过度自信 → 误码平台升高",
        "σ² 高估 → LLR 幅度偏小 → 译码器保守 → 纠错能力未充分发挥",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // T2.2 (2 slides)
  addContentSlide(pres, "T2.2 BPSK 与 QPSK 软解调", (s) => {
    s.addText([
      ...nestedBullets("BPSK 一维星座与精确 LLR", [
        "星座点: s0=+1 (bit 0), s1=-1 (bit 1)",
        "LLR = 2y/σ²",
      ]),
      ...nestedBullets("QPSK 二维星座与 Gray 映射", [
        "4 个星座点: 00/01/11/10 (Gray 编码, 相邻点仅 1 bit 不同)",
        "I/Q 两路独立: QPSK = 2 个正交 BPSK",
        "逐比特 LLR: I 路承载 bit 0, Q 路承载 bit 1, 各自独立计算",
        "Gray 映射收益: 误判为相邻点时只错 1 bit",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T2.2 硬判决 vs 软判决", (s) => {
    s.addText([
      ...nestedBullets("硬判决 (Hard Decision) — 信息损失", [
        "解调器输出: 0 或 1, 丢失置信度信息",
        "译码器看不到\"这个 bit 是 1 有 95% 可能还是 51%\"",
      ]),
      ...nestedBullets("软判决 (Soft Decision) — 保留全部信息", [
        "解调器输出: LLR (连续值), 符号=方向, 幅度=可信度",
        "Turbo/LDPC/Polar 译码器均依赖软信息做迭代置信度传播",
        "软判决相比硬判决的编码增益: 约 2 dB (AWGN, BER=10⁻⁵)",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // T2.3 (2 slides)
  addContentSlide(pres, "T2.3 QAM 软解调与 Max-Log-MAP", (s) => {
    s.addText([
      ...nestedBullets("16QAM — 4 bits 映射到 16 个星座点", [
        "I/Q 各 4 级幅度: PAM-4 × PAM-4 = 16QAM",
        "精确 LLR: 对 bit=0 和 bit=1 的所有星座点分别求和",
      ]),
      ...nestedBullets("Max-Log-MAP 近似 (复杂度降低关键)", [
        "log(∑e^xi) ≈ max(xi) — 用最大项代替全求和",
        "LLR ≈ [min dist² to bit=1] - [min dist² to bit=0], 再除以 2σ²",
        "近似误差通常 < 0.1 dB, 工程上广泛使用",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T2.3 16QAM 手算示例", (s) => {
    s.addText([
      ...nestedBullets("Gray-mapped 16QAM: I/Q 独立 PAM-4", [
        "I 路电平: [-3, -1, +1, +3] 对应 bits [00, 01, 11, 10]",
        "Q 路电平: [-3, -1, +1, +3] 对应 bits [00, 01, 11, 10]",
        "bit 0,1 由 I 路决定; bit 2,3 由 Q 路决定",
      ]),
      ...nestedBullets("接收端收到 y_I = 0.5, σ² = 1.0", [
        "bit 0 LLR: 最近 bit0=0 点 I=+1 dist²=0.25; bit0=1 点 I=-1 dist²=2.25",
        "LLR(bit0) = (2.25-0.25)/2 = 1.0 → 倾向 bit0=0, 置信度中等",
        "bit 1 LLR: 最近 bit1=0 点 I=+1 dist²=0.25; bit1=1 点 I=+3 dist²=6.25",
        "LLR(bit1) = (6.25-0.25)/2 = 3.0 → 强烈倾向 bit1=0",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // T2.4 (1 slide)
  addContentSlide(pres, "T2.4 衰落信道与 LLR 可靠度", (s) => {
    s.addText([
      ...nestedBullets("平坦衰落信道: y = hx + n", [
        "h: 信道系数 (复数), |h| 表示瞬时信道增益",
        "LLR = (2/σ²) × Re{h*y} (BPSK), LLR 幅度 ∝ 信道增益",
        "深衰落 (|h| 小) → LLR 接近 0 → 这个 bit \"不可信\"",
      ]),
      ...nestedBullets("均衡输出的幅度 = 可信度", [
        "MMSE/ZF 均衡后每个 LLR 的有效 SNR ∝ |h|²",
        "译码器可利用 CSI 对不同 bit 赋予不同权重",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // T2.5 (1 slide)
  addContentSlide(pres, "T2.5 LLR 裁剪、缩放与量化", (s) => {
    s.addText([
      ...nestedBullets("浮点 LLR → 定点译码器 (三个关键操作)", [
        "裁剪: 限制 LLR 幅度范围, 防止极端值溢出",
        "缩放: 调节动态范围以匹配定点位宽",
        "量化: 连续值 → 离散整数 (通常 4-8 bit)",
      ]),
      ...nestedBullets("量化精度 vs 硬件代价", [
        "8-bit LLR: 接近浮点性能, 仿真参考",
        "6-bit LLR: 工业主流, 损失 < 0.1 dB",
        "4-bit LLR: 低功耗场景, 损失 0.3-0.5 dB",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // ====== Module 2: CRC ======
  addSectionSlide(pres, "模块二：错误检测 — CRC", "02");

  addContentSlide(pres, "T3.1 LTE/NR CRC 家族", (s) => {
    s.addText([
      ...nestedBullets("CRC 在编码链路中的角色", [
        "CRC ≠ 前向纠错: CRC 只检测错误, 不纠正错误",
        "TB CRC: 分段前附加, 整包最终交付验收",
        "CB CRC: 分段后给每个码块附加, 支持局部验收和早停",
        "控制信息 CRC: UCI/DCI 各用不同多项式",
      ]),
      ...nestedBullets("双层防御: TB CRC + CB CRC", [
        "CB CRC 通过 → 局部码块大概率正确",
        "TB CRC 通过 → 整包最终验收 (捕获拼接/填充位错误)",
        "仅检查 CB CRC 而不查 TB CRC 是最常见工程错误之一",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.1 CRC 多项式与长度对比", (s) => {
    const rows = [
      ["名称", "位数", "多项式 (部分项)", "用途"],
      ["CRC24A", "24", "x²⁴+x²³+x¹⁸+x¹⁷+x¹⁴+x¹¹+...", "LTE TB CRC / NR TB CRC"],
      ["CRC24B", "24", "x²⁴+x²³+x⁶+x⁵+x+1", "LTE/NR CB CRC"],
      ["CRC24C", "24", "x²⁴+x²³+x²¹+x²⁰+x¹⁷+...", "NR DCI CRC"],
      ["CRC16",  "16", "x¹⁶+x¹²+x⁵+1", "NR 短 TB CRC"],
      ["CRC11",  "11", "x¹¹+x¹⁰+x⁹+x⁵+1", "NR UCI 短块 CRC"],
      ["CRC6",   "6",  "x⁶+x⁵+1", "NR UCI 极短块 CRC"],
    ];
    s.addText("LTE/NR CRC 家族一览", { x: 0.5, y: 1.1, w: 9, h: 0.4, fontSize: 16, fontFace: "Arial Black", color: C.navy, bold: true, margin: 0 });
    s.addTable(rows, {
      x: 0.3, y: 1.7, w: 9.4, colW: [1.0, 0.7, 3.8, 3.9],
      border: { type: "solid", pt: 0.5, color: C.lightBlue },
      fontFace: "Calibri", fontSize: 11, color: C.darkGray,
      rowH: 0.34, autoPage: false,
    });
  });

  // ====== Module 3: 码块分段 ======
  addSectionSlide(pres, "模块三：码块分段 (T3.2–T3.5)", "03");

  // T3.2 (5 slides)
  addContentSlide(pres, "T3.2 TB / CB / Filler 概念框架", (s) => {
    s.addText([
      ...nestedBullets("三个核心对象", [
        "TB (传输块): 物理层一次编码传输的数据单位, 来自 MAC 层",
        "CB (码块): TB 附加 CRC 后按协议规则分出的子块",
        "Filler Bit: 使块长满足编码器合法长度的占位, 非业务数据",
      ]),
      ...nestedBullets("分段原因", [
        "编码器/译码器有最大块长限制 (LTE Turbo: Z=6144)",
        "大块带来存储、时延和并行实现压力",
        "CB CRC 提供局部验收, 支持并行译码",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.2 协议处理链", (s) => {
    s.addText([
      ...nestedBullets("发送端: MAC TB → TB CRC → CB 分段 → CB CRC → 编码 → 速率匹配 → 调制", []),
      ...nestedBullets("接收端: LLR → 解速率匹配 → 各 CB 译码 → CB CRC → 去 filler/CRC → 拼接 → TB CRC", []),
      ...nestedBullets("关键协议: LTE TS 36.212 §5.1.2 | NR TS 38.212 §5.2.2 (LDPC) / §5.2.1 (Polar)", []),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.2 Table 5.1.3-3 与码块长度边界", (s) => {
    s.addText([
      ...nestedBullets("Table 5.1.3-3: Turbo 内部交织器参数表 (188 个离散 K 值)", [
        "列含义: i(序号), K(合法块长, 40~6144), f1/f2(交织器二次置换参数)",
        "交织公式: Π(i) = (f1·i + f2·i²) mod K",
      ]),
      ...nestedBullets("两个边界: 40 与 6144", [
        "6144: Table 5.1.3-3 最大 K, §5.1.2 硬性最大值 Z=6144",
        "40: Table 5.1.3-3 最小 K, B<40 需补 filler",
        "40 和 6144 限制的是硬比特数量, 非 LLR 个数",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.2 Trellis Termination (网格终止)", (s) => {
    const img = imgBase64("/tmp/T3.2_trellis_termination_shuffle.png");
    s.addImage({ data: img, x: 0.2, y: 1.1, w: 9.6, h: 3.2 });
    s.addText("Turbo 网格终止 → 12个尾比特经跨流重排填入4个输出位置 | 非咬尾卷积",
      { x: 0.5, y: 4.4, w: 9, h: 0.5, fontSize: 11, fontFace: "Calibri", color: C.gray, margin: 0 });
    s.addText([
      { text: "关键: ", options: { bold: true, color: C.red } },
      { text: "Trellis termination 强制归零 → 译码器确知终止状态 → 后向 β 证据链完整 → 消除尾部污染扩散。非 tail-biting (咬尾卷积)。", options: { color: C.darkGray } },
    ], { x: 0.5, y: 4.8, w: 9, h: 0.5, fontSize: 11, fontFace: "Calibri", margin: 0 });
  });

  addContentSlide(pres, "T3.2 Circular Buffer 与速率匹配", (s) => {
    const img = imgBase64("/tmp/T3.2_circular_buffer_decision3.png");
    s.addImage({ data: img, x: 0.3, y: 1.0, w: 9.4, h: 4.1 });
    s.addText([
      { text: "Kw=3KΠ 的环形缓冲区: ", options: { bold: true, color: C.navy } },
      { text: "系统流+两路 parity 流融合为环。E<Kw 时打孔, E>Kw 时重复 — 同一环形结构, 两种速率匹配策略。", options: { color: C.darkGray } },
    ], { x: 0.5, y: 5.2, w: 9, h: 0.3, fontSize: 11, fontFace: "Calibri", margin: 0 });
  });

  // T3.3 (3 slides)
  addContentSlide(pres, "T3.3 LTE Turbo 分段 — 核心公式", (s) => {
    s.addText([
      ...nestedBullets("分段触发 (TB CRC 后长度 B, 最大 CB 大小 Z=6144)", [
        "B ≤ Z → C=1, L=0 | B > Z → L=24, C = ceil(B/(Z-L))",
      ]),
      ...nestedBullets("合法码块长度选择 (查 Table 5.1.3-3)", [
        "B' = B + C·L | K+ = min{K: C·K ≥ B'} | K- = max{K: K < K+}",
        "C- = floor((C·K+ - B')/(K+ - K-)), C+ = C - C-",
        "F = C+·K+ + C-·K- - B'",
      ]),
      ...nestedBullets("约定", [
        "前 C- 个 CB 用 K- (短块在前), 后 C+ 个 CB 用 K+ (长块在后)",
        "Filler 在 CB0 开头, 编码器输入 <NULL>",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.3 手算例子对比", (s) => {
    const rows = [
      ["参数", "B=6145 (边界触发)", "B=10001 (通用分段)"],
      ["C / L", "2 / 24", "2 / 24"],
      ["B'", "6193", "10049"],
      ["K+ / K-", "3136 / 3072", "5056 / 4992"],
      ["C- / C+", "1 / 1", "0 / 2"],
      ["F (filler)", "15", "63"],
      ["CB 布局", "CB0:3072(filler15), CB1:3136", "均 5056 (filler63 在 CB0)"],
    ];
    s.addText("LTE Turbo 两个分段手算例子", { x: 0.5, y: 1.1, w: 9, h: 0.4, fontSize: 16, fontFace: "Arial Black", color: C.navy, bold: true, margin: 0 });
    s.addTable(rows, {
      x: 0.3, y: 1.7, w: 9.4, colW: [1.5, 3.3, 4.6],
      border: { type: "solid", pt: 0.5, color: C.lightBlue },
      fontFace: "Calibri", fontSize: 12, color: C.darkGray, rowH: 0.34, autoPage: false,
    });
  });

  addContentSlide(pres, "T3.3 接收端并行译码与 CB 描述符", (s) => {
    s.addText([
      ...nestedBullets("并行译码流程", [
        "解速率匹配 → 按 CB 描述符切分 LLR → 各 CB 独立 Turbo 译码",
        "→ 各 CB CRC24B 检查 → 按 r 顺序拼接 → 删除 filler → TB CRC24A",
      ]),
      ...nestedBullets("CB 描述符 (硬件接口核心字段)", [
        "cb_id: 拼接排序 (按协议顺序, 非译码完成顺序)",
        "k_len (≤6144): Turbo 译码器长度配置",
        "filler_count: 仅 CB0 非零, 重组时删除",
        "cb_crc_len (0/24): 局部 CRC 检查控制",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // T3.4 (4 slides)
  addContentSlide(pres, "T3.4 NR LDPC 分段 — BG1/BG2", (s) => {
    s.addText([
      ...nestedBullets("基图选择 (§6.2.2/§7.2.2)", [
        "BG1 (46行×68列): 较大净荷或较高码率, N=66Zc",
        "BG2 (42行×52列): 较小净荷或较低码率, N=50Zc",
        "前 2Zc 个系统位置被打孔, rate recovery 需对应处理",
      ]),
      ...nestedBullets("Lifting Size 集合 (Table 5.3.2-1, 8 个 Set)", [
        "Zc ∈ {2~256} ∪ {3~384} ∪ ... ∪ {15~240}",
        "选满足 Kb·Zc ≥ K' 的最小 Zc, 反查 set index(iLS) 定移位系数列",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.4 Table 5.3.2-1 Lifting Size Sets", (s) => {
    const rows = [
      ["0", "{2, 4, 8, 16, 32, 64, 128, 256}"],
      ["1", "{3, 6, 12, 24, 48, 96, 192, 384}"],
      ["2", "{5, 10, 20, 40, 80, 160, 320}"],
      ["3", "{7, 14, 28, 56, 112, 224}"],
      ["4", "{9, 18, 36, 72, 144, 288}"],
      ["5", "{11, 22, 44, 88, 176, 352}"],
      ["6", "{13, 26, 52, 104, 208}"],
      ["7", "{15, 30, 60, 120, 240}"],
    ];
    s.addText("TS 38.212 Table 5.3.2-1", { x: 0.5, y: 1.1, w: 9, h: 0.4, fontSize: 16, fontFace: "Arial Black", color: C.navy, bold: true, margin: 0 });
    s.addTable(rows, {
      x: 0.5, y: 1.7, w: 9, colW: [1.5, 7.5],
      border: { type: "solid", pt: 0.5, color: C.lightBlue },
      fontFace: "Calibri", fontSize: 13, color: C.darkGray, rowH: 0.36, autoPage: false,
    });
  });

  addContentSlide(pres, "T3.4 NR LDPC 核心公式与手算", (s) => {
    s.addText([
      ...nestedBullets("分段公式", [
        "C = ceil(B/(Kcb-L)) 当 B > Kcb (Kcb=8448(BG1)/3840(BG2))",
        "K' = B'/C, Zc = min{Z: Kb·Z ≥ K'}, K = 22Zc(BG1) 或 10Zc(BG2)",
        "F = K - K' (每个 CB 尾部 filler)",
      ]),
      ...nestedBullets("BG1 手算: B=10024, C=1, Kb=22", [
        "K' = 10024, 需要 22Zc ≥ 10024 → Zc 最小 456? 不, 从表中选",
        "查 Table 5.3.2-1: Zc=480? 表最大为 384 → B>Kcb, C=2, 分段处理",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.4 NR LDPC vs LTE Turbo Filler 位置对比", (s) => {
    const rows = [
      ["对比项", "LTE Turbo", "NR LDPC"],
      ["filler 所在 CB", "仅第 0 个 CB", "每个 CB 都可能"],
      ["在 CB 内的位置", "开头 (前 F 个)", "尾部 (K' 之后, K 之前)"],
      ["删除时机", "拼接后删开头", "各 CB 译码后各自删尾部"],
      ["出错后果", "TB 位序整体偏移", "该 CB 局部 CRC 失败"],
      ["结构原因", "K+/K- 之间分配差额", "每个 CB 独立 K-K'"],
    ];
    s.addText("NR LDPC vs LTE Turbo: Filler 位置差异 (关键易错点)", { x: 0.5, y: 1.1, w: 9, h: 0.4, fontSize: 15, fontFace: "Arial Black", color: C.navy, bold: true, margin: 0 });
    s.addTable(rows, {
      x: 0.3, y: 1.7, w: 9.4, colW: [2.0, 3.5, 3.9],
      border: { type: "solid", pt: 0.5, color: C.lightBlue },
      fontFace: "Calibri", fontSize: 12, color: C.darkGray, rowH: 0.4, autoPage: false,
    });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.3, y: 4.5, w: 9.4, h: 0.04, fill: { color: C.red } });
    s.addText("交叉误用: LTE逻辑处理NR → 尾部filler当净荷; NR逻辑处理LTE → CB1数据被误删",
      { x: 0.3, y: 4.7, w: 9.4, h: 0.4, fontSize: 12, fontFace: "Calibri", color: C.red, bold: true, margin: 0 });
  });

  // T3.5 (2 slides)
  addContentSlide(pres, "T3.5 NR Polar — 信道极化", (s) => {
    s.addText([
      ...nestedBullets("信道极化核心", [
        "N=2: W→(W⁻,W⁺), W⁻ 变差, W⁺ 变好 (信息论严格证明)",
        "递归 N=2ⁿ: 合成信道趋向两极 — 近乎完美 vs 近乎无用",
        "K 个信息比特放好位置, N-K 个冻结比特=0",
      ]),
      ...nestedBullets("NR Polar 控制信息特点", [
        "用于 UCI/DCI, 块长有限 (≤1024, UCI≤1706)",
        "始终有 CRC (6/11/24 bit), 嵌入 SCL 路径选择",
        "额外 PC 位辅助 SCL 早停",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  addContentSlide(pres, "T3.5 Polar CRC 辅助 SCL 译码", (s) => {
    s.addText([
      ...nestedBullets("CRC 在 Polar 中的特殊角色", [
        "LTE Turbo/LDPC: CRC 只做译码后错误检测",
        "NR Polar: CRC 嵌入译码 — SCL 用 CRC 筛选 L 条路径中的最终路径",
        "DCI 额外 RNTI 加扰 CRC, 同时做 UE 身份验证",
      ]),
      ...nestedBullets("SCL (Successive Cancellation List) 译码", [
        "逐比特顺序译码, 每信息 bit 分叉 0/1 两条路径",
        "维持 L=8 条候选路径, 各自独立维护 CRC 状态",
        "所有 bit 译完后选第一条通过 CRC 的路径",
      ]),
    ], { x: 0.5, y: 1.2, w: 9, h: 4.0, valign: "top", margin: 0 });
  });

  // ====== 总结 (2 slides) ======
  addSectionSlide(pres, "横向对比与总结", "04");

  addContentSlide(pres, "LTE Turbo vs NR LDPC vs NR Polar 分段对比", (s) => {
    const rows = [
      ["对比项", "LTE Turbo", "NR LDPC", "NR Polar"],
      ["协议", "TS 36.212 §5.1.2", "TS 38.212 §5.2.2", "TS 38.212 §5.2.1"],
      ["编码器约束", "Table 5.1.3-3 离散K", "BG1/BG2 + Zc", "母码 = 2ⁿ (n≤10)"],
      ["最大 CB", "6144", "8448(BG1)/3840(BG2)", "≤1706 (UCI)"],
      ["CB CRC", "C>1 时 L=24", "C>1 时 L=24", "始终有 (6/11/24)"],
      ["filler 位置", "CB0 开头", "每个CB 尾部", "K-K' 差额填充"],
      ["CRC 角色", "错误检测", "错误检测", "嵌入译码(SCL路径选择)"],
      ["并行", "每 CB 独立 (好)", "每 CB 独立 (好)", "单 CB 顺序 (有限)"],
    ];
    s.addTable(rows, {
      x: 0.2, y: 1.1, w: 9.6, colW: [1.5, 2.7, 2.7, 2.7],
      border: { type: "solid", pt: 0.5, color: C.lightBlue },
      fontFace: "Calibri", fontSize: 11, color: C.darkGray, rowH: 0.38, autoPage: false,
    });
  });

  // Final summary
  {
    const s = pres.addSlide();
    s.background = { fill: C.navy };
    s.addText("总结与展望", { x: 0.5, y: 0.8, w: 9, h: 1.0, fontSize: 36, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.8, w: 1.5, h: 0.06, fill: { color: C.accent } });
    const summaries = [
      "T2 (软信息生成): AWGN → QAM/Max-Log-MAP → 衰落/量化 — 译码器输入质量决定性能上限",
      "T3.1 (CRC): TB CRC + CB CRC 双层验收 — 局部检测+整包确认, 6种多项式覆盖全部场景",
      "T3.2-3.5 (分段): Turbo/LDPC/Polar 三种编码器的分段规则各有结构约束, filler 位置和并行策略差异显著",
      "后续 (T4+): 迭代译码、外信息交换、BCJR/MAP、LDPC BP、Polar SCL 等核心算法即将展开",
    ];
    s.addText(summaries.map((t, i) => ({
      text: t,
      options: { bullet: true, breakLine: i < summaries.length - 1, fontSize: 15, fontFace: "Calibri", color: C.lightBlue }
    })), { x: 0.5, y: 2.2, w: 9, h: 3.0, valign: "top", margin: 0 });
  }

  // ====== Write ======
  const outPath = path.join(os.homedir(), "Downloads", "3GPP_T2_T3_Overview.pptx");
  pres.writeFile({ fileName: outPath }).then(() => {
    console.log(`PPT written → ${outPath}`);
    console.log(`Slides: ${pres.slides.length}`);
  });
}

main();
