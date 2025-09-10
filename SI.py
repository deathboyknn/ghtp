
def bin_hex(x):
    sum_ = 0
    for i in range(4):
        sum_ = 2 * sum_ + int(x[i])
    if sum_ >= 10:
        return(chr(-10 + ord("A") + sum_))
    return(str(sum_))


def bin2hex(x):
    res, sum_, dvln4 = "", 0, len(x) % 4
    if dvln4 != 0:
        for elem in x[:dvln4]:
            sum_ = 2 * sum_ + int(elem)
        if sum_ >= 10:
            res = chr(ord("A") + sum_ - 10)
        else:
            res = str(sum_)
    for i in range((len(x) - dvln4) // 4):
        res += bin_hex(x[(dvln4 + i * 4):(dvln4 + (i + 1) * 4)])
    return(res)

