
inp = open('input.txt', 'r')
s = (inp.readline()).rstrip()
x, n = 0, 0
while s:
    x ^= int(s)
    n += 1
    s = (inp.readline()).rstrip()
for i in range(n):
    x ^= i
print(x)
inp.close()

