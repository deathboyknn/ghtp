
def int2ter(x):
    res = ""
    if x == 0:
        res = '0'
    while x != 0:
        if x % 3 == 2:
            res = "$" + res
            x += 1
        else:
            res = str(x % 3) + res
        x //= 3
    return(res)

