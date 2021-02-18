def positive_sum(a):
    c = []
    for i in a:
        if i > 0:
            c.append(i)
    return sum(c)



print(positive_sum([-1,2,3,4,-5]))