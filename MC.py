
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*sorted(set(a) & set(b)))

