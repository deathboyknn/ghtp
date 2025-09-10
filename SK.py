
def fb(x):
    f1, f2 = 1, 1
    for _ in range(x):
        f2 += f1
        f1 = f2 - f1
    return(f2)


def fib2int(x):
    x, sum_ = x[::-1], 0
    for i in range(len(x)):
        if x[i] == '1':
            sum_ += fb(i)
    return(sum_)

