def square_digits(num):
    c = ""
    for i in str(num):
        c = c + str(int(i)**2)
    return int(c)


print(square_digits(9119))