import turtle as t
t.pensize(2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        t.pu()
        t.setpos(self.x, self.y)
        t.pd()
        t.circle(1)

class Rectangle2D:
    def __init__(self):
        self.leftX = 0
        self.leftY = 0
        self.rightX = 0
        self.rightY = 0
        

    def getRectangle(self, points):
        
        lst_x = []
        lst_y = []
        for i in points:
            lst_x.append(i.x)
            lst_y.append(i.y)

        self.leftX  = min(lst_x)
        self.rightX = max(lst_x)

        self.leftY  = min(lst_y)
        self.rightY = max(lst_y)


        self.width = float(self.rightX -  self.leftX)
        self.height = float(self.rightY -  self.leftY)

        self.centerX = self.width / 2 + self.leftX
        self.centerY = self.height / 2 + self.leftY

        print(f"The bounding rectangle is centered at ({self.centerX}, {self.centerY}) with width {self.width} and height {self.height}")

    def draw_rec(self):
        t.pu()
        t.setpos(self.leftX, self.rightY)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)


points = input("Enter the points: ").split()
points = [eval(x) for x in points]

lst_points = []
for i in range(0,(len(points)),2):
    x = points[i]
    y = points[i+1]
    p = Point(x, y)
    lst_points.append(p)


for i in lst_points:
    i.draw()

rect = Rectangle2D()
rect.getRectangle(lst_points)
rect.draw_rec()

t.done()
