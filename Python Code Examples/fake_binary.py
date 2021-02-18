def fake_binary(x):
    suma = ""
    for i in x:
        if int(i) < 5:
            i = "0"
            suma += i
        if int(i) >= 5:
            i = "1"
            suma += i
    return suma

print(fake_binary("8899001155"))