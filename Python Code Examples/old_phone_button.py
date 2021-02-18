def presses(press):
    one_press = ["A","D","G","J","M","P","T","W"," ","*","#","a","d","g","j","m","p","t","w","1"]
    two_press = ["B","E","H","K","N","Q","U","X","0","b","e","h","k","n","q","u","x"]
    three_press = ["C","F","I","L","O","R","V","Y","c","f","ı","l","o","r","v","y"]
    four_press = ["S","Z","s","z","2","3","4","5","6","7","8","9"]
    presses_total = 0
    for i in press:
        for one in one_press:
            if i == one:
                presses_total += 1
        for two in two_press:
            if i == two:
                presses_total += 2           
        for three in three_press:
            if i == three:
                presses_total += 3
        for four in four_press:
            if i == four:
                presses_total += 4
    return presses_total

print(presses("WHERE DO U WANT 2 MEET L8R"))

        