
#-----------------jeff-----------------------
import turtle as t
table = {}
def histogram(lst):
    for c in lst:
        c_count = lst.count(c)
        table[c] = c_count
    # print(table)
    # print(table.values())
    return table

nt = histogram([1,2,3,4,2,3])

def drawColumn(i):
    # t.fd(15)
    t.pu()
    t.rt(90)
    t.fd(10)
    t.write(list(nt)[i])
    t.bk(10)
    t.lt(90)
    t.pd()
    t.lt(90)
    t.fd(list(nt.values())[i] * 20)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(list(nt.values())[i] * 20)
    t.lt(90)

print(nt.values())
t.pen(fillcolor='black')
t.seth(90)
t.fd(max(nt.values()) * 20)
# drawArrow()
t.home()
t.fd(len(nt) * 30)
t.home()
# drawArrow()
t.fd(15)
for i in range(len(nt)):
    drawColumn(i)


t.ht()
t.done() 

histogram([1,2,3,4,2,3])

for i in range(2):
    print("1")