
def substitute(key):
    temp=''
    for i in key:
        temp+=chr(ord(i)+3)
    return temp

def reverse(key):
    temp = key
    return temp[::-1]


def substitute1(key):
    temp=''
    for i in key:
        temp+=chr(ord(i)-3)
    return temp


def scrmbl(key):
    temp = substitute(key)
    temp = reverse(temp)
    return temp

def dscrmbl(key):
    temp = substitute1(key)
    temp = reverse(temp)
    return temp 




