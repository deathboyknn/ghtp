
n = int(input())
res = set(range(1, n + 1))
strng = input()
while strng != "HELP":
    strng = set(map(int, strng.split(' ')))
    if len(res & strng) <= len(res) // 2:
        res -= strng
        print("NO")
    else:
        res &= strng
        print("YES")
    strng = input()
for elem in sorted(res):
    print(elem, end=' ')

