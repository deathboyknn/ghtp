
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = map(int, x.split(' '))
        
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    
n = int(input())
max_crd, max_ = 0, 0
for i in range(n):
    a = Point(input())
    crnt = a.dist()
    if max_ <= crnt:
        max_, max_crd = crnt, a
print(max_crd)

