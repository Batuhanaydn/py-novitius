def remove_url_anchor(year):
    a = ""
    for i in year:
        a += i
        if i == "#":
            break
    a = a.replace("#","")
    return a

print(remove_url_anchor("www.codewars.com/katas/Batuhanaydn#remove"))