import turtle as t
from math import *

class Rectangle():
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        self.area = self.width * self.height
        return self.area

    def getPerimeter(self):
        self.perimeter = (self.width * 2) + (self.height * 2)
        return self.perimeter

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def intersec(self, rec):

        self.rec_x = rec.x
        self.rec_y = rec.y
        self.rec_width = rec.width
        self.rec_height = rec.height

        # top left 1
        a1 = self.x 
        a2 = self.y 

        # top right 1
        b1 = self.x + self.width  
        b2 = self.y + self.height

        # #bottom left 1
        c1 = self.x + self.width
        c2 = self.y - self.height 

        # #bottom right 1
        d1 = self.x - self.width
        d2 = self.y - self.height 


        # top left 2
        e1 = self.rec_x 
        e2 = self.rec_y

        # top right 2
        f1 = self.rec_x + self.rec_width 
        f2 = self.rec_y + self.rec_height 

        #bottom left 2
        g1 = self.rec_x + self.rec_width 
        g2 = self.rec_y - self.rec_height

        #bottom right 2
        h1 = self.rec_x - self.rec_width 
        h2 = self.rec_y - self.rec_height 




        new_rec = Rectangle()
        if (a1 <= e1 <= b1 or c2 <= e2 <= b2) or (a1 <= f1 <= b1 or c2 <= f2 <= b2) or \
    (a1 <= h1 <= b1 or c2 <= h2 <= b2) or (a1 <= g1 <= b1 or c2 <= g2 <= b2):

            new_rec.x = e1
            new_rec.y = e2
            new_rec.width = b1-e1
            new_rec.height = e2 - h2

            print(new_rec.x)
            print(new_rec.y)
            print(new_rec.width)
            print(new_rec.height)

        else:
            return 0
         
        return new_rec

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)


# rec1 = Rectangle(0,0,150,300)
rec1 = Rectangle(90, 0, 100, 100)
# rec2 = Rectangle(40,-50,200,20)
rec2 = Rectangle(0, 50, 250, 100)
rec3 = rec1.intersec(rec2)

rec1.draw()
rec2.draw()
rec3.draw()

t.done()


class Circle():
    def __init__(self, x=0, y=0, radius=0):
       self.x = x
       self.y = y
       self.radius = radius

    def getPerimeter(self):
        return 2 * pi * self.radius

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.circle(self.radius)


t.done()

# # top left 2
# e1 = x1 - width_2 / 2
# e2 = y2 + height_2 / 2

# # top right 2
# f1 = x2 + width_2 / 2
# f2 = y2 + height_2 / 2

# #bottom left 2
# g1 = x2 + width_2/ 2
# g2 = y2 - height_2 / 2


# # top left 1
# a1 = x1 - width_1 / 2
# a2 = y1 + height_1 / 2

# # top right 1
# b1 = x1 + width_1 / 2
# b2 = y1 + height_1 / 2

# #bottom left 1
# c1 = x1 + width_1 / 2
# c2 = y1 - height_1 / 2

# (a1 <= e1 <= b1 or c2 <= e2 <= b2) or (a1 <= f1 <= b1 or c2 <= f2 <= b2) or \
#     (a1 <= h1 <= b1 or c2 <= h2 <= b2) or (a1 <= g1 <= b1 or c2 <= g2 <= b2):