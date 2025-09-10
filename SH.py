
def hex_bin(x):
    res = ""
    x = x = ord(x) - ord('A') + 10 if x >= 'A' else int(x)
    for _ in range(4):
        res = str(x % 2) + res
        x //= 2
    return(res)


def hex2bin(x):
    cnt, res = 0, ""
    if x == '0':
        res = '0'
    cnt = ord(x[0]) - ord('A') + 10 if x[0] >= 'A' else int(x[0])
    while cnt > 0:
        res = str(cnt % 2) + res
        cnt //= 2
    for i in range(1, len(x)):
        res += hex_bin(x[i])
    return(res)

