/**
 * @file    build_kb_intro.js
 * @brief   生成《3GPP 译码教学知识库 · 建设汇报》PPT（24 页，浅色学术系设计系统）
 * @date    2026-09-04
 * @usage   node build_kb_intro.js
 * @args    无
 * @env     docs/slides/node_modules（npm install pptxgenjs）
 * @exit_code 0 = 成功生成 docs/slides/3gpp_kb_intro.pptx；非 0 = 生成失败
 *
 * 设计说明：
 * - 汇报场合（导师/领导），浅色学术系：白/浅灰底 + 深蓝主色 + 橙色强调；
 *   深蓝用于封面与收束页（"三明治"结构）。
 * - 统一母题：左上编号方章（章节序号）+ 卡片式内容块 + 橙色仅用于
 *   关键数字/箭头/机制条（60-70% 视觉权重归深蓝与浅灰，橙色做尖点强调）。
 * - 内容口径按实测数据（2026-09-04）：讲义正文 155（L1 46/L2 73/L3 36）、
 *   L0 引导入口 4、概念笔记 115、SVG 教学图 132 + 协议截图 11、
 *   审计工具 15、lessons 25、记忆 30、47 天 490 次提交（仅作证据小字）。
 * - 每页附演讲者备注（汇报提词）。生成后用 soffice 转 PDF + pdftoppm
 *   转图片目检，发现问题修复后重跑本脚本。
 */

const pptxgen = require("pptxgenjs");
const pres = new pptxgen();

/* ============ 全局设置 ============ */
pres.layout = "LAYOUT_WIDE"; // 13.33" x 7.5"，16:9
pres.author = "AuroraYaus";
pres.title = "3GPP 译码教学知识库 · 建设汇报";
pres.subject = "3GPP LTE/NR 译码教学知识库建设汇报（2026-09）";

const F = "Microsoft YaHei"; // 标题/正文统一微软雅黑（WPS/Win 端一致；Linux 渲染回退 Noto CJK）

/** @brief 配色表：浅色学术系——深蓝主色、浅灰底、橙色强调 */
const C = {
  bg: "F6F7F9",      // 内容页底色（浅灰）
  ink: "232B3A",     // 正文深墨
  muted: "67718A",   // 辅助灰
  navy: "1E2A52",    // 主色深蓝（封面/收束底、标题、方章）
  navy2: "31406E",   // 次蓝（装饰、深底卡片）
  panel: "E9EDF5",   // 浅蓝面板
  white: "FFFFFF",   // 卡片白
  orange: "E8833A",    // 橙色强调（色块/装饰，不带文字）
  orangeDeep: "C0571E",// 深橙（文字/带白字芯片——白底 4.51:1、浅灰底 4.24:1，过对比度门槛）
  line: "D8DEE8",    // 描边浅灰
  light: "A8B4D0",   // 深底上的浅字
  cream: "FDF1E7"    // 浅橙底（经验层条带）
};

/** @brief 卡片投影工厂——PptxGenJS 会原地改写选项对象，每次调用必须新建（禁止复用对象） */
const shd = () => ({ type: "outer", color: "1E2A52", blur: 9, offset: 2, angle: 135, opacity: 0.10 });

const MW = 0.5;   // 页面边距（英寸）
const CW = 12.33; // 内容区宽度

/**
 * @brief 内容页页头：左上编号方章 + 部分标签 + 大标题
 * @param s    幻灯片对象
 * @param n    页码（01-24，与方章一致）
 * @param label 部分标签（如"第二部分 · 结构与内容"）
 * @param title 页标题（29pt 深蓝加粗）
 */
function hdr(s, n, label, title) {
  s.background = { color: C.bg };
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: MW, y: 0.45, w: 0.62, h: 0.62, fill: { color: C.navy }, rectRadius: 0.1
  });
  s.addText(String(n).padStart(2, "0"), {
    x: MW, y: 0.45, w: 0.62, h: 0.62, fontFace: F, fontSize: 18, bold: true,
    color: C.white, align: "center", valign: "middle", margin: 0
  });
  s.addText(label, {
    x: 1.28, y: 0.47, w: 8, h: 0.3, fontFace: F, fontSize: 11, color: C.muted, charSpacing: 2, margin: 0
  });
  s.addText(title, {
    x: MW, y: 1.18, w: CW, h: 0.66, fontFace: F, fontSize: 29, bold: true, color: C.navy, margin: 0
  });
}

/**
 * @brief 页脚：分隔细线 + 左侧演示稿名 + 右侧页码
 * @param s    幻灯片对象
 * @param n    页码
 * @param dark 深底页（封面/收束）用浅色文字且不画细线
 */
function foot(s, n, dark = false) {
  s.addShape(pres.shapes.LINE, {
    x: MW, y: 7.08, w: CW, h: 0, line: { color: dark ? "3D4E7D" : C.line, width: 0.5 }
  });
  s.addText("3GPP 译码教学知识库 · 建设汇报", {
    x: MW, y: 7.14, w: 6, h: 0.3, fontFace: F, fontSize: 9, color: dark ? C.light : C.muted, margin: 0
  });
  s.addText(`${String(n).padStart(2, "0")} / 24`, {
    x: 10.83, y: 7.14, w: 2, h: 0.3, fontFace: F, fontSize: 9, color: dark ? C.light : C.muted, align: "right", margin: 0
  });
}

/**
 * @brief 白色卡片（可选橙色左缘条）：统一视觉母题
 * @param s    幻灯片对象
 * @param x,y,w,h 位置与尺寸（英寸）
 * @param o    { fill, accent } accent=true 时画橙色左缘条
 */
function card(s, x, y, w, h, o = {}) {
  s.addShape(pres.shapes.RECTANGLE, {
    x, y, w, h, fill: { color: o.fill || C.white }, line: { color: C.line, width: 0.75 }, shadow: shd()
  });
  if (o.accent) {
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.07, h, fill: { color: C.orangeDeep } });
  }
}

/**
 * @brief 卡片标题行：小橙色方块 + 加粗标题（去模板化的页内小节样式）
 * @param s    幻灯片对象
 * @param x,y  标题位置
 * @param text 标题文本
 * @param w    文本框宽
 */
function cardTitle(s, x, y, text, w) {
  s.addShape(pres.shapes.RECTANGLE, { x, y: y + 0.07, w: 0.14, h: 0.14, fill: { color: C.orangeDeep } });
  s.addText(text, {
    x: x + 0.26, y: y - 0.03, w, h: 0.36, fontFace: F, fontSize: 16, bold: true, color: C.navy, margin: 0
  });
}

/**
 * @brief 正文文本框（默认 12pt 深墨左对齐，无内边距便于对齐）
 * @param s    幻灯片对象
 * @param str  文本或富文本 run 数组
 * @param x,y,w,h 位置与尺寸
 * @param o    追加样式（fontSize/color/bold/align/valign/lineSpacing）
 */
function txt(s, str, x, y, w, h, o = {}) {
  s.addText(str, Object.assign({ x, y, w, h, fontFace: F, fontSize: 12, color: C.ink, margin: 0, valign: "top" }, o));
}

