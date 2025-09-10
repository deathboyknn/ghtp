
def fb(x):
    f1, f2 = 1, 2
    res = [1]
    while f2 <= x:
        f2 += f1
        f1 = f2 - f1
        res.append(f1)
    return(res)


def int2fib(x):
    fbl = fb(x)
    i = len(fbl)
    res = ['0'] * i
    i -= 1
    while x != 0 and 0 <= i:
        if fbl[i] <= x:
            res[-i - 1] = '1'
            x -= fbl[i]
        i -= 1
    return(''.join(res))

