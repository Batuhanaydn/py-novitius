import re
def to_underscore(name):
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name

to_underscore(str('TestController'))    