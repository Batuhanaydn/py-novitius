alphabet = 'abcdefghijklmnopqrstuvwxyz'

def high_score_word(x):
    if type(x) == str:
        x = x.lower()
        result = ""
        for letter in x:
            if letter.isalpha() == True:
                result = result + " " + str(alphabet.index(letter) + 1)
                return result.lstrip(" ")
            
def high_score_word(x):
    if type(x) == str:
        x = x.lower()
        result = ""
        total = 0
        for letter in x:
            if letter.isalpha() == True:
                result = result + " " + str(alphabet.index(letter) + 1)
                total = total + int(alphabet.index(letter) + 1)
                if total >= total:
                    total = total + int(alphabet.index(letter) + 1)
        return(print(total))
print(high_score_word("Baba taka"))      