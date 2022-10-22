import turtle as t
t.speed(0)
screen = t.Screen()
screen.bgcolor('#CD853F')

def square(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

def rectangle(length, height):
    for i in range(2):
         t.fd(length)
         t.rt(90)
         t.fd(height)
         t.rt(90)

def triangle(l1, l2):
    t.fd(l1)
    t.lt(180-55)
    t.fd(l2)
    t.lt(180-70)
    t.fd(l2)

def trapezoid(l1, l2):
    t.right(120)
    t.fd(l1)
    t.left(120)
    t.fd(l2)
    t.left(120)
    t.fd(l1)
    t.home()

def base_house(color):
    t.fillcolor(color)
    t.begin_fill()
    go_to_position(-80, -140)
    rectangle(390, 90)
    t.end_fill()

def roof(color):
    t.fillcolor(color)
    t.begin_fill()
    trapezoid(160, 390)
    t.end_fill()

def small_house(x, y):
    t.fillcolor('#4682B4')
    t.begin_fill()
    triangle(55, 50)
    t.end_fill()

    t.fillcolor('#66CDAA')
    t.begin_fill()
    t.lt(125)
    rectangle(55, 100)
    t.end_fill()

    t.pu()
    t.goto(-100, 50)
    t.pd()
    go_to_position(x, y)

    t.fillcolor('#DAA520')
    t.begin_fill()
    t.circle(3)
    t.end_fill()

def window_rectangle(length, height, color1, color2):
    t.fillcolor(color1)
    t.begin_fill()
    rectangle(length, height)
    t.end_fill()

    t.fillcolor(color2)
    t.begin_fill()
    for i in range(2):
        t.forward(length / 2)
        t.right(90)
        if i == 0:
            height = height
        else:
            height = height / 2
        t.forward(height)
        t.right(90)
    t.end_fill()

    t.forward(length)
    t.right(180)

def window_circle(radius):
    t.fillcolor('#ADD8E6')
    t.begin_fill()
    t.circle(radius)
    t.lt(90)
    t.fd(2 * radius)
    t.end_fill()

def go_to_position(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def house():
    roof('#BC8F8F')
    base_house('#FFE4B5')
    go_to_position(0, -130)
    small_house(10, -175)
    go_to_position(175, -130)
    small_house(185, -175)
    go_to_position(10, -20)
    window_rectangle(40, 30, '#20B2AA', '#5F9EA0')
    go_to_position(220, -50)
    window_rectangle(40, 30, '#20B2AA', '#5F9EA0')
    go_to_position(120, -100)
    window_circle(30)

house()
t.ht()
t.done()

# def house():
#     trapezoid(160, 390)
#     t.pu()
#     t.goto(0, -130)
#     t.pd()
#     small_house()
#     t.pu()
#     t.goto(175, -130)
#     t.pd()
#     small_house()
#     t.pu()
#     t.goto(-80, -140)
#     t.pd()
#     rectangle(390, 90)

# t.right(90)
# t.forward(400)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(height)
# t.right(90)
# t.forward(length)
# t.right(180)
# t.forward(length)
# t.right(90)


    # t.forward(200)
    # t.right(90)
    # t.forward(150)
    # t.right(90)

    # t.forward(200)
    # t.right(90)
    # t.forward(150)
    # t.right(90)

    # t.forward(100)
    # t.right(90)
    # t.forward(150)
    # t.right(90)

    # t.forward(100)
    # t.right(90)
    # t.forward(75)
    # t.right(90)
    # t.forward(200)
    # t.right(180)

# def window(s,g,size,y):
#     for i in range(1):
#         square(s)
#         t.pu()
#         t.setpos(size, y)
#         t.pd()
#         square(s - 2 * g)

# def draw_window(num1, num2):
#     window(num1, num2, num2, num2)
#     t.pu()
#     t.setpos(0, -num1)
#     t.pd()
#     window(num1, num2, num2, -num1 + num2)
#     t.pu()
#     t.setpos(num1, -num1)
#     t.pd()
#     window(num1, num2 ,num1 + num2, -num1 + num2)
#     t.pu()
#     t.setpos(num1, 0)
#     t.pd()
#     window(num1, num2,num1 + num2, num2)

# draw_window(30, 3)
# t.done()