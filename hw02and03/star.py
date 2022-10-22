import turtle as t
t.speed(0)

def star(length):
    for i in range(5):
        t.fd(length)
        t.rt(144)
    t.ht()

num_input = int(input("Enter length: "))
star(num_input)

t.done()
