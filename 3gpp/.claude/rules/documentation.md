# DOXYGEN 注释细则（知识库红线）

> CLAUDE.md 第 3 条引用的细则文件。所有 Python 脚本、Shell 脚本、配置文件中的函数/类/任务入口必须使用完整的 DOXYGEN 风格注释。代码可读性优先于功能正确性。

## 文件头

```python
#!/usr/bin/env python3
"""
@file    <文件名>
@brief   <一句话功能>
@date    YYYY-MM-DD
@note    <可选：设计说明/教训来源>
"""
```

## 函数

```python
def func(param1, param2) -> type:
    """@brief <一句话>
    @param param1 <说明>
    @param param2 <说明>
    @return <返回说明>
    @note  <可选>
    @throws <可选：异常情形>"""
```

## 脚本入口（main）

```python
def main() -> int:
    """@brief <一句话>
    @usage python3 <script> <args>
    @args  <参数说明>
    @env   <依赖环境>
    @exit_code 0 = 成功，1 = 失败"""
```

## 审查权重

代码审查时注释质量与功能正确性**同等权重**：缺文件头、缺参数说明、无教训来源注释均视为缺陷。
