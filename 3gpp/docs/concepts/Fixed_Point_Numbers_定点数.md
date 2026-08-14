---
type: definition
aliases:
  - Fixed-Point
  - 定点数
  - Q-format
  - 2s Complement
tags:
  - 3gpp
  - concepts
  - implementation
  - fixed-point
source_spec: "Engineering methodology; TS 36.212/38.212 decoder requirements"
---

# 定点数表示

## 独立解释任务

任务目标：解释定点数（Fixed-Point Number）如何用固定位宽整数表示实数 LLR，以及 Q 格式、二进制补码与饱和策略如何共同决定动态范围与精度。在 LTE/NR 译码链路中的位置：译码链路从浮点仿真走向寄存器传输级（Register Transfer Level, RTL）/专用集成电路（Application-Specific Integrated Circuit, ASIC）实现的第一步，作用于 LLR 存储、HARQ 软合并与迭代译码消息的每一次读改写。

## 科学定义

Q 格式用 `Qm.n` 描述定点数的小数点位置：总位宽 $W=m+n$（$m$ 含符号位），缩放因子 $2^n$。硬件保存整数 $q$，解释成实数时：

$$
x=\frac{q}{2^n}
$$

步长（精度）为 $\Delta=2^{-n}$，编码时 $q=\mathrm{round}(x\cdot2^n)$。有符号数统一用二进制补码（Two's Complement）：最高位为符号位，负数真值 $q=u-2^W$，其中 $u$ 是把同一串比特当无符号数的值；例如 4 bit 的 `1110` 表示 $14-16=-2$。动态范围约 $6m$ dB（$20\log_{10}(2^m)\approx6m$）。LLR 裁剪与位宽的工程权衡（T21.1 口径）：$\pm7$/4 bit 损失 <0.1 dB、$\pm15$/5 bit 损失 <0.05 dB、$\pm31$/6 bit 损失 <0.02 dB、$\pm63$/7 bit 损失 <0.01 dB；$\pm31$ 是拐点——再增位宽收益封顶而存储成本线性上涨。

## 直观模型

用 `Q4.2` 编码 LLR 值 $-1.75$，逐步演算：(1) 缩放：$-1.75\times2^2=-7$；(2) 6 bit 补码编码：$64-7=57$ 的二进制为 `111001`；(3) 解码验证：`111001` 按无符号读为 57，$57-2^6=-7$，除以 $2^2$ 还原 $-1.75$。`Q4.2` 的步长为 $2^{-2}=0.25$，最大可表示值为 $7.75$。若输入 9.0 超出范围，必须饱和（Saturation）到 7.75 而不是回绕成负数——HARQ 软合并与迭代译码会多次相加 LLR，溢出风险比单次软解调更高，饱和策略错误会使大 LLR 翻转符号、直接破坏译码。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 位宽越大越好 | 6 bit（$\pm31$）后收益封顶（<0.02 dB），而存储/面积成本线性上涨，须按工程预算权衡。 |
| `Qm.n` 的 m 不含符号位 | 本项目约定 $W=m+n$ 为总位宽、$m$ 含符号位：`Q4.2` 即 6 bit。 |
| 负数用原码表示 | 硬件统一用补码（$-x=\sim x+1$），加减法不区分符号，避免两套运算器。 |
| 溢出可以不管 | 必须饱和处理；回绕会让大 LLR 翻转符号，导致 CRC 系统性失败。 |
| 写"6 bit LLR"就足够 | 需求必须同时明确符号约定、Q 格式、$q_{\min}/q_{\max}$ 与取整方式（T18.1 要求）。 |

## 协议锚点

- 定点数与 LLR 量化策略非 3GPP 标准（接收机实现域）：协议规定编码、速率匹配与译码输入比特语义（TS 36.212/38.212），不规定接收端 LLR 位宽、Q 格式或饱和函数；详见 T5.1 资料与协议边界节。

## 图谱关联

- [[LLR_对数似然比]]
- [[LLR_Quantization_LLR量化]]
- [[T5.1_fixed_point_numbers_for_LLR]]
- [[T18.1_fixed_point_decoder_requirements]]
- [[T21.1_engineering_budget_overview]]
- [[T21.2_bitwidth_tracking_methodology]]
- [[概念图谱入口]]
- 关系语义：定点数是浮点算法到硬件整数运算的桥梁。
