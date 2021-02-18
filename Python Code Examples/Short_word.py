def find_short(n):
    c = []
    n = n.split()
    for i in n:
        c.append(len(i))
    return min(c)

print(find_short("bitcoin take over the world maybe who knows perhaps"))

def find_short(s):
    return min(len(x) for x in s.split())

def find_short(s):
    return min(map(len, s.split(' ')))

def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length

def find_short(s):
    sList = s.split()
    shortestLength = len(sList[0])
    for item in sList:
        if len(item) < shortestLength:
            shortestLength = len(item)
    return shortestLength
c = []
def divisors(n):
    
    for i in range(1,n+1):
        if n % i == 0:
            c.append(i)
    

    if len(c) > 2:
        return c[1:len(c)-1]
    else:
        return f"{n} is prime"
    

print(divisors(25))