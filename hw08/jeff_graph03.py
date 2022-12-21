import turtle as t

text = input('Enter text: ')
# text = 'aaidcdbbcdxi'
table = {}

for c in text:
    char_count = text.count(c)
    table[c] = char_count

def drawColumn(i):
    t.fd(len(table) * 30 / len(table) / 2)
    t.pu()
    t.rt(90)
    t.fd(10)
    t.write(list(table)[i])
    t.bk(10)
    t.lt(90)
    t.pd()
    t.lt(90)
    t.fd(list(table.values())[i] * 20)
    t.rt(90)
    t.fd(len(table) * 30 / len(table) / 3)
    t.rt(90)
    t.fd(list(table.values())[i] * 20)
    t.lt(90)
    
def drawArrow():
    t.begin_fill()
    t.lt(90)
    t.fd(3)
    t.rt(120)
    t.fd(6)
    t.rt(120)
    t.fd(6)
    t.rt(120)
    t.fd(3)
    t.end_fill()
    t.pu()
    t.home()
    t.pd()
            
t.pen(fillcolor='black')
t.seth(90)
t.fd(max(table.values()) * 20)
drawArrow()
t.fd(len(table) * 30)
drawArrow()

for i in range(len(table)):
    drawColumn(i)

t.ht()
t.done()


