u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = 'abcdefghijklmnopqrstuvwxyz'
d = '0123456789'
x = '!@#$%^&*?'
def check_password(s):
    if len(s)<8 : return 'not valid'
    if len(s)>20: return 'not valid'
    if any(c not in u+l+d+x for c in set(s)) : return 'not valid'
    if all(any(c in e for c in set(s)) for e in (u, l, d, x)) : return 'valid'
    return 'not valid'

print(check_password("12346A!a5789"))