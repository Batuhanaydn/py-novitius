
def find_outlier(integers):
    odd_list = []
    even_list = []
    even = 0
    odd = 0
    
    for i in integers:
        if abs(i) % 2 == 1:
            odd_list.append(i)
        if abs(i) & 2 == 0:
            even_list.append(i)
            
    if len(odd_list) > len(even_list):
        for i in even_list:
            even = even + i
            return even
    if len(even_list) > len(odd_list):
        for i in odd_list:
            odd = odd + i
            return odd


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))