/* ================================================================ */
/* S1 封面（深蓝底）                                                */
/* ================================================================ */
{
  const s = pres.addSlide();
  s.background = { color: C.navy };
  // 右侧装饰：三个渐大的半透明圆 + 一个橙色实心点（信号扩散母题）
  [[7.9, 4.9, 1.6, 20], [9.6, 4.2, 2.6, 32], [11.6, 3.2, 4.0, 46]].forEach(([cx, cy, r, t]) => {
    s.addShape(pres.shapes.OVAL, {
      x: cx, y: cy, w: r * 2, h: r * 2, fill: { color: C.navy2, transparency: t }
    });
  });
  s.addShape(pres.shapes.OVAL, { x: 9.05, y: 5.35, w: 0.22, h: 0.22, fill: { color: C.orangeDeep } });
  // 左侧文字组
  s.addText("3GPP 译码教学知识库 · 建设汇报", {
    x: MW, y: 1.0, w: 8, h: 0.4, fontFace: F, fontSize: 14, color: C.light, charSpacing: 3, margin: 0
  });
  s.addText([
    { text: "把 3GPP 协议，", options: { breakLine: true } },
    { text: "译成一座可学习的知识库", options: {} }
  ], {
    x: MW, y: 1.7, w: 12.3, h: 2.6, fontFace: F, fontSize: 40, bold: true, color: C.white, margin: 0, lineSpacing: 56
  });
  s.addText("LTE / NR 译码链路全栈教学库：理论推导 → 协议算法 → 工程实现", {
    x: MW, y: 4.35, w: 11, h: 0.5, fontFace: F, fontSize: 17, color: C.light, margin: 0
  });
  s.addText("汇报人：AuroraYaus    |    2026 年 9 月    |    Obsidian 工作区", {
    x: MW, y: 6.55, w: 11, h: 0.4, fontFace: F, fontSize: 12, color: C.light, margin: 0
  });
  foot(s, 1, true);
  s.addNotes("开场一句话：过去四个多月，我用 AI Agent 辅助，把 3GPP 协议原文做成了一座可学习、可验证、经验自积累的知识库。今天汇报五件事：它是干什么的、现状、结构与内容、积累了哪些经验、经验怎么积累的，最后如实讲不足与下一步。");
}

/* ================================================================ */
/* S2 汇报地图                                                      */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 2, "第一部分 · 定位与现状", "今天用六个问题，讲完这座库");
  const items = [
    ["01", "它是干什么的", "从零基础到 RTL 译码器的一条学习路径"],
    ["02", "现状如何", "四层全部可用，数字看板一页看清"],
    ["03", "结构与内容", "内容层 / 质量层 / 经验层，三层咬合"],
    ["04", "积累了哪些经验", "25 条教训，每条对应一次真实返工"],
    ["05", "经验如何积累", "五步闭环：拷问 → 固化 → 扫描 → 验证"],
    ["06", "不足与下一步", "如实讲缺口，逐条对应补课计划"]
  ];
  const cw = 3.84, ch = 2.15, gx = 0.405, gy = 0.4;
  items.forEach(([n, t, d], i) => {
    const x = MW + (i % 3) * (cw + gx), y = 1.95 + Math.floor(i / 3) * (ch + gy);
    card(s, x, y, cw, ch);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x + 0.25, y: y + 0.25, w: 0.52, h: 0.52, fill: { color: C.orangeDeep }, rectRadius: 0.1
    });
    s.addText(n, {
      x: x + 0.25, y: y + 0.25, w: 0.52, h: 0.52, fontFace: F, fontSize: 14, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    s.addText(t, {
      x: x + 0.25, y: y + 0.95, w: cw - 0.5, h: 0.42, fontFace: F, fontSize: 17, bold: true, color: C.navy, margin: 0
    });
    s.addText(d, {
      x: x + 0.25, y: y + 1.42, w: cw - 0.5, h: 0.6, fontFace: F, fontSize: 11.5, color: C.muted, margin: 0, lineSpacing: 16
    });
  });
  foot(s, 2);
  s.addNotes("先给一张地图。六个问题按顺序展开：前三个讲'这座库是什么'，后三个讲'它是怎么被治理出来的'。");
}

/* ================================================================ */
/* S3 它是干什么的                                                  */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 3, "第一部分 · 定位与现状", "它是一座桥：把协议条文，译成能学懂、能复现的教学内容");
  // 左列：三个定位要点
  const pts = [
    ["给谁用", "面向通信零基础学习者——不需要先修信道编码，从 GF(2) 讲起，一路带到能设计 RTL 译码器。"],
    ["解决什么", "协议原文是写给实现者的：术语密集、条文分散、没有学习路径。知识库把 7000+ 页条文翻译成四层递进的课程。"],
    ["怎么保证学会", "每篇讲义有学习目标、前置检查、例题与小结；每张图过几何审计；每个数值实例实跑验证。"]
  ];
  pts.forEach(([t, d], i) => {
    const y = 1.95 + i * 1.62;
    card(s, MW, y, 6.1, 1.45);
    cardTitle(s, MW + 0.25, y + 0.2, t, 5.3);
    txt(s, d, MW + 0.25, y + 0.58, 5.65, 0.8, { fontSize: 11.5, color: C.ink, lineSpacing: 15 });
  });
  // 右列：学习路径竖排图
  card(s, 6.95, 1.95, 5.88, 4.9);
  const steps = [
    ["零基础入门", "L0 协议阅读引导"],
    ["L1 基础", "数学 · 物理层（46 篇）"],
    ["L2 协议算法", "三族译码 · 接收链（73 篇）"],
    ["L3 工程实现", "定点 · RTL · 验证（36 篇）"],
    ["RTL 译码器", "能设计 · 能验证"]
  ];
  steps.forEach(([t, d], i) => {
    const y = 2.2 + i * 0.92;
    const last = i === steps.length - 1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: 7.25, y, w: 5.28, h: 0.72, fill: { color: last ? C.orangeDeep : C.panel }, rectRadius: 0.08
    });
    s.addText([
      { text: t + "  ", options: { bold: true, color: last ? C.white : C.navy } },
      { text: d, options: { color: last ? C.white : C.muted, fontSize: 11 } }
    ], {
      x: 7.25, y, w: 5.28, h: 0.72, fontFace: F, fontSize: 13, align: "center", valign: "middle", margin: 0
    });
    if (i < steps.length - 1) {
      s.addText("↓", { x: 9.75, y: y + 0.7, w: 0.3, h: 0.24, fontFace: F, fontSize: 14, bold: true, color: C.orangeDeep, align: "center", margin: 0 });
    }
  });
  foot(s, 3);
  s.addNotes("一句话定位：协议原文和初学者之间差一座桥，这座库就是那座桥。强调'可复现'——每篇讲义的数值实例都是实跑验证过的。");
}

/* ================================================================ */
/* S4 现状速览                                                      */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 4, "第一部分 · 定位与现状", "现在的状况：四层全部可用，一篇不跳");
  // 第一行：四个大数字
  const stats = [
    ["155", "篇讲义正文", "L1 46 · L2 73 · L3 36"],
    ["115", "篇概念笔记", "六段式模板，图谱互联"],
    ["132", "张 SVG 教学图", "另有 11 张协议截图"],
    ["25", "条经验教训", "每条对应一次真实返工"]
  ];
  stats.forEach(([n, t, d], i) => {
    const x = MW + i * (2.9 + 0.24);
    card(s, x, 2.0, 2.9, 1.9);
    s.addText(n, {
      x: x, y: 2.1, w: 2.9, h: 0.75, fontFace: F, fontSize: 36, bold: true, color: C.navy, align: "center", margin: 0
    });
    s.addText(t, {
      x: x, y: 2.92, w: 2.9, h: 0.35, fontFace: F, fontSize: 13, bold: true, color: C.ink, align: "center", margin: 0
    });
    s.addText(d, {
      x: x + 0.15, y: 3.3, w: 2.6, h: 0.5, fontFace: F, fontSize: 9.5, color: C.muted, align: "center", margin: 0, lineSpacing: 13
    });
  });
  // 第二行：体系三块
  const sys = [
    ["17 + 23", "条规则", "硬性规则 17 条 + 合规 Hard Constraints 23 条"],
    ["15", "个审计工具", "布局审计 R1-R11、圈号、Mermaid、死链、口径……"],
    ["30", "条项目记忆", "项目内权威副本 + 本地镜像双份维护"]
  ];
  sys.forEach(([n, t, d], i) => {
    const x = MW + i * (3.94 + 0.25);
    card(s, x, 4.3, 3.94, 1.4);
    s.addText([
      { text: n + " ", options: { bold: true, color: C.orangeDeep } },
      { text: t, options: { bold: true, color: C.ink } }
    ], { x: x + 0.25, y: 4.5, w: 3.4, h: 0.4, fontFace: F, fontSize: 15, margin: 0 });
    txt(s, d, x + 0.25, 4.95, 3.44, 0.65, { fontSize: 10.5, color: C.muted, lineSpacing: 14 });
  });
  txt(s, "2026-07-19 首次提交 · 至今 47 天 · 490 次提交 · 双推 Gitee + GitHub —— 过程数字只作佐证", MW, 6.35, CW, 0.35, { fontSize: 10.5, color: C.muted, align: "center" });
  foot(s, 4);
  s.addNotes("现状一页给结论：内容四层全部可用。数字口径都是实测的。底行小字：47 天 490 次提交只作佐证——重点不是做了多久，是做成了什么。");
}

