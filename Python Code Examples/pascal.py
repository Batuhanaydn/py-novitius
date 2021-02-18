import math

pascals_tri_formula = []

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y):
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    count = 0
    while count <= rows-1:
        for element in range(count + 1):
            [pascals_tri_formula.append(combination(count, element))]
        count += 1
    return pascals_tri_formula
pascals_triangle(4)

print(pascals_tri_formula)