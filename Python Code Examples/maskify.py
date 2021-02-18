def maskify(cc):
    lena = len(cc)
    b = []
    b.append(cc)
    c = lena - 4
    if lena < 4:
        return cc

    else:
        return "#"*c + cc[c:]

print(maskify("12345"))