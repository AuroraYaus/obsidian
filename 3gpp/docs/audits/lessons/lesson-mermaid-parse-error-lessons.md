# mermaid-parse-error-lessons

> Mermaid parse error 漏检教训——T2.0 括号问题被漏掉 4 层原因（范围盲区/工具形同虚设/修复不彻底/扫描规则针对性）；固化引号节点规则与验证手段

2026-08-04 用户两次报告 T2.0"时域与频域基础"Mermaid parse error（Obsidian 内渲染失败），第二次追问"为什么被漏掉"。

**漏检链条（4 层）**：
1. **范围盲区**：T2.12-T2.19 四维整改只覆盖该区间，T2.0-T2.11 的存量 Mermaid 无人做语法检查，存量错误直到用户在 Obsidian 打开才暴露
2. **验证工具形同虚设**：`audit_mermaid_diagrams.py` 用 mermaid-cli 渲染验证，依赖 Chromium；本环境无浏览器 → render_failed 输出无法区分"语法失败"与"环境失败"→"无法验证"被默认为"通过"
3. **修复不彻底**：第一次把 `X[k]`（无引号节点内方括号）改成 `X(k)`（圆括号）就收手——Obsidian 的 Mermaid 对无引号节点 `A[text]` 内的**任何括号**（方/圆）都敏感（与圆括号节点语法 `A(text)` 歧义）；没有全库扫描整类特殊字符，也没有直接用跨版本安全的引号节点写法
4. **扫描规则是"针对性的"**：全库扫描只查方括号嵌套模式（`\[[^\]]*\[`），没查圆括号——扫描规则按"已发现问题"设计，重蹈 [[lesson-svg-audit-blind-spots]] 的"针对性代替全量"教训

**How to apply（固化规则）**：
1. **引号节点规则**：Mermaid 节点文本含 `[ ] ( ) { }` 等特殊字符时一律用引号节点 `id["text"]`（所有 Mermaid 版本的安全子集）；无引号节点内禁止任何括号。全库已清零（2026-08-04）
2. **修复必须全库同类扫描**：修一类语法错误后，扫描**整类特殊字符**，不能只扫已发现的那一个字符
3. **验证手段先行**：语法修改必须有可运行验证；"工具不可用"必须显式声明为验证缺口，不能默认通过。本环境可用的验证链：mmdc + puppeteer 配置 `/tmp/pptr.json`（executablePath 指向 ~/.cache/puppeteer/chrome-headless-shell，--no-sandbox）
4. **存量冒烟**：整改某系列讲义时，至少对全库 Mermaid 块跑一遍可渲染性验证（tools/audit_mermaid_syntax.sh）
5. **验证命令**：`tools/audit_mermaid_syntax.sh`（全库 110 块 mmdc 渲染验证，2026-08-04 已打通真实浏览器链路）

**工具状态**：本环境 Chromium 已安装于 ~/.cache/puppeteer/chrome-headless-shell/linux-151.0.7922.71；mmdc 需 `-p /tmp/pptr.json` 才能启动（root 环境 --no-sandbox）。
