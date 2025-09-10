
a = input().split()
b = set()
for i in a:
    if i in b:
        print("YES")
    else:
        b.add(i)
        print("NO")

