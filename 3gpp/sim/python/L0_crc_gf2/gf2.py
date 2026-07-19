def gf2_add(a, b):
    _require_bit(a)
    _require_bit(b)
    return a ^ b


def gf2_matmul(a, b):
    # Time: O(R·C·K), Space: O(R·C)
    # where R=rows(a), K=inner dim, C=cols(b)
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


def gf2_rank(matrix):
    # Time: O(R·C·min(R,C)), Space: O(R·C) — Gaussian elimination over GF(2)
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


def encode_linear_block(u, G):
    # Time: O(K·N), Space: O(K·N) — single matrix-vector product over GF(2)
    if not u:
        raise ValueError("u must not be empty")
    if not G:
        raise ValueError("G must not be empty")
    product = gf2_matmul([u], G)
    return product[0]


def syndrome(r, H):
    # Time: O(M·N), Space: O(M·N) — H·r^T over GF(2)
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


def _require_bit(value):
    if not isinstance(value, int) or isinstance(value, bool) or value not in (0, 1):
        raise ValueError(f"GF(2) value must be int 0 or 1, got {value!r}")


def _require_rectangular(matrix, name):
    if not matrix:
        return
    width = len(matrix[0])
    for row in matrix:
        if len(row) != width:
            raise ValueError(f"{name} must be rectangular")
