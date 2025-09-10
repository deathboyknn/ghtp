
n = int(input())
res = set(range(1, n + 1))
pos, strng = "", input()
while strng != "HELP":
    pos = input()
    strng = set(map(int, strng.split(' ')))
    if pos == "YES":
        res &= strng
    else:
        res -= strng
    strng = input()
for elem in sorted(res):
    print(elem, end=' ')

