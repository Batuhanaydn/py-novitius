def fib(n):
    if(n == 0 or n == 1):
        return n
    elif (n >= 2 and n % 2 == 0 ):
        k = n / 2
        fk = fib(k)
        return(2*n * fib(k-1)+ fk) * fk
    elif (n >= 2):
        k = (n + 1) / 2
        fk1 = fib(k - 1)
        fk2 = fib(k)
        return fk2*fk2 + fk1+fk1
    else:
        a = 0 * n
        b = 1 * n
        for i in range(n+1):
            a, b = b-a, a
        return a

if __name__== "__main__":
        
    start = 100
    how_many = 1
    for i in range(start+how_many):
        print(fib(i))

