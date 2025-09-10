
inp = open('input.txt', 'r')
outp = open('output.txt', 'w')
s = (inp.readline()).rstrip()
wrds = list(s.split(' '))
sn = dict()
while len(s) and len(wrds) != 1:
    sn[wrds[0]], sn[wrds[1]] = wrds[1], wrds[0]
    s = (inp.readline()).rstrip()
    wrds = list(s.split(' '))
while len(s):
    print(sn[s])
    s = (inp.readline()).rstrip()
inp.close()
outp.close()

