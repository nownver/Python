# overlap - NOT handle negative width/height
import turtle as t

class Rectangle():
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width * 2) +  (self.height * 2)

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)


    def move(self, Newx, Newy):
        self.x = Newx
        self.y = Newy

    def intersect(self, other):
        if self.width > 0 and self.height > 0 and other.width > 0 and other.height > 0:
            range_x_self = set(range(self.x, self.x + self.width))
            range_x_other = set(range(other.x, other.x + other.width))

            range_y_self = set(range(self.y - self.height, self.y))
            range_y_other = set(range(other.y - other.height, other.y))

            intersect_x = range_x_self.intersection(range_x_other)
            intersect_y = range_y_self.intersection(range_y_other)

            if len(intersect_x) != 0 and len(intersect_y) != 0:
                w = abs(max(intersect_x) - min(intersect_x))
                h = abs(max(intersect_y) - min(intersect_y))
                return Rectangle(min(intersect_x), max(intersect_y), w, h) 
            
            else:
                return "not intersect"

# if __name__ == '__main__':
a = Rectangle(1,1,-20,30)
b = Rectangle(-3,4,40,50)
a.draw()
b.draw()

c = a.intersect(b)
if type(c) != str:
    t.color('red')
    c.draw()
else:
    print(c)

t.done()