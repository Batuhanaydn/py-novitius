import random
def number_guess(a):
    guess = random.randint(1,100)
    b = True
    while b:
        
        a = int(input("Sayıyı Gir: "))    
        if a == guess:
            print("Doğru Sayı")
            b = False
        if a < guess:
            print("Sayıyı yükselt")
        if a > guess:
            print("Sayıyı Küçült")
print(number_guess(4))