
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
n = int((inp.readline()).rstrip())
res = dict()
for i in range(n):
    s = (inp.readline()).rstrip()
    wrds = list(s.split(' '))
    res[wrds[0]] = []
    for j in range(1, len(wrds)):
        if wrds[j] == "X":
            wrds[j] = "execute"
        elif wrds[j] == "R":
            wrds[j] = "read"
        else:
            wrds[j] = "write"
        res[wrds[0]].append(wrds[j])    
m = int(inp.readline().rstrip())
x, crnt = "", ""
for i in range(m):
    s = (inp.readline()).rstrip()
    x, crnt = s.split(' ')
    if x in res[crnt]:
        outp.write("OK" + '\n')
    else:
        outp.write("Access denied" + '\n')
inp.close()
outp.close()

