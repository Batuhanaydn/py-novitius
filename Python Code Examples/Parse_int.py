def parse_int(string):
    numbers = {
        "zero" : 0,
        "one"  : 1,
        "two"  : 2,
        "three": 3,
        "four" : 4,
        "five" : 5,
        "six"  : 6,
        "seven": 7,
        "eight": 8,
        "nine" : 9
        "ten"  : 10,
        "twenty": 2
    }
    a = []
    for i in numbers.keys():
        a.append(i)
        if string == i:
            return len(a)-1

print(parse_int("ten"))