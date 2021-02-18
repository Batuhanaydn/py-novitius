def high_and_low(numbers):
    total = []
    a = numbers.split()
    for h in a:
        total.append(int(h))
    low = total[0]
    high = total[0]
    for i in total:
    
        if i < low:
            low = i
        if i > high:
            high = i


    return str(high)+ " "+ str(low)

print(high_and_low("4 5 29 54 4 214 542 64  1 9 6"))
