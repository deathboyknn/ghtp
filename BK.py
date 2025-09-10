
a, k = map(int, input().split())
print(((1 << k) ^ (1 << a)) | (((1 << a) << 1) & ((1 << k) << 1)))

