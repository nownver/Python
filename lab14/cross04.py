import turtle as t
t.tracer(0)

# t.speed(0)
# flag = 0
def cross(length, depth):
    # flag += 1
    # if flag == 1:
    #     depth += 1
    if depth > 0:
        for i in range(4):
            t.fd(length)
            # t.dot(5)
            cross(length / 2, depth - 1)
            t.bk(length)
            # t.dot(5)

            t.rt(90)
    else:
        t.dot(3)

cross(100, 5)

t.ht()
t.exitonclick()


# def cross(d, n):
#     for i in range(4):
    