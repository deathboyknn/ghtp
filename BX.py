
x, res = input(), 14695981039346656037
for i in range(len(x)):
    res = ((res * 1099511628211) & ((1 << 64) - 1)) ^ ord(x[i])
print(res)




