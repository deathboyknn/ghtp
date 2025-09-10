
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
cnt = [0] * 26
res, x = "", ''
flag = True
let = inp.read(1)
while let != '\n':
    cnt[ord(let) - ord('A')] += 1
    let = inp.read(1)
for i in range(26):
    res += chr(i + ord('A')) * (cnt[i] // 2)
    cnt[i] -= (cnt[i] // 2) * 2
    if flag and cnt[i] == 1:
        x = chr(i + ord('A'))
        flag = False
print(res + x + res[::-1])
inp.close()
outp.close()

