---
type: spec
aliases:
  - 2026-07-20-figure-numbering
tags:
  - 3gpp
  - docs
  - superpowers
  - plan
source_spec: "docs/superpowers/plans/2026-07-20-figure-numbering.md"
---
# 全项目图编号与图片嵌入 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 3GPP 项目所有讲义（94 篇 .md）添加图编号，并将 assets/ 中已有但未嵌入的图片全部嵌入对应讲义。

**Architecture:** 单脚本批处理 —— 生成 Python 脚本遍历资产清单，为每篇讲义在 `## 执行与证据记录` 之前插入 `## 图示` 节，按 `![图 N：描述](assets/filename)` 格式嵌入图片。T2.1 的 2 张已嵌入 SVG 单独手动处理（改 alt text 加编号）。

**Tech Stack:** Python 3, bash, grep 审计

## 全局约束

- 图编号：每篇讲义内独立编号（`图 1`、`图 2`…），与公式 `式 (N)` 风格一致
- 格式：`![图 N：中文描述](assets/filename)`
- 位置：`## 图示` 节，在 `## 执行与证据记录` 之前
- 不创建新资产，只嵌入已有 assets/ 中的文件
- 文件名中的技术前缀（如 `T8.3_NR_LDPC_`）在 alt text 中简化，保留语义描述

## 数据摘要

| 类别 | 数量 |
|:---|:---|
| 总讲义数 | 94 |
| 已有实际 `![]()` 嵌入的讲义 | 1（T2.1，2 张 SVG） |
| 有资产但未嵌入的讲义 | ~40 |
| 无资产（无需处理）的讲义 | ~38 |
| 总需嵌入图片 | ~65 张 |

---

### Task 1: 手动修复 T2.1 已有的 2 张 SVG 嵌入（加图编号）

**Files:**
- Modify: `docs/L1/T2.1_AWGN_noise_scaling.md:178,193`

**说明:** T2.1 是目前唯一有实际 `![]()` 图片嵌入的文件，2 张 SVG 已有描述性 alt text 但缺编号。

- [ ] **Step 1: 改第 178 行——BPSK 载波图加编号**

原文（约第 178 行）：
```markdown
![BPSK 调制载波波形 — 比特与相位的对应关系](assets/T2.1_bpsk_carrier_waveform.svg)
```

改为：
```markdown
![图 1：BPSK 调制载波波形 — 比特与相位的对应关系](assets/T2.1_bpsk_carrier_waveform.svg)
```

- [ ] **Step 2: 改第 193 行——16QAM 星座图加编号**

原文（约第 193 行）：
```markdown
![16QAM 星座图与载波波形](assets/T2.1_16qam_constellation_carrier.svg)
```

改为：
```markdown
![图 2：16QAM 星座图与载波波形](assets/T2.1_16qam_constellation_carrier.svg)
```

- [ ] **Step 3: 验证**

```bash
grep -n '图 [0-9]' docs/L1/T2.1_AWGN_noise_scaling.md
```
预期输出：两行，分别显示 `图 1` 和 `图 2`。

---

### Task 2: 编写并运行批量嵌入脚本

**Files:**
- Create: `/tmp/embed_figures.py`（临时脚本）
- Modify: ~40 个 `docs/L1/*.md`, `docs/L2/*.md`, `docs/L3/*.md`

**说明:** 脚本遍历 L1/L2/L3 的 assets/ 目录，将每张图片嵌入对应讲义，放在 `## 图示` 节中（节位于 `## 执行与证据记录` 之前）。

- [ ] **Step 1: 编写脚本**

