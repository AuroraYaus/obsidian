# Plan: 3gpp 知识库审核整改（2026-08-14 审核 → grill-me 拷问锁定版）

_Locked via grill — by Claude + AuroraYaus（2026-08-14）_

## Goal

对 2026-08-14 全库审核发现的七类问题一次性整改：规则文件自指失准、规则文件结构缺陷、M16 编号失守、模板与审计工具脱节、LaTeX 渲染失败、术语审计豁免缺口、仓库工程问题（3GB 拆仓 + .obsidian untrack）。整改后全库审计套件恢复全绿（讲义层口径），并建立"数字写死 + 同步清单强制"的防漂移机制。

## Approach

### Phase 0：拆仓准备（依赖用户外部动作）

1. **用户动作**：在 Gitee 新建协议数据仓（建议名 `obsidian-3gpp-protocol-data`，私有）。
2. 初始化数据仓：`3GPP_Rel19/`（archive/specs/processed/manifest.csv/下载清单）整体复制为数据仓内容，git init + 初始 commit。
3. 数据仓双推：origin 配 Gitee + GitHub 双 pushurl（GitHub 远端为新建空仓）；首次全量 2.6GB/81k 文件走 GitHub Import 服务器中转（沿用既有流程），Gitee 直接推。
4. 验证数据仓完整性（文件数 81342+ 对齐、`git ls-tree -r HEAD | wc -l` 核对），**通过前主仓不动 3GPP_Rel19**。

### Phase 1：Commit 1 — 编号改名 `refactor(lectures)`

5. `docs/L2_协议算法/M16.1-4_*.md` → `T16.1-4_*.md`（`git mv`）。
6. 全库引用更新（13 文件 119 处，按目录限定作用域）：4 个文件本体（标题/别名/正文/source_spec）、`T0.1` 阅读地图（`[[T16.1_scheduler_HARQ_process|M16 调度]]` 等锚点）、`L2_协议算法入口.md`、6 个概念笔记、`2026-08-13-m16-schedule-harq-beam-ca-mac.md` 设计文档。
7. **改名存在性闭环**（批量替换规则强制）：全库 `M16.` 仅剩 L3 模块号语境（`L3_工程实现入口.md` 的"## M16 接收链路工程预算"）；每个 `T16.` 引用均有对应文件存在。
8. `项目规则与记忆索引.md` 编号约定节更新：区间改为 **L2 占 T6-T16、L3 占 T17-T23**；碰撞警告表**补登记 M16**（L2 M16 = MAC 调度系列 / L3 M16 = 接收链路工程预算，跨层引用必须带层名）；注明 T2.4/T15.1 缺口为历史合并产物（T2.4→T2.2、T15.1→T15.5）。
9. 本 commit 验收：`audit_link_integrity.py` + `audit_circled_digits.py` + 存在性闭环。

### Phase 2：Commit 2 — 规则/README 统一 `docs(rules)`

10. `3gpp/CLAUDE.md`：§2 讲义数改为 **153**（L0 1 + L1 46 + L2 70 + L3 36，口径 = 仅 `type: algorithm` 讲义，另含入口/术语 spec 文件 6 个）；§4/§9 SVG 表述统一为 **R1-R11**；§12 经验库"10 条"→"**21 条**"；**章节编号重排**（现 1-10→12→11→13-15，"经验教训库"与"合规基线"对调回 11/12 顺序）。
11. `项目规则与记忆索引.md`：**章节重排**（六、七挪到五之后）；**两个"五、编号约定"合并为一节**；§七 lessons"16 条"→"21 条"+ 补登记 `lesson-skill-first-check`、`lesson-svg-render-verify-before-commit`；规则表"22 条 Hard Constraints"→"**23 条**"；同步清单六.6 豁免判据补 (h) T0.1 阅读地图整文件 (i) 概念笔记整文件 (j) `docs/superpowers/`+`docs/audits/` 台账；第 8 条 .obsidian 改写（workspace/graph untrack 后删旧路径自愈说明）。
12. 工作区根 `CLAUDE.md`："22 条 Hard Constraints"→"23 条"。
13. 三份 README（`README.md`/`README.en.md`/`3gpp/README.md`）统一：讲义 **153 + 6 spec 说明**；概念笔记 **106**；术语 **254 + 概念索引 104**；"22 条"→"23 条"；"R1-R7"→"R1-R11"；结构树口径一致（中英文同步）。
14. `L0_terminology_glossary.md` 概念索引段"104 篇"→"106 篇"。