/* ================================================================ */
/* S5 结构总览（三层条带）                                          */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 5, "第二部分 · 结构与内容", "三层结构：内容、质量、经验互相咬合");
  const bands = [
    ["内容层", C.panel, "讲义 L0-L3（正文 155 篇 + 引导入口 4 篇）｜概念图谱（115 篇）｜协议锚点（3GPP_Rel19 原始资料与结构化抽取）"],
    ["质量层", C.white, "硬性规则 17 + 23 条｜审计工具 15 个｜图片资产台账、术语总表、同步清单九类检查"],
    ["经验层", C.cream, "经验教训 lessons 25 条｜项目记忆 30 条｜五步固化闭环——把每次返工变成规则与工具"]
  ];
  bands.forEach(([label, fill, body], i) => {
    const y = 2.0 + i * 1.62;
    s.addShape(pres.shapes.RECTANGLE, { x: MW, y, w: 12.33, h: 1.44, fill: { color: fill }, line: { color: C.line, width: 0.75 }, shadow: shd() });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: MW + 0.2, y: y + 0.36, w: 1.35, h: 0.72, fill: { color: C.navy }, rectRadius: 0.1
    });
    s.addText(label, {
      x: MW + 0.2, y: y + 0.36, w: 1.35, h: 0.72, fontFace: F, fontSize: 15, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    txt(s, body, MW + 1.85, y + 0.18, 10.1, 1.1, { fontSize: 12.5, lineSpacing: 18, valign: "middle" });
    if (i < 2) {
      s.addText("↑", { x: 1.2, y: y + 1.42, w: 0.3, h: 0.24, fontFace: F, fontSize: 14, bold: true, color: C.orangeDeep, align: "center", margin: 0 });
    }
  });
  txt(s, "内容层产出内容；质量层给每一步设门；经验层把每次返工变成规则，反哺前两层。", MW, 6.32, CW, 0.35, { fontSize: 11.5, color: C.navy, bold: true, align: "center" });
  foot(s, 5);
  s.addNotes("结构一句话：三层咬合。内容层是主体，质量层是闸门，经验层是蓄水池——越用越严，也越用越厚。后面每层各讲一页。");
}

/* ================================================================ */
/* S6 讲义体系总览（L0-L3 表格 + 模板卡）                           */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 6, "第二部分 · 结构与内容", "编号即路径：从 L0 走到 L3，一篇不跳");
  const rows = [
    ["L0", "协议阅读引导", "4 篇入口：协议怎么读、术语总表、概念图谱入口、高频查询排名", "E9EDF5"],
    ["L1", "基础", "46 篇：GF(2) 数学与译码理论 · OFDM 物理层与软解调", "FFFFFF"],
    ["L2", "协议算法", "73 篇：Turbo / LDPC / Polar 三族 · MIMO · 控制信道 · 上行 · 调度", "FFFFFF"],
    ["L3", "工程实现", "36 篇：浮点 → 定点 → RTL → 验证 · 接收链工程预算（T21-T23）", "FFFFFF"]
  ];
  rows.forEach(([lv, name, desc, fill], i) => {
    const y = 1.95 + i * 1.12;
    s.addShape(pres.shapes.RECTANGLE, { x: MW, y, w: 8.15, h: 0.98, fill: { color: fill }, line: { color: C.line, width: 0.75 }, shadow: shd() });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: MW + 0.2, y: y + 0.24, w: 0.72, h: 0.5, fill: { color: C.navy }, rectRadius: 0.08
    });
    s.addText(lv, {
      x: MW + 0.2, y: y + 0.24, w: 0.72, h: 0.5, fontFace: F, fontSize: 14, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    s.addText([
      { text: name + "   ", options: { bold: true, color: C.navy } },
      { text: desc, options: { color: C.ink } }
    ], { x: MW + 1.15, y, w: 7.5, h: 0.98, fontFace: F, fontSize: 12.5, valign: "middle", margin: 0 });
  });
  // 右侧：统一模板卡
  card(s, 8.95, 1.95, 3.88, 4.43);
  cardTitle(s, 9.2, 2.2, "每篇同一模板", 3.3);
  const tpl = ["学习目标：可检验的 bullets", "前置检查：需要什么基础", "内容：公式 / 类比 / 数值实例", "例题：示范 + 引导 + 独立 ≤ 9 个", "资料与协议边界：规定 / 不规定", "小结：收束 + 指向下一篇"];
  tpl.forEach((t, i) => {
    txt(s, [
      { text: `${i + 1}.  `, options: { bold: true, color: C.orangeDeep } },
      { text: t, options: {} }
    ], 9.2, 2.75 + i * 0.55, 3.4, 0.5, { fontSize: 11, lineSpacing: 14 });
  });
  txt(s, "编号 T/TX 与层绑定；frontmatter 类型由审计工具强制。", 9.2, 6.05, 3.4, 0.3, { fontSize: 9, color: C.muted, lineSpacing: 12 });
  foot(s, 6);
  s.addNotes("编号就是路径：T 编号的层号与内容主题绑定，读者看编号就知道自己读到哪一步。每篇同一个模板——学习目标、前置检查、例题、协议边界，结构稳定学习成本才低。");
}

/* ================================================================ */
/* S7 L1 基础层                                                     */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 7, "第二部分 · 结构与内容", "L1 打地基：先换世界观，再谈译码（46 篇）");
  card(s, MW, 1.95, 6.04, 4.35);
  cardTitle(s, MW + 0.25, 2.2, "数学与译码理论", 5.2);
  const l1a = [
    ["GF(2) 有限域 → 多项式与 CRC → 向量矩阵", ""],
    ["概率与贝叶斯 → 软信息 LLR", ""],
    ["核心换脑：译码器看到的不是 0/1，而是", "「每个比特有多像 1」——软信息世界观"]
  ];
  let yy = 2.85;
  l1a.forEach(([t, d]) => {
    txt(s, [{ text: "·  ", options: { bold: true, color: C.orangeDeep } }, { text: t, options: { bold: t.includes("核心") } }], MW + 0.25, yy, 5.6, 0.35, { fontSize: 12, lineSpacing: 16 });
    yy += 0.5;
    if (d) { txt(s, d, MW + 0.5, yy - 0.08, 5.4, 0.7, { fontSize: 11.5, color: C.muted, lineSpacing: 15 }); yy += 0.72; }
  });
  txt(s, "先修数学全部内建：有限域、多项式、矩阵运算都在 L1 前几篇讲透，不需要外部教材。", MW + 0.25, 5.3, 5.6, 0.6, { fontSize: 10.5, color: C.muted, lineSpacing: 14 });
  card(s, 6.79, 1.95, 6.04, 4.35);
  cardTitle(s, 7.04, 2.2, "物理层与软解调（19 篇）", 5.2);
  txt(s, [
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "OFDM 原理：子载波、循环前缀、星座映射", options: { breakLine: true } },
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "软解调：从接收符号算出每个比特的 LLR", options: { breakLine: true } },
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "发送端镜像章：先知道信号怎么生出来，", options: { breakLine: true } },
    { text: "才懂得怎么解回去", options: {} }
  ], 7.04, 2.85, 5.55, 1.9, { fontSize: 12, lineSpacing: 30 });
  txt(s, "物理层是 L2 协议算法的上游：L2 讲的每个概念，输入输出都接在 L1 的软信息上。", 7.04, 5.3, 5.55, 0.6, { fontSize: 10.5, color: C.muted, lineSpacing: 14 });
  txt(s, "每篇 ≥500 行正文 · ≥1 张教学图 · ≥1 个实跑通过的 numpy 验证", MW, 6.48, CW, 0.35, { fontSize: 10.5, color: C.muted, align: "center" });
  foot(s, 7);
  s.addNotes("L1 的关键动作是'换世界观'：软信息。这是后面一切译码算法的地基，所以 L1 用 46 篇打透，包括发送端镜像——知道信号怎么来的才知道怎么解。");
}

