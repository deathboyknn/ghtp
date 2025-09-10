
def str_int(x):
    if x >= 'A':
        return(ord(x) - ord('A') + 10)
    return(int(x))


def int_str(x):
    if x >= 10:
        return(chr(ord("A") + x - 10))
    return(str(x))


def dec(res, n):
    arr, n = list(res), int_str(n - 1)
    i = len(res) - 1
    while i >= 0 and arr[i] == '0':
        arr[i] = n
        i -= 1
    if i == -1:
        res = '-1'
    if len(res) != 1 and not i:
        res = ''.join(arr[1::])
    else:
        arr[i] = int_str(str_int(arr[i]) - 1)
        res = ''.join(arr)
    return(res)

