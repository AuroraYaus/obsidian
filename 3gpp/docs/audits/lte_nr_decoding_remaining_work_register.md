---
type: spec
aliases:
  - lte nr decoding remaining work register
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/lte_nr_decoding_remaining_work_register.md"
---
# LTE/NR Decoding Remaining Work Register

> 用途：记录当前未收尾工作、全项目审查、模块 8-15 编写、L2/L3 总体审查和最终交付事项。每完成一项，必须勾选对应 checkbox，并在“完成记录”中追加证据。  
> 范围：`docs/L1`、`docs/L2`、后续 `docs/L3`，以及路线图、合规规则、审计脚本、图表资产。  
> 当前状态：L1 已补齐 roadmap T0.1-T5 共 28 篇，L2 已完成 T6-T11 并补充 T8.0/T9.0 专题共 43 篇，L3 已完成 T12-T15 共 23 篇；当前共有 94 篇讲义、68 张 PNG、58 个 Python 文件（57 个 `render_*.py` 绘图脚本和 1 个共享 helper）。T15.6 已明确真实工程签核状态为 `hold`，因为仓库还没有真实完整 BLER、定点、RTL、coverage、DC、STA 和功耗证据。

## 执行规则

以下 checkbox 表示后续持续遵守的工作规则，不是阶段性完成项；未勾选不代表当前 L1/L2 文档收尾未完成。

- [x] 每开始一个任务前，先确认本文件中的断点和依赖。
- [x] 每完成一个讲义小节，更新本文件对应 checkbox。
- [x] 每完成一个讲义小节，在讲义末尾“执行与证据记录”写入协议来源、脚本、图片、审计命令和结果。
- [x] 每完成一个模块，运行该模块的术语、标题、深度、LaTeX、引用重建和 Prompt 覆盖审计。
- [x] 每完成一个模块，安排审核经理或等价复核，修复 Critical/Important 问题后再进入下一模块。
- [x] 遇到用户新增全局规则，先写入 `合规与遵从.md` 和路线图，再继续执行。
- [x] 新问题默认作为并行子任务处理，不自动中断旧任务；必要时启动子代理全力执行新问题或独立审计面，同时主任务按断点持续推进；若用户明确暂停/停止/切换，按用户最新指令执行。
- [x] Python 图形连线必须按节点相对位置选择真实边界端点，禁止机械地全部从右侧或左侧出线；端点不得进入节点、越过节点边缘或靠遮罩隐藏错误。
- [x] Python 图片新增、修改、重生成和全项目逐图审核时，必须把四项视觉几何规则作为独立硬性结论记录：字体与上下边框的距离、相邻边框之间的距离、箭头是否正常、连线起始和终止位置是否合理。四项不能合并写成“无遮挡”“几何正常”“目检通过”；每张图都要逐区块检查节点、卡片、表格、说明框、图例、底部区域和密集连线区，确认文字没有贴上/下边框，外边框之间有明确间隔，箭头方向/头部/线宽正常，连线从符合读图方向的真实边界出发并到达目标真实边界。
- [x] Python 图片连线锚点必须优先落在文本框对应边的中点；同一文本框存在多条入线或出线时，锚点必须围绕该边中点等距对称分布，或按读图方向使用上下/左右边中点的对称组合。禁止从框内、角点、任意偏移点或旧坐标出线，禁止多个箭头在同一框边上视觉拥挤或不对称。修改文本框尺寸、位置或箭头数量后，必须重新计算锚点并全图复检。`T12.1_golden_model_project_layout.png` 暴露过多出线文本框未按中点/对称锚点组织的问题，后续按全局缺陷处理。
- [x] Python 图片普通流程箭头默认必须使用直线连接，不能为了“看起来规整”擅自改成折线或曲线。只有直线会穿过无关模块、表格或文字时才允许折线/曲线避让，并必须记录原因。`T12.1_golden_model_project_layout.png` 曾出现将中点/对称锚点要求误改成折线的问题，后续同类修复必须保持直线优先。
- [x] Python 图片横向宽聚合框、总线框、fanout/fanin 框不能用跨越大半张图的长斜线硬连到框边中点来迁就旧坐标。若长斜线穿过视觉中心、压近正文或使箭头形状难以判断，必须优先重排布局，让源框与聚合框中心线对齐，采用上下边中点竖直直连或短直连；修改布局后必须同步更新全部连线调用并重新目视整图。`T12.1_golden_model_project_layout.png` 曾在端点数学正确后仍因宽 Artifact Fanout 长斜线造成读图疑义，后续按全局布局缺陷处理。
- [x] Python 图片箭头头部必须沿实际连线向量绘制，不能用水平/垂直箭头头部逻辑套到斜线。斜向箭头必须用单位方向向量和法向量计算头部，使箭头形状与直线方向匹配。三角箭头两个翼点也必须围绕同一个向量回退点，用最终线段法向量对称展开，禁止固定 `±x/±y` 偏移或角度模板导致头部和线身不可审计。`T12.1_golden_model_project_layout.png` 曾暴露箭头头部与斜直线不匹配的问题，后续按全局缺陷处理。
- [x] Python 图片箭头形状必须与实际路径类型一致。直线连接必须视觉上保持直线；折线/避让线必须由清晰直线段组成，箭头头部只跟最后一段方向一致，并记录避让原因。禁止用 `joint="curve"`、Bezier、弧线、遮罩或分段错位把普通流程线画成似直非直的曲线。`T12.1_golden_model_project_layout.png` 和 `T14.4_unified_decoder_subsystem_architecture.png` 本轮已按此规则复核和修复，后续按全局缺陷处理。最新加硬：普通箭头 helper 若画三角箭头头部，必须能看到 start/end 或最后一段向量方向计算；固定方向三角形 helper 已按全局缺陷处理，`T7.5_LTE_DL_UL_decoder_context.png` 与 `T14.1_LTE_Turbo_RTL_microarchitecture.png` 已重生成并通过全项目几何/可读性审计。
- [x] Python 图片静态几何审计必须覆盖普通 `arrow()`、`connect_arrow()`、`arrow_between()` 等 helper 内的曲线、弧线、Bezier、`joint="curve"`、命名多点路径变量和未标注多段路径风险；普通流程箭头 helper 应保持两点直线 shaft。需要折线避让时，必须使用明确命名的避让 helper，函数名、调用点或资产清单必须说明避让原因，并配合 segment-rectangle 相交断言或等价检查。该规则用于防止再次出现“箭头形状和直线部分不匹配”“看起来不是直线但记录写直线”的漏检。
- [x] Python 图片表格必须按文档缩放后的阅读尺寸设计，发现表格字体偏小应优先拆表、加宽画布、增加行高或改成长图，不得用压缩字号解决信息密度问题；后续全项目图像审查必须纳入表格字号可读性。该规则是全项目规则，不只修当前被指出图片；除坐标轴刻度、码位小标签、环形缓存短索引等明确辅助标注外，表格正文、表头、首列、图例和说明框教学文字原则上不得低于 24px，表格行高原则上不得低于 56px。20-23px 只允许作为辅助索引/刻度/短地址标注，并且必须有更大字号的说明区补偿。凡表格字体、首列、表头、图例或说明文字在 Markdown 常用阅读宽度下显得过小，即使无遮挡，也必须记录为视觉审计缺陷并修复。`tools/audit_figure_readability.py` 用于静态定位表格字号/行高风险；该脚本输出 findings 是整改队列，不等同于最终失败清单，仍需逐图目检分类。
- [x] Python 图片节点、标签、说明框、图例、提示框、文本框和表格单元格内文字默认必须水平和垂直居中；只有明确作为正文段落排版的长说明才允许左对齐，并必须在目检记录中确认行距、内边距和局部留白。
- [x] Python 图片审计不得只依赖脚本成功、像素边界检查或粗略目检；每张图必须逐图检查底部说明框、脚注、图例、caption、表格块、“读图顺序”“要点”“风险”“工程检测点”等局部面板的水平/垂直居中、内边距、底部留白、标题/正文间距、相邻图元间距和缩放后观感。底部说明框、脚注或读图顺序块若使用固定 y 坐标或手写逐行递增，必须改成 bbox-based 居中/自适应布局或等价 helper；发现问题按局部视觉审计漏检记录。
- [x] 后续图片新增、重生成或脚本修改时，必须运行 `python3 tools/audit_figure_geometry.py --focus-only tools/figures` 或对应范围的静态几何风险审计；若有 findings，必须修复脚本或记录安全例外，并用 `docs/audits/python_figure_visual_geometry_checklist.md` 做逐图局部视觉复核。
- [x] 图片检测规则必须覆盖“底部说明框/脚注/读图顺序/要点/风险/工程检测点”的局部几何，不得只检查整图边界、文件可打开、脚本可运行或粗略无遮挡。`T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png` 曾暴露底部文本框纵向布局失衡，后续同类图必须单独记录底部区域的文字垂直居中、下边距、标题正文间距、说明框到相邻图元间距和缩放后观感。

## 用户原始约束摘要

以下约束来自本轮执行前用户逐条交代，已经转化为阶段任务和完成记录，后续继续按同一口径执行：

- [x] 先完成当前所有工作，再开启全项目审查。
- [x] 核对所有已完成文档的 Prompt 内容是否完全覆盖，并确认正文做了适当拓展。
- [x] 审核用户提出的全局要求是否都已遵守，文档是否合规。
- [x] 按要求完成模块 8、模块 9、模块 10、模块 11。
- [x] 阶段 5 及其之后的任务必须写到每节“要做什么、怎么验收、怎么记录证据”的粒度，并在完成后回写状态。

## 完成状态标记

| 标记 | 含义 |
|:---|:---|
| `[ ]` | 未开始或未完成。 |
| `[~]` | 进行中，需要继续补写、审查或修复。 |
| `[x]` | 已完成，并已在“完成记录”中写入证据。 |
| `BLOCKED` | 卡住，必须写明阻塞原因、需要的输入和已尝试动作。 |

## 阶段 0：当前断点确认

- [x] 确认 T7.3 已重写并扩展：覆盖 Prompt、补充 HARQ 生命周期、RV 边界、LLR 概率解释、descriptor 和工业用例。
- [x] 确认 T7.3 图片已更新为长图：包含四个 RV 在 ring buffer 中的位置、RV1 LLR 流、接收端 soft buffer 写回和四个 RV 传输模型。
- [x] 确认 T7.3 图片底部说明框已缩小并与上方表格留出间隔。
- [x] 确认 T7.3 单篇审计通过：术语、标题、深度、LaTeX。
- [x] 确认全局规则已新增：Prompt 是最低覆盖线，正文必须适当拓展。
- [x] 确认 `docs/audits/prompt_coverage_matrix.md` 已生成，作为后续全项目审查基础。
- [x] 确认 T7.3 是否还需要把 Prompt 覆盖表从正文移到审计文档。
- [x] 确认 T7.3 是否需要审核经理复核。

## 阶段 1：完成当前未收尾工作

### T7.5 LTE 下行与上行译码差异

- [x] 读取 T7.5 当前正文，定位篇幅不足和 Prompt 覆盖缺口。
- [x] 对照 roadmap T7.5 Prompt，建立 T7.5 覆盖清单。
- [x] 补充 DL-SCH 与 UL-SCH 的接收端角色差异。
- [x] 补充两条链路的输入来源：物理层控制、MAC/HARQ 状态、调制阶数、TB/CB 参数。
- [x] 补充 TS 36.212 已核验部分：UL-SCH/DL-SCH 处理锚点。
- [x] 补充 TS 36.213/TS 36.321 待核验边界：HARQ 时序、ACK/NACK、RV/过程控制来源。
- [x] 增加接收端 descriptor 字段表：`direction`、`harq_id`、`rvidx`、`E`、`Ncb`、`Qm`、`cb_id`、`tb_id`、CRC 类型等。
- [x] 增加 DL 接收流程表：demapper LLR -> rate recovery -> Turbo -> CRC -> HARQ feedback。
- [x] 增加 UL 接收流程表：eNB/gNB 侧接收 -> UL-SCH 参数 -> Turbo -> CRC -> 调度反馈边界。
- [x] 增加失败案例：同一个 Turbo core 因 `harq_id` 或方向字段错导致 soft buffer 污染。
- [x] 增加工程验证项：DL/UL descriptor 隔离、HARQ 上下文隔离、CRC 状态上报。
- [x] 补充自测题和参考答案。
- [x] 更新执行与证据记录。
- [x] 运行 T7.5 单篇术语、标题、深度、LaTeX 审计。

### T7.6 LTE Turbo 译码边界案例

- [x] 读取 T7.6 当前正文，定位篇幅不足和 Prompt 覆盖缺口。
- [x] 对照 roadmap T7.6 Prompt，建立 T7.6 覆盖清单。
- [x] 扩展边界案例总表：小块、filler、`<NULL>`、puncturing、repetition、最大 CB 数、soft buffer 限制、RV 序列不匹配、LLR 符号不匹配、CRC 误通过、超时。
- [x] 为每个边界案例补齐：触发条件、现象、必查字段、定位步骤、修复方向。
- [x] 增加详细案例 1：RV mismatch/ring buffer 起点错误。
- [x] 增加详细案例 2：`<NULL>` 与 punctured/unknown 混淆。
- [x] 增加详细案例 3：分段 filler 留进 TB 重组。
- [x] 增加详细案例 4：最大 CB 数或 soft buffer 限制导致缓存裁剪。
- [x] 增加详细案例 5：LLR 符号约定反转。
- [x] 增加最小 dump 包：descriptor、`K`、`K_w`、`Ncb`、`E`、`rvidx`、`k0`、`null_mask`、unknown mask、soft buffer before/after、first mismatch、CB CRC、TB CRC。
- [x] 增加诊断流程图或表。
- [x] 补充 Python 诊断片段或保持已有片段并扩展说明。
- [x] 补充自测题和参考答案。
- [x] 更新执行与证据记录。
- [x] 运行 T7.6 单篇术语、标题、深度、LaTeX 审计。

### 模块 7 整体收尾

- [x] 对 T7.1-T7.6 逐篇核对 Prompt 覆盖。
- [x] 对 T7.1-T7.6 逐篇核对适当拓展是否充分。
- [x] 对 T7.1-T7.6 逐篇核对协议证据、待核验边界和本地路径。
- [x] 对 T7.1-T7.6 逐篇核对术语首现、标题正式化和思考题答案。
- [x] 对 T7.1-T7.6 逐篇核对图表质量和引用复现。
- [x] 运行 T7 全量术语审计：`python3 tools/audit_lesson_terms.py docs/L2/T7.*.md`。
- [x] 运行 T7 全量标题审计：`python3 tools/audit_markdown_headings.py docs/L2/T7.*.md`。
- [x] 运行 T7 全量深度审计：`python3 tools/audit_lesson_depth.py --strict docs/L2/T7.*.md`。
- [x] 运行 T7 全量 LaTeX 审计：`python3 tools/audit_latex_render.py docs/L2/T7.*.md`。
- [x] 运行 T7 引用重建审计：`python3 tools/audit_reference_rebuilds.py docs/L2/T7.*.md`。
- [x] 运行 T7.4 嵌入式 Python reassembly 校验。
- [x] 运行 T7.6 LLR sign check 校验。
- [x] 安排审核经理复核 T7。
- [x] 修复审核经理提出的 Critical/Important 问题。
- [x] 在本文件“完成记录”写入 T7 收尾证据。

## 阶段 2：全项目已完成文档审查

### 审查范围

- [x] 收集 `docs/L1/*.md` 已完成讲义清单。
- [x] 收集 `docs/L2/*.md` 已完成讲义清单。
- [x] 确认 `docs/L3` 是否存在已完成讲义；若不存在，在报告中说明。
- [x] 对照 roadmap，识别已完成文件对应的任务卡片。
- [x] 更新或重生成 `docs/audits/prompt_coverage_matrix.md`。

### 每篇文档必查项

- [x] Prompt 点名内容是否全量覆盖。
- [x] Prompt 中“必须”“包含”“讨论”“复现”“给出例子”等硬要求是否落实到正文。
- [x] 是否做了必要拓展，而不是只满足 Prompt 字面要求。
- [x] 是否有学习目标和前置知识检查。
- [x] 是否有足够的理论介绍和零基础解释。
- [x] 是否先解释概念，再进入公式推导。
- [x] 公式前是否说明回答什么问题、符号含义和来源。
- [x] 公式后是否解释接收端或工程意义。
- [x] 3GPP 相关结论是否有 TS、Rel-19 包、章节、表/图/公式、本地路径。
- [x] 未核验内容是否标记 `待核验` 并写明关闭条件。
- [x] 是否把工程策略误写成协议强制要求。
- [x] 是否避免协议索引化。
- [x] 缩写首次出现是否按规则展开。
- [x] 标题是否正式、非口语化。
- [x] 图表是否清晰、直观、无遮挡、无拥挤。
- [x] 协议表格/公式/图是否复现或重建，或明确保留 L3/system bit-exact 条件项。
- [x] Python 图表是否记录脚本、输入、输出和证据路径；后续局部视觉审计作为持续控制执行。
- [x] 是否包含接收端流程或说明为何不适用。
- [x] 是否包含伪代码、仿真或可执行验证。
- [x] 是否包含定点化策略或说明为何不适用。
- [x] 是否包含 RTL/ASIC 映射或说明为何不适用。
- [x] 是否包含验证方法。
- [x] 是否包含常见错误。
- [x] 工程思考题是否有参考答案或验收点。
- [x] 是否包含执行与证据记录。
- [x] 是否包含参考文献。

### 全项目审查报告

- [x] 为每篇文档标记状态：通过 / 小修 / 重要修复 / 重写。
- [x] 为每篇文档列出 Prompt 缺口。
- [x] 为每篇文档列出拓展不足项。
- [x] 为每篇文档列出协议证据问题。
- [x] 为每篇文档列出图表/公式/引用问题。
- [x] 为每篇文档列出术语/标题/格式问题。
- [x] 为每篇文档列出修复动作。
- [x] 生成全项目审查报告：`docs/audits/full_project_document_review.md`。
- [x] 将审查结果摘要写入本文件“完成记录”。

## 阶段 3：全项目合规审查

- [x] 核对 `合规与遵从.md` 与 roadmap 顶部规则是否一致。
- [x] 核对用户提出的全局要求是否都已写入规则。
- [x] 核对所有已完成讲义是否遵守 3GPP 协议精读规则。
- [x] 核对所有已完成讲义是否遵守零基础教学规则。
- [x] 核对所有已完成讲义是否遵守 Prompt 最低线与适当拓展规则。
- [x] 核对所有已完成讲义是否避免协议索引化。
- [x] 核对所有已完成讲义是否遵守缩写首现规则。
- [x] 核对所有已完成讲义是否遵守标题正式化规则。
- [x] 核对所有已完成讲义是否遵守引用内容重建规则；候选清单已分类，剩余为 L3/system 条件项。
- [x] 核对所有已完成讲义是否遵守 LaTeX 全检规则。
- [x] 核对所有已完成讲义是否遵守图表质量规则。
- [x] 生成合规审查报告：`docs/audits/global_compliance_review.md`。
- [x] 将合规审查结果摘要写入本文件“完成记录”。

## 阶段 4：按审查结果整改已完成文档

- [x] 整理 Critical 问题清单。
- [x] 整理 Important 问题清单。
- [x] 整理 Minor 问题清单。
- [x] 优先修复 Prompt 漏项。
- [x] 优先修复协议证据缺失或错误。
- [x] 优先修复公式渲染失败。
- [x] 优先修复术语首次裸写。
- [x] 优先修复标题口语化。
- [x] 优先修复图表遮挡、拥挤或粗糙。
- [x] 优先修复引用协议表/图/公式但未复现的问题。
- [x] 修复讲解太薄、缺少理论铺垫的问题。
- [x] 修复缺少接收端对象模型的问题。
- [x] 修复缺少失败案例的问题。
- [x] 修复缺少思考题答案的问题。
- [x] 修复缺少执行与证据记录的问题。
- [x] 每修完一个模块，运行该模块全量审计。
- [x] 每修完一个模块，安排审核经理复核。
- [x] 更新 `docs/audits/full_project_document_review.md` 的复审状态。
- [x] 更新本文件“完成记录”。

### 阶段 4 已关闭项

- [x] 关闭 TS 36.213/TS 36.321 LTE HARQ/MAC 精确锚点缺口：T7.3/T7.5/T7.6 已补 TS 36.213 §8.3、§8.6、§8.6.1 和 TS 36.321 §4.3.2、§4.4、§5.3.2.1、§5.3.2.2、§5.4.2.1 的本地路径、行号和使用边界。
- [x] 关闭 TS 36.212 Figure 5.1.3-2 Turbo 编码器原图未重建缺口：T6.3 已新增 Python 重建图，T6.1/T6.2/T6.4/T6.5/T6.6/T6.7/T6.8 已引用该资产。
- [x] 关闭 TS 38.212 NR CRC 多项式未复现缺口：T3.1 已复现 CRC24A、CRC24B、CRC24C、CRC16、CRC11、CRC6，并记录 `source.docx` 的 OLE/media 证据链。

### 阶段 4 Important 项处理结果与持续控制

- [x] TS 38.214 MCS/TBS/RV/CBG 表格重分类：L2 已关闭 RV/CBG/CBGTI/CBGFI 的译码状态语义；T9/T11 不使用 MCS/TBS 表具体数值。MCS/TBS 表值改为 L3 bit-exact/system vector 条件项，进入 L3 或系统级调度向量时按实际使用范围重建表格子集。
- [x] Minor：T6.4 Table 5.1.3-3 资产证据链总表已补输入 CSV/HTML、脚本和输出图片路径，见 `docs/audits/image_asset_inventory.md` 与 `docs/audits/final_delivery_status.md`。
- [x] 本轮全项目 Python 图片字号与局部几何审计资料已建立并二次加严：`docs/audits/image_asset_inventory.md` 覆盖 46 张 PNG 和 42 个脚本，记录历史风险、边界检查、24px/56px 可读性门槛和后续重点。该项作为持续控制继续执行，后续任一图片新增、重生成或脚本修改都必须重新逐图审计，不能用一次边界检查永久关闭。

## 阶段 4C：全项目 Python 图片可读性整改

阶段目标：关闭用户指出的全项目图片表格字体偏小、表格/文本框文字未居中、局部间距不足、箭头端点不贴边等系统性问题。几何审计通过不代表可读性通过；`tools/audit_figure_readability.py` findings 按整改队列处理，逐图目检是最终验收的一部分。

### 阶段 4C 通用完成定义

- [x] 全项目运行 `python3 tools/audit_figure_readability.py tools/figures`，按输出脚本建立整改队列。
- [x] 审计脚本阈值使用 24px 表格/说明文字下限和 56px 表格行高下限；20-23px 只允许作为坐标轴刻度、码位小标签、环形缓存短索引等辅助标注，并必须在记录中说明补偿说明区。
- [x] 每个整改脚本重生成对应 PNG，运行 `python3 tools/audit_figure_geometry.py <script>` 和 `python3 tools/audit_figure_readability.py <script>`。
- [x] 每张重生成图必须目检：表格字号、表头/首列、单元格水平/垂直居中、文本框内边距、说明框底部留白、相邻区块间距、箭头端点、整体缩放阅读效果。
- [x] 每批整改后更新本台账完成记录；若脚本属于历史 L2/L1 图片，也必须说明对应正文图片路径。

### 阶段 4C 基线整改队列

2026-06-20 全项目可读性基线命令：

```bash
python3 tools/audit_figure_readability.py tools/figures
python3 tools/audit_figure_geometry.py --focus-only tools/figures
```

结果：可读性审计输出 `FIGURE_READABILITY_AUDIT_FINDINGS`，共 26 个脚本、154 条表格字号/行高风险；几何审计输出 `FIGURE_GEOMETRY_AUDIT_OK`。这说明当前主要缺口是 Markdown 缩放后的字体、行高、表格/说明框可读性和逐图目检闭环，而不是外边界裁切。整改完成标准是：下表脚本逐项通过单脚本可读性审计，或对确属坐标轴刻度、码位小标签、环形缓存短索引等辅助标注的 finding 写明例外理由；不能把未处理 finding 解释为“已通过”。

| Finding 数 | 脚本 |
|:---:|:---|
| 11 | `tools/figures/render_ldpc_bp_spa_round.py` |
| 7 | `tools/figures/render_ldpc_min_sum_variants.py` |
| 12 | `tools/figures/render_ldpc_tanner_syndrome.py` |
| 8 | `tools/figures/render_lte_dl_ul_decoder_context.py` |
| 3 | `tools/figures/render_lte_turbo_encoder_structure.py` |
| 3 | `tools/figures/render_lte_turbo_interleaver_table.py` |
| 7 | `tools/figures/render_nr_ldpc_base_graph_selection.py` |
| 9 | `tools/figures/render_nr_ldpc_bit_deinterleaving.py` |
| 10 | `tools/figures/render_nr_ldpc_circular_buffer_states.py` |
| 8 | `tools/figures/render_nr_ldpc_decoder_chain_overview.py` |
| 6 | `tools/figures/render_nr_ldpc_edge_case_diagnosis.py` |
| 6 | `tools/figures/render_nr_ldpc_lifting_qc_matrix.py` |
| 10 | `tools/figures/render_nr_ldpc_rate_recovery_overview.py` |
| 6 | `tools/figures/render_nr_ldpc_tables.py` |
| 4 | `tools/figures/render_nr_polar_ca_scl_selector.py` |
| 4 | `tools/figures/render_nr_polar_decoder_chain_overview.py` |
| 6 | `tools/figures/render_nr_polar_edge_case_diagnosis.py` |
| 1 | `tools/figures/render_nr_polar_rate_recovery_flow.py` |
| 7 | `tools/figures/render_nr_polar_reliability_sequence.py` |
| 6 | `tools/figures/render_nr_polar_scl_path_pruning.py` |
| 2 | `tools/figures/render_t12_1_golden_model_layout.py` |
| 2 | `tools/figures/render_t12_2_lte_turbo_float_sim_flow.py` |
| 2 | `tools/figures/render_t12_3_nr_ldpc_float_sim_flow.py` |
| 2 | `tools/figures/render_t12_4_nr_polar_float_sim_flow.py` |
| 4 | `tools/figures/render_t12_5_ber_bler_curve_reporting.py` |
| 8 | `tools/figures/render_turbo_ldpc_polar_algorithm_comparison.py` |

### 阶段 4C.1 LTE/Turbo 与 L2 早期图

- [x] `tools/figures/render_lte_harq_rv_windows.py`：已扩画布到 `2220x2460`，保留 RV ring buffer 和四个 RV 传输模型，右上 RV1 地址流改为两行大 chips，soft buffer 表与底部说明框留白复核通过；静态审计 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，目检通过。
- [x] `tools/figures/render_lte_dl_ul_decoder_context.py`：复核 DL/UL descriptor 表格字号、箭头端点、文本框宽高和工程检查区。
- [x] `tools/figures/render_lte_turbo_encoder_structure.py`：复核 Turbo encoder 图底部说明框、反馈支路说明和图例字号。
- [x] `tools/figures/render_lte_turbo_interleaver_table.py`：复核 TS 36.212 Table 5.1.3-3 重建图的行高、表格分栏、列含义说明和缩放可读性。

### 阶段 4C.2 LDPC 基础图

- [x] `tools/figures/render_ldpc_tanner_syndrome.py`：复核 Tanner graph、syndrome 表、矩阵/边标注字号和局部间距。
- [x] `tools/figures/render_ldpc_bp_spa_round.py`：复核 BP/SPA 消息表、公式说明框和箭头路径。
- [x] `tools/figures/render_ldpc_min_sum_variants.py`：复核 MS/NMS/OMS 对比表字号和说明框排布。
- [x] `tools/figures/render_ldpc_layered_schedule.py`：复核 layered schedule 表、row height、层更新流程和底部说明。
- [x] `tools/figures/render_ldpc_numeric_walkthrough.py`：复核数值走读表全部行高、字体、列宽和手算步骤说明。

### 阶段 4C.3 NR LDPC 协议图

- [x] `tools/figures/render_nr_ldpc_base_graph_selection.py`：复核 BG1/BG2 选择表、协议条件说明和节点间距。
- [x] `tools/figures/render_nr_ldpc_lifting_qc_matrix.py`：复核 lifting/QC 矩阵表、非零位置标注、标题与图元间距。
- [x] `tools/figures/render_nr_ldpc_tables.py`：复核 TS 38.212 表格重建图行高、分栏、表头和脚注字号。
- [x] `tools/figures/render_nr_ldpc_rate_recovery_overview.py`：复核 rate recovery 表、k0/RV 说明、环形缓存区域和底部说明。
- [x] `tools/figures/render_nr_ldpc_circular_buffer_states.py`：复核 circular buffer 状态、短索引例外、说明框和局部遮挡。
- [x] `tools/figures/render_nr_ldpc_bit_deinterleaving.py`：复核 bit deinterleaving 表、列组、索引标签和读图顺序。
- [x] `tools/figures/render_nr_ldpc_decoder_chain_overview.py`：复核 decoder chain 表、节点/箭头、证据区和说明框。
- [x] `tools/figures/render_nr_ldpc_edge_case_diagnosis.py`：复核边界案例诊断表、风险说明和失败 dump 字段。

### 阶段 4C.4 NR Polar 图

- [x] `tools/figures/render_nr_polar_reliability_sequence.py`：复核可靠性序列表、冻结/信息位标注和小标签例外。
- [x] `tools/figures/render_nr_polar_ca_scl_selector.py`：复核 CA-SCL path/CRC/RNTI selector 表和路径度量说明。
- [x] `tools/figures/render_nr_polar_scl_path_pruning.py`：复核 SCL pruning 表、路径复制/剪枝箭头和排序器说明。
- [x] `tools/figures/render_nr_polar_decoder_chain_overview.py`：复核 Polar decoder chain 表、rate recovery 到 CRC selector 的流程。
- [x] `tools/figures/render_nr_polar_edge_case_diagnosis.py`：复核边界案例诊断表、错误定位字段和说明框。

### 阶段 4C.5 L3/T12 图和对比图复检

- [x] `tools/figures/render_t12_1_golden_model_layout.py` 至 `render_t12_5_ber_bler_curve_reporting.py`：复核 T12 图中 17px `SMALL/TINY` 是否属于真实表格/说明文字；必要时放大或拆表。
- [x] `tools/figures/render_turbo_ldpc_polar_algorithm_comparison.py`：复核算法对比矩阵中所有表格字号、连线端点和文本居中。
- [x] 对已整改过的 T13.1-T13.4 图保持通过状态；若加严阈值产生新 finding，按当前阈值重修。

## 阶段 4B：补齐 L1 模块 4 剩余讲义

阶段目标：补齐 roadmap 中尚未生成的 `T4.4`、`T4.5`、`T4.6`。这三节属于 L1 入门阶段，但不是可省略的背景材料；`T4.6` 是 `T12.1` 的前置，因此必须先完成、审查和回写证据，再进入 L3。

