import turtle as t

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
month_range = [31,28,31,30,31,30,31,31,30,31,30,31]
month_start = [6,2,2,5,0,3,5,1,4,6,2,4]

# month = 0
# for i in range(12):
#     for i in range(2):
#         t.fd(35*7)
#         t.rt(90)
#         t.fd(20)
#         t.rt(90)
#     t.rt(90)
#     t.fd(20)
#     t.lt(90)
#     t.fd(10)
#     month += 1
#     t.write(f'Month #{month}', font=('Courier New', 15))
#     t.bk(10)

def draw_box():
    for i in range(2):
        t.fd(35)
        t.rt(90)
        t.fd(20)
        t.rt(90)

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


t.done()