/* ================================================================ */
/* S8 L2 协议算法层                                                 */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 8, "第二部分 · 结构与内容", "L2 啃协议：一套框架，通吃 Turbo / LDPC / Polar（73 篇）");
  card(s, MW, 1.95, 6.04, 4.35);
  cardTitle(s, MW + 0.25, 2.2, "三族译码器，同一套框架", 5.2);
  txt(s, [
    { text: "先讲共性：", options: { bold: true } },
    { text: "编码结构、迭代译码、置信传播", options: { breakLine: true } },
    { text: "再分族对比：", options: { bold: true } },
    { text: "Turbo（3G/4G）→ LDPC（5G 数据）→ Polar（5G 控制）", options: { breakLine: true } },
    { text: "各自参数、结构与实现差异", options: {} }
  ], MW + 0.25, 2.85, 5.6, 1.5, { fontSize: 12, lineSpacing: 24 });
  txt(s, "锚定条款：TS 36.212（Turbo）· TS 38.212（LDPC / Polar）——正文结论以协议条文为准。", MW + 0.25, 4.5, 5.6, 0.6, { fontSize: 10.5, color: C.muted, lineSpacing: 14 });
  txt(s, "学一套框架，通吃三代协议——协议会换代，译码方法论不变。", MW + 0.25, 5.55, 5.6, 0.5, { fontSize: 10.5, color: C.muted, lineSpacing: 14 });
  card(s, 6.79, 1.95, 6.04, 4.35);
  cardTitle(s, 7.04, 2.2, "接收链外延：译码之外的全链路", 5.2);
  txt(s, [
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "MIMO 检测与概率整形", options: { breakLine: true } },
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "控制信道：DCI 盲检、UCI 上报", options: { breakLine: true } },
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "上行：PRACH 随机接入、SRS 探测", options: { breakLine: true } },
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "调度、重传、小区搜索", options: { breakLine: true } },
    { text: "·  ", options: { bold: true, color: C.orangeDeep } },
    { text: "同步与信道估计", options: {} }
  ], 7.04, 2.85, 5.55, 2.1, { fontSize: 12, lineSpacing: 30 });
  txt(s, "译码不是孤岛：控制信息怎么解出来、信道怎么测出来，都是译码器的输入。", 7.04, 5.55, 5.55, 0.5, { fontSize: 10.5, color: C.muted, lineSpacing: 14 });
  txt(s, "协议族分布展示：每个概念讲清「谁定义 → 谁调度 → 谁测量 → 谁配置 → 谁验收」", MW, 6.48, CW, 0.35, { fontSize: 10.5, color: C.muted, align: "center" });
  foot(s, 8);
  s.addNotes("L2 是知识库最厚的一层。两个设计决定：一是三族译码器共用一套方法论框架，学一次通吃三代；二是把译码放回接收链整体里讲，不孤立。");
}

/* ================================================================ */
/* S9 L3 工程实现层                                                 */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 9, "第二部分 · 结构与内容", "L3 落地：浮点 → 定点 → RTL → 验证，四道瀑布（36 篇）");
  const steps = [
    ["浮点算法", [{ text: "理论译码算法", options: { breakLine: true } }, { text: "与性能基准", options: {} }]],
    ["定点化", [{ text: "位宽预算：每截一位精度", options: { breakLine: true } }, { text: "代价多少 dB 要算得出来", options: {} }]],
    ["RTL 架构", [{ text: "译码器硬件", options: { breakLine: true } }, { text: "结构设计", options: {} }]],
    ["验证", [{ text: "功能 / 性能验证", options: { breakLine: true } }, { text: "与闭环比对", options: {} }]]
  ];
  steps.forEach(([t, d], i) => {
    const x = MW + i * (2.85 + 0.31);
    card(s, x, 2.1, 2.85, 2.05, { accent: i === 1 });
    s.addText(t, {
      x: x, y: 2.3, w: 2.85, h: 0.45, fontFace: F, fontSize: 16, bold: true, color: C.navy, align: "center", margin: 0
    });
    txt(s, d, x + 0.2, 2.85, 2.45, 0.95, { fontSize: 11, color: C.muted, align: "center", lineSpacing: 16 });
    if (i < 3) {
      s.addText("→", { x: x + 2.84, y: 2.92, w: 0.33, h: 0.4, fontFace: F, fontSize: 16, bold: true, color: C.orangeDeep, align: "center", margin: 0 });
    }
  });
  card(s, MW, 4.75, 12.33, 1.7);
  cardTitle(s, MW + 0.25, 4.95, "读完一篇 L3 讲义，能带走什么", 11.5);
  txt(s, [
    { text: "一份可复算的位宽预算表：", options: { bold: true } },
    { text: "定点位宽选择不是拍脑袋，而是按目标性能逐位核算；", options: {} },
    { text: "一份可对照的 RTL 架构图：", options: { bold: true } },
    { text: "浮点算法如何映射成硬件数据通路；", options: {} },
    { text: "后端专题 T21-T23：接收链工程预算与实现。", options: { bold: true } }
  ], MW + 0.25, 5.55, 11.85, 0.8, { fontSize: 12, lineSpacing: 20 });
  foot(s, 9);
  s.addNotes("L3 是知识库的'交付层'——学完能直接进 RTL 编码。橙框标出的定点化是工程关键：截一位精度损失多少 dB，每篇都给可复算的预算方法。");
}

/* ================================================================ */
/* S10 概念图谱                                                     */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 10, "第二部分 · 结构与内容", "115 篇六段式笔记，织成一张会自更新的网");
  card(s, MW, 1.95, 5.7, 4.55);
  cardTitle(s, MW + 0.25, 2.2, "概念笔记：六段式模板", 4.9);
  const six = ["独立解释任务", "科学定义", "直观模型", "常见误解", "协议锚点", "图谱关联（wikilink 网络）"];
  six.forEach((t, i) => {
    const y = 2.8 + i * 0.55;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: MW + 0.25, y, w: 0.42, h: 0.42, fill: { color: C.panel }, rectRadius: 0.08
    });
    s.addText(String(i + 1), {
      x: MW + 0.25, y, w: 0.42, h: 0.42, fontFace: F, fontSize: 12, bold: true, color: C.navy, align: "center", valign: "middle", margin: 0
    });
    txt(s, t, MW + 0.85, y + 0.05, 4.5, 0.4, { fontSize: 12, valign: "middle" });
  });
  txt(s, "「直观模型」和「常见误解」是六段式的灵魂——先建立直觉，再拆错误直觉。", MW + 0.25, 6.08, 5.25, 0.3, { fontSize: 9, color: C.muted, lineSpacing: 12 });
  card(s, 6.5, 1.95, 6.33, 4.55);
  cardTitle(s, 6.75, 2.2, "Q&A 查询流水线：问一次，库厚一层", 5.5);
  const flow = [
    "问题润色：口语问题提炼为知识主题",
    "检索：关键词 + wikilink 邻近节点 + queries 字段",
    "命中策略：完全命中 +1 / 高度相关扩充 / 部分相关加链 / 无匹配新建",
    "沉淀回写：内容更新 + queries 计数 + 高频排名",
    "终端归纳答案：标题 + 原理 + 要点 + 关联"
  ];
  flow.forEach((t, i) => {
    const y = 2.8 + i * 0.6;
    txt(s, [
      { text: `${i + 1}  `, options: { bold: true, color: C.orangeDeep } },
      { text: t, options: {} }
    ], 6.75, y, 5.85, 0.42, { fontSize: 11.5, valign: "middle" });
    if (i < flow.length - 1) {
      s.addText("↓", { x: 7.05, y: y + 0.36, w: 0.3, h: 0.26, fontFace: F, fontSize: 12, bold: true, color: C.orangeDeep, align: "center", margin: 0 });
    }
  });
  txt(s, "高频查询排名表：被反复问的概念会被反复打磨——目前 13 篇概念已带 queries 计数。", 6.75, 5.95, 5.85, 0.42, { fontSize: 10, color: C.muted, lineSpacing: 13 });
  foot(s, 10);
  s.addNotes("概念笔记是讲义之外的第二个知识网络：六段式固定模板保证质量下限。Q&A 流水线是知识库'自更新'的引擎——每次问答都沉淀回库，问得多的概念排名靠前、被反复打磨。");
}

