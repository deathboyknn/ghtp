
a, k = map(int, input().split())
print((a | 1 << k) & ~(((a >> k) ^ (((a >> k) >> 1) << 1)) << k))

