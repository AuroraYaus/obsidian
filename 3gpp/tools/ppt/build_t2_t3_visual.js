/**
 * @file    build_t2_t3_visual.js
 * @brief   Generate PPT with embedded PDF page screenshots (T2.1-T3.5)
 * @date    2026-07-25
 * @usage   node build_t2_t3_visual.js
 * @output  ~/Downloads/3GPP_T2_T3_Visual.pptx
 */

const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");
const os = require("os");

const SLIDE_DIR = "/tmp/ppt_slides";
const C = {
  navy: "065A82", teal: "1C7293", midnight: "21295C",
  white: "FFFFFF", accent: "F39C12", lightBlue: "D6E8F0",
  gray: "7F8C8D", offWhite: "F4F7FA",
};

function img64(name) {
  const p = path.join(SLIDE_DIR, name);
  return fs.existsSync(p) ? `image/jpeg;base64,${fs.readFileSync(p).toString("base64")}` : null;
}

function addImgSlide(pres, title, imgName) {
  const s = pres.addSlide();
  s.background = { fill: C.white };
  const img = img64(imgName);
  if (img) {
    s.addImage({ data: img, x: 0.2, y: 0.1, w: 9.6, h: 5.1, sizing: { type: "contain", w: 9.6, h: 5.1 } });
  }
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.28, w: 10, h: 0.345, fill: { color: C.navy } });
  s.addText(title, { x: 0.3, y: 5.28, w: 9.4, h: 0.345, fontSize: 11, fontFace: "Calibri", color: C.white, margin: 0 });
}

function addDivider(pres, title, num) {
  const s = pres.addSlide();
  s.background = { fill: C.midnight };
  s.addText(num, { x: 0.5, y: 1.0, w: 3, h: 1.2, fontSize: 60, fontFace: "Arial Black", color: C.accent, margin: 0 });
  s.addText(title, { x: 0.5, y: 2.4, w: 9, h: 1.0, fontSize: 28, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.6, w: 1.5, h: 0.06, fill: { color: C.accent } });
}

