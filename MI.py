
n = int(input())
all, onl, cur = set(), set(), set()
for i in range(n):
    m = int(input())
    for j in range(m):
        lng = input()
        onl.add(lng)
        cur.add(lng)
        if i == 0:
            all.add(lng)
        if j == m - 1:
            all &= cur
            cur = set()
print(len(all))
for i in all:
    print(i)
print(len(onl))
for i in onl:
    print(i)

