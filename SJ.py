
def str_int(x):
    if x == '$':
        return(-1)
    return(int(x))


def ter2int(x):
    sum_ = 0
    for elem in x:
        sum_ = 3 * sum_ + str_int(elem)
    return(sum_)

