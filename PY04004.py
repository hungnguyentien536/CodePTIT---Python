import math

class fraction:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def simplify(self):
        k = math.gcd(self.x,self.y)
        self.x = int(self.x / k)
        self.y = int(self.y / k)
    def add(self, other):
        a = self.x * other.y + other.x * self.y
        b = self.y * other.y
        self.x = a
        self.y = b
    def output(self):
        print(self.x,"/",self.y,sep="")

a, b, c, d = [int(i) for i in input().split()]
x = fraction(a,b)
y = fraction(c,d)
x.add(y)
x.simplify()
x.output()


