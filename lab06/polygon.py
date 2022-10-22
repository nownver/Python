import turtle as t

def draw_polygon(x ,y , size=100, type=4):
    t.pu()
    t.goto(x, y)
    t.pd()
    for i in range(type):
        t.fd(size)
        t.rt(360 / type)

draw_polygon(0,0,100,7)
t.done()



