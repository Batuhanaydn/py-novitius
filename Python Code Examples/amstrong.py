def narcissistic(value):
    

    basamak = str(value)

    toplam=0

    for x in basamak:
        
        rakam = int(x)**len(basamak)
        toplam += rakam 
        
    if(value == toplam):
        return True
    else:
        return False
print(narcissistic(48877572545644646654645645))