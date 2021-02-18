# # # # def descending_order(num):
# # # #     c = []
# # # #     a = ""
# # # #     for i in str(num):
# # # #         c.append(i)
# # # #         c = sorted(c)
# # # #         c.reverse()
# # # #     for b in c:
# # # #         a = a + b
# # # #     return int(a)
# # # # print(descending_order(152))

# # # def Descending_Order(num):
# # #     return int("".join(sorted(str(num), reverse=True)))

# # def Descending_Order(num):
# #     s = str(num)
# #     s = list(s)
# #     s = sorted(s)
# #     s = reversed(s)
# #     s = ''.join(s)
# #     return int(s)

# def Descending_Order(num):
#     return int(''.join(sorted(str(num))[::-1]))
