


# sum=0
# x = 1
# for i in range(5):
    # Int = int(input("Enter an integer : "))
    # if Int >= 0 and x == 1:
    #     sum += Int
    #     x = 1
    #     print(f"Current Sum : {sum}")
    # elif Int >= 0 and x== 0:
    #     sum = 0
    #     sum += Int
    #     x = 1
    #     print(f"Current Sum : {sum}")
    # elif Int < 0 and x == 0:
    #     sum += Int
    #     x = 0
    #     print(f"Current Sum : {sum}")
    # elif Int < 0 and x == 1:
    #     sum = 0
    #     sum += Int
    #     x = 0
    #     print(f"Current Sum : {sum}")


# sum = 0
# sign = 1

# for i in range(5):
#     number = int(input('Enter an integer: '))
#     if number >= 0 and sign == 1:
#         sum = sum + number
#         print("Current sum: ", sum, "\n")
#         sign = 1
#     elif number >= 0 and sign == 0:
#         sum = 0
#         sum = sum + number
#         print("Current sum: ", sum, "\n")
#         sign = 1
#     elif number < 0 and sign == 1:
#         sum = 0
#         sum = sum + number
#         print("Current sum: ", sum, "\n")
#         sign = 0
#     elif number < 0 and sign == 0:
#         sum = sum + number
#         print("Current sum: ", sum, "\n")
#         sign = 0

sum = 0
sign = 1
for i in range(5):
    num = int(input("Enter num: "))
    if num >= 0 and sign == 1:
        sum += num
        sign = 1
    elif num >= 0 and sign == 0:
        sum = 0
        sum += 1
        sign = 0
    elif num < 0 and sign == 1:
        sum = 0
        sum += num
        sign = 1
    elif num < 0 and sign == 0:
        sum += num
        sign = 0
    print(f"sum is {sum}")

# sum = 0
# for i in range(5):
#     num = int(input(f"Enter number an integer: "))
#     if num >= 0:
#         if sum >= 0:
#             sum += num
#         elif sum <= 0:
#             sum = 0
#             sum += num
#     elif num < 0:
#         if sum < 0:
#             sum += num
#         elif sum >= 0:
#             sum = 0
#             sum += num
#     print(f"Current sum: {sum} \n")


# sum = 0
# for i in range(5):
#     num = int(input(f"Enter number an integer: "))
#     if num > 0:
#         if sum >= 0:
#             sum += num
#         elif sum <= 0:
#             sum = 0
#             sum += num
#     elif num < 0:
#         if sum < 0:
#             sum += num
#         elif sum >= 0:
#             sum = 0
#             sum += num
#     elif num == 0:
#         sum += num
#     print(f"Current sum: {sum} \n")

