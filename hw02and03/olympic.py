import turtle as t
t.speed(1)
t.pensize(5)

def draw_circle(radius, color):
    t.color(color)
    t.circle(radius)

def olympic(x, y, radius):
    for i in range(3):
        if i == 0:  
            draw_circle(radius, 'blue')
        if i == 1:  
            draw_circle(radius, 'black')  
        if i == 2:
            draw_circle(radius, 'red')
        x += 2 * radius + radius / 4
        y = 0
        t.pu()
        t.setpos(x,y)
        t.pd()

    t.pu()
    x = radius + 0.125 * radius
    y = -2.25 * radius + radius
    t.setpos(x, y)
    t.pd()

    for i in range(2):
        if i == 0:
            draw_circle(radius, 'yellow')
        else:
            draw_circle(radius, 'green')
        x += 2 * radius + radius / 4
        t.pu()
        t.setpos(x, y)
        t.pd()
    t.ht()

radius_input = int(input("Enter radius: "))
olympic(0, 0, radius_input)
t.done() 


#olympic
# import turtle as t

# def draw_circle(radius):
#     t.circle(radius)

# def draw_olympic(radius):
#     gap = (radius * 2) + (radius / 4)

#     # set starting point
#     t.penup()
#     t.setpos(-(radius * 2), t.pos()[1])
#     t.pendown()

#     for i in range(5):
#         current_positionX = t.pos()[0]
#         current_positionY = t.pos()[1]
#         if i % 2 == 0:
#             print("draw top circle")
#             draw_circle(radius)
#             t.pu()
#             t.setpos(current_positionX + gap / 2, current_positionY - radius * 1.2)
#             t.pd()
#         else:
#             print("draw bottom circle")
#             draw_circle(radius)
#             t.pu()
#             t.setpos(current_positionX + gap / 2, current_positionY + radius * 1.2)
#             t.pd()

# draw_olympic(50)

# t.done()