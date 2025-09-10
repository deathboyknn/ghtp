
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
bal = [0] * 301
k = int(inp.readline().rstrip())
s = inp.readline().rstrip()
while s:
    ex1, ex2, ex3 = map(int, (s.split(' '))[2:])
    if min(ex1, ex2, ex3) >= 40:
        bal[ex1 + ex2 + ex3] += 1
    s = inp.readline().rstrip()
n, res = 300, 300
cnt = 0
while cnt <= k and n >= 120:
    if bal[n] > k and cnt == 0:
        cnt = k + 1
        res = 1
    elif bal[n] != 0:
        if cnt + bal[n] <= k:
            res = n
        cnt += bal[n]
    n -= 1
if cnt <= k:
    res = 0
print(res)
inp.close()
outp.close()

