
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
nmb = [0] * 4
crnt, div29, i, res = 0, 0, 0, 0
s = inp.readline().rstrip()
for i in range(4):
    nmb[i] = int(s)
    s = inp.readline().rstrip()
i += 1
while s:
    crnt = int(s)
    i += 1
    if nmb[0] % 29 == 0:
        div29 += 1
    for j in range(3):
        nmb[j] = nmb[j + 1]
    nmb[3] = crnt
    if not crnt % 29:
        res += i - 4
    else:
        res += div29
    s = inp.readline().rstrip()
print(res)   
inp.close()
outp.close()




