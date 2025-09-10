
a, k = map(int, input().split())
print((~((a >> k) << k)) & a)

