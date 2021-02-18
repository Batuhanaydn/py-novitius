import random as rd
def yazi_tura(n):
    ilk = []
    oynanma_sayisi = 1
    liste = ['yazi' ,'tura']
    
    for i in range(n):
        a = rd.choice(liste)
        print(a)
        ilk.append(a)
        if ilk[0] == 'yazi' and (ilk[i] == 'tura' or ilk[i] == 'dik'):
            break
        elif ilk[0] == 'tura' and (ilk[i] == 'yazi' or ilk[i] == 'dik'):
            break
        # elif ilk[0] == 'dik' and (ilk[i] == 'tura' or ilk[i] == 'yazi'):
        #     break
        else:
            oynanma_sayisi +=1
    return oynanma_sayisi


    

print(yazi_tura(16))