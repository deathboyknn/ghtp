
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
mod2, mod13, mod26 = 0, 0, 0
ttl = 0
s = inp.readline().rstrip()
while s:
    crnt = int(s)
    if crnt % 26 == 0:
        mod26 += 1
    elif crnt % 2 == 0:
        mod2 += 1
    elif crnt % 13 == 0:
        mod13 += 1
    ttl += 1
    s = inp.readline().rstrip()
print(mod2 * mod13 + (2 * ttl - mod26 - 1) * (mod26) // 2)
inp.close()
outp.close()

