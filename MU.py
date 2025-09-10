
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
res = dict()
s = (inp.readline()).rstrip()
while s:
    nm, obj, sum_ = s.split(' ')
    sum_ = int(sum_) 
    if nm not in res:
        res[nm] = {obj: sum_}
    elif obj not in res[nm]:
        res[nm][obj] = sum_
    else:
        res[nm][obj] += sum_
    s = (inp.readline()).rstrip()
for i in sorted(res.items()):
    outp.write(i[0] + ":\n")
    for j in sorted(i[1].items()):
        outp.write(j[0] + ' ' + str(j[1]) + '\n')
inp.close()
outp.close()




