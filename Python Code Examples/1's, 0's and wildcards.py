# # from itertools import product

# # def possibilities(pattern):
# #     pattern_format = pattern.replace('?', '{}')
# #     return [pattern_format.format(*values) for values in product('10', repeat=pattern.count('?'))]

# def possibilities(param):
#     results = [param]
#     while '?' in results[0]:
#         new_results = []
#         for x in results:
#             new_results.append(x.replace('?', '0', 1))
#             new_results.append(x.replace('?', '1', 1))
#             new_results.append(x.replace('?', '2', 1))

#         results = new_results[:]
#     return len(results)

# print(possibilities("100000111?1?????????????1"))
