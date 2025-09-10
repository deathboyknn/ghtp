
inp = open('input.txt', 'r')
s = inp.readline().rstrip()
x = 0
while s:
    x ^= int(s)
    s = inp.readline().rstrip()
print(x)
inp.close()

