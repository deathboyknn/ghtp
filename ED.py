
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
k = int(inp.readline().rstrip())
box = [0] * k
s = inp.readline().rstrip()
while s:
    n = 0
    name, put, out = s.split(' ')
    put = int(put[0:2]) * 60 + int(put[3:5])
    out = int(out[0:2]) * 60 + int(out[3:5])
    while n < k and put < box[n]:
        n += 1
    if n != k:
        box[n] = out
        print(name, n + 1)
    s = inp.readline().rstrip()
inp.close()
outp.close()

