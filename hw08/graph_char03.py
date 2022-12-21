import turtle as t

percent = {}
input_string = input("Enter some  text: ")

def draw(c):
    t.fd(10)
    t.pu()
    t.rt(90)
    t.fd(20)
    t.write(c)
    t.bk(20)
    t.lt(90)
    t.pd()

for c in input_string:
    char_count = input_string.count(c)
    percent[c] = (char_count/len(input_string))*100

for i in percent:
    colum = i
    row = percent[i]
    draw(i)



#----------------
# from turtle import *
# text = input('Enter some text: ')
# lenght = len(text)

# t = Turtle()
# t1 = Turtle()
# t.pu()
# t1.pu()
# getStr = ''
# count = 0
# max = 0
# size = 20
# t.speed(0)
# t1.speed(0)
# t.bk(lenght * 8)
# t1.bk(lenght * 8)
# t.pd()
# t1.pd()

# for char1 in text:
#     count = 0
#     for char2 in text:
#         if char2 == char1:
#             count += 1
#     if count > max:
#         max = count
#     if count > 0:
#         t.fd(10)
#         t.pu()
#         t.rt(90)
#         t.fd(20)
#         t.write(char1)
#         t.bk(20)
#         t.lt(90)
#         t.pd()
#         for i in range(2):
#             t.fd(10)
#             t.lt(90)
#             t.fd(size * count)
#             t.lt(90)
#         t.fd(15)
#         getStr += char1
#     text = text.replace(char1, '')
# t1.lt(90)
# t1.fd((max * size) + 20)
# t.fd(20)
# Turtle.done()