function main() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "3GPP Project";
  pres.title = "3GPP LTE/NR 译码链路：T2.1-T3.5";

  // 1. Title
  {
    const s = pres.addSlide();
    s.background = { fill: C.midnight };
    s.addText("3GPP LTE/NR 译码链路", { x: 0.5, y: 1.2, w: 9, h: 1.2, fontSize: 44, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
    s.addText("从软信息生成到码块分段", { x: 0.5, y: 2.5, w: 9, h: 0.8, fontSize: 26, fontFace: "Calibri Light", color: C.accent, margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.5, w: 2, h: 0.06, fill: { color: C.accent } });
    s.addText("T2.1 AWGN → T3.5 NR Polar · 10篇讲义", { x: 0.5, y: 3.8, w: 9, h: 0.5, fontSize: 14, fontFace: "Calibri", color: C.gray, margin: 0 });
  }

  // 2. Module 1
  addDivider(pres, "模块一：软信息生成 (T2.1–T2.5)", "01");

  addImgSlide(pres, "T2.1 AWGN 信道与噪声缩放 — Eb/N0 到 LLR", "t21-01.jpg");
  addImgSlide(pres, "T2.1 AWGN 模型假设与指标转换", "t21-02.jpg");
  addImgSlide(pres, "T2.1 BPSK LLR 公式与噪声失配", "t21-03.jpg");

  addImgSlide(pres, "T2.2 BPSK / QPSK 软解调 — 星座点到逐比特 LLR", "t22-1.jpg");
  addImgSlide(pres, "T2.2 Gray 映射与硬判决 vs 软判决", "t22-2.jpg");

  addImgSlide(pres, "T2.3 QAM 软解调与 Max-Log-MAP", "t23-01.jpg");
  addImgSlide(pres, "T2.3 Max-Log 近似推导与复杂度分析", "t23-02.jpg");
  addImgSlide(pres, "T2.3 16QAM 手算示例", "t23-03.jpg");

  addImgSlide(pres, "T2.4 衰落信道与 LLR 可靠度", "t24-1.jpg");
  addImgSlide(pres, "T2.4 均衡输出与可信度差异", "t24-2.jpg");

  addImgSlide(pres, "T2.5 LLR 裁剪、缩放与量化", "t25-1.jpg");
  addImgSlide(pres, "T2.5 量化精度 vs 硬件代价", "t25-2.jpg");

  // 3. Module 2
  addDivider(pres, "模块二：错误检测 — CRC (T3.1)", "02");

  addImgSlide(pres, "T3.1 LTE/NR CRC 家族概览", "t31-1.jpg");
  addImgSlide(pres, "T3.1 CRC 多项式与双层防御 (TB CRC + CB CRC)", "t31-2.jpg");
  addImgSlide(pres, "T3.1 CRC 长度与用途对比表", "t31-3.jpg");

  // 4. Module 3
  addDivider(pres, "模块三：码块分段 (T3.2–T3.5)", "03");

  // T3.2
  addImgSlide(pres, "T3.2 TB/CB/Filler 概念框架与协议处理链", "t32a-03.jpg");
  addImgSlide(pres, "T3.2 Table 5.1.3-3 列含义与 40/6144 边界", "t32a-04.jpg");
  addImgSlide(pres, "T3.2 LTE 分段规则协议读法", "t32a-05.jpg");
  addImgSlide(pres, "T3.2 Filler 语义与小块特例协议原文位置", "t32a-06.jpg");
  addImgSlide(pres, "T3.2 Trellis Termination 网格终止与跨流重排", "t32b-09.jpg");
  addImgSlide(pres, "T3.2 Circular Buffer 交错写入与决策设计逻辑", "t32b-10.jpg");
  addImgSlide(pres, "T3.2 循环缓冲区速率匹配 (决策三)", "t32b-11.jpg");
  addImgSlide(pres, "T3.2 Turbo 母码输出 D=Kr+4 完整协议溯源", "t32b-12.jpg");

  // T3.3
  addImgSlide(pres, "T3.3 LTE Turbo 分段 — 协议定位与关键符号", "t33-02.jpg");
  addImgSlide(pres, "T3.3 分段公式推导 (C / B' / K+ / K- / F)", "t33-03.jpg");
  addImgSlide(pres, "T3.3 B=10001 手算例子", "t33-04.jpg");
  addImgSlide(pres, "T3.3 接收端并行译码与 CB 描述符", "t33-05.jpg");

  // T3.4
  addImgSlide(pres, "T3.4 NR LDPC 分段 — BG1/BG2 基图选择", "t34a-01.jpg");
  addImgSlide(pres, "T3.4 Table 5.3.2-1 Lifting Size 集合", "t34a-02.jpg");
  addImgSlide(pres, "T3.4 分段符号与尺寸公式", "t34a-03.jpg");
  addImgSlide(pres, "T3.4 BG1/BG2 手算例子", "t34a-04.jpg");
  addImgSlide(pres, "T3.4 基图移位表 (Table 5.3.2-2/3)", "t34b-06.jpg");
  addImgSlide(pres, "T3.4 NR LDPC vs LTE Turbo Filler 位置对比", "t34b-07.jpg");
  addImgSlide(pres, "T3.4 接收端流程与描述符", "t34b-08.jpg");

  // T3.5
  addImgSlide(pres, "T3.5 NR Polar 分段 — 信道极化原理", "t35-01.jpg");
  addImgSlide(pres, "T3.5 N=4 Polar 编码手算", "t35-02.jpg");
  addImgSlide(pres, "T3.5 UCI Polar 分段与 CRC 附加", "t35-03.jpg");
  addImgSlide(pres, "T3.5 CRC 辅助 SCL 路径选择", "t35-04.jpg");

  // 5. Summary
  addDivider(pres, "总结与展望", "04");
  {
    const s = pres.addSlide();
    s.background = { fill: C.navy };
    s.addText("课程总结", { x: 0.5, y: 0.6, w: 9, h: 0.8, fontSize: 32, fontFace: "Arial Black", color: C.white, bold: true, margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.4, w: 1.5, h: 0.06, fill: { color: C.accent } });
    const pts = [
      "T2 (软信息): AWGN → QAM / Max-Log-MAP → 衰落 + 量化 — 译码器输入质量决定性能上限",
      "T3.1 (CRC): TB CRC + CB CRC 双层验收, 6种多项式覆盖全部 LTE/NR 场景",
      "T3.2–3.5 (分段): Turbo / LDPC / Polar 三种编码器分段规则, filler 位置和并行策略差异显著",
      "后续 (T4+): 迭代译码、外信息交换、BCJR/MAP、LDPC BP、Polar SCL 即将展开",
    ];
    s.addText(pts.map((t, i) => ({
      text: t, options: { bullet: true, breakLine: i < pts.length - 1, fontSize: 14, fontFace: "Calibri", color: C.lightBlue }
    })), { x: 0.5, y: 1.8, w: 9, h: 3.5, valign: "top", margin: 0 });
  }

  const out = path.join(os.homedir(), "Downloads", "3GPP_T2_T3_Visual.pptx");
  pres.writeFile({ fileName: out }).then(() => {
    console.log(`PPT: ${out}  (${pres.slides.length} slides)`);
  });
}

main();
