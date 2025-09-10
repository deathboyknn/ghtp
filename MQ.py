
res, nm = dict(), []
cntr = ""
for i in range(int(input())):
    nm = list(input().split(' '))
    cntr = nm[0]
    for j in nm[1:len(nm):1]:
        res[j] = cntr
for i in range(int(input())):
    print(res[input()])

