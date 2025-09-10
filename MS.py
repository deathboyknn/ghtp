
res, trns = dict(), ""
for _ in range(int(input())):
    wrds = list(input().split(", "))
    trns, wrds[0] = wrds[0].split(" - ")
    for elem in wrds:
        if elem not in res:
            res[elem] = [trns]
        else:
            res[elem].append(trns)
print(len(res))
for i in res:
    res[i].sort()
for i in sorted(res.items()):
    print(i[0] + " - " + i[1][0], end="")
    if len(i[1]) != 1:
        for j in i[1][1::]:
            print(", " + j, end="")
    print('')

