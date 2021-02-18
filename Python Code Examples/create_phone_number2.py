# def create_phone_number(number):
#     number.insert(0,"(")
#     number.insert(4,")")
#     number.insert(5," ")
#     number.insert(9,"-")
#     c = ""
#     for i in number:
#         c = c + str(i)
#     return c



# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# En akıllıca Çözüm

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))