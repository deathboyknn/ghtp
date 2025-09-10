
n, m = map(int, input().split())
a, b = set(), set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
x = 0
ab = sorted(list(a & b))
a, b = sorted(list(a - b)), sorted(list(b - a))
print(len(ab))
for elem in ab:
    print(elem, end=' ')
print('')
print(len(a))
for elem in a:
    print(elem, end=' ')
print('')
print(len(b))
for elem in b:
    print(elem, end=' ')

