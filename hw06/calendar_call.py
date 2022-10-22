import turtle as t
import calendar as c
t.speed(0)
myCalender = c.TextCalendar(0)

def square(s, w):
    for i in range(4):
        t.fd(s)
        t.lt(90)
    if w != 0:
        t.pu()
        t.fd(s/3)
        t.lt(90)
        t.fd(s/3)
        t.rt(90)
        t.write(f" {w}", font=('Ariel', 10, 'normal'),align="left")
        t.lt(90)
        t.bk(s/3)
        t.rt(90)
        t.bk(s/3)
        t.pd()


month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def calendar_of_2022(m):
    s = 30
    date = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    date.extend(myCalender.itermonthdays(2022, m))

    t.pu()
    t.lt(90)
    t.fd(s/3)
    t.rt(90)
    t.fd(s*7/3)
    t.write(f"{month[m-1]} 2022", font=('Ariel', 10, 'normal'))
    t.bk(s*7/3)
    t.lt(90)
    t.bk(s/3)
    t.rt(90)
    t.pd()

    for i in range(2):
        t.fd(s * 7)
        t.lt(90)
        t.fd(s)
        t.lt(90)
    t.setpos(0, t.pos()[1] - s)

    for i in range(1, len(date)+1):
        t.pd()
        square(s, date[i-1])
        t.fd(s)
        if i % 7 == 0 and i != 0:
            t.pu()
            t.setpos(t.pos()[0] - s * 7, t.pos()[1] - s)
       
        
my_month = 12
calendar_of_2022(my_month)
t.done()


