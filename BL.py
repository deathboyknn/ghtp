
a, k = map(int, input().split())
a = (a << 4) + (a << 1)
k >>= 4
print((a + k) & ~(((a + k) >> 5) << 5))