/* ================================================================ */
/* S11 协议锚点                                                     */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 11, "第二部分 · 结构与内容", "每篇讲义，都锚在协议条文上");
  const cols = [
    ["原始资料", "3GPP_Rel19 规范全文 + 结构化抽取（独立数据仓 3gpp_docs，clone 即复原）", "TS 36.212 · 36.213 · 38.211-38.215 按主题归档", "协议原文是一切结论的源头"],
    ["讲义锚定", "每篇尾部「资料与协议边界」：协议规定什么 / 不规定什么（实现域）/ 接收端义务边界", "规定之外是实现的自由域——也是工程判断的起点", "规定与不规定同样重要"],
    ["概念锚点", "概念笔记含 TS/TR 小节号与本地处理稿锚点；导频类概念列全协议族分工", "五层职责范式：定义 → 调度 → 测量 → 配置 → 验收", "谁定义 → 谁调度 → 谁测量 → 谁配置 → 谁验收"]
  ];
  cols.forEach(([t, d, sub, note], i) => {
    const x = MW + i * (3.94 + 0.25);
    card(s, x, 1.95, 3.94, 4.4);
    cardTitle(s, x + 0.25, 2.2, t, 3.2);
    txt(s, d, x + 0.25, 2.85, 3.44, 1.3, { fontSize: 12, lineSpacing: 24 });
    txt(s, sub, x + 0.25, 4.35, 3.44, 0.9, { fontSize: 10.5, color: C.muted, lineSpacing: 15 });
    s.addShape(pres.shapes.RECTANGLE, { x: x + 0.25, y: 5.55, w: 3.44, h: 0.62, fill: { color: C.panel } });
    txt(s, note, x + 0.4, 5.63, 3.15, 0.48, { fontSize: 10, color: C.navy, bold: true, lineSpacing: 13, valign: "middle" });
  });
  txt(s, "3GPP 协议精读优先：正文结论以协议条文为准，教材与论文只作补充理解。", MW, 6.52, CW, 0.35, { fontSize: 11, color: C.muted, align: "center" });
  foot(s, 11);
  s.addNotes("知识库的学术立场：协议精读优先。每篇讲义都标清协议规定什么、不规定什么——'不规定'的地方正是实现者的自由域，也是工程判断的起点。");
}

/* ================================================================ */
/* S12 质量层                                                       */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 12, "第二部分 · 结构与内容", "规则不贴在墙上——每条都长在工具里");
  card(s, MW, 1.95, 5.7, 4.55);
  cardTitle(s, MW + 0.25, 2.2, "规则三层", 4.9);
  const rules = [
    ["项目硬性规则 17 条", "SKILL 优先、DOXYGEN 注释、SVG 强制验证、纠错固化、批量作用域……"],
    ["合规 Hard Constraints 23 条", "零基础保护、术语首现「中文（英文）」、LaTeX 全检、标题口语化禁止……"],
    ["文档与注释规则总纲", "讲义模板、概念六段式、资产台账、术语同步"]
  ];
  rules.forEach(([t, d], i) => {
    const y = 2.8 + i * 1.2;
    txt(s, [
      { text: "·  ", options: { bold: true, color: C.orangeDeep } },
      { text: t + "：", options: { bold: true, breakLine: true } },
      { text: d, options: { color: C.muted, fontSize: 10.5 } }
    ], MW + 0.25, y + 0.05, 5.2, 1.0, { fontSize: 11.5, lineSpacing: 16 });
  });
  card(s, 6.5, 1.95, 6.33, 4.55);
  cardTitle(s, 6.75, 2.2, "15 个审计工具：规则的可执行形态", 5.5);
  const tools = [
    ["audit_svg_layout", "图形布局审计 R1-R11：越界/重叠/边界间距/盲区兜底"],
    ["audit_circled_digits", "带圈数字禁令（全库 md/svg/py）"],
    ["audit_mermaid_syntax", "Mermaid 真实渲染验证（引号节点规则）"],
    ["audit_link_integrity", "死链全格式 + 图谱空心节点扫描"],
    ["audit_frontmatter_types", "frontmatter 类型口径一致"],
    ["audit_plantuml_syntax", "PlantUML 真实渲染验证"]
  ];
  tools.forEach(([t, d], i) => {
    const y = 2.8 + i * 0.62;
    txt(s, [
      { text: t + "  ", options: { bold: true, color: C.navy, fontFace: "Consolas" } },
      { text: d, options: { color: C.muted } }
    ], 6.75, y, 5.85, 0.5, { fontSize: 10.5, lineSpacing: 13 });
  });
  txt(s, "一张 SVG 图要过 R1-R11 几何审计 + PNG 目检，才准进讲义——「工具不可用」必须显式声明，不得默认通过。", MW, 6.52, CW, 0.35, { fontSize: 11, color: C.muted, align: "center" });
  foot(s, 12);
  s.addNotes("质量层的核心设计：规则不是给人看的，是给工具执行的。15 个审计工具各守一门，每条规则都能被机器检查——这才叫可执行。");
}

/* ================================================================ */
/* S13 经验总览                                                     */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 13, "第三部分 · 经验与积累机制", "25 条经验教训，一条对应一次真实返工");
  const cats = [
    ["图形与布局", "SVG 审计盲区、字体度量、重绘交付清单", "例：rotate 一律竖排化"],
    ["语法与渲染", "Mermaid 引号节点、LaTeX 可渲染全检", "例：引号节点取全版本安全子集"],
    ["批量操作", "作用域限定、死链全格式、计数实测", "例：T12.x 在 L2/L3 双目录合法"],
    ["写作规范", "概念首现讲解、习题上限、正文无中间结果", "例：概念首现必须讲解"],
    ["流程机制", "写作先拷问、纠错必固化、Q&A 流水线", "例：纠错必固化五步"],
    ["工具链治理", "双推 Gitee+GitHub、审计治理、图片台账", "例：一次 push 双推两端"]
  ];
  cats.forEach(([t, d, ex], i) => {
    const x = MW + (i % 3) * (3.94 + 0.25), y = 1.95 + Math.floor(i / 3) * 2.15;
    card(s, x, y, 3.94, 2.0);
    cardTitle(s, x + 0.25, y + 0.2, t, 3.2);
    txt(s, d, x + 0.25, y + 0.72, 3.44, 0.7, { fontSize: 11, color: C.muted, lineSpacing: 15 });
    txt(s, ex, x + 0.25, y + 1.48, 3.44, 0.4, { fontSize: 10, color: C.orangeDeep, bold: true });
  });
  txt(s, "每条 lesson 记录根因 + How to apply；项目内权威副本（docs/audits/lessons）+ 本地镜像双份维护", MW, 6.45, CW, 0.35, { fontSize: 10.5, color: C.muted, align: "center" });
  foot(s, 13);
  s.addNotes("经验不是抽象口号，是 25 条有编号、有根因、有案例的教训档案，按六个主题归档。接下来四页讲机制和最有代表性的案例。");
}

