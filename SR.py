
def inc_fib(x):
    arr, i = list(x), len(x) - 1
    while i > -1 and ((arr[i - 1] == '1') | (arr[i] == '1')):
        i -= 1
        arr[i + 1] = '0'
    if i < 0:
        return('1' + ''.join(arr))
    arr[i] = '1'
    return(''.join(arr))

