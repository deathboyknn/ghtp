
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
    
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    
n = int(input())
arr = [0] * n
max_ = 0
for i in range(n):
    arr[i] = Point(input())
for i in range(n):
    for j in range(i + 1, n):
        max_ = max(max_, abs((arr[i] - arr[j]).dist()))
print(max_)

