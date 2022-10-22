import calendar
import turtle

t = turtle.Turtle()
t.speed(10)

c = calendar.Calendar()
c.setfirstweekday(calendar.SUNDAY)
def square_write(text):
    t.forward(24)
    t.left(90)
    t.forward(16)
    t.left(90)
    t.forward(24)
    t.left(90)
    t.forward(16)
    t.left(90)
    if text != 0 : t.write(f' {text}')
    t.forward(24)

def write_month(n):
    data = c.monthdayscalendar(2022, n)
    t.forward(168)
    t.right(90)
    t.forward(16)
    t.backward(16)
    t.left(90)
    t.backward(168)
    t.right(90)
    t.forward(16)
    t.write(f" Month#{n}")
    t.forward(16)
    t.left(90)
    data =  [['Su','Mo','Tu','We','Th','Fr','Sa']] + data
    i = 0
    while i < len(data):
        k = data[i]
        l=0
        while l < len(k):
            j = k[l]
            square_write(j)
            l+=1
        t.penup()
        t.backward(168)
        t.right(90)
        t.forward(16)
        t.left(90)
        t.pendown()
        i+=1

x = -800
m=0
while m < 12:
    if m % 5 == 0:
        x += 200
        t.penup()
        t.setpos(x,300)
        t.pendown()
    
    turtle.tracer(0, 0)
    write_month(m+1)
    turtle.update()
    m+=1

turtle.done()