### 阶段 4B 通用完成定义

- [x] 从 roadmap 提取该小节 Prompt、验收、前置和 3GPP/证据，并写入讲义执行记录。
- [x] 将 Prompt 拆成原子要求，在正文中逐条覆盖并适当拓展。
- [x] 保持 L1 既有写法：先讲零基础理论、术语来源、问题动机和手算例子，再连接协议和工程。
- [x] 涉及 3GPP 时必须列 TS 编号、Rel-19 包、章节、本地路径、协议前因后果和接收端后果。
- [x] 明确协议规定与实现策略边界：CRC、分段、编码结构、rate matching、HARQ/RV 是协议锚点；具体早停策略、统计策略、接口封装和 RTL 微架构是实现指导，除非有明确协议依据。
- [x] 单篇技术缩写首次出现必须展开全称；项目级 3GPP/LTE/NR 不重复长篇展开。
- [x] 每节必须包含可手算或可追踪例子、伪代码或可执行验证、浮点仿真方案、定点化策略、RTL/ASIC 映射、验证方法、常见错误、工程思考题及答案、协议证据表、执行与证据记录和参考文献。
- [x] 每节完成后运行单篇审计：术语、标题、深度、LaTeX、引用重建。
- [x] 三节完成后运行 L1 全量审计，并更新 `prompt_coverage_matrix.md`、`full_project_document_review.md`、`global_compliance_review.md` 和 `final_delivery_status.md` 的 L1 状态。

### T4.4 早停与 CRC 门控译码控制

- [x] 读取 roadmap T4.4 卡片，提取 Prompt、验收和 3GPP/证据。
- [x] 读取 T3.1、T4.1、T4.3，保持 CRC、LLR、迭代译码和 HARQ 术语一致。
- [x] 讲清早停目标：降低平均迭代次数、延迟和功耗，但不能放松正确性。
- [x] 区分奇偶校验、syndrome、CB CRC、TB CRC、Polar CRC-aided selection 的层次。
- [x] 说明 CRC 是错误检测和门控条件，不是纠错算法。
- [x] 对比 Turbo、LDPC、Polar 的停止或选择流程：Turbo CRC 门控停止、LDPC syndrome/CRC 停止、Polar CA-SCL CRC 辅助路径选择。
- [x] 明确 algorithmic stopping 是实现策略，除非有直接协议引用；不得声称 3GPP 规定具体迭代次数或厂商早停策略。
- [x] 给一个最小 stop controller 表或伪代码，输入包含 `iter_count`、`max_iter`、`syndrome_zero`、`crc_pass`、`candidate_valid`。
- [x] 给 CRC 误通过定性失败案例，说明低概率事件、错误候选被接受和 BLER/FER 回归的重要性。
- [x] 工程段覆盖早停计数器、CRC latency、syndrome checker、pipeline flush、状态机 pass/fail、功耗与最坏延迟。
- [x] 写协议证据表，至少包含 TS 36.212 Rel-19 `36212-j30` 和 TS 38.212 Rel-19 `38212-j30` 的 CRC/编码结构锚点和本地路径。
- [x] 运行 T4.4 单篇术语、标题、深度、LaTeX、引用重建审计并记录结果。

### T4.5 译码器性能指标

- [x] 读取 roadmap T4.5 卡片，提取 Prompt、验收和 3GPP/证据。
- [x] 读取 T2.1、T4.3、T5.3、T5.5，保持 Eb/N0、BLER、吞吐、延迟和验证术语一致。
- [x] 定义 BER、BLER、FER，明确统计对象、分母、单位和与译码验收的关系。
- [x] 解释译码器研究为何常看 TB/CB BLER，因为 CRC pass/fail 与传输块交付直接相关。
- [x] 定义吞吐、延迟、平均/最大迭代次数、每比特能耗、面积吞吐，给基本计算式和单位。
- [x] 说明 BLER vs Eb/N0 曲线生成流程：固定码率、调制、块长、算法参数，扫 SNR 点，生成帧，解调译码，按 CRC 或已知 payload 统计错误。
- [x] 解释置信度需要多少帧：低 BLER 点需要更多样本，使用错误块数门限或二项分布置信区间直觉，不写成固定帧数万能规则。
- [x] 明确 Eb/N0、Es/N0、SNR 的边界，避免随意互换。
- [x] 工程段覆盖 early stop 对平均迭代、吞吐、能耗的影响，以及最坏延迟与平均吞吐的差异。
- [x] 写协议证据表，说明 3GPP 证据只支撑 TB/CB CRC pass/fail 和传输块交付背景，不支撑某个性能门限。
- [x] 运行 T4.5 单篇术语、标题、深度、LaTeX、引用重建审计并记录结果。

### T4.6 译码器接口契约

- [x] 读取 roadmap T4.6 卡片，提取 Prompt、验收和 3GPP/证据。
- [x] 读取 T3.2、T4.3、T5.2、T5.4，保持 TB/CB、filler、HARQ、soft buffer、握手和状态机术语一致。
- [x] 定义公共 decoder descriptor，至少包含 `llr_stream`、LLR 位宽/符号约定、`tb_id`、`cb_id`、`code_type`、长度字段、CRC 类型、RV、HARQ process ID、direction/channel、max iteration、soft-combine 状态。
- [x] 定义输出和状态表，至少包含 decoded bits、CB CRC status、TB CRC 或上层汇总状态、iteration count、early stop reason、error flags、debug counters、valid/ready 或完成握手。
- [x] 分别说明 Turbo、LDPC、Polar 如何映射到同一接口：Turbo 的交织器/CB 参数，LDPC 的 BG/Zc/rate recovery 元数据，Polar 的 frozen/CRC/list-size 背景字段。
- [x] 解释接口不能泄露过多算法内部细节，但必须保留足够协议上下文和调试字段。
- [x] 给接收端流程：descriptor 锁存、LLR 输入、可选 HARQ soft buffer 合并、算法 core、CRC/stop controller、输出提交与错误标志。
- [x] 覆盖字段合法性检查、descriptor versioning、端序/bit order、LLR sign convention、backpressure、reset、超时、错误码、debug dump。
- [x] 讲清 HARQ process ID/RV 与 soft buffer key 的关系，避免新旧 TB 或 CB/TB 状态混淆。
- [x] 保留 TS 36.213 精确分册 `待核验` 标记，不能伪造锚点；TS 36.212、TS 38.212、TS 38.214 使用本地已处理路径。
- [x] 运行 T4.6 单篇术语、标题、深度、LaTeX、引用重建审计并记录结果。

### 阶段 4B L1 收尾

- [x] T4.4-T4.6 全部完成后，将 L1 状态从 24 篇更新为 27 篇。
- [x] 运行 L1 全量术语审计：`python3 tools/audit_lesson_terms.py docs/L1/T*.md`。
- [x] 运行 L1 全量标题审计：`python3 tools/audit_markdown_headings.py docs/L1/T*.md`。
- [x] 运行 L1 全量深度审计：`python3 tools/audit_lesson_depth.py --strict docs/L1/T*.md`。
- [x] 运行 L1 全量 LaTeX 审计：`python3 tools/audit_latex_render.py docs/L1/T*.md`。
- [x] 运行 L1 引用重建审计：`python3 tools/audit_reference_rebuilds.py docs/L1/T*.md`。
- [x] 安排审核经理或等价复核 T4.4-T4.6，修复 Critical/Important 问题。
- [x] 更新本文件完成记录和相关审计文档。

## 阶段 5：完成模块 8 NR LDPC 译码协议与算法

模块目标：围绕 TS 38.212，把 NR LDPC 的协议链路、基图、提升、QC-LDPC 矩阵、BP/SPA、Min-Sum、layered schedule、syndrome early stop 和数值走读讲清楚。

### 阶段 5 通用完成定义

每个 T8 小节都必须额外满足以下完成定义，不能只完成标题级条目：

- [x] 从 roadmap 提取该小节 Prompt、验收、前置和 3GPP/证据，写入执行记录或审计矩阵。
- [x] 将 Prompt 拆成可核对的原子要求，并逐条在正文中落实。
- [x] 在正文中适当拓展 Prompt：补历史/工程来源、接收端对象模型、descriptor、边界条件、失败模式和验证证据。
- [x] 明确本节主角概念的中文名、英文全称、缩写、作用和常见误解。
- [x] 明确协议精读范围：TS 编号、Rel-19 包、章节、表/图/公式号、本地路径。
- [x] 若引用 TS 38.212 表、图或公式，核验 `TS_36.212_36212-j30_content.md`、表格 HTML/CSV、equations XML、media 或原始 Word XML。
- [x] 需要复现的协议表必须 Markdown 重建或 Python 图片化重建，并解释每列含义。
- [x] 需要复现的协议图必须 Mermaid 或 Python 图片化重建，并解释每个模块、输入输出和接收端后果。
- [x] 需要使用的公式必须完整写出、定义符号、解释公式回答的问题和接收端用途。
- [x] 增加至少一个可手算或可追踪数值例子；若本节是算法节，例子必须走到中间变量。
- [x] 增加接收端流程或说明本节为何只做理论准备。
- [x] 增加伪代码或 Python 片段；若不适合代码，给出可执行验证表。
- [x] 增加浮点模型验证点。
- [x] 增加定点化风险：位宽、缩放、饱和、符号、量化或说明本节为何只做预览。
- [x] 增加 RTL/ASIC 映射：存储、地址生成、并行度、bank、控制状态或说明本节为何只做预览。
- [x] 增加常见错误和定位方式。
- [x] 增加工程思考题和参考答案。
- [x] 增加协议证据表。
- [x] 增加执行与证据记录。
- [x] 单篇运行术语、标题、深度、LaTeX 审计。
- [x] 若本节生成图片，必须目检无文字遮挡、无拥挤、尺寸协调，并记录脚本路径；后续局部视觉审计作为持续控制执行。

### T8.1 NR LDPC 译码链路总览

- [x] 读取 roadmap T8.1 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 定位 TS 38.212 Rel-19 中 NR LDPC 接收链路相关章节：CRC、CB segmentation、LDPC 编码、rate matching、UL-SCH、DL-SCH。
- [x] 定位 TS 38.214 中 MCS/TBS/RV 背景，标记已核验与待核验边界。
- [x] 讲清 LDPC 是低密度奇偶校验码，解释名称、历史来源、为什么适合 NR 数据业务。
- [x] 解释 NR 数据传输为什么从 LTE Turbo 转向 LDPC：吞吐、并行度、硬件友好、长块性能。
- [x] 建立接收端总链路：demapper LLR -> rate recovery -> LDPC decoder -> CB CRC -> CB concat -> TB CRC -> HARQ feedback。
- [x] 画接收端链路图。
- [x] 列输入 descriptor：`BG`、`Zc`、`rvidx`、`E`、`Ncb`、`Qm`、`C`、`cb_id`、CRC 类型、HARQ ID。
- [x] 列输出：decoded CB bits、CB CRC status、TB candidate、TB CRC status、ACK/NACK boundary。
- [x] 给一个两个 CB 的小型接收流程例子。
- [x] 区分协议规定和实现策略。
- [x] 给伪代码。
- [x] 给浮点仿真检查项。
- [x] 给定点/RTL 预览：LLR buffer、message memory、syndrome checker。
- [x] 给常见错误和自测题答案。
- [x] 写协议证据表和执行记录。
- [x] 单篇审计并记录结果。

#### T8.1 细化交付物

- [x] 正文必须先说明 LDPC 的中文全称、英文全称和“低密度”的含义。
- [x] 正文必须解释 NR 数据业务为什么需要高并行吞吐译码器。
- [x] 正文必须说明 TS 38.212 在链路中的位置，TS 38.214 只提供调度/MCS/RV 背景。
- [x] 图中必须包含 LLR 来源、rate recovery、LDPC core、CB CRC、TB CRC、HARQ feedback。
- [x] 对每个链路节点列输入、输出、协议锚点和实现对象。
- [x] 用一个教学 TB 展示分成 CB、每个 CB 译码、再拼接回 TB 的路径。
- [x] 明确本节不展开 BG/Zc/Min-Sum 细节，分别指向 T8.2/T8.3/T8.6。
- [x] 给出“译码器最小 descriptor v0”表，后续 T8/T9 复用。
- [x] 给出“链路级失败定位入口”表：rate recovery 错、BG 错、Zc 错、LDPC 不收敛、CRC fail。

### T8.2 NR LDPC 基图选择

- [x] 读取 roadmap T8.2 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 精读 TS 38.212 中 BG1/BG2 选择条件。
- [x] 复现协议基图选择逻辑，不能只口头描述。
- [x] 解释 Base Graph 是基图模板，不是完整校验矩阵。
- [x] 讲清 BG1/BG2 的工程差异：块长、码率、并行度、校验结构。
- [x] 解释输入参数：payload size、code rate、CB size、direction/channel context。
- [x] 给 BG1 选择例子。
- [x] 给 BG2 选择例子。
- [x] 给接近阈值的边界例子。
- [x] 给 Python 判断函数或伪代码。
- [x] 解释基图选错后果：Zc 错、H 矩阵错、syndrome 不收敛、CRC 失败。
- [x] 补协议证据表。
- [x] 补验证方法：与协议参考向量对比、边界扫描。
- [x] 补 RTL/ASIC 映射：BG 选择进入配置寄存器和地址生成器。
- [x] 单篇审计并记录结果。

#### T8.2 细化交付物

- [x] 正文必须讲清 Base Graph 与完整 H 矩阵的区别。
- [x] 正文必须解释 BG1/BG2 与块长、码率、硬件并行度之间的关系。
- [x] 必须复现协议选择条件，不能只说“按 A 和 R 选择”。
- [x] 若协议条件包含多个分支，必须给流程图或判定表。
- [x] 必须给至少三个例子：BG1、BG2、边界值。
- [x] 每个例子必须列输入、判断过程、输出 BG、如果选错的后果。
- [x] 给 Python/伪代码函数 `select_base_graph(...)`。
- [x] 验证方法必须覆盖边界扫描和协议条件分支覆盖。
- [x] RTL/ASIC 映射必须说明 BG 字段如何进入寄存器、地址生成器和矩阵表选择。

### T8.3 提升大小与 QC-LDPC 矩阵构造

- [x] 读取 roadmap T8.3 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 精读 TS 38.212 lifting size set 和 base graph shift table。
- [x] 核验 Table 5.3.2-1/2/3 的本地 HTML/CSV/media 状态。
- [x] 根据本地证据决定 Markdown 表格复现或 Python 图片化重建。
- [x] 解释提升大小 `Zc` 的含义：一个基图元素扩展成 `Zc x Zc` 子矩阵。
- [x] 解释 QC-LDPC 的 quasi-cyclic 含义。
- [x] 解释 `-1`、非负 shift value、零矩阵、循环移位单位矩阵。
- [x] 用 2x3 玩具基图构造完整 H。
- [x] 手算 `Zc=4` 的循环移位单位矩阵。
- [x] 解释移位方向约定和协议表索引。
- [x] 说明接收端为何需要 `Zc`：syndrome、layer schedule、bank 地址。
- [x] 给 Python 生成 shift matrix 的片段。
- [x] 生成或插入矩阵构造图。
- [x] 常见错误：Zc 选错、shift 方向反、`-1` 与 `0` 混淆、BG 表错用。
- [x] 单篇审计并记录结果。

#### T8.3 细化交付物

- [x] 正文必须解释 `Zc` 与 CB 尺寸、矩阵尺寸、并行度的关系。
- [x] 正文必须解释 QC-LDPC 中循环移位结构为何利于硬件地址生成。
- [x] 必须核验 lifting size set 的本地表格证据。
- [x] 必须核验 BG shift table 的本地表格证据。
- [x] 对协议表的每列含义逐列解释。
- [x] 若表过长，必须生成精细图片或分组表，不允许粗糙长表。
- [x] 必须给玩具基图到完整 H 的构造过程。
- [x] 必须给一个 `Zc=4` 或类似小尺寸的循环移位矩阵。
- [x] 必须解释 shift value 为 `-1` 的语义。
- [x] 必须解释 shift 方向错误的观测现象。
- [x] Python 片段必须能生成移位单位矩阵并校验行列权重。
- [x] RTL 映射必须说明 base graph table、shift ROM、barrel shifter/address offset 的关系。

### T8.4 LDPC Tanner 图与消息传递

- [x] 读取 roadmap T8.4 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 精读 TS 38.212 LDPC 编码和校验矩阵相关章节。
- [x] 解释校验矩阵 H 是译码核心对象。
- [x] 解释变量节点、校验节点、边、syndrome。
- [x] 讲清 GF(2) 运算在 syndrome 中的作用。
- [x] 说明系统位、校验位、punctured systematic bits、filler bits 对接收端的影响。
- [x] 给小型 H 矩阵。
- [x] 手算 syndrome。
- [x] 画 Tanner graph。
- [x] 解释真实 NR 硬件不会完整存 H，而存 base graph + shift values。
- [x] 给 Python syndrome 校验片段。
- [x] 补定点/RTL 映射：message memory、row/column addressing、syndrome checker。
- [x] 常见错误：行列反、GF(2) 用普通加法、filler/puncturing 混淆、BG 表错用。
- [x] 单篇审计并记录结果。

#### T8.4 细化交付物

- [x] 正文必须讲清 H 矩阵每一行是一条奇偶校验方程。
- [x] 正文必须讲清变量节点和校验节点的图含义。
- [x] 必须用 GF(2) 手算一个 syndrome。
- [x] 必须给 Tanner graph 图，并解释边如何来自 H 中的 1。
- [x] 必须说明真实 NR 中 H 由 BG 和 Zc 生成，不手工保存完整大矩阵。
- [x] 必须解释 filler、punctured systematic bits 和 parity bits 对译码输入的不同影响。
- [x] 必须说明 syndrome 与 CRC 的区别：一个检查 LDPC 校验，一个检查业务块完整性。
- [x] Python 片段必须能计算 syndrome 并展示单比特错误如何改变 syndrome。
- [x] RTL 映射必须说明 syndrome checker 与 layered decoder 是否共享地址/存储。

### T8.5 BP/SPA 译码理论

- [x] 读取 roadmap T8.5 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 从零基础解释 message passing。
- [x] 解释 Belief Propagation 和 Sum-Product Algorithm 的中文含义和用途。
- [x] 解释变量节点消息、校验节点消息、channel LLR、extrinsic message。
- [x] 从概率直觉推导到 LLR 域更新。
- [x] 每个公式前说明回答的问题和符号含义。
- [x] 给极小 Tanner graph。
- [x] 手算一轮变量节点更新。
- [x] 手算一轮校验节点更新。
- [x] 说明 syndrome early stop 的理论位置。
- [x] 对比 Turbo BCJR：共同点是软信息传递，差异是图结构和局部更新。
- [x] 给 Python 浮点一轮迭代示例。
- [x] 常见错误：消息当硬比特、channel/extrinsic 混淆、回声信息。
- [x] 单篇审计并记录结果。

#### T8.5 细化交付物

- [x] 正文必须解释 BP/SPA 的中文含义、概率直觉和适用图模型。
- [x] 必须分别定义 channel LLR、variable-to-check message、check-to-variable message、posterior LLR。
- [x] 必须说明“外信息”原则，避免消息把自己带回自己。
- [x] 校验节点公式必须先给概率直觉，再给 LLR 形式。
- [x] 变量节点公式必须解释为什么是求和。
- [x] 必须手算一轮消息传递，列出每条边的消息。
- [x] 必须说明迭代停止条件：最大迭代、syndrome、CRC 的边界。
- [x] Python 片段必须至少跑一轮 toy BP。
- [x] 定点预览必须说明 tanh/atanh 或近似实现为什么昂贵。
- [x] 常见错误必须包含消息方向错、重复使用自身消息和 LLR 符号约定错。

### T8.6 Min-Sum、Normalized/Offset Min-Sum

- [x] 读取 roadmap T8.6 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 解释 SPA 校验节点更新复杂度。
- [x] 推导 Min-Sum：符号相乘、幅度取最小。
- [x] 说明 Min-Sum 丢掉的修正项和过度自信问题。
- [x] 推导 Normalized Min-Sum：缩放系数。
- [x] 推导 Offset Min-Sum：偏移量。
- [x] 给三个输入 LLR 的数值例子。
- [x] 分别计算 Min-Sum、Normalized、Offset。
- [x] 讨论性能/复杂度/硬件取舍。
- [x] 讲 min1/min2、符号异或、比较器、饱和、查表。
- [x] 给定点位宽和饱和策略。
- [x] 给 RTL/ASIC 映射：check-node unit、min tree、message memory。
- [x] 常见错误：offset 太大、normalization 太小、符号异或错、min2 选择错。
- [x] 单篇审计并记录结果。

#### T8.6 细化交付物

- [x] 正文必须从 SPA 校验节点复杂度引出 Min-Sum。
- [x] 必须解释校验节点输出符号是其他输入符号异或/相乘。
- [x] 必须解释幅度取其他输入绝对值的最小值。
- [x] 必须讲清 min1/min2 机制，不能只给公式。
- [x] 必须给同一组输入下 Min-Sum、Normalized、Offset 的数值对比。
- [x] 必须解释 Normalized 系数小于 1 的原因。
- [x] 必须解释 Offset 不能过大的原因。
- [x] 必须给硬件资源对比表：SPA、Min-Sum、Normalized、Offset。
- [x] 必须给定点饱和和截断策略。
- [x] 必须给失败案例：符号错、min2 错、offset 过大、缩放过小。

### T8.7 Layered Schedule 与 Syndrome Early Stop

- [x] 读取 roadmap T8.7 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 解释 flooding schedule。
- [x] 解释 layered schedule。
- [x] 说明 NR LDPC 工程上常用 layered 的原因：收敛速度、存储复用、硬件流水。
- [x] 用 base graph row/layer 解释一层一层更新。
- [x] 结合 `Zc` 解释一个 layer 内的地址访问。
- [x] 讲 syndrome early stop 与 CRC early stop 的区别。
- [x] 给小型 layered 更新例子。
- [x] 画 layered schedule 流程图。
- [x] 给伪代码。
- [x] 讨论硬件：bank conflict、pipeline、read-modify-write、layer parallelism。
- [x] 常见错误：更新顺序错、旧新 LLR 混用、syndrome 用了未更新值。
- [x] 单篇审计并记录结果。

#### T8.7 细化交付物

- [x] 正文必须对比 flooding 与 layered，列更新时序差异。
- [x] 必须解释 layer 与 base graph row group 的关系。
- [x] 必须给一个小 H 的 layered 更新顺序。
- [x] 必须说明 layered schedule 中变量节点值会在同一 iteration 内被更新并立即用于后续 layer。
- [x] 必须说明 syndrome early stop 与 CRC early stop 的不同层次。
- [x] 流程图必须包含 iteration loop、layer loop、check-node update、variable update、syndrome check。
- [x] RTL 映射必须包含 bank conflict、read-modify-write、pipeline stall、layer parallelism。
- [x] 必须列最小验证日志：iteration、layer、syndrome weight、updated variable count。
- [x] 常见错误必须包含旧值/新值混用、layer 顺序错、syndrome 检查时机错。

### T8.8 NR LDPC 数值走读

- [x] 读取 roadmap T8.8 卡片，提取 Prompt、验收、3GPP/证据。
- [x] 选择 toy LDPC H，明确不是 NR 一致性向量。
- [x] 给初始 channel LLR。
- [x] 计算初始 hard decision。
- [x] 计算初始 syndrome。
- [x] 做 1-2 轮 BP 或 Min-Sum 更新。
- [x] 每个中间数字解释含义。
- [x] 再次 hard decision。
- [x] 再次 syndrome。
- [x] 说明 toy 例子和真实 NR 的对应关系。
- [x] 给 Python 可复现片段。
- [x] 给预期输出。
- [x] 增加调试字段和常见错误。
- [x] 单篇审计并记录结果。

#### T8.8 细化交付物

- [x] 正文开头必须醒目标注 toy example，不是 NR conformance vector。
- [x] 必须给完整 H、初始 LLR、初始 hard decision、初始 syndrome。
- [x] 必须手算至少一轮关键消息或 Min-Sum 更新。
- [x] 必须展示更新后的 posterior LLR。
- [x] 必须展示更新后的 hard decision 和 syndrome。
- [x] 必须解释每个数字的含义，不能只贴结果表。
- [x] 必须说明 toy H 与真实 NR BG/Zc/H 的对应关系和差异。
- [x] Python 片段必须能复现正文数字或明确输出同等检查结果。
- [x] 必须给调试字段：iteration、edge messages、posterior LLR、syndrome weight。

### 模块 8 收尾

- [x] 运行 T8 全量术语审计。
- [x] 运行 T8 全量标题审计。
- [x] 运行 T8 全量深度审计。
- [x] 运行 T8 全量 LaTeX 审计。
- [x] 运行 T8 引用重建审计。
- [x] 生成或更新 T8 Prompt 覆盖矩阵。
- [x] 审核经理复核 T8。
- [x] 修复 T8 Critical/Important 问题。
- [x] 写入本文件完成记录。

## 阶段 6：完成模块 9 NR LDPC 接收侧译码链路

模块目标：围绕 TS 38.212/38.214，把 NR LDPC 接收侧 rate recovery、puncturing、shortening、repetition、HARQ soft buffer、RV、CBG、LLR 放置、CB/TB CRC 和边界案例讲清楚。

### 阶段 6 通用完成定义

- [x] 每节必须从接收端反操作展开，而不是复述发送端编码流程。
- [x] 每节必须明确 TS 38.212 与 TS 38.214 的职责边界。
- [x] 每节必须给出接收端 descriptor 字段，并说明字段来源和错误后果。
- [x] 每节必须区分协议强制规则、调度配置来源和实现策略。
- [x] 涉及 RV、CBG、HARQ 的章节必须画 soft buffer 或状态图。
- [x] 涉及 puncturing/shortening/repetition 的章节必须给 LLR 初始化/合并规则表。
- [x] 涉及 CB/TB 处理的章节必须明确 CRC 输入边界和拼接顺序。
- [x] 每节必须给失败案例，且包含可观测现象和最小 dump 字段。
- [x] 每节必须运行单篇术语、标题、深度、LaTeX 审计。

### T9.1 NR LDPC 速率恢复总览

- [x] 提取 T9.1 Prompt、验收、证据。
- [x] 精读 TS 38.212 rate matching/rate recovery 相关章节。
- [x] 解释发送端 rate matching 与接收端 rate recovery 的逆关系。
- [x] 从接收端 LLR 输入开始讲，不从编码器主线开始。
- [x] 列 descriptor：BG、Zc、RV、E、Ncb、Qm、layer、CB index、HARQ ID。
- [x] 画接收端 rate recovery 流程图。
- [x] 解释 LLR 如何放回 LDPC circular buffer。
- [x] 区分 puncturing、shortening、repetition、filler。
- [x] 给小型 circular buffer 例子。
- [x] 给伪代码。
- [x] 给浮点仿真检查项。
- [x] 给定点/RTL 映射：LLR RAM、address generator、mask。
- [x] 常见错误和自测题答案。
- [x] 单篇审计并记录结果。

#### T9.1 细化交付物

- [x] 必须解释 rate recovery 的目标：把顺序 LLR 流恢复为 LDPC decoder 需要的母码位置软信息。
- [x] 必须列发送端 rate matching 与接收端 rate recovery 的逆向关系表。
- [x] 必须给从 `rx_llr[0:E-1]` 到 `ldpc_llr[0:N-1]` 的对象转换。
- [x] 必须说明 `E`、`Ncb`、`N`、`K` 的区别。
- [x] 必须说明未知位置、已知 shortened 位置和 repeated 位置如何初始化。
- [x] 图中必须包含 demapper、bit deinterleaver、circular buffer restore、LDPC core。
- [x] 小型例子必须包含至少一个未发送位置和一个重复位置。
- [x] 伪代码必须包含地址扫描、mask 判断、LLR 写回/累加。
- [x] 验证必须包含覆盖率统计：新写入、重复、未知、shortened。

### T9.2 NR LDPC Circular Buffer、Puncturing、Shortening、Repetition

- [x] 提取 T9.2 Prompt、验收、证据。
- [x] 精读 TS 38.212 相关条文。
- [x] 解释 circular buffer。
- [x] 解释 puncturing：有效编码位未发送，接收端未知/中性 LLR。
- [x] 解释 shortening：已知固定值位置，接收端强已知 LLR。
- [x] 解释 repetition：同一编码位重复发送，LLR 累加。
- [x] 画三类位置在 circular buffer 中的图。
- [x] 给数值例子。
- [x] 讲 unknown mask、shortened mask、repetition accumulation。
- [x] 给 Python 验证片段。
- [x] 常见错误：punctured 当 0、shortened 当 unknown、repeated 覆盖旧 LLR。
- [x] 单篇审计并记录结果。

#### T9.2 细化交付物

- [x] 必须用同一张图对比 puncturing、shortening、repetition 在 circular buffer 中的状态。
- [x] 必须讲清 puncturing 不是业务 0，而是没有观测。
- [x] 必须讲清 shortening 是接收端已知约束，和 puncturing 不同。
- [x] 必须讲清 repetition 是同一编码比特多次观测，LLR 相加。
- [x] 必须给一个小型数组例子，展示三类位置的 LLR 初始化。
- [x] 必须给一个错误对照：punctured 填强 LLR、shortened 填 0、repeated 覆盖旧值。
- [x] 必须说明定点中 repeated accumulation 的饱和。
- [x] 必须给 RTL 映射：unknown mask、known mask、repeat combiner。
- [x] Python 片段必须能输出三类位置的最终 LLR 数组。

### T9.3 NR HARQ Soft Buffer、RV、CBG

- [x] 提取 T9.3 Prompt、验收、证据。
- [x] 精读 TS 38.212/TS 38.214 中 RV、HARQ、CBG 相关锚点。
- [x] 对比 LTE T7.3 的共同点和差异。
- [x] 解释 NR LDPC RV 在 circular buffer 中的意义。
- [x] 解释 CBG 的中文含义、为什么引入、解决什么问题。
- [x] 画 NR HARQ soft buffer 图：TB、CB、CBG、RV、soft buffer。
- [x] 给 CBG 部分重传例子。
- [x] 列状态字段：harq_id、tb_id、cb_id、cbg_id、rvidx、new_data_indicator、cbg_mask。
- [x] 讲新覆盖、重复覆盖、CBG 未重传保持。
- [x] 讨论定点饱和。
- [x] 给失败案例：CBG mask 错、HARQ 复用未清、RV mismatch。
- [x] 给验证方法和最小 dump 包。
- [x] 单篇审计并记录结果。

#### T9.3 细化交付物

