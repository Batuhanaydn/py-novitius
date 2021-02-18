# # def get_sum(a,b):
# #     sum_a_b = 0 
# #     if a == 0:
# #         a = -1
# #     for i in range(a,b+1):
# #         if a == b:
# #             print(a)
# #             break
# #         else:
# #             sum_a_b += i
# #     return sum_a_b
# # print(get_sum(0,-1))

# # def get_sum(a,b):
# #     suma = 0
# #     sumb = 0
# #     if a < b or a == b:    
# #         for i in range(a, b+1, 1):
# #             if a == b:
# #                 print(a)
# #             else:
# #                 suma = suma + i
# #         return suma
# #     if a > b or a == b:
# #         a, b = b, a        
# #         for c in range(a, b+1,1):
# #             if a == b:
# #                 print(a)
# #             else:
# #                 sumb = sumb + c
# #         return sumb
# # print(get_sum(1,-3))

#     def get_sum(a,b):
#         sum1 = []
#         sum2 = []
#         if a < b:
#             for i in range(a,b+1):
#                 sum1.append(i)
#             toplam1 = sum(sum1)
#             return toplam1
#         if a > b:
#             a, b = b, a
#             for x in range(a,b+1):
#                 sum2.append(x)
#             toplam2 = sum(sum2)
#             return toplam2
#         if a == b:
#             return a
#     print(get_sum(3,-3))