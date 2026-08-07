"""
@file crc.py
@brief GF(2) 上的多项式长除法 — 循环冗余校验（CRC）核心实现
@date 2026-07-19

在 GF(2) 上实现 CRC 的四个核心操作：
1. poly_div_mod2  — GF(2) 多项式长除法（求余式）
2. crc_remainder  — 计算消息的 CRC 余式
3. crc_attach     — 将 CRC 余式附加到消息末尾，形成码字
4. crc_check      — 验证码字是否通过 CRC 校验

GF(2) 上的多项式运算等价于：加法=XOR（无进位），乘法的中间步骤
仅在系数=1 时移位累加。CRC 在 LTE PDSCH/PUSCH 和 NR 的 TB-CRC、
CB-CRC 中被广泛使用。

@see gf2.py — GF(2) 加法/乘法基础运算
"""


def poly_div_mod2(dividend_bits: list[int], generator_bits: list[int]) -> list[int]:
    """
    @brief GF(2) 上的多项式长除法，返回余式

    逐位扫描 dividend：当前位为 1 时将 generator 对齐并 XOR（等价于
    GF(2) 减法），为 0 则跳过。最后 deg(generator)-1 位即为余式。

    以 [1,0,0,1] ÷ [1,0,1,1]（即 x^3+1 ÷ x^3+x+1）为例：
      1001
    ^ 1011  ← 最高位=1，异或
      ----
      0010  → 余式 (0,1,0)

    @param dividend_bits  被除多项式系数（高位在前），如 x^3+1 = [1,0,0,1]
    @param generator_bits 生成多项式系数（高位在前），如 x^3+x+1 = [1,0,1,1]
    @return               deg(generator)-1 位的余式
    @throws               ValueError 当输入为空、含非二进制值、或被除数短于除数时
    @note                 时间复杂度 O(N·G)，其中 N=dividend 长度，G=generator 长度
    """
    _validate_generator(generator_bits)
    _validate_bits(dividend_bits, "dividend_bits")
    if len(dividend_bits) < len(generator_bits):
        raise ValueError("dividend length must be at least generator length")

    work = list(dividend_bits)
    generator = list(generator_bits)
    for i in range(len(work) - len(generator) + 1):
        if work[i] == 1:
            for j, bit in enumerate(generator):
                work[i + j] ^= bit
    return work[-(len(generator) - 1):]


def crc_remainder(message_bits: list[int], generator_bits: list[int]) -> list[int]:
    """
    @brief 计算消息的 CRC 余式

    在消息尾部附加 deg(generator) 个零后再做多项式长除法。
    例如消息 [1,0,0,1,1]，生成多项式 [1,0,1,1]（deg=3）：
    dividend = [1,0,0,1,1,0,0,0]，对 generator 做长除，得到 3 位余式。

    @param message_bits   消息比特列表（高位在前）
    @param generator_bits 生成多项式系数（高位在前），deg ≥ 1
    @return               deg(generator)-1 位的 CRC 余式
    @throws               ValueError 当输入不合法时
    @note                 时间复杂度 O(M·G)，M=消息长度，G=生成多项式长度
    """
    _validate_bits(message_bits, "message_bits")
    _validate_generator(generator_bits)
    degree = len(generator_bits) - 1
    dividend = list(message_bits) + [0] * degree
    return poly_div_mod2(dividend, generator_bits)


def crc_attach(message_bits: list[int], generator_bits: list[int]) -> list[int]:
    """
    @brief 计算 CRC 余式并附加到消息末尾

    这是发送端操作：将 message_bits 和其 CRC 余式拼接，形成 CRC 码字。
    接收端用 crc_check 验证码字是否通过校验。

    @param message_bits   消息比特列表（高位在前）
    @param generator_bits 生成多项式系数（高位在前）
    @return               消息 + CRC 余式的拼接（码字）
    @see                  crc_check — 接收端的校验操作
    """
    return list(message_bits) + crc_remainder(message_bits, generator_bits)


def crc_check(codeword_bits: list[int], generator_bits: list[int]) -> bool:
    """
    @brief 验证 CRC 码字是否通过校验

    接收端操作：对码字做多项式长除法，余式全零则通过校验。
    CRC 能检测所有长度 ≤ deg(generator) 的突发错误。

    @param codeword_bits  消息 + CRC 余式的拼接（码字）
    @param generator_bits 生成多项式系数（高位在前）
    @return               True=通过校验（余式全零），False=检测到错误
    @see                  crc_attach — 发送端的编码操作
    """
    remainder = poly_div_mod2(codeword_bits, generator_bits)
    return all(bit == 0 for bit in remainder)


def _validate_generator(generator_bits: list[int]) -> None:
    """
    @brief 验证生成多项式的合法性

    生成多项式必须：长度 ≥ 2（度 ≥ 1）、最高位为 1（首一多项式）、
    所有元素为 0 或 1。

    @param generator_bits  生成多项式系数
    @throws                ValueError 当生成多项式不合法时
    """
    _validate_bits(generator_bits, "generator_bits")
    if len(generator_bits) < 2:
        raise ValueError("generator must have degree at least 1")
    if generator_bits[0] != 1:
        raise ValueError("generator must start with 1")


def _validate_bits(bits: list[int], name: str) -> None:
    """
    @brief 验证比特列表的合法性

    检查列表非空且所有元素为 int 0 或 1（不允许 bool 或 float）。

    @param bits  待验证的比特列表
    @param name  参数名，用于错误消息
    @throws      ValueError 当列表为空或包含非二进制值时
    """
    if not bits:
        raise ValueError(f"{name} must not be empty")
    for bit in bits:
        if not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1):
            raise ValueError(f"{name} must contain only int 0 or 1, got {bit!r}")
