def poly_div_mod2(dividend_bits, generator_bits):
    # Time: O(N·G) where N=len(dividend), G=len(generator)
    # Space: O(N+G) for working copies
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


def crc_remainder(message_bits, generator_bits):
    # Time: O(M·G), Space: O(M+G) where M=len(message), G=len(generator)
    _validate_bits(message_bits, "message_bits")
    _validate_generator(generator_bits)
    degree = len(generator_bits) - 1
    dividend = list(message_bits) + [0] * degree
    return poly_div_mod2(dividend, generator_bits)


def crc_attach(message_bits, generator_bits):
    return list(message_bits) + crc_remainder(message_bits, generator_bits)


def crc_check(codeword_bits, generator_bits):
    remainder = poly_div_mod2(codeword_bits, generator_bits)
    return all(bit == 0 for bit in remainder)


def _validate_generator(generator_bits):
    _validate_bits(generator_bits, "generator_bits")
    if len(generator_bits) < 2:
        raise ValueError("generator must have degree at least 1")
    if generator_bits[0] != 1:
        raise ValueError("generator must start with 1")


def _validate_bits(bits, name):
    if not bits:
        raise ValueError(f"{name} must not be empty")
    for bit in bits:
        if not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1):
            raise ValueError(f"{name} must contain only int 0 or 1, got {bit!r}")
