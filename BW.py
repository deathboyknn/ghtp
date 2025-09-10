
x = input()
a, b = 1, 0
for i in range(len(x)):
    a += ord(x[i])
    a %= 65521
    b += a
    b %= 65521
print(a + (b << 16))

