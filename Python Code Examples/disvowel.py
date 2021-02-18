# # # # # # # # # # # def anti_vowel (text):  
# # # # # # # # # # #     letters = []
# # # # # # # # # # #     for char in text:
# # # # # # # # # # #         if char not in "aeiouAEOU":
# # # # # # # # # # #             letters.append(char)
# # # # # # # # # # #     return "".join(letters)

# # # # # # # # # # # print(disemvower("asddsadli"))

# # # # # # # # # # def disemvowel(s):
# # # # # # # # # #     return s.translate(None, "aeiouAEIOU")
# # # # # # # # # def disemvowel(string):
# # # # # # # # #     return "".join(c for c in string if c.lower() not in "aeiou")

# # # # # # # # def disemvowel(s):
# # # # # # # #     for i in "aeiouAEIOU":
# # # # # # # #         s = s.replace(i,'')
# # # # # # # #     return s

# # # # # # # import re
# # # # # # # def disemvowel(string):
# # # # # # #     return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

# # # # # # def disemvowel(string):
# # # # # #     return string.translate(None, 'aeiouAEIOU')


# # # # # def disemvowel(str2handle):
# # # # #     vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
# # # # #     str2return = ""
# # # # #     i = 0
# # # # #     n = len(str2handle)
# # # # #     while i < n:
# # # # #         if not str2handle[i] in vowel_character:
# # # # #             str2return += str2handle[i]
# # # # #         i += 1
# # # # #     return str2return

# # # # def disemvowel(string):
# # # #     return string.translate(None, 'aeiuoAEIOU')

# # # import re

# # # def disemvowel(string):
# # #     return re.sub(r"[aeiouAEIOU]", "", string)

# # def disemvowel(string):
        
# #     s = ""
# #     for c in string:
# #         if c.lower() not in "aeiou":
# #             s += c
# #     return s

# def disemvowel(string):
#     vowels = 'aeiouAEIOU'
#     new_string = ''
#     for i in string:
#         if i not in vowels:
#             new_string+= i 
#     return new_string


