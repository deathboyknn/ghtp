
a, k = map(int, input().split())
x = ~((a >> k) << k) & a
print(x | ((a >> (k + 1)) << k))

