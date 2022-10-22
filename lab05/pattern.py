
# x = 1
# while x >= 1:
#     if x % 3 != 0:
#         print(f"{x}", end=",")
#     # else:
#     #     continue
#     x += 1
#     if x == 49:
#         break
# print("49")

x = 0
while x >= 0: 
    x += 1
    if x % 3 == 0:
        continue
    print(f"{x}", end ="")
    if x == 49:  
        break 
    print(",",end="")
# print("49")

# for i in range(50):
#     if i % 3 == 0:
#         pass
#     else:
#         print(i, end=", ")

# for i in range(50):
#     if i % 3 == 0:
#         continue
#     print(i)