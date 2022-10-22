import turtle as t

t.pen(speed=0)
t.screensize(2000, 4000)

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
month_range = [31,28,31,30,31,30,31,31,30,31,30,31]
month_start = [6,2,2,5,0,3,5,1,4,6,2,4]

def draw_box():
    for i in range(2):
        t.fd(35)
        t.rt(90)
        t.fd(20)
        t.rt(90)

def draw_calendar(month):
    for i in range(2):
        t.fd(35*7)
        t.rt(90)
        t.fd(20)
        t.rt(90)
    t.rt(90)
    t.fd(20)
    t.lt(90)
    t.fd(10)
    t.write(f'Month #{month}', font=('Courier New', 15))
    t.bk(10)
    
    for x in range(7):
        draw_box()
        t.pu()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.fd(5)
        t.write(day[x], font=('Courier New', 15))
        t.bk(5)
        t.lt(90)
        t.fd(20)
        t.rt(90)
        t.pd()
        t.fd(35)
    t.bk(35*7)
    t.rt(90)
    t.fd(20)
    t.lt(90)
    
    date = (0 - month_start[month - 1]) + 1
    while date <= month_range[month - 1]:
        for x in range(7):
            draw_box()
            if 1 <= date <= month_range[month - 1]:
                t.pu()
                t.rt(90)
                t.fd(20)
                t.lt(90)
                t.fd(5)
                t.write(date)
                t.bk(5)
                t.lt(90)
                t.fd(20)
                t.rt(90)
                t.pd()
            t.fd(35)
            date += 1
        t.bk(35*7)
        t.rt(90)
        t.fd(20)
        t.lt(90)
           
def select_month(a,b):
    for i in range(a,b):
        draw_calendar(i)
        t.pu()
        t.rt(90)
        t.fd(40)
        t.lt(90)
        t.pd()

for i in range(4):
    t.pu()
    t.setpos(-545 + (265*i),200)
    t.pd()
    if i == 0:
        select_month(1,4)
    if i == 1:
        select_month(4,7)
    if i == 2:
        select_month(7,10)
    if i == 3:
        select_month(10,13)
        
t.ht()
t.done()