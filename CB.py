
class Point:
    def __init__(self, x=0, y=0):
        if isinstance(x, str):
            self.x, self.y = map(int, x.split(' '))
        else:
            self.x, self.y = x, y
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    
n = int(input())
cntr = Point(0, 0)
for i in range(n):
    cntr += Point(input())
print(cntr / n)

