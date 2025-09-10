
def inc_ter(x):
    arr = list(x)
    i = len(x) - 1
    while i >= 0 and arr[i] == '1':
        arr[i] = '$'
        i -= 1
    if i == -1:
        return('1' + ''.join(arr))
    else:
        if arr[i] == '$':
            arr[i] = "0"
        else:
            arr[i] = "1"
        if not i and arr[0] == '0' and len(arr) > 1:
            return(''.join(arr[1:]))
        else:
            return(''.join(arr))

