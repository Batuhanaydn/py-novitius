def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])

print(repeats([4,5,5,4,7,8])) 
    