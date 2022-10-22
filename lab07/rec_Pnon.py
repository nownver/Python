import turtle
t = turtle.Turtle()
class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def getArea(self):
        return self.w*self.h
    
    def getPerimeter(self):
        return 2*self.w + 2*self.h
    
    def move(self,newX, newY):
        self.x = newX
        self.y = newY

    def intersect(self,rec):
        x1 = set(range(self.x, self.x+self.w))
        x2 = set(range(rec.x, rec.x+rec.w))
        y1 = set(range(self.y-self.h, self.y))
        y2 = set(range(rec.y-rec.h, rec.y))
        xs = x1.intersection(x2)
        ys = y1.intersection(y2)
        if (len(ys) == 0 or len(xs) == 0):
            return None
        leftx = min(xs)
        rightx = max(xs)
        topy = max(ys)
        boty = min(ys)
        t.begin_fill()
        return Rectangle(leftx,topy,rightx-leftx,-1*(boty-topy))

    def draw(self):
        t.up()
        t.goto(self.x,self.y)
        t.setheading(0)
        t.down()
        t.fd(self.w)
        t.rt(90)
        t.fd(self.h)
        t.rt(90)
        t.fd(self.w)
        t.rt(90)
        t.fd(self.h)
        t.rt(90)
        t.end_fill()

# r2 = Rectangle(0, 40, 100, 100)
# r1 = Rectangle(20, 150, 180, 120)
r1 = Rectangle(1,1,-20,30)
r1.draw()
r2 = Rectangle(-3,4,40,50)
r2.draw()
r3 = r1.intersect(r2)
if(r3 == None):
    print("Not overlap")
else:
    t.color('red')
    r3.draw()
turtle.exitonclick()