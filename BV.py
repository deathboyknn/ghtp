
x, res = input(), 0
for i in range(len(x)):
    res = ord(x[i]) + (res >> 1) + ((res & 1) << 15)
    res &= ((1 << 16) - 1)
print(res)

