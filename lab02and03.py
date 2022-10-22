#lab02

# #01
# w = 2
# x = 3
# y = 4
# z = 5
# answer = (x**3) + (y * z / 2) - w
# print(answer)

# #02
# import math as m
# radius = int(input("radious: "))
# length = int(input("length: "))
# area = m.pi * radius * length
# volume = area * length

# print(f"area is {area}")
# print(f"volume is {volume}")

# #03
# import turtle as t
# for i in range(6):
#     t.fd(90)
#     t.lt(60)
# t.pu()
# t.fd(20)
# t.rt(90)
# t.fd(20)

# t.pd()
# t.pensize(40)
# t.write("Size 90", font = ("Courier",14,"bold"))
# t.ht()
# t.done()

#04
# import turtle as t
# import math as m

# center_x = int(input("x: "))
# center_y = int(input("y: "))
# radius = int(input("radiuis: " ))
# area = m.pi * radius ** 2

# t.pu()
# t.setpos(center_x, center_y)
# t.write(area)
# t.setpos(center_x, center_y - radius)
# t.pd()
# t.circle(radius)
# t.done()      
#------------------------
#lab03

# #01
# import math as m
# pi = m.pi
# print(pi)

# # float_pi = float(pi)
# f = '{0:.5g}'.format(pi)
# float_pi = "{:.4f}".format(pi)
# print(float_pi)
# # print(f)

# from decimal import Decimal

# sci_pi = '%.2E' % Decimal(pi)
# print(sci_pi)


#02
# char = input("Please enter a character: ")
# unicode_char = ord(char)
# old = format(unicode_char, '04x')
# new = 'u' + old

# print(f"The Unicode of a \"{char}\" is {new}.")


# #03
# input_one = input("Please enter the first string: ")
# input_second = input("Please enter the second string: ")
# input_third = input("Please enter the third string: ")

# new = input_one + input_second + input_third

# print(new.upper())


