def get_missing_element(seq):
    toplam = 45
    return -1*(sum(seq) - toplam)

print(get_missing_element([0,5,1,3,2,9,7,6,8]))