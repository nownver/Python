import turtle as t
# t.speed(0)

def square(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

def chess(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0 and i % 2 == 0:
                t.fillcolor('black')
                t.begin_fill()
                square(100 / n)
                t.end_fill()
            elif j % 2 != 0 and i % 2 != 0:
                t.fillcolor('black')
                t.begin_fill()
                square(100 / n)
                t.end_fill()
            else:
                square(100 / n)

            t.fd(100 / n)
        t.pu()
        t.setpos(0, 0 - (100/n)*(i + 1))
        t.pd()

num_input = int(input("Enter N: "))
chess(num_input)

t.done()