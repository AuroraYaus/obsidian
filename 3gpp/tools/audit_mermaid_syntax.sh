#!/usr/bin/env bash
# @file    audit_mermaid_syntax.sh
# @brief   全库 Mermaid 块可渲染性批量验证：逐块用 mmdc（mermaid-cli）真实渲染，
#          失败块输出文档路径与错误信息。教训来源 2026-08-04 T2.0 parse error 漏检
#          （audit_mermaid_diagrams.py 依赖浏览器，环境无浏览器时 render_failed
#           无法区分语法错误与环境错误；本脚本显式配置 puppeteer 打通真实渲染）。
# @date    2026-08-04
# @usage   bash tools/audit_mermaid_syntax.sh [docs 子路径]
# @args    可选：限定扫描的 docs 子路径（默认全库）
# @env     需要 mmdc（mermaid-cli）与 puppeteer Chromium：
#          npx puppeteer browsers install chrome-headless-shell
# @exit_code 0 = 全部可渲染，1 = 存在失败块
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCOPE="${1:-docs}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# puppeteer 配置（root 环境需 --no-sandbox；executablePath 指向 puppeteer 缓存）
PPTR="$TMP/pptr.json"
CHROME_SHELL="$(ls -d ~/.cache/puppeteer/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell 2>/dev/null | head -1)"
if [ -z "$CHROME_SHELL" ]; then
    echo "ERROR: chrome-headless-shell 未安装，先运行: npx puppeteer browsers install chrome-headless-shell" >&2
    exit 2
fi
cat > "$PPTR" <<EOF
{
  "executablePath": "$CHROME_SHELL",
  "args": ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
}
EOF

# 提取全部 mermaid 块
python3 - "$ROOT/$SCOPE" "$TMP" <<'PYEOF'
import re, glob, sys, os
root, tmp = sys.argv[1], sys.argv[2]
lst = []
for f in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
    t = open(f, encoding="utf-8").read()
    for i, m in enumerate(re.finditer(r'```mermaid\n(.*?)```', t, re.S), 1):
        with open(os.path.join(tmp, f"b_{len(lst)}.mmd"), "w", encoding="utf-8") as fh:
            fh.write(m.group(1))
        lst.append(f"{f}\t{len(lst)-1}")
with open(os.path.join(tmp, "list.txt"), "w") as fh:
    fh.write("\n".join(lst))
print(f"提取 {len(lst)} 个 mermaid 块")
PYEOF

fail=0; total=0
while IFS=$'\t' read -r file bidx; do
    total=$((total+1))
    if ! timeout 40 mmdc -p "$PPTR" -i "$TMP/b_$bidx.mmd" -o "$TMP/out_$bidx.svg" >/dev/null 2>"$TMP/err.txt"; then
        fail=$((fail+1))
        echo "FAIL $file 块$((bidx+1)): $(grep -iE 'error|parse' "$TMP/err.txt" | head -1 | cut -c1-180)"
    fi
done < "$TMP/list.txt"
echo "共 $total 块, 失败 $fail"
[ "$fail" -eq 0 ]
