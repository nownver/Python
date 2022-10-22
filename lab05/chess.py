import turtle as t
t.speed(0)

def each_square(round, fill_color):
    if fill_color:
        t.fillcolor('black')
        t.begin_fill()
        for i in range(4):
            t.fd(100 / round)
            t.lt(90)
        t.end_fill()
    else:
        for i in range(4):
            t.fd(100 / round)
            t.lt(90)

def chessboard(round, filled):
    for j in range(round):
        for i in range(round):
            filled = j % 2 == 0
            if i % 2 != 0:
                filled = not filled
            each_square(round, filled)
            t.fd(100 / round)
        t.pu()
        t.setpos(0, 0 - (100 / round) * (j+1))
        t.pd()

input_num = int(input("input number: "))
chessboard(input_num, True)
t.done()
