---
type: spec
aliases:
  - GF(2) 与 CRC 仿真
  - L0 CRC GF2 教学仿真
tags:
  - sim
  - crc
  - gf2
source_spec: "T1.1-T1.3 teaching module"
---

# L0 CRC & GF(2) 仿真

GF(2) 二元有限域和 CRC 循环冗余校验的 Python 教学仿真，配套讲义 T1.1–T1.3。

## 文件

| 文件 | 内容 |
|:---|:---|
| `gf2.py` | GF(2) 加法、矩阵乘法、秩、编码、校验子 |
| `crc.py` | GF(2) 多项式长除法、CRC 余数/附加/检查 |
| `test_gf2.py` | GF(2) 模块单元测试 |
| `test_crc.py` | CRC 模块单元测试 |

## 运行

```bash
# 零外部依赖，Python 3.9+
cd sim/python/L0_crc_gf2

# 运行全部测试（预期 20 passed）
python3 -m unittest test_crc test_gf2

# 冗余输出
python3 -m unittest test_crc test_gf2 -v
```

## 验收阈值

- 全部 20 个测试用例通过
- 覆盖：手算样例、attach/check 往返、单比特错检出、全零消息、短消息、边界条件、非法输入拒绝

## 与讲义对应

| 讲义 | 本模块提供 |
|:---|:---|
| T1.1 GF(2) 二元算术 | `gf2.py`: `gf2_add`, `gf2_matmul`, `gf2_rank`, `encode_linear_block`, `syndrome` |
| T1.2 GF(2) 多项式与 CRC | `crc.py`: `poly_div_mod2`, `crc_remainder`, `crc_attach`, `crc_check` |
| T1.3 GF(2) 向量与矩阵 | `gf2.py`: Hamming(7,4) 编码 + 单比特 syndrome 示例 |
