
def hex_int(x):
    if x >= 'A':
        return(10 + (ord(x) - ord('A')))
    return(int(x))


def hex2int(x):
    sum_ = 0
    for elem in x:
        sum_ = 16 * sum_ + hex_int(elem)
    return(sum_)

