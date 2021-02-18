import random
import time

def intro():
    print("Oyun taş kağıt makas oyunudur. Hadi oynayalım...")

def play():
    secenekler = ['tas','kagıt','makas']
    devam = True
    pc_point = 0
    your_point = 0
    tekrar = 3
    while devam and tekrar > 0:
        pc = random.choice(secenekler)
        choice = input('Taş kağıt makas?\n>>>')
        time.sleep(1)
        if choice.lower() == "tas" and pc == "tas":
            pc_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "tas" + ' bilgisayarın seçimi' + " tas")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')
        if choice.lower() == "kagıt" and pc == "kagıt":
            pc_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "kagıt" + ' bilgisayarın seçimi' + " kagıt")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "makas" and pc == "makas":
            pc_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "makas" + ' bilgisayarın seçimi' + " makas")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "tas" and pc == "kagıt":
            pc_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "tas" + ' bilgisayarın seçimi' + " kagıt")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "tas" and pc == "makas":
            your_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "tas" + ' bilgisayarın seçimi ' + "makas")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "makas" and pc == "kagıt":
            your_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "makas" + ' bilgisayarın seçimi ' + "kagıt")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "kagıt" and pc == "tas":
            your_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "kagıt" + ' bilgisayarın seçimi ' + "tas")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "makas" and pc == "tas":
            pc_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "makas" + ' bilgisayarın seçimi ' + "tas")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if choice.lower() == "kagıt" and pc == "makas":
            pc_point += 1
            tekrar -= 1
            print('Senin seçimin ' + "kagıt" + ' bilgisayarın seçimi ' + "makas")
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if pc_point == 3:
            print('kaybettiniz')
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if your_point == 3:
            print('kazandınız')
            print(f'skorlar ----- You= {your_point} pc point = {pc_point}')

        if tekrar == 0:
            repeat = input('tekrar Oynamak ister misiniz Y/N')
            if repeat.upper() == 'Y':
                return play()
            else:
                devam = False
intro()
play()  
