def digital_root(n):
    toplam = 0
    
    for i in str(n):
        toplam += int(i)
    a = len(str(toplam))
    if a > 1:
        n = toplam
        return digital_root(n)
    else:
        return toplam
print(digital_root(3333))