- [x] 必须解释 CBG 的英文全称、中文含义、和 CB/TB 的层级关系。
- [x] 必须画 TB -> CBG -> CB -> circular buffer -> soft buffer 的层级图。
- [x] 必须对比 LTE T7.3：LTE 没有 NR CBG 这种部分重传粒度。
- [x] 必须说明 RV 改变 LDPC circular buffer 读取区域。
- [x] 必须说明 CBG 未被重传时对应 soft buffer 保持不变。
- [x] 必须给 CBG mask 例子：某些 CBG 重传，其他 CBG 保留。
- [x] 必须列 soft buffer key：`harq_id/tb_id/cbg_id/cb_id/addr`。
- [x] 必须给定点饱和例子。
- [x] 必须给失败案例的最小日志：CBG mask、RV、CB status、TB CRC。
- [x] 图必须体现部分重传，而不是只画整 TB 重传。

### T9.4 NR LDPC 解交织与 LLR 放置

- [x] 提取 T9.4 Prompt、验收、证据。
- [x] 精读 TS 38.212 bit interleaving/rate matching 相关章节。
- [x] 解释 Qm 如何影响 LLR 排列。
- [x] 讲 demapper 输出 LLR 与 LDPC decoder 输入 LLR 的映射。
- [x] 给 QPSK 例子。
- [x] 给 16QAM 例子。
- [x] 画 bit deinterleaving 流程图。
- [x] 讲 permutation address generator、LLR reorder buffer、bank conflict。
- [x] 给伪代码。
- [x] 常见错误：Qm 配错、bit order 反、layer/codeword 映射错。
- [x] 单篇审计并记录结果。

#### T9.4 细化交付物

- [x] 必须解释 bit interleaving 为什么与调制阶数 `Qm` 相关。
- [x] 必须给 QPSK 下每个符号两个 LLR 的顺序例子。
- [x] 必须给 16QAM 下每个符号四个 LLR 的顺序例子。
- [x] 必须说明 bit order 错误如何表现为高 SNR 下仍 CRC fail。
- [x] 必须画 LLR reorder buffer 的读写方向。
- [x] 必须给伪代码：按 `Qm` 反交织并放回 rate recovery 输入。
- [x] 必须给验证方法：固定 symbol LLR pattern，检查输出索引。
- [x] RTL 映射必须包含 reorder buffer、address generator、bank conflict。

### T9.5 NR LDPC 码块处理、CB CRC、TB CRC

- [x] 提取 T9.5 Prompt、验收、证据。
- [x] 精读 TS 38.212 segmentation、CB CRC、TB CRC、码块拼接章节。
- [x] 讲译码后每个 CB 的处理。
- [x] 讲 filler 去除。
- [x] 讲 CB CRC 检查。
- [x] 讲 CB 拼接。
- [x] 讲 TB CRC 检查。
- [x] 讲 CBG 部分重传对 CB 处理的影响。
- [x] 给单个 CB CRC 失败案例。
- [x] 给所有 CB CRC 通过但 TB CRC 失败案例。
- [x] 给 CBG 部分重传后拼接状态错误案例。
- [x] 给接收端伪代码。
- [x] 给 Python 小例子验证拼接和 CRC 输入边界。
- [x] 单篇审计并记录结果。

#### T9.5 细化交付物

- [x] 必须说明 CB CRC 与 TB CRC 的职责区别。
- [x] 必须说明 filler 去除发生在码块拼接前的哪个位置。
- [x] 必须说明 CB 按协议顺序拼接，不能按译码完成顺序拼接。
- [x] 必须说明 CBG 部分重传后未更新 CB 的状态如何使用。
- [x] 必须给一个两个 CB 的拼接例子。
- [x] 必须给一个 CBG 部分重传例子。
- [x] 必须给三类失败案例的输入、现象、定位字段。
- [x] Python 片段必须能验证拼接长度和 CRC 输入范围。
- [x] 验证方法必须区分 CB CRC fail、TB CRC fail、HARQ feedback。

### T9.6 NR LDPC 边界案例

- [x] 提取 T9.6 Prompt、验收、证据。
- [x] 整理 BG 选择边界。
- [x] 整理 Zc 选择边界。
- [x] 整理 filler 边界。
- [x] 整理 punctured systematic bits。
- [x] 整理 limited buffer。
- [x] 整理 RV mismatch。
- [x] 整理 CBG mismatch。
- [x] 整理 LLR saturation。
- [x] 整理 syndrome 通过但 CRC 失败。
- [x] 整理 CRC 通过但上层组包失败。
- [x] 每个案例列触发条件、现象、必查字段、定位步骤、修复方向。
- [x] 给最小 dump 包字段。
- [x] 给诊断流程图。
- [x] 展开两个详细案例。
- [x] 单篇审计并记录结果。

#### T9.6 细化交付物

- [x] 每个边界案例必须至少有一行：触发条件、现象、必查字段、定位步骤、修复方向。
- [x] 必须展开 BG 边界案例，说明选错 BG 的 syndrome/CRC 现象。
- [x] 必须展开 Zc 边界案例，说明矩阵尺寸和地址错位现象。
- [x] 必须展开 RV mismatch 案例，说明 soft buffer 命中区域异常。
- [x] 必须展开 CBG mismatch 案例，说明部分重传状态污染。
- [x] 必须展开 syndrome pass but CRC fail 的案例，说明 LDPC 校验与业务 CRC 的边界。
- [x] 必须给最小 dump 包表，字段要能直接用于调试。
- [x] 必须给诊断流程图：先 descriptor，再 rate recovery，再 LDPC core，再 CRC。
- [x] 必须给“不要优先怀疑 LDPC core”的排查顺序说明。

### 模块 9 收尾

- [x] 运行 T9 全量术语、标题、深度、LaTeX、引用重建审计。
- [x] 生成或更新 T9 Prompt 覆盖矩阵。
- [x] 审核经理复核 T9：由阶段 9 L2 总体审核经理复核覆盖 T6-T11 共 41 篇，T9 逐篇状态均为通过。
- [x] 修复 T9 Critical/Important 问题：T9 早期单篇审核经理问题已在对应完成记录中关闭，阶段 9 L2 复核未发现 T9 内容级 Critical/Important。
- [x] 写入本文件完成记录。

## 阶段 7：完成模块 10 NR Polar 译码协议与算法

模块目标：把 NR Polar 控制信息译码讲细，包括控制信息链路、信道极化、可靠性序列、SC、SCL、CRC-aided SCL、速率恢复和边界案例。

### 阶段 7 通用完成定义

- [x] 每节必须讲清 Polar 的零基础理论，不得粗略跳到协议。
- [x] 每节必须区分 UCI、DCI、CRC、RNTI、payload、frozen bit、information bit。
- [x] 涉及 TS 38.212 表格时必须核验本地表格/原始 XML 并复现本节所需内容。
- [x] 每个算法节必须给 N=4 或 N=8 数值例子。
- [x] 每个算法节必须给路径、LLR、partial sum 或 path metric 的中间值。
- [x] 每节必须说明接收端 descriptor 和验证 dump 字段。
- [x] 每节必须说明硬件风险：树遍历、路径存储、排序、CRC checker、低延迟控制。
- [x] 每节必须运行单篇术语、标题、深度、LaTeX 审计。

### T10.1 NR Polar 控制信息接收链路总览

- [x] 提取 T10.1 Prompt、验收、证据。
- [x] 精读 TS 38.212 UCI/DCI Polar 相关章节。
- [x] 解释 Polar 码是什么、为什么 NR 控制信道用 Polar。
- [x] 解释控制信息与数据信息差异：短块、低延迟、高可靠、盲检。
- [x] 画接收端链路图：LLR -> rate recovery -> deinterleaving -> Polar decode -> CRC aided selection -> output。
- [x] 区分 UCI 与 DCI 背景，不扩展成控制信道课程。
- [x] 给小型控制信息 block 流程例子。
- [x] 列 descriptor：A、K、E、N、nmax、CRC length、interleaver flag、RNTI context。
- [x] 给验证方法和常见错误。
- [x] 单篇审计并记录结果。

#### T10.1 细化交付物

- [x] 必须解释 Polar 码中文名、英文名、适合短控制块的原因。
- [x] 必须解释控制信息与数据信息在可靠性、时延、长度上的差异。
- [x] 必须分别说明 UCI 和 DCI 在本节中的边界。
- [x] 接收链路图必须包含 CRC 辅助路径选择。
- [x] descriptor 必须包含 `A/K/E/N`、CRC 长度、interleaver flag、RNTI context、list size。
- [x] 必须给一个小型控制块从 LLR 到控制比特输出的流程例子。
- [x] 必须说明哪些 TS 38.212 章节本节只定位、哪些会在 T10.2-T10.7 展开。
- [x] 常见错误必须包含 UCI/DCI 配置混淆、CRC 类型错、RNTI 边界错。

### T10.2 信道极化、冻结位、信息位

- [x] 提取 T10.2 Prompt、验收、证据。
- [x] 从零基础讲信道极化。
- [x] 解释 bit-channel、可靠信道、不可靠信道、冻结位、信息位。
- [x] 用 N=4 或 N=8 例子讲极化变换。
- [x] 手算生成矩阵或蝶形结构。
- [x] 说明冻结位为什么通常固定为 0。
- [x] 讲接收端 frozen mask。
- [x] 画 Polar 编码树/蝶形图。
- [x] 给 Python 小例子。
- [x] 常见错误：info/frozen mask 反、bit-reversal 错、frozen 与 punctured 混淆。
- [x] 单篇审计并记录结果。

#### T10.2 细化交付物

- [x] 必须解释“信道极化”不是物理极化天线，而是比特信道可靠性分化。
- [x] 必须给 N=4 或 N=8 的极化变换图。
- [x] 必须手算至少一个输入向量的编码变换。
- [x] 必须解释 frozen bit 为什么固定，接收端如何使用 frozen mask。
- [x] 必须说明 information set 与 frozen set 是互补集合。
- [x] 必须解释 bit-reversal 或顺序约定的边界，若不展开则标明后续章节。
- [x] 必须给 Python 生成矩阵或蝶形变换片段。
- [x] 常见错误必须包含 frozen mask 反、索引基准错、frozen 与 punctured 混淆。

### T10.3 NR Polar 可靠性序列

- [x] 提取 T10.3 Prompt、验收、证据。
- [x] 精读 TS 38.212 Table 5.3.1.2-1。
- [x] 核验本地表格 HTML/CSV/media。
- [x] 复现本节使用的可靠性序列内容；必要时 Python 图片化完整表或子表。
- [x] 解释可靠性序列是什么，为什么标准化。
- [x] 讲如何根据 K 选择信息位索引。
- [x] 给 toy 可靠性排序例子。
- [x] 讲 frozen mask 生成。
- [x] 讲实现查表原因。
- [x] 给伪代码。
- [x] 常见错误：升序/降序、0-based/1-based、K/CRC 后长度混淆。
- [x] 单篇审计并记录结果。

#### T10.3 细化交付物

- [x] 必须核验 TS 38.212 Table 5.3.1.2-1 的本地证据。
- [x] 必须说明可靠性序列的排序方向和索引基准。
- [x] 必须复现本节用到的可靠性序列子集；若完整表太长，生成图片或分组表。
- [x] 必须解释信息位选择：从可靠性序列中选 K 个位置。
- [x] 必须说明 CRC 比特是否计入 K 的边界。
- [x] 必须给 toy reliability order 例子，生成 info set/frozen set。
- [x] 必须给伪代码：输入 N、K，输出 info mask/frozen mask。
- [x] RTL 映射必须说明可靠性表 ROM 和 mask generator。
- [x] 常见错误必须包含升降序错、0/1-based 错、K 与 A 混淆。

### T10.4 SC 译码

- [x] 提取 T10.4 Prompt、验收、证据。
- [x] 解释连续消除译码 SC。
- [x] 从 Polar 树结构开始讲。
- [x] 推导 f LLR 函数。
- [x] 推导 g LLR 函数。
- [x] 解释 partial sums。
- [x] 讲 frozen bit 判决和 information bit 判决。
- [x] 用 N=4 数值例子完整走一遍。
- [x] 画树遍历图。
- [x] 讲复杂度和延迟。
- [x] 给 Python 片段。
- [x] 常见错误：f/g 符号错、partial sum 未更新、frozen 位仍按 LLR 判决。
- [x] 单篇审计并记录结果。

#### T10.4 细化交付物

- [x] 必须定义 SC、f 函数、g 函数、partial sum。
- [x] 必须先用树遍历直觉解释，再给公式。
- [x] f/g 公式必须逐符号解释。
- [x] 必须用 N=4 逐步列每次 f/g 计算。
- [x] 必须展示 frozen bit 判决强制为 0。
- [x] 必须展示 information bit 根据 LLR 符号判决。
- [x] 必须展示 partial sum 如何回传影响 g。
- [x] Python 片段必须复现 N=4 例子。
- [x] RTL 映射必须说明递归树如何变成迭代控制和存储。

### T10.5 SCL 译码

- [x] 提取 T10.5 Prompt、验收、证据。
- [x] 解释连续消除列表译码 SCL。
- [x] 讲路径分裂。
- [x] 讲路径度量 PM。
- [x] 推导或解释 LLR-domain path metric。
- [x] 讲列表大小 L。
- [x] 用 N=4、L=2 toy 例子走路径分裂、度量更新、排序、剪枝。
- [x] 讲硬件影响：sorter、path memory、copy network、partial sum memory。
- [x] 给伪代码。
- [x] 常见错误：PM 方向混淆、剪枝后状态未同步、frozen 位错误分裂。
- [x] 单篇审计并记录结果。

#### T10.5 细化交付物

- [x] 必须解释 SCL 相比 SC 解决的问题：单一路径早期判错不可恢复。
- [x] 必须定义 path、path metric、list size、split、prune。
- [x] 必须说明 frozen 位不分裂，information 位分裂。
- [x] 必须给 N=4、L=2 的完整路径表。
- [x] 每一步必须列路径比特、PM、是否保留。
- [x] 必须说明 PM 越小/越大的约定，全文保持一致。
- [x] 必须讲排序器和路径复制网络的硬件代价。
- [x] 必须给伪代码。
- [x] 常见错误必须包含 PM 方向反、路径状态未复制、frozen 位错误分裂。

### T10.6 CRC 辅助 SCL

- [x] 提取 T10.6 Prompt、验收、证据。
- [x] 精读 TS 38.212 Polar CRC 与控制信息相关章节。
- [x] 解释 CRC-aided SCL。
- [x] 讲 CRC 如何辅助路径选择。
- [x] 给最佳 PM 路径 CRC 失败、次优路径 CRC 通过案例。
- [x] 讲误通过风险。
- [x] 讲列表大小、低延迟、高可靠之间的取舍。
- [x] 讲硬件：多路径 CRC checker、final selector、early pruning。
- [x] 给伪代码。
- [x] 常见错误：只选 PM 最好、CRC bit 顺序错、RNTI scrambling 边界错。
- [x] 单篇审计并记录结果。

#### T10.6 细化交付物

- [x] 必须解释 CA-SCL 的中文含义和基本流程。
- [x] 必须说明 CRC 是路径选择辅助，不是译码算法本体替代。
- [x] 必须给“最佳 PM 路径 CRC fail，次优路径 CRC pass”的完整路径表。
- [x] 必须解释 CRC 误通过风险。
- [x] 必须讨论 list size 与性能、延迟、面积之间的关系。
- [x] 必须说明 DCI 中 CRC/RNTI 边界若未核验则保持待核验。
- [x] 必须给 final selector 伪代码。
- [x] RTL 映射必须包含多路径 CRC checker 和 sorter/final select。
- [x] 常见错误必须包含只看 PM、不看 CRC、CRC bit order 错、RNTI 边界错。

### T10.7 Polar 速率恢复

- [x] 提取 T10.7 Prompt、验收、证据。
- [x] 精读 TS 38.212 Polar rate matching 相关章节。
- [x] 讲接收端反操作。
- [x] 讲 sub-block deinterleaving。
- [x] 讲 bit collection。
- [x] 讲 puncturing。
- [x] 讲 shortening。
- [x] 讲 repetition。
- [x] 讲 bit interleaving。
- [x] 给小型循环缓存例子。
- [x] 解释 LLR 初始化：punctured unknown、shortened strong known、repeated accumulate。
- [x] 画速率恢复流程图。
- [x] 对比 LDPC/LTE Turbo rate recovery。
- [x] 给 Python toy model。
- [x] 常见错误：puncturing/shortening 反、interleaving flag 漏用、E/N/K 边界错。
- [x] 单篇审计并记录结果。

#### T10.7 细化交付物

- [x] 必须精读并定位 Polar rate matching/rate recovery 的 TS 38.212 章节。
- [x] 必须分别解释 sub-block deinterleaving、bit collection、bit interleaving。
- [x] 必须解释 puncturing、shortening、repetition 对 LLR 初始化的不同影响。
- [x] 必须给一个小型循环缓存例子，至少包含 punctured、shortened、repeated 中两类。
- [x] 必须画 rate recovery 反操作流程图。
- [x] 必须对比 LDPC 和 LTE Turbo 的差异，避免混用规则。
- [x] 必须给 Python toy model。
- [x] 常见错误必须包含 puncturing/shortening 反、interleaver flag 漏用、E/N/K 边界错。

### T10.8 NR Polar 边界案例

- [x] 提取 T10.8 Prompt、验收、证据。
- [x] 整理无 CRC 小负载。
- [x] 整理 CRC 长度选择。
- [x] 整理列表大小耗尽。
- [x] 整理 path metric 并列。
- [x] 整理 puncturing/shortening mismatch。
- [x] 整理 frozen mask 错。
- [x] 整理 DCI/UCI 背景不匹配。
- [x] 整理 RNTI/CRC 边界。
- [x] 每个案例列触发条件、现象、必查字段、定位步骤、修复建议。
- [x] 展开 frozen mask 错导致候选 CRC fail 案例。
- [x] 展开 PM 最优路径 CRC fail 但次优路径通过案例。
- [x] 给最小 dump 包。
- [x] 单篇审计并记录结果。

#### T10.8 细化交付物

- [x] 每个边界案例必须列触发条件、现象、必查字段、定位步骤、修复建议。
- [x] 必须展开无 CRC 小负载路径选择边界。
- [x] 必须展开 frozen mask 错误案例。
- [x] 必须展开 path metric 并列案例。
- [x] 必须展开 puncturing/shortening mismatch 案例。
- [x] 必须展开 DCI/UCI descriptor 不匹配案例。
- [x] 必须给最小 dump 包：A/K/E/N、CRC type、info set、frozen set、reliability slice、L、PM list、CRC results。
- [x] 必须给诊断流程：descriptor -> rate recovery -> mask -> SC/SCL -> CRC selector。

### 模块 10 收尾

- [x] 运行 T10 全量术语、标题、深度、LaTeX、引用重建审计。
- [x] 生成或更新 T10 Prompt 覆盖矩阵。
- [x] 审核经理复核 T10：由阶段 9 L2 总体审核经理复核覆盖 T6-T11 共 41 篇，T10 逐篇状态均为通过。
- [x] 修复 T10 Critical/Important 问题：T10 用户指出的 T10.2/T10.7 图形问题已修复并写入全局规则，阶段 9 L2 复核未发现 T10 内容级 Critical/Important。
- [x] 写入本文件完成记录。

## 阶段 8：完成模块 11 LTE/NR 译码对比

模块目标：从协议、算法、接收端流程、硬件、存储、延迟、吞吐、验证角度对比 Turbo、LDPC、Polar，不写成浅表速查表。

### 阶段 8 通用完成定义

- [x] 每节必须先提取 roadmap Prompt、验收、前置和 3GPP/证据，并写入讲义执行记录或审计矩阵。
- [x] 每节必须明确对比对象：LTE Turbo、NR LDPC、NR Polar 中哪些参与本节，哪些不适用及原因。
- [x] 涉及协议时必须定位 TS 36.212、TS 38.212、必要时 TS 36.213/38.214/36.321/38.321 的章节、本地路径和待核验边界。
- [x] 对比不能只给速查表，必须先讲每个对象的理论/协议背景，再讲共同点、差异、工程后果和验证方法。
- [x] 每节必须给统一接收端对象模型或 descriptor，对比字段来源、字段含义、错误后果。
- [x] 每节必须至少给一个小型例子；若是硬件对比，必须给资源/延迟/存储估算或决策矩阵。
- [x] 每节必须给常见错误、诊断字段、验证 checklist 和工程思考题答案。
- [x] 涉及图表的章节必须生成或复现清晰图表，图片必须目检无遮挡、无拥挤、读图顺序明确。
- [x] 每节必须运行术语、标题、深度、LaTeX 审计；涉及引用复现的章节还必须运行引用重建审计。
- [x] 每节完成后必须更新 `docs/audits/prompt_coverage_matrix.md` 或记录待统一更新项。

### T11.1 Turbo、LDPC、Polar 算法对比

- [x] 提取 T11.1 Prompt、验收、证据。
- [x] 定位 LTE Turbo 在 TS 36.212 中的链路，定位 NR LDPC/Polar 在 TS 38.212 中的链路。
- [x] 解释 Turbo 码、LDPC 码、Polar 码各自解决的问题和采用场景。
- [x] 对比图模型：Turbo trellis、LDPC Tanner graph、Polar decoding tree。
- [x] 对比译码行为：Turbo SISO 迭代、LDPC message passing、Polar SC/SCL path search。
- [x] 对比软信息语义：channel LLR、extrinsic information、check/variable messages、path metric。
- [x] 对比停止条件：Turbo CRC/迭代、LDPC syndrome/CRC/迭代、Polar CRC-aided selection。
- [x] 对比复杂度：计算、存储、排序、迭代、延迟、并行度。
- [x] 对比数据/控制信道适配性，说明长数据块与短控制块的需求不同。
- [x] 解释为什么不能简单说“LDPC 比 Turbo 好”，必须放在协议代际、块长、吞吐和硬件条件下讨论。
- [x] 给一张算法行为对比表和一张工程取舍矩阵。
- [x] 给一个“同样输入 LLR，被三类译码器如何消费”的教学例子。
- [x] 给验证方法：BLER 曲线、bit-exact、latency、memory trace、CRC/syndrome/path metric。
- [x] 单篇审计并记录结果。

#### T11.1 细化交付物

- [x] 正文必须先分别解释 Turbo/LDPC/Polar 名称、基本思想和接收端译码对象。
- [x] 必须说明 LTE 数据传输历史上使用 Turbo，NR 数据传输使用 LDPC，NR 控制信息使用 Polar 的协议背景。
- [x] 必须画或复现三种图模型，不允许只用文字说“图不同”。
- [x] 必须给“协议使用位置”和“算法结构”分开的对比表。
- [x] 必须给“同一工程指标下的取舍”：吞吐、时延、面积、功耗、存储、验证复杂度。
- [x] 必须说明本节是对比课，详细公式推导分别承接 T6、T8、T10。
- [x] 常见错误必须包含：把 Polar 当数据大块码、把 LDPC syndrome 当业务 CRC、把 Turbo 外信息当 LDPC 消息。

### T11.2 速率匹配/恢复对比

- [x] 提取 T11.2 Prompt、验收、证据。
- [x] 精读 TS 36.212 LTE Turbo rate matching/rate recovery 相关锚点。
- [x] 精读 TS 38.212 NR LDPC rate matching/rate recovery 相关锚点。
- [x] 精读 TS 38.212 NR Polar rate matching/rate recovery 相关锚点。
- [x] 对比三者发送端 rate matching 与接收端 rate recovery 的逆向关系。
- [x] 对比 circular buffer、sub-block interleaving、bit interleaving、puncturing、shortening、repetition、RV、LLR 放回。
- [x] 画三条并排小流程图：LTE Turbo、NR LDPC、NR Polar。
- [x] 建立统一对象模型：`rx_llr`、`E`、`Ncb/N`、address generator、mask、soft buffer、decoder input LLR。
- [x] 给一个小型循环缓存例子，分别解释 Turbo/LDPC/Polar 的相似点和差异点。
- [x] 列典型错误对比：punctured 当 0、shortened 当 unknown、repeated 覆盖、interleaver flag 错、RV 起点错。
- [x] 给验证 checklist：索引、mask、LLR 累加、饱和、CRC/syndrome/path metric。
- [x] 单篇审计并记录结果。

#### T11.2 细化交付物

- [x] 必须说明 rate recovery 的共同目标：把线性接收 LLR 流恢复成译码器母码位置软信息。
- [x] 必须明确 LTE Turbo 没有 NR Polar shortening 语义，NR LDPC/Polar 的 puncturing/shortening 不能套用 LTE filler/`<NULL>`。
- [x] 必须给统一字段表，并列出每个字段在 LTE/NR 中是否存在。
- [x] 必须给小例子，至少包含一个未发送位置和一个重复位置。
- [x] 必须说明定点实现中 repeated LLR 累加和饱和的共同风险。
- [x] 必须说明 RTL 中 address generator 和 mask RAM 可共享的抽象，以及不能共享的协议规则。
- [x] 图必须标出读图顺序和每个流程的输入输出。

### T11.3 HARQ 与 Soft Buffer 对比

- [x] 提取 T11.3 Prompt、验收、证据。
- [x] 精读 LTE HARQ soft buffer 与 RV 在 TS 36.212/36.213 中的边界。
- [x] 精读 NR HARQ soft buffer、RV、CBG 在 TS 38.212/38.214 中的边界。
- [x] 讲共同点：LLR soft combining、RV、HARQ process、soft buffer key、new data 清缓存。
- [x] 讲差异：LTE Turbo CB 级处理，NR LDPC CB/CBG，CBG partial retransmission。
- [x] 画 LTE/NR HARQ soft buffer 对比图，必须体现 LTE RV ring buffer 和 NR CBG mask。
- [x] 给 LTE TB 重传例子：RV0 初传、RV2 重传、LLR 累加、TB CRC。
- [x] 给 NR CBG 部分重传例子：只重传部分 CBG，未重传 CBG soft buffer 保持。
- [x] 讲硬件影响：indexing、bank、flush/release、saturation、CBG mask、descriptor lifetime。
- [x] 给 descriptor 对比表：`harq_id`、`tb_id`、`cb_id`、`cbg_id`、`rvidx`、`ndi`、`soft_buffer_addr`。
- [x] 常见错误：LTE 逻辑套 NR CBG、CBG mask 漏用、HARQ 复用未清、RV 只进日志不进地址。
- [x] 单篇审计并记录结果。

#### T11.3 细化交付物

- [x] 必须明确 HARQ soft buffer 是译码器状态，不只是 MAC 状态。
- [x] 必须画两种 soft buffer 生命周期：new data 分配、retransmission 合并、CRC pass 释放、fail 保留。
- [x] 必须给 LTE 和 NR 各一个小型地址/LLR 累加表。
- [x] 必须讨论定点饱和和 saturation counter。
- [x] 必须给最小 dump 包对比：LTE 必查 RV/k0/Ncb，NR 额外必查 CBG mask/BG/Zc。
- [x] 必须说明哪些调度细节本节只保留对译码器状态有影响的部分。
- [x] 验证必须包含 soft buffer 串 HARQ 进程、RV mismatch、CBG mask mismatch 的负测试。

### T11.4 硬件架构取舍对比

- [x] 提取 T11.4 Prompt、验收、证据。
- [x] 对比 Turbo 硬件瓶颈：SISO、alpha/beta、interleaver、iteration latency。
- [x] 对比 LDPC 硬件瓶颈：check-node min tree、layered schedule、message memory、bank conflict。
- [x] 对比 Polar 硬件瓶颈：path memory、sorter、partial sums、CRC selection。
- [x] 对比吞吐、延迟、面积、功耗、存储、控制复杂度。
- [x] 给工程决策矩阵。
- [x] 讲统一译码子系统中可共享和不可共享的部分。
- [x] 给验证影响对比。
- [x] 常见错误：只比算法不比存储、忽略 sorter、忽略 bank conflict。
- [x] 单篇审计并记录结果。

#### T11.4 细化交付物

- [x] 必须分别画 Turbo、LDPC、Polar 的硬件数据通路框图。
- [x] Turbo 必须包含 SISO/BCJR、alpha/beta memory、interleaver/deinterleaver、extrinsic RAM、iteration controller。
- [x] LDPC 必须包含 layered controller、check-node unit、variable-node update、message memory、LLR RAM、bank conflict 处理。
- [x] Polar 必须包含 SC/SCL tree controller、LLR memory、partial sum memory、path memory、sorter、CRC checker。
- [x] 工程决策矩阵必须包含吞吐、时延、面积、功耗、存储、控制复杂度、验证难度。
- [x] 必须说明哪些模块可以共享：DMA、输入 LLR buffer、CRC checker、寄存器文件、中断/status。
- [x] 必须说明哪些模块不宜共享：Turbo interleaver、LDPC CN/VN 更新、Polar sorter/path memory。
- [x] 必须给至少一个吞吐或周期估算示例，标明为教学估算。
- [x] 常见错误必须包含只看计算单元不看存储带宽、忽略排序器、忽略 bank conflict、忽略复位/flush。

### T11.5 信道和信息类型到译码器家族映射

- [x] 提取 T11.5 Prompt、验收、证据。
- [x] 精读 TS 36.212/38.212 相关锚点，并记录本地路径。
- [x] 映射 LTE DL-SCH/UL-SCH 到 Turbo。
- [x] 映射 NR DL-SCH/UL-SCH 到 LDPC。
- [x] 映射 NR UCI/DCI 到 Polar。
- [x] 讲控制信息和数据信息为何不同。
- [x] 给速查表和文字解释。
- [x] 讲边界情况：小 payload、UCI on PUSCH、DCI CRC/RNTI、NR CBG。
- [x] 给接收端选择逻辑。
- [x] 给工程接口字段：decoder_type、payload_type、channel_type、crc_type、harq_context。
- [x] 给配置错误案例：数据误送 Polar、控制误送 LDPC、CRC/RNTI 背景错、UCI on PUSCH 边界错。
- [x] 给验证方法：协议向量分类、descriptor 分支覆盖、错误注入和 status code。
- [x] 单篇审计并记录结果。

#### T11.5 细化交付物

- [x] 必须先说明“信道/信息类型决定译码器家族”的协议原因，不允许只给速查表。
- [x] 必须列 LTE 与 NR 的数据/控制信息映射表，包含协议锚点。
- [x] 必须解释 DL-SCH、UL-SCH、UCI、DCI 首现缩写和中文含义。
- [x] 必须说明控制信息短、低时延、高可靠和盲检背景为何影响 Polar 选择。
- [x] 必须说明数据业务长块、高吞吐为何影响 Turbo/LDPC 选择。
- [x] 接收端选择逻辑必须给伪代码或判定表。
- [x] descriptor 必须包含 `rat`、`channel_type`、`payload_type`、`decoder_type`、`crc_type`、`harq_context`、`control_context`。
- [x] 常见错误必须覆盖跨制式规则混用、UCI/DCI 背景混淆、CRC 类型错、HARQ context 缺失。

### 模块 11 收尾

