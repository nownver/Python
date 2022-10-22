
# for i in range(49, 0, -1):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(f"{i}", end = "")
#     if i == 1:
#         # print(".")
#         break
#     print(", ",end = "")



# last = int(input())
# n = 0
# while n >= 0:
#     n += 1
#     if n % 3 == 0 or n % 5 == 0:
#         continue
#     print(f"{n}", end ="")
#     if last % 3 == 0 or last % 5 == 0:
#         last = last - 1
#     if n == last:
#         print(".")
#         break
#     print(",",end="")


# last = int(input('Last integer: '))
# num = 0

# while num < last:
#     num += 1
#     if (num % 3 == 0) or (num % 5 == 0):
#         continue
#     # if (num % 3 == 0) or (num % 5 == 0) and (num == last):
#     #     print('.')
#     elif num == last:
#         print(num, end='. ')
#     else:
#         print(num, end=', ')
