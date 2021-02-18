
def validPhoneNumber(number):
    number_list = []
    for i in number:
        number_list.append(i)
    if len(number_list) == 14 and number_list[1] != "0" and number_list[0] == "(" and number_list[4] == ")" and number_list[9] == "-":
        return True
    else:
        return False

        

print(validPhoneNumber("(123) 456-7890"))


def validPhoneNumber(phoneNumber):
    number = ''
    template = '(xxx) xxx-xxxx'
    for l in phoneNumber:
        if l.isdigit():
            number += 'x'
        else:
            number += l
    
    return number == template


import re

def validPhoneNumber(phoneNumber):
    return any(re.findall("^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$", phoneNumber))



import re
def validPhoneNumber(phoneNumber):
    if re.fullmatch('\(\d{3}\)\s\d{3}\-\d{4}', phoneNumber):
        return True
    else:
        return False