import turtle as t

t.tracer(0)

txt = input("Enter some text: ")
data = []
for i in range(len(txt)):
    count = 0
    for j in range(len(txt)):
        if list(txt[i]) == list(txt[j]):
            count += 1
    data.append(count*20)

char = []
height = []
for i in range(len(txt)):
    if txt[i] not in char:
        char.append(txt[i])
        height.append(data[i])
        
for i in range(len(char)):
    t.fd(40)
    for j in range(2):
        t.fd(10)
        t.left(90)
        t.fd(height[i])
        t.left(90)

t.fd(50)
t.stamp()
t.home()
t.left(90)
t.fd(max(height) + 10)
t.stamp()
t.right(90)
t.penup()
t.setpos(40, -10)
for i in range(len(char)):
    t.write(char[i])
    t.fd(40.2)

t.hideturtle()
t.done()