/* ================================================================ */
/* S14 五步闭环                                                     */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 14, "第三部分 · 经验与积累机制", "经验是这么攒下来的：五步闭环");
  const steps = [
    ["1 拷问定标准", "先对齐方案，收敛成 PLAN"],
    ["2 执行", "AI 批量执行，人验收把关"],
    ["3 用户纠错", "错一次，就是一次免费的需求澄清"],
    ["4 固化为规则/工具", "只修不固化，视为未完成"],
    ["5 全库同类扫描", "修一类，扫全库，验证闭环"]
  ];
  steps.forEach(([t, d], i) => {
    const x = MW + i * (2.15 + 0.36);
    card(s, x, 2.1, 2.15, 1.85);
    s.addText(t, {
      x: x, y: 2.3, w: 2.15, h: 0.45, fontFace: F, fontSize: 13.5, bold: true, color: C.navy, align: "center", margin: 0
    });
    txt(s, d, x + 0.15, 2.85, 1.85, 1.0, { fontSize: 10, color: C.muted, align: "center", lineSpacing: 16 });
    if (i < 4) {
      s.addText("→", { x: x + 2.13, y: 2.9, w: 0.4, h: 0.4, fontFace: F, fontSize: 15, bold: true, color: C.orangeDeep, align: "center", margin: 0 });
    }
  });
  // 回流箭头说明
  txt(s, "◀ 验证闭环后回到第 1 步——下一轮计划从上一轮教训开始", MW, 4.35, CW, 0.4, { fontSize: 11.5, bold: true, color: C.orangeDeep, align: "center" });
  card(s, MW, 4.95, 12.33, 1.7);
  cardTitle(s, MW + 0.25, 5.15, "为什么这个闭环能滚起来", 11.5);
  txt(s, [
    { text: "每一轮都留下两样东西：", options: { bold: true } },
    { text: "内容增量（讲义/概念）+ 规则增量（新条款/新工具/新 lesson）。", options: {} },
    { text: "规则增量让同类错误在下一轮被工具拦住，", options: { bold: true } },
    { text: "于是出错率随轮次下降——积累的不仅是知识，更是'不再犯错的机制'。", options: {} }
  ], MW + 0.25, 5.75, 11.85, 0.75, { fontSize: 12, lineSpacing: 18 });
  foot(s, 14);
  s.addNotes("这是'如何积累'的核心答案：不是'我记住了教训'，而是'教训被固化成了规则与工具，下次机器直接拦住'。所以每一轮都比上一轮更不容易出错。");
}

/* ================================================================ */
/* S15 错误是原料                                                   */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 15, "第三部分 · 经验与积累机制", "错误是原料，不是成本——每条错都变成一条规则");
  card(s, MW, 1.95, 6.04, 3.9);
  cardTitle(s, MW + 0.25, 2.2, "带圈数字：两次替换 509 处，仍然复发", 5.2);
  txt(s, [
    { text: "问题：", options: { bold: true } },
    { text: "序号用带圈数字，第一次替换 323 处，子代理写新内容又引入 186 处。", options: { breakLine: true } },
    { text: "结论：", options: { bold: true } },
    { text: "一次性替换不是治理，检查规则才是。", options: { breakLine: true } },
    { text: "固化：", options: { bold: true } },
    { text: "audit_circled_digits.py 全库审计 + 统一 (1)(2)(3) 写法。", options: {} }
  ], MW + 0.25, 2.85, 5.6, 2.3, { fontSize: 11.5, lineSpacing: 25 });
  txt(s, "此后新增任何内容先过审计，同类问题绝迹。", MW + 0.25, 4.85, 5.6, 0.4, { fontSize: 10.5, color: C.muted });
  card(s, 6.79, 1.95, 6.04, 3.9);
  cardTitle(s, 7.04, 2.2, "SVG 三次遮盖漏检：根因在工具盲区", 5.2);
  txt(s, [
    { text: "问题：", options: { bold: true } },
    { text: "旋转轴标签压行标签、Δl=9 压网格、图例被色块压住——审计工具三次 PASS。", options: { breakLine: true } },
    { text: "根因：", options: { bold: true } },
    { text: "工具不解析 rotate/polygon/豁免类，盲区上宣称了通过。", options: { breakLine: true } },
    { text: "固化：", options: { bold: true } },
    { text: "R8/R9 全元素穷举规则 + 盲区登记 + 全库回归。", options: {} }
  ], 7.04, 2.85, 5.6, 2.3, { fontSize: 11.5, lineSpacing: 25 });
  txt(s, "工具升级后必须全库回归，禁止在盲区上宣称验证通过。", 7.04, 4.85, 5.6, 0.4, { fontSize: 10.5, color: C.muted });
  s.addShape(pres.shapes.RECTANGLE, { x: MW, y: 6.1, w: 12.33, h: 0.66, fill: { color: C.cream } });
  txt(s, "机制：修复 → 固化 → 同类扫描 → 验证闭环，五步走完才算修完——「只修不固化」在项目里视为未完成。", MW + 0.25, 6.24, 11.85, 0.4, { fontSize: 11.5, bold: true, color: C.navy, align: "center", valign: "middle" });
  foot(s, 15);
  s.addNotes("两个最典型的'错误资产化'案例。共同点：不是把眼前一处改掉，而是问'为什么它会发生第二次'，答案几乎都在机制缺失，于是把机制补成工具。");
}

/* ================================================================ */
/* S16 每类错都有一道门                                             */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 16, "第三部分 · 经验与积累机制", "每类错都有一道门：验证闭环咬住质量");
  const rows = [
    ["视觉返工", "T11.1 同一张图连续四次视觉返工", "交付检查清单四查：图模型居中 / 面板边距 ≥8px / 布局密度 / 文字余量 ≥10px"],
    ["字体度量", "CSS class 字号漏检：14px 按 12px 低估，文字超边 42px 仍 PASS", "审计工具解析 CSS 样式 + 宽度 8% 安全系数 + 右缘余量"],
    ["语法渲染", "Mermaid 括号节点解析失败，Obsidian 端直接不渲染", "引号节点规则（全版本安全子集）+ 真实渲染验证 + 全库同类扫描"]
  ];
  rows.forEach(([tag, prob, fix], i) => {
    const y = 1.95 + i * 1.52;
    card(s, MW, y, 12.33, 1.36);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: MW + 0.2, y: y + 0.2, w: 1.3, h: 0.96, fill: { color: C.navy }, rectRadius: 0.08
    });
    s.addText(tag, {
      x: MW + 0.2, y: y + 0.2, w: 1.3, h: 0.96, fontFace: F, fontSize: 13, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    txt(s, [
      { text: prob, options: { color: C.ink, breakLine: true } },
      { text: "→ " + fix, options: { bold: true, color: C.navy } }
    ], MW + 1.75, y + 0.18, 10.35, 1.05, { fontSize: 11.5, lineSpacing: 17, valign: "middle" });
  });
  txt(s, "验证工具不可用时，必须显式声明为验证缺口——「没验证」永远不能默认为「通过」。", MW, 6.6, CW, 0.35, { fontSize: 11.5, bold: true, color: C.navy, align: "center" });
  foot(s, 16);
  s.addNotes("三个质量门案例，同一逻辑：每一类错误都被一道专门的验证门拦住。最后一句是红线——工具缺位时要明说没验证，而不是默认通过。");
}

/* ================================================================ */
/* S17 改全库先想三件事                                             */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 17, "第三部分 · 经验与积累机制", "改全库之前，先想三件事");
  const rows = [
    ["作用域", "批量替换误伤 11 个文件——T12.x 在 L2 与 L3 都是合法编号", "按目录限定作用域 + 「每个引用 → 目标存在」闭环验证，零缺失才算完成"],
    ["全格式", "死链只修 wikilink 一种，另两种格式照样断", "wikilink / Markdown 链接 / 相对路径三格式一次扫全，备份归档文件同样受检"],
    ["实测", "README 计数宣称 254+104，实测只有 241+105", "任何计数声明先 grep/awk 实测再写，禁止凭印象报数"]
  ];
  rows.forEach(([tag, prob, fix], i) => {
    const y = 1.95 + i * 1.52;
    card(s, MW, y, 12.33, 1.36);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: MW + 0.2, y: y + 0.2, w: 1.3, h: 0.96, fill: { color: C.navy }, rectRadius: 0.08
    });
    s.addText(tag, {
      x: MW + 0.2, y: y + 0.2, w: 1.3, h: 0.96, fontFace: F, fontSize: 13, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    txt(s, [
      { text: prob, options: { color: C.ink, breakLine: true } },
      { text: "→ " + fix, options: { bold: true, color: C.navy } }
    ], MW + 1.75, y + 0.18, 10.35, 1.05, { fontSize: 11.5, lineSpacing: 17, valign: "middle" });
  });
  txt(s, "批量操作的第一问不是「怎么改」，而是「改的范围边界在哪」。", MW, 6.6, CW, 0.35, { fontSize: 11.5, bold: true, color: C.navy, align: "center" });
  foot(s, 17);
  s.addNotes("大规模改动的三条纪律：先问边界、全格式、实测数。都是被真实事故逼出来的——批量操作省下的时间，远不够填误伤的坑。");
}

