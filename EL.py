
input1 = open('input.txt', 'r')
output = open('output.txt', 'w')
cur = [0] * 6
min1 = 40001
min2 = 40002
c = input1.readline().rstrip()
num = 0
minc = -1
count = 0
curc = -1
while len(c) > 0:
    num = int(c)
    count += 1
    if count <= 6:
        for i in range(5):
            cur[i] = cur[i + 1]
        cur[5] = num
    else:
        if cur[0] % 2 == 0:
            min2 = min(cur[0], min2)
        else:
            min1 = min(cur[0], min1)
        for i in range(5):
            cur[i] = cur[i + 1]
        cur[5] = num
        if cur[5] % 2 == 0:
            curc = min(min1, min2) * cur[5]
        elif min2 != 40002:
            curc = min2 * cur[5]
        if minc > curc or minc == -1:
            minc = curc
    c = input1.readline().rstrip()
print(minc)   
input1.close()
output.close()

