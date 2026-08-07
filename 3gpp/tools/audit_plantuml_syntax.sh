#!/usr/bin/env bash
# @file    audit_plantuml_syntax.sh
# @brief   全库 PlantUML 块可渲染性批量验证：逐块用 plantuml.jar 真实渲染，
#          失败块输出文档路径与错误信息。2026-08-07 绘图政策（Python 绘图禁令，
#          大型图用 PlantUML）配套验证手段——真实渲染而非静态正则。
# @date    2026-08-07
# @usage   bash tools/audit_plantuml_syntax.sh [docs 子路径]
# @args    可选：限定扫描的 docs 子路径（默认全库）
# @env     java 21+；plantuml.jar 默认 ~/.local/bin/plantuml.jar，
#          可用环境变量 PLANTUML_JAR 覆盖；工具缺失时显式报错（不视为通过）
# @exit_code 0 = 全部可渲染，1 = 存在失败块，2 = 工具缺失
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCOPE="${1:-docs}"
JAR="${PLANTUML_JAR:-$HOME/.local/bin/plantuml.jar}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if ! command -v java >/dev/null 2>&1; then
    echo "ERROR: java 未安装（PlantUML 依赖 Java）" >&2
    exit 2
fi
if [ ! -f "$JAR" ]; then
    echo "ERROR: plantuml.jar 未找到（$JAR），先下载官方 jar 或设 PLANTUML_JAR" >&2
    exit 2
fi

# 提取全部 plantuml 块（root 不存在视为扫描异常，0 块视为正常）
python3 - "$ROOT/$SCOPE" "$TMP" <<'PYEOF'
import re, glob, sys, os
root, tmp = sys.argv[1], sys.argv[2]
if not os.path.isdir(root):
    sys.exit(1)
lst = []
for f in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r'```plantuml\n(.*?)```', t, re.S):
        with open(os.path.join(tmp, f"b_{len(lst)}.puml"), "w", encoding="utf-8") as fh:
            fh.write(m.group(1))
        lst.append(f"{f}\t{len(lst)}")
with open(os.path.join(tmp, "list.txt"), "w") as fh:
    if lst:
        fh.write("\n".join(lst) + "\n")
print(f"提取 {len(lst)} 个 plantuml 块")
PYEOF
if [ ! -s "$TMP/list.txt" ]; then
    echo "共 0 块, 失败 0（全库无 plantuml 块，正常）"
    exit 0
fi

fail=0; total=0
while IFS=$'\t' read -r file bidx; do
    total=$((total+1))
    if ! timeout 60 java -Djava.awt.headless=true -jar "$JAR" -checkonly -quiet \
            "$TMP/b_$bidx.puml" >/dev/null 2>"$TMP/err.txt"; then
        fail=$((fail+1))
        echo "FAIL $file 块$((bidx+1)): $(head -c 180 "$TMP/err.txt" | tr "\n" " ")"
        continue
    fi
    if ! timeout 60 java -Djava.awt.headless=true -jar "$JAR" -tsvg \
            "$TMP/b_$bidx.puml" -o "$TMP" >/dev/null 2>"$TMP/err2.txt"; then
        fail=$((fail+1))
        echo "FAIL(渲染) $file 块$((bidx+1)): $(head -c 180 "$TMP/err2.txt" | tr "\n" " ")"
    fi
done < "$TMP/list.txt"
echo "共 $total 块, 失败 $fail"
[ "$fail" -eq 0 ]
