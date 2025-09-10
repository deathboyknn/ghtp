
class Point:
    def __init__(self, x=0, y=0):
        if isinstance(x, str):
            self.x, self.y = map(int, x.split(' '))
        else:
            self.x, self.y = x, y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, a):
        return Point(self.x * a, self.y * a)
    
    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)
    
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __lt__(self, other):
        return self.dist() < other.dist()
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    
n = int(input())
arr = [0] * n
max_ = 0
for i in range(n):
    arr[i] = Point(input())
for i in range(n):
    for j in range(i + 1, n):
        for f in range(j + 1, n):
            p = ((arr[i] - arr[j]).dist() + (arr[j] - arr[f]).dist() + (arr[f] - arr[i]).dist()) / 2
            max_ = max(max_, (p * (p - (arr[i] - arr[j]).dist()) * (p - (arr[j] - arr[f]).dist()) * (p - (arr[f] - arr[i]).dist())) ** 0.5)
print(max_)

