from abc import ABC, abstractmethod
import turtle as t

class TwoDShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def draw(self):
        t.pu()
        t.setpos(self.x1, self.y1)
        t.pd()
        t.setpos(self.x2,self.y2)
    
class Rectangle(TwoDShape):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
    
    def draw(self):
        t.pu()
        t.setpos(self.x, self.y)
        t.pd()
        for i in range(2):
            t.fd(self.w)
            t.rt(90)
            t.fd(self.h)
            t.rt(90)

class Circle(TwoDShape):
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.r = radius
    
    def draw(self):
        t.pu()
        t.setpos(self.x,self.y)
        t.pd()
        t.circle(self.r)

class Square(TwoDShape):
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width
    
    def draw(self):
        t.pu()
        t.setpos(self.x,self.y)
        t.pd()
        for i in range(4):
            t.fd(self.width)
            t.rt(90)

shape = []

l1 =Line(0.5, 0.6, 4.8, 9.0)
shape.append(l1)
r1 = Rectangle(10, 30, 200, 150)
shape.append(r1)
c1 = Circle(0.5, 0.6, 300)
shape.append(c1)
r2 = Rectangle(-50, 80, 300, 400)
shape.append(r2)
c2 = Circle(-20, -30, 100)
shape.append(c2)
s1 = Square(0, 0, 100)
shape.append(s1)

for i in shape:
    i.draw()

t.done()