/* ================================================================ */
/* S18 AI 协作分工                                                  */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 18, "第三部分 · 经验与积累机制", "AI 在环内执行，人在环上定标准");
  card(s, MW, 1.95, 5.7, 4.55);
  cardTitle(s, MW + 0.25, 2.2, "分工：各干各最擅长的", 4.9);
  const rows = [
    ["人（环上）", "拷问定标准 · 口径取舍 · 验收把关", C.navy],
    ["AI（环内）", "检索 · 批量执行 · 审计验证 · 经验固化", C.orangeDeep]
  ];
  rows.forEach(([t, d, col], i) => {
    const y = 2.8 + i * 1.15;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: MW + 0.25, y, w: 1.75, h: 0.85, fill: { color: col }, rectRadius: 0.08 });
    s.addText(t, {
      x: MW + 0.25, y, w: 1.75, h: 0.85, fontFace: F, fontSize: 13, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    txt(s, d, MW + 2.2, y + 0.1, 3.2, 0.7, { fontSize: 11.5, lineSpacing: 16, valign: "middle" });
  });
  txt(s, "AI 提效的落点是执行与验证，不是替人做标准决策——先拷问，再动手。", MW + 0.25, 5.5, 5.2, 0.8, { fontSize: 11, color: C.muted, lineSpacing: 15 });
  card(s, 6.5, 1.95, 6.33, 4.55);
  cardTitle(s, 6.75, 2.2, "一次拷问，揪出 5 处计划漏洞", 5.5);
  txt(s, [
    { text: "一次「协议栈与 OSI」入库任务，动手前先拷问一轮，实际发现 5 处计划漏洞：", options: {} }
  ], 6.75, 2.8, 5.85, 0.65, { fontSize: 11.5, lineSpacing: 16 });
  const holes = ["术语中文名不一致", "索引区格式错误", "LTE / NR 双侧缺失", "主线桥接缺失", "工具扩展未决策"];
  holes.forEach((h, i) => {
    const x = 6.75 + (i % 2) * 2.95, y = 3.5 + Math.floor(i / 2) * 0.75;
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 2.75, h: 0.6, fill: { color: C.panel } });
    txt(s, h, x + 0.15, y + 0.08, 2.45, 0.45, { fontSize: 10.5, color: C.ink, valign: "middle" });
  });
  txt(s, "如果直接开工，这 5 处会在交付后变成 5 次返工。", 6.75, 5.75, 5.85, 0.4, { fontSize: 10.5, color: C.muted });
  foot(s, 18);
  s.addNotes("AI 协作的正确姿势：把'定标准'的决策权留给人（拷问），把执行、验证、固化交给 AI。拷问的价值有实测证据——一次拷问在开工前拦下 5 个返工点。");
}

/* ================================================================ */
/* S19 经验随项目走                                                 */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 19, "第三部分 · 经验与积累机制", "经验随项目走：拷贝文件夹，规则不失效");
  const rows = [
    ["双份维护", "项目内 docs/memory 与 lessons 是权威副本", "~/.claude 仅作会话加载镜像；方向永远「项目内 → 镜像」，项目文件夹拷贝到哪，经验跟到哪"],
    ["规则随行", "CLAUDE.md、规则总纲、SKILL 执行体、审计工具", "全部在项目文件夹内随行演进；全局规则也有项目内镜像副本，拷贝后全局约束不失效"],
    ["双推备份", "git push origin master 一次双推", "Gitee + GitHub 双仓库（GitHub 走 ssh.github.com:443），换机一条命令链恢复"]
  ];
  rows.forEach(([t, a, b], i) => {
    const y = 1.95 + i * 1.42;
    card(s, MW, y, 12.33, 1.26);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: MW + 0.2, y: y + 0.22, w: 1.5, h: 0.82, fill: { color: C.navy }, rectRadius: 0.08
    });
    s.addText(t, {
      x: MW + 0.2, y: y + 0.22, w: 1.5, h: 0.82, fontFace: F, fontSize: 12.5, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    txt(s, [
      { text: a + "：", options: { bold: true, color: C.ink, breakLine: true } },
      { text: b, options: { color: C.muted } }
    ], MW + 1.95, y + 0.14, 10.15, 1.0, { fontSize: 11.5, lineSpacing: 15, valign: "middle" });
  });
  txt(s, "2026-09-03 起落地：工作区拷到任何机器，规则、记忆、技能三样都不失效。", MW, 6.45, CW, 0.35, { fontSize: 11.5, bold: true, color: C.navy, align: "center" });
  foot(s, 19);
  s.addNotes("经验的'可携带性'治理：项目文件夹是经验的家，不是某一台机器的家。三条措施让经验跟着项目走，而不是跟着会话走。");
}

/* ================================================================ */
/* S20 怎么用                                                       */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 20, "第四部分 · 使用 · 不足 · 收束", "怎么用：跟着编号走，问着问题走");
  card(s, MW, 1.95, 6.04, 4.35);
  cardTitle(s, MW + 0.25, 2.2, "阅读路径：零基础顺着编号读", 5.2);
  txt(s, [
    { text: "L0 引导：", options: { bold: true } },
    { text: "先学会协议怎么读，术语表备查", options: { breakLine: true } },
    { text: "L1 → L2 → L3：", options: { bold: true } },
    { text: "每篇开头有「前置知识检查」，", options: { breakLine: true } },
    { text: "不够就退回上一层补", options: { breakLine: true } },
    { text: "遇到概念：", options: { bold: true } },
    { text: "点 wikilink 进概念笔记，", options: { breakLine: true } },
    { text: "六段式里找直观模型与常见误解", options: {} }
  ], MW + 0.25, 2.85, 5.6, 2.6, { fontSize: 12, lineSpacing: 24 });
  txt(s, "想验证学到哪：做篇末例题，对照参考答案。", MW + 0.25, 5.2, 5.6, 0.5, { fontSize: 10.5, color: C.muted });
  card(s, 6.79, 1.95, 6.04, 4.35);
  cardTitle(s, 7.04, 2.2, "问答路径：库是活的", 5.2);
  txt(s, [
    { text: "提一个问题，流水线先检索再回答：", options: {} },
    { text: "老问题 → 扩充打磨；新问题 → 新建概念笔记", options: { bold: true, breakLine: true } },
    { text: "回答骨架：定位 → 协议族分布 → 原理 → 要点 → 关联", options: { breakLine: true } },
    { text: "高频查询排名表告诉你哪些概念最值得先吃透", options: {} }
  ], 7.04, 2.85, 5.6, 2.0, { fontSize: 12, lineSpacing: 24 });
  txt(s, "每次问答都会沉淀回库——问题越问，库越厚。", 7.04, 5.2, 5.6, 0.5, { fontSize: 10.5, color: C.muted });
  foot(s, 20);
  s.addNotes("使用方式两条：静态的阅读路径（编号+前置检查保证零基础可用），动态的问答路径（Q&A 流水线让库随使用增长）。");
}

