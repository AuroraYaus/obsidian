# L 系列目录改名报告：`docs/L0`→`docs/L0_协议阅读引导`、`docs/L1`→`docs/L1_基础`、`docs/L3`→`docs/L3_工程实现`

- 日期：2026-08-04
- 提交 hash：`feb3e5a9ec22e0894b9240b07a3e78bb8429c26a`（`refactor(docs): L 系列目录全套改名（L0_协议阅读引导/L1_基础/L3_工程实现）+ 路径引用更新`）
- 前置：`docs/L2` → `docs/L2_协议算法` 已于 commit `8b6a47b6d` 完成，本次对剩余 L 目录做同样处理。

## 改名确认

- 三个 `git mv` 全部成功：
  - `3gpp/docs/L0` → `3gpp/docs/L0_协议阅读引导`（4 个文件）
  - `3gpp/docs/L1` → `3gpp/docs/L1_基础`（101 个文件）
  - `3gpp/docs/L3` → `3gpp/docs/L3_工程实现`（59 个文件）
- 目录内容完整：L0=4、L1=101、L3=59 与 HEAD 文件数逐一相等，无文件丢失；git rename 检测 100% 命中（58 纯改名 + 106 改名兼修改）。
- 全部 226 个文件变更均为完全对称的路径替换（`git show --numstat -M` 逐文件核对 add==del，无任何非路径修改混入）。

## 更新文件数

- 提交总变更：**226 files changed, 1732 insertions(+), 1732 deletions(-)**（164 rename + 62 修改；增删完全对称）。
- sed 批量替换 164 个文件（`grep -rlI "docs/L0\|docs/L1\|docs/L3" 3gpp/`），覆盖 .md/.py/.json/.sh/.txt/**SVG**。SVG 为超出脚本示例的合理延伸：30 个资产 SVG 的 `@note`/说明文字内嵌旧路径（如 `docs/L1/T2.17_...md 配套图`），一并替换，与 L2 提交对 SVG 的处理一致。
- 替换顺序安全：单趟 sed 内 `docs/L0→docs/L0_协议阅读引导` → `docs/L1→docs/L1_基础` → `docs/L3→docs/L3_工程实现`，无嵌套误伤（已替换串不含后续匹配子串）；`docs/L2_协议算法`（已改名目录）未被触碰。
- 手工处理（sed 无法覆盖的按目录名拼接/相对引用）：
  1. `3gpp/tools/consolidate_docs_terms.py`（L17/L18/L19 常量、L386/L392 的 `../L0/` 相对引用）
  2. `3gpp/tools/ppt/convert_md_to_pdf.py:14`（`"docs" / "L1"` 拼接）
  3. `3gpp/tools/audit_lesson_terms.py:24`（`"docs" / "L0"` 拼接）
  4. `3gpp/tests/test_docs_terminology_consolidation.py`（L10/L18 的 `DOCS / 'L1'` 等字面量）
  5. `3gpp/docs/superpowers/plans/2026-06-25-docs-terminology-consolidation.md`：`docs/L0_terminology_glossary.md`（文件名式引用，共 3 处）→ `docs/L0_协议阅读引导/L0_terminology_glossary.md`
  6. 3 个审计清单文件中的 `../L1/` 相对引用（`python_figure_to_body_content_migration.md`、`reference_rebuild_candidates_full.txt`、`reference_rebuild_candidates_L2.txt`）
- **跨库路径保护**：`lte_nr_depth_gap_backlog.md` 中 41 处 `ldpc/docs/...` 指向另一知识库（ldpc），以占位符保护后原样还原，**未被误伤**（`ldpc/docs/L1_理论基础`、`ldpc/docs/L3_硬件实现` 保持原样）。
- **顺手修复 L2 改名遗留损坏**：`ldpc/docs/L2_协议算法_算法实现`（L2 改名时 sed 误伤 ldpc 路径所致）还原为 `ldpc/docs/L2_算法实现`，共 25 处，与 ldpc 库的 `L1_理论基础`/`L3_硬件实现` 命名风格一致。

## 验证输出

1. 目录完整性：L0=4、L1=101、L3=59 与 HEAD 文件数逐一相等 ✓
2. 残留检查：`grep -rlI "docs/L[013][^_]" 3gpp/` → 0 个文件 ✓（`L0_协议阅读引导`/`L1_基础`/`L3_工程实现` 因 `_` 不被匹配，符合预期）
3. 相对引用残留：`grep -rn "\.\./L[013]/"`（.md/.py/.txt）→ 0 ✓
4. Python 语法：全部变更 .py 文件 `py_compile` 通过 ✓
5. 功能测试：`python3 -m unittest tests.test_docs_terminology_consolidation` → 2 个测试 OK（遍历改名后目录）✓
6. 入口文件：`3GPP_讲义入口.md`、`L0_术语入口.md`、`L1_基础入口.md`、`L3_工程实现入口.md` 内部 wikilink/引用均为新路径 ✓
7. superpowers 教材设计文档：`textbooks/l3-engineering-lectures/00-教材设计.md:4` 已更新为 `3gpp/docs/L3_工程实现/T21.x_*.md`；`textbooks/ps-lectures/00-教材设计.md` 引用的 `docs/L2_协议算法/T13.x` 不受影响 ✓
8. 提交后工作树干净（3gpp/ 下无未提交变更）✓

## 注意事项（concerns）

1. **`.obsidian/graph.json`（9 处）与 `.obsidian/workspace.json`（18 处）仍含旧路径**（如 `docs/L1/assets/T2.12_timing_sync_fft_window.svg` 图谱查询、打开面板的文件路径）。与 L2 改名时情况相同：Obsidian 应用状态文件在仓库根、超出 `3gpp/` 范围，未改动也未纳入提交；Obsidian 重新打开/刷新后可自愈或需手动更新查询。
2. **SVG 资产内容更新但未重渲染**：30 个 SVG 的说明文字（`@note` 等）已改为新路径，但未重新跑渲染脚本（图形内容无需变，仅文本路径变化，sed 直接改文本已等效）。下次运行 `tools/figures/*.py` 重渲染时输出一致。
3. **`2026-06-25-docs-terminology-consolidation.md` 的 `docs/L0_terminology_glossary.md` 引用**（计划文档中的 3 处）原本就省略了 `L0/` 目录段，本次按实际文件位置修正为 `docs/L0_协议阅读引导/L0_terminology_glossary.md`。
4. **ldpc 跨库路径**：`lte_nr_depth_gap_backlog.md` 中的 `ldpc/docs/L1_理论基础`、`ldpc/docs/L3_硬件实现`、`ldpc/docs/L2_算法实现`（本次还原）指向 ldpc 知识库，若 ldpc 库自身做同名改名需另行同步。
