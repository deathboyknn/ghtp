
def dec_ter(x):
    arr, i = list(x), len(x) - 1
    while i >= 0 and arr[i] == '$':
        arr[i] = '1'
        i -= 1
    if i == -1:
        return('$' + ''.join(arr))
    else:
        if arr[i] == '0':
            arr[i] = "$"
        else:
            arr[i] = "0"
        if not i and arr[0] == '0' and len(arr) > 1:
            return(''.join(arr[1:]))
        else:
            return(''.join(arr))

