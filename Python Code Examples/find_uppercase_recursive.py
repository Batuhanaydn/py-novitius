def solve(input_str, idx = 0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str)-1:
        return False
    return solve(input_str,idx+1)

print(solve("BatuhanAYdın"))

def solve(input_str):
    for i in range(len(input_str)):
        for a in input_str:
            if a[i].isupper():
                print(a[i])  
                print(a[i])
        return a[i].islower()

print(solve("BATUHAN"))