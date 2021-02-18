# import string

# def is_pangram(s):
#     alphabet = string.ascii_lowercase
#     for char in alphabet:
#         if char not in s.lower():
#             return False
#         return True

# if is_pangram("The quick, brown fox jumps over the lazy dog!") == True:
#     print(True)
# else:
#     print(False)


import string

def is_pangram(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in s:
            return False
    return True
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))