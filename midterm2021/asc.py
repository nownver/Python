
# while True:
#     n = input()

#     if ord(n) == 0x2E:
#         print("Good bye")
#         break
#     elif 0x30 <= ord(n) <= 0x39:
#         print("num")
#         continue
#     elif 0x41 <= ord(n) <= 0x5A:
#         print("cap")
#         continue
#     elif 0x61 <= ord(n) <= 0x7A:
#         print("small")
#         continue
#     else:
#         print("special")
#         continue

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

# baht = int(input("Input amount of money in integer : "))

# noc = {1:[1000,"notes"],2:[500,"notes"],3:[100,"notes"],4:[50,"notes"],5:[20,"notes"],6:[10,"coins"],7:[5,"coins"],8:[2,"coins"],9:[1,"coins"]}

# def bankncoin(type):
#     bnc = sum//type
#     return bnc
    
# sum = baht
# for i in range(1,10):
#     print(f"{noc[i][0]}-Baht {noc[i][1]} : {bankncoin(noc[i][0])}")
#     sum -= (sum//noc[i][0])*noc[i][0]

# char =input()
# if char == "    ":
#     print(ord(char))
#     print("s")