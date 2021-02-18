def validate(n):
    summ, odd = 0, 1
    while n:
        d = n % 10
        n = n // 10
        if odd % 2 == 0:
            d *= 2
            if d > 9:
                d = d - 9
        summ += d
        odd += 1
    return summ % 10 == 0