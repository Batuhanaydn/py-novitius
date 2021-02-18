def adjacent_element_product(arry):
    b = []
    for a in range(len(arry)):
        b.append(arry[a] * arry[a-1])
    b.pop(0)
    return max(b)


print(adjacent_element_product([1, 0, 1, 0, 1000]))

