
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
s = (inp.readline()).rstrip()
strng = list(s.split(' '))
res = dict()
while len(s):
    for wrd in strng:
        if wrd in res:
            res[wrd] += 1
        else:
            res[wrd] = 1
    s = (inp.readline()).rstrip()
    strng = list(s.split(' '))
outp.write(str((sorted(res.items(), key=lambda x: (-x[1], x[0]))[0][0])))
inp.close()
outp.close()

