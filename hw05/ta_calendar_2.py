# ID: 63011335 
# Name: Tawan Lekngam
# HwNo: 05
# QNo: 02

import turtle as t
import calendar as c

t.tracer(0)
t.hideturtle()

size = 15
myCalender = c.TextCalendar(0)


def drawMonthData(txt):
    if txt != 0:
        t.write(f" {txt}", font=('Ariel', size//2, 'normal'))
    i = 0
    while i < 4:
        i += 1
        t.forward(size)
        t.left(90)


def drawMonth(m):
    monthData = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    monthData.extend(myCalender.itermonthdays(2022, m))
    t.pendown()
    t.write(f" Month#{m}", font=('Ariel', size//2, 'normal'))
    i = 0
    while i < 2:
        i += 1
        t.forward(size * 7)
        t.left(90)
        t.forward(size)
        t.left(90)
    t.goto(t.pos() + (0, -size))
    i = 0
    while i < len(monthData):
        t.pendown()
        drawMonthData(monthData[i])
        t.forward(size)
        i += 1
        if i % 7 == 0:
            t.penup()
            t.goto(t.pos() + (-size * 7, -size))

    t.goto(t.pos() + (0, -size))
    print(monthData)



def drawCalendar():
    x, y = (-400, 300)
    t.penup()
    t.goto(x, y)
    i = 0
    while i < 12:
        if i % 3 == 0 and i != 0:
            # t.goto(t.pos()[0] + size * 8, y)
            t.setx(t.xcor() + size * 8)
            t.sety(300)
        i += 1
        drawMonth(i)
        t.goto(t.pos() + (0, -size))

drawMonth(1)
drawCalendar()
t.done()












