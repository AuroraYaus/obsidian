#!/usr/bin/env python3
"""@file audit_link_integrity.py
@brief 全格式链接死链审计（Obsidian 语义）：wikilink（正文+代码块）+ Markdown 链接，一次扫全。
@date 2026-08-07
@note 教训来源（2026-08-07 空心节点三连盲区）：
    1. Obsidian metadataCache 会索引【代码块/行内代码内】的无转义 [[...]]，
       解析失败即产生图谱空心节点（幽灵节点）——T8.5 Python 嵌套列表推导式
       `[[i for i, ... if row[j]]...]]`、计划文件省略号字样 `[[T2.1_AWGN...]]` 均属此类。
       审计必须含代码块，转义 `\\[[` 除外。
    2. 路径形式 wikilink 按【vault 根】（.obsidian 所在目录）解析，不是按文件所在目录——
       3GPP_译码知识库入口.md 的 `[[3gpp/docs/...]]` 系列被旧工具误报。
    3. Markdown 链接正则必须 `\\]\\(`（旧版漏 `\\(`，把 `(3GPP_Rel19/x.md` 当目标误报）。
    另：3GPP_Rel19/processed 为协议抽取噪音（`[[` 为 ASN.1 文本残留），且图谱 search 已排除，
    默认不扫（--include-rel19 可开启）。
@usage python3 tools/audit_link_integrity.py [扫描路径...]
@args 可选：限定扫描路径（默认工作目录全扫）；--include-rel19 附带扫描 3GPP_Rel19
@env 无外部依赖
@exit_code 0 = 无死链，1 = 存在死链
"""

from __future__ import annotations

import glob
import os
import re
import sys

WIKI = re.compile(r"(?<!\\)\[\[([^\]]+)\]\]")          # 无转义 wikilink（Obsidian 会索引，含代码块内）
MD_LINK = re.compile(r"\]\(([^)]*\.md)(?:#[^)]*)?\)")   # Markdown 相对链接


def find_vault_root(start: str) -> str:
    """@brief 向上查找 Obsidian vault 根（含 .obsidian 的目录）。
    @param start 起始目录
    @return vault 根路径；未找到返回 start"""
    d = os.path.abspath(start)
    while True:
        if os.path.isdir(os.path.join(d, ".obsidian")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return os.path.abspath(start)
        d = parent


def frontmatter_aliases(text: str) -> list[str]:
    """@brief 解析 frontmatter aliases 列表。
    @param text 文件全文
    @return 别名列表（Obsidian 按别名解析 wikilink，审计需纳入）"""
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end < 0:
        return []
    fm = text[3:end]
    m = re.search(r"aliases:\s*(?:\[([^\]]*)\]|(?:\n\s*-\s*[^\n]+)+)", fm)
    if not m:
        return []
    if m.group(1):
        return [a.strip().strip('"\'') for a in m.group(1).split(",") if a.strip()]
    return [a.strip().strip('"\'') for a in re.findall(r"^\s*-\s*(.+)$", m.group(0), re.M)]


def audit_dir(root: str, vault_root: str, rel19: bool) -> list[str]:
    """@brief 审计目录下全部 md 的链接死链。
    @param root 扫描根路径
    @param vault_root vault 根（路径形式 wikilink 的解析基准）
    @param rel19 是否附带扫描 3GPP_Rel19（默认排除：提取噪音 + 图谱已排除）
    @return 死链描述列表
    @note 解析语义与 Obsidian 一致：无转义 [[..]]（含代码块内）按 basename/别名/
     vault 根路径解析；`[[^block]]` 为同文件块引用不报；Markdown 链接按文件目录相对解析。"""
    all_md: dict[str, str] = {}
    aliases: dict[str, str] = {}
    for f in glob.glob(os.path.join(vault_root, "**", "*.md"), recursive=True):
        if "/.obsidian/" in f:
            continue
        if not rel19 and os.sep + "3GPP_Rel19" + os.sep in f:
            continue
        all_md[os.path.basename(f)[:-3].lower()] = f
        for a in frontmatter_aliases(open(f, encoding="utf-8").read()):
            aliases.setdefault(a.lower(), f)
    findings: list[str] = []
    for f in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        if not rel19 and os.sep + "3GPP_Rel19" + os.sep in f:
            continue
        text = open(f, encoding="utf-8").read()
        base_dir = os.path.dirname(f)
        # 1) wikilink（含代码块/行内代码内，Obsidian 均索引；转义 \[\[ 不匹配）
        for m in WIKI.finditer(text):
            target = m.group(1).split("|")[0].split("#")[0].strip()
            if target == "" or target.startswith(("^", "http", "ftp", "www")):
                continue
            if "/" in target:
                p = target if target.endswith(".md") else target + ".md"
                if not os.path.exists(os.path.join(vault_root, p)):
                    findings.append(f"{f}: wikilink [[{m.group(1)}]] 目标不存在（vault 根路径解析失败）")
            else:
                key = target[:-3].lower() if target.endswith(".md") else target.lower()
                if key not in all_md and key not in aliases:
                    findings.append(f"{f}: wikilink [[{m.group(1)}]] 目标不存在（basename/别名均无）")
        # 2) Markdown 链接（相对文件目录解析）
        for m in MD_LINK.finditer(text):
            target = m.group(1)
            if target.startswith(("http", "https", "ftp", "#")):
                continue
            cand = os.path.normpath(os.path.join(base_dir, target))
            if not os.path.exists(cand) and not os.path.exists(target):
                findings.append(f"{f}: Markdown 链接 ({target}) 目标不存在")
    return findings


def main() -> int:
    """@brief 审计入口。
    @usage python3 tools/audit_link_integrity.py [扫描路径...] [--include-rel19]
    @args 默认扫描工作目录；vault 根自动探测（向上找 .obsidian）
    @env 无
    @exit_code 0 = 通过，1 = 存在死链"""
    args = sys.argv[1:]
    rel19 = "--include-rel19" in args
    args = [a for a in args if a != "--include-rel19"]
    roots = args or ["."]
    vault_root = find_vault_root(os.getcwd())
    total: list[str] = []
    for root in roots:
        total.extend(audit_dir(root, vault_root, rel19))
    if total:
        shown = total[:40]
        for x in shown:
            print(x)
        print(f"LINK_INTEGRITY_AUDIT_FAIL total={len(total)}（显示前 {len(shown)} 条）")
        return 1
    print(f"LINK_INTEGRITY_AUDIT_OK（vault 根: {vault_root}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
