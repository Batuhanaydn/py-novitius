def is_prime(n):
    sayac = 0
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                sayac += 1
                break
        if sayac != 0:
            return False
        else:
            return True
        
print(is_prime(23))

