class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def printInfo(self):
        print(f"Position: {self.x}, {self.y}")

class Circle(Point):
    def __init__(self, x=0, y=0, radius = 0.0):
        super().__init__(x,y)
        self.radius = float(radius)
    
    def area(self):
        # self.area = 3.14 * self.radius ** 2
        return  3.14 * self.radius ** 2
    def printInfo(self):
        print(f"Position: {super().x},{super().y}; Radius: {self.radius}; Area: {self.area()}")

    


p = Point(10,20)
p.printInfo()

c = Circle(10,20,5)
print(c.area())
p.printInfo()