- [x] 运行 T11 全量术语审计。
- [x] 运行 T11 全量标题审计。
- [x] 运行 T11 全量深度审计。
- [x] 运行 T11 全量 LaTeX 审计。
- [x] 运行 T11 引用重建审计。
- [x] 生成或更新 T11 Prompt 覆盖矩阵。
- [x] 逐篇核对 T11.1-T11.5 是否覆盖 Prompt 并适当拓展。
- [x] 逐篇核对 T11.1-T11.5 是否存在口语化标题、缩写首现问题、思考题无答案问题。
- [x] 逐篇核对协议证据表、执行记录、图片脚本和本地路径。
- [x] 审核经理复核 T11：由阶段 9 L2 总体审核经理复核覆盖 T6-T11 共 41 篇，T11 逐篇状态均为通过。
- [x] 修复 T11 Critical/Important 问题：T11 用户指出的 T11.1/T11.2/T11.3 图形问题已修复并写入全局规则，阶段 9 L2 复核未发现 T11 内容级 Critical/Important。
- [x] 写入本文件完成记录。

## 阶段 9：L2 总体审查

### 阶段 9 通用审查定义

- [x] 审查范围固定为 `docs/L2/T6.*.md` 到 `docs/L2/T11.*.md`，不得抽检。
- [x] 每篇必须核对 roadmap Prompt 原文、正文覆盖证据、适当拓展、缺口和修复动作。
- [x] 每篇必须核对协议精读是否围绕本地 TS 路径、章节、表/图/公式展开。
- [x] 每篇必须核对零基础理论铺垫是否足够：概念来源、为什么需要、解决什么问题、直观例子、正式定义、工程后果。
- [x] 每篇必须核对缩写首现、标题正式化、工程思考题答案、执行与证据记录。
- [x] 每篇必须核对 LaTeX 是否全量渲染成功，不允许抽检。
- [x] 每篇必须核对协议表/图/公式引用是否复现或明确待核验关闭条件。
- [x] 每篇必须核对图片是否精美、清晰、无遮挡，脚本和输出路径是否记录。

### 阶段 9 逐主题一致性审查

- [x] 核对 LLR 定义一致性：正号含义、幅度含义、饱和、未知 LLR、符号约定。
- [x] 核对 CRC 定义一致性：TB CRC、CB CRC、Polar CRC-aided、误通过风险、CRC 与 syndrome 边界。
- [x] 核对 filler、`<NULL>`、puncturing、shortening、repetition 定义一致性。
- [x] 核对 LTE RV 与 NR RV 的共同点和差异，特别是循环缓存起点、CBG 和 soft buffer key。
- [x] 核对 LTE soft buffer 与 NR soft buffer 区分，避免把 NR CBG 逻辑写入 LTE。
- [x] 核对 Turbo、LDPC、Polar 协议证据闭环：每类译码器的 TS 章节、输入输出和接收端流程。
- [x] 核对所有 descriptor 字段命名一致性：`tb_id`、`cb_id`、`cbg_id`、`harq_id`、`rvidx`、`E`、`Ncb`、`K`、`Zc`、`BG`。
- [x] 核对所有 Python 片段是否有预期输出或可执行检查命令。
- [x] 核对所有工业用例是否不超过约定数量，且不是泛泛描述。

### 阶段 9 自动审计命令

- [x] 运行 L2 全量术语审计：`python3 tools/audit_lesson_terms.py docs/L2/T*.md`。
- [x] 运行 L2 全量标题审计：`python3 tools/audit_markdown_headings.py docs/L2/T*.md`。
- [x] 运行 L2 全量深度审计：`python3 tools/audit_lesson_depth.py --strict docs/L2/T*.md`。
- [x] 运行 L2 全量 LaTeX 审计：`python3 tools/audit_latex_render.py docs/L2/T*.md`。
- [x] 运行 L2 引用重建审计：`python3 tools/audit_reference_rebuilds.py docs/L2/T*.md`。
- [x] 运行或更新 L2 Prompt 覆盖审计，输出到 `docs/audits/prompt_coverage_matrix.md`。
- [x] 对所有嵌入式 Python 片段，能执行的必须执行；不能执行的必须记录原因和关闭条件。
- [x] 对所有图片脚本，能重生成的必须重生成或至少运行脚本 dry check；不能运行的记录原因。

### 阶段 9 输出文件

- [x] 生成 L2 总体审查报告：`docs/audits/L2_overall_review.md`。
- [x] 报告必须包含逐篇状态表：文件、Prompt 覆盖、拓展充分性、协议证据、图片/表格、LaTeX、自动审计、遗留问题。
- [x] 报告必须包含按严重度排序的问题清单：Critical、Important、Minor。
- [x] 报告必须包含修复优先级：先协议错误，再 Prompt 漏项，再渲染/图片，再风格。
- [x] 审核经理复核 L2。
- [x] 修复或重分类所有 L2 内容级 Critical/Important 问题：当前 Critical=0；T6.4 资产证据链已入总表；TS 38.214 MCS/TBS 表值已重分类为 L3 条件项；图片局部视觉审计作为持续控制保留。
- [x] 修复后重新运行受影响范围审计，不用旧结果替代。
- [x] 写入本文件完成记录。

## 阶段 10：最终交付记录

### 阶段 10 文档更新

- [x] 更新 `docs/audits/full_project_document_review.md`，包含 L1/L2 全部已完成讲义状态。
- [x] 更新 `docs/audits/global_compliance_review.md`，逐条核对用户全局要求是否遵守。
- [x] 更新 `docs/audits/prompt_coverage_matrix.md`，覆盖所有已完成文档。
- [x] 更新未关闭 `待核验` 清单，列协议、章节、缺口、关闭条件、负责人/后续动作。
- [x] 更新图片资产清单，列脚本路径、输入数据、输出图片、使用讲义、目检状态。
- [x] 更新协议表/图/公式复现清单，列本地证据路径、复现方式、正文位置。

### 阶段 10 状态汇总

- [x] 历史阶段曾列出现有 L1 24 篇完成状态（T1.1-T4.3、T5.1-T5.5）、审计结果和遗留问题；当前阶段 4B 已补齐 T4.4-T4.6，L1 更新为 27 篇。
- [x] 列出 L2 T6-T11 完成状态：每个文件、审计结果、审核经理状态、遗留问题。
- [x] 列出尚未完成的小节和阻塞项。
- [x] 列出进入 L3 前必须补齐的问题：协议证据、模型代码、定点参数、RTL 接口、验证向量。
- [x] 汇总所有审计命令和结果，必须使用最新运行结果。
- [x] 汇总所有可执行 Python 片段和运行结果。
- [x] 汇总所有生成图片资产和目检结论。

### 阶段 10 L3 前准备清单

- [x] 明确 LTE Turbo Python golden model 需要的输入/输出格式。
- [x] 明确 NR LDPC Python golden model 需要的输入/输出格式。
- [x] 明确 NR Polar Python golden model 需要的输入/输出格式。
- [x] 明确定点模型需要的位宽、饱和、缩放、舍入和 bit-exact 对比策略。
- [x] 明确 RTL/ASIC 阶段需要的统一 descriptor、寄存器字段、状态码、错误码和 dump 包。
- [x] 明确验证向量分层：协议向量、教学 toy 向量、随机 BLER 向量、边界负测试、RTL bit-exact 向量。
- [x] 明确 CI 或本地回归命令草案。
- [x] 写最终完成记录。

## 阶段 11：完成模块 12 浮点仿真

模块目标：围绕 Python/MATLAB golden model、BLER 曲线、随机种子、输出文件和阈值，完成 LTE Turbo、NR LDPC、NR Polar 的可复现实验规划。

当前依赖：`T12.1` 依赖 `T4.6`。在 T4.4-T4.6 未补齐前，本阶段只允许做只读拆解和证据规划，不得写成已开工或已完成。

### 阶段 11 通用完成定义

- [x] 每节摘录 roadmap 卡片原文：前置、Prompt、产出、验收、3GPP/证据。
- [x] 每节给输入/输出格式、随机种子、日志字段、输出命名和失败重跑规则。
- [x] 涉及流程、曲线、目录或数据流的内容，优先补 Python 图；若不用图，必须说明 Markdown 表/流程图足够的原因。
- [x] 每节写协议证据表和执行与证据记录，工程任务也要写清协议参数回链位置与 `待核验` 关闭条件。
- [x] 每节运行单篇术语、标题、深度、LaTeX、引用重建审计；新增图片时运行图形几何审计。

### T12.1 Python Golden Model 工程布局

- [x] 要做什么：规定 LTE Turbo、NR LDPC、NR Polar Python golden model 的包结构、配置文件、向量文件、随机种子、日志和可复现命令示例；补三类译码器共用目录约定、输入/输出 schema、seed 传递、失败重跑和结果归档规则。
- [x] 协议证据：工程任务；协议向量来源回链 TS 36.212 Rel-19 `36212-j30` 与 TS 38.212 Rel-19 `38212-j30`，路径为 `3GPP_Rel19/processed/TS_36.212_36212-j30`、`3GPP_Rel19/processed/TS_38.212_38212-j30`。
- [x] 图形要求：建议生成“工程目录 + 配置 + seed/log 流转”图。
- [x] 验收与记录：通用单篇审计；执行正文中的脚手架/目录初始化命令示例，记录目录树、配置字段、向量命名规则、seed 示例和图形审计结果。

### T12.2 LTE Turbo 浮点仿真计划

- [x] 要做什么：定义编码器参考、AWGN 信道、解速率匹配、Log-MAP/Max-Log-MAP 译码、CRC 检查、BLER 曲线、随机种子、输出和阈值；正文必须落成实验矩阵、SNR 扫描、停止条件、trace 字段和对比口径。
- [x] 协议证据：TS 36.212 Rel-19 `36212-j30` §5.1.1-§5.1.4.1；TS 36.213 MCS/TBS 锚点保留 `待核验`，路径 `3GPP_Rel19/processed/TS_36.213_*`。
- [x] 图形要求：必须有 LTE Turbo 接收端仿真链路图或 BLER 输出样例图。
- [x] 验收与记录：通用单篇审计；命令模板至少覆盖 `seed`、`snr sweep`、`min frames`、`bler stop`、`trace output`；记录 Log-MAP/Max-Log-MAP 配置、阈值、输出 CSV/日志路径和待核验项。只读审核子代理 Critical=0、Important=3，已修复图形审计覆盖、AWGN 码率口径和 manifest/3GPP_译码知识库入口 核验闭环。

### T12.3 NR LDPC 浮点仿真计划

- [x] 要做什么：定义基图选择、提升、速率匹配/恢复、Min-Sum 变体、CRC 检查、BLER 曲线、随机种子、输出和阈值；包含 BP/MS/NMS/OMS 比较口径、BG/Zc/RV/E/Ncb 参数表和失败诊断入口。
- [x] 协议证据：TS 38.212 Rel-19 `38212-j30` §5.2.2/§5.3.2/§5.4.2/§6.2/§7.2；TS 38.214 Rel-19 `38214-j30` §5.1.3/§6.1.4；本地路径为 `TS_38.212_38212-j30` 与 `TS_38.214_38214-j30`。
- [x] 图形要求：必须有 BG/Zc/rate recovery/decoder/CRC 仿真流程图或比较曲线示意图。
- [x] 验收与记录：通用单篇审计；命令模板确认可切换 BP/MS/NMS/OMS、可记录 BG/Zc/RV、可输出 BLER/trace；记录失败 dump 字段。只读审核子代理首轮 Critical=0、Important=4，已修复 BP/SPA 符号解释、BP/MS/NMS/OMS 命令矩阵、CBG 精确证据回链和引用候选关闭条件；复审 Critical=0、Important=0，Minor 路径展开也已处理。

### T12.4 NR Polar 浮点仿真计划

- [x] 要做什么：定义可靠性序列、速率恢复、SC/SCL/CA-SCL、列表大小扫描、CRC 检查、延迟代理指标、随机种子、输出和阈值；明确 `A/K/E/N/L` 参数、CRC 选择、list-size sweep 和延迟代理指标。
- [x] 协议证据：TS 38.212 Rel-19 `38212-j30` §5.2.1/§5.3.1/§5.4.1/§6.3/§7.3；路径 `3GPP_Rel19/processed/TS_38.212_38212-j30`。
- [x] 图形要求：必须有 SC/SCL/CA-SCL + list-size sweep + latency proxy 流程或结果图。
- [x] 验收与记录：通用单篇审计；命令模板确认 `list size`、`CRC mode`、`seed`、`latency proxy`、`output` 参数齐全；记录可靠性序列/速率恢复证据。审核经理 Popper 首轮 `Critical=0, Important=2, Minor=2`，已修复阈值可执行例子、缩写首现和 SC/SCL/CA-SCL 二维命令矩阵；横向复核确认 T12.4 Prompt 覆盖充分，剩余同步项已转入模块 12 收尾。

### T12.5 BER/BLER 曲线生成与报告

- [x] 要做什么：讲解 BER/BLER 曲线生成、保存、绘制和解读，覆盖置信区间、最小帧数、仿真早停、CSV/PNG 命名和失败诊断；统一 LTE Turbo、NR LDPC、NR Polar 的曲线输出格式。
- [x] 协议证据：工程任务；TB/CB CRC 语义回链 TS 36.212 Rel-19 `36212-j30` 与 TS 38.212 Rel-19 `38212-j30`。
- [x] 图形要求：必须有规范化 BER/BLER 曲线图和失败诊断/命名规范图。
- [x] 验收与记录：通用单篇审计；执行曲线生成命令模板和读取 CSV 绘图命令模板；记录曲线字段、置信区间算法、最小帧数、早停规则和输出工件。已新增 T12.5 报告规范、Python 图、Wilson 区间、零错误上界、统一 `metrics.csv` schema、命名规则、失败诊断流程和未执行真实报告脚本边界；审核经理 Hegel 首轮 `Critical=0, Important=3, Minor=3`，已修复各指标 CI/upper-bound 字段、TB BLER/control BLER/false-pass 命令模板拆分、TS 38.212 §6.3 UCI PUCCH/PUSCH 锚点和字段命名；单篇审计通过，引用重建输出候选清单。

### 模块 12 收尾

- [x] 运行 `python3 tools/audit_lesson_terms.py docs/L3/T12*.md`。
- [x] 运行 `python3 tools/audit_markdown_headings.py docs/L3/T12*.md`。
- [x] 运行 `python3 tools/audit_lesson_depth.py --strict docs/L3/T12*.md`。
- [x] 运行 `python3 tools/audit_latex_render.py docs/L3/T12*.md`。
- [x] 运行 `python3 tools/audit_reference_rebuilds.py docs/L3/T12*.md`。
- [x] 更新 `docs/audits/prompt_coverage_matrix.md`，把 T12.1-T12.5 纳入覆盖矩阵。
- [x] 安排审核经理或等价复核，关闭 Critical/Important 后再进入模块 13。

## 阶段 12：完成模块 13 定点 C/C++ 模型

模块目标：围绕 LLR 位宽、饱和、缩放、SIMD 布局和 bit-exact 回归，完成 LTE Turbo、NR LDPC、NR Polar 的定点模型规划。

### 阶段 12 通用完成定义

- [x] 每节明确输入 LLR 位宽、内部消息位宽、饱和、舍入、缩放、性能损失预算和 bit-exact 对比口径。
- [x] 每节给浮点/定点对比对象、允许误差或 bit-exact 要求、失败分诊字段。
- [x] 涉及数据流、内存布局、bit-exact 比对链路的内容，优先补 Python 图。
- [x] 每节区分协议参数来源和实现量化策略，不得把量化策略写成 3GPP 强制要求。
- [x] 每节写执行与证据记录，落 bitwidth 表、saturation 策略、compare 命令和向量来源。

### T13.1 定点译码器需求

- [x] 要做什么：定义 LLR 位宽、内部消息位宽、饱和规则、舍入、缩放、性能损失预算和 bit-exact 对比方案；给统一 fixed-point requirement 模板。
- [x] 协议证据：无需直接 3GPP 引用；任何协议相关位宽/字段必须回链上游 T7、T9、T10 及相应仿真/向量任务。
- [x] 图形要求：可选；若正文包含多级量化链，补位宽/饱和流转图。
- [x] 验收与记录：通用单篇审计；记录位宽约定、饱和/舍入/缩放策略、损失预算、比对对象和通过/失败判定。

### T13.2 LTE Turbo 定点模型计划

- [x] 要做什么：规划 C/C++ 定点 LTE Turbo 译码器模型，覆盖分支度量、alpha/beta 度量、外信息缩放、交织器地址、饱和、max-log 修正选项和对 Python 的 bit-exact 测试；落结构体、数组布局、状态字段和 compare checkpoints。
- [x] 协议证据：TS 36.212 Rel-19 `36212-j30` §5.1.3.2/§5.1.4.1，路径 `3GPP_Rel19/processed/TS_36.212_36212-j30`。
- [x] 图形要求：建议生成 Turbo 定点数据通路或 compare flow 图。
- [x] 验收与记录：通用单篇审计；命令模板确认分支度量、alpha/beta、extrinsic、CRC 四层检查点齐全；记录位宽表、外信息缩放、max-log 开关和失败样例。

### T13.3 NR LDPC 定点模型计划

- [x] 要做什么：规划 C/C++ 定点 NR LDPC 译码器模型，覆盖 LLR/消息位宽、最小/次小存储、归一化/偏移、layered 调度、饱和、syndrome 检查和 bit-exact 测试；给 NMS/OMS 实验口径与 BLER 损失比较方法。
- [x] 协议证据：TS 38.212 Rel-19 `38212-j30` §5.3.2/§5.4.2，路径 `3GPP_Rel19/processed/TS_38.212_38212-j30`。
- [x] 图形要求：建议生成 min1/min2 + layered memory/update 图。
- [x] 验收与记录：通用单篇审计；命令模板可区分 MS/NMS/OMS，并能记录 syndrome/CRC/BLER loss；记录失败 dump 字段。

### T13.4 NR Polar 定点模型计划

- [x] 要做什么：规划 C/C++ 定点 NR Polar 译码器模型，覆盖 f/g 函数、路径度量位宽、部分和、列表剪枝、排序器影响、CRC 辅助选择和 bit-exact 测试；给 CA-SCL 数据结构和 PM 饱和检查点。
- [x] 协议证据：TS 38.212 Rel-19 `38212-j30` §5.3.1/§5.4.1，路径 `3GPP_Rel19/processed/TS_38.212_38212-j30`。
- [x] 图形要求：建议生成 SC/SCL 数据结构 + PM/CRC selector 图。
- [x] 验收与记录：通用单篇审计；命令模板确认 `L`、PM、CRC、path copy/split 检查点完整；记录 PM 饱和、部分和存储和排序器影响。

### T13.5 C/C++ 译码器 SIMD 与内存布局

- [x] 要做什么：讲解 Turbo、LDPC、Polar C/C++ 译码器的内存布局、对齐、SIMD 友好数组、缓存局部性和向量化机会，包含 profiling 计划和非合并访存失败案例；并排比较三类译码器数组布局。
- [x] 协议证据：无需直接 3GPP 引用；若引用生成向量，必须回链对应 LTE/NR 协议向量任务。
- [x] 图形要求：必须有 SIMD/内存布局对比图和失败案例图。
- [x] 验收与记录：通用单篇审计；记录数组布局、对齐规则、SIMD 宽度假设、profiling 指标、失败案例和图形审计结果。

### T13.6 Bit-Exact 回归框架

- [x] 要做什么：设计 bit-exact 回归框架，对比 Python 浮点/定点参考、C/C++ 定点模型和后续 RTL 输出，覆盖向量格式、元数据、种子追踪、容差、通过/失败方案和 CI 命令；给统一 vector schema 和 pass/fail policy。
- [x] 协议证据：工程任务；协议向量回链 TS 36.212 Rel-19 `36212-j30` 与 TS 38.212 Rel-19 `38212-j30`。
- [x] 图形要求：必须有 Python float/fixed -> C/C++ -> RTL compare pipeline 图。
- [x] 验收与记录：通用单篇审计；执行回归命令模板，记录向量 schema、metadata、seed、容差、CI 命令和失败归档。

### 模块 13 收尾

- [x] 运行 T13 全量术语、标题、深度、LaTeX、引用重建审计。
- [x] 更新 Prompt 覆盖矩阵，纳入 T13.1-T13.6。
- [x] 安排审核经理或等价复核，关闭 Critical/Important 后再进入模块 14。
- [x] 在完成记录写入 bitwidth 口径、compare policy、向量格式、回归命令模板、图表和审计结果。

## 阶段 13：完成模块 14 RTL/ASIC 译码器架构

模块目标：完成 Turbo、LDPC、Polar 微架构、统一子系统、软缓存和寄存器配置流的 RTL/ASIC 级架构规划。

### 阶段 13 通用完成定义

- [x] 每节必须画微架构图、关键存储图或控制/FSM 图，不能只写文字。
- [x] 每节区分协议输入、寄存器字段、实现策略和性能估算。
- [x] 每节给吞吐、存储、bank、地址生成、早停和错误处理的工程检查点。
- [x] 每节给验证入口：最小 dump 包、接口字段、状态码或时序观测点。
- [x] 涉及寄存器映射或 MAC/RRC/PHY 字段来源的内容，未精确核验前必须保持 `待核验`。

### T14.1 LTE Turbo RTL 微架构

- [x] 要做什么：设计 SISO 数据通路、alpha/beta 存储、外信息存储、交织/解交织地址生成器、乒乓迭代控制、CRC 早停、时钟/复位方案和吞吐估算；给 block diagram、FSM 和存储规模估算。
- [x] 协议证据：TS 36.212 Rel-19 `36212-j30` §5.1.3.2/§5.1.4.1；RTL 设计本身属于实现指导。
- [x] 图形要求：必须有 Turbo block diagram/FSM 图。
- [x] 验收与记录：通用单篇审计；记录 SISO/alpha/beta/extrinsic 存储口径、交织地址方案、迭代控制、CRC 早停和吞吐估算。

### T14.2 NR LDPC RTL 微架构

- [x] 要做什么：设计 layered 调度控制器、校验节点单元、变量节点更新、最小/次小数据通路、消息存储、LLR 存储、bank 冲突处理、syndrome/CRC 早停和吞吐估算；明确 memory banking 约束。
- [x] 协议证据：TS 38.212 Rel-19 `38212-j30` §5.3.2 的 table-driven QC 结构。
- [x] 图形要求：必须有 layered LDPC 架构/存储 bank 图。
- [x] 验收与记录：通用单篇审计；记录 bank conflict、layer schedule、min1/min2 路径和 early stop 观测点。

### T14.3 NR Polar RTL 微架构

- [x] 要做什么：设计 SC/SCL 树遍历、LLR 存储、部分和存储、路径存储、路径度量更新、排序/剪枝器、CRC 检查器和低延迟控制；点出 sorter bottleneck。
- [x] 协议证据：TS 38.212 Rel-19 `38212-j30` §5.3.1/§5.4.1。
- [x] 图形要求：必须有 CA-SCL 数据通路/排序器瓶颈图。
- [x] 验收与记录：通用单篇审计；记录 LLR/partial-sum/path/PM/sorter/CRC 结构和低延迟控制。

### T14.4 统一译码子系统架构

- [x] 要做什么：设计统一译码子系统，覆盖 Turbo、LDPC、Polar 引擎、共享输入/输出 DMA、软缓存、配置寄存器、中断/状态和错误处理，边界清晰到每个引擎可独立测试。
- [x] 协议证据：只作 context evidence，不能在未核验前把字段名写成协议强制要求；LTE/NR 配置上下文来自 TS 36.213、36.321、36.331、38.214、38.321、38.331，其中 TS 36.213 精确分册仍 `待核验`。
- [x] 图形要求：必须有 unified subsystem 顶层框图。
- [x] 验收与记录：通用单篇审计；记录共享/独占资源、状态码、错误码、DMA/soft-buffer 流转和待核验清单。

### T14.5 软缓存与 HARQ 存储架构

- [x] 要做什么：设计软缓存与 HARQ 存储架构，覆盖进程 ID、TB/CB/CBG 索引、RV 放置、饱和、存储 bank 划分、淘汰方案和 CRC 失败后的恢复，并比较 LTE 与 NR 差异。
- [x] 协议证据：TS 36.212 §5.1.4.1、TS 38.212 §5.4.2、TS 38.214 §5.1.7/§6.1.5；TS 36.213 anchors `待核验`。
- [x] 图形要求：必须有 LTE/NR soft buffer 地址和生命周期对比图。
- [x] 验收与记录：通用单篇审计；记录 `harq_id/tb_id/cb_id/cbg_id/rvidx` 地址键、bank 策略、淘汰/恢复规则。

### T14.6 译码器寄存器表与配置流

- [x] 要做什么：定义算法选择、块长、码率、BG、Zc、RV、Qm、HARQ ID、列表大小、迭代上限、start/status/error 中断，并追踪字段来自 PHY/MAC/RRC 的哪里。
- [x] 协议证据：算法参数来自 TS 36.212、TS 38.212；调度/HARQ 上下文来自 TS 36.213、TS 38.214；MAC/RRC 上下文来自 TS 36.321、36.331、38.321、38.331；精确字段未核验时保持 `待核验`。
- [x] 图形要求：必须有寄存器表/配置流/字段来源图。
- [x] 验收与记录：通用单篇审计；记录寄存器字段表、字段来源映射、配置流时序、错误码、状态码和待核验字段。

### 模块 14 收尾

- [x] 运行 T14 全量术语、标题、深度、LaTeX、引用重建审计。
- [x] 更新 Prompt 覆盖矩阵，纳入 T14.1-T14.6。
- [x] 安排审核经理或等价复核，关闭 Critical/Important 后再进入模块 15。
- [x] 在完成记录写入微架构图、寄存器/状态码、soft buffer 地址策略、`待核验` 字段和模块审计结果。

## 阶段 14：完成模块 15 综合与验证

模块目标：完成 SystemVerilog testbench、协议向量、覆盖率、DC 综合、时序收敛和最终证据报告的验证/签收规划。

### 阶段 14 通用完成定义

- [x] 每节给验证对象、输入向量、pass/fail 口径、随机种子、失败分诊和输出工件。
- [x] 每节区分文档中的命令模板和仓库现有可直接运行命令；工具不可用时明确写限制。
- [x] 牵涉测试架构、覆盖率、时序或 sign-off 流的内容，优先补 Python 图。
- [x] 最终报告类任务必须回链具体 TS 包名、章节、表/图/公式锚点和本地路径，不能用“参考前文”替代。
- [x] 每节写执行与证据记录，记录工具可用性、向量来源、覆盖率/综合/时序结果和遗留风险。

### T15.1 译码器 Testbench 架构

- [x] 要做什么：设计 Turbo、LDPC、Polar 译码引擎的 SystemVerilog testbench 架构，覆盖 driver、monitor、scoreboard、参考向量加载器、断言、复位测试和超时方案。
- [x] 协议证据：无需直接 3GPP 引用；生成向量必须回链 T7、T9、T10、T15.2 的 Rel-19 证据。
- [x] 图形要求：必须有 testbench block diagram。
- [x] 验收与记录：通用单篇审计；记录 driver/monitor/scoreboard/vector loader/assert/reset/timeout 和输出日志字段。

### T15.2 协议向量与边界案例套件

- [x] 要做什么：定义 LTE Turbo、NR LDPC、NR Polar 的协议向量和边界案例套件，覆盖最小/最大大小、填充位、CRC 失败、RV 不匹配、CBG、列表大小压力、LLR 饱和和运行中复位；给 directed test 清单与每项抓错目标。
- [x] 协议证据：TS 36.212、TS 38.212 提供尺寸、rate matching、CRC 锚点；精确 corner tables 必须核验。
- [x] 图形要求：建议有测试分类矩阵或边界案例分诊图。
- [x] 验收与记录：通用单篇审计；记录向量分类、协议章节、本地路径、最小 dump 包和未核验 exact tables。

### T15.3 覆盖率与回归方案

- [x] 要做什么：定义功能覆盖率、代码覆盖率、回归层级、随机种子、夜间运行、失败分诊和 sign-off 标准；覆盖算法家族、块长、RV、Qm、CRC 状态和复位。
- [x] 协议证据：无需直接 3GPP 引用；依赖协议参数的 coverage bin 必须回链 T7/T9/T10/T15.2。
- [x] 图形要求：建议有 coverage bin / regression tier 图。
- [x] 验收与记录：通用单篇审计；记录 coverage bins、回归层级、seed 策略、nightly 计划、pass criteria 和失败分诊。

### T15.4 Synopsys Design Compiler 综合流程

- [x] 要做什么：讲解译码 RTL 的 DC 综合流程，覆盖文件列表、时钟约束、复位假设、compile 方案、时序报告、面积报告、功耗估算和常见关键路径；若未安装 DC，必须说明工具可用性限制。
- [x] 协议证据：无需直接 3GPP 引用；若用协议向量做 DC 后验证，必须回链上游协议向量任务。
- [x] 图形要求：可选；建议给综合流程图。
- [x] 验收与记录：通用单篇审计；记录工具可用性、脚本骨架、约束假设、报告项、关键路径类型和风险声明。

### T15.5 时序收敛与关键路径调试

- [x] 要做什么：讲解关键路径识别、LDPC check-node min tree、Polar sorter、Turbo ACS/度量更新、流水线、retiming、寄存器复制和面积/时序取舍；给至少一个可诊断的违例样例。
- [x] 协议证据：无需直接 3GPP 引用；若引用协议向量或 block 参数，必须回链上游任务。
- [x] 图形要求：必须有关键路径/流水线改造图。
- [x] 验收与记录：通用单篇审计；记录关键路径类别、违例样例、pipeline/retiming/复制策略和面积/时序 tradeoff。

### T15.6 最终译码验证与证据报告

- [x] 要做什么：定义最终验证与证据报告格式，覆盖协议证据表、仿真摘要、定点损失、RTL 回归、覆盖率、综合时序/面积/功耗、已知限制和 sign-off 清单；给 audit-ready 模板。
- [x] 协议证据：必须汇总所有协议任务的精确 Rel-19 证据，列具体 TS 包名、章节、表/图/公式锚点和 `3GPP_Rel19/processed/...` 本地路径。
- [x] 图形要求：建议有证据汇总/签收面板图；若不用图，必须给清晰汇总表。
- [x] 验收与记录：通用单篇审计；记录最终报告模板、证据字段、仿真/定点/RTL/覆盖率/综合摘要项、已知限制和 sign-off checklist。

### 模块 15 收尾

- [x] 运行 T15 全量术语、标题、深度、LaTeX、引用重建审计。
- [x] 更新 Prompt 覆盖矩阵，纳入 T15.1-T15.6。
- [x] 安排审核经理或等价复核，关闭 Critical/Important 后再宣称 L3 文档阶段完成。
- [x] 在完成记录写入测试架构、向量分类、coverage/sign-off、DC 可用性、时序/综合证据、最终报告模板和遗留风险。

## 完成记录

