
def hex_int(x):
    if x >= 10:
        return(chr(ord("A") - 10 + x))
    return(x)


def int2hex(x):
    res = ''
    if not x:
        return('0')
    while x > 0:
        res = str(hex_int(x % 16)) + res
        x //= 16
    return(res)

