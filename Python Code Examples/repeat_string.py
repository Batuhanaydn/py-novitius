from math import sqrt


def find_next_square(sq):
    if sq == 0:
        return -1
    elif sq % sqrt(sq) == 0:
        return int((sqrt(sq) + 1) ** 2)
    else:
        return -1
print(find_next_square(16))  