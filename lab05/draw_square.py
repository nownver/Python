import turtle as t
t.speed(0)

def each_square(round):
    for i in range(4):
        t.fd(100 / round)
        t.lt(90)

def big_square (n):
    for i in range(n):
        for j in range(n):
            each_square(n)
            t.fd(100 / n)
        t.pu()
        t.setpos(0, 0 - (100 / n) * (i + 1)) 
        t.pd()

num_input = int(input("Enter N: "))
big_square(num_input)    
t.done()