
def str_int(x):
    if x >= 'A':
        return(ord(x) - ord('A') + 10)
    return(int(x))


def int_str(x):
    if x >= 10:
        return(chr(ord("A") + x - 10))
    return(str(x))


def inc(res, n):
    n = int_str(n - 1)
    arr = list(res)
    i = len(res) - 1
    while i >= 0 and arr[i] == n:
        arr[i] = '0'
        i -= 1
    if i == -1:
        res = "1" + ''.join(arr)
    else:
        arr[i] = int_str(str_int(arr[i]) + 1)
        res = ''.join(arr)
    return(res)

