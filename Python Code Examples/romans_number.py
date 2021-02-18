class RomanNumerals:
    def to_roman(num):
        val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
            ]
        syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


    def from_roman(s):
        d = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
        n = [d[i] for i in s.lower() if i in d]
        return sum([i if i>=n[min(j+1, len(n)-1)] else -i for j,i in enumerate(n)])

print(RomanNumerals.from_roman('MMVIII'))
print(RomanNumerals.to_roman(1990))