"""
@file gf2.py
@brief GF(2) 二元域上的线性代数运算
@date 2025

在 GF(2)（二元域，仅有 0 和 1 两个元素，加法=异或，乘法=与）上实现：
- 矩阵乘法
- 矩阵求秩（Gaussian elimination，高斯消元）
- 线性分组码编码（u × G）
- 伴随式计算（H × r^T）

这些是理解信道编码（LDPC、Turbo、Polar）的数学基础。
所有元素运算等价于整数的 XOR 和 AND 操作。

@see crc.py — 基于 GF(2) 多项式长除法的 CRC 实现
"""


def gf2_add(a: int, b: int) -> int:
    """
    @brief GF(2) 域上的加法（等价于 XOR）

    @param a  操作数，必须为 0 或 1（int 类型，不允许 bool）
    @param b  操作数，必须为 0 或 1（int 类型，不允许 bool）
    @return   a XOR b 的结果（0 或 1）
    @throws  ValueError 当输入不是 int 0 或 1 时
    """
    _require_bit(a)
    _require_bit(b)
    return a ^ b


def gf2_matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """
    @brief GF(2) 域上的矩阵乘法 C = A × B

    标准矩阵乘法但在 GF(2) 上执行：点积中的乘法用 AND，累加用 XOR。
    例如 [1,0,1] · [1,1,0]^T = (1&1) ^ (0&1) ^ (1&0) = 1 ^ 0 ^ 0 = 1。

    @param a  R×K 的左矩阵，每个元素必须为 0 或 1
    @param b  K×C 的右矩阵，每个元素必须为 0 或 1
    @return   R×C 的结果矩阵
    @throws  ValueError 当维度不匹配、矩阵非矩形、或元素不是 0/1 时
    @note    时间复杂度 O(R·K·C)，空间复杂度 O(R·C)
    """
    _require_rectangular(a, "a")
    _require_rectangular(b, "b")
    if not a or not b:
        return []
    if len(a[0]) != len(b):
        raise ValueError("matrix dimensions do not match")

    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    out = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            value = 0
            for k in range(inner):
                _require_bit(a[i][k])
                _require_bit(b[k][j])
                value ^= a[i][k] & b[k][j]
            out[i][j] = value
    return out


def gf2_rank(matrix: list[list[int]]) -> int:
    """
    @brief 计算 GF(2) 上矩阵的秩（Gaussian elimination，高斯消元）

    对矩阵执行 GF(2) 上的高斯消元：对每一列找主元（第一个 1），
    若找到则交换到当前行，并对所有其他行消去该列的非零元素。
    主元计数即为秩。

    @param matrix  R×C 的矩阵，每个元素必须为 0 或 1
    @return        矩阵的秩（独立行数）
    @note          时间复杂度 O(R·C·min(R,C))，空间 O(R·C)
    """
    _require_rectangular(matrix, "matrix")
    rows = [row[:] for row in matrix]
    if not rows:
        return 0

    rank = 0
    col_count = len(rows[0])
    for col in range(col_count):
        pivot = None
        for row in range(rank, len(rows)):
            _require_bit(rows[row][col])
            if rows[row][col] == 1:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for row in range(len(rows)):
            if row != rank and rows[row][col] == 1:
                rows[row] = [x ^ y for x, y in zip(rows[row], rows[rank])]
        rank += 1
    return rank


def encode_linear_block(u: list[int], G: list[list[int]]) -> list[int]:
    """
    @brief 线性分组码编码：c = u × G

    将 k 位信息向量 u 通过生成矩阵 G 编码为 n 位码字。
    运算在 GF(2) 上执行（矩阵乘法 = AND 累加 + XOR 归约）。

    @param u  k 位信息比特向量，每个元素为 0 或 1，不可为空
    @param G  k×n 的生成矩阵，不可为空
    @return   n 位编码后的码字
    @throws  ValueError 当 u 或 G 为空时
    @note    时间复杂度 O(k·n)，空间 O(k·n)
    @see     gf2_matmul — 底层矩阵乘法实现
    """
    if not u:
        raise ValueError("u must not be empty")
    if not G:
        raise ValueError("G must not be empty")
    product = gf2_matmul([u], G)
    return product[0]


def syndrome(r: list[int], H: list[list[int]]) -> list[int]:
    """
    @brief 计算接收向量的伴随式 s = H × r^T

    伴随式用于判断接收向量 r 是否为合法码字：
    - s = 0 向量 → r 是合法码字（或错误不可检测）
    - s ≠ 0 向量 → 检测到传输错误

    @param r  n 位接收向量，每个元素为 0 或 1，不可为空
    @param H  m×n 的校验矩阵，不可为空，列数必须与 r 长度一致
    @return   m 位伴随式向量
    @throws  ValueError 当 r 或 H 为空、或维度不匹配时
    @note    时间复杂度 O(m·n)，空间 O(m·n)
    @see     gf2_matmul — 底层矩阵乘法实现
    """
    if not r:
        raise ValueError("r must not be empty")
    if not H:
        raise ValueError("H must not be empty")
    if len(r) != len(H[0]):
        raise ValueError(
            f"r length {len(r)} does not match H column count {len(H[0])}"
        )
    column = [[bit] for bit in r]
    product = gf2_matmul(H, column)
    return [row[0] for row in product]


def _require_bit(value: int) -> None:
    """
    @brief 断言 value 是合法的 GF(2) 元素（int 0 或 1）

    GF(2) 上仅允许整数 0 和 1。bool 被拒绝是因为 True/False 虽是
    int 子类，但在 GF(2) 语境下容易引起语义混淆。float 被拒绝是
    因为 GF(2) 没有实数概念。

    @param value  待检查的值
    @throws       ValueError 当 value 不是 int 0 或 1 时
    """
    if not isinstance(value, int) or isinstance(value, bool) or value not in (0, 1):
        raise ValueError(f"GF(2) value must be int 0 or 1, got {value!r}")


def _require_rectangular(matrix: list[list[int]], name: str) -> None:
    """
    @brief 断言矩阵是矩形的（所有行长度相等）

    空矩阵（[]）视为合法，不做检查。

    @param matrix  待检查的二维列表
    @param name    矩阵名称，用于错误消息
    @throws        ValueError 当矩阵非矩形时（各行长度不一致）
    """
    if not matrix:
        return
    width = len(matrix[0])
    for row in matrix:
        if len(row) != width:
            raise ValueError(f"{name} must be rectangular")
