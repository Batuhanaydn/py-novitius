def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))