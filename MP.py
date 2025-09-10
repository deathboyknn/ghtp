
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
s = (inp.readline()).rstrip()
wrds = list(s.split(' '))
res = dict()
while len(s):
    for elem in wrds:
        if elem not in res:
            res[elem] = 0
        else:
            res[elem] += 1
    s = (inp.readline()).rstrip()
    wrds = list(s.split(' '))
for elem in sorted(res.items(), key=lambda x: (-x[1], x[0])):
    outp.write(elem[0] + '\n')
inp.close()
outp.close()

