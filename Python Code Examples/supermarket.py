def queue_time(customers, n):
    l=[0]*n
    print(l)
    for i in customers:
        l[l.index(min(l))]+=i
        print(l)
    return max(l)

print(queue_time([5,4,3,2,1],2))