def sezar(metin, a):
    cıktı = ""

    for i in range(len(metin)):
        char = metin[i]

        if (char.isupper()):
            cıktı += chr((ord(char)+ a-65) % 26 + 65)

        else:
            cıktı += chr((ord(char)+ a-97) % 26 + 97)

    return cıktı

print(sezar("kafa sozluk", 0))