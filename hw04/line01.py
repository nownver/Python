import turtle as t

x0, y0, x1, y1, x2, y2 = [float(x) for x in (input("Enter coordinate(split with space): ")).split()]

# y = m * x + c
m = (y1 - y0) / (x1 - x0)
c = y1 - m * x1
x_on_the_line = (y2 - c) / m

if y2 == m * x2 + c and min(x0, x1) <= x2 <= max(x0, x1) and min(y0, y1) <= y2 <= max(y0, y1):
    print("p2 is on the line between po qnd p1")
elif x2 < x_on_the_line:
    print("p2 is on the left side of po qnd p1")
elif x2 > x_on_the_line:
    print("p2 is on the right side of po qnd p1")
else:
    print("neither left nor right but not on the line")

#draw a line
t.pu()
t.goto(x0, y0)
t.write(f"{x0}, {y0}")
t.pd()
t.goto(x1, y1)
t.write(f"{x1}, {y1}")
t.pu()
t.goto(x2, y2)
t.dot()
t.write(f"{x2}, {y2}")
t.ht()

t.done()