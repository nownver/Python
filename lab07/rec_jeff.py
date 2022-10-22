import turtle as t
t.pen(speed=10)

class Rectangle:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def draw(self):
        t.pu()
        t.setpos(self.x, self.y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)
        
    def intersect(self, rec):
        # Rectangle 1
        x1 = self.x #top left
        y1 = self.y #top left
        x2 = self.x + self.width #bottom right
        y2 = self.y - self.height #bottom right
        # Rectangle 2
        x3 = rec.x #top left
        y3 = rec.y #top left
        x4 = rec.x + rec.width #bottom right
        y4 = rec.y - rec.height #bottom right
        
        # topleft verlap
        if ((min(x1,x2) < x3 < max(x1,x2)) and (min(y1,y2) < y3 < max(y1,y2))):
            x5 = x3
            y5 = y3
            new_rec = Rectangle(x5, y5, abs(x5-x2), abs(y5-y2))
            return new_rec
        
        # bottomright overlap
        elif ((min(x1,x2) < x4 < max(x1,x2)) and (min(y1,y2) < y4 < max(y1,y2))): 
            x5 = x1
            y5 = y1
            new_rec = Rectangle(x5, y5, abs(x5-x4), abs(y5-y4))
            return new_rec
        
        # topright overlap
        elif ((min(x1,x2) < x4 < max(x1,x2)) and (min(y1,y2) < y3 < max(y1,y2))):
            x5 = x1
            y5 = y3
            new_rec = Rectangle(x5, y5, abs(x5-x4), abs(y5-y2))
            return new_rec
        
        # bottomleft overlap
        elif ((min(x1,x2) < x3 < max(x1,x2)) and (min(y1,y2) < y4 < max(y1,y2))): 
            x5 = x3
            y5 = y1
            new_rec = Rectangle(x5, y5, abs(x5-x2), abs(y5-y4))
            return new_rec
        
        # INSIDE
        elif ((min(x1,x2) <= x3 <= max(x1,x2)) and (min(y1,y2) <= y3 <= max(y1,y2))) and ((min(x1,x2) <= x4 <= max(x1,x2)) and (min(y1,y2) <= y4 <= max(y1,y2))) and \
            ((min(x1,x2) <= x4 <= max(x1,x2)) and (min(y1,y2) <= y3 <= max(y1,y2))) and ((min(x1,x2) <= x3 <= max(x1,x2)) and (min(y1,y2) <= y4 <= max(y1,y2))): 
            x5 = x3
            y5 = y3
            new_rec = Rectangle(x5, y5, rec.width, rec.height)
            return new_rec
        
        else:
            print("NO INTERSECT")
            return Rectangle(0,0,0,0)

rec1 = Rectangle(0, 0, 100, 100)
rec2 = Rectangle(-8, -10, 120, -60)

rec3 = rec1.intersect(rec2)

rec1.draw()
t.write('a')
rec2.draw()
t.write('b')

t.fillcolor('red')
t.begin_fill()
rec3.draw()
t.end_fill()

print(rec3)

t.done()