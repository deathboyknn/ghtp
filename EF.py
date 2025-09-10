
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
task = dict()
s = (inp.readline()).rstrip()
while s:
    if s not in task:
        task[s] = 1
    else:
        task[s] += 1
    s = (inp.readline()).rstrip()
task = sorted(task.items(), key=lambda item: (-item[1], item[0]))
i, old, cnt = 0, 0, 0 
while i < len(task) and (cnt < 3 or task[i][1] == old):
    old = task[i][1]
    cnt += 1
    i += 1
for i, j in sorted(task[:i]):
    print(i + ' ' + str(j))
inp.close()
outp.close()

