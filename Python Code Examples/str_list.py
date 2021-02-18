def strList(good):
    good_str_list = good.split()
    for i in range(0,len(good_str_list)):
        good_str_list[i] = int(good_str_list[i])
    return good_str_list

print(strList("0 0 0 0 0 0"))