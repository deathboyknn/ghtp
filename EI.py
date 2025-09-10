
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
s = inp.readline().rstrip()
bal = [0] * 101
N = 0
while s:    
    bal[int((s.split(' '))[-1])] += 1
    N += 1
    s = inp.readline().rstrip()
N = (N * 45) // 100 
cnt, res = 0, 0
n = 100
while cnt < N:
    if bal[n]:
        if N < cnt + bal[n]:
            if 50 < n:
                res = n
        else:
            res = n
        cnt += bal[n]
    n -= 1
print(res)
inp.close()
outp.close()

