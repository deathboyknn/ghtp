
def dec_fib(x):
    arr, i = list(x), len(x) - 1
    while i > -1 and (arr[i] == '0'):
        i -= 1
    if len(arr) > 1 and not i:
        arr = arr[1:]
    else:
        arr[i] = '0'
        i += 1
    while i < len(arr):
        arr[i] = '1'
        i += 2
    return(''.join(arr))

