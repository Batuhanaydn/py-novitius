def get_middle(s):
    s_list = []
    for i in s:
        s_list.append(i)

    if len(s) % 2 == 1:
        mid = len(s)//2 
        return s_list[mid]
    if len(s) % 2 == 0:
        mid = len(s)//2 
        return s_list[mid-1]+s_list[mid]

print(get_middle("of"))

# def get_middle(s):
#    return s[(len(s)-1)/2:len(s)/2+1]
    