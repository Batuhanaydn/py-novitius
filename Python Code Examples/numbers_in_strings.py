import re


def solve(s):
    return max(map(int,re.findall(r"(\d+)", s)))

print(solve("dsadsa56464dsadds45dsadsa8dsd5dsa1sa5d4sad5a554dsa545ds5a4dsads8ad7a"))