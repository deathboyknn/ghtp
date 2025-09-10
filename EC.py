
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
sum_, mdf = 0, 10001
s = inp.readline().rstrip()
while s:
    x, y = map(int, s.split())
    sum_ += max(x, y)
    if abs(x - y) < mdf and abs(x - y) % 3:
        mdf = abs(x - y)
    s = inp.readline().rstrip()
if not (sum_ % 3):
    if mdf != 10001:
        sum_ -= mdf
    else:
        sum_ = 0
print(sum_)
inp.close()
outp.close()