### Phase 3：Commit 3 — 工具治理 `fix(tools)`

15. `tools/audit_lesson_depth.py`：必检章节移除"自测题/自测题参考答案"；**L3 分层指标**——`docs/L3_工程实现/` 讲义理论信号阈值放宽（15→8），protocol-index risk 在 L3 仅 WARN 不阻断（工程篇主题为综合/功耗/后端，协议理论少属主题性质；实现与口径写入工具 @note 固化）。
16. `tools/audit_term_first_use.py`：EXEMPT 常量补 T0.1、`docs/concepts/`、`docs/superpowers/`、`docs/audits/`；验收口径 = **L1/L2/L3 讲义层必须 PASS**（写入 @note）。
17. `.claude/rules/documentation.md`：§2.2 写明"自测题为可选（示范/引导/独立习题 3+3+3 已覆盖检验职能，重复设自测题有凑字数之嫌）；`## 资料与协议边界` 为必选"；§四 R1-R7→R1-R11。
18. `合规与遵从.md` Rule 20 补一条：`\tag` 禁止出现在 `aligned`/`gather` 等子环境内（KaTeX 不支持，教训来源 T1.4:333）。
19. 本 commit 验收：工具自身语法 + 跑一遍确认新口径生效。

### Phase 4：Commit 4 — 内容修复 `docs(lectures)`

20. **LaTeX 修复**（1 处）：`T1.4:333` 拆为两个独立双美元围栏块，各自保留 tag 编号 17/18；全库同类扫描（grep `aligned`/`gather` 内 `\tag` 模式）确认无存量；`audit_latex_render.py` 全库 PASS。
21. **补"资料与协议边界"章节**（31 篇，每篇一小节，表格或短段落，禁止注水）：TX1-5、T14.1-5、T15.2-5、T16.1-4、T22.1-4、T23.1-3（新批次 26 篇）+ T2.7、T9.7、T9.8、T10.9、T11.4（旧篇 5 篇）。内容口径：协议规定什么 / 不规定什么（实现域）/ 接收端义务边界。
22. **协议索引化定向补写**（5 篇，各 100-200 行实义内容）：T2.5、T2.6、T9.8、T15.4、T11.4 补"本节主角为什么需要它 / 最小可手算模型"小节；每篇补写后单篇重跑 depth 审计确认 TRIAGE 消除。
23. **T18.3、T21.6**：按 Phase 3 新 L3 口径重估——通过则不动，仍 TRIAGE 则同法补写。
24. 本 commit 验收：`audit_latex_render.py` PASS + `audit_lesson_depth.py`（新口径，讲义层 TRIAGE 清零）+ 术语审计讲义层 PASS。

### Phase 5：Commit 5 — 工程治理 `chore(repo)`

25. `.obsidian/workspace.json`、`.obsidian/graph.json`：`git rm --cached` + 写入 `.gitignore`（保留 app.json/appearance.json/core-plugins.json/snippets 配置类）；同步清单第 8 条已随 Phase 2 改写。
26. 主仓 `git rm -r --cached 3GPP_Rel19` + `.gitignore` 追加 `3gpp/3GPP_Rel19/`；README 增加"协议证据数据可选下载：将数据仓 clone 到 `3gpp/3GPP_Rel19/` 即复原讲义锚点"说明（三份 README 同步）。**仅在 Phase 0 数据仓推送并验证完成后执行**。
27. 提交：每 commit 后 `git push origin master`（双推）。

### Phase 6：全库验收（收尾）

28. 验收套件：`audit_link_integrity.py` / `audit_circled_digits.py` / `audit_markdown_headings.py docs/` / `audit_mermaid_syntax.sh` / `audit_latex_render.py` / `audit_lesson_terms.py` / `audit_term_first_use.py`（讲义层）/ `audit_lesson_depth.py`（新口径）/ `audit_project_image_inventory.py`。
29. 数字复核：讲义 153、概念 106、术语 254 + 索引 104、HC 23、lessons 21、R1-R11 与三份 README + 规则文件逐项一致。
30. 经验固化：审核整改本身如产生新教训（如"命名约定被工具依赖"），登记 `docs/audits/lessons/` + 索引第七节 + 双推。

## Key decisions & tradeoffs

