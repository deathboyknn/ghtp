
a, k = map(int, input().split())
print((a >> k) ^ (((a >> k) >> 1) << 1))

