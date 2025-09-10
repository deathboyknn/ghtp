
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
res = dict()
s = (inp.readline()).rstrip()
while len(s):
    nm, cnt = s.split(" ")
    if nm not in res:
        res[nm] = int(cnt)
    else:
        res[nm] += int(cnt)
    s = (inp.readline()).rstrip()
for elem in sorted(res):
    outp.write(elem + ' ' + str(res[elem]) + '\n')
inp.close()
outp.close()

