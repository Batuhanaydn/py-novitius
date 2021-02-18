def score(dice):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    puan = 0
    for i in dice:
        
        if i == 1:
            one += 1
            if one % 3 == 0:
                puan = one //3 *1000
                
            if one < 3:
                puan = one * 100
        if i == 5:
            five += 1
            if five < 3:
                puan = five * 50
            if five % 3 == 0:
                puan = five //3 *500
        if i == 2:
            two += 1
            if two % 3 == 0:
                puan = two //3 *200
        if i == 3:
            three += 1
            if three % 3 == 0:
                puan = three //3 *300
        if i == 4:
            four += 1
            if four % 3 == 0:
                puan = four //3 *400

        if i == 6:
            six += 1       
            if six % 3 == 0:
                puan = six //3 *600
    return puan

        





        
        
    
print(score([5, 4, 3, 4, 4] ))