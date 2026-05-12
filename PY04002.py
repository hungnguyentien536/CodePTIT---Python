class Rectangle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color.title()
    
    def check(self):
        if self.x > 0 and self.y > 0:
            return 1
        return 0
    
    def perimeter(self):
        return (int(self.x) + int(self.y)) * 2
    
    def area(self):
        return int(self.x * self.y)
    def output(self):
        if self.check() == 1:
            print('{} {} {}'.format(self.perimeter(), self.area(), self.color))
        else: print("INVALID")
    



arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])  
r.output()