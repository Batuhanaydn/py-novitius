def hydrate(drink_string): 
    toplam = 0
    a = drink_string.split()
    
    for i in a:
        if i.isdigit() == True:
            toplam = toplam + int(i)
    if toplam == 1:
        return str(toplam) + ' glass of water'
    return str(toplam) + ' glasses of water'
                
print(hydrate("1 shot"))