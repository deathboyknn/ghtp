
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
k = int(inp.readline().rstrip())
pas, res = [0] * (k + 1), []
s = inp.readline().rstrip()
while s:
    inn, out = map(int, (s.split(' '))[2:])
    pas[inn] += 1
    pas[out] -= 1
    s = inp.readline().rstrip()
max_trn, crnt = 0, 0
for i in range(1, k + 1):
    crnt += pas[i]
    if max_trn < crnt:
        max_trn = crnt
        res = [i]
    elif max_trn == crnt:
        res.append(i)
for elem in res:
    print(str(elem) + '-' + str(elem + 1))
inp.close()
outp.close()