| 时间 | 完成项 | 证据 |
|:---|:---|:---|
| 2026-06-20 | T7.3 单篇术语、标题、深度、LaTeX 审计通过 | `LESSON_TERM_AUDIT_OK`；`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；`LATEX_RENDER_AUDIT_OK formulas=63` |
| 2026-06-20 | T7.3 RV 长图重新生成并目检 | `tools/figures/render_lte_harq_rv_windows.py`；`docs/L2/assets/T7.3_LTE_HARQ_RV_windows.png` |
| 2026-06-20 | 全局规则新增 Prompt 最低线与适当拓展要求 | `合规与遵从.md`；`2026-06-19-lte-nr-decoding-learning-roadmap.md` |
| 2026-06-20 | Prompt 覆盖矩阵初版生成 | `docs/audits/prompt_coverage_matrix.md` |
| 2026-06-20 | T7.6 按 Prompt 和台账要求重写并通过单篇审计 | `LESSON_TERM_AUDIT_OK`；`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；`LATEX_RENDER_AUDIT_OK formulas=134`；`T7.6_LLR_SIGN_CHECK_OK` |
| 2026-06-20 | 剩余工作台账阶段 8-10 细化 | `docs/audits/lte_nr_decoding_remaining_work_register.md` 阶段 8 通用完成定义、T11.1-T11.5 细化交付物、阶段 9 全量审查、阶段 10 最终交付记录 |
| 2026-06-20 | T7.5 按 Prompt 和台账要求重写、补 Python 直观图并通过单篇审计 | `tools/figures/render_lte_dl_ul_decoder_context.py`；`docs/L2/assets/T7.5_LTE_DL_UL_decoder_context.png`；`LESSON_TERM_AUDIT_OK`；`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；`LATEX_RENDER_AUDIT_OK formulas=46` |
| 2026-06-20 | 全局规则新增难理解内容 Python 直观化和 Python 图片视觉审计要求 | `合规与遵从.md`；`2026-06-19-lte-nr-decoding-learning-roadmap.md` |
| 2026-06-20 | T7 全量自动审计通过，引用重建审计已生成 candidates 清单 | `LESSON_TERM_AUDIT_OK`；`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；`LATEX_RENDER_AUDIT_OK formulas=383`；`REFERENCE_REBUILD_AUDIT_CANDIDATES` |
| 2026-06-20 | T7.4/T7.6 嵌入式 Python 检查通过 | `T7.4_REASSEMBLY_OK`；`T7.6_LLR_SIGN_CHECK_OK` |
| 2026-06-20 | T7.3 关闭 `k0/NIR/Ncb` 公式重建缺口 | `docs/L2/T7.3_LTE_HARQ_soft_buffer_RV.md` 已复原 DL-SCH/PCH 主线 `Ncb`、`NIR`、`E`、`k0`、`<NULL>` 跳过公式；本地证据为 TS 36.212 `source.docx` 的 `rId155-rId177` 公式图片映射，并用 ETSI TS 36.212 V14.5.1 PDF 文本交叉核验。 |
| 2026-06-20 | T7 审核经理 Important 修复完成主线程侧整改 | T7.1 补 `<NULL>`/扫描指针/T7.2 承接说明；T7.4 新增“失败案例”；T7.1-T7.6 执行记录更新到最新审计结果；TS 36.213/36.321 精确锚点作为系统边界留待阶段 2/3 审查，不作为 TS 36.212 结论。 |
| 2026-06-20 | T7 最新全量自动审计与嵌入式校验通过 | `LESSON_TERM_AUDIT_OK`；`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；`LATEX_RENDER_AUDIT_OK formulas=434`；`REFERENCE_REBUILD_AUDIT_CANDIDATES`；`T7.4_REASSEMBLY_OK`；`T7.6_LLR_SIGN_CHECK_OK`。 |
| 2026-06-20 | T7 审核经理复核通过并修复 Minor | 审核经理结论：Critical=0、Important=0；已修复 T7.3 式号交叉引用和 §5.1.4.1.2 证据范围描述。修复后 T7 全量审计通过：`LESSON_TERM_AUDIT_OK`；`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；`LATEX_RENDER_AUDIT_OK formulas=435`；引用重建审计仍输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单。 |
| 2026-06-20 | 历史记录：阶段 2 已完成文档审查基线建立 | 当时已收集 L1 24 篇、L2 14 篇，确认当前无 L3 讲义；`docs/audits/full_project_document_review.md` 已生成逐篇状态表；当时全项目审计基线：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=2738`，深度审计仍有 5 篇 L1 triage，引用重建审计仍为候选清单待分类。该记录为历史快照，最新全项目 LaTeX 公式数以 2026-06-21 depth backlog 收尾记录的分段合计 `6428` 为准。 |
| 2026-06-20 | Prompt 覆盖矩阵同步 T7.3 最新状态 | `docs/audits/prompt_coverage_matrix.md` 已移除 T7.3 `k0/NIR/Ncb` 未复现的过期结论，改为记录 TS 36.212 主线公式已重建，TS 36.213/36.321 HARQ 控制锚点仍作为后续系统边界。 |
| 2026-06-20 | 阶段 4C 图片可读性整改：T7.3 LTE HARQ RV ring buffer 图 | 修复 `tools/figures/render_lte_harq_rv_windows.py`：画布从 `1900x1845` 扩为 `2220x2460`，保留并强化四个 RV 在 ring buffer 上的位置和四个 RV 传输模型；RV1 LLR 地址格改为两行 `104x68` chips，soft buffer 表提升到 20px 字号和 `56/64px` 表头/行高，下方四行 RV 模型表地址流改为两行 `76x42` chips，底部检查点与脚注重新留白。重生成 `docs/L2/assets/T7.3_LTE_HARQ_RV_windows.png` 后执行 `python3 tools/audit_figure_geometry.py tools/figures/render_lte_harq_rv_windows.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`；执行 `python3 tools/audit_figure_readability.py tools/figures/render_lte_harq_rv_windows.py` 输出 `FIGURE_READABILITY_AUDIT_OK`；目检确认表格字号可读、文字水平/垂直居中、箭头端点正常、底部留白充足、无遮挡、无硬拆词。 |
| 2026-06-20 | 5 篇 L1 深度 triage 已整改并通过全项目深度审计 | 已压缩 T1.1、T1.5、T2.3、T3.1、T3.3 中重复的“后续/不展开/未核验”边界表述，同时保留协议边界和关闭条件；审计结果：`python3 tools/audit_lesson_depth.py --strict docs/L1/T*.md docs/L2/T*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；术语和标题审计分别输出 `LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`。 |
| 2026-06-20 | 引用重建候选完整输出已生成 | 执行 `python3 tools/audit_reference_rebuilds.py docs/L1/T*.md docs/L2/T*.md > docs/audits/reference_rebuild_candidates_full.txt`，退出码 0，输出 633 行；该文件是候选清单，后续需分类，不直接等同为失败。 |
| 2026-06-20 | 历史记录：全项目 LaTeX 公式渲染全检通过 | 当时 `python3 tools/audit_latex_render.py docs/L1/T*.md docs/L2/T*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=2738`。该记录为历史快照，最新全项目 LaTeX 公式数以 2026-06-21 depth backlog 收尾记录的分段合计 `6428` 为准。 |
| 2026-06-20 | 阶段 3 全项目合规审查完成 | 已生成 `docs/audits/global_compliance_review.md` 和 `docs/audits/reference_rebuild_candidates_review.md`；结论：术语、标题、深度、LaTeX 均通过，Prompt 矩阵已同步；引用重建规则仍有 C 类 Important 协议证据项需阶段 4 关闭，包括 TS 36.213/36.321 HARQ/MAC 锚点、TS 36.212 Figure 5.1.3-2、TS 38.212 NR CRC 多项式、TS 38.214 MCS/TBS/RV/CBG 表格。 |
| 2026-06-20 | 阶段 4 关闭 TS 36.213/36.321 LTE HARQ/MAC 精确锚点缺口 | T7.3/T7.5/T7.6 已补 TS 36.213 `36213-j30_s08-s09` §8.3、§8.6、§8.6.1 和 TS 36.321 `36321-j20` §4.3.2、§4.4、§5.3.2.1、§5.3.2.2、§5.4.2.1 的本地路径、行号和使用边界；已同步 `reference_rebuild_candidates_review.md` 与 `global_compliance_review.md`；受影响三篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=283`。 |
| 2026-06-20 | 阶段 4 关闭 TS 36.212 Figure 5.1.3-2 Turbo 编码器图重建缺口 | 新增 `tools/figures/render_lte_turbo_encoder_structure.py`，生成 `docs/L2/assets/T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png`；T6.3 已插入图和读图说明，T6.1/T6.2/T6.4/T6.5/T6.6/T6.7/T6.8 已引用该资产；目检无文字遮挡；T6 审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=594`，T6.3 单篇补检 `LATEX_RENDER_AUDIT_OK formulas=60`。 |
| 2026-06-20 | 阶段 4 关闭 TS 38.212 NR CRC 多项式复现缺口 | T3.1 已复现 NR CRC24A、CRC24B、CRC24C、CRC16、CRC11、CRC6；证据为 TS 38.212 `source.docx` 的 `word/_rels/document.xml.rels` 映射：`rId25 -> media/image7.wmf`、`rId29 -> image9.wmf`、`rId32 -> image10.wmf`、`rId35 -> image11.wmf`、`rId39 -> image13.wmf`、`rId43 -> image15.wmf`；同步 `reference_rebuild_candidates_review.md` 与 `global_compliance_review.md`；T3.1 审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=36`。 |
| 2026-06-20 | 历史记录：阶段 4 后全项目自动审计重新确认 | 当时 `python3 tools/audit_lesson_terms.py docs/L1/T*.md docs/L2/T*.md` 输出 `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L1/T*.md docs/L2/T*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L1/T*.md docs/L2/T*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L1/T*.md docs/L2/T*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=2759`；引用重建审计仍输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，其中 TS 38.214 MCS/TBS/RV/CBG 表按阶段 6/8 使用点重建。该记录为历史快照，最新全项目 LaTeX 公式数以 2026-06-21 depth backlog 收尾记录的分段合计 `6428` 为准。 |
| 2026-06-20 | T8.1 NR LDPC 译码链路总览完成、审核经理 Important 已修复 | 新增 `docs/L2/T8.1_NR_LDPC_decoder_chain_overview.md`；新增 `tools/figures/render_nr_ldpc_decoder_chain_overview.py` 和 `docs/L2/assets/T8.1_NR_LDPC_decoder_chain_overview.png`；图片已目检无裁切、无遮挡、箭头未压字；审核经理结论 Critical=0、Important=2，已修复 CB CRC 条件性流程和 TS 38.214 §6.1.5 行 7099-7125 精确证据；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=40`。 |
| 2026-06-20 | T8.2 NR LDPC 基图选择完成，审核经理 Important 已修复 | 新增 `docs/L2/T8.2_NR_LDPC_base_graph_selection.md`；新增 `tools/figures/render_nr_ldpc_base_graph_selection.py` 和 `docs/L2/assets/T8.2_NR_LDPC_base_graph_selection_flow.png`；新增 `docs/audits/T8.2_NR_LDPC_BG_selection_formula_evidence.md` 固化 TS 38.212 `source.docx` 段落、关系 ID、媒体 SHA-256 和人工转写公式映射；审核经理结论 Critical=0、Important=2、Minor=2，已修复公式证据链、图表贴边、PCH 漏写和 `$K_b$` 未定义；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=157`。 |
| 2026-06-20 | T8.3 NR LDPC 提升大小与 QC-LDPC 矩阵构造完成并通过单篇审计 | 新增 `docs/L2/T8.3_NR_LDPC_lifting_QC_matrix.md`；新增 `tools/figures/render_nr_ldpc_lifting_qc_matrix.py` 和三张资产：`T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table.png`、`T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table.png`、`T8.3_NR_LDPC_toy_QC_expansion.png`；核验 `table_0013/0014/0015.csv/html` 行列数和 SHA-256，Table 5.3.2-1 已 Markdown 复现，Table 5.3.2-2/3 已图片化完整复现；图片目检无裁切、无遮挡；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=128`。 |
| 2026-06-20 | T8.4 LDPC Tanner 图与消息传递完成，审核经理 Important 已修复 | 新增 `docs/L2/T8.4_LDPC_Tanner_graph_message_passing.md`；新增/复用 `tools/figures/render_ldpc_tanner_syndrome.py` 和 `docs/L2/assets/T8.4_LDPC_Tanner_syndrome_toy.png`；覆盖 Tanner 图、变量节点、校验节点、边级消息流、GF(2) syndrome、TS 38.212 §5.4.2.1 rate matching 证据、系统位/校验位/punctured/filler、syndrome 与 CRC 边界、Python syndrome 校验、定点和 RTL/ASIC 映射；审核经理结论 Critical=0、Important=5，已修复边级一轮消息流、puncturing/filler 协议锚点和 LLR 语义、伪代码完整列空间边界；图片检查输出 `IMAGE_OK ... (1600, 1060) RGB`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=195`。 |
| 2026-06-20 | T8.5 LDPC 和积置信传播完成，审核经理 Important 已修复 | 新增 `docs/L2/T8.5_LDPC_sum_product_BP.md`；新增 `tools/figures/render_ldpc_bp_spa_round.py` 和 `docs/L2/assets/T8.5_LDPC_BP_SPA_one_round.png`；覆盖 BP/SPA 含义、VN/CN 消息、外信息原则、LLR 域变量节点/校验节点/后验公式、tanh/atanh 直觉、toy 一轮手算、$q^{(1)}$ 数值闭环、syndrome/CRC/CBG 停止边界、Turbo BCJR 对比、Python toy BP、定点和硬件映射；审核经理结论 Critical=0、Important=2，已修复一轮 VN 更新闭环和 §5.4.2.1 rate recovery 实现推论边界；图片检查输出 `IMAGE_OK ... (1600, 1090) RGB`；正文 Python 输出 `T8.5_TOY_BP_OK`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=196`。 |
| 2026-06-20 | T8.6 LDPC Min-Sum、NMS、OMS 完成，审核经理无 Important | 新增 `docs/L2/T8.6_LDPC_MS_NMS_OMS.md`；新增 `tools/figures/render_ldpc_min_sum_variants.py` 和 `docs/L2/assets/T8.6_LDPC_MS_NMS_OMS_compare.png`；覆盖 SPA 复杂度、Min-Sum 符号/最小幅度近似、min1/min2、NMS、OMS、同输入数值对比、硬件资源取舍、定点策略、RTL/ASIC 映射和失败案例；图片初版存在连线压文字，已修复为先画边后画节点并目检通过；审核经理结论 Critical=0、Important=0，已按 Minor 补并列最小值 tie-break 和来源检查说明；图片检查输出 `IMAGE_OK ... (1600, 1080) RGB`；正文 Python 输出 `T8.6_MIN_SUM_VARIANTS_OK`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=109`。 |
| 2026-06-20 | T8.7 Layered LDPC 译码调度审核经理 Important 修复完成 | `docs/L2/T8.7_layered_LDPC_decoding_schedule.md` 已修复审核经理提出的日志字段、CB CRC 条件性、syndrome 非单调、首现缩写、row order 协议边界、式号和 `<NULL>` 误解风险；`tools/figures/render_ldpc_layered_schedule.py` 已同步底部日志字段为 `bank_conflict_count`、`pipeline_stall_count`，重生成 `docs/L2/assets/T8.7_LDPC_layered_schedule_flow.png` 并目检无裁切、无遮挡、无箭头压字；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=63`。 |
| 2026-06-20 | T8.8 NR LDPC 译码数值走读完成，审核经理 Important 已修复 | 新增 `docs/L2/T8.8_NR_LDPC_decoder_numeric_walkthrough.md`；新增 `tools/figures/render_ldpc_numeric_walkthrough.py` 和 `docs/L2/assets/T8.8_LDPC_numeric_walkthrough.png`；覆盖 toy H、channel LLR、初始 hard decision、初始 syndrome、一轮 Min-Sum CN 消息、VN posterior、更新后 hard decision/syndrome、syndrome early stop 边界、Python 数值校验、定点/RTL/ASIC/验证和常见错误；审核经理结论 Critical=0、Important=3，已修复“列空间”术语、CRC mask 语境、CN 公式 q 消息边界；图片 Minor 已修复，目检无裁切、无遮挡、无拆字；正文 Python 输出 `T8.8_NUMERIC_WALKTHROUGH_OK`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=263`。 |
| 2026-06-20 | T8 模块自动审计通过 | 模块 8 全量审计：`python3 tools/audit_lesson_terms.py docs/L2/T8.*.md` 输出 `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L2/T8.*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L2/T8.*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L2/T8.*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=1149`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 共 165 行，作为候选清单，T8.3 已完整图片化复现 TS 38.212 Table 5.3.2-2/3。 |
| 2026-06-20 | T8 模块总复核通过并更新 Prompt 覆盖矩阵 | 审核经理模块总复核结论：Critical=0、Important=0、Minor=0；确认 T8.1-T8.8 链路连贯、TS 38.212/38.214 边界准确、T8.8 旧问题未扩散；已将 `docs/audits/prompt_coverage_matrix.md` 更新到 46 篇，新增 T8.1-T8.8 覆盖矩阵，并从“未纳入矩阵”中移除 `T8.*`。 |
| 2026-06-20 | T9.1 NR LDPC 速率恢复总览完成，审核经理 Important 已修复 | 新增 `docs/L2/T9.1_NR_LDPC_rate_recovery_overview.md`；新增 `tools/figures/render_nr_ldpc_rate_recovery_overview.py` 和 `docs/L2/assets/T9.1_NR_LDPC_rate_recovery_overview.png`；覆盖接收端 rate recovery 目标、bit deinterleaving、circular buffer restore、RV、limited-buffer rate matching、soft combining、`E/Ncb/N/K` 区分、toy circular buffer 写回/重复/unknown/shortened 例子、伪代码、浮点检查、定点饱和、RTL/ASIC 映射、协议证据和自测答案；审核经理结论 Critical=0、Important=3、Minor=2，已修复图文 toy 语义不一致、执行记录未闭环、协议证据路径不自包含和反交织映射符号歧义；图片输出 `IMAGE_OK ... (1600, 1200) RGB`，目检无裁切、无遮挡、无箭头压字，底部留白充足；正文 Python 输出 `T9.1_RATE_RECOVERY_TOY_OK`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=73`。 |
| 2026-06-20 | T9.2 NR LDPC circular buffer 状态专题完成，审核经理 Important 已修复 | 新增 `docs/L2/T9.2_NR_LDPC_circular_buffer_states.md`；新增 `tools/figures/render_nr_ldpc_circular_buffer_states.py` 和 `docs/L2/assets/T9.2_NR_LDPC_circular_buffer_states.png`；按登记表 T9.2 覆盖 circular buffer、punctured/unknown、shortened/filler、repeated、unknown mask、known mask、repeat accumulation、错误对照、Python 校验、定点饱和和 RTL/ASIC 映射；已在正文说明 roadmap T9.2 与登记表 T9.2/T9.4 的命名错位并按登记表执行；审核经理结论 Critical=0、Important=1、Minor=3，已修复 Python toy 用 LLR 数值推断 prior observation 的问题，改用独立 `old_observed` 集合，并修复常见错误表述歧义、BG/RV/PCH 首现展开和执行记录闭环；图片目检无裁切、无遮挡、无箭头压字；正文 Python 输出 `T9.2_CIRCULAR_BUFFER_STATES_OK`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=43`。 |
| 2026-06-20 | T9.3 NR LDPC HARQ soft buffer、RV k0 与 CBG 部分重传完成，复审剩余问题已修复 | 新增 `docs/L2/T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0.md`；新增 `tools/figures/render_nr_ldpc_harq_cbg_rv.py` 和 `docs/L2/assets/T9.3_NR_LDPC_HARQ_CBG_RV.png`；覆盖 roadmap T9.3 的 NR LDPC RV、`k0`、circular buffer 起点、HARQ soft combining、limited-buffer、toy LLR 放置，并覆盖登记表 T9.3 的 CBG 英文全称/中文含义、TB/CB/CBG 层级、CBGTI/CBGFI、partial retransmission、未重传 CBG 保持、状态字段、定点饱和、失败案例和最小 dump；已修正并复现 TS 38.212 Table 5.4.2.1-2 的 `rvid/BG/k0` 公式形式，包含 $Z_c$ 对齐项，并说明本地 `TS_36.212_36212-j30_content.md`/`table_0016/0017` 抽取限制；审核经理首轮结论 `Critical=1, Important=3, Minor=2`，已修复 `k0` 公式缺 $Z_c$、toy repeat 不自洽、CBGFI 边界遗漏、`held_cbg_count` 统计歧义；复审剩余 `Important=1` 为读图说明旧地址残留，已修正为 RV2 覆盖地址 3-6、addr3 重复；图片目检无裁切、无遮挡、无箭头压字，repeat 由 RV0/RV2 在 addr3 的真实重叠体现；正文 Python 输出 `T9.3_HARQ_CBG_RV_TOY_OK [0, -2, 1, 0] {'new_coverage': 6, 'repeat_coverage': 2, 'held_cbg_count': 1, 'held_cb_count': 2, 'saturation_count': 0}`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=32`。 |
| 2026-06-20 | T9.4 NR LDPC bit deinterleaving 与 LLR 放置完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T9.4_NR_LDPC_bit_deinterleaving.md`；新增 `tools/figures/render_nr_ldpc_bit_deinterleaving.py` 和 `docs/L2/assets/T9.4_NR_LDPC_bit_deinterleaving.png`；按登记表覆盖 TS 38.212 §5.4.2/§5.4.2.2 bit interleaving、`Qm` 对 LLR 排列的影响、demapper symbol-order LLR 到 rate-recovery `e` 顺序的放置、QPSK/16QAM 固定 pattern、permutation address generator、LLR reorder buffer、bank conflict、伪代码、浮点/定点/RTL/验证和常见错误；已修正协议公式与工程接口边界为 `f_{b+sQ_m}=e_{bS+s}`、`L_e[bS+s]=L_f[b+sQ_m]`，避免混淆协议 `f` 顺序和 demapper symbol 顺序；审核经理首轮结论 Critical=0、Important=1、Minor=2，已新增 `docs/audits/T9.4_NR_LDPC_bit_interleaving_formula_evidence.md` 固化 `source.docx`/`document.xml` SHA-256、`sections.jsonl` paragraph_index 684、`document.xml` 段落 8955-8959 和旧式公式对象关系 ID，并已修复图中关键公式字号/拆行和执行记录状态；图片重新目检无裁切、无遮挡、无箭头压字；正文 Python 输出 `T9.4_BIT_DEINTERLEAVING_TOY_OK [10, 20, 30, 40, 11, 21, 31, 41] [100, 200, 300, 101, 201, 301, 102, 202, 302, 103, 203, 303]`；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=121`。 |
| 2026-06-20 | 本轮 NR LDPC 图片脚本整体整改完成并重生成资产 | 已重生成 `T8.1`、`T8.2`、`T8.3`、`T9.1`、`T9.2`、`T9.4`、`T9.6` 相关 PNG；重点扩大表格/说明框字号、行高、内边距与画布宽度，消除 BG 表、circular buffer、rate recovery 的局部拥挤问题；保留少量协议短索引与 `Qm` / `Ncb` / `f_i` / `e_i` 等必要缩写作为例外。 |
| 2026-06-20 | T9.5 NR LDPC 码块重组、CB CRC 与 TB CRC 完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T9.5_NR_LDPC_reassembly_TB_CRC.md`；新增 `tools/figures/render_nr_ldpc_reassembly_tb_crc.py` 和 `docs/L2/assets/T9.5_NR_LDPC_reassembly_TB_CRC.png`；覆盖路线图/登记表要求：译码后 CB 处理、filler 去除、条件性 CB CRC、按协议 CB index 拼接、TB CRC、CBG 部分重传下未更新 CB 使用历史状态、单 CB CRC fail、所有 CB CRC pass 但 TB CRC fail、CBG 状态错误三类失败案例、伪代码、Python toy、RTL/ASIC 映射和验证 dump；协议锚点包括 TS 38.212 §5.2.2/§5.5/§6.2.1/§6.2.3/§6.2.6/§7.2.1/§7.2.3/§7.2.6 以及 TS 38.214 §5.1.7/§6.1.5；图片目检无裁切、无遮挡、无箭头压字；正文 Python 输出 `T9.5_REASSEMBLY_TB_CRC_TOY_OK AAAABBBB AAAABBBBCCCCDDDD`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=5`。 |
| 2026-06-20 | T9.6 NR LDPC 译码边界案例完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T9.6_NR_LDPC_decoder_edge_cases.md`；新增 `tools/figures/render_nr_ldpc_edge_case_diagnosis.py` 和 `docs/L2/assets/T9.6_NR_LDPC_edge_case_diagnosis.png`；覆盖 BG、Zc、filler、punctured systematic bits、limited buffer、RV mismatch、CBG mismatch、LLR saturation、syndrome pass but CRC fail、CRC pass but upper assembly fail、最小 dump 包和 descriptor->rate recovery->LDPC core->CRC 诊断流程；展开 BG、Zc、RV、CBG、syndrome/CRC 五个详细案例，并补直观坐标系、RV 地址错位数值例子和 LLR 饱和理论推导；图片边界检查 `IMAGE_EDGE_CHECK (1600, 1100) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无箭头压字；正文 Python 输出 `T9.6_EDGE_CASE_CLASSIFIER_OK RATE_RECOVERY_OR_RV_MISMATCH`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=47`。 |
| 2026-06-20 | T9 模块自动审计通过并更新 Prompt 覆盖矩阵 | 模块 9 全量审计：`python3 tools/audit_lesson_terms.py docs/L2/T9.*.md` 输出 `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L2/T9.*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L2/T9.*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L2/T9.*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=321`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，作为候选清单，T9.3/T9.4 已记录关键公式人工复核证据；`docs/audits/prompt_coverage_matrix.md` 已更新到 52 篇，新增 T9.6 行并从未纳入列表移除。 |
| 2026-06-20 | T10.1 NR Polar 控制信息接收链路总览完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T10.1_NR_Polar_decoder_chain_overview.md`；新增 `tools/figures/render_nr_polar_decoder_chain_overview.py` 和 `docs/L2/assets/T10.1_NR_Polar_decoder_chain_overview.png`；覆盖 Polar 名称/来源、短控制块动机、TS 38.212 Table 5.3-2 控制信息编码映射、信道极化最小直觉、frozen/information/CRC 位、UCI/DCI 协议分支、接收端逆链路、最小 descriptor、小型 CA-SCL selector 例子、伪代码、浮点/定点/RTL/验证和常见错误；图片边界检查 `IMAGE_EDGE_CHECK (1800, 1240) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无箭头压字；正文 Python 输出 `T10.1_CA_SCL_SELECTOR_OK P1 [1, 0, 0, 1]`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=30`。 |
| 2026-06-20 | T10.2 信道极化、冻结位与信息位完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T10.2_channel_polarization_frozen_bits.md`；新增 `tools/figures/render_nr_polar_channel_polarization.py` 和 `docs/L2/assets/T10.2_NR_Polar_N4_transform_frozen_mask.png`；覆盖信道极化不是物理极化、bit-channel、可靠/不可靠 bit-channel、frozen bit、information bit、information/frozen 互补集合、N=4 生成矩阵和逐列手算、frozen mask 接收端行为、bit-reversal/顺序约定边界、Python 标准库 toy、浮点/定点/RTL/ASIC/验证和常见错误；图片边界检查 `IMAGE_EDGE_CHECK (1600, 1020) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无箭头压字，图中 GF(2) 加法已使用异或符号；正文 Python 输出 `T10.2_POLAR_N4_ENCODE_OK [1, 0, 1, 0]`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=63`。 |
| 2026-06-20 | T10.3 NR Polar 可靠性序列完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T10.3_NR_Polar_reliability_sequence.md`；新增 `tools/figures/render_nr_polar_reliability_sequence.py` 和 `docs/L2/assets/T10.3_TS38.212_Table_5.3.1.2-1_Polar_sequence.png`；覆盖 TS 38.212 Table 5.3.1.2-1 本地核验、1024 项 Polar sequence 图片化复现、可靠性升序和 0-based 索引、按 $q<N$ 筛选 $Q_N$、从末尾选 $K$ 个 information bit、$A/K/CRC$ 边界、N=8/K=4 和 N=16/K=6 数值例子、伪代码、ROM/mask generator 映射、验证和常见错误；图片边界检查 `IMAGE_EDGE_CHECK (1452, 3450) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无拥挤；Python 输出 `T10.3_POLAR_RELIABILITY_MASK_OK [0, 1, 2, 4, 3, 5, 6, 7] ['F', 'F', 'F', 'I', 'F', 'I', 'I', 'I']` 和 `T10.3_POLAR_RELIABILITY_N16_OK [0, 1, 2, 4, 8, 3, 5, 9, 6, 10, 12, 7, 11, 13, 14, 15] [7, 11, 12, 13, 14, 15]`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=104`。 |
| 2026-06-20 | T10.4 Polar SC 译码完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T10.4_Polar_SC_decoding.md`；新增 `tools/figures/render_nr_polar_sc_decoding_tree.py` 和 `docs/L2/assets/T10.4_NR_Polar_SC_N4_tree.png`；覆盖 SC 定义、Polar 树遍历、二比特节点概率模型、$f$ LLR 函数精确式与 min-sum 近似、$g$ LLR 函数、partial sum 定义与回传、frozen/information 判决规则、N=4 全流程手算、伪代码、浮点仿真、定点饱和、RTL/ASIC 迭代控制和存储、验证方法和常见错误；图片边界检查 `IMAGE_EDGE_CHECK (1800, 1260) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无拥挤，箭头未压文字；正文 Python 输出 `T10.4_SC_N4_OK [0, 0, 1, 0] [1, 0, 1, 0]`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=178`。 |
| 2026-06-20 | T10.5 Polar SCL 译码完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T10.5_Polar_SCL_decoding.md`；新增 `tools/figures/render_nr_polar_scl_path_pruning.py` 和 `docs/L2/assets/T10.5_NR_Polar_SCL_N4_L2_paths.png`；覆盖 SCL 相比 SC 的动机、path/PM/list size/split/prune 定义、frozen 不分裂、information 分裂、PM 越小越好约定、LLR-domain PM 精确式和近似式、N=4/L=2 完整路径表、排序剪枝、复杂度/延迟、定点 PM、sorter/path memory/copy network/partial sum memory、验证方法和常见错误；图片边界检查 `IMAGE_EDGE_CHECK (2000, 1280) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无拥挤，箭头和文本框间距正常；正文 Python 输出 `T10.5_SCL_N4_L2_OK [([0, 0, 1, 0], 0.0), ([0, 0, 0, 0], 2.2)]`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=94`。 |
| 2026-06-20 | T10.6 CRC 辅助 SCL 与控制信道可靠性完成，历史记录：后续阶段复核已覆盖 | 新增 `docs/L2/T10.6_CRC_aided_SCL_control_reliability.md`；新增 `tools/figures/render_nr_polar_ca_scl_selector.py` 和 `docs/L2/assets/T10.6_NR_Polar_CA_SCL_final_selector.png`；覆盖 CA-SCL 名称与基本流程、CRC 是路径选择辅助而非替代树译码、受约束 PM 最小化推导、UCI 6/11 bit CRC 与无 CRC 小负载边界、DCI 24 bit CRC/RNTI 边界、最佳 PM 路径 CRC fail 而次优路径 CRC pass 的完整选择表、CRC 误通过风险、list size/低延迟/高可靠取舍、final selector 伪代码、多路径 CRC checker、RNTI checker、final selector、验证方法和常见错误；图片边界检查 `IMAGE_EDGE_CHECK (1900, 1300) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无拥挤，说明框留白正常；正文 Python 输出 `T10.6_CA_SCL_SELECTOR_OK P1 1.3`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=26`。 |
| 2026-06-20 | T10.7 NR Polar 速率恢复完成并修复图形留白问题 | 新增 `docs/L2/T10.7_NR_Polar_rate_recovery.md`；新增 `tools/figures/render_nr_polar_rate_recovery_flow.py` 和 `docs/L2/assets/T10.7_NR_Polar_rate_recovery_flow.png`；覆盖 TS 38.212 §5.4.1、§5.4.1.1、§5.4.1.2、§5.4.1.3、Table 5.4.1.1-1、UCI/DCI 调用边界、sub-block deinterleaving、bit selection reverse、puncturing/shortening/repetition LLR 初始化、coded-bit deinterleaving、N=8/E=10 toy circular buffer、LDPC/LTE Turbo 差异、定点饱和、RTL/ASIC 映射和常见错误；确认 `table_0019.csv/html` 是 Polar sub-block interleaver pattern，`table_0013` 是 LDPC lifting size set；用户指出图中“LLR 初始化规则”文字框离下边界过近后，已修复脚本画布、说明框高度、行距和下方表格位置，并把文本框内边距/模块间距检查写入全局规则；图片边界检查 `IMAGE_EDGE_CHECK (2000, 1450) bottom_nonwhite 0 right_nonwhite 0`，目检说明框内边距和下方表格间距正常；正文 Python 输出 `T10.7_POLAR_RATE_RECOVERY_TOY_OK [0.0, 0.0, 1.2, 31.0, -0.7, 2.0, -1.5, 1.4]`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=54`。 |
| 2026-06-20 | T10.2 图形节点、文字居中和连线端点复修 | 用户指出 `docs/L2/assets/T10.2_NR_Polar_N4_transform_frozen_mask.png` 中 `u0=0` 等节点框过小、文字上下不居中，后续又指出节点变更后连线和箭头端点不协调；已修复 `tools/figures/render_nr_polar_channel_polarization.py`：固定半径圆节点改为文字尺寸自适应圆角胶囊，使用 `anchor=\"mm\"` 视觉居中，`node()` 返回真实 bbox，连线从输入节点真实右边界到 XOR 真实左边界，箭头从 XOR 真实右边界到输出节点真实左边界；图片重新生成，边界检查 `IMAGE_EDGE_CHECK (1600, 1020) bottom_nonwhite 0 right_nonwhite 0`；全图目检确认节点尺寸、文字上下居中、连线端点、箭头方向、公式区和底部说明区协调。相关防复发规则已写入 `合规与遵从.md` 和 roadmap。 |
| 2026-06-20 | T10.8 NR Polar 边界案例完成 | 新增 `docs/L2/T10.8_NR_Polar_decoder_edge_cases.md`；新增 `tools/figures/render_nr_polar_edge_case_diagnosis.py` 和 `docs/L2/assets/T10.8_NR_Polar_edge_case_diagnosis.png`；覆盖无 CRC 小负载、CRC 长度选择、list size 耗尽、PM 并列、puncturing/shortening mismatch、frozen mask 错误、UCI/DCI descriptor 不匹配、RNTI/CRC 边界，每个案例列触发条件、现象、必查字段、定位步骤和修复方向；展开 frozen mask 数值例子和 PM 最优路径 CRC fail 但次优路径通过数值例子；给最小 dump 包和 descriptor -> rate recovery -> mask -> SC/SCL -> CRC/RNTI selector 诊断流程；图片边界检查 `IMAGE_EDGE_CHECK (1900, 1340) bottom_nonwhite 0 right_nonwhite 0`，目检无裁切、无遮挡、无箭头压字，文本框内边距、说明框底部留白和模块间距正常；正文 Python 输出 `T10.8_POLAR_EDGE_CLASSIFIER_OK DCI_CRC_LENGTH_ERROR`；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=32`。 |
| 2026-06-20 | T10 模块自动审计通过并更新 Prompt 覆盖矩阵 | 模块 10 全量审计：`python3 tools/audit_lesson_terms.py docs/L2/T10.*.md` 输出 `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L2/T10.*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L2/T10.*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L2/T10.*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=581`；`python3 tools/audit_reference_rebuilds.py docs/L2/T10.*.md` 输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单，T10.3 已完整图片化复现 TS 38.212 Table 5.3.1.2-1，T10.7 已复现 TS 38.212 Table 5.4.1.1-1；T10 图片全量边界检查通过，T10.2/T10.7/T10.8 已按新增视觉规则复修或复检；`docs/audits/prompt_coverage_matrix.md` 已更新到 60 篇，新增 T10.8 行并从未纳入列表移除。审核经理复核仍待工具/复核结果返回，未伪造完成状态。 |
| 2026-06-20 | 全局审视快照：L1/L2 自动审计和图像边界检查（历史快照，已被后续记录覆盖） | 当时范围为 `docs/L1/T*.md` 24 篇、`docs/L2/T*.md` 36 篇，T11 尚未完成；当时全量 LaTeX 为 `LATEX_RENDER_AUDIT_OK formulas=4810`。该记录保留为历史执行轨迹，当前状态以阶段 4B/后续最新记录为准：L1 27 篇、L2 41 篇、T6.4 资产证据链已关闭、TS 38.214 MCS/TBS 表值已重分类为 L3 条件项。 |
| 2026-06-20 | 全局图形连线规则加严并应用到 T11.1 | 用户指出 `T11.1_Turbo_LDPC_Polar_algorithm_comparison.png` 中连线/箭头不能机械从右侧连接、不能进入框内、不能超过框边缘，要求端点正好在框边缘。已同步写入 `合规与遵从.md` 和 `2026-06-19-lte-nr-decoding-learning-roadmap.md`：Python 图的连线端点必须精确落在节点/文本框边缘，不能在框内、越过框边缘或靠遮罩掩盖穿框线；带箭头连线的线身应在箭头头部之前停止，箭头尖端精确到达目标边缘。已修复 `tools/figures/render_turbo_ldpc_polar_algorithm_comparison.py`，使用 `boundary_point()` 按节点真实边界取端点，重新生成 `docs/L2/assets/T11.1_Turbo_LDPC_Polar_algorithm_comparison.png`；边界检查 `IMAGE_EDGE_CHECK (1900, 1340) {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}`；目检确认不再统一右侧连接，连线和箭头端点按节点几何关系连接到边缘。 |
| 2026-06-20 | T11.1 Turbo、LDPC、Polar 算法对比完成 | 新增 `docs/L2/T11.1_Turbo_LDPC_Polar_algorithm_comparison.md`；新增/修复 `tools/figures/render_turbo_ldpc_polar_algorithm_comparison.py` 和 `docs/L2/assets/T11.1_Turbo_LDPC_Polar_algorithm_comparison.png`；覆盖路线图/登记表要求：三类码名称、基本思想、接收端对象，LTE Turbo、NR LDPC、NR Polar 协议使用位置，trellis/Tanner graph/decoding tree 图模型，SISO/message passing/SC-SCL 行为，软信息语义、停止条件、复杂度、数据/控制适配性、工程取舍矩阵、同一组 LLR 的三种消费方式、descriptor、验证方法和常见错误。正文复现 TS 36.212 Table 5.1.3-1/2 和 TS 38.212 Table 5.3-1/2 的本节使用子集；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=22`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单；`docs/audits/prompt_coverage_matrix.md` 已新增 T11.1 行并将未纳入列表从 `T11.*` 改为 T11.2-T11.5。 |
| 2026-06-20 | T11.2 LTE/NR 速率匹配与速率恢复对比完成并加严全项目图像字号/间距要求 | 新增 `docs/L2/T11.2_LTE_NR_rate_matching_comparison.md`；新增并多轮修复 `tools/figures/render_lte_nr_rate_matching_comparison.py` 和 `docs/L2/assets/T11.2_LTE_NR_rate_matching_comparison.png`；覆盖 LTE Turbo、NR LDPC、NR Polar 的发送端 rate matching 与接收端 rate recovery 逆向关系、circular buffer、sub-block interleaving、bit interleaving、puncturing、shortening、repetition、RV、LLR 放回、统一对象模型、小型循环缓存例子、典型错误、验证 checklist、定点饱和和 RTL/ASIC 映射。正文复现 TS 36.212 Table 5.1.4-1 和 TS 38.212 Table 5.4.1.1-1；TS 38.212 Table 5.4.2.1-2 `k0` 当前表格抽取为空，正文明确不使用具体值并记录关闭条件。用户指出图中循环缓存例子遮挡、表格字体偏小、表格离上方框图过近后，脚本新增标题到节点最小 36px 间距断言、流程框到表格最小 80px 间距断言，放大表格字号并增加列宽/行高/画布高度；最新图片边界检查 `IMAGE_EDGE_CHECK (1900, 2980) {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}`，目检无裁切、无遮挡、无箭头压字，表格可读。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=71`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单；`docs/audits/prompt_coverage_matrix.md` 已新增 T11.2 行并从未纳入列表移除。已把全项目 Python 图片表格字号和局部几何间距审计加入阶段 4 剩余 Important 项。 |
| 2026-06-20 | T11.3 LTE/NR HARQ 与软缓存对比完成 | 新增 `docs/L2/T11.3_HARQ_soft_buffer_comparison.md`；新增并修复 `tools/figures/render_harq_soft_buffer_comparison.py` 和 `docs/L2/assets/T11.3_HARQ_soft_buffer_comparison.png`；覆盖 LTE/NR HARQ soft buffer 共同抽象、RV 含义、NR CBG partial retransmission、CBGTI/CBGFI、soft buffer 是译码器状态、两套生命周期、LTE RV0/RV2 地址/LLR 累加例子、NR CBG 部分重传例子、descriptor 对比、定点饱和、RTL/ASIC 映射、最小 dump 包和负测试。协议证据包括 TS 36.212 §5.1.4.1.2、TS 36.213 §8.3/§8.6、TS 36.321 §5.3.2、TS 38.212 §5.4.2.1、TS 38.214 §5.1.7/§6.1.5、TS 38.321 §5.3.2；TS 38.212 Table 5.4.2.1-2 具体 `k0` 表值不在本节使用并已写明边界。用户要求图片文本框和表格文字居中后，脚本已统一节点、说明框、例子框、底部说明框和表格单元格内文字水平/垂直居中，并把“全项目图片也按此标准审计”写入全局规则和阶段 4 Important 项；图片边界检查 `IMAGE_EDGE_CHECK (1900, 3040) {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}`，目检无裁切、无遮挡、无箭头压字，文本框和表格文字居中。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=13`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单；`docs/audits/prompt_coverage_matrix.md` 已新增 T11.3 行并从未纳入列表移除。 |
| 2026-06-20 | T11.4 Turbo、LDPC、Polar 硬件架构取舍对比完成 | 新增 `docs/L2/T11.4_decoder_hardware_tradeoff_comparison.md`；新增 `tools/figures/render_decoder_hardware_tradeoff_comparison.py` 和 `docs/L2/assets/T11.4_decoder_hardware_tradeoff_comparison.png`；覆盖 Turbo SISO/BCJR、alpha/beta memory、interleaver/deinterleaver、extrinsic RAM、iteration controller，LDPC layered controller、CN/VN update、message memory、LLR RAM、bank conflict，Polar SC/SCL tree、LLR memory、partial sum、path memory、sorter、CRC checker；补充三类依赖形状、工程决策矩阵、共享/不可共享模块、教学级周期估算、定点策略、RTL/ASIC 映射、验证 dump 和常见错误。图片边界检查 `IMAGE_EDGE_CHECK (1900, 3340) {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}`，目检文本框和表格单元格水平/垂直居中、箭头端点贴合节点边界、表格字号可读、区块间距无接触。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=55`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单；`docs/audits/prompt_coverage_matrix.md` 已新增 T11.4 行并从未纳入列表移除。 |
| 2026-06-20 | T11.5 按信道和信息类型选择译码器完成 | 新增 `docs/L2/T11.5_decoder_selection_by_channel_type.md`；新增 `tools/figures/render_decoder_selection_by_channel_type.py` 和 `docs/L2/assets/T11.5_decoder_selection_by_channel_type.png`；覆盖 LTE DL-SCH/UL-SCH 到 Turbo、LTE 控制到 TBCC/block/repetition、NR DL-SCH/UL-SCH/PCH 到 LDPC、NR DCI 到 Polar、NR UCI 到 small-block/Polar、PBCH 边界、UCI on PUSCH、DCI CRC/RNTI、NR CBG、selector 伪代码、descriptor 字段、四个 descriptor 分类走读、配置错误案例和验证方法。图片边界检查 `IMAGE_EDGE_CHECK (1900, 2200) {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}`，目检表格单元格、节点、说明框文字水平/垂直居中，箭头端点贴合节点边界，表格字号可读，底部说明框留白充足。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=0`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单；`docs/audits/prompt_coverage_matrix.md` 已新增 T11.5 行并从未纳入列表移除。 |
| 2026-06-20 | 模块 11 自动审计通过 | 模块 11 全量审计：`python3 tools/audit_lesson_terms.py docs/L2/T11.*.md` 输出 `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L2/T11.*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L2/T11.*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L2/T11.*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=161`；`python3 tools/audit_reference_rebuilds.py docs/L2/T11.*.md` 输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单。T11 图片脚本全量重生成成功，统一边界检查覆盖 `T11.1` 到 `T11.5` 五张 PNG，top/bottom/left/right 非白边界计数均为 0；T11.5 已目检表格和文本框文字水平/垂直居中。 |
| 2026-06-20 | T6.3/T7.5/T8.4/T8.5/T8.6/T3.3 图片可读性整改完成 | 本轮仅整改负责的 6 张图：`tools/figures/render_lte_dl_ul_decoder_context.py`、`tools/figures/render_lte_turbo_encoder_structure.py`、`tools/figures/render_lte_turbo_interleaver_table.py`、`tools/figures/render_ldpc_tanner_syndrome.py`、`tools/figures/render_ldpc_bp_spa_round.py`、`tools/figures/render_ldpc_min_sum_variants.py`；对应重生成 `docs/L2/assets/T7.5_LTE_DL_UL_decoder_context.png`、`docs/L2/assets/T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png`、`docs/L1/assets/T3.3_TS36.212_Table_5.1.3-3.png`、`docs/L2/assets/T8.4_LDPC_Tanner_syndrome_toy.png`、`docs/L2/assets/T8.5_LDPC_BP_SPA_one_round.png`、`docs/L2/assets/T8.6_LDPC_MS_NMS_OMS_compare.png`。六张图均已运行 `python3 tools/audit_figure_geometry.py <script>` 与 `python3 tools/audit_figure_readability.py <script>`，结果全部为 `FIGURE_GEOMETRY_AUDIT_OK` / `FIGURE_READABILITY_AUDIT_OK`；PIL 局部检查确认标题区、表格区、说明框和底部区域无裁切，尺寸分别为 `(1920, 1540)`、`(2040, 1540)`、`(2360, 1980)`、`(1600, 1105)`、`(1600, 1125)`、`(1600, 1125)`。`T3.3` 已改为 2x2 分面长图，正文/表头/首列维持 20px+，左上角 `i` 仅作索引字段；`T6.3`、`T7.5`、`T8.4`、`T8.5`、`T8.6` 的说明框、表格和节点文字也已统一抬升到 20px+。 |
| 2026-06-20 | 阶段 9 L2 审核经理复核完成，Critical=0、Important=3（初审快照，后续已关闭/重分类） | 审核经理复核确认 `docs/audits/L2_overall_review.md` 覆盖 T6-T11 共 41 篇，`docs/audits/prompt_coverage_matrix.md` 覆盖 L2 41 篇且无差集；自动审计可复现：术语、标题、深度均 OK，L2 LaTeX 最新 `LATEX_RENDER_AUDIT_OK formulas=3241`，引用重建候选 544 行。后续已关闭 T6.4 资产证据链和 T9/T10/T11 复核状态问题，并把 TS 38.214 MCS/TBS 表值重分类为 L3/system bit-exact 条件项；图片局部视觉审计作为持续控制保留。 |
| 2026-06-20 | 历史记录：阶段 10 最终交付状态总表初版生成 | 当时新增 `docs/audits/final_delivery_status.md`，汇总 L1/L2 完成范围、自动审计结果、Prompt 覆盖状态、图片资产状态、协议表/图/公式复现状态、未关闭待核验清单、L3 前准备清单和后续小节。当时全项目审计：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=5105`；引用重建候选 `reference_rebuild_candidates_full.txt` 更新为 1020 行。该记录为 L1/L2 阶段历史快照，当前最新状态以 2026-06-21 最终同步记录为准。 |
| 2026-06-20 | 阶段 10 图片资产清单生成（历史快照） | 当时新增 `docs/audits/image_asset_inventory.md`，列出早期图片资产和 Python 绘图脚本、输入证据、使用讲义、当前状态和历史视觉风险。该记录为历史快照，已被后续 46 张 PNG、42 个脚本和 24px/56px 二次加严记录覆盖；持续控制原则不变，不能因一次边界检查通过而永久关闭。 |
| 2026-06-20 | 阶段 10 回归命令草案生成 | 新增 `docs/audits/regression_command_plan.md`，汇总文档审计、图片回归、L3 golden model、定点 bit-exact、RTL 对比和可执行 Python 片段归档策略。当前已完成讲义级执行记录和关键 toy 输出记录；进入 L3 前需把正文片段抽取为统一测试套件，不能提前声明 CI 已覆盖所有正文片段。 |
| 2026-06-20 | 历史记录：阶段 10 最终收尾状态更新并完成 fresh 审计 | 当时已更新 `docs/audits/lte_nr_decoding_remaining_work_register.md`、`final_delivery_status.md`、`L2_overall_review.md`、`global_compliance_review.md`、`full_project_document_review.md`、`reference_rebuild_candidates_review.md`、`regression_command_plan.md`；关闭 T6.4 Table 5.1.3-3 资产证据链，重分类 TS 38.214 MCS/TBS 表值为 L3 条件项，明确图片局部视觉审计为持续控制。当时 fresh 审计：`MARKDOWN_HEADING_AUDIT_OK`；`LESSON_TERM_AUDIT_OK`；`LESSON_DEPTH_AUDIT_OK`；全项目 `LATEX_RENDER_AUDIT_OK formulas=5105`；L2 `LATEX_RENDER_AUDIT_OK formulas=3241`。该记录为 L1/L2 阶段历史快照，最新全项目 LaTeX 公式数以 2026-06-21 depth backlog 收尾记录的分段合计 `6428` 为准。 |
| 2026-06-20 | 历史复核状态口径回写 | 完成记录中早期 `T9.4`、`T9.5`、`T9.6`、`T10.1`-`T10.6`、`T10.8` 等条目已改为“历史记录：后续阶段复核已覆盖”；当前以阶段 9 L2 总体审核经理复核和阶段 10 最终交付状态为准：L2 T6-T11 共 41 篇已完成总体审查，Critical=0，T6.4 资产证据链已关闭，T9/T10/T11 复核状态问题已关闭，TS 38.214 MCS/TBS 表值重分类为 L3/system bit-exact 条件项。 |
| 2026-06-20 | 图片局部视觉几何审计工具化入口新增 | 新增 `tools/audit_figure_geometry.py` 和 `tests/test_audit_figure_geometry.py`；新增 `docs/audits/python_figure_visual_geometry_checklist.md`；更新 `docs/audits/regression_command_plan.md` 和 `docs/audits/image_asset_inventory.md`。验证：`python3 -m unittest tests/test_audit_figure_geometry.py` 通过。初次 `python3 tools/audit_figure_geometry.py --focus-only tools/figures` 曾暴露 T10.7、T11.1、T10.2 的脚本级风险；已修复 T10.7 表格/说明框居中与边界箭头、T11.1 比较矩阵居中和矩阵到说明框间距、T10.2 底部/局部间距断言。当前重点图范围输出 `FIGURE_GEOMETRY_AUDIT_OK`；三张重生成图片边界检查均为 0。 |
| 2026-06-20 | 阶段 4B L1 T4.4-T4.6 补齐并通过审计 | 新增并完善 `docs/L1/T4.4_early_stopping_crc_gated_control.md`、`docs/L1/T4.5_decoder_performance_metrics.md`、`docs/L1/T4.6_decoder_interface_contracts.md`；T4.4 审核经理 Important 已修复：补 `candidate_valid`、CRC latency、pipeline flush、commit/flush 条件和协议证据表本地路径；T4.6 审核经理 Important 已修复：补 `llr_sign_convention` 合法性检查和 RV 作为完整 soft buffer 访问事务上下文。单篇审计：T4.4 `LATEX_RENDER_AUDIT_OK formulas=21`，T4.5 `LATEX_RENDER_AUDIT_OK formulas=87`，T4.6 `LATEX_RENDER_AUDIT_OK formulas=26`，三篇术语/标题/深度均 OK，引用重建审计均为候选清单且退出码 0。L1 全量审计：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=1864`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单。L1 状态更新为 27 篇，下一断点为 L3 T12-T15。 |
| 2026-06-20 | T12.1 Python Golden Model 工程布局完成 | 新增 `docs/L3/T12.1_python_golden_model_project_layout.md`；新增 `tools/figures/render_t12_1_golden_model_layout.py` 和 `docs/L3/assets/T12.1_golden_model_project_layout.png`；覆盖包结构、配置文件、向量文件、随机种子、日志字段、失败重跑、结果归档、协议向量来源、T13/T14/T15 承接和小型失败帧证据链例子。图形初版底部说明框留白不足，已按全局视觉规则修复并重生成；`python3 tools/audit_figure_geometry.py --focus-only tools/figures` 输出 `FIGURE_GEOMETRY_AUDIT_OK`，已目检文本框、箭头端点、底部说明框和缩放观感。只读审核指出 seed 派生、vector schema、NR CRC 回链、协议证据粒度和 scaffold 验证口径问题后，已补 `canonical_json_sha256_u64le_v1`、数组 dtype/shape/hash、`vector.json` 最小 schema、NR LDPC/Polar CRC 回链、表/图/公式证据粒度边界和 scaffold 验收记录；复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=4`；引用重建审计输出候选清单，候选为本节声明不重建的协议公式边界。 |
| 2026-06-20 | T12.2 LTE Turbo 浮点仿真计划完成，审核 Important 已修复 | 新增 `docs/L3/T12.2_LTE_Turbo_float_sim_plan.md`；新增并修复 `tools/figures/render_t12_2_lte_turbo_float_sim_flow.py` 和 `docs/L3/assets/T12.2_LTE_Turbo_float_sim_flow.png`。正文覆盖编码器参考、AWGN 信道、BPSK/QPSK LLR、解速率匹配、HARQ 软合并、Log-MAP/Max-Log-MAP、CRC 检查、BLER/BER 曲线、随机种子、输出 CSV/JSONL、阈值、命令模板、失败 replay、定点化承接、RTL/ASIC 映射、验证和常见错误；协议证据锚定 TS 36.212 §5.1.1-§5.1.4.1，TS 36.213 MCS/TBS 保留 `待核验`。图形初版被指出底部说明贴边、表格第一列越界风险和箭头端点不严格，已改成长画布、边界箭头、列宽驱动表格和 bbox-based 居中说明框；审核子代理指出原图形审计命令未覆盖 T12.2 后，已改为 `python3 tools/audit_figure_geometry.py tools/figures/render_t12_2_lte_turbo_float_sim_flow.py` 并输出 `FIGURE_GEOMETRY_AUDIT_OK`，目检底部 `Engineering Checks`、表格单元格、节点文字水平/垂直居中、箭头端点和缩放阅读效果。审核子代理还指出 AWGN 码率口径和协议 manifest/3GPP_译码知识库入口 核验缺口，已补 `R_eff=A_payload/sum(E_r)` 默认口径、`rate_definition/R_eff/sum_E/Qm/energy_normalization` 落盘字段、命令模板和伪代码，并补 `manifest.csv`、`processed/manifest.json`、TS 36.212 3GPP_译码知识库入口 核验结果。复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=91`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选来自 TS 36.213 `待核验`、上游已重建表/图回链和正文公式引用。 |
| 2026-06-20 | T12.3 NR LDPC 浮点仿真计划完成，审核 Important 已修复 | 新增并完善 `docs/L3/T12.3_NR_LDPC_float_sim_plan.md`；新增 `tools/figures/render_t12_3_nr_ldpc_float_sim_flow.py` 和 `docs/L3/assets/T12.3_NR_LDPC_float_sim_flow.png`。正文覆盖 BG 选择、$Z_c$、lifting set、$H$ 身份、rate matching/recovery、RV/$k_0$、limited buffer、BP/SPA/MS/NMS/OMS、AWGN 有效码率、CRC、BLER/BER、随机种子、输出 CSV/JSONL、失败 replay、定点承接、RTL/ASIC 映射、验证和常见错误；协议证据锚定 TS 38.212 §5.2.2/§5.3.2/§5.4.2/§6.2/§7.2 和 TS 38.214 §5.1.3/§6.1.4，并记录 `manifest.csv`、`processed/manifest.json`、TS 38.212/38.214 3GPP_译码知识库入口 核验结果。图片直接审计 `python3 tools/audit_figure_geometry.py tools/figures/render_t12_3_nr_ldpc_float_sim_flow.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`，目检底部说明、实验矩阵、节点文字居中、箭头端点和缩放观感无贴边或遮挡。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=104`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选来自 PCH/MCS/TBS 边界、上游已重建表格回链和正文公式引用。只读审核子代理首轮 `Critical=0, Important=4`，已补 BP/SPA 符号解释与 SPA 全称、BP/MS/NMS/OMS 可执行命令矩阵、CBG/CBGTI/CBGFI 精确本地锚点和未复现协议资产关闭条件；复审 `Critical=0, Important=0`，Minor 短路径也已展开。 |
| 2026-06-20 | T12.4 NR Polar 浮点仿真计划完成并修复审核问题 | 新增 `docs/L3/T12.4_NR_Polar_float_sim_plan.md`；新增并使用 `tools/figures/render_t12_4_nr_polar_float_sim_flow.py` 和 `docs/L3/assets/T12.4_NR_Polar_float_sim_flow.png`。正文覆盖可靠性序列、information/frozen/PC set、rate recovery、puncturing/shortening/repetition、SC/SCL/CA-SCL、list-size sweep、CRC/RNTI final selector、具体数值例子、AWGN 有效码率、随机种子、输出 CSV/JSONL、失败 replay、延迟代理指标、定点承接、RTL/ASIC 映射、验证和常见错误；协议证据锚定 TS 38.212 §5.1/§5.2.1/§5.3.1/§5.4.1/§6.3/§7.3，并记录 `manifest.csv`、`processed/manifest.json`、TS 38.212 3GPP_译码知识库入口 核验结果。图片直接审计 `python3 tools/audit_figure_geometry.py tools/figures/render_t12_4_nr_polar_float_sim_flow.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`，已目检表格文字居中、底部 `Engineering Checks` 留白、箭头端点和整体缩放观感。审核经理 Popper 首轮 `Critical=0, Important=2, Minor=2`，已修复阈值可执行例子、缩写首现和 SC/SCL/CA-SCL 二维命令矩阵；单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=94`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选来自上游已重建协议表、PDCCH blind detection/UCI payload field 边界和正文工程公式引用，正文已在“未复现协议资产与关闭条件”中逐项说明。 |
| 2026-06-20 | T12.5 BER/BLER 曲线报告规范完成并修复审核问题 | 新增并完善 `docs/L3/T12.5_BER_BLER_curve_reporting.md`；新增 `tools/figures/render_t12_5_ber_bler_curve_reporting.py` 和 `docs/L3/assets/T12.5_BER_BLER_curve_reporting.png`。正文覆盖 BER、TB BLER、CB BLER、control BLER、FER、false-pass、Wilson 置信区间、零错误上界、最小帧数、最小错误数、早停、统一 `metrics.csv` schema、CSV/PNG/PDF/report.json 命名、曲线解读、失败诊断、接收端报告流程、定点承接和 RTL/ASIC 映射。审核经理 Hegel 首轮 `Critical=0, Important=3, Minor=3`，已修复：为 BER/TB BLER/CB BLER/control BLER/FER/false-pass 分别给出 CI 与 95% upper-bound 字段；命令模板拆分为 LTE/NR 数据链路 `tb_bler`、NR Polar `control_bler`、NR Polar DCI `false_pass_rate`；补 TS 38.212 §6.3.1/§6.3.2 UCI on PUCCH/PUSCH Polar CRC/channel coding/rate matching 锚点；修正 `tb_fail_count` 和通用 target CI 字段命名。Copernicus 复核 `Critical=0, Important=3, Minor=3`，已修复 bundle 示例旧路径、`target_*` 诊断别名 schema、PUSCH UCI 锚点范围、false-pass 分母归属、前置术语首现和重复“上”字。图片直接审计输出 `FIGURE_GEOMETRY_AUDIT_OK`，单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=42`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选均在正文边界表中说明。 |
| 2026-06-20 | 模块 12 自动审计和复核关闭 | 模块 12 全量审计：`python3 tools/audit_lesson_terms.py docs/L3/T12*.md` 输出 `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L3/T12*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L3/T12*.md` 输出 `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L3/T12*.md` 输出 `LATEX_RENDER_AUDIT_OK formulas=335`；`python3 tools/audit_reference_rebuilds.py docs/L3/T12*.md` 输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES` 作为候选清单。T12 图形脚本几何审计 `python3 tools/audit_figure_geometry.py tools/figures/render_t12_1_python_golden_model_project_layout.py tools/figures/render_t12_2_lte_turbo_float_sim_plan.py tools/figures/render_t12_3_nr_ldpc_float_sim_plan.py tools/figures/render_t12_4_nr_polar_float_sim_plan.py tools/figures/render_t12_5_ber_bler_curve_reporting.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`；`python3 -m unittest tests/test_audit_figure_geometry.py` 输出 `Ran 3 tests ... OK`。审核经理复核 Critical/Important 均已关闭，模块 12 可进入模块 13。 |
| 2026-06-20 | T13.1 定点译码器需求完成 | 新增 `docs/L3/T13.1_fixed_point_decoder_requirements.md`；新增 `tools/figures/render_t13_1_fixed_point_requirements.py` 和 `docs/L3/assets/T13.1_fixed_point_decoder_requirements.png`。正文覆盖 LLR 位宽、内部消息位宽、Q 格式、裁剪、缩放、舍入、饱和、符号扩展、性能损失预算、bit-exact 检查点、fixed-point requirement 模板、三类译码器位宽对象、RTL/ASIC 映射、验证方法和自测答案；明确 3GPP 不规定内部定点位宽，协议字段只作为 descriptor 和向量来源。正文 toy 片段输出 `T13.1_FIXED_REQUIREMENT_TOY_OK`；图片几何审计输出 `FIGURE_GEOMETRY_AUDIT_OK`，目检表格文字居中、箭头端点贴合节点边界、底部说明框留白充足。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=34`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_NO_CANDIDATES`。 |
| 2026-06-20 | T13.1 审核反馈修复 | 审核经理 Carson 复核 `Critical=0, Important=2, Minor=2`；已修复：公共 requirement 模板新增 `turbo.*`、`ldpc.*`、`polar.*`、`simd_memory.*`、`regression.*` namespace 和 T13.2-T13.6 字段挂载点；执行记录区分“文档级验证闭环”和“边界整数/符号扩展/Python-vs-C/C++ bit-exact/fixed-vs-float 曲线预算”等后续模型级验证；图中 Q 格式范围改为 raw two's-complement range 与 symmetric example range 区分；台账依据修正为模块 13。修复后复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=34`、`REFERENCE_REBUILD_AUDIT_NO_CANDIDATES`、`FIGURE_GEOMETRY_AUDIT_OK`；图片重新目检通过。 |
| 2026-06-20 | T13.2 LTE Turbo 定点模型计划完成 | 新增并完善 `docs/L3/T13.2_LTE_Turbo_fixed_point_model_plan.md`；新增 `tools/figures/render_t13_2_lte_turbo_fixed_point_model.py` 和 `docs/L3/assets/T13.2_LTE_Turbo_fixed_point_model.png`。正文覆盖 Turbo 定点理论底座、分支度量、alpha/beta 归一化、Log-MAP/Max-Log-MAP/LUT/scaled mode、外信息缩放、内部交织器二次置换公式和 `pi/depi` 约定、$D=K+4$ 与 tail bits 边界、C/C++ descriptor/config/buffer/trace 结构体、数组布局、bit-exact 命令模板、性能预算、RTL/ASIC 映射、验证方法和自测答案。审核经理 Ohm 复核 `Critical=0, Important=6, Minor=3`，已修复 `branch_metric_sat_count`、`TurboFixedConfig` bit-exact 字段、交织器公式/方向、`K+tail` 含糊长度、TS 36.212 rate matching 与接收端 soft buffer 实现策略边界、执行记录闭环、缩写首现和图形圆角。图片几何审计输出 `FIGURE_GEOMETRY_AUDIT_OK`，目检字号可读、表格文字居中、箭头贴边、底部说明留白充足。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=57`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已重建表/图/关系式回链、论文引用和 TS 36.213 MCS/TBS 条件项。 |
| 2026-06-20 | T13.3 NR LDPC 定点模型计划完成并修复图表字号问题 | 新增并完善 `docs/L3/T13.3_NR_LDPC_fixed_point_model_plan.md`；新增并重生成 `tools/figures/render_t13_3_nr_ldpc_fixed_point_model.py` 和 `docs/L3/assets/T13.3_NR_LDPC_fixed_point_model.png`。正文覆盖 LLR/消息位宽、CN min1/min2、符号排除目标边、NMS/OMS 定点参数、layered read-modify-write、C/C++ descriptor/config/buffer/trace、数组布局、bit-exact 命令模板、NMS/OMS BLER 损失比较、RTL/ASIC 映射、验证方法和自测答案。用户指出项目图片表格字体偏小后，已将全局规则写入 `合规与遵从.md` 和本台账，新增 `tools/audit_figure_readability.py`，并把 T13.3 图内表格字号从 17/18 提升到 21/22 级，重生成后目检表格字号可读、文字水平/垂直居中、箭头端点贴边、底部说明留白充足。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=55`、`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已重建 TS 38.212 表格回链、实现策略边界、论文引用和 TS 38.214 MCS/TBS 条件项。全项目 `python3 tools/audit_figure_readability.py tools/figures` 已输出表格字号/行高风险 findings，作为后续全项目图片整改队列，不按 T13.3 单篇失败处理。 |
| 2026-06-20 | T13.3 审核经理复核关闭，T13.1/T13.2 图片可读性补救 | 审核经理 Planck 只读复核 T13.3：`Critical=0, Important=0, Minor=2`。已修复 Minor：命令模板显式加入 `--decoder-variant nms`、`--variant-sweep ms,nms,oms` 和 `decoder_golden.reporting.fixed_loss` 报告产物，覆盖 `syndrome_stop_rate/cb_crc_pass_rate/tb_crc_pass_rate/bler/fixed_loss_db/sat_count_*`；修正 `layer/poterior/syndrome` 为 `layer/posterior/syndrome`。复审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=55`、`REFERENCE_REBUILD_AUDIT_CANDIDATES`、`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`。新可读性审计同时指出 T13.1/T13.2 图存在 17px 表格字号风险，已将 `tools/figures/render_t13_1_fixed_point_requirements.py` 和 `tools/figures/render_t13_2_lte_turbo_fixed_point_model.py` 字号提升到与 T13.3 同级，重生成 `docs/L3/assets/T13.1_fixed_point_decoder_requirements.png`、`docs/L3/assets/T13.2_LTE_Turbo_fixed_point_model.png`；三张 T13 图统一通过几何与可读性审计，且 T13.1/T13.2 已目检表格字号可读、文字居中、箭头端点贴边、底部留白正常。 |
| 2026-06-20 | T13.4 NR Polar 定点模型计划完成并关闭审核 Minor | 新增并完善 `docs/L3/T13.4_NR_Polar_fixed_point_model_plan.md`；新增并重生成 `tools/figures/render_t13_4_nr_polar_fixed_point_model.py` 和 `docs/L3/assets/T13.4_NR_Polar_fixed_point_model.png`。正文覆盖 Polar 定点理论底座、$f/g$ 定点化、partial sum 与 path state、PM 饱和和稳定 tie-break、`2L -> L` sorter、CRC/RNTI final selector、C/C++ descriptor/config/buffer/trace、bit-exact 命令模板、RTL/ASIC 映射、验证方法和自测答案。自动审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=83`、`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；引用重建审计输出候选项，正文已说明上游已复现 TS 38.212 表格回链和实现策略边界。审核经理 Chandrasekhar 只读复核 `Critical=0, Important=0, Minor=1`，已修复：`list_size/L` 从 protocol vector/descriptor 侧移到 fixed config/test harness 侧，图中明确 `L belongs to fixed config`，避免把 list size 误读成 3GPP 协议参数。`docs/audits/prompt_coverage_matrix.md` 已新增 T13.4 行并从未纳入列表移除。 |
| 2026-06-20 | 阶段 4C 首批图片可读性整改：T8.7 layered schedule 图 | 用户指出整个项目存在图片表格字体偏小问题后，已按 20px 表格/说明文字下限和 48px 行高下限加严 `tools/audit_figure_readability.py`。首批修复 `tools/figures/render_ldpc_layered_schedule.py`：画布从 `(1600, 1100)` 扩为 `(1920, 1420)`，表格正文/表头提升到 20px，行高提升到 54px，节点正文提升到 20px，并修复英文 token 硬拆问题；重生成 `docs/L2/assets/T8.7_LDPC_layered_schedule_flow.png`。审计通过：`python3 tools/audit_figure_geometry.py tools/figures/render_ldpc_layered_schedule.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures/render_ldpc_layered_schedule.py` 输出 `FIGURE_READABILITY_AUDIT_OK`；目检表格字号可读、单元格居中、箭头端点正常、底部日志区留白正常。`docs/L2/T8.7_layered_LDPC_decoding_schedule.md` 和 `docs/audits/image_asset_inventory.md` 已同步更新。 |
| 2026-06-20 | 阶段 4C 图片可读性整改：T8.8 LDPC 数值走读图 | 修复 `tools/figures/render_ldpc_numeric_walkthrough.py`：画布从 `(1600, 1280)` 扩为 `(2000, 1980)`，核心数值表正文/表头提升到 20px，主要行高提升到 54/64px，扩大列宽并重排 posterior 说明和底部调试字段面板；重生成 `docs/L2/assets/T8.8_LDPC_numeric_walkthrough.png`。首轮目检发现红色说明遮挡 posterior 表，已继续调整 y 坐标和底部面板后复检通过。审计通过：`python3 tools/audit_figure_geometry.py tools/figures/render_ldpc_numeric_walkthrough.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures/render_ldpc_numeric_walkthrough.py` 输出 `FIGURE_READABILITY_AUDIT_OK`；`docs/L2/T8.8_NR_LDPC_decoder_numeric_walkthrough.md` 复审计通过 `LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=263`。 |
| 2026-06-20 | 阶段 4C 图片可读性整改：NR Polar、T11.1、T12 与 T13.5 复核 | 本轮仅整改和复核负责项：`tools/figures/render_nr_polar_ca_scl_selector.py`、`render_nr_polar_decoder_chain_overview.py`、`render_nr_polar_edge_case_diagnosis.py`、`render_nr_polar_rate_recovery_flow.py`、`render_nr_polar_reliability_sequence.py`、`render_nr_polar_scl_path_pruning.py`、`render_turbo_ldpc_polar_algorithm_comparison.py`、`render_t12_1_golden_model_layout.py`、`render_t12_2_lte_turbo_float_sim_flow.py`、`render_t12_3_nr_ldpc_float_sim_flow.py`、`render_t12_4_nr_polar_float_sim_flow.py`、`render_t12_5_ber_bler_curve_reporting.py`、`render_t13_5_simd_memory_layout_decoders.py`；对应 PNG 已全部重生成。逐脚本审计结果均为 `FIGURE_GEOMETRY_AUDIT_OK` 与 `FIGURE_READABILITY_AUDIT_OK`，包括 `python3 tools/audit_figure_geometry.py tools/figures/render_t13_5_simd_memory_layout_decoders.py` / `python3 tools/audit_figure_readability.py tools/figures/render_t13_5_simd_memory_layout_decoders.py`。本轮整改动作包括：把表格正文/表头/首列/说明框教学文字统一抬到 20px+，把表格行高统一抬到 48px 以上，扩大画布、列宽和底部说明框留白，修复 T11.1 比较面板长说明、T12.2 输出枢纽与实验矩阵间距、T12.5 `metrics.csv` 表格换行，确保表格单元格水平/垂直居中并复核箭头端点贴边。人工目检重点覆盖 T11.1 连线/表格、T12 小字、Polar 表格和底部说明框；结果可接受。保留例外：`T10.3_TS38.212_Table_5.3.1.2-1_Polar_sequence.png` 为完整 1024 项可靠性序列长图，`rank/Q(rank)` 属码位短索引例外，但标题、表头、脚注和行高已按本轮规则放大。 |
| 2026-06-20 | 阶段 4C 全项目图片可读性整改清零（历史快照） | 在并行代理完成三组整改后，主线程复核并继续修复 NR LDPC 残留 finding。当时全项目命令 `python3 tools/audit_figure_readability.py tools/figures` 输出 `FIGURE_READABILITY_AUDIT_OK`，`python3 tools/audit_figure_geometry.py --focus-only tools/figures` 输出 `FIGURE_GEOMETRY_AUDIT_OK`。该记录为旧 20px/48px 门槛下的历史快照，已被后续 24px/56px 全局字体扫描和 46 张 PNG 资产清单覆盖；当前最终状态以后续“阶段 4C 图片可读性二次加严与漏网图修复完成”记录为准。 |
| 2026-06-20 | T13.5 C/C++ 译码器 SIMD 与内存布局完成 | 新增 `docs/L3/T13.5_SIMD_memory_layout_decoders.md`，使用 `tools/figures/render_t13_5_simd_memory_layout_decoders.py` 生成 `docs/L3/assets/T13.5_SIMD_memory_layout_decoders.png`。正文覆盖 Turbo/LDPC/Polar C/C++ 内存布局、对齐、SIMD 友好数组、缓存局部性、向量化机会、profiling 计划、非合并访存失败案例，并扩展 AoS/SoA、cache line、lane、stride、padding/tail mask 手算例子、packed/unpacked、false sharing、hot/cold trace、RTL/ASIC 映射和验证方法；明确 SIMD/cache 是实现策略，协议对象只通过上游 T7/T8/T9/T10/T12/T13.2-T13.4 的 descriptor/hash 回链。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=36`、`REFERENCE_REBUILD_AUDIT_NO_CANDIDATES`、`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；目检 T13.5 图表格字号、单元格居中、底部说明、失败案例区和箭头路径可接受。`docs/audits/prompt_coverage_matrix.md` 已纳入 T13.5，覆盖总数更新为 78 篇，未纳入列表改为 `T13.6`、`T14.*`、`T15.*`。 |
| 2026-06-20 | 阶段 4C 图片可读性二次加严与漏网图修复完成 | 用户指出“整个项目都存在表格字体偏小问题”后，主线程将 `tools/audit_figure_readability.py` 从表格上下文检查扩展为全局字体扫描：除显式辅助例外外，`font(13..23)` 均报错；当前验收门槛为主体教学文字 24px+、表格行高 56px+。并行修复 LTE/Turbo、LDPC、NR LDPC、NR Polar/T11、L3 T12/T13 图后，主线程继续修复自动审计漏网的 `T9.3_NR_LDPC_HARQ_CBG_RV.png`、`T9.5_NR_LDPC_reassembly_TB_CRC.png`、`T10.2_NR_Polar_N4_transform_frozen_mask.png`、`T10.4_NR_Polar_SC_N4_tree.png` 和 T13.1-T13.5 的 22px 常量。重点目检中发现并修复 T9.3 顶部标题挤压、底部 dump 卡片贴边、英文 token 硬拆，T9.5 重组标签遮挡和 CBG 卡片溢出。最终命令：`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`python3 tools/audit_figure_geometry.py --focus-only tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 -m py_compile tools/figures/*.py tools/audit_figure_readability.py tools/audit_figure_geometry.py` 无输出且退出码 0。剩余小字例外仅两处：T12.5 BLER 曲线 `axis_font=20` 坐标刻度，T7.3 ring buffer `font(12)` 短地址索引；两者均有更大字号说明区补偿。`docs/audits/image_asset_inventory.md` 已更新为 46 张 PNG、42 个脚本和二次加严审计记录。 |
| 2026-06-20 | T13.6 Bit-Exact 回归框架完成并修复审核 Important | 新增并完善 `docs/L3/T13.6_bit_exact_regression_harness.md`；新增 `tools/figures/render_t13_6_bit_exact_regression_harness.py` 和 `docs/L3/assets/T13.6_bit_exact_regression_harness.png`。正文覆盖 Python float/fixed、C/C++ fixed、RTL output 的 compare policy，统一 `decoder_vector_v1` schema、三类译码器专属 `protocol_fields`、metadata/hash、seed 派生、float-vs-fixed 容差、fixed/C++/RTL exact integer policy、Turbo/LDPC/Polar checkpoint manifest、小型 HARQ soft-combine 例子、failure bundle、CI 命令模板、RTL/ASIC 映射和自测答案。单篇审计：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=13`、`REFERENCE_REBUILD_AUDIT_NO_CANDIDATES`、`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`、`py_compile` exit 0；图片尺寸 `2300x2160`。审核经理文档复核首轮 `Critical=0, Important=3, Minor=3`，已修复 T13.6 三类 decoder 专属协议字段、`metadata.json` schema、执行记录真实结果、Prompt 覆盖验收表、first mismatch `lhs/rhs` 字段，并修正 T13.5 式号引用。 |
| 2026-06-20 | 模块 13 自动审计、Prompt 矩阵和图片复核关闭 | 模块 13 全量审计：`python3 tools/audit_lesson_terms.py docs/L3/T13*.md` -> `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L3/T13*.md` -> `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L3/T13*.md` -> `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L3/T13*.md` -> `LATEX_RENDER_AUDIT_OK formulas=278`；`python3 tools/audit_reference_rebuilds.py docs/L3/T13*.md` -> `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已复现表格/公式回链、论文引用、实现策略边界和 T13.6 新增字段来源说明。`docs/audits/prompt_coverage_matrix.md` 已纳入 T13.1-T13.6，覆盖总数更新为 79 篇，未纳入列表改为 `T14.*`、`T15.*`。图片审核经理逐图复核 T13.1-T13.6：Critical=0、Important=0；Minor 为 T13.5 lane 连线源 bbox 表达和 T13.6 Compare Core 入线集中度，已写入 `docs/audits/image_asset_inventory.md`，不阻塞模块 14。图片资产清单更新为 47 张 PNG、43 个脚本。 |
| 2026-06-20 | T14.1 LTE Turbo RTL 微架构完成 | 新增并完善 `docs/L3/T14.1_LTE_Turbo_RTL_microarchitecture.md`；新增 `tools/figures/render_t14_1_lte_turbo_rtl_microarchitecture.py` 和 `docs/L3/assets/T14.1_LTE_Turbo_RTL_microarchitecture.png`。正文覆盖 SISO 数据通路、alpha/beta 存储、外信息 RAM、交织/解交织地址生成器、乒乓迭代控制、CRC 早停、时钟/复位、吞吐和存储估算、接收端流程、RTL/ASIC 映射、验证方法、自测答案和 Prompt 覆盖表。图片首版出现 FSM 文本拥挤和 CRC fail 返回箭头穿行风险，已加高 FSM 节点并把返回箭头改为节点下方绕行；重生成后 `python3 tools/audit_figure_geometry.py tools/figures/render_t14_1_lte_turbo_rtl_microarchitecture.py` -> `FIGURE_GEOMETRY_AUDIT_OK`，`python3 tools/audit_figure_readability.py tools/figures/render_t14_1_lte_turbo_rtl_microarchitecture.py` -> `FIGURE_READABILITY_AUDIT_OK`，`python3 -m py_compile tools/figures/render_t14_1_lte_turbo_rtl_microarchitecture.py` 退出码 0。逐图目检按四项独立规则记录：字体与上下边框距离充足，边框间距正常，箭头方向/头部/线宽正常，连线起点按节点相对位置选择真实边界且不机械从右侧出线。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=55`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已重建协议表回链、工程估算公式和实现策略边界。 |
| 2026-06-20 | T14.2 NR LDPC RTL 微架构完成 | 新增并完善 `docs/L3/T14.2_NR_LDPC_RTL_microarchitecture.md`；新增 `tools/figures/render_t14_2_nr_ldpc_rtl_microarchitecture.py` 和 `docs/L3/assets/T14.2_NR_LDPC_RTL_microarchitecture.png`。正文覆盖 TS 38.212 §5.3.2 的 BG/$Z_c$/$i_{\mathrm{LS}}$/shift/QC 展开到 RTL 地址生成的协议精读，layered 调度控制器、CN sign/min1/min2/argmin、VN read-modify-write、message RAM、posterior LLR RAM、edge schedule ROM、bank conflict 处理、syndrome/CRC 早停、吞吐/存储估算、接收端流程、伪代码、定点策略、RTL/ASIC 映射、验证方法、自测答案和 Prompt 覆盖表。图片首轮目检发现中部表格底边和 FSM 标题条距离太近，已扩画布并下移 FSM/底部说明区；重生成后 `python3 tools/audit_figure_geometry.py tools/figures/render_t14_2_nr_ldpc_rtl_microarchitecture.py` -> `FIGURE_GEOMETRY_AUDIT_OK`，`python3 tools/audit_figure_readability.py tools/figures/render_t14_2_nr_ldpc_rtl_microarchitecture.py` -> `FIGURE_READABILITY_AUDIT_OK`，`python3 -m py_compile tools/figures/render_t14_2_nr_ldpc_rtl_microarchitecture.py` 退出码 0。逐图目检按四项独立规则记录：字体与上下边框距离充足，边框间距正常，箭头方向/头部/线宽正常，连线起点按模块相对位置从真实边界出发。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=85`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已复现 Table 5.3.2-1/2/3 回链、§5.3.2 协议公式转写和工程估算公式。审核经理 Newton 只读复核 `Critical=0, Important=0, Minor=1`；Minor 为台账 checklist 同步时序问题，主线程复核时 T14.2 checklist 已为 `[x]`，无需正文修改。 |
| 2026-06-20 | 全项目 Python 图片箭头头部方向修复批次 | 用户指出 `T12.1_golden_model_project_layout.png` 中斜直线箭头头部和直线方向不匹配后，已将“箭头头部必须沿实际连线向量绘制”写入 `合规与遵从.md`、路线图、台账和两份图片审核清单。修复 `tools/figures/render_t12_1_golden_model_layout.py`，并全局扫描固定三角箭头风险；本批次改为向量箭头头的脚本包括 `render_ldpc_layered_schedule.py`、`render_nr_ldpc_rate_recovery_overview.py`、`render_nr_ldpc_reassembly_tb_crc.py`、`render_ldpc_bp_spa_round.py`、`render_ldpc_tanner_syndrome.py`、`render_nr_ldpc_decoder_chain_overview.py`、`render_nr_polar_channel_polarization.py`、`render_nr_polar_ca_scl_selector.py`、`render_nr_polar_scl_path_pruning.py`、`render_nr_ldpc_edge_case_diagnosis.py`、`render_nr_ldpc_circular_buffer_states.py`、`render_nr_polar_edge_case_diagnosis.py`、`render_nr_polar_sc_decoding_tree.py`、`render_nr_polar_decoder_chain_overview.py`、`render_nr_ldpc_base_graph_selection.py`、`render_nr_ldpc_bit_deinterleaving.py`。对应 PNG 已重生成；逐脚本几何/可读性审计均通过。最终全局验证：`python3 tools/audit_figure_geometry.py --focus-only tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`python3 -m py_compile tools/figures/*.py` 退出码 0。目检抽查 `T12.1`、`T10.2`、`T10.5`、`T10.6`、`T9.4`，确认普通流程箭头为直线，端点在中点/对称锚点，箭头头部与斜直线方向匹配。 |
| 2026-06-20 | 全项目 Python 图片箭头/连线复审追加记录 | 针对用户继续指出的“箭头形状和直线不匹配”问题，重新核对全局规则落点：`合规与遵从.md`、路线图、`docs/audits/image_review_detailed_checklist.md` 和 `docs/audits/python_figure_visual_geometry_checklist.md` 均已写入箭头头部按实际连线向量绘制、普通流程直线优先、单条连线边中点、多入多出对称锚点和全图复检要求。fresh 验证结果：`python3 tools/audit_figure_geometry.py --focus-only tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`python3 -m py_compile tools/figures/*.py tools/audit_figure_geometry.py tools/audit_figure_readability.py` 退出码 0。手动代码扫描确认剩余少量垂直专用箭头只用于纯上下箭头，T14.2/T14.3 的 `polyline_arrow` 为反馈/回环避让，箭头头部已按末段向量绘制；该类例外后续仍需逐图记录避让原因，不能泛化为普通流程线。 |
| 2026-06-20 | T14.3 NR Polar RTL 微架构完成并关闭审核经理 Important | 新增并完善 `docs/L3/T14.3_NR_Polar_RTL_microarchitecture.md`；新增 `tools/figures/render_t14_3_nr_polar_rtl_microarchitecture.py` 和 `docs/L3/assets/T14.3_NR_Polar_RTL_microarchitecture.png`。正文覆盖 SC/SCL 树遍历、rate recovery 到 decoder input、LLR memory、partial-sum memory、path memory、PM update、`2L -> L` sorter/pruner、CRC/RNTI final selector、低延迟 FSM、存储/吞吐估算、数值例子、伪代码、RTL/ASIC 映射、验证方法、自测答案和 Prompt 覆盖表；明确 TS 38.212 约束 Polar construction/rate matching，而 list size、PM 近似、sorter、lazy copy 和低延迟控制属于实现策略。图片生成与审计：`python3 tools/figures/render_t14_3_nr_polar_rtl_microarchitecture.py` 写出 `2500x2500` PNG；`python3 tools/audit_figure_geometry.py tools/figures/render_t14_3_nr_polar_rtl_microarchitecture.py` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures/render_t14_3_nr_polar_rtl_microarchitecture.py` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/figures/render_t14_3_nr_polar_rtl_microarchitecture.py` 退出码 0。逐图目检按四项独立规则记录：字体与上下边框距离充足，边框间距正常，箭头方向/头部/线宽正常，主要流程线端点按边中点或真实边界计算，回环线为避让反馈路径且头部按末段向量绘制。审核经理复核 `Critical=0, Important=2, Minor=2`；已修复 roadmap 锚点错链、执行记录缺文档级审计结果、frozen leaf 与 information leaf 的 `SPLIT` 退出条件混写、`py_compile` 命令副作用记录。修复后单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=102`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已复现 TS 38.212 表格回链、实现策略边界和工程估算公式。 |
| 2026-06-20 | T14.4 统一译码子系统架构完成并关闭审核经理 Important | 新增并完善 `docs/L3/T14.4_unified_decoder_subsystem_architecture.md`；新增 `tools/figures/render_t14_4_unified_decoder_subsystem.py` 和 `docs/L3/assets/T14.4_unified_decoder_subsystem_architecture.png`。正文覆盖 Turbo/LDPC/Polar 三类引擎的统一外壳、common descriptor、family extension、共享输入/输出 DMA、HARQ soft buffer manager、RV transaction、配置寄存器分区、状态码、错误码、IRQ、顶层 FSM、每引擎独立测试、三任务具体数值例子、伪代码、定点字段传递、RTL/ASIC 映射、验证方法、自测答案和 Prompt 覆盖表；明确 TS 36.213/36.321/36.331/38.214/38.321/38.331 只作 context evidence，寄存器字段、地址、IRQ bit 和错误码是实现设计，未核验前不写成协议强制要求。图片首轮目检记录不准确：审核经理指出 Trace 到 Output DMA 紫色线仍穿过 Polar engine。已二次重画为 Trace 顶边右侧出线、上行、水平、再进入 Output DMA 底边的正交避让路径，并在脚本加入 `assert_no_unrelated_crossing()` 防复发断言；最终 `python3 tools/figures/render_t14_4_unified_decoder_subsystem.py` 写出 `2600x2400` PNG，`python3 tools/audit_figure_geometry.py tools/figures/render_t14_4_unified_decoder_subsystem.py` -> `FIGURE_GEOMETRY_AUDIT_OK`，`python3 tools/audit_figure_readability.py tools/figures/render_t14_4_unified_decoder_subsystem.py` -> `FIGURE_READABILITY_AUDIT_OK`，`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/figures/render_t14_4_unified_decoder_subsystem.py` 退出码 0；全项目图形审计也输出 OK。逐图目检按四项独立规则记录：字体与上下边框距离充足，边框间距正常，箭头方向/头部/线宽正常，dispatcher fanout 对称，trace 折线为记录过的避让例外，逐段避开 Polar engine 不穿框。审核经理复核 `Critical=0, Important=1, Minor=2`；Important 为首轮图片复检结论与实际 PNG 不一致，已修复；Minor 中 roadmap 锚点已改为 `1171`，`cbg_mask` 来源已明确为实现 descriptor 字段并回链 TS 38.214/T9.3 CBG 上下文。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=5`；引用重建审计输出 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为 `待核验` 上下文、实现边界和工程解释。 |
| 2026-06-20 | 全项目 Python 图片连线穿框规则落地与高风险折线整改 | 针对用户继续指出“箭头形状和直线部匹配、连线不能穿框、T12.1 连线不是直线”等问题，将规则追加到 `合规与遵从.md`、路线图和两份图片审核清单：跨层线、斜线、折线和反馈线不得穿过无关节点/卡片/表格/说明框；已知 bbox 时必须加入 segment-rectangle 相交断言或等价检查；折线/曲线必须记录避让原因并逐段检查。修复和加固范围：`render_t14_4_unified_decoder_subsystem.py` 加 `assert_no_unrelated_crossing()` 并重画 Trace 到 Output DMA；`render_t14_1_lte_turbo_rtl_microarchitecture.py` 为 CRC fail 回环加入穿框断言；`render_t14_2_nr_ldpc_rtl_microarchitecture.py` 为 layered feedback 和 retry loop 加穿框断言；`render_t14_3_nr_polar_rtl_microarchitecture.py` 为 remap feedback 和 next-bit loop 加穿框断言；`render_nr_polar_sc_decoding_tree.py` 的断言发现旧 partial-sum 回传斜段穿过 `再译 u2,u3` 框，已改为左侧短折线路径并加断言。验证：T14.1/T14.2/T14.3/T14.4/T10.4 均重新生成，单图 `audit_figure_geometry` 与 `audit_figure_readability` 通过；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile` 对这五个脚本退出码 0；T10.4 和 T14.4 已重新目检。`docs/audits/image_asset_inventory.md` 已更新相关资产记录。 |
| 2026-06-20 | 全项目 Python 图片明确穿框点第二批整改 | 根据只读子代理 Hilbert 全项目扫描结果，继续修复坐标可确认的穿框点：`render_t12_2_lte_turbo_float_sim_flow.py` 将 `Decoder -> Decoder Outputs` 改为垂直下行，避免贴/穿 `AWGN + LLR`；`render_t12_3_nr_ldpc_float_sim_flow.py` 将 decoder 放到 AWGN 正下方，避免旧长斜线穿 `Rate Match + RV` 和 `Trace + Metrics`；`render_t12_4_nr_polar_float_sim_flow.py` 同步修复旧长斜线穿 `Rate Match` 和 `CRC/RNTI + Metrics`；`render_t13_5_simd_memory_layout_decoders.py` 将 lane 到 map 的长斜线改为 bus 分流，避免穿 `LDPC lane map`；`render_t13_6_bit_exact_regression_harness.py` 改 RTL Output 到 Compare Core 的连接点，避免穿 `C/C++ Fixed`；`render_decoder_selection_by_channel_type.py` 调换 NR control/data 分支上下位置，避免 `RAT = NR -> UCI/DCI` 穿 `NR data`。以上图片均已重新生成，单脚本几何/可读性审计通过；T12.3、T13.5 已目检。重新生成缺失的 `docs/L3/assets/T14.2_NR_LDPC_RTL_microarchitecture.png`，关闭资产缺失问题。 |
| 2026-06-20 | 全项目 Python 图片箭头线身/头部一致性整改 | 针对用户指出 `T12.1` 图片箭头形状和直线部不匹配的问题，启动只读审核经理 Carver 全局扫描并修复 Critical/Important。修复范围：`tools/figures/render_t12_1_golden_model_layout.py` 重新布局为上方水平主链路 + `Artifact Fanout` 垂直扇出，消除普通流程斜向跨层线，并二次修复 fanout 框正文压下边框；`render_lte_harq_rv_windows.py`、`render_lte_turbo_encoder_structure.py`、`render_nr_ldpc_harq_cbg_rv.py`、`render_nr_polar_sc_decoding_tree.py` 将线身截断到箭头头部前，不再先画到尖端再叠三角头；`render_t14_1_lte_turbo_rtl_microarchitecture.py` 修复 FSM 回环线进入 `SISO A` 框内 22px 的问题，箭头尖端落在目标框底边。全局规则已补入 `合规与遵从.md`、路线图和两份图片审核清单：带三角箭头的线身必须在箭头头部之前停止，禁止线段画到箭头尖端后再覆盖；普通流程箭头优先水平/垂直或直接直线，例外必须是回传/避让路径并记录原因。审计工具 `tools/audit_figure_geometry.py` 新增直接画到箭头尖端的静态风险检查。重生成图片：T12.1、T14.1、T9.3、T7.3、T6.3、T10.4。验证命令：`python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tools/figures/*.py` 退出码 0。人工目视复核 T12.1、T14.1、T7.3、T9.3、T10.4、T6.3：字体上下边距、边框间距、箭头方向/头部/线宽、连线起止位置均可接受；T10.4 绿色回传线为 SC partial-sum 回传/避让路径例外，箭头头部按末段向量绘制。`docs/audits/image_asset_inventory.md` 已逐图更新。 |
| 2026-06-20 | 全项目 Python 图片箭头形状与路径一致规则加严 | 针对用户继续指出 `T12.1` 图片“箭头形状和直线不匹配”的问题，新增全局规则：箭头形状必须匹配实际路径类型，直线连接必须视觉上保持直线，折线/避让线必须由清晰直线段组成，箭头头部只按最后一段向量绘制；禁止 `joint="curve"`、Bezier、弧线、遮罩或分段错位把普通流程线画成似直非直。已写入 `合规与遵从.md`、`2026-06-19-lte-nr-decoding-learning-roadmap.md`、`docs/audits/image_review_detailed_checklist.md`、`docs/audits/python_figure_visual_geometry_checklist.md` 和本台账执行规则。修复范围：`tools/figures/render_t12_1_golden_model_layout.py` 扩画布到 `(2500, 1500)`，将 `Artifact Fanout` 四条出线固定为 `[-960, -450, 450, 960]` 对称锚点并保持垂直直线；`tools/figures/render_t14_4_unified_decoder_subsystem.py` 去掉 Trace 折线的 `joint="curve"`，改为逐段直线绘制；`tools/audit_figure_geometry.py` 增加 `joint="curve"` 风险检查并补 `tests/test_audit_figure_geometry.py` 单测。验证：`python3 tools/figures/render_t12_1_golden_model_layout.py` -> 写出 `(2500, 1500)`；`python3 tools/figures/render_t14_4_unified_decoder_subsystem.py` -> 写出 `(2600, 2400)`；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 4 tests OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/figures/render_t12_1_golden_model_layout.py tools/figures/render_t14_4_unified_decoder_subsystem.py` 退出码 0；单图与全项目 `audit_figure_geometry` / `audit_figure_readability` 均输出 OK。人工目视复核 T12.1 和 T14.4：字体上下边距、相邻边框间距、箭头头部/线宽、连线起止位置和路径形态均通过；T14.4 Trace 线仍是有记录的避让例外，但不再使用曲线 join。 |
| 2026-06-20 | 全项目 Python 图片箭头路径静态审计加硬 | 针对用户继续指出“箭头的形状和直线部不匹配”，在既有规则基础上进一步把问题固化到自动审计：`tools/audit_figure_geometry.py` 新增普通 `arrow()`/`connect_arrow()`/`arrow_between()` helper 内曲线、弧线、Bezier 风格 token 和未标注多段路径风险检查；`tests/test_audit_figure_geometry.py` 新增曲线连接器和普通箭头 helper 多段路径两个回归测试。同步更新 `合规与遵从.md`、路线图、`image_review_detailed_checklist.md`、`python_figure_visual_geometry_checklist.md` 和本台账执行规则，要求后续新增或修改绘图脚本必须运行回归测试和全项目几何审计。本轮验证：`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 6 tests OK`；`python3 tools/audit_figure_geometry.py tools/figures && python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK` / `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tests/test_audit_figure_geometry.py tools/figures/*.py` 退出码 0。未发现新的实际图片脚本违规；本轮主要是规则和工具加固。 |
| 2026-06-20 | T14.5 软缓存与 HARQ 存储架构完成 | 新增 `docs/L3/T14.5_soft_buffer_HARQ_memory_architecture.md`；新增 `tools/figures/render_t14_5_soft_buffer_harq_memory.py` 和 `docs/L3/assets/T14.5_soft_buffer_HARQ_memory_architecture.png`。正文覆盖进程 ID、TB/CB/CBG 索引、RV 放置、饱和、存储 bank、淘汰、CRC fail 恢复、LTE/NR 差异、ContextKey/BlockKey/AddrKey/Access 分层、LTE RV overlap 小例子、NR CBGTI/CBGFI 小例子、接收端流程、伪代码、浮点仿真计划、定点化、RTL/ASIC 映射、验证方法、最小 dump 包、自测答案和 Prompt 覆盖表。图片首轮目检发现 Lifecycle FSM abort 线贴状态框底边，已改为框下方折线路径并加 `assert_no_unrelated_crossing()`；复检通过。审计结果：图形生成写出 `(2600, 2500)`；`python3 tools/audit_figure_geometry.py tools/figures/render_t14_5_soft_buffer_harq_memory.py` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures/render_t14_5_soft_buffer_harq_memory.py` -> `FIGURE_READABILITY_AUDIT_OK`；全项目图形几何/可读性审计均 OK；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/figures/render_t14_5_soft_buffer_harq_memory.py` 退出码 0。文档审计：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=15`；引用重建审计输出候选清单，候选均已分类为 `待核验` TS 36.213、TS 38.212 表格抽取边界、本节已生成图形资产或项目内参考讲义。`docs/audits/prompt_coverage_matrix.md` 和 `docs/audits/image_asset_inventory.md` 已更新。 |
| 2026-06-20 | 全项目 Python 图片箭头头部向量计算规则加严 | 针对用户指出 `T12.1` 箭头形状与直线不匹配的问题继续扩展静态审计：`tools/audit_figure_geometry.py` 新增普通 arrow helper 中三角箭头头部缺少 start/end 或最后一段向量方向计算的风险检查，`tests/test_audit_figure_geometry.py` 新增回归用例。全项目审计因此暴露 `render_lte_dl_ul_decoder_context.py` 的固定向下三角箭头 helper 和 `render_t14_1_lte_turbo_rtl_microarchitecture.py` 的固定向上三角箭头 helper；已分别改为 `arrow(start,end)` 和 `point_arrow(start,end)`，由实际线段向量计算头部并在头部前截断线身。重生成 `docs/L2/assets/T7.5_LTE_DL_UL_decoder_context.png` 和 `docs/L3/assets/T14.1_LTE_Turbo_RTL_microarchitecture.png`。验证：`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 7 tests OK`；两张单图几何/可读性审计均 OK；全项目 `python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；全项目 `python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/figures/render_lte_dl_ul_decoder_context.py tools/figures/render_t14_1_lte_turbo_rtl_microarchitecture.py tools/audit_figure_geometry.py tests/test_audit_figure_geometry.py` 退出码 0。 |
| 2026-06-20 | 全项目 Python 图片箭头线身与头部共线规则加严 | 针对用户继续指出 `T12.1` 图片“箭头形状和直线部匹配”问题，在既有头部向量规则上继续加硬：箭头头部方向正确还不够，线身截断点也必须沿同一个 start/end 或折线最后一段单位向量计算，不能只做固定 x/y 偏移导致线身轴线与头部中轴线不共线。已更新 `合规与遵从.md`、路线图、`docs/audits/image_review_detailed_checklist.md`、`docs/audits/python_figure_visual_geometry_checklist.md`。`tools/audit_figure_geometry.py` 新增 vector-shortened shaft 检查，`tests/test_audit_figure_geometry.py` 新增两个回归测试：固定轴截断必须报错，等价向量截断必须通过。初次全项目运行暴露 18 个 findings，其中多数为 `end = (...)`、`x1 - head_len * ux`、`line_points` 等等价写法被窄正则误判；已修正审计器以识别等价向量写法。最终验证：`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 9 tests OK`；`python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tests/test_audit_figure_geometry.py tools/figures/render_t12_1_golden_model_layout.py` 退出码 0。目视复核当前 `T12.1_golden_model_project_layout.png`：普通流程箭头为水平/垂直直线，fanout 锚点对称，箭头头部与线身方向一致。 |
| 2026-06-20 | 全项目 Python 图片箭头翼点法向量规则加严 | 针对用户继续指出 `T12.1` 图片“箭头的形状和直线部不匹配”，在既有线身/头部共线规则上继续补齐根因：线身按向量截断仍不够，三角箭头两个翼点也必须围绕同一个向量回退点，并由最终线段单位向量的法向量对称展开；禁止固定 `±x/±y` 偏移或角度模板导致人工无法确认头线一致。已更新 `合规与遵从.md`、路线图、`docs/audits/image_review_detailed_checklist.md`、`docs/audits/python_figure_visual_geometry_checklist.md` 和本台账执行规则。`tools/audit_figure_geometry.py` 新增 arrowhead wing points 静态检查，`tests/test_audit_figure_geometry.py` 新增两个回归测试：固定偏移翼点必须失败，法向量翼点必须通过。全项目审计暴露 `tools/figures/render_lte_harq_rv_windows.py` 和 `tools/figures/render_nr_ldpc_harq_cbg_rv.py` 仍使用旧角度/模板式翼点；已改为 `px, py = -uy, ux` 的统一法向量写法，重生成 `docs/L2/assets/T7.3_LTE_HARQ_RV_windows.png` 和 `docs/L2/assets/T9.3_NR_LDPC_HARQ_CBG_RV.png`，并更新 `docs/audits/image_asset_inventory.md`。验证：`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 11 tests OK`；`python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tests/test_audit_figure_geometry.py tools/figures/*.py` 退出码 0。 |
| 2026-06-21 | 全项目 Python 图片普通箭头两点直线规则加严并修复 T12.1 | 针对用户继续指出 `T12.1` 箭头起点/终点、非直线和箭头形状问题，完成根因复查：旧审计能抓 `joint="curve"` 和显式多段路径，但没有用 AST 覆盖普通 `arrow()` helper 内通过命名变量传入三点及以上路径的风险；T12.1 还存在 Runner 到 `Artifact Fanout` 不是边中点到边中点的问题。已更新 `合规与遵从.md`、路线图、`docs/audits/image_review_detailed_checklist.md`、`docs/audits/python_figure_visual_geometry_checklist.md` 和本台账执行规则，明确普通 `arrow()`/`connect_arrow()`/`arrow_between()` 只能绘制两点直线 shaft，三点及以上路径必须使用命名避让 helper 并配套穿框断言。`tools/audit_figure_geometry.py` 新增 AST 静态审计，`tests/test_audit_figure_geometry.py` 新增普通箭头命名三点路径失败和 `elbow_arrow` 命名避让通过两个回归测试。`tools/figures/render_t12_1_golden_model_layout.py` 已改为 Runner 底边中点到 Fanout 顶边中点，Bus 四条下行出线围绕底边中点对称，并新增 `title_to_node_gap`、`flow_to_table_gap`、`bottom_margin` 断言；重生成 `docs/L3/assets/T12.1_golden_model_project_layout.png`。验证：`python3 tools/figures/render_t12_1_golden_model_layout.py` -> 写出 `(2500, 1500)`；单图几何/可读性审计 OK；全项目 `python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；全项目 `python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 13 tests OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tests/test_audit_figure_geometry.py tools/figures/*.py` 退出码 0；规则文档标题审计 OK。 |
| 2026-06-20 | T14.6 译码器寄存器表与配置流完成并纳入台账/矩阵/图片清单 | 新增 `docs/L3/T14.6_decoder_register_map_configuration_flow.md`；新增 `tools/figures/render_t14_6_decoder_register_config_flow.py` 和 `docs/L3/assets/T14.6_decoder_register_map_configuration_flow.png`。正文覆盖算法选择、块长、码率、BG、Zc、RV、Qm、HARQ ID、列表大小、迭代上限、start/status/error/IRQ、字段来自 PHY/MAC/RRC/实现策略的分类、十类寄存器组、shadow lock 配置流、descriptor hash、错误码、软件伪代码、RTL/ASIC 映射、验证方法、自测答案和 Prompt 覆盖表；明确寄存器地址/IRQ/error code 是实现接口，不是 3GPP 强制字段。图片生成写出 `(2800, 2500)`，单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=2`；引用重建审计输出候选清单，候选已分类为 TS 36.213/MAC/RRC 精确字段 `待核验`、TS 38.212 上游表格回链或实现边界，不阻塞本节。`docs/audits/prompt_coverage_matrix.md` 已更新到 85 篇并移除 `T14.6` 未纳入项；`docs/audits/image_asset_inventory.md` 已更新到 53 张 PNG、49 个脚本并新增 T14.6 图片行。 |
| 2026-06-20 | 模块 14 自动审计通过 | 模块 14 全量审计：`python3 tools/audit_lesson_terms.py docs/L3/T14*.md` -> `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L3/T14*.md` -> `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L3/T14*.md` -> `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L3/T14*.md` -> `LATEX_RENDER_AUDIT_OK formulas=264`；`python3 tools/audit_reference_rebuilds.py docs/L3/T14*.md` -> `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选为上游已复现协议表回链、工程估算公式、项目内参考讲义和明确标注的 TS 36.213/MAC/RRC `待核验` 字段，不构成模块阻塞。全项目图片审计：`python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/figures/*.py tools/audit_figure_geometry.py tools/audit_figure_readability.py tests/test_audit_figure_geometry.py` 退出码 0；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 7 tests OK`。规则/台账类 Markdown 审计也输出 `MARKDOWN_HEADING_AUDIT_OK`。 |
| 2026-06-20 | 模块 14 等价审核经理复核完成，Critical=0、Important=0 | 子代理因线程上限无法启动，主线程按审核经理清单完成只读复核：T14.1-T14.6 均有自测题和参考答案、执行与证据记录、协议证据表或边界表；T14.6 已覆盖 roadmap Prompt 并扩展字段分类、寄存器组、配置 FSM、数值走读、driver 伪代码和验证计划；寄存器地址、IRQ、error code、`max_iterations/list_size/trace_mask` 等均明确为实现策略或实现接口，没有写成 3GPP 强制字段；TS 36.213、MAC/RRC 精确字段均保持 `待核验`；`prompt_coverage_matrix.md` 已纳入 T14.6 且未纳入列表只剩 `T15.*`；`image_asset_inventory.md` 记录 53 张 PNG/49 个脚本并包含 T14.6。目视复核 T14.6、T14.1、T7.5 图片：字体上下边距、相邻边框间距、箭头头部/线身方向、连线起止位置和底部留白均通过。 |
| 2026-06-20 | T15.1 译码器 SystemVerilog Testbench 架构完成 | 新增 `docs/L3/T15.1_decoder_testbench_architecture.md`；新增并修复 `tools/figures/render_t15_1_decoder_testbench_architecture.py` 和 `docs/L3/assets/T15.1_decoder_testbench_architecture.png`。正文覆盖 reference vector loader、driver、monitor、scoreboard、SVA assertions、reset/timeout tests、failure bundle、UVM/非 UVM 映射、C/C++ fixed vs RTL 比较关系、三类 decoder directed tests，以及一条 NR LDPC CBG 重传向量走读。协议边界明确：testbench methodology 不需要直接 3GPP 引用，向量必须回链 T7/T9/T10/T15.2 和 Rel-19 本地证据。图片首轮目检发现 Scoreboard 到 Failure Bundle 直线穿过 Assertions 卡片，已改成下方折线避让并加入 `assert_no_unrelated_crossing()`；复检四项硬规则通过。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=12`；引用重建审计输出候选清单，其中 `RV/k0` 是 directed test 标签不是新公式引用，项目内参考讲义候选已由正文证据表回链，不构成阻塞。图片审计通过：单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，全项目几何/可读性审计均 OK，`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 9 tests OK`。`docs/audits/prompt_coverage_matrix.md` 已更新到 86 篇并新增 T15.1 行，未纳入列表改为 `T15.2-T15.6`；`docs/audits/image_asset_inventory.md` 已更新到 54 张 PNG、50 个脚本并新增 T15.1 图片行。 |
| 2026-06-20 | T15.2 协议向量与边界案例套件完成 | 新增 `docs/L3/T15.2_protocol_vector_corner_case_suite.md`；新增并修复 `tools/figures/render_t15_2_protocol_vector_corner_case_suite.py` 和 `docs/L3/assets/T15.2_protocol_vector_corner_case_suite.png`。正文覆盖协议向量对象模型、`suite_manifest.json`、`suite_policy.json`、positive/negative expected-fail pass/fail policy、LTE Turbo directed cases、NR LDPC directed cases、NR Polar directed cases、cross-family LLR/sign/saturation/reset/timeout/schema/hash vectors、小型循环缓存合并数值例子、Python 分类片段、RTL/ASIC 映射、最小 dump 包和 Prompt 覆盖表。协议边界明确：TS 36.212、TS 38.212、TS 38.214 提供协议派生字段和证据锚点；suite tier、expected fail class、timeout、checkpoint manifest 和 vector schema 为工程测试策略，不写成 3GPP 强制字段。图片首轮目检发现第一张表右边界贴近画布且底部说明框与第二张表接触，已缩表宽、加高画布并下移说明框，复检四项硬规则通过。单篇审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=17`；引用重建审计输出候选清单，候选已在执行记录中分类为上游已复现资产回链、边界防护用 `待核验` 表述或项目内部参考讲义，不构成阻塞。Python 片段输出 `T15.2_VECTOR_CLASSIFIER_OK [6, 7]`。图片审计通过：单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，脚本 py_compile 退出码 0。`docs/audits/prompt_coverage_matrix.md` 已更新到 87 篇并新增 T15.2 行，未纳入列表改为 `T15.3-T15.6`；`docs/audits/image_asset_inventory.md` 已更新到 55 张 PNG、51 个脚本并新增 T15.2 图片行。 |
| 2026-06-21 | T15.3 覆盖率与回归方案完成 | 新增 `docs/L3/T15.3_coverage_regression_strategy.md`；新增 `tools/figures/render_t15_3_coverage_regression_strategy.py` 和 `docs/L3/assets/T15.3_coverage_regression_strategy.png`。正文覆盖功能覆盖率、代码覆盖率、断言覆盖率、交叉覆盖率、回归健康度、coverage event 对象模型、LTE Turbo/NR LDPC/NR Polar family-specific bins、算法家族、块长、RV、Qm、CRC 状态、reset/abort/timeout、deterministic seed 公式、pre-commit/commit/nightly/weekly/release regression tier、nightly 五阶段计划、failure triage、failure class、sign-off gate、RTL/ASIC 可观测点、Prompt 覆盖表和协议证据表。协议边界明确：coverage methodology 不需要直接 3GPP 引用，依赖协议参数的 bins 回链 T7/T9/T10/T15.2 和 Rel-19 本地路径。图片生成写出 `(3000, 2860)`，单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，脚本 py_compile 退出码 0；Python 片段输出 `T15.3_COVERAGE_TOY_OK []`。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=15`；引用重建审计输出候选清单，候选已在执行记录中分类为协议证据边界或上游已复现表格回链，不构成阻塞。`docs/audits/prompt_coverage_matrix.md` 已更新到 88 篇并新增 T15.3 行，未纳入列表改为 `T15.4-T15.6`；`docs/audits/image_asset_inventory.md` 已更新到 56 张 PNG、52 个脚本并新增 T15.3 图片行。 |
| 2026-06-21 | T15.4 Synopsys Design Compiler 综合流程完成 | 新增 `docs/L3/T15.4_DC_synthesis_flow_decoders.md`；新增 `tools/figures/render_t15_4_dc_synthesis_flow_decoders.py` 和 `docs/L3/assets/T15.4_DC_synthesis_flow_decoders.png`。正文覆盖 DC 工具可用性边界、filelist、DC Tcl 脚本骨架、clock/SDC 约束、reset 假设、input/output delay、false path/multicycle 风险、compile/compile_ultra 方案、timing/area/power 报告解读、Turbo/LDPC/Polar/unified subsystem 常见关键路径、post-synthesis 协议向量回链、Prompt 覆盖表和协议证据表。当前环境 `command -v dc_shell || true` 与 `command -v design_vision || true` 均无输出，正文明确未安装可调用 DC，不能声称真实综合已运行；未生成 mapped netlist、真实 timing/area/power 报告或 gate-level replay。图片生成写出 `(3000, 2860)`，单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，脚本 py_compile 退出码 0；Python 片段输出 `T15.4_TIMING_TRIAGE_OK polar_sorter NR Polar SCL sorter -0.31`。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=3`；引用重建审计候选为本节自写 STA 基本公式，不是外部协议/论文复现缺口。`docs/audits/prompt_coverage_matrix.md` 已更新到 89 篇并新增 T15.4 行，未纳入列表改为 `T15.5-T15.6`；`docs/audits/image_asset_inventory.md` 已更新到 57 张 PNG、53 个脚本并新增 T15.4 图片行。 |
| 2026-06-21 | T15.5 时序收敛与关键路径调试完成 | 新增并审计 `docs/L3/T15.5_timing_closure_decoder_critical_paths.md`；新增 `tools/figures/render_t15_5_timing_closure_critical_paths.py` 和 `docs/L3/assets/T15.5_timing_closure_critical_paths.png`。正文覆盖 timing report 字段、path family 分类、LDPC check-node min tree、Polar sorter、Turbo ACS/度量更新、pipeline、retiming、register duplication、tree split、banking、面积/时序/功耗/延迟/验证取舍、Polar sorter 负 slack 数值例子、Python 分诊片段、自测答案、Prompt 覆盖表和协议证据表。协议边界明确：TS 36.212/38.212/38.214 只提供译码任务语义和向量回链，pipeline、retiming、register duplication、clock period 和 timing exception 是实现策略；当前仓库没有真实 STA/timing report，不能声称真实时序已收敛。图片生成写出 `(3000, 2940)`，单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，脚本 py_compile 退出码 0；Python 片段输出 `T15.5_TIMING_FIX_PLAN_OK stage_sorter ['pm_tie', 'crc_aided_selector', 'rnti_mismatch', 'latency_counter']`。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=10`；引用重建审计候选为本节自写路径分类公式和 sorter 复杂度公式，不是外部协议/论文复现缺口。`docs/audits/prompt_coverage_matrix.md` 已更新到 90 篇并新增 T15.5 行，未纳入列表改为 `T15.6`；`docs/audits/image_asset_inventory.md` 已更新到 58 张 PNG、54 个脚本并新增 T15.5 图片行。T15.1-T15.5 合并审计通过：术语、标题、深度、LaTeX `formulas=57`；全项目图形几何/可读性审计 OK；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 13 tests OK`。 |
| 2026-06-21 | T15.6 最终译码验证与证据报告完成 | 新增并审计 `docs/L3/T15.6_final_decoder_verification_evidence_report.md`；新增并生成 `tools/figures/render_t15_6_final_evidence_report.py` 和 `docs/L3/assets/T15.6_final_decoder_evidence_report.png`。正文覆盖最终证据对象模型、协议证据汇总表、仿真摘要、定点损失、RTL 回归、覆盖率、综合时序/面积/功耗、已知限制、waiver、sign-off 清单、NR LDPC CBG 重传证据包、JSON schema、Python manifest 校验片段、自测答案、Prompt 覆盖表和协议证据表。协议证据按具体 TS 包名、章节、表/图/公式锚点和本地路径汇总：TS 36.212、TS 36.213、TS 36.321、TS 38.212、TS 38.214；正文明确当前仓库没有真实完整 BLER campaign、真实定点损失结果、真实 SystemVerilog RTL regression、真实 coverage database、真实 DC mapped netlist 或真实 timing/area/power reports，最终工程签核状态应为 `hold`，不能把模板写成真实通过。图片生成写出 `(3000, 3060)`，单图 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，脚本 py_compile 退出码 0；正文 Python 片段输出 `T15.6_FINAL_EVIDENCE_SCHEMA_OK pass`。单篇文档审计通过：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=11`；引用重建审计输出候选清单，候选均为最终报告字段、上游已复现协议表/图/公式资产回链或本节明确边界，不构成新复现缺口。当时 `docs/audits/prompt_coverage_matrix.md` 已更新到模块 15 结束范围并新增 T15.6 行，`docs/audits/image_asset_inventory.md` 已更新到当时图片和脚本范围；最新全项目范围见后续 depth backlog 收尾记录。 |
| 2026-06-21 | 模块 15 自动审计与等价审核经理复核完成 | 模块 15 T15.1-T15.6 全量审计通过：`python3 tools/audit_lesson_terms.py docs/L3/T15.*.md` -> `LESSON_TERM_AUDIT_OK`；`python3 tools/audit_markdown_headings.py docs/L3/T15.*.md docs/audits/prompt_coverage_matrix.md docs/audits/image_asset_inventory.md docs/audits/lte_nr_decoding_remaining_work_register.md` -> `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_lesson_depth.py --strict docs/L3/T15.*.md` -> `LESSON_DEPTH_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/L3/T15.*.md` -> `LATEX_RENDER_AUDIT_OK formulas=68`；`python3 tools/audit_reference_rebuilds.py docs/L3/T15.*.md` 输出候选清单，候选分类为上游已复现协议表/图/公式回链、自写工程公式、项目内部参考讲义或明确标注的真实工具未运行边界。全项目图片审计通过：`python3 tools/audit_figure_geometry.py tools/figures` -> `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` -> `FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tests/test_audit_figure_geometry.py tools/figures/*.py` 退出码 0；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 13 tests OK`。等价审核经理复核 Critical=0、Important=0：T15.6 覆盖 Prompt 全量并适当扩展，具体 Rel-19 协议锚点写到 TS 包、章节、表/图/公式和本地路径；未把真实 BLER、定点、RTL、coverage、DC/timing/area/power 写成已通过；T15.6 图片普通流程箭头为两点直线、起终点在相邻卡片边中点、箭头头部按实际线段向量生成，表格 24px 且居中，底部说明框留白正常。 |
| 2026-06-21 | T12.1 宽聚合框长斜线问题全局规则化并复修 | 针对用户指出 `T12.1` 图片箭头形状和直线部不匹配、连线形态不直观的问题，完成主线程等效全局审计。根因不是当前 `arrow()` helper 的向量头部，而是宽 `Artifact Fanout` 作为横向聚合框时，旧布局用 Runner 到 Fanout 顶边中点的长斜线连接，虽然端点数学上落在中点，但读图上穿过视觉中心且容易造成箭头头部/线身匹配疑义；首次重排还暴露了未同步更新 Seed->Runner 连线调用导致斜线穿过 Runner 正文、底部说明行压边的问题，已立即修复。`tools/figures/render_t12_1_golden_model_layout.py` 已重排为 Seed 底边中点到 Runner 顶边中点、Runner 底边中点到 Fanout 顶边中点的竖直中心线直连，画布改为 `(2500, 1700)`，保留 Bus 四条下行出线 `[-960, -450, 450, 960]` 对称，新增中心线连接断言，并把 `bottom_margin` 改为从 note 框真实底边计算。重生成 `docs/L3/assets/T12.1_golden_model_project_layout.png`，目视复核四项硬规则通过：字体与上下边框距离充足，相邻边框间距正常，箭头方向/头部/线宽正常，连线起止位置为真实边中点且宽聚合框不再使用跨图长斜线。全局规则已写入 `合规与遵从.md`、路线图、`docs/audits/image_review_detailed_checklist.md`、`docs/audits/python_figure_visual_geometry_checklist.md`、本台账执行规则和 `docs/audits/image_asset_inventory.md`。验证：`python3 tools/figures/render_t12_1_golden_model_layout.py` 写出 `(2500, 1700)`；单图 `audit_figure_geometry`/`audit_figure_readability` 均 OK；后续全项目图形审计和单元测试另见本轮命令记录。 |
| 2026-06-21 | 历史记录：模块 15 结束时状态文件同步 | 当时已更新 `docs/audits/final_delivery_status.md`、`docs/audits/full_project_document_review.md`、`docs/audits/global_compliance_review.md`、`docs/audits/regression_command_plan.md` 和本台账开头状态，清理活跃状态文件中过期的 L1/L2 旧快照口径。当时实物计数：讲义 `91`、PNG `59`、Python 绘图脚本 `55`。当时全项目文档审计已复跑：术语首现 `LESSON_TERM_AUDIT_OK`，标题正式化 `MARKDOWN_HEADING_AUDIT_OK`，深度审计 `LESSON_DEPTH_AUDIT_OK`，LaTeX 全检 `LATEX_RENDER_AUDIT_OK formulas=6050`；引用重建候选重新生成并为候选清单，不是硬失败。图片审计已复跑：`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，脚本 py_compile 退出码 0，单元测试 `Ran 13 tests OK`。该记录为模块 15 结束时的历史快照；最新全项目范围见后续 depth backlog 收尾记录。 |
| 2026-06-21 | 本台账未完成项关闭与持续规则状态同步 | 按用户要求复核并关闭 `docs/audits/lte_nr_decoding_remaining_work_register.md` 中未执行完项。未勾选任务扫描已确认不存在 `- [ ]` 或 `* [ ]` 任务行；仅状态说明表保留 `[~]` 和 `BLOCKED` 的含义解释。开头“执行规则”区原未勾选项均为持续控制规则，本轮已按当前项目状态勾选并保留规则含义：后续新增/修改讲义和图片仍必须继续遵守。规则和台账格式审计通过：`python3 tools/audit_markdown_headings.py docs/audits/lte_nr_decoding_remaining_work_register.md docs/audits/lte_nr_depth_gap_backlog.md 合规与遵从.md` -> `MARKDOWN_HEADING_AUDIT_OK`；`python3 tools/audit_latex_render.py docs/audits/lte_nr_decoding_remaining_work_register.md docs/audits/lte_nr_depth_gap_backlog.md 合规与遵从.md` -> `LATEX_RENDER_AUDIT_OK formulas=17`。 |
| 2026-06-21 | Depth gap backlog 执行完成并同步当前范围 | 按 `docs/audits/lte_nr_depth_gap_backlog.md` 完成 A-G 全部任务，覆盖协议地图、TS 38.212 Chapter 5 接收侧地图、TS 38.214 MCS/TBS descriptor、共同理论底座、LTE Turbo、NR LDPC、NR Polar、L3 工程与图表/审计收尾。当前实物计数：讲义 `94` 篇，其中 L1 `28`、L2 `43`、L3 `23`；PNG `61` 张；Python 绘图脚本 `56` 个。全项目审计结果：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`；LaTeX 分段全检 L1 `2036`、L2 `3444`、L3 `948`，合计 `6428`；图片 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile ...` 退出码 0；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 13 tests OK`；引用重建候选刷新为 `1320` 行且仍为候选清单，不是硬失败。 |
