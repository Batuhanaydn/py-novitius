def pattern(n):
    print("1")
    for i in range(2,n+1):
        print("1"+((i-1)*"*")+str(i))
pattern(5)