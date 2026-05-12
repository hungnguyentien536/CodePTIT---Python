from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt((pow(self.x - other.x, 2) + pow(self.y - other.y, 2)))


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def cnt(self):
        d1 = self.p1.distance(self.p2)
        d2 = self.p2.distance(self.p3)
        d3 = self.p3.distance(self.p1)
        if max(d1, d2, d3) * 2 >= d1 + d2 + d3:
            print("INVALID")
        else:
            area = sqrt((d1 + d2 + d3) * (d1 + d2 - d3) * (-d1 + d2 + d3) * (d1 - d2 + d3)) / 4
            print("{:.2f}".format(area)) 
        

n = []
t = int(input())
for x in range(t):
    n += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(n[i], n[i+1]), Point(n[i+2], n[i+3]), Point(n[i+4], n[i+5]))
    triagle.cnt()
    i += 6