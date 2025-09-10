
def int2bin(x):
    res = ''
    if not x:
        return('0')
    while x > 0:
        res = str(x % 2) + res
        x //= 2
    return(res)

