# DONT FORGRT WHEN ITS EQUAL

import turtle as t

x1, y1 = eval(input("Enter coordinate 1 (separate with comma): "))
width_1 = eval(input("Enter width 1: "))
height_1 = eval(input("Enter height 1: "))
x2, y2 = eval(input("Enter coordinate 2: "))
width_2 = eval(input("Enter width 2: "))
height_2 = eval(input("Enter height 2: "))

# top left 1
a1 = x1 - width_1 / 2
a2 = y1 + height_1 / 2

# top right 1
b1 = x1 + width_1 / 2
b2 = y1 + height_1 / 2

#bottom left 1
c1 = x1 + width_1 / 2
c2 = y1 - height_1 / 2

#bottom right 1
d1 = x1 - width_1 / 2
d2 = y1 - height_1 / 2

#---------------

# top left 2
e1 = x1 - width_2 / 2
e2 = y2 + height_2 / 2

# top right 2
f1 = x2 + width_2 / 2
f2 = y2 + height_2 / 2

#bottom left 2
g1 = x2 + width_2/ 2
g2 = y2 - height_2 / 2

#bottom right 2
h1 = x2 - width_2 / 2
h2 = y2 - height_2 / 2

#draw squares
t.pu()
t.setpos(d1, d2)
t.pd()

for i in range(2):
    t.fd(width_1)
    t.lt(90)
    t.fd(height_1)
    t.lt(90)

t.pu()
t.setpos(h1, h2)
t.pd()

for i in range(2):
    t.fd(width_2)
    t.lt(90)
    t.fd(height_2)
    t.lt(90)

#efgh is smaller
if (a1 < e1 < b1 and c2 < e2 < b2) and (a1 < f1 < b1 and c2 < f2 < b2) and \
    (a1 < h1 < b1 and c2 < h2 < b2) and (a1 < g1 < b1 and c2 < g2 < b2):
    print("rectangle 2 inside 1")
    t.write("rectangle 2 inside 1")
#abcd is smaller
elif (e1 < a1 < f1 and h2 < a2 < e2) and (e1 < b1 < f1 and h2 < b2 < e2) and \
    (e1 < c1 < f1 and h2 < c2 < e2) and (e1 < d1 < f1 and h2 < d2 < e2):
    print("rectangle 1 inside 2")
    t.write("rectangle 1 inside 2")
#overlap
elif (a1 <= e1 <= b1 or c2 <= e2 <= b2) or (a1 <= f1 <= b1 or c2 <= f2 <= b2) or \
    (a1 <= h1 <= b1 or c2 <= h2 <= b2) or (a1 <= g1 <= b1 or c2 <= g2 <= b2):
    print("overlap")
    t.write("overlap")
#outside
else:
    print("outside")
    t.write("outside")

t.ht()
t.done() 

