# obsidian — 3GPP LTE/NR 译码链路全栈教学知识库

3GPP LTE/NR 译码链路的全栈教学 Obsidian 知识库：从数学基础、物理层链路、信道编码算法，到浮点仿真、定点模型、RTL 微架构与验证，打通「理论推导 → 算法 → 硬件实现」的完整路径。

## 仓库结构

```
├── 3gpp/                      # 核心知识库（讲义/概念/审计/工具）
│   ├── docs/L0_协议阅读引导/    # 协议阅读地图、术语总表（255 术语 + 114 概念索引）
│   ├── docs/L1_基础/           # 数学基础、OFDM 与软解调、CRC/分段、译码理论、硬件基础
│   ├── docs/L2_协议算法/       # 译码协议算法（Turbo/LDPC/Polar）、MIMO 接收、概率整形
│   ├── docs/L3_工程实现/       # 译码器工程（仿真/定点/RTL/验证）、接收链路工程预算
│   ├── docs/concepts/          # 概念图谱（114 概念笔记，六段式模板）
│   ├── docs/audits/            # 审计台账、经验教训库（23 条）与评审
│   ├── sim/ tools/ tests/      # Python 仿真、审计工具链、单元测试
│   ├── CLAUDE.md               # 会话硬性规则（15 条）
│   ├── 合规与遵从.md            # 23 条 Hard Constraints
│   ├── 项目规则与记忆索引.md     # 规则/写作规范/同步清单一处总览
│   └── README.md               # 知识库详细说明
├── .obsidian/                 # Obsidian 应用配置
└── 3gpp/3GPP_Rel19/           # 协议证据数据（可选 clone，见「协议证据数据」）
```

## 快速开始

1. **详细说明**：见 [`3gpp/README.md`](3gpp/README.md)（知识库结构/讲义体系/阅读路径/质量体系）
2. **阅读总入口**：`3gpp/docs/3GPP_讲义入口.md`
3. **术语速查**：`3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`
4. **讲义体系**：L1 基础（T1-T5 + TX1-TX5 发送端镜像）→ L2 协议算法（M6-M16：译码/控制面/上行/调度）→ L3 工程实现（T17-T23：译码器/接收链/后端），全部完成 ✅（156 讲义 + 6 入口/术语文件 + 114 概念笔记）

## 质量体系

- 合规基线：23 条 Hard Constraints（`3gpp/合规与遵从.md`）
- SVG 图强制验证：几何审计 R1-R11（含边界间距 ≥8px、重叠禁止）
- 讲义审计：术语配对 / LaTeX 渲染 / 深度 / 标题
- 代码注释：DOXYGEN 风格强制
- 经验教训库：`3gpp/docs/audits/lessons/`（23 条，纠错必固化、随库双推保存）
- 全库同步：术语/入口/编号/资产/路径/台账等八类同步清单（`3gpp/项目规则与记忆索引.md` 第六节）

## 使用说明

本仓库是一个 **Obsidian 知识库（vault）**，推荐用 Obsidian 打开以获得完整体验（`[[wikilink]]` 图谱导航、双链跳转、关系图谱）。

### Obsidian 下载与安装

| 平台 | 下载方式 |
|---|---|
| **官网（推荐）** | 访问 [obsidian.md](https://obsidian.md/) → 页面右侧 **Download** 按钮；或直接打开 [obsidian.md/download](https://obsidian.md/download) 按平台选择 |
| Windows | 官网下载 `.exe` 安装包（或 Microsoft Store 搜索 "Obsidian"） |
| macOS | 官网下载 `.dmg`（或 App Store 搜索 "Obsidian"） |
| Linux | 官网提供 AppImage / Snap / Flatpak / deb / rpm（Debian/Ubuntu 可用 `snap install obsidian`） |
| iOS / Android | App Store / Google Play 搜索 "Obsidian"（移动端可同步阅读） |

> Obsidian 个人使用**免费**（商用需订阅）；vault 就是一个普通文件夹，克隆本仓库后**直接「打开文件夹作为仓库」**即可，无需额外配置。

### 打开本知识库

1. 克隆仓库：`git clone https://gitee.com/aurorayaus/obsidian.git`
2. 打开 Obsidian → **Open folder as vault** → 选择克隆下来的 `obsidian` 文件夹
3. 从 `3gpp/docs/3GPP_讲义入口.md` 开始阅读；左侧文件树按 `L0_协议阅读引导 → L1_基础 → L2_协议算法 → L3_工程实现` 层级浏览

- 讲义正文包含内嵌 numpy 验证代码，可独立运行复现数值结论
- 概念层与讲义层双向链接，概念笔记为独立可读的六段式教学单元

## 协议证据数据

`3gpp/3GPP_Rel19/` 存放 Rel-19 协议原文与结构化抽取（讲义协议锚点的本地引用源）。该目录已拆分至**独立数据仓**（Gitee `gitee.com/aurorayaus/3gpp_docs`，GitHub 镜像 `AuroraYaus/3gpp_docs`），主仓不再跟踪；需要时可复原：

```bash
git clone https://gitee.com/aurorayaus/3gpp_docs.git 3gpp/3GPP_Rel19
```

## 参与贡献

1. 新增内容（概念笔记/讲义/术语）必须对照同步清单逐项完成
2. 代码必须 DOXYGEN 注释 + 测试通过
3. 提交后推送（gitee 2FA 账号需私人令牌）