/* ================================================================ */
/* S21 当前不足                                                     */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 21, "第四部分 · 使用 · 不足 · 收束", "如实说不足：这座库还缺什么");
  const gaps = [
    ["L3 后半段未写透", "接收链工程预算与后端（T21-T23）仍在展开，四道瀑布的「验证」一档内容最薄"],
    ["教材化未完成", "讲义是按层组织的库，还不是一本按章排序的书——从库到书还差一次重组"],
    ["queries 未全库回填", "高频排名仅覆盖 13 篇概念笔记，存量笔记按口径暂不回填"],
    ["审计工具仍有盲区", "rotate / 复杂曲线等场景依赖人工核查，工具每次升级需要全库回归"],
    ["链路级仿真偏少", "目前以 numpy 单元验证为主，缺端到端译码链路的系统级仿真实验"]
  ];
  gaps.forEach(([t, d], i) => {
    const y = 1.95 + i * 0.91;
    s.addShape(pres.shapes.RECTANGLE, { x: MW, y, w: 12.33, h: 0.78, fill: { color: C.white }, line: { color: C.line, width: 0.75 }, shadow: shd() });
    s.addShape(pres.shapes.RECTANGLE, { x: MW, y, w: 0.07, h: 0.78, fill: { color: C.orangeDeep } });
    txt(s, [
      { text: t + "  ", options: { bold: true, color: C.navy } },
      { text: d, options: { color: C.ink } }
    ], MW + 0.35, y + 0.12, 11.7, 0.55, { fontSize: 12, valign: "middle" });
  });
  txt(s, "不足不是遮羞布——下面每条都对应一个计划动作。", MW, 6.55, CW, 0.35, { fontSize: 11, color: C.muted, align: "center" });
  foot(s, 21);
  s.addNotes("如实汇报缺口，5 条都真实存在：L3 尾部、教材化、queries 回填、工具盲区、系统级仿真。每条都在下一页有计划承接。");
}

/* ================================================================ */
/* S22 下一步计划                                                   */
/* ================================================================ */
{
  const s = pres.addSlide();
  hdr(s, 22, "第四部分 · 使用 · 不足 · 收束", "下一步：把 L3 补完，把经验复制出去");
  const plans = [
    ["1", "L3 完备化", [{ text: "补完接收链工程预算与后端专题，", options: { breakLine: true } }, { text: "闭环「浮点 → 定点 → RTL → 验证」四道瀑布", options: {} }]],
    ["2", "教材化", [{ text: "讲义重组为教材章节顺序，术语总表合并，", options: { breakLine: true } }, { text: "产出可直接阅读的成体系教材", options: {} }]],
    ["3", "体系复制", [{ text: "同一套规则 / 工具 / 沉淀机制，", options: { breakLine: true } }, { text: "迁移到 ic 数字 IC 知识库（进行中）", options: {} }]],
    ["4", "链路级仿真", [{ text: "sim 补齐端到端译码链路仿真实验，补上系统级验证短板", options: {} }]]
  ];
  plans.forEach(([n, t, d], i) => {
    const x = MW + (i % 2) * (6.04 + 0.25), y = 1.95 + Math.floor(i / 2) * 2.1;
    card(s, x, y, 6.04, 1.95);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.25, y: y + 0.22, w: 0.55, h: 0.55, fill: { color: C.orangeDeep }, rectRadius: 0.1 });
    s.addText(n, {
      x: x + 0.25, y: y + 0.22, w: 0.55, h: 0.55, fontFace: F, fontSize: 16, bold: true, color: C.white,
      align: "center", valign: "middle", margin: 0
    });
    txt(s, t, x + 1.0, y + 0.22, 4.7, 0.4, { fontSize: 16, bold: true, color: C.navy });
    txt(s, d, x + 1.0, y + 0.7, 4.8, 1.1, { fontSize: 11.5, color: C.muted, lineSpacing: 16 });
  });
  txt(s, "优先级：内容完备 > 教材化 > 体系复制——先把手头这座库盖完整。", MW, 6.4, CW, 0.35, { fontSize: 11.5, bold: true, color: C.navy, align: "center" });
  foot(s, 22);
  s.addNotes("四条计划与上一页五条不足一一对应，按优先级排序：先补 L3，再教材化，体系复制已在 ic 项目进行中，仿真短板最后补。");
}

/* ================================================================ */
/* S23 收束（深蓝底）                                               */
/* ================================================================ */
{
  const s = pres.addSlide();
  s.background = { color: C.navy };
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: MW, y: 0.45, w: 0.62, h: 0.62, fill: { color: C.orangeDeep }, rectRadius: 0.1 });
  s.addText("23", {
    x: MW, y: 0.45, w: 0.62, h: 0.62, fontFace: F, fontSize: 18, bold: true, color: C.white, align: "center", valign: "middle", margin: 0
  });
  s.addText("第四部分 · 使用 · 不足 · 收束", {
    x: 1.28, y: 0.47, w: 8, h: 0.3, fontFace: F, fontSize: 11, color: C.light, charSpacing: 2, margin: 0
  });
  s.addText("标准、验证、沉淀——三件事让知识库长出来", {
    x: MW, y: 1.18, w: CW, h: 0.66, fontFace: F, fontSize: 30, bold: true, color: C.white, margin: 0
  });
  const trio = [
    ["标准", "拷问定标准：规则 17+23 条，先想清楚再动手"],
    ["验证", "审计工具 + 目检闭环：每一类错都有一道门"],
    ["沉淀", "纠错必固化：25 条 lessons，错误变资产"]
  ];
  trio.forEach(([t, d], i) => {
    const x = MW + i * (3.94 + 0.25);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 2.4, w: 3.94, h: 2.35, fill: { color: C.navy2 } });
    s.addText(t, {
      x, y: 2.75, w: 3.94, h: 0.6, fontFace: F, fontSize: 22, bold: true, color: C.white, align: "center", margin: 0
    });
    txt(s, d, x + 0.3, 3.55, 3.34, 1.0, { fontSize: 12.5, color: C.light, align: "center", lineSpacing: 18 });
  });
  s.addText("内容会长，规则会老；但只要每一步都留下可复用的经验，这座库就能一直长下去。", {
    x: MW, y: 5.6, w: CW, h: 0.5, fontFace: F, fontSize: 15, bold: true, color: C.orangeDeep, align: "center", margin: 0
  });
  foot(s, 23, true);
  s.addNotes("收束给方法论结论：这座库真正长出来的原因不是工作量，是'标准、验证、沉淀'三件事的循环。这也是可复制到其他知识库的东西。");
}

/* ================================================================ */
/* S24 致谢（深蓝底）                                               */
/* ================================================================ */
{
  const s = pres.addSlide();
  s.background = { color: C.navy };
  s.addShape(pres.shapes.OVAL, { x: 10.6, y: 1.6, w: 3.4, h: 3.4, fill: { color: C.navy2, transparency: 30 } });
  s.addShape(pres.shapes.OVAL, { x: 11.7, y: 4.9, w: 2.4, h: 2.4, fill: { color: C.navy2, transparency: 45 } });
  s.addShape(pres.shapes.OVAL, { x: 10.05, y: 2.15, w: 0.2, h: 0.2, fill: { color: C.orangeDeep } });
  s.addText("谢谢", {
    x: MW, y: 2.3, w: 8, h: 1.3, fontFace: F, fontSize: 60, bold: true, color: C.white, margin: 0
  });
  s.addText("欢迎提问与交流", {
    x: MW, y: 3.8, w: 8, h: 0.6, fontFace: F, fontSize: 20, color: C.light, margin: 0
  });
  s.addText([
    { text: "仓库：Gitee · GitHub — aurorayaus/obsidian", options: { breakLine: true } },
    { text: "本演示稿：docs/slides/3gpp_kb_intro.pptx", options: {} }
  ], {
    x: MW, y: 4.75, w: 9, h: 0.9, fontFace: F, fontSize: 12, color: C.light, lineSpacing: 20, margin: 0
  });
  foot(s, 24, true);
  s.addNotes("结束页。留仓库地址，欢迎提问。");
}

/* ============ 生成 ============ */
pres.writeFile({ fileName: "3gpp_kb_intro.pptx" }).then((f) => {
  console.log("OK:", f);
}).catch((e) => {
  console.error("FAIL:", e);
  process.exit(1);
});
