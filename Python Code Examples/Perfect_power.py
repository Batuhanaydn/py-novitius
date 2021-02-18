
from math import log, sqrt
def isPP(n):
    n = int(n)
    if n < 4: return None
    sr = round(sqrt(n),6)
    if sr == round(sr): return [int(sr), 2]
    for m in range(2,n/2):
        k = round(log(n, m),6)
        if k == round(k): return [int(m), int(k)]
    return None

print(isPP(100))