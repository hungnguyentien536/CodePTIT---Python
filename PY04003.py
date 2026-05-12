import math

class fraction:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def simplify(self):
        k = math.gcd(self.x,self.y)
        self.x = int(self.x / k)
        self.y = int(self.y / k)
    def output(self):
        print(self.x,"/",self.y,sep="")

a, b = [int(i) for i in input().split()]
x = fraction(a,b)
x.simplify()
x.output()


