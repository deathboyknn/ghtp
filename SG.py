
def int_str(x):
    if x >= 10:
        return(chr(ord("A") - 10 + x))
    return(x)


def str_int(x):
    if x >= 'A':
        return(10 + ord(x) - ord('A'))
    return(x)


def int2str(a, n):
    res = ''
    if a == 0:
        res = '0'
    while a > 0:
        res = str(int_str(a % n)) + res
        a //= n
    return(res)


def str2int(a, n):
    sum_ = 0
    for elem in a:
        sum_ = n * sum_ + int(str_int(elem))
    return(sum_)


n = int(input())
a = input()
print(int2str(str2int(a, n), int(input())))

