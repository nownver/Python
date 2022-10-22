# import turtle as t
# import math as m

# def hex(n):
#     for i in range(6):
#         t.fd(n)
#         t.rt(60)

# def nested_hexa(s):
#     while s >= 10:
#         hex(s)
#         t.pu()
#         t.setheading(0)

#         t.rt(90)
#         t.fd(s * m.sqrt(3) / 2)
#         t.lt(90)
#         t.fd(s/4)
#         t.setheading(0)
#         t.lt(30)
#         t.pd()
#         s = 0.75 * s


# nested_hexa(80)
# # hex(80)
# t.done()

# import turtle as t

# def draw_sq(n):
#     for i in range(4):
#         t.fd(n)
#         t.rt(90)
        
# def spiral_sq(s):
#     while s > 5:
#         draw_sq(s)
#         t.pu()
#         t.fd(s/10)
#         t.rt(90)
#         t.fd(s/5)
#         t.lt(90)
#         t.pd()
#         t.lt(10)
#         s *= 0.75
        
# spiral_sq(150)  
        
# t.ht()
# t.done()



# import turtle as t

# def draw_hex(n):
#     for i in range(6):
#         t.fd(n)
#         t.rt(60)
        
# def spiral_hex(s):
#     while s >= 10:
#         draw_hex(s)
#         t.pu()
#         t.fd(s/2)
#         t.rt(90)
#         t.fd(s/12)
#         t.lt(90)
#         t.rt(30)
#         t.pd()
#         s *= 0.75
        
# spiral_hex(80)
# t.ht()
# t.done()



