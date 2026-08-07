# L2 目录改名报告：`docs/L2` → `docs/L2_协议算法`

- 日期：2026-08-04
- 提交 hash：`8b6a47b6d13aa098af45fa807b2c066c92ecb03b`（`refactor(docs): docs/L2 目录改名 docs/L2_协议算法（避免与协议层 2 混淆）+ 全库路径引用更新`）

## 改名确认

- `git mv 3gpp/docs/L2 3gpp/docs/L2_协议算法` 执行成功，rename 记录 107 条（54 篇 T6.1–T13.6 讲义 + `assets/` 51 个资产 + `L2_协议算法入口.md` + `术语表.md` = 57 个文件）。
- 目录内容完整：`ls 3gpp/docs/L2_协议算法/` 包含 T6.1–T13.6 全部讲义、`assets/`、入口文件、术语表。

## 更新文件数

- 提交总变更：**173 files changed, 1894 insertions(+), 1894 deletions(-)**（107 rename + 66 内容修改；增删完全对称，均为路径替换）。
- sed 批量替换 113 个文件（`grep -rl "docs/L2" 3gpp/` + `sed -i 's|docs/L2|docs/L2_协议算法|g'`，覆盖 .md/.py/.json/.sh）。
- 额外处理：
  - 2 个 `.txt` 审计候选清单（`docs/audits/reference_rebuild_candidates_full.txt`、`reference_rebuild_candidates_L2.txt`）同样替换。
  - 2 处 Python 代码按目录名拼接路径，sed 无法覆盖，手工更新：
    - `3gpp/tools/consolidate_docs_terms.py:17`：`DOCS_ROOT / "L2"` → `DOCS_ROOT / "L2_协议算法"`
    - `3gpp/tests/test_docs_terminology_consolidation.py:10`：`DOCS / 'L2'` → `DOCS / 'L2_协议算法'`
- 纯文本 "L1/L2/L3"（讲义层级表述）与协议正文 "L2/3"（36.300/38.331 协议层概念）**未动**。

## 验证输出

1. 目录完整性：`ls 3gpp/docs/L2_协议算法/` → 54 篇 T* 讲义 + 51 assets + 入口 + 术语表 ✓
2. 残留检查：`grep -rl "docs/L2[^_]" 3gpp/ --include="*.md" --include="*.py"` → 无输出 ✓（.json/.sh/.txt 同样复检为 0）
3. `docs/L2` 全部出现均为 `docs/L2_协议算法`：`grep -rn "docs/L2" ... | grep -vc "L2_协议算法"` → 0 ✓
4. 入口文件 `L2_协议算法入口.md`：frontmatter `source_spec` 已更新为 `"3gpp/docs/L2_协议算法"`；内部 wikilink 均为相对链接（`[ [T6.1_...]]`），不受影响 ✓
5. Python 语法：两个手工修改文件 `py_compile` 通过 ✓
6. 功能测试：`python3 -m unittest tests.test_docs_terminology_consolidation` → 2 个测试 OK（遍历改名后目录）✓
7. 提交后工作树干净 ✓

## 注意事项（concerns）

1. **`.obsidian/graph.json`（6 处）与 `.obsidian/workspace.json`（16 处）仍含旧路径**（如 `path:3gpp/docs/L2/T6.` 图谱查询、打开面板的文件路径）。这两个文件是 Obsidian 应用状态，按脚本范围（`3gpp/`）未改动，也未纳入本次提交；Obsidian 重新打开/刷新后会自愈或需手动更新查询。
2. 本次提交按指令 `git add -A 3gpp/` 执行，**包含 1 处非本次任务的既有修改**：`3gpp/docs/L1_基础/T2.0_OFDM_system_overview.md`（T2 系列文案补 OFDM 全称，与改名无关）。
3. `regression_command_plan.md:43` 中 `docs/L1_基础/L2/L3/assets` 为讲义层级简写（非真实路径，不包含 `docs/L2` 子串），保持原样未改。
