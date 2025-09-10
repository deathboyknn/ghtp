
def hex2int(x):
    if x >= 'A':
        return(ord(x) - ord('A') + 10)
    return(int(x))


def int2hex(x):
    if x >= 10:
        return(chr(ord("A") + x - 10))
    return(str(x))


def sum_hex(n1, n2):
    if len(n1) > len(n2):
        n1, n2 = n2, n1
    arr = list(n2)
    mod, pls, i = 0, 0, -1
    while -i <= len(n1):
        pls = hex2int(n1[i]) + hex2int(n2[i]) + mod
        arr[i] = int2hex(pls % 16)
        i -= 1
        mod = pls // 16
    while -i <= len(arr) and 0 < mod:
        pls = hex2int(arr[i]) + mod
        arr[i] = int2hex(pls % 16)
        i -= 1
        mod = pls // 16
    if mod == 1 and -i > len(arr):
        return('1' + ''.join(arr))
    return(''.join(arr))




