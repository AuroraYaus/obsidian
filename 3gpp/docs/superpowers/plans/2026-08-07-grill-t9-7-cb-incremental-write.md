# Plan: T9.7 CB 增量写讲义设计收敛（grill-me 拷问结果）

_Locked via grill — by Claude + 用户_

## Goal
按 grill-me 六轮拷问收敛的设计决策，改造 T9.7 讲义并拆出 CBG 系统性内容为新讲义 T9.8。

## Approach
1. **T9.7 改造**（docs/L2_协议算法/T9.7_CB_incremental_write.md）：
   - 前置概念速览压缩：四段 → 两段（TB/CB/CBG+IR 一段，LLR 软合并+NDI/CBGTI 一段）
   - CBG 内容压缩为触发视角：保留配置开启（PDSCH-CodeBlockGroupTransmission）、分组公式一行（M=min(N,C)）、CBGTI/CBGFI 语义简述；系统性展开（分组推导例子、反馈流程、与 TB-HARQ 对比）移除
   - 硬件视角保持清单式（不展开推导）
   - 新增判定链 Mermaid（NDI 翻转 + CBGTI 命中 → 覆盖/增量/保持三态）
   - 新增地址级覆盖演化表格例子（6 地址 × 3 轮，展示"未覆盖→中性 LLR"）
   - 学习目标 7 → 6 条（第 7 条改为触发视角）
   - 自测题：第 5 题（CBG 分组手算）移除，补 1 道覆盖演化题
2. **新建 T9.8_CBG 讲义**（docs/L2_协议算法/T9.8_CBG_code_block_group.md）：引入动机（R15）、配置参数、分组公式与 C=10/N=4 推导、CBGTI/CBGFI 完整语义、反馈流程、与 TB 粒度 HARQ 对比表
3. **验证**：latex 审计、标题审计、Mermaid 可渲染、T9.7 图审计（已有图不动）
4. **提交双推**（git push origin master）

## Key decisions & tradeoffs
- L2 定位（非 L3）：判定链是"协议字段→缓存行为"的翻译层，硬件落点只是展望
- CBG 拆出（非并入）：主题聚焦 + 可复用性（T9.0/T9.5/T11.x 将引用）
- 覆盖演化不画图（表格代替）：收益/成本比
- 判定链用 Mermaid（非 SVG）：简单决策树

## Risks / open questions
- T9.8 为拆出成果，需确保 T9.7 压缩后 CBG 触发视角自洽
- CBGTI 位图与 DCI format 的位级映射未核对（38.212 §7.3.1），T9.8 中标注待核验

## Out of scope
- 硬件实现细节（banking/RTL，留 T14.x）
- DCI format 位级展开
