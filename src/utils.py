def is_vowel(c: str) -> bool:
    return c.lower() in ['а', 'є', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']


def word_to_bits(word1):
    return [1 if is_vowel(c) else 0 for c in word1]


def fill_zeros_to_size(array, size):
    while len(array) != size:
        array.append(0)


def inverse_bit(bits, i):
    x = bits.copy()
    x[i] = int(not x[i])
    return x


def get_fullname_vectors(fullname_vector):
    word1, word2, word3 = sorted(fullname_vector,
                                 key=lambda x: len(x),
                                 reverse=True)
    word1_bits = word_to_bits(word1)
    word2_bits = word_to_bits(word2)
    word3_bits = word_to_bits(word3)
    fill_zeros_to_size(word2_bits, len(word1_bits))
    fill_zeros_to_size(word3_bits, len(word1_bits))

    v1 = word1_bits
    v4 = word2_bits
    v5 = word3_bits

    v2 = inverse_bit(v1, -3)
    v3 = inverse_bit(v1, -4)
    v6 = inverse_bit(v4, -3)
    v7 = inverse_bit(v4, -4)
    v8 = inverse_bit(v5, -3)
    v9 = inverse_bit(v5, -4)

    return v1, v2, v3, v4, v5, v6, v7, v8, v9


def get_initial_weights():
    return [
        [0.1, 0.2, 0.3],
        [0.1, 0.2, 0.3],
        [0.1, 0.2, 0.3],
        [0.1, 0.5, 0.3],
        [0.8, 0.7, 0.3],
        [0.9, 0.2, 0.2],
        [0.0, 0.6, 0.6],
        [0.2, 0.6, 0.5],
        [0.3, 0.3, 0.3],
        [0.1, 0.2, 1.0],
    ]
