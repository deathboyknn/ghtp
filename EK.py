
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
cur = [0] * 7
s = inp.readline().rstrip()
min_, cnt = 0, 0
while s:
    num = float(s)
    cnt += 1
    if cnt <= 7:
        for i in range(6):
            cur[i] = cur[i + 1]
        cur[6] = num
        if cnt == 7:
            min_ = cur[6] * cur[0]
    else:
        cur[0] = min(cur[0], cur[1])
        for i in range(1, 6):
            cur[i] = cur[i + 1]
        cur[6] = num
        min_ = min(min_, cur[0] * cur[6])
    s = inp.readline().rstrip()
print(min_)
inp.close()
outp.close()

