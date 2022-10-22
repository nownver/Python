# # don't forget to find min of (x,y) in order to write below sth

import math as m
import turtle as t
t.speed()

def draw_triangle(x1, y1, x2, y2, x3, y3):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)

def find_length(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y2 - y1
    dd = dx * dx + dy * dy
    return m.sqrt(dd)

def calculate_area(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    area = m.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    return area


x1, y1, x2, y2, x3, y3 = [int(x) for x in input("Enter three point (split with ,): ").split(",")]

length1 = find_length(x1, y1, x2, y2)
length2 = find_length(x1, y1, x3, y3)
length3 = find_length(x2, y2, x3, y3)

min_x = min(x1, x2, x3)
min_y = min(y1, y2, y3)
draw_triangle(x1, y1, x2, y2, x3, y3)
area_of_triangle = calculate_area(length1, length2, length3)
t.pu()
t.setpos(min_x, min_y - 10)
t.pd()
t.write(area_of_triangle)

t.done()


# def calculate_area(x1, y1, x2, y2, x3, y3):
#     area = (1 / 2 ) * ((x1 *(y2 - y3)) + (x2 *(y3 - y1)) + (x3 *(y1 - y2)))
#     return area

# 1.5, -3.4, 4.6, 5, 9.5, -3.4
# 15, -34, 46, 50, 95, -34

