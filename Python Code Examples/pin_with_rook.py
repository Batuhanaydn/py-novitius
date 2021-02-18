def pin_rook(K, B):
    return [f'R{f}{r}'
        for r in '12345678'
        for f in 'abcdefgh'
        if K[2] == B[2] == r and (K[1] < B[1] < f or f < B[1] < K[1])
        or K[1] == B[1] == f and (K[2] < B[2] < r or r < B[2] < K[2])]

print(pin_rook("Kb2", "Bb3"))