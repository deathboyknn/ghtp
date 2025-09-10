
wrd, key = [], ""
err, hp = 0, 0
res = dict()
for i in range(int(input())):
    wrd = input()
    if wrd.lower() not in res:
        res[wrd.lower()] = [wrd]
    else:
        res[wrd.lower()].append(wrd)
for i in list(input().split()):
    key = i.lower()
    if key in res:
        if i not in res[key]:
            err += 1
    else:
        hp = 0
        for j in range(len(key)):
            if key[j] != i[j]:
                hp += 1
        if hp != 1:
            err += 1
print(err)