```python
#!/usr/bin/env python3
"""为所有讲义嵌入 assets 中的图片并添加图编号。

规则：
- 每篇讲义内的图片从 图 1 开始编号
- 如果文件已有 ![](assets/...) 嵌入，跳过（交给 Task 1 手动处理）
- 如果文件已有 ## 图示 节，跳过（避免重复添加）
- 插入位置：## 执行与证据记录 之前
"""

import os, re, sys

DOCS_ROOT = '/home/yys/AGENT/3gpp/docs'

# alt text 描述映射：从文件名提取可读描述
def make_alt_text(asset_name):
    """从资产文件名生成中文描述。"""
    name_no_ext = os.path.splitext(asset_name)[0]
    # 去掉 Txx.yy_ 前缀
    name_no_prefix = re.sub(r'^T\d+\.\d+_', '', name_no_ext)
    # 将下划线替换为空格，做基本可读化
    readable = name_no_prefix.replace('_', ' ')
    # 常见缩写展开
    replacements = {
        'NR': 'NR',
        'LTE': 'LTE',
        'LDPC': 'LDPC',
        'Polar': 'Polar',
        'Turbo': 'Turbo',
        'QAM': 'QAM',
        'BPSK': 'BPSK',
        'QC': 'QC',
        'BG1': 'BG1',
        'BG2': 'BG2',
        'BP': 'BP',
        'SPA': 'SPA',
        'MS': 'MS',
        'NMS': 'NMS',
        'OMS': 'OMS',
        'SC': 'SC',
        'SCL': 'SCL',
        'CA': 'CA',
        'CRC': 'CRC',
        'TB': 'TB',
        'CBG': 'CBG',
        'RV': 'RV',
        'HARQ': 'HARQ',
        'RTL': 'RTL',
        'SIMD': 'SIMD',
        'BER': 'BER',
        'BLER': 'BLER',
        'DC': 'DC',
        'TS38 212': 'TS 38.212',
        'TS36 212': 'TS 36.212',
        'N4': 'N=4',
        'L2': 'L=2',
    }
    # 按长度降序替换（避免短串先替换破坏长串）
    for old, new in sorted(replacements.items(), key=lambda x: -len(x[0])):
        readable = readable.replace(old, new)
    return readable.strip()

def main():
    stats = {'embedded': 0, 'skipped_has_section': 0, 'skipped_has_embed': 0, 'no_assets': 0}
    
    for level in ['L1', 'L2', 'L3']:
        assets_dir = os.path.join(DOCS_ROOT, level, 'assets')
        md_dir = os.path.join(DOCS_ROOT, level)
        if not os.path.exists(assets_dir):
            continue
        
        # 收集该层级所有资产，按讲义前缀分组
        md_assets = {}  # md_filename -> [(asset_name, sort_key), ...]
        md_files_set = {f for f in os.listdir(md_dir) if f.endswith('.md')}
        
        for asset in sorted(os.listdir(assets_dir)):
            m = re.match(r'(T\d+\.\d+)', asset)
            if not m:
                continue
            prefix = m.group(1)
            matches = [f for f in md_files_set if f.startswith(prefix)]
            if len(matches) != 1:
                continue
            md_file = matches[0]
            if md_file not in md_assets:
                md_assets[md_file] = []
            md_assets[md_file].append(asset)
        
        # 处理每篇讲义
        for md_file, assets in sorted(md_assets.items()):
            md_path = os.path.join(md_dir, md_file)
            with open(md_path, 'r') as f:
                content = f.read()
            
            # 检查是否已有 ![](assets/...) 嵌入
            has_embed = bool(re.search(r'!\[.*\]\(assets/', content))
            # 检查是否已有 ## 图示 节
            has_section = '## 图示' in content
            
            if has_section:
                stats['skipped_has_section'] += 1
                continue
            if has_embed and md_file != 'T2.1_AWGN_noise_scaling.md':
                # T2.1 已在 Task 1 处理，其他有嵌入的也应该处理
                pass
            
            # 构建图示节
            lines = ['\n## 图示\n']
            for i, asset in enumerate(assets, 1):
                alt = make_alt_text(asset)
                lines.append(f'![图 {i}：{alt}](assets/{asset})\n')
            
            figure_section = ''.join(lines)
            
            # 插入到 ## 执行与证据记录 之前
            if '## 执行与证据记录' in content:
                content = content.replace('## 执行与证据记录', figure_section + '\n## 执行与证据记录', 1)
            else:
                # fallback: 追加到文件末尾
                content += figure_section
            
            with open(md_path, 'w') as f:
                f.write(content)
            
            stats['embedded'] += 1
            print(f'  OK: {level}/{md_file} <- {len(assets)} figures')
        
        # 统计无资产的讲义
        for f in md_files_set:
            if f not in md_assets:
                stats['no_assets'] += 1
    
    print(f'\nDone. embedded={stats["embedded"]}, skipped_has_section={stats["skipped_has_section"]}, no_assets={stats["no_assets"]}')

if __name__ == '__main__':
    main()
```

