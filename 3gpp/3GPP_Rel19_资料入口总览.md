---
type: spec
aliases:
  - Rel-19 资料总入口
  - 3GPP 原始资料入口
tags:
  - 3gpp
  - rel19
  - index
source_spec: "3GPP_Rel19/manifest.csv"
---

# 3GPP Rel-19 资料入口总览

这个页面只做一件事：把当前工作区里可用的 Rel-19 原始资料、结构化抽取和索引页串起来。

## 核心入口

| 入口 | 用途 |
|:---|:---|
| [Rel-19 协议下载清单](3GPP_Rel19/Rel19_协议下载清单.md) | 协议号、ZIP 包、官方 URL 对照表。 |
| `3GPP_Rel19/manifest.csv` | 下载清单和 SHA-256 校验。 |
| `3GPP_Rel19/processed/manifest.json` | 结构化抽取状态总表。 |
| `3GPP_Rel19/processed/extraction_report.md` | 抽取报告和处理摘要。 |
| `3GPP_Rel19/processed/Rel19_processed_目录入口.md` | 抽取目录总入口。 |

## 使用顺序

1. 先确认协议号和包版本。
2. 再去 `processed/` 找对应的 `TS_36.213_36213-j30_s00-s05_index.md` 和 `TS_36.212_36212-j30_content.md`。
3. 如果要核对表格、公式或 media，回到 `processed/` 子目录里的 `tables/`、`equations/`、`media/` 和 `source.docx`。

## 关联说明

这页是仓库级入口，不替代协议正文，也不复写协议条文。
