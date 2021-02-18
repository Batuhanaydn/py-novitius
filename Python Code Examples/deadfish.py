def parse(data):
    basla = 0
    basla_list = []
    for i in data:
        for a in range(len(i)):
            if i[a] == "i":
                basla += 1
            if i[a] == "d":
                basla -= 1
            if i[a] == "s":
                basla = basla **2
            if i[a] == "o":
                basla_list.append(basla)
    return basla_list

print(parse("codewars"))
