# def swap(a, b) :
#     a, b = b, a
#     return a, b

# def isEqual(a, b) :
#     return True if a==b else False

# print(swap(1,2))
# print(isEqual(3,6))
# print(isEqual(3,3))

# import turtle
# from turtle import *
# from datetime import datetime

# mode("logo")
# def jump(distanz, winkel=0):
#     penup()
#     right(winkel)
#     forward(distanz)
#     left(winkel)
#     pendown()

sum = 0

def num_negative():
    global sum
    if sum > 0:
        sum =0
        sum += num
    else:
        sum += num

def num_positive():
    global sum
    if sum < 0:
        sum =0
        sum += num
    else:
        sum += num

def zero():
    global sum
    if sum < 0:
        sum += num
    else:
        sum += num

n = 0
sum = 0


while (n < 30):
    num = int(input("Please enter your num:"))
    n = n + 1
    if num == 0:
        zero()
    elif num > 0:
        num_positive()
    else:
        num_negative()
    print(f"Current sum is: {sum}")

