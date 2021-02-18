from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
  print(f(10))

#so fast solve