- [ ] **Step 2: 运行脚本**

```bash
python3 /tmp/embed_figures.py
```

预期：输出每篇处理结果，最后显示 `embedded=N`（N 约 40-45）。

- [ ] **Step 3: 快速抽查 3 个文件**

```bash
# 抽查单图文件
grep -A2 '## 图示' docs/L2/T10.1_NR_Polar_decoder_chain_overview.md

# 抽查多图文件（T8.3 有 9 张资产）
grep -A10 '## 图示' docs/L2/T8.3_NR_LDPC_lifting_QC_matrix.md

# 抽查 L3 文件
grep -A2 '## 图示' docs/L3/T14.1_LTE_Turbo_RTL_microarchitecture.md
```

预期：每个文件都有 `## 图示` 节，图片从 `图 1` 开始编号，路径为 `assets/xxx.png`。

---

### Task 3: 全量审计

- [ ] **Step 1: 统计所有图示节**

```bash
grep -rn '## 图示' docs/L1/ docs/L2/ docs/L3/ --include="*.md" | wc -l
```

- [ ] **Step 2: 检查是否有遗漏资产（asset 存在但未嵌入）**

```bash
python3 -c "
import os, re
for level in ['L1','L2','L3']:
    ad = f'docs/{level}/assets'
    md_dir = f'docs/{level}'
    if not os.path.exists(ad): continue
    mds = {f for f in os.listdir(md_dir) if f.endswith('.md')}
    for a in sorted(os.listdir(ad)):
        pf = re.match(r'(T\d+\.\d+)', a)
        if not pf: continue
        matches = [f for f in mds if f.startswith(pf.group(1))]
        if len(matches)!=1: continue
        md = matches[0]
        content = open(f'{md_dir}/{md}').read()
        if a not in content:
            print(f'MISSING: {level}/{md} -> {a}')
"
```

预期：无输出（所有资产都已嵌入）。

- [ ] **Step 3: 检查图编号连续性**

```bash
python3 -c "
import os, re
for level in ['L1','L2','L3']:
    md_dir = f'docs/{level}'
    for f in sorted(os.listdir(md_dir)):
        if not f.endswith('.md'): continue
        content = open(f'{md_dir}/{f}').read()
        figs = re.findall(r'!\[图 (\d+)：', content)
        if figs:
            nums = [int(x) for x in figs]
            expected = list(range(1, len(nums)+1))
            if nums != expected:
                print(f'GAP: {level}/{f}: got {nums}, expected {expected}')
"
```

预期：无输出（所有图编号连续无缺）。

- [ ] **Step 4: 检查无重复的 ## 图示 节**

```bash
python3 -c "
import os
for level in ['L1','L2','L3']:
    md_dir = f'docs/{level}'
    for f in sorted(os.listdir(md_dir)):
        if not f.endswith('.md'): continue
        content = open(f'{md_dir}/{f}').read()
        count = content.count('## 图示')
        if count > 1:
            print(f'DUPLICATE: {level}/{f}: {count} sections')
"
```

预期：无输出。

---

### Task 4: 提交

- [ ] **Step 1: 查看 diff 统计**

```bash
git diff --stat
```

- [ ] **Step 2: 提交**

```bash
git add docs/L1/ docs/L2/ docs/L3/ docs/superpowers/plans/2026-07-20-figure-numbering.md
git commit -m "docs: 全项目图片嵌入与图编号 — 65 张图片嵌入 40+ 篇讲义，统一图 N 编号体系"
```

---
