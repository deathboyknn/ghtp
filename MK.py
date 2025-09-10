
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
wrds = dict()
s = (inp.readline()).rstrip()
while len(s):
    line = list(s.split(" "))
    s = (inp.readline()).rstrip()
    for elem in line:
        if elem in wrds:
            wrds[elem] += 1
            outp.write(str(wrds[elem]) + ' ')
        else:
            outp.write("0 ")
            wrds[elem] = 0
inp.close()
outp.close()

