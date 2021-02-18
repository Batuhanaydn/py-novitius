import time
import random

def frp_dice():
    print('''Bu Bir frp zar similatörüdür hadi oynayalım...''')
    time.sleep(3)
    devam = True
    dice = input('Ne tür bir zar atmak istersiniz: \n/d4/d6/d8/d10/d12/d20:  ')
    if dice == 'd4':
        while devam:
            zar = random.randint(1,4)
            print(zar)
            tekrar = input('Tekrar atmak istiyor musun? Y/N ')
            if tekrar.upper() == 'Y':
                time.sleep(0.2)
            else:
                devam = False
    elif dice == 'd6':
        while devam:
            zar = random.randint(1,6)
            print(zar)
            tekrar = input('Tekrar atmak istiyor musun? Y/N ')
            if tekrar.upper() == 'Y':
                time.sleep(0.2)
            else:
                devam = False
    elif dice == 'd8':
        while devam:
            zar = random.randint(1,8)
            print(zar)
            tekrar = input('Tekrar atmak istiyor musun? Y/N ')
            if tekrar.upper() == 'Y':
                time.sleep(0.2)
            else:
                devam = False 
    elif dice == 'd10':
        while devam:
            zar = random.randint(1,10)
            print(zar)
            tekrar = input('Tekrar atmak istiyor musun? Y/N ')
            if tekrar.upper() == 'Y':
                time.sleep(0.2)
            else:
                devam = False
    elif dice == 'd12':
        while devam:
            zar = random.randint(1,12)
            print(zar)
            tekrar = input('Tekrar atmak istiyor musun? Y/N ')
            if tekrar.upper() == 'Y':
                time.sleep(0.2)
            else:
                devam = False
    elif dice == 'd20':
        while devam:
            zar = random.randint(1,20)
            print(zar)
            tekrar = input('Tekrar atmak istiyor musun? Y/N ')
            if tekrar.upper() == 'Y':
                time.sleep(0.2)
            else:
                devam = False
    return 'Oyun Bitti...'
print(frp_dice())