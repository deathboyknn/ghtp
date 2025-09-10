
x, y = (input()).split("~")
sum_ = 0
for i in range(len(y)):
    sum_ += (int(y[-i - 1]) << i)
print(-((1 << len(y)) - sum_) if x == '1' else sum_)

