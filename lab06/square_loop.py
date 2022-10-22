import turtle as t
t.speed(3)
def square(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

def nested_square():
    for i in range(4):
        for j in range(4):
            square(50 * (j + 1))

        t.seth(90 * (i + 1))


nested_square()
t.done() 

