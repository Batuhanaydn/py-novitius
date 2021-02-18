x = 20000
y = 54564

def iterative_multipy(x,y):
    z = 0
    for i in range(1,y):
        z = z + (i * x)
    return z
print(iterative_multipy(x,y))