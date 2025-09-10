
class Fraction:
    def __init__(self, n=0, d=1):
        if type(n) == str:
            if ' ' in n:
                self.a, self.b = map(int, n.split(' '))
            elif '/' in n:
                self.a, self.b = map(int, n.split('/'))
            else:
                self.a, self.b = int(n), 1
        elif type(n) == Fraction:
            self.a, self.b = n.a, n.b
        elif type(n) == int:
            self.a, self.b = n, d
        else:
            self.a, self.b = 0, 1
        self.reduce()
            
    def reduce(self):
        a, b = abs(self.a), abs(self.b)
        c = gcd(a, b)
        if self.a * self.b < 0:
            a = -a
        self.a, self.b = a // c, b // c

    def __str__(self):
        return str(self.a) if self.b == 1 else f"{self.a}/{self.b}"
    
        
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


inp = open('input.txt', 'r', encoding="utf-8")
a = inp.readline().rstrip()
while a:
    print(Fraction(a))
    a = inp.readline().rstrip()
inp.close()

CH CI CJ CK CL CM CN CO CP

from sys import set_int_max_str_digits


set_int_max_str_digits(1000000000)


class Fraction:
    def __init__(self, n=0, d=1):
        if type(n) == str:
            if ' ' in n:
                self.a, self.b = map(int, n.split(' '))
            elif '/' in n:
                self.a, self.b = map(int, n.split('/'))
            else:
                self.a, self.b = int(n), 1
        elif type(n) == Fraction:
            self.a, self.b = n.a, n.b
        elif type(n) == int:
            self.a, self.b = n, d
        else:
            self.a, self.b = 0, 1
        self.reduce()
            
    def reduce(self):
        a, b = abs(self.a), abs(self.b)
        c = gcd(a, b)
        if self.a * self.b < 0:
            a = -a
        self.a, self.b = a // c, b // c

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return self.a == self.b * other
    
    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b != self.b * other.a
        return self.a != self.b * other
    
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return self.a > self.b * other
        
    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b >= self.b * other.a
        return self.a >= self.b * other
    
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a
        return self.a < self.b * other

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b <= self.b * other.a
        return self.a <= self.b * other
    
    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.a + other * self.b, self.b)
        elif isinstance(other, Fraction):
            return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
        return (self.a / self.b) + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self = self.__add__(other)
        return self
    
    def __sub__(self, other):
        if isinstance(other, int):
            return self.__add__(-other)
        elif type(other) == Fraction:
            return self.__add__(-other)
        return (self.a / self.b) - other
    
    def __rsub__(self, other):
        return (-self).__add__(other)

    def __isub__(self, other):
        self = self.__add__(-other)
        return self

    def __pos__(self):
        return self

    def __neg__(self):
        return Fraction(-self.a, self.b)

    def __abs__(self):
        return Fraction(-self.a, self.b) if self.a < 0 else self

    def __mul__(self, other):
        if isinstance(self, Fraction):
            if isinstance(other, Fraction):
                t = Fraction(self.a * other.a, other.b * self.b)
                t.reduce()
            elif isinstance(other, int):
                t = Fraction(self.a * other, self.b)
                t.reduce()
            else:
                t = self.a * other / self.b
        elif isinstance(self, int):
            if isinstance(other, Fraction):
                t = Fraction(self * other.a, other.b)
                t.reduce()
        else:
            t = other.a * self / other.b
        return t
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __imul__(self, other):
        self = self.__mul__(other)
        return self
    
    def __truediv__(self, other):
        if isinstance(self, Fraction):
            if type(other) == Fraction:
                t = Fraction(self.a * other.b, other.a * self.b)
                t.reduce()
            elif type(other) == int:
                t = Fraction(self.a, self.b * other)
                t.reduce()
            else:
                t = self.a / (other * self.b)
        return t
    
    def __rtruediv__(self, other):
        if isinstance(self, Fraction):
            if type(other) == Fraction:
                t = Fraction(self.a * other.b, other.a * self.b)
                t.reduce()
            elif type(other) == int:
                t = Fraction(self.b * other, self.a)
                t.reduce()
            else:
                t = (other * self.b) / self.a 
        return t
    
    def __itruediv__(self, other):
        self = self.__truediv__(other)
        return self
    
    def __pow__(self, other):
        if isinstance(other, int):
            if other < 0:
                return Fraction((self.b ** -other), (self.a ** -other))
            else:
                return Fraction((self.a ** other), (self.b ** other))
        elif isinstance(other, float):
            return (self.a / self.b) ** other
        else:
            return (self.a / self.b) ** (other.a / other.b)

    def __rpow__(self, other):
        if other:
            return other ** (self.a / self.b)
        return 0

    def __ipow__(self, other):
        self = self.__pow__(other)
        return self
    
    def __int__(self):
        return self.a // self.b

    def __float__(self):
        return self.a / self.b

    def __round__(self, d=0):
        return round(self.__float__(), d)

    def __str__(self):
        return str(self.a) if self.b == 1 else f"{self.a}/{self.b}"
    
        
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


