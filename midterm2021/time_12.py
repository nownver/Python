# import turtle as t
# t.pendown()
# def square(size):
#     for i in range(4):
#         t.fd(size)
#         t.lt(90)

# def spiral_sq(s):
#     while s**2 >5:
#         t.penup()
#         square(s)
#         t.degree(-10)
#         s = s*75/100


# size = int(input("square size:"))
# s = size
# spiral_sq(s)
# t.done()

import turtle as t

print("Hello, welcome to Turtle World!")
t.setup()
command = 0

while command != 'quit':
    command = (input("turtle|> "))
    if command == 'quit':
        t.bye()
    elif command == 'fd':
        unit = int(input('Please input its argument: '))
        t.fd(unit)
    elif command == 'bk':
        unit = int(input('Please input its argument: '))
        t.bk(unit)
    elif command == 'lt':
        unit = int(input('Please input its argument: '))
        t.lt(unit)
    elif command == 'rt':
        unit = int(input('Please input its argument: '))
        t.rt(unit)
    elif command == 'pu':
        t.pu()
    elif command == 'pd':
        t.pd()
    elif command == 'reset':
        t.reset()
    else:
        print("Wrong command, please try again.")