| 决策点 | 结论 | 理由 |
|:---|:---|:---|
| 整改范围 | 一次性全量（七类），3GB 拆仓/T23 深度作为独立议题收敛 | (1)-(6) 低风险机械修改；(7) 需要单独慎重但同批收敛 |
| M16 处置 | 文件改名 T16.1-4；区间改 L2 T6-T16 / L3 T17-T23；模块号双义按 M12/M13 先例登记碰撞警告 | T16 空置可回收；回归 T*.md 约定使深度审计自动恢复覆盖（不改工具扫描）；消除双义需动 L3 台账且占掉 M17 预留号 |
| 讲义数口径 | 153 = 仅 `type: algorithm`；入口/术语 6 个 spec 文件单独注明；数字写死 + 同步清单强制 | 入口文件从讲义数剥离才能让数字可复算；不引入自动统计脚本（过度工程） |
| 模板 vs 工具 | 自测题降可选（工具移除必检）；"资料与协议边界"升必选并补齐 31 篇 | 习题 3+3+3 已覆盖检验职能，再设自测题是刚整治过的凑字数路子；边界章节对 Rule 7/19 有实义 |
| LaTeX 修法 | 拆两个独立双美元围栏块保留 tag 编号；Rule 20 固化禁令 | 编号语义不丢、审计连续性检查继续有效；工具已能检出无需新工具 |
| 术语豁免 | T0.1/概念笔记/superpowers/audits 整文件（目录）豁免；验收口径改为讲义层 PASS | 概念笔记是术语定义文件本体，"自己给自己配对"是怪文；设计文档/台账是内部工作文档 |
| T22/T23 深度 | 工具按层分级（L3 理论信号阈值 15→8、protocol-index 仅 WARN）+ L1/L2 五篇定向补写 + T18.3/T21.6 按新口径重估 | T23 三篇主题独立非凑行数，合并不当；风险在 L1/L2 协议索引化而非 L3 工程篇 |
| 3GB 处置 | 拆独立数据仓双推；主仓 rm --cached + gitignore；**历史 639MB 保留，不 filter-repo 不强推** | 双端 force push 风险大于收益；证据链路对读者可选复原（路径前缀不变）；无 >100MB 文件拆仓可行 |
| .obsidian | untrack workspace.json + graph.json；保留 app/appearance/core-plugins/snippets | 前者纯 UI 状态必 dirty，后者是跨机器配置与自研样式 |
| 提交方式 | 5 个主题 commit（改名/规则/工具/内容/工程），每 commit 双推 | 便于回溯与 review；改名与内容修改不混在一起 |

## Risks / open questions

- **拆仓依赖用户外部动作**（Gitee 建仓）；数据仓首次推送 2.6GB/81k 文件耗时长，GitHub Import 中转若失败需改用 ssh.github.com:443 直推（慢）。
- 31 篇边界章节 + 5 篇理论补写的质量以"实义不注水"为准，验收时逐篇目检，不能只跑审计。
- T18.3/T21.6 重估结果未定：若新口径下仍 TRIAGE 则补写（工作量为浮动项）。
- 术语豁免扩宽后，讲义层必须仍 PASS——豁免清单若写得过宽（如误伤 L2 讲义同路径前缀）需回退。
- 深度审计新口径（L3 阈值 8）是本次设定值，若后续新增 L3 讲义仍需微调。
- SVG 全库几何审计（R1-R11 逐图）与 PlantUML 审计、sim/tests（pytest 未装）不在本次验收范围，作为已知验证缺口留存。

## Out of scope

- `git filter-repo` 历史重写与双端 force push（明确不做）。
- T23.1-3 合并（明确不做，主题独立）。
- 概念笔记薄篇（TB/Turbo 码/TDL 等）补写（本次不动，仅登记观察）。
- Python 绘图政策、SVG 资产调整（本次整改不触及图片资产）。

## 追加批次：frontmatter type 治理（2026-08-14 下午 grill 锁定）

**决策（2 问收敛）**：全库规范化 + 工具化防复发——76 篇误标修正（L1 41 篇 definition→algorithm、L3 24 篇 spec→algorithm、L2 T9.8/T10.9 两篇 spec→algorithm、9 个概念笔记 algorithm→definition）；新建 `tools/audit_frontmatter_types.py`（讲义 T/TX=algorithm / 概念 English_中文=definition / 入口规则术语表=spec，audits/superpowers/清单豁免）；documentation.md §2.1 语义写死；映射表登记。
