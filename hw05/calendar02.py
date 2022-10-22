import turtle as t
# import calendar
# cal= calendar.Calendar()
# print(cal.monthdayscalendar(2022, 1))

t.speed(0)
t.screensize(1000, 5000)

def set_pos(x, y) :
    t.pu()
    t.setpos(x, y)
    t.pd()

day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa", ""]

date_start = [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
date_stop = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calendar(w, h, m, y):
    set_pos(0, -y)
    for i in range(9):
        t.fd(w)
        t.pu()
        t.setpos(0, 0 - (h / 8) * (i + 1) -y)
        if i == 0:
            t.write(f"Month#{m}", font = ['Corior new', 16, 'normal'])
        # t.setpos(0, 0 - (h / 8) * (i + 1))                         
        t.pd()

    set_pos(0, 0 -y)
    t.rt(90)
    t.fd(h)

    set_pos(w, 0 -y)
    t.fd(h)
    set_pos(0, 0 - h / 8 - y)

    for i in range(8):
        t.fd(h - h / 7)
        t.pu()
        t.setpos(0 + (w / 7) * (i + 1), 0 - h / 7 - y)
        for j in range(7):
            t.setpos(0 + (w / 7) * (i + 1) - 2 * (w/7)/3, 0 - h / 7 - 2 * (h/7)/3 -y)
            t.write(day[i],font = ['Corior new', 16, 'normal'])
        t.setpos(0 + (w / 7) * (i + 1), 0 - h / 7 - y)
        t.pd()

# calendar(300, 180)

x = 1
set_x = 0
set_y = 0

while x >= 0:
    calendar(300, 180, x, set_y)
    set_pos(0, 0 - (300 + 10) * x)
    t.lt(90)
    x += 1
    set_y += 190
    if x == 13:
        break

t.done()

