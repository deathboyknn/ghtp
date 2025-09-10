
n, k = map(int, input().split())
res = set()
ppl = []
for i in range(k):
    ppl.append(tuple(map(int, input().split())))
for i in set(ppl):
    x, y = i[0], i[1]
    for j in range(((n - x) // y) + 1):
        if (x + j * y) % 7 != 0 and (x + j * y) % 7 != 6:
            res.add(x + j * y)
print(len(res))

