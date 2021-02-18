def multiplication_table(n):
    m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
    for i in m:
        i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
        a = ''.join(i)
        return a
multiplication_table(3)